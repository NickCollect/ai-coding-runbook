---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja
fetched_at: 2026-09-14T05:42:05.748790+00:00
title: "\u30b9\u30c8\u30ea\u30fc\u30df\u30f3\u30b0\u306b\u3088\u308b\u30ed\u30dc\u30c3\u30c8\u5de5\u5b66 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)

フィードバックを送信

# ストリーミングによるロボット工学

`gemini-robotics-er-2-streaming-preview` モデル エンドポイントは、[Live
API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja) と統合された専用の
ストリーミング エンドポイントを公開し、アプリケーションとロボット間のリアルタイムの
双方向通信を可能にします。これにより、迅速なフィードバック ループと環境への反応型レスポンスを必要とするエージェントに適しています。

[Google AI Studio で試す](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=ja)
[GitHub からサンプルアプリのクローンを作成する](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## ユースケース

- **マルチロボット連携**: 共有セッションを通じてタスクの状態を通信し、
  サブタスクを委任する複数のロボット。
- **継続的なモニタリング**: シーンを観察し、コンテナが満杯になるなど、特定のイベントが発生したときにアクションをトリガーするロボット。
- **倉庫と物流**: 品物を
  目視で確認し、梱包の進捗状況を追跡し、エラーから復旧するピッキングと梱包のエージェント。

## 技術仕様

次の表に、Live API の技術仕様の概要を示します。

| カテゴリ | 詳細 |
| --- | --- |
| 入力モダリティ | 音声（RAW 16 ビット PCM 音声、16kHz、リトル エンディアン）、画像（JPEG <= 1FPS）、テキスト |
| 出力モダリティ | テキスト |
| プロトコル | ステートフル WebSocket 接続（WSS） |

## エージェントの設定を構築する

Live API で構築されたすべてのロボット工学エージェントは、次の 3 つのステップに従います。

1. **ロボットの機能をツールとして宣言する。**ロボットが実行できる各アクション（移動、把握、発話）は、名前、説明、パラメータ スキーマを持つ関数宣言になります。物理アクションでは、
   `"behavior": "BLOCKING"` を使用する必要があります。これにより、ロボットが完了するまでモデルが待機してから
   次のステップを選択します。
2. **マルチモーダル入力を永続的なセッションにストリーミングする。**`live.connect` セッションを開き、タスクの実行中は開いたままにします。ロボットのセンサーから到着した動画フレーム、音声、テキストを送信します。
3. **受信ループでツール呼び出しを処理する。**モデルがアクションを選択するたびに、`tool_call` メッセージが送信されます。受信ループは、ロボット SDK に対して関数を実行し、`tool_response` を返します。セッションは開いたままになり、モデルは結果に基づいて次のアクションを選択します。

以降のセクションでは、これらのステップを 3 つの一般的なパターン（ベースライン エージェント ループ、ハートビートを使用したプロアクティブなシーン モニタリング、ツールとしての TTS を介した音声のルーティング）に適用する方法について説明します。

## 関数呼び出しでロボットをオーケストレートする

次の例は、3 つのステップすべてが 1 つの Python スクリプトにまとめられています。

ステップ 1（ツールの定義）では、ロボットの機能が関数宣言として宣言されます。`navigate` 関数は `"behavior": "BLOCKING"` を使用するため、
モデルはロボットがウェイポイントに到達するまで待機してから別のツールを呼び出します。
同じリストに関数宣言を追加して、ロボットの追加機能を公開します。

ステップ 2（入力ヘルパー）では、さまざまなモダリティ入力をセッションにストリーミングする 3 つの関数を示します。`send_text` はコマンド用、`send_image` はカメラフレーム用（オプションのテキスト プロンプト付き）、`send_audio` はマイクからの RAW PCM 音声用です。

ステップ 3（受信ループ）は同時に実行され、`server_content` メッセージ（モデルのテキスト出力）と `tool_call` メッセージ（ロボット アクションをリクエストするモデル）の 2 種類のメッセージを処理します。ツール呼び出しが到着すると、ループは `execute_tool`（実際のロボット SDK に置き換えるスタブ）を呼び出し、`tool_response` を返して、モデルが次のアクションを選択できるようにします。

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

受信ループは、各ツール レスポンスの後もアクティブなままです。モデルは、アクション シーケンス全体を事前にエンコードすることなく、長期的な計画を構築して修正します。

## プロアクティブな空間的および時間的推論

Live API は動画をストリーミングしますが、動画フレームだけでは新しい推論ターンはトリガーされません。モデル レスポンスをトリガーするには、動画フレームにテキストまたは音声プロンプトを添える必要があります。詳細については、
[Live API の機能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ja)をご覧ください。

プロアクティブな推論を有効にするには、**ハートビート** を実装します。
最新のカメラフレームを定期的に送信し、その後に短いテキスト プロンプトを送信して、モデルに
シーンを検査して明示的な決定を下させます。動画入力は 1 秒あたり 1 フレームにレート制限されます。

前のセクションの受信ループとともに、このコルーチンを追加します。同じセッションで別の `asyncio` タスクとして実行されます。

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

ロボット アクション中にハートビートを一時停止する必要はありません。**暗黙的な成功検出機能**として使用すると、実行中のアクションをモデルが継続的に観察し（把握が安全かどうか、注ぎがターゲット上にあるかどうか、オブジェクトが正しく配置されているかどうかを追跡）、結果が明確になった瞬間に反応できます。

ハートビート メッセージはユーザーターンとして機能し、進行中のモデル生成を中断します。
Live API がこの動作を処理する方法については、
[中断に関する Live API ガイド](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ja#interruptions)
をご覧ください。

## 外部 TTS によるオーディオ出力

Gemini Robotics ER 2 はテキストを返します。アプリケーションは、挿入されたコールバックを介して、完了したレスポンス
を別の TTS プロバイダ（
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)など）にルーティングします。
これにより、音声のレイテンシ、音声の選択、中断動作を制御し、エージェント ロジックを変更せずに TTS バックエンドを切り替えることができます。

TTS をツールとして宣言して、モデルが「何か言う」を「アームを動かす」と同じように扱うこともできます。 最初のセクションの `tools` リストに次の関数宣言を追加します。

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

TTS を関数宣言でラップすることで、モデルは他のロボット アクションと同じツール呼び出しパスで音声を処理します。アプリケーションは、挿入されたコールバックで呼び出しを完了します。

## GitHub の例

Spot ロボットのスナック取得デモや Tinybot
パン / チルト Hello World など、実際の動作例については、
[ロボット工学 Live API の例をご覧ください](https://github.com/google-gemini/robotics-samples/tree/main/live-api)。

## 次のステップ

- [動画理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - 瞬間検出と進捗状況の分類。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - ストリーミングなしの長期的なタスク。
- [Live API の概要](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja) - Live API の完全なドキュメント。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-08 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-08 UTC。"],[],[]]
