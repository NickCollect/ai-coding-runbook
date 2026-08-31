---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=th
fetched_at: 2026-08-31T06:40:31.624654+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e23\u0e39\u0e1b\u0e20\u0e32\u0e1e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจรูปภาพ

โมเดล Gemini ถูกสร้างขึ้นตั้งแต่เริ่มต้นให้เป็นแบบหลายรูปแบบ ซึ่งจะปลดล็อกงานประมวลผลรูปภาพและคอมพิวเตอร์วิชันซิสเต็มที่หลากหลาย รวมถึงการใส่คำบรรยายรูปภาพ การจัดหมวดหมู่ และการตอบคำถามเกี่ยวกับภาพโดยไม่ต้องฝึกโมเดล ML เฉพาะ

นอกจากความสามารถแบบหลายรูปแบบทั่วไปแล้ว โมเดล Gemini ยังมี
**ความแม่นยำที่เพิ่มขึ้น** สำหรับกรณีการใช้งานที่เฉพาะเจาะจง เช่น [การตรวจจับออบเจ็กต์](#object-detection)
และ [การแบ่งกลุ่ม](#segmentation) ผ่านการฝึกเพิ่มเติม

## การส่งรูปภาพไปยัง Gemini

คุณสามารถระบุรูปภาพเป็นอินพุตไปยัง Gemini ได้หลายวิธีดังนี้

- [การส่งรูปภาพโดยใช้ URL](#url-image): เหมาะสำหรับรูปภาพที่เข้าถึงได้แบบสาธารณะ
- [การส่งข้อมูลรูปภาพแบบอินไลน์](#inline-image): สำหรับข้อมูลรูปภาพที่เข้ารหัส Base64
- [การอัปโหลดรูปภาพโดยใช้ File API](#upload-image): แนะนำให้ใช้กับ
  ไฟล์ขนาดใหญ่หรือเพื่อนำรูปภาพกลับมาใช้ซ้ำในคำขอหลายรายการ

### การส่งรูปภาพโดยใช้ URL

คุณสามารถอัปโหลดรูปภาพโดยใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) และส่งรูปภาพ
ในคำขอได้ดังนี้

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
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

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
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
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### การส่งข้อมูลรูปภาพแบบอินไลน์

คุณสามารถระบุข้อมูลรูปภาพเป็นสตริงที่เข้ารหัส Base64 ได้ดังนี้

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### การอัปโหลดรูปภาพโดยใช้ File API

หากต้องการใช้ไฟล์ขนาดใหญ่หรือใช้ไฟล์รูปภาพเดิมซ้ำๆ ให้ใช้ Files API ดูคู่มือ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## การใช้พรอมต์ที่มีรูปภาพหลายรูป

คุณสามารถระบุรูปภาพหลายรูปในพรอมต์เดียวได้โดยการรวมออบเจ็กต์รูปภาพหลายรายการไว้ในอาร์เรย์ `input`

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
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
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## การตรวจจับออบเจ็กต์

โมเดลได้รับการฝึกให้ตรวจจับออบเจ็กต์ในรูปภาพและรับพิกัดกรอบล้อมรอบของออบเจ็กต์ พิกัดจะปรับขนาดเป็น [0, 1000] โดยอิงตามขนาดรูปภาพ คุณต้องปรับขนาดพิกัดเหล่านี้ตามขนาดรูปภาพเดิม

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

ดูตัวอย่างเพิ่มเติมได้ที่ [สูตรการแก้ปัญหาของ Gemini](https://github.com/google-gemini/cookbook)

## การแบ่งกลุ่ม

โมเดล Gemini ไม่เพียงแต่ตรวจจับรายการต่างๆ เท่านั้น แต่ยังแบ่งกลุ่มรายการเหล่านั้นและระบุมาสก์เส้นขอบด้วย

โมเดลจะคาดการณ์รายการ JSON โดยแต่ละรายการจะแสดงมาสก์การแบ่งกลุ่ม แต่ละรายการจะมีกรอบล้อมรอบ ("`box_2d`") ในรูปแบบ `[ymin, xmin, ymax, xmax]` ที่มีพิกัดปกติระหว่าง 0 ถึง 1000, ป้ายกำกับ ("`label`") ที่ระบุออบเจ็กต์ และสุดท้ายคือมาสก์การแบ่งกลุ่มภายในกรอบล้อมรอบเป็นรูปหลายเหลี่ยมที่มีพิกัด `[x, y]` ที่ปรับให้เป็นปกติเป็น 0-1000

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![โต๊ะที่มีคัพเค้ก โดยไฮไลต์วัตถุที่ทำจากไม้และแก้ว](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=th)

ตัวอย่างเอาต์พุตการแบ่งกลุ่มที่มีออบเจ็กต์และมาสก์การแบ่งกลุ่ม

## รูปแบบรูปภาพที่รองรับ

Gemini รองรับประเภท MIME ของรูปแบบรูปภาพต่อไปนี้

- PNG - `image/png`
- JPEG - `image/jpeg`
- WebP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ ได้ที่
[คู่มือวิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

## ความสามารถ

โมเดล Gemini ทุกเวอร์ชันเป็นแบบหลายรูปแบบและสามารถใช้ในงานประมวลผลรูปภาพและคอมพิวเตอร์วิชันซิสเต็มที่หลากหลาย ซึ่งรวมถึงแต่ไม่จำกัดเพียง การใส่คำบรรยายรูปภาพ การตอบคำถามเกี่ยวกับภาพ การจัดหมวดหมู่รูปภาพ การตรวจจับออบเจ็กต์ และการแบ่งกลุ่มออบเจ็กต์

Gemini สามารถลดความจำเป็นในการใช้โมเดล ML เฉพาะได้ ทั้งนี้ขึ้นอยู่กับข้อกำหนดด้านคุณภาพและประสิทธิภาพ

โมเดลเวอร์ชันล่าสุดได้รับการฝึกมาโดยเฉพาะเพื่อปรับปรุงความแม่นยำของ
งานเฉพาะทาง นอกเหนือจากความสามารถทั่วไป เช่น การตรวจจับ
[ออบเจ็กต์](#object-detection)ที่ได้รับการปรับปรุง และ [การแบ่งกลุ่ม](#segmentation)

## ข้อจำกัดและข้อมูลทางเทคนิคที่สำคัญ

### ขีดจำกัดของไฟล์

โมเดล Gemini รองรับไฟล์รูปภาพสูงสุด 3,600 ไฟล์ต่อคำขอ

### การคำนวณโทเค็น

- 258 โทเค็นหากทั้ง 2 ด้านมีขนาด <= 384 พิกเซล
  รูปภาพขนาดใหญ่จะถูกแบ่งเป็นรูปภาพขนาด 768x768 พิกเซล โดยแต่ละรูปภาพใช้โทเค็น 258 รายการ

สูตรคร่าวๆ สำหรับการคำนวณจำนวนรูปภาพที่แบ่งมีดังนี้

- คำนวณขนาดหน่วยครอบตัดซึ่งมีค่าประมาณ `floor(min(width, height)` / 1.5)
- หารแต่ละด้านด้วยขนาดหน่วยครอบตัดแล้วคูณกันเพื่อหาจำนวนรูปภาพที่แบ่ง

ตัวอย่างเช่น รูปภาพขนาด 960x540 จะมีขนาดหน่วยครอบตัด 360 หารแต่ละด้านด้วย 360 และจำนวนรูปภาพที่แบ่งคือ 3 \* 2 = 6

### ความละเอียดของสื่อ

Gemini 3 มีการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลภาพแบบหลายรูปแบบด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**
ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง

## เคล็ดลับและแนวทางปฏิบัติแนะนำ

- ตรวจสอบว่ารูปภาพหมุนอย่างถูกต้อง
- ใช้รูปภาพที่ชัดเจนและไม่เบลอ
- เมื่อใช้รูปภาพเดียวที่มีข้อความ ให้วางพรอมต์ข้อความ *ก่อน* รูปภาพในอาร์เรย์ `input`

## ขั้นตอนถัดไป

คู่มือนี้จะแสดงวิธีอัปโหลดไฟล์รูปภาพและสร้างเอาต์พุตข้อความจากอินพุตรูปภาพ ดูข้อมูลเพิ่มเติมได้ที่แหล่งข้อมูลต่อไปนี้

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): ดูข้อมูลเพิ่มเติมเกี่ยวกับการอัปโหลดและจัดการไฟล์เพื่อใช้กับ Gemini
- [คำแนะนำระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตาม
  ความต้องการและกรณีการใช้งานที่เฉพาะเจาะจง
- [กลยุทธ์การเขียนพรอมต์กับไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini API รองรับการเขียนพรอมต์กับข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ ซึ่งเรียกอีกอย่างว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th): บางครั้งโมเดล Generative
  AI จะสร้างเอาต์พุตที่ไม่คาดคิด เช่น เอาต์พุตที่ไม่ถูกต้อง
  มีอคติ หรือไม่เหมาะสม การประมวลผลภายหลังและการประเมินโดยเจ้าหน้าที่เป็นสิ่งสำคัญในการจำกัดความเสี่ยงที่จะเกิดอันตรายจากเอาต์พุตดังกล่าว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
