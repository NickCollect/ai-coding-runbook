---
source_url: https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=th
fetched_at: 2026-06-01T06:07:42.839063+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e15\u0e33\u0e41\u0e2b\u0e19\u0e48\u0e07\u0e14\u0e49\u0e27\u0e22 Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอ้างอิงตำแหน่งด้วย Google Maps

การอ้างอิงด้วย Google Maps จะเชื่อมต่อความสามารถในการสร้างของ Gemini กับข้อมูลที่สมบูรณ์ เป็นข้อเท็จจริง และเป็นข้อมูลล่าสุดของ Google Maps ฟีเจอร์นี้ช่วยให้นักพัฒนาแอปผสานรวมฟังก์ชันการทำงานที่รับรู้ตำแหน่งไว้ในแอปพลิเคชันของตนได้อย่างง่ายดาย เมื่อคำค้นหาของผู้ใช้มีบริบทที่เกี่ยวข้องกับข้อมูล Maps โมเดล Gemini
จะใช้ประโยชน์จาก Google Maps เพื่อให้คำตอบที่ถูกต้องตามข้อเท็จจริงและเป็นข้อมูลล่าสุด ซึ่ง
เกี่ยวข้องกับตำแหน่งที่ผู้ใช้ระบุหรือพื้นที่ทั่วไป

- **คำตอบที่ถูกต้องและรับรู้ตำแหน่ง:** ใช้ประโยชน์จากข้อมูลที่ครอบคลุมและเป็นปัจจุบันของ Google Maps สำหรับคำค้นหาที่เจาะจงทางภูมิศาสตร์
- **การปรับเปลี่ยนในแบบของผู้ใช้ที่ดียิ่งขึ้น:** ปรับแต่งคำแนะนำและข้อมูลตามตำแหน่งที่ผู้ใช้ระบุ
- **ข้อมูลและวิดเจ็ตตามบริบท:** โทเค็นบริบทเพื่อแสดงวิดเจ็ต Google Maps แบบอินเทอร์แอกทีฟควบคู่ไปกับเนื้อหาที่สร้างขึ้น

## เริ่มต้นใช้งาน

ตัวอย่างนี้แสดงวิธีผสานรวมการเชื่อมต่อแหล่งข้อมูลกับ Google Maps เข้ากับแอปพลิเคชันของคุณ เพื่อให้คำตอบที่แม่นยำและรับรู้ถึงตำแหน่งสำหรับคำค้นหาของผู้ใช้
พรอมต์ขอคำแนะนำในพื้นที่พร้อมตำแหน่งของผู้ใช้ (ไม่บังคับ) เพื่อให้โมเดล
Gemini ใช้ข้อมูล Google Maps ได้

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## วิธีการทำงานของการเชื่อมต่อแหล่งข้อมูลกับ Google Maps

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะผสานรวม Gemini API กับระบบนิเวศทางภูมิศาสตร์ของ Google โดยใช้ Maps API เป็นแหล่งข้อมูลที่เชื่อมต่อ เมื่อคำค้นหาของผู้ใช้
มีบริบททางภูมิศาสตร์ โมเดล Gemini จะเรียกใช้เครื่องมือการอ้างอิงกับ
Google Maps ได้ จากนั้นโมเดลจะสร้างคำตอบโดยอิงตามข้อมูล Google Maps ที่เกี่ยวข้องกับสถานที่ที่ระบุ

โดยปกติแล้วกระบวนการนี้จะเกี่ยวข้องกับสิ่งต่อไปนี้

