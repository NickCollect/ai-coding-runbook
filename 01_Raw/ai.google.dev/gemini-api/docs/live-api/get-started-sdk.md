---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-CN
fetched_at: 2026-07-20T04:37:26.095605+00:00
title: "\u901a\u8fc7 Google GenAI SDK \u5f00\u59cb\u4f7f\u7528 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 通过 Google GenAI SDK 开始使用 Gemini Live API

Gemini Live API 支持与 Gemini 模型进行实时双向互动，并支持音频、视频和文本输入以及原生音频输出。本指南介绍了如何在服务器上使用 Google GenAI SDK 与 API 集成。

[在 Google AI Studio 中试用 Live APImic](https://aistudio.google.com/live?hl=zh-cn)
[从 GitHub 克隆示例应用code](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[使用编码代理技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn)

## 概览

Gemini Live API 使用 WebSocket 进行实时通信。`google-genai` SDK 提供了一个用于管理这些连接的高级异步接口。

主要概念：

- **会话**：与模型的持久连接。
- **配置**：设置模态（音频/文本）、语音和系统指令。
- **实时输入**：以 blob 形式发送音频和视频帧。

## 连接到 Live API

使用 API 密钥启动 Live API 会话：

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

## 正在发送短信

您可以使用 `send_realtime_input` (Python) 或 `sendRealtimeInput` (JavaScript) 发送文本。

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

## 发送音频

音频需要以原始 PCM 数据（原始 16 位 PCM 音频，16kHz，小端序）的形式发送。

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

如需查看如何从客户端设备（例如浏览器）获取音频的示例，请参阅 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70) 上的端到端示例。

## 正在发送视频

视频帧以特定帧速率（每秒最多 1 帧）作为单独的图片（例如 JPEG 或 PNG）发送。

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

如需查看如何从客户端设备（例如浏览器）获取视频的示例，请参阅 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120) 上的端到端示例。

## 接收音频

模型以数据块的形式返回音频回答。

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

如需了解如何[在服务器上接收音频](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98)以及如何[在浏览器中播放音频](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174)，请参阅 GitHub 上的示例应用。

## 正在接收短信

服务器内容中包含用户输入和模型输出的转写内容。

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

## 处理工具调用

该 API 支持工具调用（函数调用）。当模型请求工具调用时，您必须执行该函数并将响应发送回去。

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

## 后续步骤

- 如需了解主要功能和配置（包括语音活动检测和原生音频功能），请参阅完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn)指南。
- 请参阅[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn)指南，了解如何将 Live API 与工具和函数调用集成。
- 如需了解如何管理长时间运行的对话，请参阅[会话管理](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn)指南。
- 请参阅[临时令牌](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-cn)指南，了解如何在[客户端到服务器](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn#implementation-approach)应用中进行安全身份验证。
- 如需详细了解底层 WebSockets API，请参阅 [WebSockets API 参考文档](https://ai.google.dev/api/live?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-08。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-08。"],[],[]]
