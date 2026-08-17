---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th
fetched_at: 2026-08-17T02:19:07.072586+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e15\u0e33\u0e41\u0e2b\u0e19\u0e48\u0e07\u0e14\u0e49\u0e27\u0e22 Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอ้างอิงตำแหน่งด้วย Google Maps

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะเชื่อมต่อความสามารถในการสร้างเนื้อหาของ Gemini กับข้อมูลที่สมบูรณ์ เป็นข้อเท็จจริง และเป็นข้อมูลล่าสุดของ Google Maps ฟีเจอร์นี้ช่วยให้นักพัฒนาแอปสามารถผสานรวมฟังก์ชันการทำงานที่รับรู้ตำแหน่งลงในแอปพลิเคชันได้อย่างง่ายดาย เมื่อคำค้นหาของผู้ใช้มีบริบทที่เกี่ยวข้องกับข้อมูล Maps โมเดล Gemini จะใช้ประโยชน์จาก Google Maps เพื่อให้คำตอบที่เป็นข้อเท็จจริงและเป็นข้อมูลล่าสุดซึ่งเกี่ยวข้องกับสถานที่ที่ผู้ใช้ระบุหรือพื้นที่ทั่วไป

- **คำตอบที่แม่นยำและรับรู้ตำแหน่ง:** ใช้ประโยชน์จากข้อมูลที่ครอบคลุมและเป็นปัจจุบันของ Google Maps สำหรับคำค้นหาที่เฉพาะเจาะจงทางภูมิศาสตร์
- **การปรับเปลี่ยนในแบบของผู้ใช้ที่มีประสิทธิภาพมากขึ้น:** ปรับแต่งคำแนะนำและข้อมูลตามสถานที่ที่ผู้ใช้ระบุ

## เริ่มต้นใช้งาน

ตัวอย่างนี้แสดงวิธีผสานรวมการเชื่อมต่อแหล่งข้อมูลกับ Google Maps เข้ากับแอปพลิเคชันเพื่อให้คำตอบที่แม่นยำและรับรู้ตำแหน่งสำหรับคำค้นหาของผู้ใช้ พรอมต์จะขอคำแนะนำในพื้นที่พร้อมสถานที่ของผู้ใช้ (ไม่บังคับ) ซึ่งช่วยให้โมเดล Gemini ใช้ข้อมูล Google Maps ได้

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## วิธีการทำงานของการเชื่อมต่อแหล่งข้อมูลกับ Google Maps

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะผสานรวม Gemini API กับระบบนิเวศ Geo ของ Google โดยใช้ Maps API เป็นแหล่งข้อมูล เมื่อคำค้นหาของผู้ใช้มีบริบททางภูมิศาสตร์ โมเดล Gemini จะเรียกใช้เครื่องมือการเชื่อมต่อแหล่งข้อมูลกับ Google Maps ได้ จากนั้นโมเดลจะสร้างคำตอบที่อิงตามข้อมูล Google Maps ที่เกี่ยวข้องกับสถานที่ที่ระบุ

โดยปกติกระบวนการจะมีลักษณะดังนี้

1. **คำค้นหาของผู้ใช้:** ผู้ใช้ส่งคำค้นหาไปยังแอปพลิเคชันของคุณ ซึ่งอาจมีบริบททางภูมิศาสตร์ (เช่น "ร้านกาแฟใกล้ฉัน" "พิพิธภัณฑ์ในซานฟรานซิสโก")
2. **การเรียกใช้เครื่องมือ:** โมเดล Gemini จะเรียกใช้เครื่องมือการเชื่อมต่อแหล่งข้อมูลกับ Google Maps เมื่อรับรู้ถึงความตั้งใจทางภูมิศาสตร์ คุณสามารถระบุ `latitude` และ `longitude` ของผู้ใช้ให้กับเครื่องมือนี้ได้ (ไม่บังคับ)
   เครื่องมือนี้เป็นเครื่องมือค้นหาข้อความและทำงานคล้ายกับการค้นหาใน Maps โดยคำค้นหาในพื้นที่ ("ใกล้ฉัน") จะใช้พิกัด ส่วนคำค้นหาที่เฉพาะเจาะจงหรือไม่ใช่ในพื้นที่นั้นๆ จะไม่ได้รับผลกระทบจากสถานที่ที่ระบุ
