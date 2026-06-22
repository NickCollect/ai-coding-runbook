---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=vi
fetched_at: 2026-06-22T06:25:54.825258+00:00
title: "Kh\u1ea3 n\u0103ng t\u01b0\u01a1ng th\u00edch v\u1edbi OpenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Khả năng tương thích với OpenAI

Bạn có thể truy cập vào các mô hình Gemini bằng cách sử dụng các thư viện OpenAI (Python và TypeScript/Javascript) cùng với API REST, bằng cách cập nhật 3 dòng mã và sử dụng [khoá Gemini API](https://aistudio.google.com/apikey?hl=vi). Nếu chưa sử dụng thư viện OpenAI, bạn nên gọi [Gemini API trực tiếp](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Điều gì đã thay đổi? Chỉ có 3 dòng!

- **`api_key="GEMINI_API_KEY"`**: Thay thế "`GEMINI_API_KEY`" bằng khoá Gemini API thực tế của bạn. Bạn có thể lấy khoá này trong [Google AI Studio](https://aistudio.google.com?hl=vi).
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** Lệnh này yêu cầu thư viện OpenAI gửi các yêu cầu đến điểm cuối Gemini API thay vì URL mặc định.
- **`model="gemini-3.5-flash"`**: Chọn một mô hình Gemini tương thích

## Tư duy

Các mô hình Gemini được huấn luyện để suy nghĩ thấu đáo về những vấn đề phức tạp, từ đó cải thiện đáng kể khả năng suy luận. Gemini API đi kèm với [các tham số tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) giúp bạn kiểm soát chi tiết mức độ tư duy của mô hình.

Các mô hình Gemini khác nhau có cấu hình suy luận khác nhau. Bạn có thể xem cách các mô hình này tương ứng với nỗ lực suy luận của OpenAI như sau:

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

Nếu bạn không chỉ định `reasoning_effort`, Gemini sẽ sử dụng [cấp](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#levels) hoặc [ngân sách](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#set-budget) mặc định của mô hình.

Nếu muốn tắt tính năng tư duy, bạn có thể đặt `reasoning_effort` thành `"none"` cho các mô hình 2.5. Bạn không thể tắt tính năng suy luận cho các mô hình Gemini 2.5 Pro hoặc 3.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    reasoning_effort: "low",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Các mô hình tư duy của Gemini cũng tạo ra [bản tóm tắt suy nghĩ](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#summaries).
Bạn có thể sử dụng trường [`extra_body`](#extra-body) để đưa các trường Gemini vào yêu cầu của mình.

Xin lưu ý rằng `reasoning_effort` và `thinking_level`/`thinking_budget` có chức năng trùng lặp, nên bạn không thể sử dụng chúng cùng một lúc.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": "Explain to me how AI works"}],
    extra_body={
      'extra_body': {
        "google": {
          "thinking_config": {
            "thinking_level": "low",
            "include_thoughts": True
          }
        }
      }
    }
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [{role: "user", content: "Explain to me how AI works",}],
    extra_body: {
      "google": {
        "thinking_config": {
          "thinking_level": "low",
          "include_thoughts": true
        }
      }
    }
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
        "messages": [{"role": "user", "content": "Explain to me how AI works"}],
        "extra_body": {
          "google": {
            "thinking_config": {
              "thinking_level": "low",
              "include_thoughts": true
            }
          }
        }
      }'
```

Gemini 3 hỗ trợ khả năng tương thích với OpenAI cho chữ ký tư duy trong các API hoàn thành cuộc trò chuyện. Bạn có thể xem ví dụ đầy đủ trên trang [chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=vi#openai).

## Phát trực tiếp

Gemini API hỗ trợ [truyền trực tuyến câu trả lời](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=vi#generate-a-text-stream).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {   "role": "user",
        "content": "Hello!"
    }
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
          "role": "system",
          "content": "You are a helpful assistant."
      },
      {
          "role": "user",
          "content": "Hello!"
      }
    ],
    stream: true,
  });

  for await (const chunk of completion) {
    console.log(chunk.choices[0].delta.content);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## Gọi hàm

Tính năng gọi hàm giúp bạn dễ dàng nhận được dữ liệu có cấu trúc từ các mô hình tạo sinh và được [hỗ trợ trong Gemini API](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=vi).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}]
response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}];
  const tools = [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. Chicago, IL",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
          },
        }
      }
  ];

  const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: messages,
    tools: tools,
    tool_choice: "auto",
  });

  console.log(response);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Chicago today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. Chicago, IL"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

## Hiểu hình ảnh

Các mô hình Gemini có khả năng đa phương thức tự nhiên và mang lại hiệu suất tốt nhất trong số các mô hình cùng loại đối với [nhiều tác vụ thị giác phổ biến](https://ai.google.dev/gemini-api/docs/vision?hl=vi).

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

### JavaScript

```
import OpenAI from "openai";
import fs from 'fs/promises';

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function encodeImage(imagePath) {
  try {
    const imageBuffer = await fs.readFile(imagePath);
    return imageBuffer.toString('base64');
  } catch (error) {
    console.error("Error encoding image:", error);
    return null;
  }
}

async function main() {
  const imagePath = "Path/to/agi/image.jpeg";
  const base64Image = await encodeImage(imagePath);

  const messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": `data:image/jpeg;base64,${base64Image}`
          },
        },
      ],
    }
  ];

  try {
    const response = await openai.chat.completions.create({
      model: "gemini-3.5-flash",
      messages: messages,
    });

    console.log(response.choices[0]);
  } catch (error) {
    console.error("Error calling Gemini API:", error);
  }
}

