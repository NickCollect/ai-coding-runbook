---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja
fetched_at: 2026-10-26T05:50:21.780467+00:00
title: "\u30b9\u30c8\u30ea\u30fc\u30df\u30f3\u30b0\u306b\u3088\u308b\u30ed\u30dc\u30c3\u30c8\u5de5\u5b66 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# ストリーミングによるロボット工学

`gemini-robotics-er-2-streaming-preview` モデル エンドポイントは、[Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja) と統合された専用のストリーミング エンドポイントを公開します。これにより、アプリケーションとロボット間のリアルタイムの双方向のやり取りが可能になります。そのため、高速なフィードバック ループと環境へのリアクティブなレスポンスを必要とするエージェントに適しています。

[Google AI Studio で試す](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=ja)
[GitHub からサンプルアプリのクローンを作成する](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## ユースケース

- **マルチロボットの連携**: 共有セッションを通じてタスクの状態を通信し、サブタスクを委任する複数のロボット。
- **継続的モニタリング**: シーンを監視し、コンテナの充填レベルに達するなど、特定のイベントが発生したときにアクションをトリガーするロボット。
- **倉庫とロジスティクス**: 商品を目視で確認し、梱包の進捗状況を追跡し、エラーから復旧するピッキングと梱包のエージェント。

## 技術仕様

次の表に、Live API の技術仕様の概要を示します。

| カテゴリ | 詳細 |
| --- | --- |
| 入力モダリティ | 音声（RAW 16 ビット PCM 音声、16kHz、リトル エンディアン）、画像（JPEG <= 1FPS）、テキスト |
| 出力モダリティ | テキスト |
| プロトコル | ステートフル WebSocket 接続（WSS） |

## エージェント設定を構築する

Live API で構築されたすべてのロボット エージェントは、次の 3 つのステップに従います。

1. **ロボットの機能をツールとして宣言します。**ロボットが実行できる各アクション（移動、つかむ、話すなど）は、名前、説明、パラメータ スキーマを含む関数宣言になります。物理アクションは `"behavior": "BLOCKING"` を使用する必要があります。これにより、モデルはロボットが終了するまで待ってから次のステップを選択します。
2. **マルチモーダル入力を永続セッションにストリーミングします。**`live.connect` セッションを開き、タスクの存続期間中開いたままにします。ロボットのセンサーから届いた動画フレーム、音声、テキストを送信します。
3. **受信ループでツール呼び出しを処理します。**モデルがアクションを選択するたびに、`tool_call` メッセージが送信されます。受信ループは、ロボット SDK に対して関数を実行し、`tool_response` を返送します。セッションは開いたままになり、モデルは結果に基づいて次のアクションを選択します。

以降のセクションでは、これらの手順を 3 つの一般的なパターン（ベースライン エージェント ループ、ハートビートによるプロアクティブなシーン モニタリング、ツールとしての TTS を介した音声のルーティング）に適用する方法を示します。

## 関数呼び出しでロボットをオーケストレートする

次の例は、3 つのステップすべてが 1 つの Python スクリプトで連携している様子を示しています。

ステップ 1（ツールの定義）では、ロボットの機能を関数宣言として宣言します。`navigate` 関数は `"behavior": "BLOCKING"` を使用するため、モデルはロボットがウェイポイントに到達するまで待ってから別のツールを呼び出します。同じリストに関数宣言を追加して、ロボットの機能を追加で公開します。

ステップ 2 - 入力ヘルパー - は、さまざまなモダリティ入力をセッションにストリーミングする 3 つの関数を示しています。`send_text` はコマンド、`send_image` はテキスト プロンプト（省略可）を含むカメラ フレーム、`send_audio` はマイクからの未加工の PCM 音声です。

ステップ 3（受信ループ）は同時に実行され、`server_content` メッセージ（モデルのテキスト出力）と `tool_call` メッセージ（モデルがロボット アクションをリクエストしている）の 2 種類のメッセージを処理します。ツール呼び出しが届くと、ループは `execute_tool`（実際のロボット SDK に置き換えるスタブ）を呼び出し、`tool_response` を返送して、モデルが次のアクションを選択できるようにします。

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

受信ループは、各ツールのレスポンス後もアクティブなままです。モデルは、アクション シーケンス全体を事前にエンコードすることなく、長期的な計画を構築して修正します。

## プロアクティブな空間時間推論

Live API は動画をストリーミングしますが、動画フレームだけでは新しい推論ターンはトリガーされません。動画フレームには、モデルのレスポンスをトリガーするテキストまたは音声のプロンプトが必要です。詳しくは、[Live API の機能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ja)をご覧ください。

プロアクティブな推論を有効にするには、**ハートビート**を実装します。最新のカメラフレームを定期的に送信し、その後にモデルにシーンの検査と明示的な判断を強制する短いテキスト プロンプトを送信します。動画入力は 1 秒あたり 1 フレームにレート制限されます。

### ハートビートを実装する

ハートビート コルーチンは、同じセッション内の別の `asyncio` タスクとして実行されます。各ターンの完了（`er_turn_done`）を待機しながら、インフライト推論の中断を回避するために、1 Hz のケイデンス（動画入力レート制限に一致）を機会的にターゲットにします。

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

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

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### 受信ループを更新する

モデルのターンが完了したことを通知するには、`receive_loop` を更新して `er_turn_done` を設定します。

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## 外部 TTS によるオーディオ出力

Gemini Robotics ER 2 はテキストを返します。アプリケーションは、完了したレスポンスを、挿入されたコールバックを介して別の TTS プロバイダ（[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja) など）に転送します。これにより、音声のレイテンシ、音声の選択、割り込み動作を制御し、エージェント ロジックを変更せずに TTS バックエンドを切り替えることができます。

TTS をツールとして宣言して、モデルが「何かを言う」を「腕を動かす」と同じように扱うようにすることもできます。最初のセクションの `tools` リストに次の関数宣言を追加します。

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

TTS を関数宣言でラップすることで、モデルは他のロボット アクションと同じツール呼び出しパスで音声を処理します。アプリは、挿入されたコールバックで呼び出しを完了します。

## GitHub の例

Spot ロボットのおやつ取得デモや Tinybot パンチルト Hello World などの完全な動作例については、[Robotics Live API の例](https://github.com/google-gemini/robotics-samples/tree/main/live-api)をご覧ください。

## 次のステップ

- [動画の理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - 瞬間検出と進行状況の分類。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - ストリーミングなしの長期的なタスク。
- [Live API の概要](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja) - Live API の完全なドキュメント。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-16 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-16 UTC。"],[],[]]
