---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-CN
fetched_at: 2026-07-20T04:40:18.786188+00:00
title: "\u901a\u8fc7 WebSocket \u5f00\u59cb\u4f7f\u7528 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 通过 WebSocket 开始使用 Gemini Live API

Gemini Live API 支持与 Gemini 模型进行实时双向互动，并支持音频、视频和文本输入以及原生音频输出。本指南介绍了如何使用原始 WebSocket 直接与 API 集成。

[在 Google AI Studio 中试用 Live APImic](https://aistudio.google.com/live?hl=zh-cn)
[从 GitHub 克隆示例应用code](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[使用编码代理技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn)

## 概览

Gemini Live API 使用 WebSocket 进行实时通信。与使用 SDK 不同，此方法涉及直接管理 WebSocket 连接，并以 API 定义的特定 JSON 格式发送/接收消息。

主要概念：

- **WebSocket 端点**：要连接到的特定网址。
- **消息格式**：所有通信均通过符合 [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentclientmessage) 和 [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentservermessage) 结构的 JSON 消息完成。
- **会话管理**：您负责维护 WebSocket 连接。

## 身份验证

身份验证通过在 WebSocket 网址中添加 API 密钥作为查询参数来处理。

端点格式为：

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

将 `YOUR_API_KEY` 替换为您的实际 API 密钥。

## 使用临时令牌进行身份验证

如果您使用的是[临时令牌](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-cn)，则需要连接到 `v1alpha` 端点。临时令牌需要作为 `access_token` 查询参数传递。

临时密钥的端点格式为：

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

将 `{short-lived-token}` 替换为实际的临时令牌。

## 连接到 Live API

如需开始实时会话，请与经过身份验证的端点建立 WebSocket 连接。
通过 WebSocket 发送的第一条消息必须是包含 `config` 的 [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentsetup)。如需查看完整的配置选项，请参阅 [Live API - WebSockets API 参考文档](https://ai.google.dev/api/live?hl=zh-cn)。

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## 正在发送短信

如需发送文本输入，请构建包含 `text` 字段的 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentrealtimeinput) 消息。

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## 发送音频

音频需要以原始 PCM 数据（原始 16 位 PCM 音频，16kHz，小端字节序）的形式发送。使用音频数据构建 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentrealtimeinput) 消息。`mimeType` 至关重要。

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

如需查看如何从客户端设备（例如浏览器）获取音频的示例，请参阅 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74) 上的端到端示例。

## 正在发送视频

视频帧以单独的图片（例如 JPEG 或 PNG）形式发送。与音频类似，请将 `realtimeInput` 与 `Blob` 搭配使用，并指定正确的 `mimeType`。

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

如需查看如何从客户端设备（例如浏览器）获取视频的示例，请参阅 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222) 上的端到端示例。

## 接收回答

WebSocket 将发回 [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentservermessage) 消息。您需要解析这些 JSON 消息并处理不同类型的内容。

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

如需查看有关如何处理响应的示例，请参阅 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75) 上的端到端示例。

## 处理工具调用

当模型请求工具调用时，[`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentservermessage) 将包含 `toolCall` 字段。您必须在本地执行该函数，并使用 [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontenttoolresponse) 消息将结果发送回 WebSocket。

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## 后续步骤

- 如需了解主要功能和配置（包括语音活动检测和原生音频功能），请参阅完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn)指南。
- 请参阅[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn)指南，了解如何将 Live API 与工具和函数调用集成。
- 如需了解如何管理长时间运行的对话，请参阅[会话管理](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn)指南。
- 请参阅[临时令牌](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-cn)指南，了解如何在[客户端到服务器](#implementation-approach)应用中进行安全身份验证。
- 如需详细了解底层 WebSockets API，请参阅 [WebSockets API 参考文档](https://ai.google.dev/api/live?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-09。"],[],[]]
