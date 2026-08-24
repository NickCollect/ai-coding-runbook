---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=th
fetched_at: 2026-08-24T02:20:48.638774+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้างข้อความ

Gemini API สามารถสร้างเอาต์พุตข้อความจากอินพุตข้อความ รูปภาพ วิดีโอ และเสียง

ตัวอย่างเบื้องต้นมีดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?"
  }'
```

Google GenAI SDK มีพร็อพเพอร์ตี้ที่สะดวกในออบเจ็กต์ `Interaction` ที่ส่งกลับมาโดยตรงเพื่อให้เข้าถึงการตอบกลับของโมเดลได้

ตัวช่วยที่ใช้บ่อยที่สุดคือ **`interaction.output_text`** (String) ซึ่งจะแสดงผลบล็อกข้อความสุดท้ายในการตอบกลับของโมเดล หากการตอบกลับแยกออกเป็นบล็อก `TextContent` หลายบล็อกที่ต่อเนื่องกัน ระบบจะรวมบล็อกเหล่านั้นโดยอัตโนมัติ
โปรดทราบว่า `.output_text` จะไม่รวมบล็อกข้อความก่อนหน้าที่คั่นด้วยเนื้อหาที่ไม่ใช่ข้อความ (เช่น ความคิด รูปภาพ เสียง หรือการเรียกใช้เครื่องมือ) สำหรับคำตอบแบบหลายรูปแบบที่ซับซ้อนหรือมีการสลับกัน คุณต้องวนซ้ำ `steps` ด้วยตนเองแทน ดูข้อมูลเพิ่มเติมเกี่ยวกับพร็อพเพอร์ตี้ที่สะดวกอื่นๆ ของสื่อได้ที่
[ภาพรวมของการโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions?hl=th#convenience-properties)

## การคิดด้วย Gemini

โมเดล Gemini มักจะเปิดใช้ ["การคิด"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=th)
ไว้โดยค่าเริ่มต้น ซึ่งช่วยให้โมเดลใช้เหตุผลก่อนที่จะตอบกลับ
คำขอได้

โมเดลแต่ละรายการรองรับการกำหนดค่าการคิดที่แตกต่างกัน ซึ่งช่วยให้คุณควบคุมต้นทุน เวลาในการตอบสนอง และความฉลาดได้ ดูรายละเอียดเพิ่มเติมได้ที่
[คู่มือการคิด](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=th#set-budget)

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## คำแนะนำระบบและการกำหนดค่าอื่นๆ

คุณสามารถกำหนดลักษณะการทำงานของโมเดล Gemini ด้วยคำแนะนำระบบได้ ส่งพารามิเตอร์ `system_instruction` เพื่อกำหนดค่าลักษณะการทำงานของโมเดล

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

นอกจากนี้ คุณยังลบล้างพารามิเตอร์การสร้างเริ่มต้น เช่น อุณหภูมิ โดยใช้พารามิเตอร์ `generation_config` ได้ด้วย

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

โปรดดูรายการพารามิเตอร์ที่กำหนดค่าได้ทั้งหมดและคำอธิบายของพารามิเตอร์เหล่านั้นได้ที่ข้อมูลอ้างอิง [Interactions API](https://ai.google.dev/api/interactions-api?hl=th)

## อินพุตหลายรูปแบบ

Gemini API รองรับอินพุตหลายรูปแบบ ซึ่งช่วยให้คุณรวมข้อความกับไฟล์สื่อได้ ตัวอย่างต่อไปนี้แสดงการระบุรูปภาพ

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

ดูวิธีการระบุรูปภาพแบบอื่นและการประมวลผลรูปภาพขั้นสูงเพิ่มเติมได้ที่
ดู[คู่มือการทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=th)ของเรา
นอกจากนี้ API ยังรองรับอินพุตและการทำความเข้าใจ[เอกสาร](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th) [วิดีโอ](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=th) และ
[เสียง](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=th)ด้วย

## การตอบกลับแบบสตรีม

โดยค่าเริ่มต้น โมเดลจะแสดงผลการตอบกลับหลังจากกระบวนการสร้างทั้งหมดเสร็จสมบูรณ์แล้วเท่านั้น

หากต้องการให้การโต้ตอบราบรื่นขึ้น ให้ใช้การสตรีมเพื่อจัดการกับส่วนการตอบกลับเมื่อมีการสร้าง [ดูคู่มือ
การโต้ตอบแบบสตรีม
โดยเฉพาะ ซึ่งครอบคลุมประเภทเหตุการณ์
การสตรีมด้วยเครื่องมือ การคิด เอเจนต์ และการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=th)

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
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
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

## การสนทนาไปมา

Interactions API รองรับการสนทนาไปมาโดยการเชื่อมโยงการโต้ตอบเข้าด้วยกันโดยใช้ `previous_interaction_id` แต่ละรอบเป็นการโต้ตอบแยกกัน และ API จะจัดการประวัติการสนทนาโดยอัตโนมัติ

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
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
}

await main();
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

นอกจากนี้ยังใช้การสตรีมสำหรับการสนทนาไปมาได้ด้วยการรวม `previous_interaction_id` กับวิธีการสตรีม

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## การสนทนาแบบไม่เก็บสถานะ

โดยค่าเริ่มต้น Interactions API จะจัดการสถานะการสนทนาฝั่งเซิร์ฟเวอร์เมื่อคุณใช้ `previous_interaction_id` อย่างไรก็ตาม คุณยังทำงานในโหมดไร้สถานะได้ด้วยการจัดการประวัติการสนทนาด้วยตนเองฝั่งไคลเอ็นต์

วิธีใช้โหมดไร้สถานะ 1. ตั้งค่า `store=false` ในคำขอเพื่อเลือกไม่ใช้พื้นที่เก็บข้อมูลฝั่งเซิร์ฟเวอร์
2. เก็บประวัติการสนทนาเป็นอาร์เรย์ของ**ขั้นตอน** ฝั่งไคลเอ็นต์
3. ในคำขอที่ตามมา ให้ส่งขั้นตอนที่สะสมไว้ในช่อง `input` และเพิ่มรอบใหม่เป็นขั้นตอน `user_input`

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

async function main() {
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
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
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

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## เคล็ดลับเกี่ยวกับพรอมต์

โปรดดู[คู่มือวิศวกรรมพรอมต์](https://ai.google.dev/gemini/docs/prompting-strategies?hl=th)สำหรับ
คำแนะนำในการใช้ประโยชน์จาก Gemini ให้ได้มากที่สุด

## ขั้นตอนถัดไป

- ลองใช้ [Gemini ใน Google AI Studio](https://aistudio.google.com?hl=th)
- ทดลองใช้
  [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=th)สำหรับการตอบกลับที่คล้ายกับ
  JSON
- สำรวจความสามารถในการทำความเข้าใจ[รูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=th),
  [วิดีโอ](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=th),
  [เสียง](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=th) และ
  [เอกสาร](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th)ของ Gemini
- ดูข้อมูลเกี่ยวกับกลยุทธ์การใช้พรอมต์กับไฟล์หลายรูปแบบ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
