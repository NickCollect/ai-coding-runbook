---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-TW
fetched_at: 2026-06-22T06:27:59.701257+00:00
title: "\u4f7f\u7528 Live API \u7ba1\u7406\u5de5\u4f5c\u968e\u6bb5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Live API 管理工作階段

在 Live API 中，工作階段是指持續連線，輸入和輸出內容會透過同一連線持續串流 (進一步瞭解[運作方式](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw))。這種獨特的工作階段設計可實現低延遲，並支援獨特功能，但也會帶來一些挑戰，例如工作階段時間限制和提早終止。本指南涵蓋相關策略，可協助您克服使用 Live API 時可能發生的工作階段管理問題。

## 工作階段生命週期

如果沒有壓縮，純音訊通話時間上限為 15 分鐘，音訊和視訊通話時間上限為 2 分鐘。如果超過這些限制，工作階段 (以及連線) 就會終止，但您可以使用[內容視窗壓縮](#context-window-compression)功能，將工作階段延長至無限時間。

連線的生命週期也有所限制，大約為 10 分鐘。連線終止時，工作階段也會終止。在這種情況下，您可以設定單一工作階段，透過[工作階段續傳](#session-resumption)在多個連線中保持有效。連線結束前，您也會收到 [GoAway 訊息](#goaway-message)，可採取進一步行動。

## 壓縮脈絡窗口

如要延長工作階段時間，避免連線突然終止，您可以啟用內容視窗壓縮功能，方法是在工作階段設定中設定 [contextWindowCompression](https://ai.google.dev/api/live?hl=zh-tw#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) 欄位。

在 [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=zh-tw#contextwindowcompressionconfig) 中，您可以設定[滑動視窗機制](https://ai.google.dev/api/live?hl=zh-tw#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)和觸發壓縮的[權杖數量](https://ai.google.dev/api/live?hl=zh-tw#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)。

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

## 繼續工作階段

如要防止伺服器定期重設 WebSocket 連線時終止工作階段，請在[設定設定](https://ai.google.dev/api/live?hl=zh-tw#BidiGenerateContentSetup)中設定 [sessionResumption](https://ai.google.dev/api/live?hl=zh-tw#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) 欄位。

傳遞這項設定會導致伺服器傳送 [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=zh-tw#SessionResumptionUpdate) 訊息，這些訊息可用於恢復工作階段，方法是將最後一個恢復權杖做為後續連線的 [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=zh-tw#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) 傳遞。

在最後一個工作階段終止後，續傳權杖的有效時間為 2 小時。

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

## 在工作階段中斷前收到訊息

伺服器會傳送「GoAway」[GoAway](https://ai.google.dev/api/live?hl=zh-tw#GoAway)訊息，表示目前的連線即將終止。這則訊息包含 [timeLeft](https://ai.google.dev/api/live?hl=zh-tw#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left)，指出剩餘時間，並讓您在連線因 ABORTED 而終止前採取進一步行動。

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

## 在生成完成時收到訊息

伺服器會傳送 [generationComplete](https://ai.google.dev/api/live?hl=zh-tw#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete) 訊息，表示模型已完成生成回覆。

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

## 後續步驟

如要進一步瞭解如何使用 Live API，請參閱[完整的功能](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw)指南、[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw)頁面或 [Live API 教戰手冊](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
