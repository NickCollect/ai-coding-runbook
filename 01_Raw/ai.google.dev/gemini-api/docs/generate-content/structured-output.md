---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=th
fetched_at: 2026-08-24T02:26:48.243945+00:00
title: "\u0e40\u0e2d\u0e32\u0e15\u0e4c\u0e1e\u0e38\u0e15\u0e17\u0e35\u0e48\u0e21\u0e35\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอาต์พุตที่มีโครงสร้าง

คุณสามารถกำหนดค่าโมเดล Gemini ให้สร้างการตอบกลับที่เป็นไปตาม JSON Schema ที่ให้ไว้ได้ ซึ่งจะช่วยให้ได้ผลลัพธ์ที่คาดการณ์ได้และมีความปลอดภัยในการกำหนดประเภท รวมถึงทำให้การแยก Structured Data จากข้อความที่ไม่มีโครงสร้างเป็นเรื่องง่าย

การใช้เอาต์พุตที่มีโครงสร้างเหมาะสำหรับกรณีต่อไปนี้

- **การแยกข้อมูล:** ดึงข้อมูลที่เฉพาะเจาะจง เช่น ชื่อและวันที่ จากข้อความ
- **การจัดประเภทที่มีโครงสร้าง:** จัดประเภทข้อความเป็นหมวดหมู่ที่กำหนดไว้ล่วงหน้า
- **เวิร์กโฟลว์แบบ Agent:** สร้างอินพุตที่มีโครงสร้างสำหรับเครื่องมือหรือ API

นอกจากจะรองรับ JSON Schema ใน REST API แล้ว Google GenAI SDKs
ยังช่วยให้คุณกำหนดสคีมาได้ง่ายๆ โดยใช้
[Pydantic](https://docs.pydantic.dev/latest/) (Python) และ
[Zod](https://zod.dev/) (JavaScript)

## ตัวอย่างเอาต์พุตที่มีโครงสร้าง

### ตัวแยกสูตรอาหาร

ตัวอย่างนี้แสดงวิธีแยก Structured Data จากข้อความโดยใช้ประเภท JSON Schema พื้นฐาน เช่น `object`, `array`, `string` และ `integer`

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
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Recipe.model_json_schema()}},
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
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
          }
        }
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

**ตัวอย่างการตอบกลับ:**

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

### การกลั่นกรองเนื้อหา

ตัวอย่างนี้แสดง `anyOf` สำหรับสคีมาแบบมีเงื่อนไขและ `enum` สำหรับการจัดประเภท ซึ่งช่วยให้โครงสร้างเอาต์พุตแตกต่างกันไปตามเนื้อหาได้

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Union, Literal

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"] = Field(description="The type of spam.")

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

client = genai.Client()

