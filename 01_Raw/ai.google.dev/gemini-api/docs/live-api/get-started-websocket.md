---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ko
fetched_at: 2026-05-05T13:17:05.130118+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/live-api/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/live-api/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/live-api/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/live-api/문서)

의견 보내기

# Get started with Gemini Live API using WebSockets

Gemini Live API를 사용하면 Gemini 모델과 실시간 양방향 상호작용이 가능하며 오디오, 동영상, 텍스트 입력과 네이티브 오디오 출력을 지원합니다. 이 가이드에서는 원시 WebSockets를 사용하여 API와 직접 통합하는 방법을 설명합니다.

[Google AI Studio에서 Live API 사용해 보기mic](https://ai.google.dev/gemini-api/docs/live-api/Google AI Studio에서 Live API 사용해 보기mic)
[GitHub에서 샘플 앱 클론하기code](https://ai.google.dev/gemini-api/docs/live-api/GitHub에서 샘플 앱 클론하기code)
[코딩 에이전트 기술 사용하기terminal](https://ai.google.dev/gemini-api/docs/live-api/코딩 에이전트 기술 사용하기terminal)

## 개요

Gemini Live API는 실시간 통신에 WebSockets를 사용합니다. SDK를 사용하는 것과 달리 이 접근 방식은 WebSocket 연결을 직접 관리하고 API에서 정의한 특정 JSON 형식으로 메시지를 주고받는 것과 관련이 있습니다.

주요 개념

- **WebSocket 엔드포인트**: 연결할 특정 URL입니다.
- **메시지 형식**: 모든 통신은 [`BidiGenerateContentClientMessage`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentClientMessage`) 및 [`BidiGenerateContentServerMessage`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentServerMessage`) 구조를 준수하는 JSON 메시지를 통해 이루어집니다.
- **세션 관리**: WebSocket 연결을 유지하는 것은 사용자의 책임입니다.

## 인증

인증은 API 키를 WebSocket URL의 쿼리 매개변수로 포함하여 처리됩니다.

엔드포인트 형식은 다음과 같습니다.

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

`YOUR_API_KEY`를 실제 API 키로 바꿉니다.

## 단기 토큰으로 인증

단기 토큰을 사용하는 경우 [단기 토큰](https://ai.google.dev/gemini-api/docs/live-api/단기 토큰) 엔드포인트에 연결해야 합니다.`v1alpha`
단기 토큰은 `access_token` 쿼리 매개변수로 전달되어야 합니다.

단기 키의 엔드포인트 형식은 다음과 같습니다.

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

`{short-lived-token}`을 실제 단기 토큰으로 바꿉니다.

## Live API에 연결

실시간 세션을 시작하려면 인증된 엔드포인트에 WebSocket 연결을 설정합니다.
WebSocket을 통해 전송되는 첫 번째 메시지는 [`BidiGenerateContentSetup`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentSetup`)가 포함된 `config`이어야 합니다.
전체 구성 옵션은 [Live API - WebSockets API 참조](https://ai.google.dev/gemini-api/docs/live-api/Live API - WebSockets API 참조)를 확인하세요.

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
        config_message = {
            "config": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(config_message))
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
  const configMessage = {
    config: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(configMessage));
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

## 텍스트 전송 중

텍스트 입력을 전송하려면 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentRealtimeInput`) 메시지를 `text` 필드로 구성합니다.

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

## 오디오 전송 중

오디오는 원시 PCM 데이터 (원시 16비트 PCM 오디오, 16kHz, 리틀 엔디안)로 전송되어야 합니다. 오디오 데이터로 [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentRealtimeInput`) 메시지를 구성합니다. `mimeType`은 매우 중요합니다.

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

클라이언트 기기 (예: 브라우저)에서 오디오를 가져오는 방법의 예시는
[GitHub](https://ai.google.dev/gemini-api/docs/live-api/GitHub)의 포괄적인 예시를 참조하세요.

## 동영상 전송 중

동영상 프레임은 개별 이미지 (예: JPEG 또는 PNG)로 전송됩니다. 오디오와 마찬가지로 올바른 `mimeType`을 지정하여 `Blob`과 함께 `realtimeInput`을 사용합니다.

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

클라이언트 기기 (예: 브라우저)에서 동영상을 가져오는 방법의 예시는
[GitHub](https://ai.google.dev/gemini-api/docs/live-api/GitHub)의 포괄적인 예시를 참조하세요.

## 응답 수신

WebSocket은 [`BidiGenerateContentServerMessage`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentServerMessage`) 메시지를 다시 전송합니다. 이러한 JSON 메시지를 파싱하고 다양한 유형의 콘텐츠를 처리해야 합니다.

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

응답을 처리하는 방법의 예시는 [GitHub](https://ai.google.dev/gemini-api/docs/live-api/GitHub)의 포괄적인 예시를 참조하세요.

## 도구 호출 처리

모델이 도구 호출을 요청하면 [`BidiGenerateContentServerMessage`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentServerMessage`)에 `toolCall` 필드가 포함됩니다. 함수를 로컬에서 실행하고 [`BidiGenerateContentToolResponse`](https://ai.google.dev/gemini-api/docs/live-api/`BidiGenerateContentToolResponse`) 메시지를 사용하여 결과를 WebSocket으로 다시 전송해야 합니다.

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

## 다음 단계

- 음성 활동 감지 및 네이티브 오디오 기능을 비롯한 주요 기능 및 구성은 전체 Live API [기능](https://ai.google.dev/gemini-api/docs/live-api/기능) 가이드를 읽어보세요.
- Live API를 도구 및 함수 호출과 통합하는 방법을 알아보려면 [도구 사용](https://ai.google.dev/gemini-api/docs/live-api/도구 사용) 가이드를 읽어보세요.
- 장기 실행 대화를 관리하려면 [세션 관리](https://ai.google.dev/gemini-api/docs/live-api/세션 관리) 가이드를 읽어보세요.
- [클라이언트-서버 애플리케이션에서 보안 인증을 하려면 [단기 토큰](https://ai.google.dev/gemini-api/docs/live-api/클라이언트-서버 애플리케이션에서 보안 인증을 하려면 [단기 토큰) 가이드를 읽어보세요.](#implementation-approach)
- 기본 WebSockets API에 관한 자세한 내용은 [WebSockets API 참조](https://ai.google.dev/gemini-api/docs/live-api/WebSockets API 참조)를 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/live-api/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/live-api/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/live-api/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?