3. **การดึงข้อมูล:** บริการการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะค้นหาข้อมูลที่เกี่ยวข้องจาก Google Maps (เช่น สถานที่ รีวิว รูปภาพ ที่อยู่ เวลาทำการ)
4. **การสร้างเนื้อหาที่อิงตามแหล่งข้อมูล:** ระบบจะใช้ข้อมูล Maps ที่ดึงมาเพื่อแจ้งคำตอบของโมเดล Gemini เพื่อให้มั่นใจในความถูกต้องของข้อเท็จจริงและความเกี่ยวข้อง
5. **คำตอบและคำอธิบายประกอบ:** โมเดลจะแสดงคำตอบเป็นข้อความพร้อมคำอธิบายประกอบแบบอินไลน์ที่ลิงก์ไปยังแหล่งข้อมูล Google Maps ซึ่งช่วยให้นักพัฒนาแอปแสดงการอ้างอิงได้

## เหตุผลและเวลาที่ควรใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Maps

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เหมาะอย่างยิ่งสำหรับแอปพลิเคชันที่ต้องใช้ข้อมูลที่แม่นยำ เป็นข้อมูลล่าสุด และเฉพาะเจาะจงสถานที่ ฟีเจอร์นี้ช่วยยกระดับประสบการณ์การใช้งานของผู้ใช้ด้วยการแสดงเนื้อหาที่เกี่ยวข้องและปรับเปลี่ยนในแบบของผู้ใช้ ซึ่งอิงตามฐานข้อมูลที่ครอบคลุมของ Google Maps ที่มีสถานที่มากกว่า 250 ล้านแห่งทั่วโลก

คุณควรใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เมื่อแอปพลิเคชันของคุณต้องทำสิ่งต่อไปนี้

- ให้คำตอบที่สมบูรณ์และถูกต้องสำหรับคำถามที่เฉพาะเจาะจงทางภูมิศาสตร์
- สร้างเครื่องมือวางแผนการเดินทางและไกด์นำเที่ยวในพื้นที่แบบสนทนา
- แนะนำจุดที่น่าสนใจตามสถานที่และการกำหนดค่าของผู้ใช้ เช่น ร้านอาหารหรือร้านค้า
- สร้างประสบการณ์ที่รับรู้ตำแหน่งสำหรับบริการโซเชียลมีเดีย บริการค้าปลีก หรือบริการจัดส่งอาหาร

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps เหมาะอย่างยิ่งสำหรับกรณีการใช้งานที่ระยะทางและข้อมูลข้อเท็จจริงปัจจุบันมีความสำคัญอย่างยิ่ง เช่น การค้นหา "ร้านกาแฟที่ดีที่สุดใกล้ฉัน" หรือการดูเส้นทาง

## กรณีการใช้งาน

การเชื่อมต่อแหล่งข้อมูลกับ Google Maps รองรับกรณีการใช้งานที่รับรู้ตำแหน่งได้หลากหลาย

### การจัดการคำถามที่เฉพาะเจาะจงสถานที่

ถามคำถามโดยละเอียดเกี่ยวกับสถานที่ที่เฉพาะเจาะจงเพื่อรับคำตอบตามรีวิวของผู้ใช้ Google และข้อมูล Maps อื่นๆ

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### การปรับเปลี่ยนในแบบของผู้ใช้ตามสถานที่

รับคำแนะนำที่ปรับให้เหมาะกับการกำหนดค่าของผู้ใช้และพื้นที่ทางภูมิศาสตร์ที่เฉพาะเจาะจง

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### การช่วยเหลือในการวางแผนการเดินทาง

