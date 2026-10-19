---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=th
fetched_at: 2026-10-19T05:50:02.585217+00:00
title: "\u0e1a\u0e23\u0e34\u0e1a\u0e17 URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บริบท URL

เครื่องมือบริบท URL ช่วยให้คุณระบุบริบทเพิ่มเติมให้กับโมเดลในรูปแบบ URL ได้ การใส่ URL ในคำขอจะช่วยให้โมเดลเข้าถึงเนื้อหาจากหน้าเว็บเหล่านั้นได้ (ตราบใดที่ URL ไม่ใช่ประเภทที่ระบุไว้ในส่วน[ข้อจำกัด](#limitations)) เพื่อให้ข้อมูลและปรับปรุงการตอบกลับ

เครื่องมือบริบท URL มีประโยชน์สำหรับงานต่างๆ เช่น

- **ดึงข้อมูล**: ดึงข้อมูลที่เฉพาะเจาะจง เช่น ราคา ชื่อ หรือผลการค้นพบที่สำคัญ
  จาก URL หลายรายการ
- **เปรียบเทียบเอกสาร**: วิเคราะห์รายงาน บทความ หรือ PDF หลายรายการเพื่อ
  ระบุความแตกต่างและติดตามแนวโน้ม
- **สังเคราะห์และสร้างเนื้อหา**: รวมข้อมูลจาก URL แหล่งที่มาหลายรายการเพื่อสร้างสรุปที่ถูกต้อง บล็อกโพสต์ หรือรายงาน
- **วิเคราะห์โค้ดและเอกสาร**: ชี้ไปยังที่เก็บ GitHub หรือเอกสารทางเทคนิคเพื่ออธิบายโค้ด สร้างวิธีการตั้งค่า หรือตอบคำถาม

ตัวอย่างต่อไปนี้แสดงวิธีเปรียบเทียบสูตรอาหาร 2 สูตรจากเว็บไซต์ต่างๆ

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    url1 := "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
    url2 := "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                fmt.Sprintf("Compare the ingredients and cooking times from the recipes at %s and %s", url1, url2),
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and its source annotations
    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                    if len(contentBlock.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range contentBlock.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                fmt.Printf("  - %s: %s\n", annotation.URLCitation.GetTitle(), annotation.URLCitation.GetURL())
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## วิธีการทำงาน

เครื่องมือบริบท URL ใช้กระบวนการดึงข้อมูล 2 ขั้นตอนเพื่อสร้างสมดุลระหว่างความเร็ว ต้นทุน และการเข้าถึงข้อมูลล่าสุด เมื่อคุณระบุ URL เครื่องมือจะพยายามดึงเนื้อหาจากแคชดัชนีภายในก่อน ซึ่งทำหน้าที่เป็นแคชที่ได้รับการเพิ่มประสิทธิภาพอย่างสูง หาก URL ไม่พร้อมใช้งานในดัชนี (เช่น หากเป็นหน้าเว็บใหม่มาก) เครื่องมือจะกลับไปดึงข้อมูลแบบสดโดยอัตโนมัติ
ซึ่งจะเข้าถึง URL โดยตรงเพื่อดึงเนื้อหาแบบเรียลไทม์

## การใช้ร่วมกับเครื่องมืออื่นๆ

คุณสามารถใช้เครื่องมือบริบท URL ร่วมกับเครื่องมืออื่นๆ เพื่อสร้างเวิร์กโฟลว์ที่มีประสิทธิภาพมากขึ้น

[โมเดล Gemini 3](#supported-models) รองรับการใช้เครื่องมือในตัว
(เช่น บริบท URL) ร่วมกับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ในหน้าการใช้เครื่องมือร่วมกัน

### การเชื่อมต่อแหล่งข้อมูลกับ Search

เมื่อเปิดใช้ทั้งบริบท URL และ
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th) โมเดลจะใช้ความสามารถในการค้นหาเพื่อค้นหา
ข้อมูลที่เกี่ยวข้องทางออนไลน์ แล้วใช้เครื่องมือบริบท URL เพื่อทำความเข้าใจหน้าเว็บที่พบในเชิงลึกมากขึ้น แนวทางนี้มีประสิทธิภาพสำหรับพรอมต์ที่ต้องใช้ทั้งการค้นหาแบบกว้างและการวิเคราะห์หน้าเว็บที่เฉพาะเจาะจงในเชิงลึก

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## ทำความเข้าใจการตอบกลับ

เมื่อโมเดลใช้เครื่องมือบริบท URL การตอบกลับที่เป็นข้อความจะมีคำอธิบายประกอบ `url_citation` แบบอินไลน์ในบล็อกเนื้อหาข้อความ คำอธิบายประกอบแต่ละรายการจะลิงก์ส่วนของข้อความตอบกลับ (ผ่าน `start_index` และ `end_index`) กับ URL แหล่งที่มา นี่คือวิธีหลักในการแสดงคำอ้างอิงในแอปพลิเคชันของคุณ
โปรดดูวิธีแยกคำอ้างอิงใน[ตัวอย่างหลักด้านบน](#get-started)

การตอบกลับจะมีขั้นตอน `url_context_result` พร้อมข้อมูลเมตาเกี่ยวกับการพยายามดึงข้อมูล URL แต่ละครั้ง (สถานะ, URL ที่ดึงข้อมูล) ซึ่งมีประโยชน์สำหรับการแก้ไขข้อบกพร่องเป็นหลัก

### การตรวจสอบความปลอดภัย

ระบบจะตรวจสอบการกลั่นกรองเนื้อหาใน URL เพื่อยืนยันว่า URL เป็นไปตามมาตรฐานความปลอดภัย หาก URL ไม่ผ่านการตรวจสอบนี้ ขั้นตอนที่เกี่ยวข้อง
`url_context_result` จะแสดง `status` เป็น `"unsafe"`

### จำนวนโทเค็น

ระบบจะนับเนื้อหาที่ดึงมาจาก URL ที่คุณระบุในพรอมต์เป็นส่วนหนึ่งของโทเค็นอินพุต คุณดูจำนวนโทเค็นได้ในออบเจ็กต์ `usage` ของการโต้ตอบ ตัวอย่างเช่น

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

ราคาต่อโทเค็นจะขึ้นอยู่กับโมเดลที่ใช้ โปรดดูรายละเอียดในหน้าราคา

## โมเดลที่รองรับ

| รุ่น | บริบท URL |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=th) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=th) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Pro (เวอร์ชันทดลอง)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3 Flash (เวอร์ชันตัวอย่าง)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## แนวทางปฏิบัติแนะนำ

- **ระบุ URL ที่เฉพาะเจาะจง**: เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด ให้ระบุ URL โดยตรงไปยัง
  เนื้อหาที่ต้องการให้โมเดลวิเคราะห์ โมเดลจะดึงเนื้อหาจาก URL ที่คุณระบุเท่านั้น ไม่ดึงเนื้อหาจากลิงก์ที่ซ้อนกัน
- **ตรวจสอบการเข้าถึง**: ตรวจสอบว่า URL ที่คุณระบุไม่ได้นำไปยัง
  หน้าเว็บที่ต้องเข้าสู่ระบบหรืออยู่หลังเพย์วอลล์
- **ใช้ URL ที่สมบูรณ์**: ระบุ URL แบบเต็ม รวมถึงโปรโตคอล
  (เช่น https://www.google.com แทนที่จะเป็น google.com)

## ข้อจำกัด

- ขีดจำกัดคำขอ: เครื่องมือสามารถประมวลผล URL ได้สูงสุด 20 รายการต่อคำขอ
- ขนาดเนื้อหา URL: ขนาดสูงสุดของเนื้อหาที่ดึงมาจาก URL เดียวคือ 34 MB
- การเข้าถึงแบบสาธารณะ: URL ต้องเข้าถึงได้แบบสาธารณะบนเว็บ
  ระบบไม่รองรับที่อยู่ localhost (เช่น localhost, 127.0.0.1), เครือข่ายส่วนตัว และบริการทันเนล (เช่น ngrok, pinggy)

### ประเภทเนื้อหาที่รองรับและไม่รองรับ

เครื่องมือสามารถแยกเนื้อหาจาก URL ที่มีประเภทเนื้อหาต่อไปนี้

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

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-13 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-13 UTC"],[],[]]
