---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=th
fetched_at: 2026-06-01T06:01:35.113425+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บริบท URL

เครื่องมือบริบท URL ช่วยให้คุณระบุบริบทเพิ่มเติมให้กับโมเดลใน
รูปแบบ URL โดยการใส่ URL ในคำขอ โมเดลจะเข้าถึง
เนื้อหาจากหน้าเหล่านั้น (ตราบใดที่เป็น URL ประเภทที่ไม่อยู่ในส่วน
[ข้อจำกัด](#limitations)) เพื่อให้ข้อมูล
และปรับปรุงการตอบกลับ

เครื่องมือบริบท URL มีประโยชน์สำหรับงานต่างๆ เช่น

- **ดึงข้อมูล**: ดึงข้อมูลที่เฉพาะเจาะจง เช่น ราคา ชื่อ หรือผลการค้นหาที่สำคัญ จาก URL หลายรายการ
- **เปรียบเทียบเอกสาร**: วิเคราะห์รายงาน บทความ หรือ PDF หลายรายการเพื่อ
  ระบุความแตกต่างและติดตามแนวโน้ม
- **สังเคราะห์และสร้างเนื้อหา**: รวมข้อมูลจาก URL แหล่งที่มาหลายรายการเพื่อสร้างข้อมูลสรุปที่ถูกต้อง บล็อกโพสต์ หรือรายงาน
- **วิเคราะห์โค้ดและเอกสาร**: ชี้ไปยังที่เก็บ GitHub หรือเอกสารทางเทคนิคเพื่ออธิบายโค้ด สร้างวิธีการตั้งค่า หรือตอบคำถาม

ตัวอย่างต่อไปนี้แสดงวิธีเปรียบเทียบสูตรอาหาร 2 สูตรจากเว็บไซต์ต่างๆ

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## วิธีการทำงาน

เครื่องมือบริบท URL ใช้กระบวนการดึงข้อมูล 2 ขั้นตอนเพื่อสร้างสมดุลระหว่างความเร็ว ต้นทุน และการเข้าถึงข้อมูลล่าสุด เมื่อคุณระบุ URL เครื่องมือจะพยายามดึงข้อมูลเนื้อหาจากแคชดัชนีภายในก่อน ซึ่งทำหน้าที่เป็นแคชที่ได้รับการเพิ่มประสิทธิภาพอย่างสูง หาก URL ไม่พร้อมใช้งานในดัชนี (เช่น หากเป็นหน้าใหม่มาก) เครื่องมือจะย้อนกลับไปดึงข้อมูลแบบสดโดยอัตโนมัติ
ซึ่งจะเข้าถึง URL โดยตรงเพื่อดึงข้อมูลเนื้อหาแบบเรียลไทม์

## การรวมกับเครื่องมืออื่นๆ

คุณสามารถรวมเครื่องมือบริบท URL กับเครื่องมืออื่นๆ เพื่อสร้างเวิร์กโฟลว์ที่มีประสิทธิภาพมากขึ้น

[โมเดล Gemini 3](#supported-models) รองรับการรวมเครื่องมือในตัว
(เช่น บริบท URL) กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ในหน้าการรวมเครื่องมือ

### การเชื่อมต่อแหล่งข้อมูลกับ Search

เมื่อเปิดใช้ทั้งบริบท URL และ
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th) โมเดลจะใช้ความสามารถในการค้นหาเพื่อค้นหา
ข้อมูลที่เกี่ยวข้องทางออนไลน์ แล้วใช้เครื่องมือบริบท URL เพื่อทำความเข้าใจหน้าเว็บที่พบในเชิงลึกมากขึ้น แนวทางนี้มีประสิทธิภาพสำหรับพรอมต์ที่ต้องมีการค้นหาในวงกว้างและการวิเคราะห์หน้าเว็บที่เฉพาะเจาะจงในเชิงลึก

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## ทำความเข้าใจการตอบกลับ

เมื่อโมเดลใช้เครื่องมือบริบท URL การตอบกลับจะมีออบเจ็กต์ `url_context_metadata` ออบเจ็กต์นี้จะแสดงรายการ URL ที่โมเดลดึงข้อมูลเนื้อหามาและสถานะของความพยายามในการดึงข้อมูลแต่ละครั้ง ซึ่งมีประโยชน์สำหรับการยืนยันและการแก้ไขข้อบกพร่อง

ต่อไปนี้เป็นตัวอย่างส่วนหนึ่งของการตอบกลับ (เราได้ละเว้นบางส่วนของการตอบกลับเพื่อความกระชับ)

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

ดูรายละเอียดทั้งหมดเกี่ยวกับออบเจ็กต์นี้ได้ที่เอกสารอ้างอิง API ของ
[`UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=th#UrlContextMetadata)

### การตรวจสอบความปลอดภัย

ระบบจะทำการตรวจสอบการกลั่นกรองเนื้อหาใน URL เพื่อยืนยันว่า URL เป็นไปตามมาตรฐานความปลอดภัย หาก URL ที่คุณระบุไม่ผ่านการตรวจสอบนี้ คุณจะได้รับ `url_retrieval_status` เป็น `URL_RETRIEVAL_STATUS_UNSAFE`

### จำนวนโทเค็น

ระบบจะนับเนื้อหาที่ดึงข้อมูลจาก URL ที่คุณระบุในพรอมต์เป็นส่วนหนึ่งของโทเค็นอินพุต คุณดูจำนวนโทเค็นสำหรับการใช้งานพรอมต์และ
เครื่องมือได้ใน [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=th#UsageMetadata)
ของเอาต์พุตโมเดล ต่อไปนี้เป็นตัวอย่างเอาต์พุต

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

ราคาต่อโทเค็นจะขึ้นอยู่กับโมเดลที่ใช้ โปรดดูรายละเอียดในหน้าราคา

## โมเดลที่รองรับ

| โมเดล | บริบท URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## แนวทางปฏิบัติแนะนำ

- **ระบุ URL ที่เฉพาะเจาะจง**: เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด ให้ระบุ URL โดยตรงไปยัง
  เนื้อหาที่ต้องการให้โมเดลวิเคราะห์ โมเดลจะดึงข้อมูลเนื้อหาจาก URL ที่คุณระบุเท่านั้น ไม่ใช่เนื้อหาจากลิงก์ที่ซ้อนกัน
- **ตรวจสอบการเข้าถึง**: ตรวจสอบว่า URL ที่คุณระบุไม่ได้นำไปยัง
  หน้าเว็บที่ต้องเข้าสู่ระบบหรืออยู่หลังเพย์วอลล์
- **ใช้ URL ที่สมบูรณ์**: ระบุ URL แบบเต็ม รวมถึงโปรโตคอล
  (เช่น https://www.google.com แทนที่จะเป็น google.com)

## ข้อจำกัด

- การเรียกใช้ฟังก์ชัน: ปัจจุบันระบบไม่รองรับการใช้เครื่องมือ (บริบท URL, การเชื่อมต่อแหล่งข้อมูลกับ Google Search ฯลฯ) กับการเรียกใช้ฟังก์ชัน
- ขีดจำกัดคำขอ: เครื่องมือสามารถประมวลผล URL ได้สูงสุด 20 รายการต่อคำขอ
- ขนาดเนื้อหา URL: ขนาดสูงสุดของเนื้อหาที่ดึงข้อมูลจาก URL เดียวคือ 34 MB
- การเข้าถึงแบบสาธารณะ: URL ต้องเข้าถึงได้แบบสาธารณะบนเว็บ
  ระบบไม่รองรับที่อยู่ localhost (เช่น localhost, 127.0.0.1), เครือข่ายส่วนตัว และบริการ Tunneling (เช่น ngrok, pinggy)
- Gemini API เท่านั้น: บริบท URL ใช้ได้ใน Gemini API เท่านั้น ไม่ใช่ผ่านแพลตฟอร์ม Agent ของ Gemini Enterprise

### ประเภทเนื้อหาที่รองรับและไม่รองรับ

เครื่องมือสามารถดึงข้อมูลเนื้อหาจาก URL ที่มีประเภทเนื้อหาต่อไปนี้

- ข้อความ (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- รูปภาพ (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

ระบบ**ไม่** รองรับเนื้อหาประเภทต่อไปนี้

- เนื้อหาเพย์วอลล์
- วิดีโอ YouTube (ดู
  [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#youtube)เพื่อเรียนรู้วิธีประมวลผล URL ของ YouTube
  )
- ไฟล์ Google Workspace เช่น Google เอกสารหรือชีต
- ไฟล์วิดีโอและเสียง

## ขั้นตอนถัดไป

- ดูตัวอย่างเพิ่มเติมได้ที่คู่มือบริบท [URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=th#url-context)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-29 UTC"],[],[]]