สร้างแผนการเดินทางหลายวันพร้อมเส้นทางและข้อมูลเกี่ยวกับสถานที่ต่างๆ ซึ่งเหมาะสำหรับแอปพลิเคชันการเดินทาง

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
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
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## ข้อกำหนดในการใช้งานบริการ

ส่วนนี้อธิบายข้อกำหนดในการใช้งานบริการสำหรับการเชื่อมต่อแหล่งข้อมูลกับ Google Maps

### แจ้งให้ผู้ใช้ทราบเกี่ยวกับการใช้แหล่งข้อมูล Google Maps

ผลลัพธ์แต่ละรายการที่อิงตาม Google Maps จะมีคำอธิบายประกอบแหล่งข้อมูลในบล็อกเนื้อหาของขั้นตอน `model_output` ที่รองรับคำตอบแต่ละรายการ ระบบจะแสดงข้อมูลเมตาดังต่อไปนี้

- URL ต้นทาง
- ชื่อ

เมื่อแสดงผลลัพธ์จากการเชื่อมต่อแหล่งข้อมูลกับ Google Maps คุณต้องระบุแหล่งข้อมูล Google Maps ที่เกี่ยวข้องและแจ้งให้ผู้ใช้ทราบดังต่อไปนี้

- แหล่งข้อมูล Google Maps ต้องอยู่ต่อจากเนื้อหาที่สร้างขึ้นซึ่งแหล่งข้อมูลรองรับโดยทันที เนื้อหาที่สร้างขึ้นนี้เรียกอีกอย่างว่าผลลัพธ์ที่อิงตาม Google Maps
- แหล่งข้อมูล Google Maps ต้องดูได้ภายใน 1 การโต้ตอบของผู้ใช้

### แสดงแหล่งข้อมูล Google Maps พร้อมลิงก์ Google Maps

คำอธิบายประกอบแหล่งข้อมูลแต่ละรายการต้องสร้างตัวอย่างลิงก์ตามข้อกำหนดต่อไปนี้

- ระบุแหล่งที่มาแต่ละรายการเป็น Google Maps ตามหลักเกณฑ์การระบุแหล่งที่มาด้วยข้อความของ Google Maps
- แสดงชื่อแหล่งที่มาที่ระบุไว้ในคำตอบ
- ลิงก์ไปยังแหล่งที่มาโดยใช้ `url` จากคำอธิบายประกอบ

### หลักเกณฑ์การระบุแหล่งที่มาด้วยข้อความของ Google Maps

เมื่อระบุแหล่งที่มาเป็น Google Maps ในข้อความ ให้ทำตามหลักเกณฑ์ต่อไปนี้

- อย่าแก้ไขข้อความ Google Maps ในลักษณะใดก็ตาม ดังนี้
  - อย่าเปลี่ยนการใช้ตัวพิมพ์ใหญ่และตัวพิมพ์เล็กของ Google Maps
  - อย่าขึ้นบรรทัดใหม่สำหรับ Google Maps
  - อย่าแปล Google Maps เป็นภาษาอื่น
  - ป้องกันไม่ให้เบราว์เซอร์แปล Google Maps โดยใช้แอตทริบิวต์ HTML translate="no"