1. **คำค้นหาของผู้ใช้:** ผู้ใช้ส่งคำค้นหาไปยังแอปพลิเคชันของคุณ ซึ่งอาจรวมถึงบริบททางภูมิศาสตร์ (เช่น "ร้านกาแฟใกล้ฉัน" "พิพิธภัณฑ์ในซานฟรานซิสโก")
2. **การเรียกใช้เครื่องมือ:** โมเดล Gemini จะเรียกใช้เครื่องมือการเชื่อมต่อแหล่งข้อมูลกับ Google Maps เมื่อรับรู้ถึงความตั้งใจทางภูมิศาสตร์ คุณอาจเลือกให้เครื่องมือนี้มี`latitude`และ`longitude`ของผู้ใช้ก็ได้ เครื่องมือนี้เป็นเครื่องมือค้นหาแบบข้อความ
   และทำงานคล้ายกับการค้นหาใน Maps โดยที่คำค้นหาในพื้นที่ ("ใกล้ฉัน") จะใช้พิกัด ส่วนคำค้นหาที่เฉพาะเจาะจงหรือไม่ใช่ในพื้นที่
   จะไม่ได้รับผลกระทบจากตำแหน่งที่ระบุอย่างชัดเจน
3. **การดึงข้อมูล:** บริการการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะค้นหาข้อมูลที่เกี่ยวข้องใน Google Maps (เช่น สถานที่ รีวิว รูปภาพ ที่อยู่ เวลาทำการ)
4. **การสร้างข้อมูลที่อิงตามข้อมูลจริง:** ระบบจะใช้ข้อมูล Maps ที่ดึงมาเพื่อแจ้งคำตอบของโมเดล Gemini เพื่อให้มั่นใจถึงความถูกต้องและความเกี่ยวข้องของข้อเท็จจริง
5. **คำตอบและคำอธิบายประกอบ:** โมเดลจะแสดงคำตอบเป็นข้อความพร้อมคำอธิบายประกอบในบรรทัดที่ลิงก์ไปยังแหล่งที่มาของ Google Maps ซึ่งช่วยให้นักพัฒนาแอปแสดงการอ้างอิงและแสดงวิดเจ็ต Google Maps ตามบริบทได้ (ไม่บังคับ)

## เหตุผลและเวลาที่ควรใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Maps

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เหมาะสำหรับแอปพลิเคชันที่ต้องการข้อมูลที่ถูกต้อง เป็นปัจจุบัน และเฉพาะเจาะจงตำแหน่ง โดยจะช่วยยกระดับประสบการณ์ของผู้ใช้
ด้วยการแสดงเนื้อหาที่เกี่ยวข้องและปรับเปลี่ยนในแบบของคุณ ซึ่งขับเคลื่อนโดยฐานข้อมูลขนาดใหญ่ของ Google Maps
ที่มีสถานที่กว่า 250 ล้านแห่งทั่วโลก

คุณควรใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เมื่อแอปพลิเคชันของคุณต้องการทำสิ่งต่อไปนี้

- ตอบคำถามที่เฉพาะเจาะจงตามภูมิศาสตร์ให้ถูกต้องและครบถ้วน
- สร้างผู้ช่วยวางแผนการเดินทางและ Local Guides แบบสนทนา
- แนะนำจุดที่น่าสนใจตาม
  ตำแหน่งและความชอบของผู้ใช้ เช่น ร้านอาหารหรือร้านค้า
- สร้างประสบการณ์ที่รับรู้ตำแหน่งสำหรับบริการโซเชียล การค้าปลีก หรือการนำส่งอาหาร

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เหมาะอย่างยิ่งสำหรับ Use Case ที่ต้องใช้ข้อมูลความใกล้เคียงและข้อมูลข้อเท็จจริงปัจจุบัน เช่น การค้นหา "ร้านกาแฟที่ดีที่สุดใกล้ฉัน" หรือการขอเส้นทาง

## กรณีการใช้งาน

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps รองรับกรณีการใช้งานที่หลากหลายซึ่งรับรู้ตำแหน่ง

### การจัดการคำถามเกี่ยวกับสถานที่

ถามคำถามโดยละเอียดเกี่ยวกับสถานที่หนึ่งๆ เพื่อรับคำตอบตามรีวิวของผู้ใช้ Google และข้อมูลอื่นๆ ของ Maps

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### การปรับเปลี่ยนในแบบของคุณตามตำแหน่ง

รับคำแนะนำที่ปรับให้เหมาะกับค่ากำหนดของผู้ใช้และพื้นที่ทางภูมิศาสตร์ที่เฉพาะเจาะจง

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### ช่วยวางแผนการเดินทาง

