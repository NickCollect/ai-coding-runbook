---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=th
fetched_at: 2026-08-31T06:37:09.181581+00:00
title: "\u0e1e\u0e37\u0e49\u0e19\u0e10\u0e32\u0e19\u0e14\u0e49\u0e27\u0e22 Google Search \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# พื้นฐานด้วย Google Search

การเชื่อมต่อแหล่งข้อมูลกับ Google Search จะเชื่อมต่อโมเดล Gemini กับเนื้อหาเว็บแบบเรียลไทม์และจะใช้งานได้กับทุกภาษาที่มี ซึ่งจะช่วยให้ Gemini ให้คำตอบที่แม่นยำยิ่งขึ้นและอ้างอิงแหล่งข้อมูลที่ตรวจสอบได้แม้จะผ่านการตัดข้อมูลมาแล้ว

การเชื่อมต่อแหล่งข้อมูลช่วยให้คุณสร้างแอปพลิเคชันที่ทำสิ่งต่อไปนี้ได้

- **เพิ่มความแม่นยำของข้อเท็จจริง:** ลดการสร้างข้อมูลที่ไม่ถูกต้องของโมเดลโดยอิงตามข้อมูลในโลกแห่งความเป็นจริง
- **เข้าถึงข้อมูลแบบเรียลไทม์:** ตอบคำถามเกี่ยวกับเหตุการณ์และหัวข้อล่าสุด
- **ระบุแหล่งที่มา:** สร้างความเชื่อมั่นให้ผู้ใช้ด้วยการแสดงแหล่งที่มาของการอ้างสิทธิ์ของโมเดล

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.7-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.7-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## วิธีการทำงานของการเชื่อมต่อแหล่งข้อมูลกับ Google Search

เมื่อคุณเปิดใช้เครื่องมือ `google_search` โมเดลจะจัดการเวิร์กโฟลว์ทั้งหมดของการค้นหา ประมวลผล และอ้างอิงข้อมูลโดยอัตโนมัติ

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=th)

1. **พรอมต์ของผู้ใช้:** แอปพลิเคชันของคุณจะส่งพรอมต์ของผู้ใช้ไปยัง Gemini API โดยเปิดใช้เครื่องมือ `google_search`
2. **การวิเคราะห์พรอมต์:** โมเดลจะวิเคราะห์พรอมต์และพิจารณาว่าการค้นหาใน Google Search จะช่วยปรับปรุงคำตอบได้หรือไม่
3. **Google Search:** หากจำเป็น โมเดลจะสร้างคำค้นหาอย่างน้อย 1 รายการและดำเนินการค้นหาโดยอัตโนมัติ
4. **การประมวลผลผลการค้นหา:** โมเดลจะประมวลผลผลการค้นหา สังเคราะห์ข้อมูล และกำหนดคำตอบ
5. **คำตอบที่เชื่อมต่อแหล่งข้อมูล:** API จะแสดงคำตอบสุดท้ายที่ใช้งานง่ายซึ่งเชื่อมต่อแหล่งข้อมูลกับผลการค้นหา คำตอบนี้ประกอบด้วยคำตอบที่เป็นข้อความของโมเดลพร้อม `annotations` ในบรรทัดที่มีการอ้างอิง รวมถึง
   `google_search_call` และ `google_search_result` ขั้นตอนพร้อมคำค้นหาและคำแนะนำการค้นหา

## ทำความเข้าใจคำตอบที่เชื่อมต่อแหล่งข้อมูล

เมื่อเชื่อมต่อแหล่งข้อมูลกับคำตอบได้สำเร็จ เอาต์พุตข้อความของโมเดลจะมี
ในบรรทัด `annotations` ในบล็อกเนื้อหาข้อความโดยตรง คำอธิบายประกอบเหล่านี้จะให้ข้อมูลการอ้างอิงที่ลิงก์ส่วนต่างๆ ของคำตอบกับแหล่งที่มา

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

ฟิลด์สำคัญในคำตอบ

