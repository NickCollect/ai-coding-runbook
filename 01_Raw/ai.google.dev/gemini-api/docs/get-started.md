---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=vi
fetched_at: 2026-06-29T05:39:40.546843+00:00
title: "B\u1eaft \u0111\u1ea7u \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bắt đầu

Hướng dẫn này giúp bạn bắt đầu sử dụng Gemini API bằng [API Tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi). Bạn sẽ thực hiện lệnh gọi API đầu tiên trong vòng chưa đầy một phút và khám phá tính năng tạo văn bản, hiểu đa phương thức, tạo hình ảnh, đầu ra có cấu trúc, công cụ, gọi hàm, tác nhân và thực thi ở chế độ nền.

Bạn có thể sử dụng Interactions API thông qua SDK [Python](https://github.com/googleapis/python-genai) và [JavaScript](https://github.com/googleapis/js-genai), cũng như thông qua REST.

## 1. Lấy khoá API

Để sử dụng Gemini API, bạn cần có [khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi). Hãy tạo một khoá API miễn phí để bắt đầu:

[Tạo khoá Gemini API](https://aistudio.google.com/apikey?hl=vi)

Sau đó, hãy đặt khoá này làm biến môi trường:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

## 2. Cài đặt SDK và thực hiện lệnh gọi đầu tiên

Cài đặt SDK và tạo văn bản bằng một lệnh gọi API.

### Python

Cài đặt SDK:

```
pip install -U google-genai
```

Khởi chạy ứng dụng và đưa ra yêu cầu:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

Cài đặt SDK:

```
npm install @google/genai
```

Khởi chạy ứng dụng và đưa ra yêu cầu:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**Câu trả lời:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Khi sử dụng REST, API sẽ trả về tài nguyên `Interaction` đầy đủ chứa siêu dữ liệu, số liệu thống kê về mức sử dụng và nhật ký từng bước của lượt tương tác.

Mặc dù các SDK hiển thị toàn bộ câu trả lời, nhưng chúng cũng cung cấp các thuộc tính tiện lợi như `interaction.output_text` và `interaction.output_image` để truy cập trực tiếp vào đầu ra cuối cùng. Tìm hiểu thêm về cấu trúc câu trả lời trong phần [Tổng quan về tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hoặc đọc [hướng dẫn tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi) để biết thông tin chi tiết về hướng dẫn hệ thống và cấu hình tạo.

## 3. Truyền câu trả lời

Để có các lượt tương tác mượt mà hơn, hãy truyền câu trả lời khi câu trả lời được tạo. Mỗi sự kiện `step.delta` sẽ cung cấp một đoạn văn bản mà bạn có thể hiển thị ngay lập tức.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

Khi truyền, máy chủ sẽ phản hồi bằng một luồng sự kiện được gửi bởi máy chủ (SSE). Mỗi sự kiện bao gồm một loại và dữ liệu JSON.

**Câu trả lời:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

Để xem chi tiết về cách xử lý các sự kiện truyền và loại delta, hãy xem [hướng dẫn về các lượt tương tác truyền](https://ai.google.dev/gemini-api/docs/streaming?hl=vi).

## 4. Cuộc trò chuyện nhiều lượt

Interactions API hỗ trợ cuộc trò chuyện nhiều lượt theo 2 phương pháp:

- **Có trạng thái (nên dùng)**: Tiếp tục cuộc trò chuyện trên máy chủ bằng `previous_interaction_id`. Phù hợp với hầu hết các quy trình trò chuyện và tác nhân mà bạn muốn máy chủ quản lý nhật ký và tối ưu hoá việc lưu vào bộ nhớ đệm.
- **Không có trạng thái**: Quản lý lịch sử cuộc trò chuyện trên ứng dụng bằng cách truyền tất cả các lượt tương tác trước đó (bao gồm cả ý tưởng mô hình trung gian và các bước công cụ) trong mỗi yêu cầu.

### Có trạng thái (nên dùng)

Xâu chuỗi các lượt tương tác bằng cách truyền `previous_interaction_id`. Máy chủ sẽ quản lý toàn bộ nhật ký trò chuyện cho bạn.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### Không có trạng thái

Đặt `store=false` và quản lý nhật ký cuộc trò chuyện ở phía máy khách. Bạn phải giữ nguyên và gửi lại tất cả các bước do mô hình tạo (bao gồm cả các bước `thought` và `function_call`) chính xác như đã nhận.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**Câu trả lời:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

Lượt tương tác thứ hai trả về một đối tượng phản hồi hoàn chỉnh chỉ bao gồm các bước mới, nhưng dựa trên bối cảnh của lượt tương tác trước đó. Tìm hiểu thêm về cách duy trì trạng thái trong [hướng dẫn về cuộc trò chuyện nhiều lượt](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#multi-turn-conversations) hoặc khám phá [chế độ không có trạng thái](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#stateless-conversations) để quản lý nhật ký ở phía máy khách.

## 5. Hiểu đa phương thức

Các mô hình Gemini hiểu hình ảnh, âm thanh, video và tài liệu một cách tự nhiên. Truyền nội dung đa phương tiện cùng với văn bản trong một yêu cầu.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**Câu trả lời:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Khám phá cách truyền hình ảnh, video và tệp âm thanh trong [hướng dẫn hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi).

[hearing

Hiểu âm thanh

Chuyển lời nói thành văn bản, tóm tắt hoặc trả lời câu hỏi về tệp âm thanh.](https://ai.google.dev/gemini-api/docs/audio?hl=vi)
[videocam

Hiểu video

Phân tích nội dung video, xác định vị trí các sự kiện và mô tả hành động.](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi)
[description

Xử lý tài liệu

Trích xuất thông tin từ tệp PDF và các định dạng tài liệu khác.](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi)

## 6. Tạo đa phương thức

Gemini có thể tạo hình ảnh một cách tự nhiên bằng các mô hình tạo ảnh [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**Câu trả lời:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

Khi tạo hình ảnh, mô hình sẽ trả về dữ liệu hình ảnh được mã hoá base64 trong một bước trong mảng `steps`, cũng như thông qua thuộc tính tiện lợi `output_image`. Hãy xem [hướng dẫn tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) để tìm hiểu về tỷ lệ khung hình, chỉnh sửa hình ảnh và tài liệu tham khảo.

[record\_voice\_over

Tạo lời nói

Tạo lời nói biểu cảm, nhiều người nói bằng Gemini 3.1 Flash TTS.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi)
[music\_note

Tạo nhạc

Tạo đoạn nhạc và bài hát đầy đủ bằng Lyria 3.](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi)

## 7. Sử dụng đầu ra có cấu trúc

Định cấu hình mô hình để trả về JSON phù hợp với giản đồ mà bạn xác định. Đầu ra có cấu trúc hoạt động với [Pydantic](https://docs.pydantic.dev/latest/) (Python) và [Zod](https://zod.dev/) (JavaScript).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**Câu trả lời:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Khối văn bản đầu ra chứa một chuỗi JSON hợp lệ tuân thủ chính xác giản đồ được yêu cầu. Để tìm hiểu cách xác định các cấu trúc phức tạp hơn và giản đồ đệ quy, hãy xem [hướng dẫn về đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi).

## 8. Sử dụng công cụ

Dựa trên thông tin theo thời gian thực với Google Tìm kiếm để tạo câu trả lời cho mô hình. API sẽ tự động tìm kiếm, xử lý kết quả và trả về trích dẫn.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**Câu trả lời:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Các bước tìm kiếm được trình bày chi tiết trong nhật ký tương tác và đầu ra cuối cùng bao gồm các trích dẫn nội tuyến trỏ đến các nguồn trên web.

Bạn có thể tìm hiểu cách trích xuất trích dẫn tìm kiếm trong [hướng dẫn về cách dựa trên Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) hoặc xem cách kết hợp nhiều công cụ trong [hướng dẫn kết hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

[code

Thực thi mã

Chạy mã Python trong môi trường Borg hộp cát an toàn.](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)
[link

Bối cảnh URL

Truyền trực tiếp URL web công khai để dựa trên nội dung trang web để tạo câu trả lời.](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)
[search

Tìm tệp

Lập chỉ mục và tìm kiếm trên các tài liệu và tệp đa phương tiện đã tải lên.](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)
[map

Google Maps

Dựa trên dữ liệu vị trí và không gian địa lý trong thế giới thực để tạo câu trả lời.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)
[computer

Sử dụng máy tính

Tự động hoá trình duyệt và tương tác trên màn hình.](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)

## 9. Gọi hàm riêng của bạn

Tính năng gọi hàm cho phép bạn kết nối mô hình với mã của mình. Bạn khai báo tên và tham số của hàm, mô hình sẽ quyết định thời điểm gọi hàm đó và trả về các đối số có cấu trúc, đồng thời bạn sẽ thực thi hàm đó cục bộ và gửi kết quả trở lại.

### Có trạng thái (nên dùng)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Không có trạng thái

Bạn cũng có thể sử dụng tính năng gọi hàm ở chế độ không có trạng thái bằng cách quản lý nhật ký trò chuyện ở phía ứng dụng và đặt `store=false`. Ở chế độ không có trạng thái, bạn phải truyền toàn bộ nhật ký trò chuyện trong trường `input` của mỗi yêu cầu tiếp theo. Nhật ký này phải bao gồm:

1. Bước `user_input` ban đầu.
2. Tất cả các bước do mô hình tạo được trả về trong Lượt tương tác 1 (bao gồm cả các bước `thought` và `function_call`) chính xác như đã nhận.
3. Bước `function_result` chứa đầu ra của hàm đã thực thi.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**Câu trả lời:**

Trong Lượt tương tác 1, mô hình sẽ trả về câu trả lời có trạng thái `requires_action` và bước `function_call`:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

Sau khi bạn chạy hàm cục bộ và gửi kết quả (Lượt tương tác 2), lượt tương tác hoàn tất cuối cùng sẽ trả về:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Để biết các tính năng nâng cao như gọi hàm song song hoặc các chế độ lựa chọn hàm, hãy xem [hướng dẫn gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

## 10. Chạy tác nhân được quản lý

Các tác nhân được quản lý chạy trong một hộp cát từ xa có quyền truy cập vào các công cụ như thực thi mã và quản lý tệp. Truyền `agent` thay vì `model` và đặt `environment="remote"`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

Bạn cũng có thể xác định và lưu [các tác nhân tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi) bằng hướng dẫn, kỹ năng và nguồn dữ liệu của riêng mình.

[rocket\_launch

Bắt đầu nhanh

Thực hiện lệnh gọi tác nhân đầu tiên, truyền câu trả lời và tạo tác nhân tuỳ chỉnh.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi)
[smart\_toy

Tác nhân Antigravity

Chức năng, công cụ, dữ liệu đầu vào đa phương thức và giá cho tác nhân mặc định.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi)
[experiment

Tác nhân trong AI Studio

Sân chơi trực quan để tạo mẫu tác nhân mà không cần viết mã.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=vi)

## 11. Chạy các tác vụ ở chế độ nền

Đặt `background=True` để chạy các tác vụ dài hạn theo cách không đồng bộ. Thăm dò kết quả bằng `interactions.get()`. Để biết thêm thông tin chi tiết, hãy xem [Hướng dẫn thực thi ở chế độ nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**Câu trả lời:**

Câu trả lời ban đầu sẽ trả về ngay lập tức với trạng thái `in_progress`:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

Sau khi tác vụ ở chế độ nền được thực thi đầy đủ, việc kiểm tra trạng thái tương tác sẽ trả về:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

Đọc về cách chạy mô hình và tác nhân theo cách không đồng bộ trong [hướng dẫn thực thi ở chế độ nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi).

## Bước tiếp theo

- [Thực thi ở chế độ nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi): Chạy các tác vụ dài hạn theo cách không đồng bộ và quản lý trạng thái.
- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi): Hướng dẫn hệ thống, cấu hình tạo và các mẫu văn bản nâng cao.
- [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi): Tỷ lệ khung hình, chỉnh sửa hình ảnh và tài liệu tham khảo về kiểu.
- [Hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi): Phân loại, phát hiện đối tượng và hỏi đáp bằng hình ảnh.
- Thinking: The user wants to translate the source text while preserving the placeholder [and . The source text is "Thinking: Use chain-of-thought reasoning for complex tasks." The example translation is "Tư duy: Sử dụng phương pháp suy luận theo chuỗi tư duy cho các tác vụ phức tạp." The source text is similar to the example source, with the addition of placeholders around "Thinking". I need to translate the source text and include the placeholders in the correct positions. The translation of "Thinking" is "Tư duy". The rest of the sentence "Use chain-of-thought reasoning for complex tasks." translates to "Sử dụng phương pháp suy luận theo chuỗi tư duy cho các tác vụ phức tạp." I will combine the translated parts and include the placeholders.
  Tư duy: Sử dụng phương pháp suy luận theo chuỗi tư duy cho các tác vụ phức tạp.<ctrl95>Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi): Sử dụng phương pháp suy luận theo chuỗi tư duy cho các tác vụ phức tạp.
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi): Các chế độ hàm song song, kết hợp và bị hạn chế.
- [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi): Dựa trên, trích dẫn và đề xuất tìm kiếm.
- [Tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi): Các tác nhân được tạo sẵn có tính năng thực thi mã và quản lý tệp.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi): Nghiên cứu tự động nhiều bước có lập kế hoạch và tổng hợp.
- [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi): Giản đồ JSON, enum và định nghĩa loại đệ quy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-26 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-26 UTC."],[],[]]