สร้างแผนการเดินทางหลายวันพร้อมเส้นทางและข้อมูลเกี่ยวกับสถานที่ต่างๆ
เหมาะสำหรับแอปพลิเคชันการเดินทาง

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476,
        "enable_widget": True
    }]
)
# ... code to process response and widget token
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476,
      enable_widget: true
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476,
      "enable_widget": true
    }]
  }'
```

## ข้อกำหนดในการใช้งานบริการ

ส่วนนี้อธิบายข้อกำหนดในการใช้บริการสำหรับ Grounding with Google
Maps

### แจ้งให้ผู้ใช้ทราบเกี่ยวกับการใช้แหล่งข้อมูลของ Google Maps

ผลการค้นหาที่อิงตามข้อมูลจริงของ Google Maps แต่ละรายการจะมีการอธิบายแหล่งที่มาในบล็อกเนื้อหาของขั้นตอน `model_output` ที่รองรับคำตอบแต่ละรายการ ระบบจะแสดงข้อมูลเมตาดังต่อไปนี้

- URL แหล่งที่มา
- ชื่อ

เมื่อแสดงผลลัพธ์จากการเชื่อมต่อแหล่งข้อมูลกับ Google Maps คุณต้องระบุแหล่งที่มาของ Google Maps ที่เกี่ยวข้อง และแจ้งให้ผู้ใช้ทราบข้อมูลต่อไปนี้

- แหล่งที่มาของ Google Maps ต้องอยู่ต่อจากเนื้อหาที่สร้างขึ้นซึ่งแหล่งที่มานั้นรองรับ เนื้อหาที่สร้างขึ้นนี้เรียกอีกอย่างว่าผลลัพธ์ที่อิงตามข้อมูลจริงของ Google
  Maps
- แหล่งข้อมูลของ Google Maps ต้องดูได้ภายใน 1 การโต้ตอบของผู้ใช้

### แสดงแหล่งข้อมูล Google Maps ด้วยลิงก์ Google Maps

สำหรับคำอธิบายประกอบแหล่งที่มาแต่ละรายการ ระบบจะต้องสร้างตัวอย่างลิงก์
ตามข้อกำหนดต่อไปนี้

- ระบุแหล่งที่มาแต่ละแหล่งเป็น Google Maps ตามข้อความของ Google Maps
  [หลักเกณฑ์การระบุแหล่งที่มา](#maps-attribution-guidelines)
- แสดงชื่อแหล่งที่มาที่ระบุไว้ในการตอบกลับ
- ลิงก์ไปยังแหล่งที่มาโดยใช้ `url` จากคำอธิบายประกอบ

### หลักเกณฑ์การระบุแหล่งที่มาของข้อความใน Google Maps

เมื่อระบุแหล่งที่มาของ Google Maps ในข้อความ ให้ทำตามหลักเกณฑ์ต่อไปนี้

- โปรดอย่าแก้ไขข้อความ Google Maps ในลักษณะใดก็ตาม
  - อย่าเปลี่ยนการใช้อักษรตัวพิมพ์ใหญ่ของ Google Maps
  - อย่าวาง Google Maps ในหลายบรรทัด
  - อย่าแปล Google Maps เป็นภาษาอื่น
  - ป้องกันไม่ให้เบราว์เซอร์แปล Google Maps โดยใช้แอตทริบิวต์ HTML
    translate="no"

ดูข้อมูลเพิ่มเติมเกี่ยวกับผู้ให้บริการข้อมูล Google Maps บางรายและข้อกำหนดของใบอนุญาตได้ที่[ประกาศทางกฎหมายของ Google Maps และ Google Earth](https://www.google.com/help/legalnotices_maps/?hl=th)

## แนวทางปฏิบัติแนะนำ

- **ระบุตำแหน่งของผู้ใช้:** เพื่อให้ได้คำตอบที่เกี่ยวข้องและปรับเปลี่ยนในแบบของคุณมากที่สุด
  ให้ระบุ `latitude` และ `longitude` ในการกำหนดค่าเครื่องมือ `google_maps` เสมอเมื่อทราบตำแหน่งของผู้ใช้
- **แสดงวิดเจ็ตตามบริบทของ Google Maps:** วิดเจ็ตตามบริบทจะแสดงโดยใช้โทเค็นบริบท `google_maps_widget_context_token` ซึ่งจะแสดงในคำตอบของ Gemini API และใช้เพื่อแสดงเนื้อหาภาพจาก Google Maps ได้
- **แจ้งผู้ใช้ปลายทาง:** แจ้งให้ผู้ใช้ปลายทางทราบอย่างชัดเจนว่าระบบกำลังใช้ข้อมูล Google Maps
  เพื่อตอบคำค้นหาของผู้ใช้ โดยเฉพาะเมื่อเปิดใช้เครื่องมือ
- **ปิดเมื่อไม่จำเป็น:** การเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะปิดอยู่โดยค่าเริ่มต้น เปิดใช้ (`"tools": [{"type": "google_maps"}]`) เมื่อการค้นหามีบริบททางภูมิศาสตร์ที่ชัดเจนเท่านั้น เพื่อเพิ่มประสิทธิภาพและต้นทุน

## ข้อจำกัด

- ปัจจุบันการเชื่อมต่อแหล่งข้อมูลกับ Google Maps รองรับเฉพาะพรอมต์และการตอบกลับที่เป็นภาษาอังกฤษเท่านั้น
- เครื่องมือนี้อาจไม่พร้อมให้บริการในบางภูมิภาค
- ผลลัพธ์อาจแตกต่างกันไปตามความแม่นยำของตำแหน่งและข้อมูล Maps ที่พร้อมใช้งาน
- **ขอบเขตทางภูมิศาสตร์:** การเชื่อมต่อแหล่งข้อมูลกับ Google Maps มีให้บริการทั่วโลก
- **สถานะเริ่มต้น:** เครื่องมือการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะปิดอยู่โดยค่าเริ่มต้น
  คุณต้องเปิดใช้ฟีเจอร์นี้อย่างชัดแจ้งในคำขอ API

## ราคาและขีดจำกัดอัตรา

ราคาของการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะอิงตามคำค้นหา ปัจจุบันอัตราค่าบริการคือ
**$25 / 1,000 พรอมต์ที่อิงตามความจริง** นอกจากนี้ รุ่นฟรียังมีคำขอได้สูงสุด 500 รายการต่อวัน
ระบบจะนับคำขอรวมในโควต้าเฉพาะเมื่อพรอมต์แสดงผลลัพธ์ที่อิงตามข้อมูลของ Google Maps อย่างน้อย 1 รายการ (เช่น ผลลัพธ์ที่มีแหล่งที่มาของ Google Maps อย่างน้อย 1 รายการ) หากมีการส่งการค้นหาหลายรายการไปยัง Google Maps จากคำขอเดียว ระบบจะนับเป็นคำขอเดียวในการจำกัดอัตราการใช้งาน

ดูข้อมูลการกำหนดราคาโดยละเอียดได้ที่[หน้าราคาของ Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## โมเดลที่รองรับ

รุ่นต่อไปนี้รองรับการเชื่อมต่อแหล่งข้อมูลกับ Google Maps

| รุ่น | การเชื่อมต่อแหล่งข้อมูลกับ Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=th) | ✔️ |

## ชุดเครื่องมือที่รองรับ

โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัว (เช่น การอ้างอิงกับ Google
Maps) กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ที่หน้า[ชุดเครื่องมือ](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=th)

## ขั้นตอนถัดไป

- ดูข้อมูลเกี่ยวกับ[เครื่องมืออื่นๆ ที่มี](https://ai.google.dev/gemini-api/docs/tools?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับแนวทางปฏิบัติแนะนำด้าน AI ที่มีความรับผิดชอบและตัวกรองความปลอดภัยของ Gemini API ได้ที่[คู่มือการตั้งค่าความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-28 UTC"],[],[]]
