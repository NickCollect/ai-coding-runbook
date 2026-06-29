---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=th
fetched_at: 2026-06-29T05:38:11.191379+00:00
title: "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e19\u0e31\u0e01\u0e1e\u0e31\u0e12\u0e19\u0e32\u0e0b\u0e2d\u0e1f\u0e15\u0e4c\u0e41\u0e27\u0e23\u0e4c Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)

ส่งความคิดเห็น

# คู่มือสำหรับนักพัฒนาซอฟต์แวร์ Gemini 3

Gemini 3 เป็นกลุ่มผลิตภัณฑ์โมเดลที่ชาญฉลาดที่สุดของเราในปัจจุบัน ซึ่งสร้างขึ้นจากพื้นฐานของการให้เหตุผลที่ล้ำสมัย โดยได้รับการออกแบบมาเพื่อทำให้ทุกไอเดียเป็นจริงได้ด้วยการเชี่ยวชาญเวิร์กโฟลว์แบบ Agentic AI, การเขียนโค้ดอัตโนมัติ และงานที่ซับซ้อนแบบหลายรูปแบบ
คู่มือนี้จะครอบคลุมฟีเจอร์หลักของกลุ่มผลิตภัณฑ์โมเดล Gemini 3 และวิธีใช้ฟีเจอร์ดังกล่าวให้เกิดประโยชน์สูงสุด

สำรวจ[คอลเล็กชันแอป Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=th) เพื่อ
ดูวิธีที่โมเดลจัดการการให้เหตุผลขั้นสูง การเขียนโค้ดอัตโนมัติ และงานที่ซับซ้อน
แบบหลายรูปแบบ

เริ่มต้นด้วยโค้ด 2-3 บรรทัดดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## ขอแนะนำ Gemini 3 Series

Gemini 3.1 Pro เหมาะที่สุดสำหรับงานที่ซับซ้อนซึ่งต้องใช้ความรู้เกี่ยวกับโลกในวงกว้างและการให้เหตุผลขั้นสูงในรูปแบบต่างๆ

Gemini 3 Flash เป็นโมเดลล่าสุดในซีรีส์ 3 ที่มีความสามารถระดับ Pro ในด้านความชาญฉลาดด้วยความเร็วและราคาของ Flash

Nano Banana Pro (หรือที่เรียกว่า Gemini 3 Pro Image) เป็นโมเดลการสร้างรูปภาพคุณภาพสูงสุด และ Nano Banana 2 (หรือที่เรียกว่า Gemini 3.1 Flash Image) เป็นโมเดลที่มีประสิทธิภาพสูงและมีปริมาณงานสูงในราคาที่ต่ำกว่า

Gemini 3.1 Flash-Lite เป็นโมเดลที่ใช้งานได้หลากหลายซึ่งสร้างขึ้นเพื่อประสิทธิภาพด้านต้นทุนและงานที่มีปริมาณงานสูง

ปัจจุบันโมเดล Gemini 3 ทั้งหมดอยู่ในเวอร์ชันตัวอย่าง

| รหัสโมเดล | หน้าต่างบริบท (อินพุต / เอาต์พุต) | การตัดข้อมูล | การกำหนดราคา (อินพุต / เอาต์พุต)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 ล้าน / 64,000 | ม.ค. 2025 | $0.25 (ข้อความ รูปภาพ วิดีโอ), $0.50 (เสียง) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | ม.ค. 2025 | $0.25 (อินพุตข้อความ) / $0.067 (เอาต์พุตรูปภาพ)\*\* |
| **gemini-3.1-pro-preview** | 1 ล้าน / 64,000 | ม.ค. 2025 | $2 / $12 (<200,000 โทเค็น)   $4 / $18 (>200,000 โทเค็น) |
| **gemini-3-flash-preview** | 1 ล้าน / 64,000 | ม.ค. 2025 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | ม.ค. 2025 | $2 (อินพุตข้อความ) / $0.134 (เอาต์พุตรูปภาพ)\*\* |

