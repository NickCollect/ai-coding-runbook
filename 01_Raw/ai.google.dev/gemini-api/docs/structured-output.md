---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=th
fetched_at: 2026-05-05T20:07:10.712568+00:00
title: "\u0e40\u0e2d\u0e32\u0e15\u0e4c\u0e1e\u0e38\u0e15\u0e17\u0e35\u0e48\u0e21\u0e35\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอาต์พุตที่มีโครงสร้าง

คุณสามารถกำหนดค่าโมเดล Gemini ให้สร้างการตอบสนองที่เป็นไปตาม JSON Schema ที่ระบุได้ ซึ่งจะช่วยให้ได้ผลลัพธ์ที่คาดการณ์ได้และมีความปลอดภัยในการกำหนดประเภท รวมถึงทำให้การดึง Structured Data จากข้อความที่ไม่มีโครงสร้างเป็นเรื่องง่าย

การใช้เอาต์พุตที่มีโครงสร้างเหมาะสำหรับกรณีต่อไปนี้

- **การดึงข้อมูล:** ดึงข้อมูลที่เฉพาะเจาะจง เช่น ชื่อและวันที่ จากข้อความ
- **การจัดประเภทที่มีโครงสร้าง:** จัดประเภทข้อความเป็นหมวดหมู่ที่กำหนดไว้ล่วงหน้า
- **เวิร์กโฟลว์แบบ Agent:** สร้างอินพุตที่มีโครงสร้างสำหรับเครื่องมือหรือ API

นอกจากจะรองรับ JSON Schema ใน REST API แล้ว Google GenAI SDKs
ยังช่วยให้คุณกำหนดสคีมาได้ง่ายๆ โดยใช้
[Pydantic](https://docs.pydantic.dev/latest/) (Python) และ
[Zod](https://zod.dev/) (JavaScript)

Recipe Extractor
Content Moderation
Recursive Structures

ตัวอย่างนี้แสดงวิธีดึง Structured Data จากข้อความโดยใช้ประเภท JSON Schema พื้นฐาน เช่น `object`, `array`, `string` และ `integer`

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(recipeSchema),
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please extract the recipe from the following text.
  The user wants to make delicious chocolate chip cookies.
  They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
  1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
  3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
  For the best part, they'll need 2 cups of semisweet chocolate chips.
  First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
  baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
  until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
  ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
  onto ungreased baking sheets and bake for 9 to 11 minutes.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "recipe_name": map[string]any{
                    "type":        "string",
                    "description": "The name of the recipe.",
                },
                "prep_time_minutes": map[string]any{
                    "type":        "integer",
                    "description": "Optional time in minutes to prepare the recipe.",
                },
                "ingredients": map[string]any{
                    "type": "array",
                    "items": map[string]any{
                        "type": "object",
                        "properties": map[string]any{
                            "name": map[string]any{
                                "type":        "string",
                                "description": "Name of the ingredient.",
                            },
                            "quantity": map[string]any{
                                "type":        "string",
                                "description": "Quantity of the ingredient, including units.",
                            },
                        },
                        "required": []string{"name", "quantity"},
                    },
                },
                "instructions": map[string]any{
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
        ]
      }],
      "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
                },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
    }'
```

**ตัวอย่างการตอบสนอง**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    {
      "name": "all-purpose flour",
      "quantity": "2 and 1/4 cups"
    },
    {
      "name": "baking soda",
      "quantity": "1 teaspoon"
    },
    {
      "name": "salt",
      "quantity": "1 teaspoon"
    },
    {
      "name": "unsalted butter (softened)",
      "quantity": "1 cup"
    },
    {
      "name": "granulated sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "packed brown sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "vanilla extract",
      "quantity": "1 teaspoon"
    },
    {
      "name": "large eggs",
      "quantity": "2"
    },
    {
      "name": "semisweet chocolate chips",
      "quantity": "2 cups"
    }
  ],
  "instructions": [
    "Preheat the oven to 375°F (190°C).",
    "In a small bowl, whisk together the flour, baking soda, and salt.",
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
    "Beat in the vanilla and eggs, one at a time.",
    "Gradually beat in the dry ingredients until just combined.",
    "Stir in the chocolate chips.",
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
  ]
}
```

## สตรีมมิง

คุณสามารถสตรีมเอาต์พุตที่มีโครงสร้าง ซึ่งจะช่วยให้คุณเริ่มประมวลผลการตอบสนองได้ทันทีที่ระบบสร้างการตอบสนองนั้น โดยไม่ต้องรอให้เอาต์พุตทั้งหมดเสร็จสมบูรณ์ ซึ่งอาจช่วยปรับปรุงประสิทธิภาพที่รับรู้ได้ของแอปพลิเคชัน