- `google_search_call` : มี `queries` ที่โมเดลดำเนินการ
- `google_search_result` : มี `search_suggestions` ซึ่งเป็นข้อมูลโค้ด HTML สำหรับแสดงคำแนะนำการค้นหาใน UI ข้อกำหนดการใช้งานทั้งหมดมี
  รายละเอียดอยู่ใน[ข้อกำหนดในการให้บริการ](https://ai.google.dev/gemini-api/terms?hl=th#grounding-with-google-search)
- `text` พร้อม `annotations` : คำตอบที่สังเคราะห์ของโมเดลพร้อมการอ้างอิงในบรรทัด คำอธิบายประกอบ `url_citation` แต่ละรายการจะลิงก์ส่วนข้อความ (กำหนดโดย `start_index` และ `end_index`) กับ URL แหล่งที่มา ซึ่งเป็นสิ่งสำคัญในการสร้างการอ้างอิงในบรรทัด

นอกจากนี้ คุณยังใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับเครื่องมือบริบท [URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) เพื่อเชื่อมต่อแหล่งข้อมูลกับคำตอบทั้งใน
ข้อมูลเว็บสาธารณะและ URL ที่เฉพาะเจาะจงที่คุณระบุได้ด้วย

## การระบุแหล่งที่มาด้วยการอ้างอิงในบรรทัด

API จะแสดงคำอธิบายประกอบ `url_citation` ในบรรทัดในบล็อกเนื้อหาข้อความ ซึ่งช่วยให้คุณควบคุมวิธีแสดงแหล่งที่มาในอินเทอร์เฟซผู้ใช้ได้อย่างสมบูรณ์
คำอธิบายประกอบแต่ละรายการจะมี `start_index` และ `end_index` เพื่อระบุส่วนของข้อความที่อ้างอิง วิธีแยกและแสดงคำอธิบายประกอบมีดังนี้

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

เอาต์พุตจะแสดงข้อความตามด้วยการอ้างอิง ดังนี้

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## ราคา

เมื่อคุณใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับ Gemini 3 ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณสำหรับคำค้นหาแต่ละรายการที่โมเดลตัดสินใจดำเนินการ หากโมเดลตัดสินใจที่จะดำเนินการคำค้นหาหลายรายการเพื่อตอบพรอมต์รายการเดียว (เช่น ค้นหา `"UEFA Euro 2024 winner"` และ `"Spain vs England Euro 2024 final
score"` ภายใน การเรียก API เดียวกัน) ระบบจะนับเป็นการใช้เครื่องมือที่เรียกเก็บเงินได้ 2 ครั้งสำหรับคำขอนั้น ระบบจะละเว้นคำค้นหาเว็บที่ว่างเปล่าเมื่อนับคำค้นหาที่ไม่ซ้ำกันเพื่อวัตถุประสงค์ในการเรียกเก็บเงิน รูปแบบการเรียกเก็บเงินนี้ใช้ได้กับโมเดล Gemini 3 เท่านั้น เมื่อคุณใช้การเชื่อมต่อแหล่งข้อมูลกับ Search ร่วมกับโมเดล Gemini 2.5 หรือโมเดลเก่ากว่า ระบบจะเรียกเก็บเงินจากโปรเจ็กต์ของคุณต่อพรอมต์

ดูข้อมูลการเรียกเก็บเงินโดยละเอียดได้ที่[หน้าการเรียกเก็บเงินของ Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

## โมเดลที่รองรับ

คุณดูความสามารถทั้งหมดได้ในหน้าภาพรวมของ[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

| รุ่น | การเชื่อมต่อแหล่งข้อมูลกับ Google Search |
| --- | --- |
| Gemini 3.7 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## ชุดเครื่องมือที่รองรับ

คุณสามารถใช้การเชื่อมต่อแหล่งข้อมูลกับ Google Search ร่วมกับเครื่องมืออื่นๆ เช่น
[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th),
[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) และ
[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) (รองรับใน
Gemini 3.5 Flash และโมเดลที่ใหม่กว่า) เพื่อรองรับกรณีการใช้งานที่ซับซับซ้อนมากขึ้น โมเดล Gemini 3 ยังรองรับการรวมเครื่องมือในตัวเหล่านี้กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ในหน้า
[ชุดเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

## ขั้นตอนถัดไป

- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ที่มี เช่น [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- ดูวิธีเพิ่มพรอมต์ด้วย URL ที่เฉพาะเจาะจงโดยใช้เครื่องมือบริบท URL

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-08-20 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-08-20 UTC"],[],[]]
