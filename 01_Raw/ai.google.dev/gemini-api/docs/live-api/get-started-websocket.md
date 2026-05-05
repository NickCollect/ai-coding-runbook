---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=vi
fetched_at: 2026-05-05T20:43:51.406142+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Get started with Gemini Live API using WebSockets

Gemini Live API cho phép tương tác hai chiều theo thời gian thực với các mô hình Gemini, hỗ trợ đầu vào âm thanh, video và văn bản cũng như đầu ra âm thanh gốc. Hướng dẫn này giải thích cách tích hợp trực tiếp với API bằng cách sử dụng WebSocket thô.

[Dùng Live API trong Google AI Studiomic](https://aistudio.google.com/live?hl=vi)
[Sao chép ứng dụng mẫu từ GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Sử dụng các kỹ năng của tác nhân lập trìnhterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi)

## Tổng quan

Gemini Live API sử dụng WebSockets để giao tiếp theo thời gian thực. Không giống như việc sử dụng SDK, phương pháp này liên quan đến việc quản lý trực tiếp kết nối WebSocket và gửi/nhận thông báo ở một định dạng JSON cụ thể do API xác định.

Các khái niệm chính:

- **Điểm cuối WebSocket**: URL cụ thể để kết nối.
- **Định dạng thông báo**: Mọi hoạt động giao tiếp đều được thực hiện thông qua các thông báo JSON tuân thủ cấu trúc [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentclientmessage) và [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentservermessage).
- **Quản lý phiên**: Bạn chịu trách nhiệm duy trì kết nối WebSocket.

## Xác thực

Quá trình xác thực được xử lý bằng cách thêm khoá API dưới dạng tham số truy vấn trong URL WebSocket.

Định dạng điểm cuối là:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Thay thế `YOUR_API_KEY` bằng khoá API thực tế của bạn.

## Xác thực bằng mã thông báo tạm thời

Nếu đang sử dụng [mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=vi), bạn cần kết nối với điểm cuối `v1alpha`.
Bạn cần truyền mã thông báo tạm thời dưới dạng tham số truy vấn `access_token`.

Định dạng điểm cuối cho khoá tạm thời là:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Thay thế `{short-lived-token}` bằng mã thông báo tạm thời thực tế.

## Kết nối với Live API

Để bắt đầu một phiên trực tiếp, hãy thiết lập kết nối WebSocket đến điểm cuối đã xác thực.
Thông báo đầu tiên được gửi qua WebSocket phải là [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentsetup) chứa `config`.
Để biết các lựa chọn cấu hình đầy đủ, hãy xem [Live API - Tài liệu tham khảo API WebSockets](https://ai.google.dev/api/live?hl=vi).

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

## Đang gửi tin nhắn

Để gửi dữ liệu đầu vào là văn bản, hãy tạo một thông báo [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentrealtimeinput) có trường `text`.

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

## Đang gửi âm thanh

Bạn cần gửi âm thanh dưới dạng dữ liệu PCM thô (âm thanh PCM thô 16 bit, 16 kHz, little-endian). Tạo một thông báo [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentrealtimeinput) bằng dữ liệu âm thanh. `mimeType` là yếu tố quan trọng.

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

Để biết ví dụ về cách lấy âm thanh từ thiết bị của khách hàng (ví dụ: trình duyệt), hãy xem ví dụ toàn diện trên [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Đang gửi video

Khung hình video được gửi dưới dạng hình ảnh riêng lẻ (ví dụ: JPEG hoặc PNG). Tương tự như âm thanh, hãy sử dụng `realtimeInput` với `Blob`, chỉ định `mimeType` chính xác.

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

Để biết ví dụ về cách lấy video từ thiết bị của khách hàng (ví dụ: trình duyệt), hãy xem ví dụ toàn diện trên [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Nhận phản hồi

WebSocket sẽ gửi lại thông báo [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentservermessage). Bạn cần phân tích cú pháp các thông báo JSON này và xử lý nhiều loại nội dung.

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

Để biết ví dụ về cách xử lý phản hồi, hãy xem ví dụ toàn diện trên [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Xử lý lệnh gọi công cụ

Khi mô hình yêu cầu một lệnh gọi công cụ, [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentservermessage) sẽ chứa một trường `toolCall`. Bạn phải thực thi hàm cục bộ và gửi kết quả trở lại WebSocket bằng thông báo [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontenttoolresponse).

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

## Bước tiếp theo

- Đọc hướng dẫn đầy đủ về [Các chức năng](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi) của Live API để biết các chức năng và cấu hình chính, bao gồm cả tính năng Phát hiện hoạt động bằng giọng nói và các tính năng âm thanh gốc.
- Đọc hướng dẫn về [Sử dụng công cụ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi) để tìm hiểu cách tích hợp Live API với các công cụ và lệnh gọi hàm.
- Hãy đọc hướng dẫn [Quản lý phiên](https://ai.google.dev/gemini-api/docs/live-session?hl=vi) để quản lý các cuộc trò chuyện kéo dài.
- Đọc hướng dẫn về [Mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=vi) để xác thực an toàn trong các ứng dụng [từ ứng dụng đến máy chủ](#implementation-approach).
- Để biết thêm thông tin về API WebSockets cơ bản, hãy xem [Tài liệu tham khảo API WebSockets](https://ai.google.dev/api/live?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
