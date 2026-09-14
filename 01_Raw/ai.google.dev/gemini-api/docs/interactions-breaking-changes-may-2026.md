---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=th
fetched_at: 2026-09-14T05:46:39.832717+00:00
title: "API \u0e01\u0e32\u0e23\u0e42\u0e15\u0e49\u0e15\u0e2d\u0e1a: \u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e22\u0e49\u0e32\u0e22\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 (\u0e1e\u0e24\u0e29\u0e20\u0e32\u0e04\u0e21 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# API การโต้ตอบ: คู่มือการย้ายข้อมูลการเปลี่ยนแปลงที่ไม่รองรับการทำงานย้อนหลัง (พฤษภาคม 2026)

Interactions API `v1beta` มีการเปลี่ยนแปลงที่ทำให้เกิดข้อผิดพลาด ซึ่งจะปรับโครงสร้าง API ใหม่เพื่อรองรับความสามารถในอนาคต เช่น การควบคุมระหว่างการเดินทางและการเรียกใช้เครื่องมือแบบไม่พร้อมกัน หน้านี้จะอธิบายสิ่งที่เปลี่ยนแปลงและแสดงตัวอย่างโค้ดก่อนและหลังการเปลี่ยนแปลงเพื่อช่วยคุณย้ายข้อมูล การเปลี่ยนแปลงมี 2 หมวดหมู่ ได้แก่