ก้อนข้อมูลที่สตรีมจะเป็นสตริง JSON บางส่วนที่ถูกต้อง ซึ่งสามารถนำมารวมกันเพื่อสร้างออบเจ็กต์ JSON ที่สมบูรณ์

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Feedback.model_json_schema(),
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
  sentiment: z.enum(["positive", "neutral", "negative"]),
  summary: z.string(),
});

const stream = await ai.models.generateContentStream({
  model: "gemini-3-flash-preview",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(feedbackSchema),
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## เอาต์พุตที่มีโครงสร้างพร้อมเครื่องมือ

 

Gemini 3 ช่วยให้คุณรวมเอาต์พุตที่มีโครงสร้างเข้ากับเครื่องมือในตัวได้ ซึ่งรวมถึง
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th),
[URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=th),
[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution?hl=th),
[File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=th#structured-output) และ
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

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

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
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
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
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
        "responseMimeType": "application/json",
        "responseJsonSchema": {
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

## การรองรับ JSON Schema

หากต้องการสร้างออบเจ็กต์ JSON ให้ตั้งค่า `response_mime_type` ในการกำหนดค่าการสร้างเป็น `application/json` และระบุ `response_json_schema` สคีมาต้องเป็น [JSON Schema](https://json-schema.org/) ที่ถูกต้องซึ่งอธิบายรูปแบบเอาต์พุตที่ต้องการ

จากนั้นโมเดลจะสร้างการตอบสนองที่เป็นสตริง JSON ที่ถูกต้องตามหลักไวยากรณ์ซึ่งตรงกับสคีมาที่ระบุ เมื่อใช้เอาต์พุตที่มีโครงสร้าง โมเดลจะสร้างเอาต์พุตตามลำดับเดียวกับคีย์ในสคีมา

โหมดเอาต์พุตที่มีโครงสร้างของ Gemini รองรับข้อมูลย่อยของข้อกำหนด [JSON Schema](https://json-schema.org)

ระบบรองรับค่า `type` ต่อไปนี้

- **`string`**: สำหรับข้อความ
- **`number`**: สำหรับเลขจุดลอยตัว
- **`integer`**: สำหรับจำนวนเต็ม
- **`boolean`**: สำหรับค่าจริง/เท็จ
- **`object`**: สำหรับ Structured Data พร้อมคู่คีย์-ค่า
- **`array`**: สำหรับรายการไอเทม
- **`null`**: หากต้องการอนุญาตให้พร็อพเพอร์ตี้เป็น Null ให้ใส่ `"null"` ในอาร์เรย์ประเภท (เช่น `{"type": ["string", "null"]}`)

พร็อพเพอร์ตี้เชิงอธิบายเหล่านี้ช่วยแนะนำโมเดล

- **`title`**: คำอธิบายสั้นๆ ของพร็อพเพอร์ตี้
- **`description`**: คำอธิบายที่ยาวและละเอียดมากขึ้นของพร็อพเพอร์ตี้

### พร็อพเพอร์ตี้เฉพาะประเภท

**สำหรับค่า `object`**

- **`properties`**: ออบเจ็กต์ที่แต่ละคีย์เป็นชื่อพร็อพเพอร์ตี้และแต่ละค่าเป็นสคีมาสำหรับพร็อพเพอร์ตี้นั้น
- **`required`**: อาร์เรย์ของสตริงที่แสดงรายการพร็อพเพอร์ตี้ที่จำเป็น
- **`additionalProperties`**: ควบคุมว่าจะอนุญาตพร็อพเพอร์ตี้ที่ไม่ได้ระบุไว้ใน `properties` หรือไม่ โดยอาจเป็นบูลีนหรือสคีมา

**สำหรับค่า `string`**

- **`enum`**: แสดงรายการชุดสตริงที่เป็นไปได้ที่เฉพาะเจาะจงสำหรับงานการจัดประเภท
- **`format`**: ระบุไวยากรณ์สำหรับสตริง เช่น `date-time`, `date`, `time`

**สำหรับค่า `number` และ `integer`**

- **`enum`**: แสดงรายการชุดค่าตัวเลขที่เป็นไปได้ที่เฉพาะเจาะจง
- **`minimum`**: ค่าต่ำสุดแบบรวม
- **`maximum`**: ค่าสูงสุดแบบรวม

**สำหรับค่า `array`**

- **`items`**: กำหนดสคีมาสำหรับไอเทมทั้งหมดในอาร์เรย์
- **`prefixItems`**: กำหนดรายการสคีมาสำหรับไอเทม N รายการแรก ซึ่งอนุญาตให้ใช้โครงสร้างคล้ายทูเพิล
- **`minItems`**: จำนวนไอเทมขั้นต่ำในอาร์เรย์
- **`maxItems`**: จำนวนไอเทมสูงสุดในอาร์เรย์

## การรองรับโมเดล

โมเดลต่อไปนี้รองรับเอาต์พุตที่มีโครงสร้าง

| โมเดล | เอาต์พุตที่มีโครงสร้าง |
| --- | --- |
| Gemini 3.1 Pro (เวอร์ชันตัวอย่าง) | ✔️ |
| Gemini 3 Flash (เวอร์ชันตัวอย่าง) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* โปรดทราบว่า Gemini 2.0 ต้องมีรายการ `propertyOrdering` ที่ชัดเจนภายในอินพุต JSON เพื่อกำหนดโครงสร้างที่ต้องการ คุณดูตัวอย่างได้ในคู่มือนี้ [cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb).*

## เอาต์พุตที่มีโครงสร้างเทียบกับการเรียกฟังก์ชัน

ทั้งเอาต์พุตที่มีโครงสร้างและการเรียกฟังก์ชันใช้ JSON Schema แต่มีวัตถุประสงค์ที่แตกต่างกัน

| ฟีเจอร์ | กรณีการใช้งานหลัก |
| --- | --- |
| **เอาต์พุตที่มีโครงสร้าง** | **การจัดรูปแบบการตอบสนองสุดท้ายที่จะแสดงต่อผู้ใช้** ใช้ฟีเจอร์นี้เมื่อต้องการให้ *คำตอบ* ของโมเดลอยู่ในรูปแบบที่เฉพาะเจาะจง (เช่น การดึงข้อมูลจากเอกสารเพื่อบันทึกลงในฐานข้อมูล) |
| **การเรียกฟังก์ชัน** | **การดำเนินการระหว่างการสนทนา** ใช้ฟีเจอร์นี้เมื่อโมเดลต้อง *ขอให้คุณ* ทำงาน (เช่น "รับสภาพอากาศปัจจุบัน") ก่อนที่จะให้คำตอบสุดท้ายได้ |

## แนวทางปฏิบัติแนะนำ

- **คำอธิบายที่ชัดเจน:** ใช้ช่อง `description` ในสคีมาเพื่อระบุวิธีการที่ชัดเจนให้โมเดลทราบว่าพร็อพเพอร์ตี้แต่ละรายการแสดงถึงอะไร ซึ่งเป็นสิ่งสำคัญในการแนะนำเอาต์พุตของโมเดล
- **การพิมพ์ที่เข้มงวด:** ใช้ประเภทที่เฉพาะเจาะจง (`integer`, `string`, `enum`) ทุกครั้งที่ทำได้ หากพารามิเตอร์มีชุดค่าที่ถูกต้องแบบจำกัด ให้ใช้ `enum`
- **วิศวกรรมพรอมต์ (Prompt Engineering):** ระบุในพรอมต์อย่างชัดเจนว่าต้องการให้โมเดลทำอะไร เช่น "ดึงข้อมูลต่อไปนี้จากข้อความ..." หรือ "จัดประเภทความคิดเห็นนี้ตามสคีมาที่ระบุ..."
- **การตรวจสอบความถูกต้อง:** แม้ว่าเอาต์พุตที่มีโครงสร้างจะรับประกัน JSON ที่ถูกต้องตามหลักไวยากรณ์ แต่ก็ไม่ได้การันตีว่าค่าจะถูกต้องตามความหมาย ดังนั้นให้ตรวจสอบความถูกต้องของเอาต์พุตสุดท้ายในโค้ดของแอปพลิเคชันก่อนที่จะใช้งานเสมอ
- **การจัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดที่มีประสิทธิภาพในแอปพลิเคชันเพื่อจัดการกรณีที่เอาต์พุตของโมเดลเป็นไปตามสคีมา แต่ไม่ตรงกับข้อกำหนดทางตรรกะทางธุรกิจของคุณ

## ข้อจำกัด

- **ข้อมูลย่อยของสคีมา:** ระบบไม่รองรับฟีเจอร์บางอย่างของข้อกำหนด JSON Schema โดยโมเดลจะละเว้นพร็อพเพอร์ตี้ที่ไม่รองรับ
- **ความซับซ้อนของสคีมา:** API อาจปฏิเสธสคีมาที่มีขนาดใหญ่มากหรือมีการซ้อนกันหลายชั้น หากพบข้อผิดพลาด ให้ลองลดความซับซ้อนของสคีมาโดยย่อชื่อพร็อพเพอร์ตี้ ลดการซ้อน หรือจำกัดจำนวนข้อจำกัด

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