*\* การกำหนดราคาต่อ 1 ล้านโทเค็น เว้นแต่จะระบุไว้เป็นอย่างอื่น*
*\*\* การกำหนดราคารูปภาพจะแตกต่างกันไปตามความละเอียด ดูรายละเอียดได้ใน[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)*

ดูขีดจำกัดโดยละเอียด การกำหนดราคา และข้อมูลเพิ่มเติมได้ใน
[หน้าโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

## ฟีเจอร์ใหม่ของ API ใน Gemini 3

Gemini 3 ขอแนะนำพารามิเตอร์ใหม่ที่ออกแบบมาเพื่อให้นักพัฒนาแอปควบคุมเวลาในการตอบสนอง ต้นทุน และความถูกต้องของข้อมูลหลายรูปแบบได้มากขึ้น

### ระดับการคิด

โมเดล Gemini 3 Series ใช้การคิดแบบไดนามิกเป็นค่าเริ่มต้นเพื่อใช้เหตุผลกับพรอมต์ คุณสามารถใช้พารามิเตอร์ `thinking_level` ซึ่งควบคุมความลึก**สูงสุด** ของกระบวนการให้เหตุผลภายในของโมเดลก่อนที่จะสร้างคำตอบ Gemini 3 ถือว่าระดับเหล่านี้เป็นค่าเผื่อสัมพัทธ์สำหรับการคิด ไม่ใช่การรับประกันโทเค็นที่เข้มงวด

หากไม่ได้ระบุ `thinking_level` ไว้ Gemini 3 จะใช้ `high` เป็นค่าเริ่มต้น หากไม่จำเป็นต้องใช้การให้เหตุผลที่ซับซ้อน คุณสามารถจำกัดระดับการคิดของโมเดลเป็น `low` เพื่อให้ได้คำตอบที่เร็วขึ้นและมีเวลาในการตอบสนองที่สั้นลง

| ระดับการคิด | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | คำอธิบาย |
| --- | --- | --- | --- | --- |
| **`minimal`** | ไม่รองรับ | สิ่งที่ทำได้ (ค่าเริ่มต้น) | สิ่งที่ทำได้ | ตรงกับการตั้งค่า "ไม่คิด" สำหรับการค้นหาส่วนใหญ่ โมเดลอาจคิดน้อยมากสำหรับงานเขียนโค้ดที่ซับซ้อน ลดเวลาในการตอบสนองสำหรับแอปพลิเคชันแชทหรือแอปพลิเคชันที่มีการส่งข้อความปริมาณมาก โปรดทราบว่า `minimal` ไม่ได้รับประกันว่าจะปิดการคิด |
| **`low`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | ลดเวลาในการตอบสนองและต้นทุน เหมาะที่สุดสำหรับการทำตามคำสั่งง่ายๆ การแชท หรือแอปพลิเคชันที่มีปริมาณงานสูง |
| **`medium`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | การคิดที่สมดุลสำหรับงานส่วนใหญ่ |
| **`high`** | สิ่งที่ทำได้ (ค่าเริ่มต้น, ไดนามิก) | สิ่งที่ทำได้ (ไดนามิก) | สิ่งที่ทำได้ (ค่าเริ่มต้น, ไดนามิก) | เพิ่มความลึกในการให้เหตุผลให้สูงสุด โมเดลอาจใช้เวลานานขึ้นอย่างมากในการ เข้าถึงโทเค็นเอาต์พุตแรก (ที่ไม่ใช่การคิด) แต่เอาต์พุตจะได้รับการพิจารณาอย่างรอบคอบมากขึ้น |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### อุณหภูมิ

สำหรับโมเดล Gemini 3 ทั้งหมด เราขอแนะนำอย่างยิ่งให้ตั้งค่าพารามิเตอร์อุณหภูมิเป็นค่าเริ่มต้นที่ `1.0`

แม้ว่าโมเดลก่อนหน้านี้มักจะได้รับประโยชน์จากการปรับอุณหภูมิเพื่อควบคุมความคิดสร้างสรรค์เทียบกับความแน่นอน แต่ความสามารถในการให้เหตุผลของ Gemini 3 ได้รับการปรับให้เหมาะกับการตั้งค่าเริ่มต้น การเปลี่ยนอุณหภูมิ (ตั้งค่าต่ำกว่า 1.0) อาจทำให้เกิดลักษณะการทำงานที่ไม่คาดคิด เช่น การวนซ้ำหรือประสิทธิภาพลดลง โดยเฉพาะอย่างยิ่งในงานทางคณิตศาสตร์หรือการให้เหตุผลที่ซับซ้อน

### ลายเซ็นความคิด

โมเดล Gemini 3 ใช้ลายเซ็นความคิดเพื่อรักษาบริบทการให้เหตุผลในการเรียก API ลายเซ็นเหล่านี้เป็นการแสดงที่เข้ารหัสของกระบวนการคิดภายในของโมเดล

- **โหมด Stateful (แนะนำ)**: เมื่อใช้ Interactions API ในโหมด Stateful (ระบุ `previous_interaction_id`) เซิร์ฟเวอร์จะจัดการประวัติการสนทนาและลายเซ็นความคิดโดยอัตโนมัติ
- **โหมด Stateless**: หากคุณจัดการประวัติการสนทนาด้วยตนเอง คุณต้องใส่บล็อกความคิดพร้อมลายเซ็นในคำขอที่ตามมาเพื่อตรวจสอบความถูกต้อง

ดูข้อมูลโดยละเอียดได้ในหน้า [ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

### เอาต์พุตที่มีโครงสร้างพร้อมเครื่องมือ

โมเดล Gemini 3 ช่วยให้คุณรวม[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)เข้ากับเครื่องมือในตัว ซึ่งรวมถึง
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th), [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th), [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) และ [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### การสร้างรูปภาพ

Gemini 3.1 Flash Image และ Gemini 3 Pro Image ช่วยให้คุณสร้างและแก้ไขรูปภาพจากพรอมต์ข้อความได้ โดยใช้
การให้เหตุผลเพื่อ "คิด" ผ่านพรอมต์ และดึงข้อมูลแบบเรียลไทม์ เช่น
พยากรณ์อากาศหรือแผนภูมิหุ้น ก่อนที่จะใช้การเชื่อมต่อแหล่งข้อมูลกับ [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) ก่อนที่จะสร้างรูปภาพที่มีความถูกต้องสูง

**ความสามารถใหม่และที่ได้รับการปรับปรุง**

- **การแสดงผล 4K และข้อความ:** สร้างข้อความและแผนภูมิที่คมชัดและอ่านง่ายด้วยความละเอียดสูงสุด 2K และ 4K
- **การสร้างที่เชื่อมต่อแหล่งข้อมูล:** ใช้เครื่องมือ `google_search` เพื่อยืนยันข้อเท็จจริงและสร้างภาพตามข้อมูลในโลกแห่งความเป็นจริง การเชื่อมต่อแหล่งข้อมูลกับ Google *Image* Search พร้อมใช้งานสำหรับ Gemini 3.1 Flash Image
- **การแก้ไขแบบผ่านการสนทนาไปมา:** แก้ไขรูปภาพหลายครั้งได้เพียงแค่ขอให้เปลี่ยนแปลง (เช่น "เปลี่ยนพื้นหลังให้เป็นภาพพระอาทิตย์ตก") เวิร์กโฟลว์นี้อาศัย**ลายเซ็นความคิด** เพื่อรักษาบริบทภาพระหว่างการสนทนา

ดูรายละเอียดทั้งหมดเกี่ยวกับสัดส่วนภาพ เวิร์กโฟลว์การแก้ไข และตัวเลือกการกำหนดค่า
ได้ใน[คู่มือการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**ตัวอย่างคำตอบ**

![สภาพอากาศ โตเกียว](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=th)

### การเรียกใช้โค้ดพร้อมรูปภาพ

Gemini 3 Flash สามารถมองเห็นเป็นกระบวนการตรวจสอบที่ใช้งานอยู่ ไม่ใช่แค่การมองผ่านๆ ด้วยการรวมการให้เหตุผลเข้ากับการ[เรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) โมเดลจะกำหนดแผน จากนั้นเขียนและ
เรียกใช้โค้ด Python เพื่อซูม ครอบตัด ใส่คำอธิบายประกอบ หรือจัดการรูปภาพอื่นๆ
ทีละขั้นตอนเพื่อเชื่อมต่อคำตอบกับข้อมูลภาพ

**Use cases**

- **ซูมและตรวจสอบ:** โมเดลจะตรวจหาโดยนัยเมื่อรายละเอียดมีขนาดเล็กเกินไป (เช่น การอ่านมาตรวัดหรือหมายเลขซีเรียลที่อยู่ไกลออกไป) และเขียนโค้ดเพื่อครอบตัดและตรวจสอบพื้นที่อีกครั้งด้วยความละเอียดที่สูงขึ้น
- **คณิตศาสตร์และการพล็อตภาพ:** โมเดลสามารถทำการคำนวณหลายขั้นตอนโดยใช้โค้ด (เช่น การรวมรายการในใบเสร็จ หรือการสร้างแผนภูมิ Matplotlib จากข้อมูลที่แยกออกมา)
- **คำอธิบายประกอบรูปภาพ:** โมเดลสามารถวาดลูกศร กรอบล้อมรอบ หรือคำอธิบายประกอบอื่นๆ ลงในรูปภาพโดยตรงเพื่อตอบคำถามเชิงพื้นที่ เช่น "ควรวางรายการนี้ไว้ที่ใด"

หากต้องการเปิดใช้การคิดเชิงภาพ ให้กำหนดค่า [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) เป็นเครื่องมือ โมเดลจะใช้โค้ดเพื่อจัดการรูปภาพโดยอัตโนมัติเมื่อจำเป็น

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการเรียกใช้โค้ดพร้อมรูปภาพได้ที่ [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#images)

### คำตอบของฟังก์ชันแบบหลายรูปแบบ

[การเรียกใช้ฟังก์ชันแบบหลายรูปแบบ](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#multimodal)
ช่วยให้ผู้ใช้ได้รับคำตอบของฟังก์ชันที่มี
ออบเจ็กต์แบบหลายรูปแบบ ซึ่งช่วยให้ใช้ความสามารถในการเรียกใช้ฟังก์ชัน
ของโมเดลได้ดียิ่งขึ้น การเรียกใช้ฟังก์ชันมาตรฐานรองรับเฉพาะคำตอบของฟังก์ชันแบบข้อความเท่านั้น

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### รวมเครื่องมือในตัวและการเรียกใช้ฟังก์ชัน

Gemini 3 อนุญาตให้ใช้เครื่องมือในตัว (เช่น Google Search, บริบท URL
และ [อื่นๆ](https://ai.google.dev/gemini-api/docs/tools?hl=th)) และเครื่องมือการเรียกใช้[ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ที่กำหนดเองในการเรียก API เดียวกัน ซึ่งช่วยให้เวิร์กโฟลว์มีความซับซ้อนมากขึ้น

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## การย้ายข้อมูลจาก Gemini 2.5

Gemini 3 เป็นกลุ่มผลิตภัณฑ์โมเดลที่มากความสามารถที่สุดของเราในปัจจุบัน และมีการปรับปรุงทีละขั้นตอนเมื่อเทียบกับ Gemini 2.5 เมื่อย้ายข้อมูล โปรดพิจารณาสิ่งต่อไปนี้

- **การคิด:** หากก่อนหน้านี้คุณใช้เทคนิควิศวกรรมพรอมต์ที่ซับซ้อน (เช่น
  Chain of Thought) เพื่อบังคับให้ Gemini 2.5 ใช้เหตุผล ให้ลองใช้ Gemini 3 ที่มี
  `thinking_level: "high"` และพรอมต์ที่ง่ายขึ้น
- **การตั้งค่าอุณหภูมิ:** หากโค้ดที่มีอยู่ตั้งค่าอุณหภูมิอย่างชัดเจน (โดยเฉพาะค่าต่ำสำหรับเอาต์พุตที่แน่นอน) เราขอแนะนำให้นำพารามิเตอร์นี้ออกและใช้ค่าเริ่มต้นของ Gemini 3 ที่ 1.0 เพื่อหลีกเลี่ยงปัญหาการวนซ้ำที่อาจเกิดขึ้นหรือประสิทธิภาพลดลงในงานที่ซับซ้อน
- **ความเข้าใจ PDF และเอกสาร:** หากคุณอาศัยลักษณะการทำงานที่เฉพาะเจาะจงสำหรับการแยกวิเคราะห์เอกสารที่มีข้อมูลหนาแน่น ให้ทดสอบการตั้งค่า `media_resolution_high` ใหม่เพื่อให้มั่นใจในความถูกต้องอย่างต่อเนื่อง
- **การใช้โทเค็น:** การย้ายข้อมูลไปยังค่าเริ่มต้นของ Gemini 3 อาจ**เพิ่ม** การใช้โทเค็นสำหรับ PDF แต่**ลด** การใช้โทเค็นสำหรับวิดีโอ หากคำขอเกินหน้าต่างบริบทเนื่องจากความละเอียดเริ่มต้นสูงขึ้น เราขอแนะนำให้ลดความละเอียดของสื่ออย่างชัดเจน
- **การแบ่งส่วนรูปภาพ:** Gemini 3 Pro หรือ Gemini 3 Flash ไม่รองรับความสามารถในการแบ่งส่วนรูปภาพ (การแสดงผลมาสก์ระดับพิกเซลสำหรับออบเจ็กต์) สำหรับ
  เวิร์กโหลดที่ต้องใช้การแบ่งส่วนรูปภาพในตัว เราขอแนะนำให้ใช้ Gemini 2.5 Flash ต่อไปโดยปิดการคิด หรือใช้ [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)
- **การใช้คอมพิวเตอร์:** Gemini 3 Pro และ Gemini 3 Flash รองรับ[การใช้
  คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th) คุณไม่จำเป็นต้องใช้โมเดลแยกต่างหากเพื่อเข้าถึงเครื่องมือการใช้คอมพิวเตอร์ ซึ่งแตกต่างจากซีรีส์ 2.5
- **การรองรับเครื่องมือ**: [ตอนนี้โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัวเข้ากับการเรียกใช้ฟังก์ชันแล้ว](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th) [โมเดล
  Gemini 3](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) ยังรองรับการเชื่อมต่อแหล่งข้อมูลกับ Maps
  แล้วด้วย

## ความเข้ากันได้กับ OpenAI

สำหรับผู้ใช้ที่ใช้เลเยอร์ความเข้ากันได้กับ [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)
ระบบจะจับคู่พารามิเตอร์มาตรฐาน (พารามิเตอร์ `reasoning_effort` ของ OpenAI) กับ
พารามิเตอร์ที่เทียบเท่าของ Gemini (`thinking_level`) โดยอัตโนมัติ

## แนวทางปฏิบัติแนะนำในการใช้พรอมต์

Gemini 3 เป็นโมเดลการให้เหตุผล ซึ่งจะเปลี่ยนวิธีที่คุณควรใช้พรอมต์

- **คำแนะนำที่แม่นยำ:** ใช้พรอมต์อินพุตที่กระชับ Gemini 3 ตอบสนองได้ดีที่สุดต่อคำแนะนำที่ชัดเจนและตรงไปตรงมา โมเดลอาจวิเคราะห์เทคนิควิศวกรรมพรอมต์ (Prompt Engineering) ที่ละเอียดหรือซับซ้อนเกินไปซึ่งใช้กับโมเดลเก่ามากเกินไป
- **ความละเอียดของเอาต์พุต:** โดยค่าเริ่มต้น Gemini 3 จะมีความละเอียดน้อยกว่าและชอบให้คำตอบที่ตรงไปตรงมาและมีประสิทธิภาพ หาก Use Case ของคุณต้องใช้บุคลิกที่สนทนาหรือ "ช่างพูด" มากขึ้น คุณต้องนำโมเดลไปในทิศทางนั้นอย่างชัดเจนในพรอมต์ (เช่น "อธิบายเรื่องนี้ในฐานะผู้ช่วยที่เป็นมิตรและช่างพูด")
- **การจัดการบริบท:** เมื่อทำงานกับชุดข้อมูลขนาดใหญ่ (เช่น หนังสือทั้งเล่ม
  ฐานโค้ด หรือวิดีโอขนาดยาว) ให้วางคำแนะนำหรือคำถามที่เฉพาะเจาะจงไว้ที่
  ส่วนท้ายของพรอมต์ หลังจากบริบทข้อมูล ยึดการให้เหตุผลของโมเดลกับข้อมูลที่ให้ไว้โดยเริ่มคำถามด้วยวลี เช่น "จากข้อมูลข้างต้น..."

ดูข้อมูลเพิ่มเติมเกี่ยวกับกลยุทธ์การออกแบบพรอมต์ได้ใน[คู่มือวิศวกรรมพรอมต์ (Prompt Engineering)](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=th)

## คำถามที่พบบ่อย

1. **การตัดข้อมูลของ Gemini 3 คือเมื่อใด** โมเดล Gemini 3 มีการตัดข้อมูลในเดือนมกราคม 2025 หากต้องการข้อมูลล่าสุด ให้ใช้เครื่องมือ
   [การเชื่อมต่อแหล่งข้อมูลกับ Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
2. **ขีดจำกัดของหน้าต่างบริบทคือเท่าใด** โมเดล Gemini 3 รองรับหน้าต่างบริบทอินพุต 1 ล้านโทเค็นและเอาต์พุตสูงสุด 64,000 โทเค็น
3. **Gemini 3 มีแพ็กเกจฟรีไหม** Gemini 3 Flash `gemini-3-flash-preview` มีแพ็กเกจฟรีใน Gemini API คุณสามารถลองใช้ Gemini 3.1 Pro และ 3 Flash ได้โดยไม่มีค่าใช้จ่ายใน Google AI Studio แต่ `gemini-3.1-pro-preview` ใน Gemini API ไม่มีแพ็กเกจฟรี
4. **โค้ด `thinking_budget` เก่าของฉันจะยังใช้งานได้ไหม** ได้ `thinking_budget` ยังคงได้รับการรองรับเพื่อความเข้ากันได้แบบย้อนกลับ แต่เราขอแนะนำให้ย้ายข้อมูลไปใช้ `thinking_level` เพื่อให้ได้ประสิทธิภาพที่คาดการณ์ได้มากขึ้น อย่าใช้ทั้ง 2 อย่างในคำขอเดียวกัน
5. **Gemini 3 รองรับ Batch API ไหม** ใช่ Gemini 3 รองรับ
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)
6. **ระบบรองรับการแคชบริบทไหม** ใช่ [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th) รองรับสำหรับ Gemini 3
7. **Gemini 3 รองรับเครื่องมือใดบ้าง** Gemini 3 รองรับ
   [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th),
   [การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th),
   [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th),
   [การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) และ
   [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) นอกจากนี้ ยังรองรับ
   การเรียกใช้[ฟังก์ชันมาตรฐาน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)สำหรับ
   เครื่องมือที่กำหนดเองของคุณเอง และเมื่อใช้
   [ร่วมกับเครื่องมือในตัว](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)
8. **คืออะไร`gemini-3.1-pro-preview-customtools`?** หากคุณใช้
   `gemini-3.1-pro-preview` และโมเดลไม่สนใจเครื่องมือที่กำหนดเอง แต่เลือกใช้
   คำสั่ง Bash ให้ลองใช้โมเดล `gemini-3.1-pro-preview-customtools` แทน
   ดูข้อมูลเพิ่มเติมได้[ที่นี่][customtools-model]

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-22 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-22 UTC"],[],[]]
