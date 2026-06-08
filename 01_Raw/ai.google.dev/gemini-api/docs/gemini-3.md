---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=th
fetched_at: 2026-06-08T05:28:31.013708+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# คู่มือนักพัฒนาซอฟต์แวร์ Gemini 3

Gemini 3 เป็นตระกูลโมเดลที่ชาญฉลาดที่สุดของเราในปัจจุบัน ซึ่งสร้างขึ้นบนพื้นฐานของ
การให้เหตุผลที่ล้ำสมัย โดยออกแบบมาเพื่อทำให้ไอเดียใดๆ เป็นจริงได้ด้วยการ
เชี่ยวชาญเวิร์กโฟลว์แบบ Agent การเขียนโค้ดแบบอัตโนมัติ และงานแบบ Multimodal ที่ซับซ้อน
คู่มือนี้ครอบคลุมฟีเจอร์หลักของกลุ่มผลิตภัณฑ์โมเดล Gemini 3 และวิธีใช้ประโยชน์จากโมเดลนี้ให้ได้มากที่สุด

[ลองใช้ Gemini 3.1 Pro เวอร์ชันตัวอย่าง](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=th)
[ลองใช้ Gemini 3 Flash เวอร์ชันตัวอย่าง](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=th)
[ลองใช้ Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=th)
[ลองใช้ Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=th)

สำรวจ[คอลเล็กชันแอป Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=th) เพื่อดูว่าโมเดลจัดการการให้เหตุผลขั้นสูง การเขียนโค้ดอัตโนมัติ และงานมัลติโมดัลที่ซับซ้อนได้อย่างไร

เริ่มต้นใช้งานด้วยโค้ดเพียงไม่กี่บรรทัด

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## พบกับซีรีส์ Gemini 3

Gemini 3.1 Pro เหมาะที่สุดสำหรับงานที่ซับซ้อนซึ่ง
ต้องใช้ความรู้เกี่ยวกับโลกในวงกว้างและการให้เหตุผลขั้นสูงในรูปแบบต่างๆ

Gemini 3 Flash เป็นโมเดลซีรีส์ 3 ล่าสุดของเราที่มีความสามารถอันชาญฉลาดระดับ Pro ใน
ความเร็วและราคาของ Flash

Nano Banana Pro (หรือที่เรียกว่ารูปภาพ Gemini 3 Pro) คือโมเดลการสร้างรูปภาพคุณภาพสูงสุดของเรา และ Nano Banana 2 (หรือที่เรียกว่ารูปภาพ Gemini 3.1 Flash) คือโมเดลที่มีปริมาณมาก ประสิทธิภาพสูง และมีราคาต่ำกว่า

Gemini 3.1 Flash-Lite คือโมเดลที่ใช้งานได้จริงของเรา ซึ่งสร้างขึ้นเพื่อโมเดลที่ประหยัดค่าใช้จ่ายและ
งานที่มีปริมาณมาก

| รหัสโมเดล | หน้าต่างบริบท (เข้า / ออก) | การตัดข้อมูล | การกำหนดราคา (อินพุต / เอาต์พุต)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | มกราคม 2025 | $0.25 (ข้อความ รูปภาพ วิดีโอ), $0.50 (เสียง) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | มกราคม 2025 | $0.25 (อินพุตข้อความ) / $0.067 (เอาต์พุตรูปภาพ)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | มกราคม 2025 | $2 / $12 (<200,000 โทเค็น)   $4 / $18 (>200,000 โทเค็น) |
| **gemini-3-flash-preview** | 1M / 64k | มกราคม 2025 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | มกราคม 2025 | $2 (ป้อนข้อความ) / $0.134 (เอาต์พุตรูปภาพ)\*\* |

*\* ราคาต่อโทเค็น 1 ล้านรายการ เว้นแต่จะระบุไว้เป็นอย่างอื่น*
*\*\* ราคาของรูปภาพจะแตกต่างกันไปตามความละเอียด ดูรายละเอียดได้ที่[หน้าการกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)*

