---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-TW
fetched_at: 2026-07-06T05:16:44.436860+00:00
title: "\u4f7f\u7528 WebSocket \u958b\u59cb\u4f7f\u7528 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 WebSocket 開始使用 Gemini Live API

Gemini Live API 支援音訊、影片和文字輸入，以及原生音訊輸出，可與 Gemini 模型進行即時雙向互動。本指南說明如何使用原始 WebSocket 直接整合 API。

[在 Google AI Studio 中試用 Live APImic](https://aistudio.google.com/live?hl=zh-tw)
[從 GitHub 複製範例應用程式code](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[使用程式碼編寫代理程式技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw)

## 總覽

Gemini Live API 使用 WebSocket 進行即時通訊。與使用 SDK 不同，這種做法需要直接管理 WebSocket 連線，並以 API 定義的特定 JSON 格式傳送/接收訊息。

重要概念：

- **WebSocket 端點**：用於連線的特定網址。
- **訊息格式**：所有通訊都是透過符合 [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentclientmessage) 和 [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentservermessage) 結構的 JSON 訊息完成。
- **工作階段管理**：您必須負責維護 WebSocket 連線。

## 驗證

驗證作業的處理方式，是在 WebSocket 網址中加入 API 金鑰做為查詢參數。

端點格式為：

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

然後將 `YOUR_API_KEY` 替換成您的實際 API 金鑰。

## 使用臨時權杖進行驗證

如果您使用[臨時權杖](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-tw)，則需要連線至 `v1alpha` 端點。臨時權杖必須以 `access_token` 查詢參數的形式傳遞。

臨時金鑰的端點格式如下：

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

請將 `{short-lived-token}` 替換為實際的暫時性權杖。

## 連線至 Live API

如要啟動即時工作階段，請與已驗證的端點建立 WebSocket 連線。透過 WebSocket 傳送的第一則訊息必須是包含 `config` 的 [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentsetup)。如需完整設定選項，請參閱「[Live API - WebSockets API 參考資料](https://ai.google.dev/api/live?hl=zh-tw)」。

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

## 正在傳送文字內容

如要傳送輸入文字，請使用 `text` 欄位建構 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentrealtimeinput) 訊息。

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

## 正在傳送音訊

音訊必須以原始 PCM 資料 (原始 16 位元 PCM 音訊，16 kHz，小端序) 傳送。使用音訊資料建構 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentrealtimeinput) 訊息。`mimeType`至關重要。

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

如要瞭解如何從用戶端裝置 (例如瀏覽器) 取得音訊，請參閱 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74) 上的端對端範例。

## 正在傳送影片

影片影格會以個別圖片 (例如 JPEG 或 PNG) 傳送。與音訊類似，請使用 `realtimeInput` 和 `Blob`，並指定正確的 `mimeType`。

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

如需如何從用戶端裝置 (例如瀏覽器) 取得影片的範例，請參閱 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222) 上的端對端範例。

## 接收回覆

WebSocket 會傳回 [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentservermessage) 訊息。您需要剖析這些 JSON 訊息，並處理不同類型的內容。

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

如需處理回應的範例，請參閱 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75) 上的端對端範例。

## 處理工具呼叫

模型要求呼叫工具時，[`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontentservermessage) 會包含 `toolCall` 欄位。您必須在本機執行函式，並使用 [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=zh-tw#bidigeneratecontenttoolresponse) 訊息將結果傳送回 WebSocket。

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

## 後續步驟

- 如需重要功能和設定 (包括語音活動偵測和原生音訊功能)，請參閱完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-tw)指南。
- 詳閱[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-tw)指南，瞭解如何整合 Live API 與工具和函式呼叫。
- 如要管理長時間進行的對話，請參閱[工作階段管理](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-tw)指南。
- 請參閱[臨時權杖](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-tw)指南，瞭解如何在[用戶端對伺服器](#implementation-approach)應用程式中安全地進行驗證。
- 如要進一步瞭解基礎 WebSockets API，請參閱 [WebSockets API 參考資料](https://ai.google.dev/api/live?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-09 (世界標準時間)。"],[],[]]