main();
```

### REST

```
bash -c '
  base64_image=$(base64 -i "Path/to/agi/image.jpeg");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"What is in this image?\" },
            {
              \"type\": \"image_url\",
              \"image_url\": { \"url\": \"data:image/jpeg;base64,${base64_image}\" }
            }
          ]
        }
      ]
    }"
'
```

## Tạo một hình ảnh

Tạo hình ảnh bằng `gemini-2.5-flash-image` hoặc `gemini-3-pro-image-preview`. Các thông số được hỗ trợ bao gồm `prompt`, `model`, `n`, `size` và `response_format`. Mọi thông số khác không có trong danh sách này hoặc trong phần [`extra_body`](#extra-body) sẽ bị lớp tương thích bỏ qua một cách âm thầm.

### Python

```
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="a portrait of a sheepadoodle wearing a cape",
    response_format='b64_json',
    n=1,
)

for image_data in response.data:
  image = Image.open(BytesIO(base64.b64decode(image_data.b64_json)))
  image.show()
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const image = await openai.images.generate(
    {
      model: "gemini-2.5-flash-image",
      prompt: "a portrait of a sheepadoodle wearing a cape",
      response_format: "b64_json",
      n: 1,
    }
  );

  console.log(image.data);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
        "model": "gemini-2.5-flash-image",
        "prompt": "a portrait of a sheepadoodle wearing a cape",
        "response_format": "b64_json",
        "n": 1,
      }'
```

## Tạo video

Tạo video bằng `veo-3.1-generate-preview` thông qua điểm cuối `/v1/videos` tương thích với Sora. Các tham số cấp cao nhất được hỗ trợ là `prompt` và `model`. Bạn phải truyền các tham số bổ sung như `duration_seconds`, `image` và `aspect_ratio` bằng `extra_body`. Xem phần [`extra_body`](#extra-body) để biết tất cả các tham số có sẵn.

Tạo video là một thao tác thực hiện lâu và trả về một mã thao tác mà bạn có thể thăm dò để biết trạng thái hoàn tất.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Returns a Long Running Operation (status: processing)
response = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="A cinematic drone shot of a waterfall",
)

print(f"Operation ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Returns a Long Running Operation (status: processing)
    const response = await openai.videos.create({
        model: "veo-3.1-generate-preview",
        prompt: "A cinematic drone shot of a waterfall",
    });

    console.log(`Operation ID: ${response.id}`);
    console.log(`Status: ${response.status}`);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=A cinematic drone shot of a waterfall"
```