ดูขีดจำกัดโดยละเอียด ราคา และข้อมูลเพิ่มเติมได้ที่[หน้าโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

## ฟีเจอร์ใหม่ของ API ใน Gemini 3

Gemini 3 มีพารามิเตอร์ใหม่ที่ออกแบบมาเพื่อช่วยให้นักพัฒนาแอปควบคุมเวลาในการตอบสนอง ต้นทุน และความเที่ยงตรงของโมเดลหลายรูปแบบได้มากขึ้น

### ระดับการคิด

โมเดลชุด Gemini 3 ใช้การคิดแบบไดนามิกโดยค่าเริ่มต้นเพื่อใช้เหตุผลผ่านพรอมต์ คุณสามารถใช้พารามิเตอร์ `thinking_level` ซึ่งควบคุมความลึก**สูงสุด**ของกระบวนการให้เหตุผลภายในของโมเดลก่อนที่จะสร้างคำตอบ Gemini 3 จะถือว่าระดับเหล่านี้เป็นการอนุญาตแบบสัมพัทธ์สำหรับการคิดมากกว่าการรับประกันโทเค็นที่เข้มงวด

หากไม่ได้ระบุ `thinking_level` ไว้ Gemini 3 จะใช้ `high` เป็นค่าเริ่มต้น หากต้องการให้โมเดลตอบกลับเร็วขึ้นและมีเวลาในการตอบสนองที่ต่ำลงเมื่อไม่จำเป็นต้องใช้การให้เหตุผลที่ซับซ้อน คุณสามารถจำกัดระดับการคิดของโมเดลไว้ที่ `low` ได้

| ระดับการคิด | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | คำอธิบาย |
| --- | --- | --- | --- | --- |
| **`minimal`** | สิ่งที่ทำไม่ได้ | รองรับ (ค่าเริ่มต้น) | สิ่งที่ทำได้ | ตรงกับการตั้งค่า "ไม่ต้องคิด" สำหรับคำค้นหาส่วนใหญ่ โมเดลอาจคิดน้อยมากสำหรับงานการเขียนโค้ดที่ซับซ้อน ลดเวลาในการตอบสนองสำหรับแอปพลิเคชันแชทหรือแอปพลิเคชันที่มีการส่งข้อความปริมาณมาก โปรดทราบว่า `minimal` ไม่รับประกันว่าการคิดจะหยุดทำงาน |
| **`low`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | ลดเวลาในการตอบสนองและต้นทุน เหมาะที่สุดสำหรับการปฏิบัติตามคำสั่งง่ายๆ แชท หรือแอปพลิเคชันที่มีปริมาณงานสูง |
| **`medium`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | การคิดแบบสมดุลสำหรับงานส่วนใหญ่ |
| **`high`** | รองรับ (ค่าเริ่มต้น, ไดนามิก) | รองรับ (ไดนามิก) | รองรับ (ค่าเริ่มต้น, ไดนามิก) | เพิ่มความลึกในการให้เหตุผลสูงสุด โมเดลอาจใช้เวลานานขึ้นอย่างมากในการ สร้างโทเค็นเอาต์พุตแรก (ที่ไม่ใช่การคิด) แต่เอาต์พุตจะได้รับการพิจารณาอย่างรอบคอบมากขึ้น |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### ความละเอียดของสื่อ

Gemini 3 เปิดตัวการควบคุมการประมวลผลวิสัยทัศน์แบบหลายรูปแบบอย่างละเอียดโดยใช้พารามิเตอร์ `media_resolution` ความละเอียดที่สูงขึ้นจะช่วยปรับปรุงความสามารถของโมเดลในการ
อ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง
พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุด
ที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**

ตอนนี้คุณสามารถตั้งค่าความละเอียดเป็น `media_resolution_low`,
`media_resolution_medium`, `media_resolution_high` หรือ
`media_resolution_ultra_high` ต่อเสียงประกอบแต่ละรายการหรือทั่วโลก (ผ่าน
`generation_config`, ความละเอียดสูงพิเศษไม่พร้อมใช้งาน) หากไม่ได้ระบุ
โมเดลจะใช้ค่าเริ่มต้นที่เหมาะสมที่สุดตามประเภทสื่อ

**การตั้งค่าที่แนะนำ**

| ประเภทสื่อ | การตั้งค่าที่แนะนำ | โทเค็นสูงสุด | คำแนะนำในการใช้งาน |
| --- | --- | --- | --- |
| **รูปภาพ** | `media_resolution_high` | 1120 | แนะนำสำหรับงานวิเคราะห์รูปภาพส่วนใหญ่เพื่อให้มั่นใจว่ามีคุณภาพสูงสุด |
| **PDF** | `media_resolution_medium` | 560 | เหมาะสำหรับการทำความเข้าใจเอกสาร โดยปกติแล้วคุณภาพจะอิ่มตัวที่ `medium` การเพิ่มเป็น `high` แทบจะไม่ช่วยปรับปรุงผลลัพธ์ OCR สำหรับเอกสารมาตรฐาน |
| **วิดีโอ** (ทั่วไป) | `media_resolution_low` (หรือ `media_resolution_medium`) | 70 (ต่อเฟรม) | **หมายเหตุ:** สำหรับวิดีโอ ระบบจะถือว่าการตั้งค่า `low` และ `medium` เหมือนกัน (70 โทเค็น) เพื่อเพิ่มประสิทธิภาพการใช้บริบท ซึ่งเพียงพอสำหรับงานการจดจำและการอธิบายการกระทำส่วนใหญ่ |
| **วิดีโอ** (มีข้อความจำนวนมาก) | `media_resolution_high` | 280 (ต่อเฟรม) | จำเป็นเฉพาะเมื่อ Use Case เกี่ยวข้องกับการอ่านข้อความหนาแน่น (OCR) หรือรายละเอียดเล็กๆ ภายในเฟรมวิดีโอ |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### อุณหภูมิ

สำหรับโมเดล Gemini 3 ทั้งหมด เราขอแนะนำอย่างยิ่งให้คงพารามิเตอร์อุณหภูมิ
ไว้ที่ค่าเริ่มต้น `1.0`

แม้ว่าโมเดลก่อนหน้ามักจะได้รับประโยชน์จากการปรับอุณหภูมิเพื่อควบคุมความคิดสร้างสรรค์เทียบกับเชิงกำหนด แต่ความสามารถในการให้เหตุผลของ Gemini 3 ได้รับการเพิ่มประสิทธิภาพสำหรับการตั้งค่าเริ่มต้น การเปลี่ยนอุณหภูมิ (ตั้งค่าต่ำกว่า 1.0) อาจ
ทำให้เกิดลักษณะการทำงานที่ไม่คาดคิด เช่น การวนซ้ำหรือประสิทธิภาพลดลง
โดยเฉพาะในงานทางคณิตศาสตร์หรือการให้เหตุผลที่ซับซ้อน

### ลายเซ็นความคิด

Gemini 3 ใช้[ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th)เพื่อ
รักษาบริบทการให้เหตุผลในการเรียก API ลายเซ็นเหล่านี้คือการแสดงที่เข้ารหัส
กระบวนการคิดภายในของโมเดล คุณต้องส่งลายเซ็นเหล่านี้กลับไปยังโมเดลในคำขอของคุณตามที่ได้รับมาทุกประการเพื่อให้โมเดลยังคงมีความสามารถในการให้เหตุผล

- **การเรียกใช้ฟังก์ชัน (เข้มงวด):** API จะบังคับใช้การตรวจสอบที่เข้มงวดกับ "เทิร์นปัจจุบัน" หากไม่มีลายเซ็น ระบบจะแสดงข้อผิดพลาด 400
- **ข้อความ/แชท:** ระบบไม่ได้บังคับใช้การตรวจสอบอย่างเคร่งครัด แต่การละเว้นลายเซ็นจะทำให้คุณภาพการให้เหตุผลและคำตอบของโมเดลลดลง
- **การสร้าง/แก้ไขรูปภาพ (เข้มงวด)**: API จะบังคับใช้การตรวจสอบอย่างเข้มงวดกับทุกส่วนของโมเดล รวมถึง `thoughtSignature` หากไม่มีลายเซ็น ระบบจะแสดงข้อผิดพลาด 400

#### การเรียกใช้ฟังก์ชัน (การตรวจสอบอย่างเข้มงวด)

เมื่อ Gemini สร้าง `functionCall` ระบบจะใช้ `thoughtSignature` เพื่อ
ประมวลผลเอาต์พุตของเครื่องมืออย่างถูกต้องในเทิร์นถัดไป "เทิร์นปัจจุบัน"
ประกอบด้วยขั้นตอนทั้งหมดของโมเดล (`functionCall`) และผู้ใช้ (`functionResponse`) ที่
เกิดขึ้นนับตั้งแต่ข้อความ **User** `text` มาตรฐานล่าสุด

- **การเรียกใช้ฟังก์ชันเดียว:** ส่วน `functionCall` มีลายเซ็น คุณต้องส่งคืน
- **การเรียกใช้ฟังก์ชันแบบขนาน:** เฉพาะส่วน `functionCall` แรกในรายการเท่านั้นที่จะมีลายเซ็น คุณต้องส่งคืนชิ้นส่วนตามลำดับที่ได้รับ
- **หลายขั้นตอน (ตามลำดับ):** หากโมเดลเรียกใช้เครื่องมือ รับผลลัพธ์
  และเรียกใช้เครื่องมือ*อีก*เครื่องมือหนึ่ง (ภายในเทิร์นเดียวกัน) การเรียกใช้ฟังก์ชัน**ทั้ง 2 รายการ**จะมีลายเซ็น คุณต้องส่งคืนลายเซ็นสะสม**ทั้งหมด**ในประวัติ

#### ข้อความและการสตรีม

สำหรับการแชทหรือการสร้างข้อความมาตรฐาน ระบบไม่รับประกันการมีอยู่ของลายเซ็น

- **ไม่ใช่การสตรีม**: ส่วนเนื้อหาสุดท้ายของการตอบกลับอาจมี
  `thoughtSignature` แม้ว่าจะไม่ได้มีอยู่เสมอไปก็ตาม หากมีการส่งกลับมา คุณ
  ควรส่งกลับเพื่อรักษาประสิทธิภาพที่ดีที่สุด
- **การสตรีม**: หากมีการสร้างลายเซ็น ลายเซ็นอาจอยู่ในก้อนข้อมูลสุดท้าย
  ซึ่งมีส่วนข้อความที่ว่างเปล่า ตรวจสอบว่าตัวแยกวิเคราะห์สตรีมของคุณตรวจสอบลายเซ็น
  แม้ว่าฟิลด์ข้อความจะว่างเปล่าก็ตาม

#### การสร้างและแก้ไขรูปภาพ

สำหรับ `gemini-3-pro-image-preview` และ `gemini-3.1-flash-image-preview` ลายเซ็นความคิด มีความสำคัญอย่างยิ่งต่อ การแก้ไขโดยใช้การสนทนา เมื่อขอให้โมเดลแก้ไขรูปภาพ โมเดลจะอิงตาม`thoughtSignature`จากเทิร์นก่อนหน้าเพื่อทำความเข้าใจองค์ประกอบและตรรกะของรูปภาพต้นฉบับ

- **การแก้ไข:** ระบบรับประกันลายเซ็นในส่วนแรกหลังจากความคิด
  ของการตอบกลับ (`text` หรือ `inlineData`) และในทุกส่วน `inlineData`
  ต่อๆ ไป คุณต้องส่งคืนลายเซ็นทั้งหมดเหล่านี้เพื่อหลีกเลี่ยงข้อผิดพลาด

#### ตัวอย่างโค้ด

#### การเรียกใช้ฟังก์ชันแบบหลายขั้นตอน (ตามลำดับ)

ผู้ใช้ถามคำถามที่ต้องใช้ 2 ขั้นตอนแยกกัน (ตรวจสอบเที่ยวบิน -> จองแท็กซี่) ในครั้งเดียว  
  
**ขั้นตอนที่ 1: โมเดลเรียกใช้เครื่องมือเที่ยวบิน**  
โมเดลจะแสดงลายเซ็น `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**ขั้นตอนที่ 2: ผู้ใช้ส่งผลการค้นหาเที่ยวบิน**  
เราต้องส่ง `<Sig_A>` กลับเพื่อรักษาลำดับความคิดของโมเดล

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**ขั้นตอนที่ 3: โมเดลเรียกใช้เครื่องมือแท็กซี่**  
โมเดลจดจำเรื่องเที่ยวบินล่าช้าผ่าน `<Sig_A>` และตัดสินใจจองแท็กซี่ ซึ่งจะสร้างลายเซ็น*ใหม่* `<Sig_B>`

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**ขั้นตอนที่ 4: ผู้ใช้ส่งผลแท็กซี่**  
หากต้องการดำเนินการให้เสร็จสมบูรณ์ คุณต้องส่งทั้งเชนกลับมา ซึ่งได้แก่ `<Sig_A>` และ `<Sig_B>`

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### การเรียกใช้ฟังก์ชันแบบคู่ขนาน

ผู้ใช้ถามว่า "ตรวจสอบสภาพอากาศในปารีสและลอนดอน" โมเดลจะแสดงผลการเรียกใช้ฟังก์ชัน 2 รายการในคำตอบเดียว

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### การให้เหตุผลแบบข้อความ/ในบริบท (ไม่มีการตรวจสอบ)

ผู้ใช้ถามคำถามที่ต้องใช้การให้เหตุผลในบริบทโดยไม่ต้องใช้เครื่องมือภายนอก แม้ว่าจะไม่ได้ตรวจสอบอย่างเข้มงวด แต่การใส่ลายเซ็นจะช่วยให้โมเดลคงห่วงโซ่การให้เหตุผลสำหรับคำถามติดตามผลได้

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### การสร้างและแก้ไขรูปภาพ

สำหรับการสร้างรูปภาพ ระบบจะตรวจสอบลายเซ็นอย่างเข้มงวด โดยจะปรากฏใน**ส่วนแรก** (ข้อความหรือรูปภาพ) และ**ส่วนรูปภาพทั้งหมดที่ตามมา** โดยจะต้องส่งคืนทั้งหมดในรอบถัดไป

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### การย้ายข้อมูลจากรุ่นอื่นๆ

หากคุณโอนการติดตามการสนทนาจากโมเดลอื่น (เช่น Gemini 2.5) หรือแทรกการเรียกใช้ฟังก์ชันที่กำหนดเองซึ่งไม่ได้สร้างโดย Gemini 3 คุณจะไม่มีลายเซ็นที่ถูกต้อง

หากต้องการข้ามการตรวจสอบอย่างเข้มงวดในสถานการณ์ที่เฉพาะเจาะจงเหล่านี้ ให้ป้อนฟิลด์ด้วยสตริงจำลองที่เฉพาะเจาะจงนี้
`"thoughtSignature": "context_engineering_is_the_way
to_go"`

### เอาต์พุตที่มีโครงสร้างด้วยเครื่องมือ

โมเดล Gemini 3 ช่วยให้คุณรวม[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)เข้ากับเครื่องมือในตัวได้ ซึ่งรวมถึง
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th), [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th), [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) และ[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### การสร้างรูปภาพ

Gemini 3.1 Flash สำหรับรูปภาพและ Gemini 3 Pro สำหรับรูปภาพช่วยให้คุณสร้างและแก้ไขรูปภาพ
จากพรอมต์ข้อความได้ โดยจะใช้การให้เหตุผลเพื่อ "คิด" ตามพรอมต์ และสามารถดึงข้อมูลแบบเรียลไทม์ เช่น พยากรณ์อากาศหรือแผนภูมิหุ้น ก่อนที่จะใช้การอ้างอิงจาก [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) ก่อนสร้างรูปภาพที่มีความเที่ยงตรงสูง

**ความสามารถใหม่และที่ได้รับการปรับปรุง**

- **การแสดงข้อความและ 4K:** สร้างข้อความและไดอะแกรมที่คมชัดและอ่านได้ด้วยความละเอียดสูงสุด 2K และ 4K
- **การสร้างแบบอิงตามข้อมูล:** ใช้`google_search`เครื่องมือเพื่อยืนยันข้อเท็จจริงและ
  สร้างภาพตามข้อมูลในโลกแห่งความเป็นจริง การอิงตามข้อมูลด้วย Google *Image*
  Search พร้อมใช้งานสำหรับ Gemini 3.1 Flash Image
- **การแก้ไขโดยใช้การสนทนา:** การแก้ไขรูปภาพแบบหลายรอบโดยเพียงแค่ขอให้เปลี่ยนแปลง (เช่น "เปลี่ยนพื้นหลังเป็นพระอาทิตย์ตก") เวิร์กโฟลว์นี้อาศัย**ลายเซ็นความคิด**เพื่อรักษาบริบทภาพระหว่างการสนทนา

ดูรายละเอียดทั้งหมดเกี่ยวกับสัดส่วนการแสดงผล เวิร์กโฟลว์การแก้ไข และตัวเลือกการกำหนดค่าได้ใน[คู่มือการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**ตัวอย่างคำตอบ**

![สภาพอากาศ โตเกียว](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=th)

### การรันโค้ดด้วยรูปภาพ

Gemini 3 Flash สามารถมองเห็นเป็นกระบวนการตรวจสอบที่ใช้งานได้จริง ไม่ใช่แค่การมองแบบคงที่
เมื่อรวมการให้เหตุผลเข้ากับ[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) โมเดลจะวางแผน จากนั้นเขียนและ
เรียกใช้โค้ด Python เพื่อซูมเข้า ครอบตัด ใส่คำอธิบายประกอบ หรือจัดการรูปภาพ
ทีละขั้นตอนเพื่ออ้างอิงคำตอบด้วยภาพ

**กรณีการใช้งาน**

- **ซูมและตรวจสอบ:** โมเดลจะตรวจหาโดยนัยเมื่อรายละเอียดมีขนาดเล็กเกินไป (เช่น การอ่านมาตรวัดหรือหมายเลขซีเรียลที่อยู่ไกล) และเขียนโค้ดเพื่อครอบตัด และตรวจสอบพื้นที่อีกครั้งที่ความละเอียดสูงขึ้น
- **คณิตศาสตร์และการลงจุดแบบภาพ:** โมเดลสามารถทำการคำนวณหลายขั้นตอนโดยใช้โค้ด (เช่น การรวมรายการในใบเสร็จ หรือการสร้างแผนภูมิ Matplotlib จากข้อมูลที่ดึงออกมา)
- **การอธิบายประกอบรูปภาพ:** โมเดลสามารถวาดลูกศร กรอบล้อม หรือคำอธิบายประกอบอื่นๆ
  ลงในรูปภาพโดยตรงเพื่อตอบคำถามเชิงพื้นที่ เช่น "ควรวาง
  รายการนี้ไว้ที่ไหน"

หากต้องการเปิดใช้การคิดเชิงภาพ ให้กำหนดค่า[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)เป็นเครื่องมือ โมเดลจะใช้
โค้ดเพื่อปรับแต่งรูปภาพโดยอัตโนมัติเมื่อจำเป็น

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการเรียกใช้โค้ดด้วยรูปภาพได้ที่[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#images)

### คำตอบของฟังก์ชันมัลติโมดัล

[การเรียกใช้ฟังก์ชันแบบหลายรูปแบบ](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#multimodal)
ช่วยให้ผู้ใช้ได้รับคำตอบของฟังก์ชันที่มี
ออบเจ็กต์แบบหลายรูปแบบ ซึ่งช่วยให้ใช้ความสามารถในการเรียกใช้ฟังก์ชัน
ของโมเดลได้ดียิ่งขึ้น การเรียกใช้ฟังก์ชันมาตรฐานรองรับเฉพาะการตอบกลับฟังก์ชันที่เป็นข้อความ
เท่านั้น

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### รวมเครื่องมือในตัวและการเรียกใช้ฟังก์ชัน

Gemini 3 อนุญาตให้ใช้เครื่องมือในตัว (เช่น Google Search, บริบท URL และ[อื่นๆ](https://ai.google.dev/gemini-api/docs/tools?hl=th)) และเครื่องมือ[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ที่กำหนดเองในการเรียก API เดียวกัน ซึ่งช่วยให้เวิร์กโฟลว์มีความซับซ้อนมากขึ้น ดูข้อมูลเพิ่มเติมได้ที่หน้า[ชุดเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## การย้ายข้อมูลจาก Gemini 2.5

Gemini 3 เป็นตระกูลโมเดลที่มีความสามารถมากที่สุดของเราในปัจจุบัน และมีการปรับปรุงทีละขั้นเมื่อเทียบกับ Gemini 2.5 เมื่อย้ายข้อมูล ให้พิจารณาสิ่งต่อไปนี้

- **การคิด:** หากก่อนหน้านี้คุณใช้วิศวกรรมพรอมต์ที่ซับซ้อน (เช่น เชนออฟทอท) เพื่อบังคับให้ Gemini 2.5 ให้เหตุผล ให้ลองใช้ Gemini 3 กับ `thinking_level: "high"` และพรอมต์ที่เรียบง่าย
- **การตั้งค่าอุณหภูมิ:** หากโค้ดที่มีอยู่ตั้งค่าอุณหภูมิอย่างชัดเจน
  (โดยเฉพาะค่าต่ำสำหรับเอาต์พุตที่แน่นอน) เราขอแนะนำให้นำพารามิเตอร์นี้ออก
  และใช้ค่าเริ่มต้นของ Gemini 3 ซึ่งคือ 1.0 เพื่อหลีกเลี่ยงปัญหาการวนซ้ำที่อาจเกิดขึ้น
  หรือประสิทธิภาพลดลงในงานที่ซับซ้อน
- **การทำความเข้าใจ PDF และเอกสาร:**
  หากคุณอาศัยลักษณะการทำงานที่เฉพาะเจาะจงสำหรับการแยกวิเคราะห์เอกสารที่มีข้อมูลหนาแน่น ให้ทดสอบการตั้งค่า `media_resolution_high` ใหม่
  เพื่อให้มั่นใจว่าข้อมูลจะยังคงถูกต้องต่อไป
- **การใช้โทเค็น:** การย้ายข้อมูลไปใช้ค่าเริ่มต้นของ Gemini 3 อาจ**เพิ่ม**การใช้โทเค็น
  สำหรับ PDF แต่**ลด**การใช้โทเค็นสำหรับวิดีโอ หากคำขอเกิน
  หน้าต่างบริบทเนื่องจากความละเอียดเริ่มต้นสูงขึ้น เราขอแนะนำให้
  ลดความละเอียดของสื่ออย่างชัดเจน
- **การแบ่งกลุ่มรูปภาพ:** Gemini 3 Pro หรือ Gemini 3 Flash ไม่รองรับความสามารถในการแบ่งกลุ่มรูปภาพ (การแสดงผลมาสก์ระดับพิกเซลสำหรับออบเจ็กต์) สำหรับภาระงานที่ต้องใช้การแบ่งกลุ่มรูปภาพดั้งเดิม เราขอแนะนำให้ใช้ Gemini 2.5 Flash ต่อไปโดยปิดการคิด หรือใช้ [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)
- **การใช้คอมพิวเตอร์:** Gemini 3 Pro และ Gemini 3 Flash รองรับ[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th) คุณไม่จำเป็นต้องใช้โมเดลแยกต่างหากเพื่อเข้าถึงเครื่องมือการใช้งานคอมพิวเตอร์ ซึ่งต่างจากซีรีส์ 2.5
- **การรองรับเครื่องมือ**: ตอนนี้โมเดล Gemini 3 [รองรับการรวมเครื่องมือในตัวเข้ากับการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)แล้ว และโมเดล Gemini 3 ยังรองรับ[การอ้างอิงจาก Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) ด้วย
- **จำนวนคำตอบ**: โมเดล Gemini 3 ไม่รองรับ `candidateCount > 1`
  การตั้งค่าพารามิเตอร์นี้เป็นค่าที่มากกว่า `1` จะทําให้ระบบแสดงข้อผิดพลาด 400

## ความเข้ากันได้กับ OpenAI

สำหรับผู้ใช้ที่ใช้[เลเยอร์ความเข้ากันได้ของ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)
ระบบจะแมปพารามิเตอร์มาตรฐาน (`reasoning_effort` ของ OpenAI) กับ
พารามิเตอร์ที่เทียบเท่าของ Gemini (`thinking_level`) โดยอัตโนมัติ

## แนวทางปฏิบัติแนะนำในการเขียนพรอมต์

Gemini 3 เป็นโมเดลการให้เหตุผล ซึ่งจะเปลี่ยนวิธีที่คุณควรใช้พรอมต์

- **วิธีการที่ชัดเจน:** ระบุพรอมต์อินพุตให้กระชับ Gemini 3 ตอบสนองต่อคำสั่งที่ชัดเจนและตรงไปตรงมาได้ดีที่สุด ซึ่งอาจวิเคราะห์เทคนิควิศวกรรมพรอมต์ (Prompt Engineering) ที่ซับซ้อนหรือมีรายละเอียดมากเกินไปที่ใช้กับโมเดลรุ่นเก่ามากเกินไป
- **ความละเอียดของเอาต์พุต:** โดยค่าเริ่มต้น Gemini 3 จะมีความละเอียดน้อยกว่าและต้องการให้คำตอบที่ตรงไปตรงมาและมีประสิทธิภาพ หากกรณีการใช้งานของคุณต้องมีลักษณะการสนทนาหรือลักษณะ "แชท" มากขึ้น คุณต้องชี้นำโมเดลอย่างชัดเจนในพรอมต์ (เช่น "อธิบายเรื่องนี้ในฐานะผู้ช่วยที่เป็นมิตรและช่างพูด")
- **การจัดการบริบท:** เมื่อทำงานกับชุดข้อมูลขนาดใหญ่ (เช่น หนังสือทั้งเล่ม ฐานโค้ด หรือวิดีโอยาว) ให้วางคำสั่งหรือคำถามที่เฉพาะเจาะจงไว้ท้ายพรอมต์หลังจากบริบทของข้อมูล ยึดการให้เหตุผลของโมเดลกับข้อมูลที่ให้ไว้โดยเริ่มคำถามด้วยวลี เช่น "จากข้อมูลด้านบน..."

ดูข้อมูลเพิ่มเติมเกี่ยวกับกลยุทธ์การออกแบบพรอมต์ได้ใน[คู่มือวิศวกรรมพรอมต์ (Prompt Engineering)](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=th)

## คำถามที่พบบ่อย

1. **การตัดข้อมูลความรู้สำหรับ Gemini 3 คือเมื่อใด** โมเดล Gemini 3 มีการตัดข้อมูลความรู้คือเดือนมกราคม 2025 หากต้องการข้อมูลล่าสุด ให้ใช้เครื่องมือ[การอ้างอิงจาก Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
2. **ขีดจำกัดของหน้าต่างบริบทคืออะไร** โมเดล Gemini 3 รองรับหน้าต่างบริบทอินพุตขนาด 1 ล้าน
   โทเค็นและเอาต์พุตสูงสุด 64,000 โทเค็น
3. **Gemini 3 มีแพ็กเกจฟรีไหม** Gemini 3 Flash
   `gemini-3-flash-preview` และ 3.1 Flash-Lite `gemini-3.1-flash-lite` มี
   ระดับฟรีใน Gemini API คุณสามารถทดลองใช้ Gemini 3.1 Pro และ 3 Flash ได้ฟรีใน
   Google AI Studio แต่จะไม่มีระดับฟรีสำหรับ
   `gemini-3.1-pro-preview` ใน Gemini API
4. **โค้ด `thinking_budget` เก่าของฉันจะยังใช้งานได้ไหม** ได้ `thinking_budget` ยังคงรองรับการใช้งานกับเวอร์ชันก่อนหน้า แต่เราขอแนะนำให้ย้ายข้อมูลไปยัง `thinking_level` เพื่อให้ได้ประสิทธิภาพที่คาดการณ์ได้มากขึ้น อย่าใช้ทั้ง 2 อย่างในคำขอเดียวกัน
5. **Gemini 3 รองรับ Batch API ไหม** ได้ Gemini 3 รองรับ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)
6. **ระบบรองรับการแคชบริบทไหม** ได้ Gemini 3 รองรับ[การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)
7. **Gemini 3 รองรับเครื่องมือใดบ้าง** Gemini 3 รองรับ [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th), [การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th), [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th), [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) และ[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) นอกจากนี้ยังรองรับ[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)มาตรฐานสำหรับเครื่องมือที่กำหนดเอง
   และ[ใช้ร่วมกับเครื่องมือในตัว](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)
8. **`gemini-3.1-pro-preview-customtools` คืออะไร** หากคุณใช้ `gemini-3.1-pro-preview` และโมเดลไม่สนใจเครื่องมือที่กำหนดเองของคุณเพื่อใช้คำสั่ง Bash ให้ลองใช้โมเดล `gemini-3.1-pro-preview-customtools` แทน ดูข้อมูลเพิ่มเติมได้[ที่นี่](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th#gemini-31-pro-preview-customtools)

## ขั้นตอนถัดไป

- เริ่มต้นใช้งาน [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=th#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- ดูคำแนะนำเฉพาะสำหรับ Cookbook เกี่ยวกับ[ระดับการพิจารณา](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=th#gemini3)และวิธีย้ายข้อมูลจากงบประมาณการพิจารณาไปยังระดับการพิจารณา

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-04 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-04 UTC"],[],[]]
