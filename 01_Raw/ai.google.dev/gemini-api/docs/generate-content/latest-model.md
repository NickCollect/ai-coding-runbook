---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=th
fetched_at: 2026-09-14T05:50:56.008128+00:00
title: "\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e42\u0e21\u0e40\u0e14\u0e25 Gemini \u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การใช้โมเดล Gemini ล่าสุด

[หน้านี้](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=th)

Gemini 3.6 Flash (`gemini-3.6-flash`) และ Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) และพร้อมสำหรับการใช้งานจริงแล้ว

- **Gemini 3.6 Flash**: ประสิทธิภาพที่ดียิ่งขึ้นในงานที่ซับซ้อนแบบ Agent และ Multimodal พร้อมทั้งลดการใช้โทเค็น โดยมีราคาต่ำกว่า 3.5 Flash
- **Gemini 3.5 Flash-Lite**: โมเดลที่เร็วที่สุดและมีค่าใช้จ่ายต่ำที่สุดในตระกูล 3.5 มีประสิทธิภาพเหนือกว่า Flash-Lite รุ่นก่อนๆ ในการดำเนินการที่มีปริมาณงานสูง

คู่มือนี้จะอธิบายสิ่งใหม่ๆ ในแต่ละโมเดล การเปลี่ยนแปลง API ที่ส่งผลต่อโค้ด และวิธีย้ายข้อมูล

### Gemini 3.6 Flash

1. ติดตั้งทักษะโดยทำดังนี้

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. ใช้ทักษะโดยทำดังนี้

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. ติดตั้งทักษะโดยทำดังนี้

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. ใช้ทักษะโดยทำดังนี้

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## โมเดลใหม่

| โมเดล | รหัสโมเดล | ระดับการคิดเริ่มต้น | ราคา | คำอธิบาย |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | $1.50/1M โทเค็นอินพุต และ $7.50/1M โทเค็นเอาต์พุต | สมดุลระหว่างความเร็วและความฉลาดสำหรับงานแบบ Agent และ Multimodal |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | $0.30/1M โทเค็นอินพุต และ $2.50/1M โทเค็นเอาต์พุต | โมเดล 3.5 ที่เร็วที่สุดและมีค่าใช้จ่ายต่ำที่สุดสำหรับการดำเนินการที่มีปริมาณงานสูง |

