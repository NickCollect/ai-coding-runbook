---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ja
fetched_at: 2026-06-15T06:21:18.919063+00:00
title: "Live API \u3092\u4f7f\u7528\u3057\u305f\u30bb\u30c3\u30b7\u30e7\u30f3\u7ba1\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Live API を使用したセッション管理

Live API では、セッションとは、入力と出力が同じ接続で継続的にストリーミングされる永続的な接続を指します（[仕組み](https://ai.google.dev/gemini-api/docs/live?hl=ja)をご覧ください）。この独自のセッション設計により、低レイテンシが実現し、独自の機能がサポートされますが、セッションの制限時間や早期終了などの問題も発生する可能性があります。このガイドでは、Live API の使用時に発生する可能性のあるセッション管理の課題を克服するための戦略について説明します。

## セッションの有効期間

圧縮なしの場合、音声のみのセッションは 15 分、音声と動画のセッションは 2 分に制限されます。これらの上限を超えるとセッション（接続）が終了しますが、[コンテキスト ウィンドウの圧縮](#context-window-compression)を使用すると、セッションを無制限に延長できます。

接続の有効期間も約 10 分に制限されています。接続が終了すると、セッションも終了します。この場合、[セッションの再開](#session-resumption)を使用して、複数の接続でアクティブな状態を維持するように 1 つのセッションを構成できます。接続が終了する前に [GoAway メッセージ](#goaway-message)も届くため、さらなるアクションを実行できます。

## コンテキスト ウィンドウの圧縮

セッションを長くして、接続が突然終了しないようにするには、セッション構成の一部として [contextWindowCompression](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) フィールドを設定して、コンテキスト ウィンドウの圧縮を有効にします。

[ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=ja#contextwindowcompressionconfig) では、[スライディング ウィンドウ メカニズム](https://ai.google.dev/api/live?hl=ja#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)と、圧縮をトリガーする[トークン数](https://ai.google.dev/api/live?hl=ja#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)を構成できます。

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## セッションの再開

サーバーが WebSocket 接続を定期的にリセットしたときにセッションが終了しないようにするには、[設定構成](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentSetup)内の [sessionResumption](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) フィールドを構成します。

この構成を渡すと、サーバーは [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=ja#SessionResumptionUpdate) メッセージを送信します。このメッセージは、後続の接続の [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=ja#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) として最後の再開トークンを渡すことで、セッションの再開に使用できます。

再開トークンは、最後のセッションの終了後 2 時間有効です。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## セッションが切断される前にメッセージを受信する

サーバーは、現在の接続がまもなく終了することを示す [GoAway](https://ai.google.dev/api/live?hl=ja#GoAway) メッセージを送信します。このメッセージには、残り時間を示す [timeLeft](https://ai.google.dev/api/live?hl=ja#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left) が含まれています。接続が ABORTED として終了する前に、さらなるアクションを実行できます。

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## 生成が完了したときにメッセージを受信する

サーバーは、モデルがレスポンスの生成を完了したことを示す [generationComplete](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete) メッセージを送信します。

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## 次のステップ

Live API を使用するその他の方法については、[機能](https://ai.google.dev/gemini-api/docs/live?hl=ja)ガイド、[ツールの使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja)ページ、[Live API クックブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
