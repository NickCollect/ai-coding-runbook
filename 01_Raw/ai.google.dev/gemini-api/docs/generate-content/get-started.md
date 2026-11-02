---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th
fetched_at: 2026-11-02T07:21:12.572057+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน

คู่มือนี้จะช่วยให้คุณเริ่มต้นใช้งาน API **generateContent** เวอร์ชันเดิม สำหรับโปรเจ็กต์และแอปพลิเคชันใหม่ เราขอแนะนำอย่างยิ่งให้ใช้ **Interactions API** ใหม่แทน ซึ่งเป็นวิธีที่ง่ายที่สุดและดีที่สุดในการสร้างด้วยโมเดลและเอเจนต์ของ Gemini

การเริ่มต้นอย่างรวดเร็วนี้จะแสดงวิธีติดตั้ง[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)ของเราและส่งคำขอแรก สตรีมคำตอบ สร้างการสนทนาแบบหลายรอบ และใช้เครื่องมือโดยใช้วิธี`generateContent` มาตรฐาน

## รับคีย์ API

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

## ติดตั้ง Google GenAI SDK

### Python

ใช้ [Python 3.9 ขึ้นไป](https://www.python.org/downloads/) เพื่อติดตั้ง[แพ็กเกจ`google-genai`](https://pypi.org/project/google-genai/)
โดยใช้[คำสั่ง pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) ต่อไปนี้

```
pip install -q -U google-genai
```

### JavaScript

หากใช้ [Node.js v18 ขึ้นไป](https://nodejs.org/en/download/package-manager) ให้ติดตั้ง [Google Gen AI SDK สำหรับ TypeScript และ JavaScript](https://www.npmjs.com/package/@google/genai) โดยใช้[คำสั่ง npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) ต่อไปนี้

```
npm install @google/genai
```

## สร้างข้อความ

ใช้เมธอด `models.generate_content` เพื่อ[สร้างการตอบกลับเป็นข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## สตรีมคำตอบ

โดยค่าเริ่มต้น โมเดลจะแสดงคำตอบหลังจากกระบวนการสร้างทั้งหมดเสร็จสมบูรณ์แล้วเท่านั้น
หากต้องการประสบการณ์การใช้งานที่รวดเร็วและโต้ตอบได้มากขึ้น คุณสามารถ[สตรีม](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#stream)ก้อนคำตอบขณะที่ระบบ
สร้างคำตอบ

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## การสนทนาแบบหลายรอบ

สําหรับการสนทนาแบบหลายรอบ SDK มี`chats`ตัวช่วยแบบมีสถานะ
เพื่อสร้าง[ประสบการณ์แชทแบบหลายรอบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#chat)
ที่จัดการประวัติการสนทนาโดยอัตโนมัติ

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## ใช้เครื่องมือ

ขยายความสามารถของโมเดลโดย
[อ้างอิงคำตอบด้วย Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
เพื่อเข้าถึงเนื้อหาเว็บแบบเรียลไทม์ โมเดลจะตัดสินใจโดยอัตโนมัติว่าจะค้นหาเมื่อใด ดำเนินการค้นหา และสังเคราะห์คำตอบ

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

นอกจากนี้ Gemini API ยังรองรับเครื่องมืออื่นๆ ที่มาพร้อมกับเครื่องมือต่อไปนี้ด้วย

- **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**:
  ช่วยให้โมเดลเขียนและเรียกใช้โค้ด Python เพื่อแก้โจทย์คณิตศาสตร์ที่ซับซ้อนได้
- **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**: ช่วยให้คุณ
  อ้างอิงคำตอบจาก URL ของหน้าเว็บที่เฉพาะเจาะจงซึ่งคุณระบุ
- **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**: ช่วยให้คุณ
  อัปโหลดไฟล์และอ้างอิงคำตอบในเนื้อหาของไฟล์โดยใช้การค้นหาเชิงความหมาย
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**: ช่วยให้คุณ
  อ้างอิงคำตอบจากข้อมูลตำแหน่งและค้นหาสถานที่ เส้นทาง และ
  แผนที่
- **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**: ช่วยให้โมเดลโต้ตอบกับหน้าจอคอมพิวเตอร์เสมือน แป้นพิมพ์ และเมาส์เพื่อทำงานต่างๆ ได้

## เรียกใช้ฟังก์ชันที่กำหนดเอง

ใช้**[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)**เพื่อเชื่อมต่อโมเดลกับเครื่องมือและ API ที่กำหนดเอง โมเดลจะพิจารณาเวลาที่จะเรียกใช้ฟังก์ชันของคุณและส่งคืน `functionCall` ในการตอบกลับเพื่อให้แอปพลิเคชันของคุณ
ดำเนินการ

ตัวอย่างนี้ประกาศฟังก์ชันอุณหภูมิจำลองและตรวจสอบว่าโมเดล
ต้องการเรียกใช้ฟังก์ชันดังกล่าวหรือไม่

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## ขั้นตอนถัดไป

ตอนนี้คุณได้เริ่มต้นใช้งาน Gemini API แล้ว ลองดูคำแนะนำต่อไปนี้
เพื่อสร้างแอปพลิเคชันขั้นสูงเพิ่มเติม

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)
- [การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
- [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
- [บริบทแบบยาว](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
- [การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-12 UTC"],[],[]]