### Kiểm tra trạng thái video

Quá trình tạo video diễn ra không đồng bộ. Sử dụng `GET /v1/videos/{id}` để thăm dò trạng thái và truy xuất URL cuối cùng của video khi hoàn tất:

### Python

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Poll until video is ready
video_id = response.id  # From the create call
while True:
    video = client.videos.retrieve(video_id)
    if video.status == "completed":
        print(f"Video URL: {video.url}")
        break
    elif video.status == "failed":
        print(f"Generation failed: {video.error}")
        break
    print(f"Status: {video.status}. Waiting...")
    time.sleep(10)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Poll until video is ready
    const videoId = response.id;  // From the create call
    while (true) {
        const video = await openai.videos.retrieve(videoId);
        if (video.status === "completed") {
            console.log(`Video URL: ${video.url}`);
            break;
        } else if (video.status === "failed") {
            console.log(`Generation failed: ${video.error}`);
            break;
        }
        console.log(`Status: ${video.status}. Waiting...`);
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos/VIDEO_ID" \
  -H "Authorization: Bearer $GEMINI_API_KEY"
```

## Hiểu được âm thanh

Phân tích đầu vào âm thanh:

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("/path/to/your/audio/file.wav", "rb") as audio_file:
  base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio",
        },
        {
              "type": "input_audio",
              "input_audio": {
                "data": base64_audio,
                "format": "wav"
          }
        }
      ],
    }
  ],
)

print(response.choices[0].message.content)
```

### JavaScript

```
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

const audioFile = fs.readFileSync("/path/to/your/audio/file.wav");
const base64Audio = Buffer.from(audioFile).toString("base64");

async function main() {
  const response = await client.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Transcribe this audio",
          },
          {
            type: "input_audio",
            input_audio: {
              data: base64Audio,
              format: "wav",
            },
          },
        ],
      },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### REST

```
bash -c '
  base64_audio=$(base64 -i "/path/to/your/audio/file.wav");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"Transcribe this audio file.\" },
            {
              \"type\": \"input_audio\",
              \"input_audio\": {
                \"data\": \"${base64_audio}\",
                \"format\": \"wav\"
              }
            }
          ]
        }
      ]
    }"
'
```

## Đầu ra có cấu trúc

Các mô hình Gemini có thể xuất các đối tượng JSON theo [cấu trúc mà bạn xác định](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi).

### Python

```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### JavaScript

```
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai"
});

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.chat.completions.parse({
  model: "gemini-3.5-flash",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## Mục nhúng

Vectơ nhúng văn bản đo lường mức độ liên quan của các chuỗi văn bản và có thể được tạo bằng [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi). Bạn có thể dùng `gemini-embedding-2-preview` cho các mục nhúng đa phương thức hoặc `gemini-embedding-001` cho các mục nhúng chỉ có văn bản.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="gemini-embedding-2-preview"
)

print(response.data[0].embedding)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const embedding = await openai.embeddings.create({
    model: "gemini-embedding-2-preview",
    input: "Your text string goes here",
  });

  console.log(embedding);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/embeddings" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
    "input": "Your text string goes here",
    "model": "gemini-embedding-2-preview"
  }'
```

## Batch API