1. [**สคีมา `steps`**](#steps-schema): อาร์เรย์ `steps` ใหม่จะแทนที่อาร์เรย์
   `outputs` เพื่อแสดงไทม์ไลน์ที่มีโครงสร้างของการโต้ตอบแต่ละครั้ง
2. [**การกำหนดค่ารูปแบบเอาต์พุต**](#output-format-config): `response\_format` แบบ Polymorphic ใหม่จะรวมการควบคุมรูปแบบเอาต์พุตทั้งหมดและนำ `response\_mime\_type` ออก`response_format``response_mime_type`

ทำตามขั้นตอนใน [วิธีย้ายข้อมูลไปยังสคีมาใหม่](#how-to-migrate) เพื่อ
อัปเดตการผสานรวม

## การเปลี่ยนแปลงหลัก: `outputs` เป็น `steps`

สคีมาใหม่จะแทนที่อาร์เรย์ `outputs` ด้วยอาร์เรย์ `steps`

- **เดิม**: การตอบกลับจะแสดงอาร์เรย์ `outputs` แบบแบนที่มีเฉพาะเนื้อหาที่สร้างขึ้นโดยโมเดล
- **สคีมาใหม่**: การตอบกลับจะแสดงอาร์เรย์ `steps` ที่มีขั้นตอนที่มีโครงสร้างพร้อมตัวแยกประเภท

`POST /interactions` จะแสดงเฉพาะขั้นตอนเอาต์พุต `GET /interactions/{id}`
จะแสดงไทม์ไลน์ขั้นตอนทั้งหมด รวมถึงขั้นตอน `user_input` เริ่มต้น

### อินพุต/เอาต์พุตพื้นฐาน (Unary)

#### ก่อนการเปลี่ยนแปลง (เดิม)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
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

### การเรียกใช้ฟังก์ชัน

โครงสร้างคำขอจะยังคงเหมือนเดิม แต่การตอบกลับจะแทนที่เนื้อหา `outputs` แบบแบนด้วยขั้นตอนที่มีโครงสร้าง

#### ก่อนการเปลี่ยนแปลง (เดิม)

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
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
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

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

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
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
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

### เครื่องมือฝั่งเซิร์ฟเวอร์

ตอนนี้เครื่องมือฝั่งเซิร์ฟเวอร์ (เช่น Google Search หรือการดำเนินการโค้ด) จะแสดงประเภทขั้นตอนที่เฉพาะเจาะจงในอาร์เรย์ `steps` แม้ว่าสคีมาเดิมจะแสดงการดำเนินการเหล่านี้เป็นประเภทเนื้อหาที่เฉพาะเจาะจงภายในอาร์เรย์ `outputs` แต่สคีมาใหม่จะย้ายการดำเนินการเหล่านี้ไปยังอาร์เรย์ `steps` ตัวอย่างต่อไปนี้ใช้ Google Search

#### ก่อนการเปลี่ยนแปลง (เดิม)

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
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
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

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
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
    "model": "gemini-3.6-flash",
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

### สตรีมมิง

สตรีมมิงจะแสดงประเภทเหตุการณ์ใหม่ ดังนี้

#### ประเภทเหตุการณ์ใหม่

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### ประเภทเหตุการณ์ที่เลิกใช้งานแล้ว

ระบบจะแทนที่ประเภทเหตุการณ์เดิมต่อไปนี้ด้วยเหตุการณ์ใหม่ที่ระบุไว้ข้างต้น

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → แทนที่ด้วย `interaction.in_progress`, `interaction.requires_action` และอื่นๆ

**การเรียกใช้ฟังก์ชันสตรีมมิง**: เมื่อใช้สตรีมมิงกับการเรียกใช้ฟังก์ชัน
เหตุการณ์ `step.start` จะแสดงชื่อฟังก์ชัน และเหตุการณ์ `step.delta` จะ
สตรีมอาร์กิวเมนต์เป็นสตริง JSON บางส่วน (โดยใช้ `arguments_delta`) คุณ
ต้องสะสม Delta เหล่านี้เพื่อรับอาร์กิวเมนต์ทั้งหมด ซึ่งแตกต่างจากการเรียกใช้แบบ Unary ที่คุณจะได้รับออบเจ็กต์การเรียกใช้ฟังก์ชันที่สมบูรณ์ในครั้งเดียว

#### ตัวอย่าง

##### ก่อนการเปลี่ยนแปลง (เดิม)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

##### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.6-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
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
     "model": "gemini-3.6-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.6-flash"}, "event_type": "interaction.created"}
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

### ประวัติการสนทนาแบบ Stateless

หากคุณจัดการประวัติการสนทนาด้วยตนเองในฝั่งไคลเอ็นต์ (กรณีการใช้งานแบบ Stateless) คุณต้องอัปเดตวิธีเชื่อมโยงการสนทนาก่อนหน้า

- **เดิม**: นักพัฒนามักจะรวบรวมอาร์เรย์ `outputs` จากการตอบกลับและส่งกลับในช่อง `input` ในการสนทนาครั้งถัดไป
- **สคีมาใหม่**: ตอนนี้คุณควรรวบรวมอาร์เรย์ `steps` จากการตอบกลับและส่งในช่อง `input` ของคำขอถัดไป โดยเพิ่มการสนทนาใหม่ของผู้ใช้เป็นขั้นตอน `user_input`

## การกำหนดค่ารูปแบบเอาต์พุต: การเปลี่ยนแปลง `response_format`

API ที่อัปเดตจะรวมการควบคุมรูปแบบเอาต์พุตทั้งหมดไว้ในช่อง `response_format` แบบ Polymorphic ที่รวมเป็นหนึ่งเดียว ซึ่งจะรวมการกำหนดค่าเอาต์พุตไว้ที่ระดับบนสุด และทำให้ `generation_config` มุ่งเน้นไปที่ลักษณะการทำงานของโมเดล (เช่น อุณหภูมิ, top\_p และการคิด)

### การเปลี่ยนแปลงที่สำคัญ

- **API จะนำ `response_mime_type` ออก** ตอนนี้คุณระบุประเภท MIME ต่อรายการรูปแบบภายใน `response_format`
- **ตอนนี้ `response_format` เป็นออบเจ็กต์ (หรืออาร์เรย์) แบบ Polymorphic** แต่ละรายการมีตัวแยกประเภท `type` (`text`, `audio`, `image`) และช่องที่เฉพาะเจาะจงตามประเภท หากต้องการขอเอาต์พุตหลายรูปแบบ ให้ส่งอาร์เรย์ของรายการรูปแบบ
- **`image_config` จะย้ายจาก `generation_config` ไปยัง `response_format`**
  ตอนนี้คุณระบุการตั้งค่าเอาต์พุตของรูปภาพ เช่น `aspect_ratio` และ `image_size`
  ในรายการ `response_format` ที่มี `"type": "image"`

### เอาต์พุตที่มีโครงสร้าง (JSON)

สคีมาใหม่จะนำช่อง `response_mime_type` ออก แต่ให้ระบุประเภท
MIME และสคีมา JSON ภายในออบเจ็กต์ `response_format` ที่มี
`"type": "text"`

#### ก่อนการเปลี่ยนแปลง (เดิม)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

### การกำหนดค่ารูปภาพ

สคีมาใหม่จะนำ `image_config` ออกจาก `generation_config` ตอนนี้คุณระบุ
การตั้งค่าเอาต์พุตของรูปภาพในรายการ `response_format` ที่มี `"type": "image"`

#### ก่อนการเปลี่ยนแปลง (เดิม)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### การกำหนดค่าเสียง

สคีมาใหม่จะแทนที่ `response_modalities: ["audio"]` ด้วยรายการ `response_format` ที่มี `"type": "audio"`

#### ก่อนการเปลี่ยนแปลง (เดิม)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### หลังการเปลี่ยนแปลง (สคีมาใหม่)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
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
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

หากต้องการขอเอาต์พุตหลายรูปแบบ (เช่น ข้อความและเสียงพร้อมกัน) ให้ส่งอาร์เรย์ของรายการรูปแบบไปยัง `response_format` แทนที่จะส่งออบเจ็กต์เดียว

## วิธีย้ายข้อมูลไปยังสคีมาใหม่

### ผู้ใช้ SDK

อัปเกรดเป็น SDK เวอร์ชันล่าสุด (Python ≥2.0.0, JavaScript ≥2.0.0) SDK จะเลือกใช้สคีมาใหม่ให้คุณโดยอัตโนมัติ คุณจึงไม่ต้องเปลี่ยนแปลงโค้ดใดๆ นอกเหนือจากการอัปเดตวิธีอ่านการตอบกลับ (ดูตัวอย่างด้านบน) โปรดทราบว่า SDK เวอร์ชันเหล่านี้รองรับเฉพาะสคีมาใหม่ SDK เวอร์ชันเก่า (Python 1.x.x, JavaScript 1.x.x) จะยังคงทำงานได้จนกว่าระบบจะนำสคีมาเดิมออกในวันที่ **8 มิถุนายน 2026**

### ผู้ใช้ REST API

เพิ่มส่วนหัว `Api-Revision: 2026-05-20` ลงในคำขอเพื่อเลือกใช้สคีมาใหม่ได้แล้วตอนนี้ หลังจากวันที่ **26 พฤษภาคม** สคีมาใหม่จะกลายเป็นค่าเริ่มต้นสำหรับคำขอทั้งหมด
คุณเลือกไม่ใช้ชั่วคราวได้ด้วย `Api-Revision: 2026-05-07`
จนถึงวันที่ **8 มิถุนายน** ซึ่งเป็นวันที่ API จะนำสคีมาเดิมออกอย่างถาวร

### ไทม์ไลน์

| วันที่ | ระยะ | ผู้ใช้ SDK | ผู้ใช้ REST API |
| --- | --- | --- | --- |
| **7 พฤษภาคม** | เลือกเข้าร่วม | SDK เวอร์ชันใหม่พร้อมใช้งานแล้ว (Python ≥2.0.0, JS ≥2.0.0) อัปเกรดเพื่อรับสคีมาใหม่โดยอัตโนมัติ | เพิ่มส่วนหัว `Api-Revision: 2026-05-20` เพื่อเลือกเข้าร่วม ค่าเริ่มต้นจะยังคงเป็นสคีมาเดิม |
| **26 พฤษภาคม** | พลิกค่าเริ่มต้น | หากอัปเกรดแล้ว คุณไม่ต้องดำเนินการใดๆ SDK เวอร์ชันเก่า (Python 1.x.x, JS 1.x.x) จะยังคงทำงานได้ แต่จะแสดงการตอบกลับเดิม | ตอนนี้สคีมาใหม่เป็นค่าเริ่มต้นแล้ว ส่งส่วนหัว `Api-Revision: 2026-05-07` เพื่อเลือกไม่ใช้ |
| **8 มิถุนายน** | การเลิกใช้งาน | SDK เวอร์ชัน Python 1.x.x และ JS 1.x.x จะหยุดทำงานสำหรับการเรียกใช้ Interactions API | ระบบจะนำสคีมาเดิมออกสำหรับ Interactions API ระบบจะไม่สนใจส่วนหัว `Api-Revision` |

## รายการตรวจสอบการย้ายข้อมูล

### สคีมา `steps`

- อัปเดตโค้ดเพื่ออ่านเนื้อหาการตอบกลับจากอาร์เรย์ `steps` แทน `outputs` [ดูตัวอย่าง](#basic-unary)
- ตรวจสอบว่าโค้ดของคุณจัดการประเภทขั้นตอน `user_input` และ `model_output` ได้ [ดูตัวอย่าง](#basic-unary)
- (การเรียกใช้ฟังก์ชัน) อัปเดตโค้ดเพื่อค้นหาขั้นตอน `function_call` ในอาร์เรย์ `steps` [ดูตัวอย่าง](#function-calling)
- (เครื่องมือฝั่งเซิร์ฟเวอร์) อัปเดตโค้ดเพื่อจัดการขั้นตอนที่เฉพาะเจาะจงของเครื่องมือ (เช่น `google_search_call`, `google_search_result`) [ดูตัวอย่าง](#server-side-tools)
- (ประวัติแบบ Stateless) อัปเดตการจัดการประวัติเพื่อส่งอาร์เรย์ `steps` ในช่อง `input` ของคำขอถัดไป [ดูรายละเอียด](#stateless-history)
- (สตรีมมิงเท่านั้น) อัปเดตไคลเอ็นต์เพื่อฟังประเภทเหตุการณ์ SSE ใหม่ (`interaction.created`, `step.delta` และอื่นๆ) [ดูตัวอย่าง](#streaming)

### การกำหนดค่ารูปแบบเอาต์พุต (`response_format`)

- แทนที่ `response_mime_type` ด้วยช่อง `mime_type` ภายใน `response_format` [ดูตัวอย่าง](#structured-output)
- รวมสคีมา JSON `response_format` ที่มีอยู่ภายในออบเจ็กต์ `{"type": "text", "schema": ...}` [ดูตัวอย่าง](#structured-output)
- (การสร้างรูปภาพ) ย้าย `image_config` จาก `generation_config` ไปยังรายการ `{"type": "image", ...}` ใน `response_format` [ดูตัวอย่าง](#image-config)
- (การสร้างคำพูด) แทนที่ `response_modalities=["audio"]` ด้วยรายการ `{"type": "audio"}` ใน `response_format` [ดูตัวอย่าง](#audio-config)
- (มัลติโมดัล) แปลง `response_format` จากออบเจ็กต์เดียวเป็นอาร์เรย์เมื่อขอเอาต์พุตหลายรูปแบบ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-12 UTC"],[],[]]
