---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=th
fetched_at: 2026-07-20T04:37:04.766279+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e02\u0e2d\u0e07\u0e2a\u0e37\u0e48\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความละเอียดของสื่อ

พารามิเตอร์ `media_resolution` จะควบคุมวิธีที่ Gemini API ประมวลผลอินพุตสื่อ เช่น รูปภาพ วิดีโอ และเอกสาร PDF โดยการกำหนด**จำนวนโทเค็นสูงสุด**ที่จัดสรรไว้สำหรับอินพุตสื่อ ซึ่งจะช่วยให้คุณปรับสมดุลคุณภาพของคำตอบกับเวลาในการตอบสนองและค่าใช้จ่ายได้ ดูการตั้งค่าต่างๆ ค่าเริ่มต้น และวิธีที่การตั้งค่าเหล่านี้สอดคล้องกับโทเค็นได้ที่ส่วน[จำนวนโทเค็น](#token-counts)

คุณสามารถกำหนดค่าความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการ (รายการเนื้อหา) ภายในคำขอ (Gemini 3 เท่านั้น)

## ความละเอียดของสื่อต่อรายการเนื้อหา (Gemini 3 เท่านั้น)

Gemini 3 ช่วยให้คุณตั้งค่าความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการภายในคำขอได้ ซึ่งจะช่วยให้เพิ่มประสิทธิภาพการใช้โทเค็นได้อย่างละเอียด คุณสามารถผสมระดับความละเอียดในคำขอเดียวได้ เช่น ใช้ความละเอียดสูงสำหรับไดอะแกรมที่ซับซ้อน และใช้ความละเอียดต่ำสำหรับรูปภาพตามบริบทอย่างง่าย

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
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
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
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
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## ค่าความละเอียดที่ใช้ได้

Gemini API กำหนดระดับความละเอียดของสื่อดังต่อไปนี้

- `unspecified`: การตั้งค่าเริ่มต้น จำนวนโทเค็นสำหรับระดับนี้จะแตกต่างกันอย่างมากระหว่าง Gemini 3 กับโมเดล Gemini รุ่นก่อนหน้า
- `low`: จำนวนโทเค็นน้อยลง ส่งผลให้ประมวลผลได้เร็วขึ้นและมีต้นทุนต่ำลง แต่มีรายละเอียดน้อยลง
- `medium`: ความสมดุลระหว่างรายละเอียด ต้นทุน และเวลาในการตอบสนอง
- `high`: จำนวนโทเค็นที่สูงขึ้น ซึ่งให้รายละเอียดเพิ่มเติมแก่โมเดลในการทำงาน แต่จะทำให้เวลาในการตอบสนองและค่าใช้จ่ายเพิ่มขึ้น
- `ultra_high` (ต่อรายการเนื้อหาเท่านั้น): จำนวนโทเค็นสูงสุดที่จำเป็นสำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น [การใช้งานคอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

โปรดทราบว่า `high` ให้ประสิทธิภาพสูงสุดสำหรับกรณีการใช้งานส่วนใหญ่

จำนวนโทเค็นที่แน่นอนซึ่งสร้างขึ้นสำหรับแต่ละระดับจะขึ้นอยู่กับทั้ง**ประเภทสื่อ** (รูปภาพ วิดีโอ PDF) และ**เวอร์ชันโมเดล**

## จำนวนโทเค็น

ตารางด้านล่างสรุปจำนวนโทเค็นโดยประมาณสำหรับค่า `media_resolution` และประเภทสื่อแต่ละรายการต่อตระกูลโมเดล

**โมเดล Gemini 3**

| MediaResolution | รูปภาพ | วิดีโอ | PDF |
| --- | --- | --- | --- |
| `unspecified` (ค่าเริ่มต้น) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + ข้อความเนทีฟ |
| `medium` | 560 | 70 | 560 + ข้อความเนทีฟ |
| `high` | 1120 | 280 | 1120 + ข้อความเนทีฟ |
| `ultra_high` | 2240 | ไม่มี | ไม่มี |

## การเลือกความละเอียดที่เหมาะสม

- **ค่าเริ่มต้น (`unspecified`):** เริ่มต้นด้วยค่าเริ่มต้น โดยได้รับการปรับแต่งให้มีความสมดุลที่ดีระหว่างคุณภาพ เวลาในการตอบสนอง และต้นทุนสำหรับกรณีการใช้งานที่พบบ่อยที่สุด
- **`low`:** ใช้ในสถานการณ์ที่ต้นทุนและเวลาในการตอบสนองมีความสำคัญสูงสุด และรายละเอียดแบบละเอียดมีความสำคัญน้อยกว่า
- **`medium` / `high`:** เพิ่มความละเอียดเมื่องานต้องทำความเข้าใจรายละเอียดที่ซับซ้อนภายในสื่อ ซึ่งมักจำเป็นสำหรับการวิเคราะห์ภาพที่ซับซ้อน การอ่านแผนภูมิ หรือการทำความเข้าใจเอกสารที่มีข้อมูลหนาแน่น
- **`ultra_high`** - ใช้ได้กับการตั้งค่าต่อรายการเนื้อหาเท่านั้น แนะนําสําหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น การใช้คอมพิวเตอร์ หรือในกรณีที่การทดสอบแสดงให้เห็นว่ามีการปรับปรุงที่ชัดเจนเมื่อเทียบกับ `high`
- **การควบคุมต่อรายการเนื้อหา (Gemini 3):** เพิ่มประสิทธิภาพการใช้โทเค็น เช่น ในพรอมต์ที่มีรูปภาพหลายรูป ให้ใช้ `high` สำหรับไดอะแกรมที่ซับซ้อน และใช้ `low` หรือ `medium` สำหรับรูปภาพตามบริบทที่เรียบง่ายกว่า

**การตั้งค่าที่แนะนำ**

รายการต่อไปนี้คือการตั้งค่าความละเอียดของสื่อที่แนะนำสำหรับสื่อแต่ละประเภทที่รองรับ

| ประเภทสื่อ | การตั้งค่าที่แนะนำ | โทเค็นสูงสุด | คำแนะนำในการใช้งาน |
| --- | --- | --- | --- |
| **รูปภาพ** | `high` | 1120 | แนะนำสำหรับงานวิเคราะห์รูปภาพส่วนใหญ่เพื่อให้มั่นใจว่ามีคุณภาพสูงสุด |
| **PDF** | `medium` | 560 | เหมาะสำหรับการทำความเข้าใจเอกสาร โดยปกติคุณภาพจะอิ่มตัวที่ `medium` การเพิ่มเป็น `high` แทบจะไม่ช่วยปรับปรุงผลลัพธ์ OCR สำหรับเอกสารมาตรฐาน |
| **วิดีโอ** (ทั่วไป) | `low` (หรือ `medium`) | 70 (ต่อเฟรม) | **หมายเหตุ:** สำหรับวิดีโอ ระบบจะถือว่าการตั้งค่า `low` และ `medium` เหมือนกัน (70 โทเค็น) เพื่อเพิ่มประสิทธิภาพการใช้บริบท ซึ่งเพียงพอสำหรับงานการจดจำและการอธิบายการกระทำส่วนใหญ่ |
| **วิดีโอ** (มีข้อความจำนวนมาก) | `high` | 280 (ต่อเฟรม) | จำเป็นเฉพาะเมื่อ Use Case เกี่ยวข้องกับการอ่านข้อความหนาแน่น (OCR) หรือรายละเอียดเล็กๆ ภายในเฟรมวิดีโอ |

โปรดทดสอบและประเมินผลกระทบของการตั้งค่าความละเอียดต่างๆ ในแอปพลิเคชันเสมอ เพื่อหาจุดสมดุลที่ดีที่สุดระหว่างคุณภาพ เวลาในการตอบสนอง และต้นทุน

## สรุปความเข้ากันได้ของเวอร์ชัน

- การตั้งค่า `resolution` ในเนื้อหาแต่ละรายการ**ใช้ได้เฉพาะกับโมเดล Gemini 3**

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับความสามารถแบบหลายรูปแบบของ Gemini API ได้ในคำแนะนำเกี่ยวกับ[การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th) [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th) และ[การทำความเข้าใจเอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-06 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-06 UTC"],[],[]]
