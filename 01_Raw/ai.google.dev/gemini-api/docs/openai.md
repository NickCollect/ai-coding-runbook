---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=th
fetched_at: 2026-09-28T06:19:49.044637+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e01\u0e31\u0e19\u0e44\u0e14\u0e49\u0e01\u0e31\u0e1a OpenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความเข้ากันได้กับ OpenAI

คุณเข้าถึงโมเดล Gemini ได้โดยใช้ไลบรารี OpenAI (Python และ TypeScript/
JavaScript) พร้อมกับ REST API โดยอัปเดตโค้ด 3 บรรทัด
และใช้[คีย์ Gemini API](https://aistudio.google.com/apikey?hl=th) หากยังไม่ได้ใช้ไลบรารี OpenAI เราขอแนะนำให้คุณเรียกใช้
[Gemini API โดยตรง](https://ai.google.dev/gemini-api/docs/get-started?hl=th)

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

สิ่งที่เปลี่ยนแปลง มีเพียง 3 บรรทัด

- **`api_key="GEMINI_API_KEY"`**: แทนที่ "`GEMINI_API_KEY`" ด้วยคีย์ Gemini
  API จริง ซึ่งคุณรับได้ใน [Google AI Studio](https://aistudio.google.com?hl=th)
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** นี่
  บอกให้ไลบรารี OpenAI ส่งคำขอไปยังปลายทาง Gemini API แทน
  URL เริ่มต้น
- **`model="gemini-3.6-flash"`**: เลือกโมเดล Gemini ที่เข้ากันได้

## การคิด

โมเดล Gemini ได้รับการฝึกให้คิดแก้ปัญหาที่ซับซ้อน ซึ่งนำไปสู่การใช้เหตุผลที่ดีขึ้นอย่างมาก Gemini API มาพร้อมกับ [พารามิเตอร์
การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)ที่ช่วยให้คุณควบคุมได้อย่างละเอียด
ว่าโมเดลจะคิดมากน้อยเพียงใด

โมเดล Gemini แต่ละโมเดลมีการกำหนดค่าการใช้เหตุผลที่แตกต่างกัน คุณสามารถดูวิธีที่โมเดลเหล่านี้แมปกับการใช้เหตุผลของ OpenAI ได้ดังนี้

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

หากไม่ได้ระบุ `reasoning_effort` ไว้ Gemini จะใช้
ระดับ [เริ่มต้น](https://ai.google.dev/gemini-api/docs/thinking?hl=th#levels) หรืองบประมาณ [ของโมเดล](https://ai.google.dev/gemini-api/docs/thinking?hl=th#set-budget)

หากต้องการปิดใช้การคิด คุณสามารถตั้งค่า `reasoning_effort` เป็น `"none"` สำหรับ
โมเดล 2.5 คุณจะปิดการใช้เหตุผลสำหรับโมเดล Gemini 2.5 Pro หรือ 3 ไม่ได้

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

โมเดลการคิดของ Gemini ยังสร้าง[สรุปความคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#summaries)ด้วย
คุณสามารถใช้ช่อง [`extra_body`](#extra-body) เพื่อรวมช่อง Gemini ไว้ในคำขอ

โปรดทราบว่า `reasoning_effort` และ `thinking_level`/`thinking_budget` มีฟังก์ชันการทำงานที่ทับซ้อนกัน จึงใช้พร้อมกันไม่ได้

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
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

Gemini 3 รองรับความเข้ากันได้กับ OpenAI สำหรับลายเซ็นความคิดใน Chat Completion API คุณดูตัวอย่างทั้งหมดได้ในหน้า[ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th#openai)

## สตรีมมิง

Gemini API รองรับ[การสตรีมมิงคำตอบ](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=th#generate-a-text-stream)

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## การเรียกใช้ฟังก์ชัน

การเรียกใช้ฟังก์ชันช่วยให้คุณรับเอาต์พุตข้อมูลที่มีโครงสร้างจาก
โมเดล Generative ได้ง่ายขึ้น และ [Gemini API รองรับฟีเจอร์นี้](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=th)

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
  model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  "model": "gemini-3.6-flash",
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

## การทำความเข้าใจรูปภาพ

โมเดล Gemini เป็นโมเดลมัลติโมดัลโดยกำเนิดและมีประสิทธิภาพดีที่สุดใน
[งานด้านวิชันซิสติกส์ทั่วไปหลายอย่าง](https://ai.google.dev/gemini-api/docs/vision?hl=th)

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
  model="gemini-3.6-flash",
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
      model: "gemini-3.6-flash",
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
      \"model\": \"gemini-3.6-flash\",
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

## สร้างรูปภาพ

สร้างรูปภาพโดยใช้ `gemini-2.5-flash-image` หรือ `gemini-3-pro-image-preview` พารามิเตอร์ที่รองรับ ได้แก่ `prompt`, `model`, `n`, `size`, และ `response_format` ระบบจะละเว้นพารามิเตอร์อื่นๆ ที่ไม่ได้ระบุไว้ที่นี่หรือในส่วน [`extra_body`](#extra-body) โดยไม่มีการแจ้งเตือน

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

## สร้างวิดีโอ

สร้างวิดีโอโดยใช้ `veo-3.1-generate-preview` ผ่านปลายทาง `/v1/videos` ที่เข้ากันได้กับ Sora พารามิเตอร์ระดับบนสุดที่รองรับคือ `prompt` และ `model` คุณต้องส่งพารามิเตอร์เพิ่มเติม เช่น `duration_seconds`, `image` และ `aspect_ratio` พร้อมกับ `extra_body` ดูพารามิเตอร์ทั้งหมดที่ใช้ได้ในส่วน [`extra_body`](#extra-body)

การสร้างวิดีโอเป็นการดำเนินการที่ใช้เวลานาน ซึ่งจะแสดงผลรหัสการดำเนินการที่คุณสามารถโพลเพื่อตรวจสอบสถานะการดำเนินการได้

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

### ตรวจสอบสถานะวิดีโอ

การสร้างวิดีโอเป็นการดำเนินการแบบอะซิงโครนัส ใช้ `GET /v1/videos/{id}` เพื่อโพลสถานะและดึงข้อมูล URL วิดีโอสุดท้ายเมื่อเสร็จสมบูรณ์

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

## การทำความเข้าใจเสียง

วิเคราะห์อินพุตเสียง

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
      \"model\": \"gemini-3.6-flash\",
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

## เอาต์พุตที่มีโครงสร้าง

โมเดล Gemini สามารถแสดงผลออบเจ็กต์ JSON ใน[โครงสร้างใดก็ได้ที่คุณกำหนด](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## การฝัง

การฝังข้อความจะวัดความเกี่ยวข้องของสตริงข้อความและสร้างได้
โดยใช้ [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=th) คุณสามารถใช้ `gemini-embedding-2-preview` สำหรับการฝังมัลติโมดัล หรือ `gemini-embedding-001` สำหรับการฝังข้อความเท่านั้น

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

คุณสามารถสร้าง[งานแบบกลุ่ม](https://ai.google.dev/gemini-api/docs/batch-mode?hl=th) ส่งงาน และตรวจสอบ
สถานะของงานได้โดยใช้ไลบรารี OpenAI

คุณจะต้องเตรียมไฟล์ JSONL ในรูปแบบอินพุตของ OpenAI เช่น

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.6-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.6-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

ความเข้ากันได้กับ OpenAI สำหรับ Batch รองรับการสร้างกลุ่ม การตรวจสอบสถานะงาน และการดูผลลัพธ์แบบกลุ่ม

ปัจจุบันระบบยังไม่รองรับความเข้ากันได้สำหรับการอัปโหลดและดาวน์โหลด ตัวอย่างต่อไปนี้จึงใช้ไคลเอ็นต์ `genai` สำหรับการอัปโหลดและดาวน์โหลด
[ไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th) ซึ่งเป็นวิธีเดียวกับที่ใช้เมื่อใช้ Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=th#input-file)

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

OpenAI SDK ยังรองรับ[การสร้างการฝังด้วย Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embeddings) ด้วย หากต้องการทำเช่นนั้น ให้เปลี่ยนช่อง `endpoint` ของเมธอด `create` เป็นปลายทางการฝัง รวมถึงคีย์ `url` และ `model` ในไฟล์ JSONL

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

ดูตัวอย่างฉบับเต็มได้ในส่วน[การสร้างการฝังแบบกลุ่ม](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)
ของคู่มือความเข้ากันได้กับ OpenAI

## Flex และ Priority Inference

Gemini API ตรงกับพารามิเตอร์ `service_tier` ของ OpenAI ในชื่อและตรรกะ โดยบังคับใช้ขีดจำกัดและกำหนดเส้นทางการรับส่งข้อมูลอย่างเหมาะสมสำหรับทั้งระดับ Flex และ Priority Inference

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.6-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

เมื่อไม่ได้กำหนดไว้อย่างชัดเจน `service_tier` จะใช้ `standard` เป็นค่าเริ่มต้น ซึ่งเทียบเท่ากับ `default` สำหรับ OpenAI
ดูข้อมูลเพิ่มเติมเกี่ยวกับระดับ Inference ได้ในเอกสารประกอบการ[เพิ่มประสิทธิภาพ](https://ai.google.dev/gemini-api/docs/optimization?hl=th)

## เปิดใช้ฟีเจอร์ Gemini ด้วย `extra_body`

Gemini รองรับฟีเจอร์หลายอย่างที่โมเดล OpenAI ไม่มี แต่คุณสามารถเปิดใช้ได้โดยใช้ช่อง `extra_body`

| พารามิเตอร์ | ประเภท | ปลายทาง | คำอธิบาย |
| --- | --- | --- | --- |
| **`cached_content`** | ข้อความ | แชท | สอดคล้องกับแคชเนื้อหาทั่วไปของ Gemini |
| **`thinking_config`** | วัตถุ | แชท | สอดคล้องกับ ThinkingConfig ของ Gemini |
| **`aspect_ratio`** | ข้อความ | รูปภาพ | สัดส่วนภาพเอาต์พุต (เช่น `"16:9"`, `"1:1"`, `"9:16"`) |
| **`generation_config`** | วัตถุ | รูปภาพ | ออบเจ็กต์การกำหนดค่าการสร้างของ Gemini (เช่น `{"responseModalities": ["IMAGE"], "candidateCount": 2}`) |
| **`safety_settings`** | รายการ | รูปภาพ | ตัวกรองเกณฑ์ความปลอดภัยที่กำหนดเอง (เช่น `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`) |
| **`tools`** | รายการ | รูปภาพ | เปิดใช้การอ้างอิง (เช่น `[{"google_search": {}}]`) สำหรับ `gemini-3-pro-image-preview` เท่านั้น |
| **`aspect_ratio`** | ข้อความ | วิดีโอ | ขนาดของวิดีโอเอาต์พุต (`16:9` สำหรับแนวนอน, `9:16` สำหรับแนวตั้ง) แมปจาก `size` หากไม่ได้ระบุไว้ |
| **`resolution`** | ข้อความ | วิดีโอ | ความละเอียดเอาต์พุต (`720p`, `1080p`, `4K`) หมายเหตุ: `1080p` และ `4K` จะทริกเกอร์ไปป์ไลน์การเพิ่มขนาด |
| **`duration_seconds`** | จำนวนเต็ม | วิดีโอ | ความยาวการสร้าง (ค่า: `4`, `6`, `8`) ต้องเป็น `8` เมื่อใช้ `reference_images`, การประมาณค่า หรือส่วนขยาย |
| **`frame_rate`** | ข้อความ | วิดีโอ | อัตราเฟรมสำหรับเอาต์พุตวิดีโอ (เช่น `"24"`) |
| **`input_reference`** | ข้อความ | วิดีโอ | อินพุตอ้างอิงสำหรับการสร้างวิดีโอ |
| **`extend_video_id`** | ข้อความ | วิดีโอ | รหัสของวิดีโอที่มีอยู่เพื่อขยาย |
| **`negative_prompt`** | ข้อความ | วิดีโอ | รายการที่จะยกเว้น (เช่น `"shaky camera"`) |
| **`seed`** | จำนวนเต็ม | วิดีโอ | จำนวนเต็มสำหรับการสร้างแบบดีเทอร์มินิสติก |
| **`style`** | ข้อความ | วิดีโอ | การจัดสไตล์ภาพ (`cinematic` เป็นค่าเริ่มต้น, `creative` สำหรับการเพิ่มประสิทธิภาพโซเชียลมีเดีย) |
| **`person_generation`** | ข้อความ | วิดีโอ | ควบคุมการสร้างบุคคล (`allow_adult`, `allow_all`, `dont_allow`) |
| **`reference_images`** | รายการ | วิดีโอ | รูปภาพสูงสุด 3 รูปสำหรับการอ้างอิงสไตล์/ตัวละคร (ชิ้นงาน Base64) |
| **`image`** | ข้อความ | วิดีโอ | รูปภาพอินพุตเริ่มต้นที่เข้ารหัส Base64 เพื่อกำหนดเงื่อนไขการสร้างวิดีโอ |
| **`last_frame`** | วัตถุ | วิดีโอ | รูปภาพสุดท้ายสำหรับการประมาณค่า (ต้องมี `image` เป็นเฟรมแรก) |

### ตัวอย่างการใช้ `extra_body`

ตัวอย่างการใช้ `extra_body` เพื่อตั้งค่า `cached_content`

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.6-flash",
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

## แสดงรายการโมเดล

รับรายการโมเดล Gemini ที่พร้อมใช้งาน

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

## ดึงข้อมูลโมเดล

ดึงข้อมูลโมเดล Gemini

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.6-flash")
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
  const model = await openai.models.retrieve("gemini-3.6-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.6-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## ข้อจำกัดปัจจุบัน

การรองรับไลบรารี OpenAI ยังอยู่ในเวอร์ชันเบต้าในขณะที่เราขยายการรองรับฟีเจอร์

หากมีคำถามเกี่ยวกับพารามิเตอร์ที่รองรับ ฟีเจอร์ที่จะเปิดตัว หรือพบปัญหาในการเริ่มต้นใช้งาน Gemini โปรดเข้าร่วม
ฟอรัมนักพัฒนาแอป

## ขั้นตอนถัดไป

ลองใช้ [Colab ความเข้ากันได้กับ OpenAI](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=th) เพื่อดูตัวอย่างโดยละเอียดเพิ่มเติม

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-12 UTC"],[],[]]