prompt = """
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": ModerationResult.model_json_schema()}},
    },
)

result = ModerationResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const spamDetailsSchema = z.object({
  reason: z.string().describe("The reason why the content is considered spam."),
  spam_type: z.enum(["phishing", "scam", "unsolicited promotion", "other"]).describe("The type of spam."),
});

const notSpamDetailsSchema = z.object({
  summary: z.string().describe("A brief summary of the content."),
  is_safe: z.boolean().describe("Whether the content is safe for all audiences."),
});

const moderationResultSchema = z.object({
  decision: z.union([spamDetailsSchema, notSpamDetailsSchema]),
});

const ai = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(moderationResultSchema) } },
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
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
  Please moderate the following content and provide a decision.
  Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "decision": map[string]any{
                    "anyOf": []map[string]any{
                        {
                            "type":        "object",
                            "title":       "SpamDetails",
                            "description": "Details for content classified as spam.",
                            "properties": map[string]any{
                                "reason": map[string]any{
                                    "type":        "string",
                                    "description": "The reason why the content is considered spam.",
                                },
                                "spam_type": map[string]any{
                                    "type":        "string",
                                    "enum":        []string{"phishing", "scam", "unsolicited promotion", "other"},
                                    "description": "The type of spam.",
                                },
                            },
                            "required": []string{"reason", "spam_type"},
                        },
                        {
                            "type":        "object",
                            "title":       "NotSpamDetails",
                            "description": "Details for content classified as not spam.",
                            "properties": map[string]any{
                                "summary": map[string]any{
                                    "type":        "string",
                                    "description": "A brief summary of the content.",
                                },
                                "is_safe": map[string]any{
                                    "type":        "boolean",
                                    "description": "Whether the content is safe for all audiences.",
                                },
                            },
                            "required": []string{"summary", "is_safe"},
                        },
                    },
                },
            },
            "required": []string{"decision"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please moderate the following content and provide a decision.\nContent: ''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com''" }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "decision": {
              "anyOf": [
                {
                  "type": "object",
                  "title": "SpamDetails",
                  "description": "Details for content classified as spam.",
                  "properties": {
                    "reason": { "type": "string", "description": "The reason why the content is considered spam." },
                    "spam_type": { "type": "string", "enum": ["phishing", "scam", "unsolicited promotion", "other"], "description": "The type of spam." }
          }
        }
      },
                   "required": ["reason", "spam_type"]
                 },
                 {
                   "type": "object",
                   "title": "NotSpamDetails",
                   "description": "Details for content classified as not spam.",
                   "properties": {
                     "summary": { "type": "string", "description": "A brief summary of the content." },
                     "is_safe": { "type": "boolean", "description": "Whether the content is safe for all audiences." }
                   },
                   "required": ["summary", "is_safe"]
                 }
               ]
             }
           },
           "required": ["decision"]
         }
       }
     }'
 ```

**Example Response:**

```json
{
"decision": {
 "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
 "spam_type": "scam"
}
}
```

### โครงสร้างแบบวนซ้ำ

ตัวอย่างนี้แสดงวิธีกำหนดสคีมาแบบวนซ้ำ เช่น แผนผังองค์กร

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class Employee(BaseModel):
    """Represents an employee in an organization."""
    name: str
    employee_id: int
    reports: List["Employee"] = Field(
        default_factory=list,
        description="A list of employees reporting to this employee."
    )

client = genai.Client()

prompt = """
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Employee.model_json_schema()}},
    },
)

employee = Employee.model_validate_json(response.text)
print(employee)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const employeeSchema = z.object({
  name: z.string(),
  employee_id: z.number().int(),
  reports: z.lazy(() => z.array(employeeSchema)).describe("A list of employees reporting to this employee."),
});

const ai = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(employeeSchema) } },
  },
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
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
  Generate an organization chart for a small team.
  The manager is Alice, who manages Bob and Charlie. Bob manages David.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "name":        map[string]any{"type": "string"},
                "employee_id": map[string]any{"type": "integer"},
                "reports": map[string]any{
                    "type":        "array",
                    "description": "A list of employees reporting to this employee.",
                    "items": map[string]any{
                        "$ref": "#",
                    },
                },
            },
            "required": []string{"name", "employee_id", "reports"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David." }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "employee_id": { "type": "integer" },
            "reports": {
              "type": "array",
              "description": "A list of employees reporting to this employee.",
              "items": {
                "$ref": "#"
              }
          }
        }
      }
          },
          "required": ["name", "employee_id", "reports"]
        }
      }
    }'
