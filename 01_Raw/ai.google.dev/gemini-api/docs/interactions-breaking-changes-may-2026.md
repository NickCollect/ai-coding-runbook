---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=vi
fetched_at: 2026-06-15T06:22:16.284542+00:00
title: "Interactions API: H\u01b0\u1edbng d\u1eabn di chuy\u1ec3n c\u00e1c thay \u0111\u1ed5i c\u00f3 th\u1ec3 g\u00e2y ra l\u1ed7i (th\u00e1ng 5 n\u0103m 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Interactions API: Hướng dẫn di chuyển các thay đổi có thể gây ra lỗi (tháng 5 năm 2026)

API `v1beta` Interactions đang giới thiệu các thay đổi có thể gây lỗi, giúp tái cấu trúc hình dạng API để hỗ trợ các chức năng trong tương lai như chỉ đạo giữa chuyến bay và các lệnh gọi công cụ không đồng bộ. Trang này giải thích những thay đổi và cung cấp các ví dụ về mã trước và sau để giúp bạn di chuyển. Có 2 danh mục thay đổi:

1. [**Giản đồ bước**](#steps-schema): Một mảng `steps` mới sẽ thay thế mảng `outputs`, cung cấp một dòng thời gian có cấu trúc của từng lượt tương tác.
2. [**Cấu hình định dạng đầu ra**](#output-format-config): `response_format` đa hình mới sẽ hợp nhất tất cả các chế độ kiểm soát định dạng đầu ra và xoá `response_mime_type`.

Làm theo các bước trong phần [Cách di chuyển sang giản đồ mới](#how-to-migrate) để cập nhật quy trình tích hợp.

## Thay đổi cốt lõi: `outputs` thành `steps`

Lược đồ mới sẽ thay thế mảng `outputs` bằng mảng `steps`.

- **Cũ**: Các phản hồi trả về một mảng `outputs` phẳng chỉ chứa nội dung do mô hình tạo.
- **Lược đồ mới**: Các phản hồi trả về một mảng `steps` chứa các bước có cấu trúc với bộ phân biệt loại.

`POST /interactions` chỉ trả về các bước đầu ra. `GET /interactions/{id}` trả về toàn bộ dòng thời gian của bước, bao gồm cả bước `user_input` ban đầu.

### Đầu vào/đầu ra cơ bản (đơn vị)

#### Trước (cũ)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Sau (lược đồ mới)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions#convenience-properties

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### Gọi hàm

Cấu trúc yêu cầu vẫn không thay đổi, nhưng phản hồi sẽ thay thế nội dung `outputs` dạng phẳng bằng các bước có cấu trúc.

#### Trước (cũ)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Sau (lược đồ mới)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Công cụ phía máy chủ

Các công cụ phía máy chủ (chẳng hạn như Google Tìm kiếm hoặc Thực thi mã) hiện tạo ra các loại bước cụ thể trong mảng `steps`. Mặc dù giản đồ cũ trả về các thao tác này dưới dạng các loại nội dung cụ thể trong mảng `outputs`, nhưng giản đồ mới sẽ di chuyển các thao tác này vào mảng `steps`. Các ví dụ sau đây sử dụng Google Tìm kiếm.

#### Trước (cũ)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Sau (lược đồ mới)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Phát trực tiếp

Tính năng phát trực tuyến cho thấy các loại sự kiện mới:

#### Loại sự kiện mới

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Loại sự kiện không còn được dùng

Các loại sự kiện cũ sau đây sẽ được thay thế bằng các sự kiện mới được liệt kê ở trên:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → được thay thế bằng `interaction.in_progress`, `interaction.requires_action`, v.v.

**Truyền trực tuyến lệnh gọi hàm**: Khi dùng tính năng truyền trực tuyến với lệnh gọi hàm, sự kiện `step.start` sẽ gửi tên hàm và các sự kiện `step.delta` sẽ truyền trực tuyến các đối số dưới dạng chuỗi JSON một phần (bằng cách dùng `arguments_delta`). Bạn phải tích luỹ các phần chênh lệch này để nhận được đầy đủ các đối số. Điều này khác với các lệnh gọi đơn nguyên, trong đó bạn nhận được toàn bộ đối tượng lệnh gọi hàm cùng một lúc.

#### Ví dụ

##### Trước (Cũ)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Sau (Giản đồ mới)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Lịch sử cuộc trò chuyện không trạng thái

Nếu quản lý nhật ký trò chuyện theo cách thủ công ở phía máy khách (trường hợp sử dụng không trạng thái), bạn phải cập nhật cách xâu chuỗi các lượt trước đó.

- **Cũ**: Nhà phát triển thường thu thập mảng `outputs` từ các phản hồi và gửi lại trong trường `input` ở lượt tiếp theo.
- **Lược đồ mới**: Giờ đây, bạn nên thu thập mảng `steps` từ phản hồi và truyền mảng đó vào trường `input` của yêu cầu tiếp theo, đồng thời thêm lượt tương tác mới của người dùng dưới dạng một bước `user_input`.

## Cấu hình định dạng đầu ra: Các thay đổi về `response_format`

API được cập nhật sẽ hợp nhất tất cả các chế độ kiểm soát định dạng đầu ra thành một trường `response_format` đa hình, hợp nhất. Điều này tập trung cấu hình đầu ra ở cấp cao nhất và giữ cho `generation_config` tập trung vào hành vi của mô hình (chẳng hạn như nhiệt độ, top\_p và suy nghĩ).

### Thay đổi quan trọng

- **API sẽ xoá `response_mime_type`.** Giờ đây, bạn chỉ định loại MIME cho mỗi mục định dạng bên trong `response_format`.
- **`response_format` hiện là một đối tượng (hoặc mảng) đa hình.** Mỗi mục nhập có một thuộc tính phân biệt `type` (`text`, `audio`, `image`) và các trường dành riêng cho từng loại. Để yêu cầu nhiều phương thức đầu ra, hãy truyền một mảng các mục nhập định dạng.
- **`image_config` di chuyển từ `generation_config` sang `response_format`.**
  Giờ đây, bạn có thể chỉ định các chế độ cài đặt đầu ra của hình ảnh như `aspect_ratio` và `image_size` trong mục `response_format` bằng `"type": "image"`.

### Đầu ra có cấu trúc (JSON)

Giản đồ mới sẽ xoá trường `response_mime_type`. Thay vào đó, hãy chỉ định loại MIME và giản đồ JSON bên trong một đối tượng `response_format` bằng `"type": "text"`.

#### Trước (cũ)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Sau (lược đồ mới)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Cấu hình hình ảnh

Giản đồ mới sẽ xoá `image_config` khỏi `generation_config`. Giờ đây, bạn chỉ định chế độ cài đặt đầu ra hình ảnh trong một mục `response_format` bằng `"type": "image"`.

#### Trước (cũ)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Sau (lược đồ mới)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

Để yêu cầu nhiều phương thức đầu ra (ví dụ: cả văn bản và âm thanh), hãy truyền một mảng các mục định dạng đến `response_format` thay vì một đối tượng duy nhất.

## Cách di chuyển sang giản đồ mới

### Người dùng SDK

Nâng cấp lên phiên bản SDK mới nhất (Python ≥2.0.0, JavaScript ≥2.0.0). SDK sẽ tự động chọn sử dụng giản đồ mới — không cần mã thay đổi ngoài việc cập nhật cách đọc phản hồi (xem ví dụ ở trên). Xin lưu ý rằng chỉ lược đồ mới được hỗ trợ trong các phiên bản SDK này. Các phiên bản SDK cũ (Python 1.x.x, JavaScript 1.x.x) sẽ tiếp tục hoạt động cho đến khi lược đồ cũ bị xoá vào **ngày 8 tháng 6 năm 2026**.

### Người dùng API REST

Thêm tiêu đề `Api-Revision: 2026-05-20` vào các yêu cầu của bạn để chọn sử dụng lược đồ mới ngay bây giờ. Sau **ngày 26 tháng 5**, giản đồ mới sẽ trở thành giản đồ mặc định cho tất cả các yêu cầu. Bạn có thể tạm thời chọn không sử dụng `Api-Revision: 2026-05-07` cho đến **ngày 8 tháng 6**. Sau ngày này, API sẽ xoá vĩnh viễn giản đồ cũ.

### Dòng thời gian

| Ngày | Pha ban đầu | Người dùng SDK | Người dùng API REST |
| --- | --- | --- | --- |
| **Ngày 7 tháng 5** | Chọn sử dụng | Đã có phiên bản SDK mới (Python ≥2.0.0, JS ≥2.0.0). Nâng cấp để tự động nhận giản đồ mới. | Thêm tiêu đề `Api-Revision: 2026-05-20` để chọn sử dụng. Giá trị mặc định vẫn là giá trị cũ. |
| **Ngày 26 tháng 5** | Lật mặc định | Bạn không cần làm gì nếu đã nâng cấp. Các SDK cũ (Python 1.x.x, JS 1.x.x) vẫn hoạt động nhưng trả về các phản hồi cũ. | Giờ đây, giản đồ mới là giản đồ mặc định. Gửi tiêu đề `Api-Revision: 2026-05-07` để chọn không sử dụng. |
| **Ngày 8 tháng 6** | Hoàng hôn | Các phiên bản SDK Python 1.x.x và JS 1.x.x sẽ bị lỗi đối với các lệnh gọi Interactions API. | Xoá giản đồ cũ cho Interactions API. Tiêu đề `Api-Revision` bị bỏ qua. |

## Danh sách kiểm tra di chuyển

### Lược đồ các bước (`steps`)

- Cập nhật mã để đọc nội dung phản hồi từ mảng `steps` thay vì `outputs`. [Xem ví dụ](#basic-unary).
- Xác minh rằng mã của bạn xử lý cả hai loại bước `user_input` và `model_output`. [Xem ví dụ](#basic-unary).
- (Gọi hàm) Cập nhật mã để tìm các bước `function_call` trong mảng `steps`. [Xem ví dụ](#function-calling).
- (Công cụ phía máy chủ) Cập nhật mã để xử lý các bước dành riêng cho công cụ (ví dụ: `google_search_call`, `google_search_result`). [Xem ví dụ](#server-side-tools).
- (Stateless History) Cập nhật tính năng quản lý nhật ký để truyền mảng `steps` trong trường `input` của yêu cầu tiếp theo. [Xem chi tiết](#stateless-history).
- (Chỉ truyền phát trực tiếp) Cập nhật ứng dụng để theo dõi các loại sự kiện SSE mới (`interaction.created`, `step.delta`, v.v.). [Xem ví dụ](#streaming).

### Cấu hình định dạng đầu ra (`response_format`)

- Thay thế `response_mime_type` bằng trường `mime_type` bên trong `response_format`. [Xem ví dụ](#structured-output).
- Bao bọc giản đồ JSON `response_format` hiện có bên trong một đối tượng `{"type": "text", "schema": ...}`. [Xem ví dụ](#structured-output).
- (Tạo hình ảnh) Di chuyển `image_config` từ `generation_config` sang một mục `{"type": "image", ...}` trong `response_format`. [Xem ví dụ](#image-config).
- (Đa phương thức) Chuyển đổi `response_format` từ một đối tượng thành một mảng khi yêu cầu nhiều phương thức đầu ra.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-01 UTC."],[],[]]
