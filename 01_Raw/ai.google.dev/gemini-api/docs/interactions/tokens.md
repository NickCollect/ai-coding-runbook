---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=vi
fetched_at: 2026-06-15T06:33:26.588733+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tìm hiểu và đếm mã thông báo

Gemini và các mô hình AI tạo sinh khác xử lý dữ liệu đầu vào và đầu ra ở mức độ chi tiết được gọi là *mã thông báo*.

**Đối với các mô hình Gemini, một mã thông báo tương đương với khoảng 4 ký tự.
100 mã thông báo tương đương với khoảng 60 đến 80 từ tiếng Anh.**

## Giới thiệu về mã thông báo

Mã thông báo có thể là các ký tự đơn như `z` hoặc toàn bộ từ như `cat`. Các từ dài được chia thành nhiều mã thông báo. Tập hợp tất cả các mã thông báo mà mô hình sử dụng được gọi là từ vựng và quy trình phân tách văn bản thành mã thông báo được gọi là *mã hoá*.

Khi bật tính năng thanh toán, [chi phí của một lệnh gọi đến Gemini API](https://ai.google.dev/pricing?hl=vi) sẽ được xác định một phần dựa trên số lượng mã thông báo đầu vào và đầu ra. Vì vậy, việc biết cách đếm mã thông báo có thể hữu ích.

## Đếm mã thông báo

Tất cả dữ liệu đầu vào và đầu ra từ Gemini API đều được mã hoá thành mã thông báo, bao gồm cả văn bản, tệp hình ảnh và các phương thức không phải văn bản khác.

Bạn có thể đếm mã thông báo theo những cách sau:

- **Gọi `count_tokens` bằng dữ liệu đầu vào của yêu cầu.** Trả về tổng số mã thông báo trong *chỉ đầu vào*. Hãy thực hiện lệnh gọi này trước khi gửi dữ liệu đầu vào để kiểm tra kích thước của các yêu cầu.
- **Sử dụng `usage` trên câu trả lời tương tác.** Trả về số lượng mã thông báo cho dữ liệu đầu vào (`total_input_tokens`), dữ liệu đầu ra (`total_output_tokens`), suy nghĩ (`total_thought_tokens`), nội dung được lưu vào bộ nhớ đệm (`total_cached_tokens`), việc sử dụng công cụ (`total_tool_use_tokens`) và tổng số (`total_tokens`).

### Đếm mã thông báo văn bản

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Đếm mã thông báo nhiều lượt

Đếm số lượng token trong nhật ký trò chuyện bằng cách sử dụng `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Đếm mã thông báo đa phương thức

Mọi dữ liệu đầu vào cho Gemini API đều được mã hoá thành mã thông báo, bao gồm cả hình ảnh, video và âm thanh.
Những điểm chính về việc mã hoá:

- **Hình ảnh**: Hình ảnh có kích thước ≤384 pixel ở cả hai chiều được tính là 258 mã thông báo. Các hình ảnh lớn hơn được chia thành các ô có kích thước 768x768 pixel, mỗi ô được tính là 258 mã thông báo.
- **Video**: 263 mã thông báo mỗi giây
- **Âm thanh**: 32 mã thông báo mỗi giây

#### Mã thông báo hình ảnh

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**Ví dụ về dữ liệu nội tuyến:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### Mã thông báo video

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Mã thông báo âm thanh

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Đếm mã thông báo hướng dẫn hệ thống

Các chỉ dẫn hệ thống được tính là một phần của mã thông báo đầu vào:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Đếm mã thông báo công cụ

Các công cụ (hàm, thực thi mã, Google Tìm kiếm) cũng được tính:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Cửa sổ ngữ cảnh

Mỗi mô hình Gemini đều có số lượng mã thông báo tối đa mà mô hình đó có thể xử lý. Cửa sổ ngữ cảnh xác định giới hạn kết hợp của mã thông báo đầu vào và đầu ra.

### Lấy kích thước cửa sổ ngữ cảnh theo phương thức lập trình

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.5-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.5-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

Tìm kích thước cửa sổ ngữ cảnh trên trang [các mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

## Bước tiếp theo

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi): Các kiến thức cơ bản về việc tạo văn bản
- [Lưu vào bộ nhớ đệm](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=vi): Giảm chi phí bằng cách lưu vào bộ nhớ đệm
- [Giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi): Tìm hiểu về chi phí

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-01 UTC."],[],[]]
