---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-TW
fetched_at: 2026-06-08T05:27:41.487408+00:00
title: "\u4f7f\u7528 Google GenAI SDK \u958b\u59cb\u4f7f\u7528 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Google GenAI SDK 開始使用 Gemini Live API

Gemini Live API 支援音訊、影片和文字輸入，以及原生音訊輸出，可與 Gemini 模型進行即時雙向互動。本指南說明如何在伺服器上使用 Google GenAI SDK，與 API 整合。

[在 Google AI Studio 中試用 Live APImic](https://aistudio.google.com/live?hl=zh-tw)
[從 GitHub 複製範例應用程式code](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[使用程式碼編寫代理程式技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw)

## 總覽

Gemini Live API 使用 WebSocket 進行即時通訊。`google-genai` SDK 提供高階非同步介面，可管理這些連線。

重要概念：

- **工作階段**：與模型建立的持續連線。
- **設定**：設定模式 (語音/文字)、聲音和系統指令。
- **即時輸入**：以 Blob 形式傳送音訊和視訊影格。

## 連線至 Live API

使用 API 金鑰啟動 Live API 會話：

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## 正在傳送文字內容

您可以使用 `send_realtime_input` (Python) 或 `sendRealtimeInput` (JavaScript) 傳送文字。

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## 正在傳送音訊

音訊必須以原始 PCM 資料 (原始 16 位元 PCM 音訊、16 kHz、小端序) 傳送。

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

如要瞭解如何從用戶端裝置 (例如瀏覽器) 取得音訊，請參閱 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70) 上的端對端範例。

## 正在傳送影片

系統會以特定影格率 (每秒最多 1 個影格) 傳送影片影格，並以個別圖片 (例如 JPEG 或 PNG) 形式傳送。

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

如需如何從用戶端裝置 (例如瀏覽器) 取得影片的範例，請參閱 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120) 上的端對端範例。

## 接收音訊

模型會以資料區塊的形式傳回音訊回覆。

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

如要瞭解如何[在伺服器上接收音訊](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98)，以及[在瀏覽器中播放音訊](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174)，請參閱 GitHub 上的範例應用程式。

## 正在接收文字內容

伺服器內容會提供使用者輸入內容和模型輸出內容的轉錄稿。

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## 處理工具呼叫

這個 API 支援工具呼叫 (函式呼叫)。模型要求呼叫工具時，您必須執行函式並傳回回應。

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## 後續步驟

- 如需重要功能和設定 (包括語音活動偵測和原生音訊功能)，請參閱完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw)指南。
- 詳閱[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw)指南，瞭解如何整合 Live API 與工具和函式呼叫。
- 如要管理長時間進行的對話，請參閱[工作階段管理](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-tw)指南。
- 請參閱[臨時權杖](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-tw)指南，瞭解如何在[用戶端對伺服器](#implementation-approach)應用程式中安全地進行驗證。
- 如要進一步瞭解基礎 WebSockets API，請參閱 [WebSockets API 參考資料](https://ai.google.dev/api/live?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
