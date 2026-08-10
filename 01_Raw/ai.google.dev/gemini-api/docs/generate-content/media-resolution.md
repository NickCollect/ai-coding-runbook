---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=th
fetched_at: 2026-08-10T03:22:54.664507+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e02\u0e2d\u0e07\u0e2a\u0e37\u0e48\u0e2d \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความละเอียดของสื่อ

พารามิเตอร์ `media_resolution` จะควบคุมวิธีที่ Gemini API ประมวลผลอินพุตสื่อ เช่น รูปภาพ วิดีโอ และเอกสาร PDF โดยกำหนด**จำนวนโทเค็นสูงสุด** ที่จัดสรรไว้สำหรับอินพุตสื่อ ซึ่งช่วยให้คุณปรับสมดุลคุณภาพของคำตอบกับเวลาในการตอบสนองและค่าใช้จ่ายได้ ดูการตั้งค่าต่างๆ ค่าเริ่มต้น และวิธีที่การตั้งค่าเหล่านั้นสอดคล้องกับโทเค็นได้ในส่วน[จำนวนโทเค็น](#token-counts)

คุณกำหนดค่าความละเอียดของสื่อได้ 2 วิธี ดังนี้

- [ต่อส่วน](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th#per-part-media-resolution) (Gemini 3 เท่านั้น)
- [ทั่วโลก](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th#global-media-resolution)สำหรับคำขอ `generateContent` ทั้งหมด (โมเดลมัลติโมดัลทั้งหมด)

## ความละเอียดของสื่อต่อส่วน (Gemini 3 เท่านั้น)

Gemini 3 ช่วยให้คุณกำหนดความละเอียดของสื่อสำหรับออบเจ็กต์สื่อแต่ละรายการภายในคำขอได้ ซึ่งช่วยให้เพิ่มประสิทธิภาพการใช้งานโทเค็นได้อย่างละเอียด คุณสามารถผสมระดับความละเอียดในคำขอเดียวได้ เช่น ใช้ความละเอียดสูงสำหรับแผนภาพที่ซับซ้อน และความละเอียดต่ำสำหรับรูปภาพบริบทอย่างง่าย การตั้งค่านี้จะลบล้างการกำหนดค่าส่วนกลางสำหรับส่วนที่เฉพาะเจาะจง ดูการตั้งค่าเริ่มต้นได้ในส่วน[จำนวนโทเค็น](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th#token-counts)

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## ความละเอียดของสื่อส่วนกลาง

คุณสามารถกำหนดความละเอียดเริ่มต้นสำหรับส่วนสื่อทั้งหมดในคำขอได้โดยใช้ `GenerationConfig` ซึ่งโมเดลมัลติโมดัลทั้งหมดรองรับ หากคำขอ
มีการตั้งค่าทั้งส่วนกลางและ[ต่อส่วน](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th#per-part-media-resolution) ระบบจะใช้การตั้งค่าต่อส่วนสำหรับรายการนั้นๆ

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## ค่าความละเอียดที่ใช้ได้

Gemini API กำหนดระดับความละเอียดของสื่อไว้ดังนี้

- `MEDIA_RESOLUTION_UNSPECIFIED`: การตั้งค่าเริ่มต้น จำนวนโทเค็นสำหรับระดับนี้จะแตกต่างกันอย่างมากระหว่าง Gemini 3 กับโมเดล Gemini เวอร์ชันก่อนหน้า
- `MEDIA_RESOLUTION_LOW`: จำนวนโทเค็นต่ำกว่า ส่งผลให้ประมวลผลได้เร็วขึ้นและค่าใช้จ่ายต่ำลง แต่รายละเอียดน้อยลง
- `MEDIA_RESOLUTION_MEDIUM`: ความสมดุลระหว่างรายละเอียด ค่าใช้จ่าย และเวลาในการตอบสนอง
- `MEDIA_RESOLUTION_HIGH`: จำนวนโทเค็นสูงกว่า ให้รายละเอียดมากขึ้นเพื่อให้โมเดลทำงานได้ แต่เวลาในการตอบสนองและค่าใช้จ่ายจะเพิ่มขึ้น
- `MEDIA_RESOLUTION_ULTRA_HIGH` (ต่อส่วนเท่านั้น): จำนวนโทเค็นสูงสุด ซึ่งจำเป็นสำหรับกรณีการใช้งานที่เฉพาะเจาะจง
  เช่น [การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

โปรดทราบว่า `MEDIA_RESOLUTION_HIGH` ให้ประสิทธิภาพสูงสุดสำหรับกรณีการใช้งานส่วนใหญ่

จำนวนโทเค็นที่แน่นอนซึ่งสร้างขึ้นสำหรับแต่ละระดับเหล่านี้จะขึ้นอยู่กับทั้ง**ประเภทสื่อ** (รูปภาพ วิดีโอ, PDF) และ**เวอร์ชันของโมเดล**

## จำนวนโทเค็น

ตารางด้านล่างสรุปจำนวนโทเค็นโดยประมาณสำหรับค่า `media_resolution` แต่ละค่าและประเภทสื่อต่อตระกูลโมเดล

**โมเดล Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **รูปภาพ** | **วิดีโอ** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (ค่าเริ่มต้น) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | ไม่มี | ไม่มี |

**โมเดล Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **รูปภาพ** | **วิดีโอ** | **PDF (สแกน)** | **PDF (เนทีฟ)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (ค่าเริ่มต้น) | 256 + แพนและสแกน (~2048) | 256 | 256 + OCR | 256 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + ข้อความเนทีฟ |
| `MEDIA_RESOLUTION_HIGH` | 256 + แพนและสแกน | 256 | 256 + OCR | 256 + ข้อความเนทีฟ |

## การเลือกความละเอียดที่เหมาะสม

- **ค่าเริ่มต้น (`UNSPECIFIED`):** เริ่มต้นด้วยค่าเริ่มต้น ซึ่งได้รับการปรับแต่งให้มีความสมดุลที่ดีระหว่างคุณภาพ เวลาในการตอบสนอง และค่าใช้จ่ายสำหรับกรณีการใช้งานที่พบบ่อยที่สุด
- **`LOW`:** ใช้ในสถานการณ์ที่ค่าใช้จ่ายและเวลาในการตอบสนองมีความสำคัญสูงสุด และรายละเอียดที่ละเอียดมีความสำคัญน้อยกว่า
- **`MEDIUM` / `HIGH`:** เพิ่มความละเอียดเมื่องานต้องใช้ความเข้าใจรายละเอียดที่ซับซ้อนภายในสื่อ ซึ่งมักจำเป็นสำหรับการวิเคราะห์ภาพที่ซับซ้อน การอ่านแผนภูมิ หรือความเข้าใจเอกสารที่มีข้อมูลหนาแน่น
- **`ULTRA HIGH`** - ใช้ได้กับการตั้งค่าต่อส่วนเท่านั้น แนะนำสำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น การใช้คอมพิวเตอร์ หรือกรณีที่การทดสอบแสดงให้เห็นถึงการปรับปรุงที่ชัดเจนเมื่อเทียบกับ `HIGH`
- **การควบคุมต่อส่วน (Gemini 3):** เพิ่มประสิทธิภาพการใช้งานโทเค็น เช่น ในพรอมต์ที่มีรูปภาพหลายรูป ให้ใช้ `HIGH` สำหรับแผนภาพที่ซับซ้อน และ `LOW` หรือ `MEDIUM` สำหรับรูปภาพบริบทที่ง่ายกว่า

**การตั้งค่าที่แนะนำ**

รายการต่อไปนี้แสดงการตั้งค่าความละเอียดของสื่อที่แนะนำสำหรับสื่อแต่ละประเภทที่รองรับ

|  |  |  |  |
| --- | --- | --- | --- |
| **ประเภทสื่อ** | **การตั้งค่าที่แนะนำ** | **โทเค็นสูงสุด** | **คำแนะนำการใช้งาน** |
| **Google รูปภาพ** | `MEDIA_RESOLUTION_HIGH` | 1120 | แนะนำสำหรับงานวิเคราะห์รูปภาพส่วนใหญ่เพื่อให้ได้คุณภาพสูงสุด |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | เหมาะที่สุดสำหรับความเข้าใจเอกสาร โดยคุณภาพจะอิ่มตัวที่ `medium` โดยทั่วไป การเพิ่มเป็น `high` ไม่ค่อยปรับปรุงผลลัพธ์ OCR สำหรับเอกสารมาตรฐาน |
| **วิดีโอ** (ทั่วไป) | `MEDIA_RESOLUTION_LOW` (หรือ `MEDIA_RESOLUTION_MEDIUM`) | 70 (ต่อเฟรม) | **หมายเหตุ:** สำหรับวิดีโอ ระบบจะถือว่าการตั้งค่า `low` และ `medium` เหมือนกัน (70 โทเค็น) เพื่อเพิ่มประสิทธิภาพการใช้งานบริบท ซึ่งเพียงพอสำหรับงานการจดจำและการอธิบายการกระทำส่วนใหญ่ |
| **วิดีโอ** (มีข้อความจำนวนมาก) | `MEDIA_RESOLUTION_HIGH` | 280 (ต่อเฟรม) | จำเป็นเฉพาะเมื่อกรณีการใช้งานเกี่ยวข้องกับการอ่านข้อความที่มีข้อมูลหนาแน่น (OCR) หรือรายละเอียดเล็กๆ ภายในเฟรมวิดีโอ |

ทดสอบและประเมินผลกระทบของการตั้งค่าความละเอียดต่างๆ ในแอปพลิเคชันที่เฉพาะเจาะจงเสมอ เพื่อค้นหาความสมดุลที่ดีที่สุดระหว่างคุณภาพ เวลาในการตอบสนอง และค่าใช้จ่าย

## ข้อมูลสรุปความเข้ากันได้ของเวอร์ชัน

- Enum `MediaResolution` ใช้ได้กับโมเดลทั้งหมดที่รองรับอินพุตสื่อ
- จำนวนโทเค็นที่เชื่อมโยงกับแต่ละระดับ Enum จะ**แตกต่างกัน** ระหว่างโมเดล Gemini 3 กับ Gemini เวอร์ชันก่อนหน้า
- การตั้งค่า `media_resolution` ในออบเจ็กต์ `Part` แต่ละรายการ**ใช้ได้กับโมเดล Gemini 3 เท่านั้น**

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับความสามารถในการประมวลผลข้อมูลหลายรูปแบบของ Gemini API ได้ใน
  [คำแนะนำการทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=th) [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=th) และ
  [ความเข้าใจเอกสาร](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
