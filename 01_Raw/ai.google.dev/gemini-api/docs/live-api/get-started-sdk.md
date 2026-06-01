---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=vi
fetched_at: 2026-06-01T05:59:55.974841+00:00
title: "B\u1eaft \u0111\u1ea7u s\u1eed d\u1ee5ng Gemini Live API b\u1eb1ng Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bắt đầu sử dụng Gemini Live API bằng Google GenAI SDK

Gemini Live API cho phép tương tác hai chiều theo thời gian thực với các mô hình Gemini, hỗ trợ đầu vào âm thanh, video và văn bản cũng như đầu ra âm thanh gốc. Hướng dẫn này giải thích cách tích hợp với API bằng Google GenAI SDK trên máy chủ của bạn.

[Dùng Live API trong Google AI Studiomic](https://aistudio.google.com/live?hl=vi)
[Sao chép ứng dụng mẫu từ GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Sử dụng các kỹ năng của tác nhân lập trìnhterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi)

## Tổng quan

Gemini Live API sử dụng WebSockets để giao tiếp theo thời gian thực. SDK `google-genai` cung cấp một giao diện không đồng bộ cấp cao để quản lý các kết nối này.

Các khái niệm chính:

- **Phiên**: Kết nối liên tục với mô hình.
- **Config**: Thiết lập phương thức (âm thanh/văn bản), giọng nói và hướng dẫn hệ thống.
- **Đầu vào theo thời gian thực**: Gửi các khung hình âm thanh và video dưới dạng blob.

## Kết nối với Live API

Bắt đầu phiên Live API bằng khoá API:

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

## Đang gửi tin nhắn

Bạn có thể gửi văn bản bằng `send_realtime_input` (Python) hoặc `sendRealtimeInput` (JavaScript).

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

## Đang gửi âm thanh

Bạn cần gửi âm thanh dưới dạng dữ liệu PCM thô (âm thanh PCM thô 16 bit, 16 kHz, little-endian).

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

Để biết ví dụ về cách lấy âm thanh từ thiết bị của khách hàng (ví dụ: trình duyệt), hãy xem ví dụ toàn diện trên [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Đang gửi video

Khung hình video được gửi dưới dạng hình ảnh riêng lẻ (ví dụ: JPEG hoặc PNG) ở một tốc độ khung hình cụ thể (tối đa 1 khung hình/giây).

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

Để biết ví dụ về cách lấy video từ thiết bị của khách hàng (ví dụ: trình duyệt), hãy xem ví dụ toàn diện trên [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Nhận âm thanh

Các câu trả lời bằng âm thanh của mô hình được nhận dưới dạng các khối dữ liệu.

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

Hãy xem ứng dụng mẫu trên GitHub để tìm hiểu cách [nhận âm thanh trên máy chủ](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) và [phát âm thanh đó trong trình duyệt](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Đang nhận tin nhắn

Bản chép lời cho cả dữ liệu đầu vào của người dùng và dữ liệu đầu ra của mô hình đều có trong nội dung trên máy chủ.

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

## Xử lý lệnh gọi công cụ

API này hỗ trợ lệnh gọi công cụ (lệnh gọi hàm). Khi mô hình yêu cầu một lệnh gọi công cụ, bạn phải thực thi hàm và gửi phản hồi trở lại.

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

## Bước tiếp theo

- Đọc hướng dẫn đầy đủ về [Các chức năng](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi) của Live API để biết các chức năng và cấu hình chính, bao gồm cả tính năng Phát hiện hoạt động bằng giọng nói và các tính năng âm thanh gốc.
- Đọc hướng dẫn về [Sử dụng công cụ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi) để tìm hiểu cách tích hợp Live API với các công cụ và lệnh gọi hàm.
- Hãy đọc hướng dẫn [Quản lý phiên](https://ai.google.dev/gemini-api/docs/live-session?hl=vi) để quản lý các cuộc trò chuyện kéo dài.
- Đọc hướng dẫn về [Mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=vi) để xác thực an toàn trong các ứng dụng [từ ứng dụng đến máy chủ](#implementation-approach).
- Để biết thêm thông tin về API WebSockets cơ bản, hãy xem [Tài liệu tham khảo về API WebSockets](https://ai.google.dev/api/live?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-29 UTC."],[],[]]