ทั้ง 2 โมเดลรองรับหน้าต่างบริบทขนาด 1 ล้านโทเค็น, โทเค็นเอาต์พุตสูงสุด 64, 000 รายการ, การคิด และชุดเครื่องมือในตัวทั้งหมด รวมถึง[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

ดูสเปคทั้งหมดได้ที่หน้าโมเดลต่อไปนี้

- [หน้าโมเดล Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th)
- [หน้าโมเดล Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th)

ดูราคาโดยละเอียดได้ที่[หน้าการกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## คู่มือเริ่มใช้งานฉบับย่อ

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
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
    contents: "Write a three.js script that renders an interactive 3D robot.",
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
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## มีอะไรใหม่ใน Gemini 3.6 Flash

- **การลดโทเค็นและการโต้ตอบ:** ทำเวิร์กโฟลว์แบบหลายขั้นตอนให้เสร็จสมบูรณ์ด้วยขั้นตอนการให้เหตุผล การโต้ตอบ และการเรียกเครื่องมือที่น้อยกว่า Gemini 3.5 นอกจากนี้ยังช่วยลดการวนซ้ำในการดำเนินการ
- **การสร้างโค้ดที่ปรับปรุงแล้ว:** สร้างโค้ดคุณภาพสูงที่พร้อมใช้งานจริงโดยมีการแก้ไขที่ไม่ต้องการและลูปการแก้ไขข้อบกพร่องน้อยลง
- **การปฏิบัติตามคำแนะนำที่ดีขึ้น**: ลดการเปลี่ยนแปลงไฟล์ที่ไม่ต้องการระหว่างงานการวินิจฉัย
- **การให้เหตุผลแบบ Multimodal และเชิงพื้นที่ที่มีประสิทธิภาพ:** ประสิทธิภาพที่ดียิ่งขึ้นในการตีความแผนภูมิ การแปลงพิมพ์เขียวแบบภาพ และการสร้างเลย์เอาต์เว็บแบบหลายองค์ประกอบ
- **การตรวจสอบเชิงโปรแกรมล่วงหน้า:** ชอบที่จะเรียกใช้สคริปต์โค้ดการวินิจฉัยก่อนทำการเปลี่ยนแปลงบ่อยกว่า Gemini 3.5 Flash ซึ่งช่วยเพิ่มความแม่นยำในงานที่ซับซ้อน แต่สามารถเพิ่มขั้นตอนการสำรวจเพิ่มเติมในงานฟรอนท์เอนด์อย่างง่าย
- **การรองรับการใช้คอมพิวเตอร์:** รองรับเป็นเครื่องมือเนทีฟสำหรับการทำงานอัตโนมัติของ UI แบบ Agent
- **ความชอบในการจัดสไตล์ UI**: สร้างโค้ดที่ใช้งานได้ดีขึ้น แม้ว่าผู้ประเมินที่เป็นมนุษย์จะชอบโมเดลก่อนหน้านี้สำหรับการจัดวางเลย์เอาต์ภาพและการจัดสไตล์ คุณสามารถลดปัญหานี้ได้โดยระบุหลักเกณฑ์การออกแบบอย่างชัดเจน
- **ความพยายามในการคิดเริ่มต้น (ปานกลาง):** ใช้ระดับการคิดเริ่มต้น `medium` เดียวกับ Gemini 3.5 Flash
- **ราคาที่ลดลง**: ค่าใช้จ่ายโทเค็นเอาต์พุตที่ต่ำลง ($7.50/1M เทียบกับ $9.00/1M สำหรับ 3.5 Flash) โทเค็นอินพุตยังคงอยู่ที่ $1.50/1M

## มีอะไรใหม่ใน Gemini 3.5 Flash-Lite

- **เวลาในการตอบสนองในการดำเนินการงานที่ลดลง:** อัตราการส่งข้อมูลสูงสุดในตระกูล 3.5 สำหรับการแยกวิเคราะห์ข้อมูลและการแยกเอกสารปริมาณมาก
- **ประสิทธิภาพการให้เหตุผลและ Multimodal ที่ดียิ่งขึ้น:** เส้นทางการย้ายข้อมูลที่ราบรื่นจาก Gemini 2.5 Flash โดยมีคะแนนสูงขึ้นในงานการให้เหตุผล เช่น HLE (18.0% เทียบกับ 11.0%) และเกณฑ์มาตรฐาน Multimodal เช่น CharXIV (74.5% เทียบกับ 63.7%)
- **การจัดระเบียบ Subagent และความน่าเชื่อถือของเครื่องมือ:** ปรับปรุงความน่าเชื่อถือในการดำเนินการเครื่องมือสำหรับการดำเนินการโค้ด การค้นหา และเวิร์กโฟลว์ MCP เพิ่มระดับการคิดสำหรับการวางแผนแบบอัตโนมัติและงาน Subagent ที่ซับซ้อน
- **ความเข้าใจเอกสารที่ดียิ่งขึ้น:** ปรับปรุงความแม่นยำในการแยกวิเคราะห์เอกสารและการแยกข้อมูลที่มีโครงสร้าง ทดลองใช้ระดับการคิดทั้งต่ำและสูงขึ้นอยู่กับความซับซ้อนของเอกสาร
- **การเขียนโค้ดเว็บแบบโต้ตอบและการประมวลผลข้อมูลแบบตาราง:** ทำงานได้ดีในการประมวลผล JavaScript ส่วนหน้าและข้อมูลแบบตารางโดยการวางแผนผ่านการดำเนินการโค้ดแบบเบา
- **ความต่อเนื่องของแชทบ็อตและลักษณะตัวตน:** การปฏิบัติตามคำแนะนำแบบการสนทนาไปมาและความสอดคล้องของลักษณะตัวตนที่ดียิ่งขึ้นเมื่อเทียบกับ Gemini 3.1 Flash-Lite
- **การรองรับการใช้คอมพิวเตอร์:** รองรับเป็นเครื่องมือเนทีฟสำหรับการทำงานอัตโนมัติของ UI แบบ Agent

## การเลือกโมเดล Flash หรือ Flash-Lite ที่เหมาะสม

ใช้ตารางนี้เพื่อเลือกโมเดลและเส้นทางการย้ายข้อมูลที่เหมาะสมสำหรับปริมาณงานของคุณ

ทั้ง 2 โมเดลกำหนดให้ต้องนำพารามิเตอร์การสุ่มตัวอย่างที่เลิกใช้งานแล้ว (`temperature`, `top_p`, `top_k`) และการโต้ตอบของโมเดลที่เติมไว้ล่วงหน้าออก ดูรายละเอียดได้ที่[การเปลี่ยนแปลง API](#api-changes-and-parameter-updates)

| โมเดล | กรณีการใช้งานหลัก | เป้าหมายการย้ายข้อมูลที่แนะนำ |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | การสร้างโค้ด การให้เหตุผลเชิงพื้นที่/Multimodal เวิร์กโฟลว์แบบ Agent หลายขั้นตอน | **Gemini 3.5 Flash**, **Gemini 3 Flash (Preview)** หรือ **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | การดำเนินการ Subagent แบบอัตโนมัติ การวิเคราะห์ข้อมูลและการแยกเอกสารปริมาณมาก การแยกวิเคราะห์ JSON ที่มีโครงสร้าง | **Gemini 3.1 Flash-Lite** หรือ **Gemini 2.5 Flash** |

## Agent ของ Antigravity ที่อัปเดตแล้ว

เนื่องจากประสิทธิภาพที่ดียิ่งขึ้น ตอนนี้ Gemini 3.6 Flash จึงเป็นโมเดลเริ่มต้นใหม่ที่ขับเคลื่อน [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=th) ใน Agent ที่ได้รับการจัดการของ Gemini คุณสามารถเปลี่ยนโมเดลนี้ได้โดยการตั้งค่าฟิลด์ใหม่ใน API

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## การเปลี่ยนแปลง API และการอัปเดตพารามิเตอร์

การเปลี่ยนแปลง API ต่อไปนี้จะมีผลกับโมเดล Gemini 3.6 Flash และ Gemini 3.5 Flash-Lite รวมถึงโมเดล Gemini รุ่นต่อๆ ไป

- **การเลิกใช้งานพารามิเตอร์การสุ่มตัวอย่าง**: `temperature`, `top_p` และ `top_k` เลิกใช้งานแล้ว API จะไม่สนใจพารามิเตอร์เหล่านี้และแสดงข้อผิดพลาดในโมเดลรุ่นต่อๆ ไป
- **การตรวจสอบการโต้ตอบของโมเดลที่เติมไว้ล่วงหน้า**: ระบบไม่รองรับการเติมการโต้ตอบของโมเดลไว้ล่วงหน้าอีกต่อไป หากการโต้ตอบสุดท้ายที่ไม่ว่างเปล่าในคำขอเป็นการโต้ตอบ `model` API จะแสดงข้อผิดพลาด `400`

ด้านล่างนี้คือคำอธิบายโดยละเอียดและตัวอย่างโค้ดสำหรับการเปลี่ยนแปลง API แต่ละรายการ

### 1. การเลิกใช้งานพารามิเตอร์การสุ่มตัวอย่าง (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` และ `top_k` เลิกใช้งานแล้วและระบบจะไม่สนใจพารามิเตอร์เหล่านี้ ในโมเดลรุ่นต่อๆ ไป การระบุพารามิเตอร์เหล่านี้จะแสดงข้อผิดพลาด HTTP 400 **นำพารามิเตอร์เหล่านี้ออกจากคำขอทั้งหมด**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

หากต้องการปรับปรุงความแน่นอน ให้กำหนดคำแนะนำของระบบด้วยกฎที่ชัดเจนสำหรับกรณีการใช้งานเฉพาะของคุณ

### 2. การตรวจสอบการโต้ตอบของโมเดลที่เติมไว้ล่วงหน้า

ระบบไม่อนุญาตคำขอ API ที่สิ้นสุดด้วยการโต้ตอบที่มีบทบาทเป็นโมเดลที่ไม่ว่างเปล่า และจะแสดง**ข้อผิดพลาด HTTP 400**

#### ⚠️ หลีกเลี่ยง

ใน `generateContent` แบบเดิมหรือเพย์โหลด REST แบบดิบ ตอนนี้ระบบไม่อนุญาตให้สิ้นสุดด้วยการโต้ตอบที่มีบทบาทเป็นโมเดลแล้ว

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ การย้ายข้อมูลที่แนะนำ

หากแอปพลิเคชันของคุณเคยเติมการโต้ตอบของโมเดลไว้ล่วงหน้าเพื่อระงับคำนำหรือบังคับใช้การจัดรูปแบบ JSON ให้ใช้ `system_instruction` หรือ [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th) แทน

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## รายการตรวจสอบการย้ายข้อมูล

### Gemini 3.6 Flash

1. ติดตั้งทักษะโดยทำดังนี้

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. ใช้ทักษะโดยทำดังนี้

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. ติดตั้งทักษะโดยทำดังนี้

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. ใช้ทักษะโดยทำดังนี้

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### ย้ายข้อมูลไปยัง gemini-3.6-flash

- **อัปเดตรหัสโมเดล:** เปลี่ยนสตริงโมเดลเป้าหมายเป็น `gemini-3.6-flash`
- **นำพารามิเตอร์การสุ่มตัวอย่างที่เลิกใช้งานแล้วออก**
  - นำ `temperature`, `top_p` และ `top_k` ออกจากการกำหนดค่าการสร้าง
  - แทนที่ `thinking_budget` ด้วย Enum สตริง `thinking_level` ที่ตั้งค่าเป็น `"medium"` หรือ `"high"`
  - นำ `candidate_count` ออก (ไม่รองรับใน Gemini 3.x)
- **บังคับใช้กฎการตรวจสอบการโต้ตอบ**
  - นำการโต้ตอบของโมเดลที่เติมไว้ล่วงหน้าออก
  - ตรวจสอบว่าการโต้ตอบสุดท้ายของผู้ใช้มีข้อความที่ไม่ว่างเปล่า
- **ตรวจสอบการเรียกฟังก์ชัน**
  - ตรวจสอบว่าออบเจ็กต์ `FunctionResponse` ทั้งหมดมี `call_id` และ `name`
  - วางเนื้อหา Multimodal ไว้ในเพย์โหลดการตอบกลับ
  - จัดรูปแบบคำแนะนำแบบอินไลน์โดยใช้ `\\n\\n`
  - หากเห็นข้อผิดพลาด `Malformed_Function_Call` ที่เชื่อมโยงกับข้อความก่อนเครื่องมือ โปรดดู [วิธีแก้ปัญหาสำหรับข้อกำหนดข้อความก่อนเครื่องมือ](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=th#workarounds-for-pre-tool-text-requirements)
- **ข้อกำหนดพื้นฐานของ Gemini 3.x:** สำหรับการอัปเดต SDK และการเก็บรักษาลายเซ็นความคิด โปรดดูที่ [รายการตรวจสอบการย้ายข้อมูล Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=th#migration)

### ย้ายข้อมูลไปยัง gemini-3.5-flash-lite

- **อัปเดตรหัสโมเดล:** เปลี่ยนสตริงโมเดลเป้าหมายเป็น `gemini-3.5-flash-lite`
- **กำหนดค่าระดับความพยายามในการคิด**
  - สำหรับการแยก การกำหนดเส้นทาง หรือการจัดประเภทปริมาณมาก ให้ตั้งค่า `thinking_level` เป็น `"minimal"` (ค่าเริ่มต้น) เพื่อให้ได้ปริมาณงานสูงสุด
  - สำหรับ Subagent แบบอัตโนมัติที่มีการเรียกเครื่องมือ การเรียกใช้โค้ด หรือการให้เหตุผลหลายขั้นตอน ให้ตั้งค่า `thinking_level` เป็น `"medium"` หรือ `"high"` เพื่อป้องกันไม่ให้เครื่องมือหยุดทำงานก่อนเวลาอันควร
- **นำพารามิเตอร์ที่เลิกใช้งานแล้วออกและตรวจสอบการเรียกฟังก์ชัน:** ใช้[กฎเดียวกับ 3.6 Flash](#migrate-to-gemini-3-6-flash)
- **ข้อกำหนดพื้นฐานของ Gemini 3.x:** โปรดดู [รายการตรวจสอบการย้ายข้อมูล Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=th#migration)

## ขั้นตอนถัดไป

- ตรวจสอบสเปค API ใน[ภาพรวมของโมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)
- สำรวจการจัดระเบียบ Agent หลายรายการในคู่มือ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th)
- ทดสอบและปรับแต่งพรอมต์ใน [Google AI Studio](https://aistudio.google.com/?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-12 UTC"],[],[]]