Bạn có thể tạo [công việc hàng loạt](https://ai.google.dev/gemini-api/docs/batch-mode?hl=vi), gửi công việc và kiểm tra trạng thái của công việc bằng thư viện OpenAI.

Bạn sẽ cần chuẩn bị tệp JSONL ở định dạng đầu vào của OpenAI. Ví dụ:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Khả năng tương thích với OpenAI cho Batch hỗ trợ việc tạo một lô, giám sát trạng thái công việc và xem kết quả lô.

Hiện tại, chúng tôi chưa hỗ trợ khả năng tương thích cho việc tải lên và tải xuống. Thay vào đó, ví dụ sau đây sử dụng ứng dụng `genai` để tải lên và tải xuống [tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi), giống như khi sử dụng [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=vi#input-file) của Gemini.

### Python

```
from openai import OpenAI

# Regular genai client for uploads & downloads
from google import genai
client = genai.Client()

openai_client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Upload the JSONL file in OpenAI input format, using regular genai SDK
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

# Create batch
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Wait for batch to finish (up to 24h)
while True:
    batch = client.batches.retrieve(batch.id)
    if batch.status in ('completed', 'failed', 'cancelled', 'expired'):
        break
    print(f"Batch not finished. Current state: {batch.status}. Waiting 30 seconds...")
    time.sleep(30)
print(f"Batch finished: {batch}")

# Download results in OpenAI output format, using regular genai SDK
file_content = genai_client.files.download(file=batch.output_file_id).decode('utf-8')

# See batch_output JSONL in OpenAI output format
for line in file_content.splitlines():
    print(line)
```

SDK OpenAI cũng hỗ trợ [tạo các mục nhúng bằng Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi#batch-embeddings). Để thực hiện việc này, hãy thay đổi trường `endpoint` của phương thức `create` thành một điểm cuối nhúng, cũng như các khoá `url` và `model` trong tệp JSONL:

```
# JSONL file using embeddings model and endpoint
# {"custom_id": "request-1", "method": "POST", "url": "/v1/embeddings", "body": {"model": "ggemini-embedding-001", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
# {"custom_id": "request-2", "method": "POST", "url": "/v1/embeddings", "body": {"model": "gemini-embedding-001", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}

# ...

# Create batch step with embeddings endpoint
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/embeddings",
    completion_window="24h"
)
```

Hãy xem phần [Tạo nhiều vectơ nhúng cùng lúc](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb) trong sổ tay tương thích của OpenAI để biết ví dụ hoàn chỉnh.

## Suy luận linh hoạt và ưu tiên

API Gemini có tên và logic tương ứng với tham số `service_tier` của OpenAI, đồng thời thực thi các giới hạn và chuyển hướng lưu lượng truy cập một cách hiệu quả cho cả các cấp suy luận Linh hoạt và Ưu tiên.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

Khi không được chỉ định rõ ràng, `service_tier` sẽ mặc định là `standard`, tương đương với `default` đối với OpenAI.
Tìm hiểu thêm về các cấp suy luận trong tài liệu [Tối ưu hoá](https://ai.google.dev/gemini-api/docs/optimization?hl=vi).

## Bật các tính năng của Gemini bằng `extra_body`

Có một số tính năng được Gemini hỗ trợ nhưng không có trong các mô hình OpenAI. Tuy nhiên, bạn có thể bật các tính năng này bằng cách sử dụng trường `extra_body`.

| Tham số | Loại | Điểm cuối | Mô tả |
| --- | --- | --- | --- |
| **`cached_content`** | Văn bản | Trò chuyện | Tương ứng với bộ nhớ đệm nội dung chung của Gemini. |
| **`thinking_config`** | Đối tượng | Trò chuyện | Tương ứng với ThinkingConfig của Gemini. |
| **`aspect_ratio`** | Văn bản | Hình ảnh | Tỷ lệ khung hình đầu ra (ví dụ: `"16:9"`, `"1:1"`, `"9:16"`). |
| **`generation_config`** | Đối tượng | Hình ảnh | Đối tượng cấu hình tạo của Gemini (ví dụ: `{"responseModalities": ["IMAGE"], "candidateCount": 2}`). |
| **`safety_settings`** | Danh sách | Hình ảnh | Bộ lọc ngưỡng an toàn tuỳ chỉnh (ví dụ: `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`). |
| **`tools`** | Danh sách | Hình ảnh | Cho phép căn cứ (ví dụ: `[{"google_search": {}}]`). Chỉ dành cho `gemini-3-pro-image-preview`. |
| **`aspect_ratio`** | Văn bản | Video | Kích thước của video đầu ra (`16:9` cho chế độ ngang, `9:16` cho chế độ dọc). Bản đồ từ `size` nếu không được chỉ định. |
| **`resolution`** | Văn bản | Video | Độ phân giải đầu ra (`720p`, `1080p`, `4K`). Lưu ý: `1080p` và `4K` kích hoạt quy trình tăng độ phân giải. |
| **`duration_seconds`** | Số nguyên | Video | Độ dài của thế hệ (giá trị: `4`, `6`, `8`). Phải là `8` khi sử dụng `reference_images`, nội suy hoặc phần mở rộng. |
| **`frame_rate`** | Văn bản | Video | Tốc độ khung hình cho video đầu ra (ví dụ: `"24"`). |
| **`input_reference`** | Văn bản | Video | Đầu vào tham chiếu để tạo video. |
| **`extend_video_id`** | Văn bản | Video | Mã nhận dạng của video hiện có cần mở rộng. |
| **`negative_prompt`** | Văn bản | Video | Các mục cần loại trừ (ví dụ: `"shaky camera"`). |
| **`seed`** | Số nguyên | Video | Số nguyên để tạo một cách xác định. |
| **`style`** | Văn bản | Video | Kiểu hiển thị (`cinematic` mặc định, `creative` được tối ưu hoá cho mạng xã hội). |
| **`person_generation`** | Văn bản | Video | Kiểm soát việc tạo hình ảnh về con người (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | Danh sách | Video | Tối đa 3 hình ảnh tham khảo về phong cách/nhân vật (thành phần base64). |
| **`image`** | Văn bản | Video | Hình ảnh đầu vào ban đầu được mã hoá Base64 để điều kiện hoá quá trình tạo video. |
| **`last_frame`** | Đối tượng | Video | Hình ảnh cuối cùng để nội suy (yêu cầu `image` làm khung hình đầu tiên). |

### Ví dụ sử dụng `extra_body`

Sau đây là một ví dụ về cách dùng `extra_body` để đặt `cached_content`:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.5-flash",
    n=1,
    messages=[
        {
            "role": "user",
            "content": "Summarize the video"
        }
    ],
    stream=True,
    stream_options={'include_usage': True},
    extra_body={
        'extra_body':
        {
            'google': {
              'cached_content': "cachedContents/0000aaaa1111bbbb2222cccc3333dddd4444eeee"
          }
        }
    }
)

for chunk in stream:
    print(chunk)
    print(chunk.usage.to_dict())
```

## Liệt kê các mô hình

Xem danh sách các mô hình Gemini hiện có:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

models = client.models.list()
for model in models:
  print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## Truy xuất một mô hình

Truy xuất mô hình Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.5-flash")
print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3.5-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.5-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## Các điểm hạn chế hiện tại

Chúng tôi vẫn đang trong giai đoạn thử nghiệm đối với các thư viện OpenAI trong khi mở rộng phạm vi hỗ trợ tính năng.

Nếu bạn có thắc mắc về các tham số được hỗ trợ, các tính năng sắp ra mắt hoặc gặp phải bất kỳ vấn đề nào khi bắt đầu sử dụng Gemini, hãy tham gia [Diễn đàn dành cho nhà phát triển](https://discuss.ai.google.dev/c/gemini-api/4?hl=vi) của chúng tôi.

## Bước tiếp theo

Hãy thử [Colab tương thích với OpenAI](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=vi) của chúng tôi để xem các ví dụ chi tiết hơn.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-19 UTC."],[],[]]