ดูข้อมูลเพิ่มเติมเกี่ยวกับผู้ให้บริการข้อมูล Google Maps บางรายและ
ข้อกำหนดสิทธิ์การใช้งานได้ที่ [ประกาศทางกฎหมายของ Google Maps และ Google Earth](https://www.google.com/help/legalnotices_maps/?hl=th)

## แนวทางปฏิบัติแนะนำ

- **ระบุสถานที่ของผู้ใช้:** เพื่อให้ได้คำตอบที่เกี่ยวข้องมากที่สุดและปรับเปลี่ยนในแบบของผู้ใช้
  ระบุ `latitude` และ `longitude` ในการกำหนดค่าเครื่องมือ `google_maps` เสมอเมื่อทราบสถานที่ของผู้ใช้
- **แจ้งผู้ใช้ปลายทาง:** แจ้งให้ผู้ใช้ปลายทางทราบอย่างชัดเจนว่าระบบกำลังใช้ข้อมูล Google Maps เพื่อตอบคำค้นหาของผู้ใช้ โดยเฉพาะอย่างยิ่งเมื่อเปิดใช้เครื่องมือ
- **ปิดเมื่อไม่จำเป็น:** การเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะปิดอยู่โดยค่าเริ่มต้น ให้เปิดใช้ (`"tools": [{"type": "google_maps"}]`) เมื่อคำค้นหามี
  บริบททางภูมิศาสตร์ที่ชัดเจนเท่านั้น เพื่อเพิ่มประสิทธิภาพและลดค่าใช้จ่าย

## ข้อจำกัด

- ปัจจุบันการเชื่อมต่อแหล่งข้อมูลกับ Google Maps รองรับเฉพาะพรอมต์และคำตอบที่เป็นภาษาอังกฤษเท่านั้น
- เครื่องมือนี้อาจไม่พร้อมให้บริการในบางภูมิภาค
- ผลลัพธ์อาจแตกต่างกันไปตามความแม่นยำของสถานที่และข้อมูล Maps ที่มี
- **ขอบเขตทางภูมิศาสตร์:** การเชื่อมต่อแหล่งข้อมูลกับ Google Maps พร้อมให้บริการทั่วโลก
- **สถานะเริ่มต้น:** เครื่องมือการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะปิดอยู่โดยค่าเริ่มต้น
  คุณต้องเปิดใช้เครื่องมือนี้อย่างชัดเจนในคำขอ API

## ราคาและขีดจำกัดอัตรา

ราคาการเชื่อมต่อแหล่งข้อมูลกับ Google Maps จะแตกต่างกันไปตามรุ่นของโมเดล ดังนี้

- **โมเดล Gemini 3:** ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณสำหรับ**คำค้นหา**แต่ละรายการที่โมเดลตัดสินใจดำเนินการ **พรอมต์การค้นหา**รายการเดียว (คำขอ API ของคุณที่ส่งไปยังโมเดล) อาจทำให้โมเดลดำเนินการคำค้นหาหลายรายการเพื่อค้นหาข้อมูลที่จำเป็น คำค้นหาแต่ละรายการจะนับเป็นการใช้งานเครื่องมือที่เรียกเก็บเงินได้
- **โมเดล Gemini 2.5 และโมเดลเก่ากว่า:** ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณต่อ**พรอมต์การค้นหา**
  ระบบจะเรียกเก็บเงินจากคำขอเฉพาะในกรณีที่พรอมต์แสดงผลลัพธ์ที่อิงตาม Google Maps อย่างน้อย 1 รายการได้สำเร็จ ไม่ว่าโมเดลจะดำเนินการคำค้นหาแต่ละรายการภายในกี่รายการก็ตามเพื่อให้ได้ผลลัพธ์นั้น

ดูข้อมูลราคาโดยละเอียดได้ที่หน้าการกำหนดราคา [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## โมเดลที่รองรับ

โมเดลต่อไปนี้รองรับการเชื่อมต่อแหล่งข้อมูลกับ Google Maps

| โมเดล | การเชื่อมต่อแหล่งข้อมูลกับ Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ชุดเครื่องมือที่รองรับ

โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัว (เช่น การเชื่อมต่อแหล่งข้อมูลกับ Google Maps) กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ที่หน้า
[ชุดเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

## ขั้นตอนถัดไป

- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ที่[พร้อมให้บริการ](https://ai.google.dev/gemini-api/docs/tools?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับแนวทางปฏิบัติแนะนำด้าน AI ที่มีความรับผิดชอบและตัวกรองความปลอดภัยของ Gemini API ได้ที่[คู่มือการตั้งค่าความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
