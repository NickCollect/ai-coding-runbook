---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=th
fetched_at: 2026-09-14T05:44:24.622315+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน

คู่มือนี้จะช่วยให้คุณเริ่มต้นใช้งาน Gemini API โดยใช้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) คุณจะทำการเรียก API ครั้งแรกได้ภายในไม่ถึงนาที และสำรวจการสร้างข้อความ ความเข้าใจแบบหลายรูปแบบ การสร้างรูปภาพ เอาต์พุตที่มีโครงสร้าง เครื่องมือ การเรียกใช้ฟังก์ชัน Agent และการดำเนินการในเบื้องหลัง

Interactions API พร้อมใช้งานผ่าน SDK ของ [Python](https://github.com/googleapis/python-genai) และ [JavaScript](https://github.com/googleapis/js-genai) รวมถึงผ่าน REST

## 1. รับคีย์ API

หากต้องการใช้ Gemini API คุณต้องมีคีย์ API เพื่อตรวจสอบสิทธิ์คำขอ บังคับใช้ขีดจำกัดด้านความปลอดภัย และติดตามการใช้งานในบัญชี

- Google AI Studio จะสร้างโปรเจ็กต์และคีย์ API ให้กับผู้ใช้ใหม่โดยอัตโนมัติ
  คุณคัดลอกได้จาก[หน้าคีย์ API](https://aistudio.google.com/api-keys?hl=th)
- หากต้องการคีย์ใหม่ ให้คลิก**สร้างคีย์ API** ใน AI Studio แล้วทำตาม
  กล่องโต้ตอบเพื่อเพิ่มคู่คีย์-โปรเจ็กต์ใหม่

[สร้างคีย์ Gemini API](https://aistudio.google.com/apikey?hl=th)

ตั้งค่าคีย์เป็นตัวแปรสภาพแวดล้อม

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### อัปเกรดเป็นระดับแบบชำระเงิน

การอัปเกรดเป็นระดับแบบชำระเงินจะเพิ่มการจำกัดอัตราคำขอและต้องตั้งค่าการเรียกเก็บเงินใน Cloud

- คลิก**ตั้งค่าการเรียกเก็บเงิน**ในหน้า[คีย์ API](https://aistudio.google.com/api-keys?hl=th) หรือ[โปรเจ็กต์](https://aistudio.google.com/projects?hl=th)ของ AI Studio
- ทำตามกล่องโต้ตอบการเรียกเก็บเงินใน Cloud เพื่อสร้างหรือลิงก์บัญชีสำหรับการเรียกเก็บเงิน เพิ่ม
  วิธีการชำระเงิน และชำระเงินล่วงหน้าอย่างน้อย $10 (หรือเทียบเท่าในสกุลเงินอื่น) ใน
  เครดิตที่ชำระเงินแล้ว
- ดูการใช้งาน API ใน [Google AI Studio](https://aistudio.google.com/usage?hl=th)
  ในส่วน**แดชบอร์ด** > **การใช้งาน**

ดูข้อมูลเพิ่มเติมได้ที่[หน้าการเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)

## 2. ติดตั้ง SDK และทำการเรียกครั้งแรก

ติดตั้ง SDK และสร้างข้อความด้วยการเรียก API เพียงครั้งเดียว

### Python

ติดตั้ง SDK โดยทำดังนี้

```
pip install -U google-genai
```

เริ่มต้นไคลเอ็นต์และส่งคำขอ

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

ติดตั้ง SDK โดยทำดังนี้

```
npm install @google/genai
```

เริ่มต้นไคลเอ็นต์และส่งคำขอ

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**คำตอบ:**

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
  "model": "gemini-3.6-flash",
}
```

เมื่อใช้ REST API จะแสดง`Interaction`แบบเต็มซึ่งมีข้อมูลเมตา สถิติการใช้งาน และประวัติแบบทีละขั้นตอนของคำพูด

แม้ว่า SDK จะแสดงการตอบกลับทั้งหมด แต่ก็ยังมีพร็อพเพอร์ตี้ที่สะดวก เช่น `interaction.output_text` และ `interaction.output_image` เพื่อเข้าถึงเอาต์พุตสุดท้ายได้โดยตรง ดูข้อมูลเพิ่มเติมเกี่ยวกับโครงสร้างการตอบกลับได้ใน[ภาพรวมของการโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) หรืออ่าน[คู่มือการสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)เพื่อดูรายละเอียดเกี่ยวกับวิธีการของระบบและการกำหนดค่าการสร้าง

## 3. สตรีมคำตอบ

สตรีมคำตอบขณะที่ระบบสร้างขึ้นเพื่อให้การโต้ตอบราบรื่นยิ่งขึ้น เหตุการณ์ `step.delta` แต่ละรายการจะส่งข้อความเป็นกลุ่มที่คุณแสดงได้ทันที

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

เมื่อสตรีม เซิร์ฟเวอร์จะตอบกลับด้วยสตรีมของเหตุการณ์ที่เซิร์ฟเวอร์ส่ง (SSE) แต่ละเหตุการณ์จะมีประเภทและข้อมูล JSON

**คำตอบ:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

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

ดูรายละเอียดเกี่ยวกับการจัดการเหตุการณ์การสตรีมและประเภทเดลต้าได้ที่[คู่มือการโต้ตอบในการสตรีม](https://ai.google.dev/gemini-api/docs/streaming?hl=th)

## 4. การสนทนาแบบหลายรอบ

API การโต้ตอบรองรับการสนทนาแบบหลายรอบด้วย 2 วิธีดังนี้

- **มีสถานะ (แนะนำ)**: สนทนาต่อในเซิร์ฟเวอร์โดยใช้ `previous_interaction_id` เหมาะสำหรับเวิร์กโฟลว์การแชทและเวิร์กโฟลว์ของเอเจนต์ส่วนใหญ่ที่คุณต้องการให้เซิร์ฟเวอร์จัดการประวัติและเพิ่มประสิทธิภาพการแคช
- **ไม่มีสถานะ**: จัดการประวัติการสนทนาในไคลเอ็นต์โดยส่งทุกช่วงของการสนทนาที่ผ่านมา (รวมถึงความคิดของโมเดลขั้นกลางและขั้นตอนของเครื่องมือ) ในแต่ละคำขอ

### มีสถานะ (แนะนำ)

เชื่อมโยงการโต้ตอบโดยส่ง `previous_interaction_id` เซิร์ฟเวอร์จะจัดการประวัติการสนทนาทั้งหมดให้คุณ

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### ไม่เก็บสถานะ

ตั้งค่า`store=false`และจัดการประวัติการสนทนาในฝั่งไคลเอ็นต์ คุณต้องเก็บรักษาและส่งขั้นตอนทั้งหมดที่โมเดลสร้างขึ้น (รวมถึงขั้นตอน `thought` และ `function_call`) อีกครั้งตามที่ได้รับ

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
    model="gemini-3.6-flash",
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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**คำตอบ:**

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
  "model": "gemini-3.6-flash"
}
```

การโต้ตอบครั้งที่ 2 จะแสดงออบเจ็กต์การตอบกลับที่สมบูรณ์ซึ่งมีเฉพาะขั้นตอนใหม่ แต่จะอิงตามบริบทของเทิร์นก่อนหน้า ดูข้อมูลเพิ่มเติมเกี่ยวกับการรักษาสถานะใน[คู่มือการสนทนาแบบหลายรอบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#multi-turn-conversations) หรือสำรวจ[โหมดแบบไม่เก็บสถานะ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#stateless-conversations)สำหรับการจัดการประวัติฝั่งไคลเอ็นต์

## 5. การทำความเข้าใจแบบ Multimodal

โมเดล Gemini เข้าใจรูปภาพ เสียง วิดีโอ และเอกสารได้โดยตรง ส่งสื่อพร้อมกับข้อความในคำขอเดียว

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**คำตอบ:**

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
  "model": "gemini-3.6-flash",
}
```

ดูวิธีส่งไฟล์รูปภาพ วิดีโอ และเสียงใน[คู่มือการทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)

[hearing

การทำความเข้าใจเสียง

ถอดเสียง สรุป หรือตอบคำถามเกี่ยวกับไฟล์เสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)
[videocam

การทำความเข้าใจวิดีโอ

วิเคราะห์เนื้อหาวิดีโอ ค้นหาเหตุการณ์ และอธิบายการดำเนินการ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th)
[description

การประมวลผลเอกสาร

ดึงข้อมูลจาก PDF และรูปแบบเอกสารอื่นๆ](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

## 6. การสร้างแบบหลายรูปแบบ

Gemini สามารถสร้างรูปภาพได้โดยตรงโดยใช้โมเดลรูปภาพ [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

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

**คำตอบ:**

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

เมื่อโมเดลสร้างรูปภาพ ระบบจะแสดงผลข้อมูลรูปภาพที่เข้ารหัส Base64 ในขั้นตอนภายในอาร์เรย์ `steps` รวมถึงผ่านพร็อพเพอร์ตี้ความสะดวก `output_image` ดู[คำแนะนำในการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)เพื่อดูข้อมูลเกี่ยวกับสัดส่วนภาพ การแก้ไขรูปภาพ และข้อมูลอ้างอิง

[record\_voice\_over

การสร้างคำพูด

สร้างคำพูดที่สื่ออารมณ์ซึ่งมีผู้พูดหลายคนด้วย TTS ของ Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)
[music\_note

การสร้างเสียงดนตรี

สร้างคลิปและเพลงแบบเต็มด้วย Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)

## 7. ใช้เอาต์พุตที่มีโครงสร้าง

กำหนดค่าโมเดลให้แสดงผล JSON ที่ตรงกับสคีมาที่คุณกำหนด เอาต์พุตที่มีโครงสร้างใช้ได้กับ [Pydantic](https://docs.pydantic.dev/latest/) (Python) และ [Zod](https://zod.dev/) (JavaScript)

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**คำตอบ:**

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
  "model": "gemini-3.6-flash",
}
```

บล็อกข้อความเอาต์พุตมีสตริง JSON ที่ถูกต้องซึ่งเป็นไปตามสคีมาที่ขออย่างแน่นอน ดูวิธีกำหนดโครงสร้างที่ซับซ้อนและสคีมาแบบเรียกซ้ำได้ที่[คู่มือเอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)

## 8. ใช้เครื่องมือ

อ้างอิงคำตอบของโมเดลจากข้อมูลแบบเรียลไทม์ด้วย Google Search API จะค้นหา ประมวลผลผลลัพธ์ และแสดงการอ้างอิงโดยอัตโนมัติ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**คำตอบ:**

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
  "model": "gemini-3.6-flash",
}
```

ขั้นตอนการค้นหาจะแสดงรายละเอียดภายในประวัติการโต้ตอบ และเอาต์พุตสุดท้ายจะมีอ้างอิงในบรรทัดที่ชี้ไปยังแหล่งข้อมูลบนเว็บ

คุณดูวิธีแยกข้อมูลอ้างอิงในการค้นหาได้ใน[คู่มือการอ้างอิงของ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) หรือดูวิธีรวมเครื่องมือหลายอย่างได้ใน[คู่มือการรวมเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

[code

การเรียกใช้โค้ด

เรียกใช้โค้ด Python ในสภาพแวดล้อม Borg ที่แซนด์บ็อกซ์และปลอดภัย](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)
[link

บริบท URL

ส่ง URL ของเว็บสาธารณะโดยตรงเพื่ออ้างอิงคำตอบในเนื้อหาหน้าเว็บ](https://ai.google.dev/gemini-api/docs/url-context?hl=th)
[search

ค้นหาไฟล์

จัดทำดัชนีและค้นหาในเอกสารและไฟล์สื่อที่อัปโหลด](https://ai.google.dev/gemini-api/docs/file-search?hl=th)
[map

Google Maps

อ้างอิงคำตอบจากข้อมูลเชิงพื้นที่และข้อมูลตำแหน่งในโลกแห่งความเป็นจริง](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)
[computer

การใช้คอมพิวเตอร์

การทำงานอัตโนมัติของเบราว์เซอร์และการโต้ตอบกับหน้าจอ](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

## 9. เรียกใช้ฟังก์ชันของคุณเอง

การเรียกใช้ฟังก์ชันช่วยให้คุณเชื่อมต่อโมเดลกับโค้ดได้ คุณประกาศชื่อและพารามิเตอร์ของฟังก์ชัน โมเดลจะตัดสินใจว่าจะเรียกใช้ฟังก์ชันเมื่อใดและส่งคืนอาร์กิวเมนต์ที่มีโครงสร้าง จากนั้นคุณจะเรียกใช้ฟังก์ชันในเครื่องและส่งผลลัพธ์กลับ

### มีสถานะ (แนะนำ)

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
        model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

### ไม่เก็บสถานะ

นอกจากนี้ คุณยังใช้การเรียกฟังก์ชันในโหมดแบบไม่เก็บสถานะได้โดยจัดการประวัติการสนทนาฝั่งไคลเอ็นต์และตั้งค่า `store=false` ในโหมดแบบไม่เก็บสถานะ คุณต้องส่งประวัติการสนทนาทั้งหมดในฟิลด์ `input` ของคำขอที่ตามมาแต่ละรายการ ประวัติการเข้าชมต้องมีข้อมูลต่อไปนี้

1. `user_input`ขั้นตอนเริ่มต้น
2. ขั้นตอนทั้งหมดที่โมเดลสร้างขึ้นซึ่งส่งคืนในเทิร์นที่ 1 (รวมถึงขั้นตอน `thought` และ `function_call`) จะเหมือนกับที่ได้รับทุกประการ
3. `function_result` ขั้นตอนที่มีเอาต์พุตของฟังก์ชันที่เรียกใช้

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
        model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    \"model\": \"gemini-3.6-flash\",
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

**คำตอบ:**

ในเทิร์นที่ 1 โมเดลจะแสดงคำตอบที่มีสถานะ `requires_action` และขั้นตอน `function_call` ดังนี้

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
  "model": "gemini-3.6-flash"
}
```

หลังจากเรียกใช้ฟังก์ชันในเครื่องและส่งผลลัพธ์ (เทิร์นที่ 2) แล้ว การโต้ตอบที่เสร็จสมบูรณ์สุดท้ายจะแสดงขึ้น

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
  "model": "gemini-3.6-flash",
}
```

สำหรับฟีเจอร์ขั้นสูง เช่น การเรียกใช้ฟังก์ชันแบบขนานหรือโหมดการเลือกฟังก์ชัน โปรดดู[คู่มือการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

## 10. เรียกใช้ Agent ที่มีการจัดการ

เอเจนต์ที่มีการจัดการจะทำงานในแซนด์บ็อกซ์ระยะไกลพร้อมสิทธิ์เข้าถึงเครื่องมือต่างๆ เช่น การรันโค้ดและการจัดการไฟล์ ส่ง `agent` แทน `model` และตั้งค่า `environment="remote"`

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

นอกจากนี้ คุณยังกำหนดและบันทึก[เอเจนต์ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th)พร้อมคำสั่ง ทักษะ และแหล่งข้อมูลของคุณเองได้ด้วย

[rocket\_launch

คู่มือเริ่มใช้งานฉบับย่อ

โทรหา Agent เป็นครั้งแรก สตรีมคำตอบ และสร้าง Agent ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)
[smart\_toy

Agent ของ Antigravity

ความสามารถ เครื่องมือ อินพุตมัลติโมดอล และราคาสำหรับเอเจนต์เริ่มต้น](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)
[experiment

Agent ใน AI Studio

พื้นที่ทดลองแบบภาพสำหรับการสร้างต้นแบบเอเจนต์โดยไม่ต้องเขียนโค้ด](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=th)

## 11. เรียกใช้งานในเบื้องหลัง

ตั้งค่า `background=True` ให้เรียกใช้ฟังก์ชันที่ใช้เวลานานแบบไม่พร้อมกัน สำรวจผลลัพธ์ด้วย `interactions.get()` ดูรายละเอียดเพิ่มเติมได้ที่[คู่มือการดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**คำตอบ:**

การตอบกลับครั้งแรกจะแสดงทันทีพร้อมสถานะ `in_progress` ดังนี้

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

เมื่อดำเนินการงานในเบื้องหลังเสร็จสมบูรณ์แล้ว การตรวจสอบสถานะการโต้ตอบจะแสดงผลดังนี้

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
  "model": "gemini-3.6-flash",
}
```

อ่านเกี่ยวกับการเรียกใช้โมเดลและเอเจนต์แบบไม่พร้อมกันได้ใน[คู่มือการดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th)

## ขั้นตอนถัดไป

- [การดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/background-execution?hl=th): เรียกใช้งานที่ใช้เวลานานแบบไม่พร้อมกันและจัดการสถานะ
- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th): คำสั่งของระบบ การกำหนดค่าการสร้าง และรูปแบบข้อความขั้นสูง
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th): สัดส่วนภาพ การแก้ไขรูปภาพ และการอ้างอิงสไตล์
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th): การจัดประเภท การตรวจจับออบเจ็กต์ และคำถามและคำตอบเกี่ยวกับภาพ
- [การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th): ใช้การให้เหตุผลแบบลูกโซ่สำหรับงานที่ซับซ้อน
- [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th): โหมดฟังก์ชันแบบขนาน แบบประกอบ และแบบจำกัด
- [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th): การอ้างอิง การอ้างอิง และคำแนะนำในการค้นหา
- [Agent ที่ได้รับการจัดการ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): Agent ที่สร้างไว้ล่วงหน้าพร้อมการรันโค้ดและการจัดการไฟล์
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th): การค้นคว้าแบบอัตโนมัติหลายขั้นตอนพร้อมการวางแผนและการสังเคราะห์
- [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th): สคีมา JSON, การแจงนับ และคำจำกัดความประเภทแบบเรียกซ้ำ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-12 UTC"],[],[]]