```

**ตัวอย่างการตอบกลับ:**

```
{
  "name": "Alice",
  "employee_id": 101,
  "reports": [
    {
      "name": "Bob",
      "employee_id": 102,
      "reports": [
        {
          "name": "David",
          "employee_id": 104,
          "reports": []
        }
      ]
    },
    {
      "name": "Charlie",
      "employee_id": 103,
      "reports": []
    }
  ]
}
```

## การสตรีม

คุณสามารถสตรีมเอาต์พุตที่มีโครงสร้าง ซึ่งจะช่วยให้คุณเริ่มประมวลผลการตอบกลับได้ทันทีที่ระบบสร้างการตอบกลับ โดยไม่ต้องรอให้เอาต์พุตทั้งหมดเสร็จสมบูรณ์ ซึ่งจะช่วยปรับปรุงประสิทธิภาพการทำงานของแอปพลิเคชันที่คุณรับรู้ได้

ก้อนข้อมูลที่สตรีมจะเป็นสตริง JSON บางส่วนที่ถูกต้อง ซึ่งสามารถนำมารวมกันเพื่อสร้างออบเจ็กต์ JSON ที่สมบูรณ์และถูกต้อง

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
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Feedback.model_json_schema()}},
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## เอาต์พุตที่มีโครงสร้างพร้อมเครื่องมือ

Gemini 3 ช่วยให้คุณรวมเอาต์พุตที่มีโครงสร้างเข้ากับเครื่องมือในตัวได้ ซึ่งรวมถึง
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th),
[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th),
[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th),
[File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=th#structured-output) และ
[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

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

## การรองรับ JSON Schema

หากต้องการสร้างออบเจ็กต์ JSON ให้ตั้งค่า `response_format` ในการกำหนดค่าการสร้าง สคีมาต้องเป็น [JSON Schema](https://json-schema.org/) ที่ถูกต้องซึ่งอธิบายรูปแบบเอาต์พุตที่ต้องการ

จากนั้นโมเดลจะสร้างการตอบกลับที่เป็นสตริง JSON ที่ถูกต้องตามหลักไวยากรณ์ซึ่งตรงกับสคีมาที่ให้ไว้ เมื่อใช้เอาต์พุตที่มีโครงสร้าง โมเดลจะสร้างเอาต์พุตตามลำดับเดียวกับคีย์ในสคีมา

โหมดเอาต์พุตที่มีโครงสร้างของ Gemini รองรับข้อมูลย่อยของข้อกำหนด [JSON Schema](https://json-schema.org)

ระบบรองรับค่า `type` ต่อไปนี้

- **`string`**: สำหรับข้อความ
- **`number`**: สำหรับเลขทศนิยม
- **`integer`**: สำหรับจำนวนเต็ม
- **`boolean`**: สำหรับค่าจริง/เท็จ
- **`object`**: สำหรับ Structured Data พร้อมคู่คีย์-ค่า
- **`array`**: สำหรับรายการไอเทม
- **`null`**: หากต้องการอนุญาตให้พร็อพเพอร์ตี้เป็นค่า Null ให้ใส่ `"null"` ในอาร์เรย์ประเภท (เช่น `{"type": ["string", "null"]}`)

พร็อพเพอร์ตี้เชิงอธิบายเหล่านี้จะช่วยแนะนำโมเดล

- **`title`**: คำอธิบายสั้นๆ ของพร็อพเพอร์ตี้
- **`description`**: คำอธิบายที่ยาวและละเอียดมากขึ้นของพร็อพเพอร์ตี้

### พร็อพเพอร์ตี้เฉพาะประเภท

**สำหรับค่า `object`**

- **`properties`**: ออบเจ็กต์ที่แต่ละคีย์เป็นชื่อพร็อพเพอร์ตี้และแต่ละค่าเป็นสคีมาสำหรับพร็อพเพอร์ตี้นั้น
- **`required`**: อาร์เรย์ของสตริงที่แสดงรายการพร็อพเพอร์ตี้ที่ต้องระบุ
- **`additionalProperties`**: ควบคุมว่าจะอนุญาตพร็อพเพอร์ตี้ที่ไม่ได้แสดงใน `properties` หรือไม่ โดยอาจเป็นค่าบูลีนหรือสคีมา

**สำหรับค่า `string`**

- **`enum`**: แสดงรายการชุดสตริงที่เป็นไปได้ที่เฉพาะเจาะจงสำหรับงานการจัดประเภท
- **`format`**: ระบุไวยากรณ์สำหรับสตริง เช่น `date-time`, `date`, `time`

**สำหรับค่า `number` และ `integer`**

- **`enum`**: แสดงรายการชุดค่าตัวเลขที่เป็นไปได้ที่เฉพาะเจาะจง
- **`minimum`**: ค่าต่ำสุดแบบรวม
- **`maximum`**: ค่าสูงสุดแบบรวม

**สำหรับค่า `array`**

- **`items`**: กำหนดสคีมาสำหรับไอเทมทั้งหมดในอาร์เรย์
- **`prefixItems`**: กำหนดรายการสคีมาสำหรับไอเทม N รายการแรก ซึ่งอนุญาตให้ใช้โครงสร้างคล้ายกับ Tuple
- **`minItems`**: จำนวนไอเทมขั้นต่ำในอาร์เรย์
- **`maxItems`**: จำนวนไอเทมสูงสุดในอาร์เรย์

## การรองรับโมเดล

โมเดลต่อไปนี้รองรับเอาต์พุตที่มีโครงสร้าง

| โมเดล | เอาต์พุตที่มีโครงสร้าง |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro (เวอร์ชันตัวอย่าง) | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* โปรดทราบว่า Gemini 2.0 ต้องมีรายการ `propertyOrdering` ที่ชัดเจนภายในอินพุต JSON เพื่อกำหนดโครงสร้างที่ต้องการ ดูตัวอย่างได้ใน [Cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb) นี้*

## เอาต์พุตที่มีโครงสร้างเทียบกับการเรียกฟังก์ชัน

ทั้งเอาต์พุตที่มีโครงสร้างและการเรียกฟังก์ชันใช้ JSON Schema แต่มีวัตถุประสงค์ที่แตกต่างกัน

| ฟีเจอร์ | กรณีการใช้งานหลัก |
| --- | --- |
| **เอาต์พุตที่มีโครงสร้าง** | **การจัดรูปแบบการตอบกลับสุดท้ายที่จะแสดงต่อผู้ใช้** ใช้ฟีเจอร์นี้เมื่อต้องการให้ *คำตอบ* ของโมเดลอยู่ในรูปแบบที่เฉพาะเจาะจง (เช่น การแยกข้อมูลจากเอกสารเพื่อบันทึกลงในฐานข้อมูล) |
| **การเรียกฟังก์ชัน** | **การดำเนินการระหว่างการสนทนา** ใช้ฟีเจอร์นี้เมื่อโมเดลต้อง *ขอให้คุณ* ทำงาน (เช่น "รับสภาพอากาศปัจจุบัน") ก่อนที่จะให้คำตอบสุดท้ายได้ |

## แนวทางปฏิบัติแนะนำ

- **คำอธิบายที่ชัดเจน:** ใช้ช่อง `description` ในสคีมาเพื่อระบุคำแนะนำที่ชัดเจนแก่โมเดลเกี่ยวกับสิ่งที่พร็อพเพอร์ตี้แต่ละรายการแสดง ซึ่งมีความสำคัญอย่างยิ่งในการแนะนำเอาต์พุตของโมเดล
- **การพิมพ์ที่เข้มงวด:** ใช้ประเภทที่เฉพาะเจาะจง (`integer`, `string`, `enum`) ทุกครั้งที่ทำได้ หากพารามิเตอร์มีชุดค่าที่ถูกต้องแบบจำกัด ให้ใช้ `enum`
- **วิศวกรรมพรอมต์ (Prompt Engineering):** ระบุในพรอมต์อย่างชัดเจนว่าต้องการให้โมเดลทำอะไร เช่น "แยกข้อมูลต่อไปนี้จากข้อความ..." หรือ "จัดประเภทความคิดเห็นนี้ตามสคีมาที่ให้ไว้..."
- **การตรวจสอบความถูกต้อง:** แม้ว่าเอาต์พุตที่มีโครงสร้างจะรับประกัน JSON ที่ถูกต้องตามหลักไวยากรณ์ แต่ก็ไม่รับประกันว่าค่าจะถูกต้องตามความหมาย ดังนั้นคุณควรตรวจสอบความถูกต้องของเอาต์พุตสุดท้ายในโค้ดของแอปพลิเคชันก่อนที่จะนำไปใช้เสมอ
- **การจัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดที่มีประสิทธิภาพในแอปพลิเคชันเพื่อจัดการกรณีที่เอาต์พุตของโมเดลเป็นไปตามสคีมา แต่ไม่ตรงกับข้อกำหนดทางตรรกะทางธุรกิจของคุณ

## ข้อจำกัด

- **ข้อมูลย่อยของสคีมา:** ระบบไม่รองรับฟีเจอร์บางอย่างของข้อกำหนด JSON Schema โดยโมเดลจะละเว้นพร็อพเพอร์ตี้ที่ไม่รองรับ
- **ความซับซ้อนของสคีมา:** API อาจปฏิเสธสคีมาที่มีขนาดใหญ่มากหรือมีการซ้อนกันหลายชั้น หากพบข้อผิดพลาด ให้ลองลดความซับซ้อนของสคีมาโดยย่อชื่อพร็อพเพอร์ตี้ ลดการซ้อน หรือจำกัดจำนวนข้อจำกัด

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
