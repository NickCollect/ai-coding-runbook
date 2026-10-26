---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=bn
fetched_at: 2026-10-26T05:48:26.659521+00:00
title: "\u09b8\u09cd\u099f\u09cd\u09b0\u09be\u0995\u099a\u09be\u09b0\u09cd\u09a1 \u0986\u0989\u099f\u09aa\u09c1\u099f \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# স্ট্রাকচার্ড আউটপুট

আপনি Gemini মডেল কনফিগার করতে পারেন যাতে এটি প্রদত্ত JSON স্কিমা মেনে চলে এমন উত্তর তৈরি করে। এটি অনুমানযোগ্য, টাইপ-নিরাপদ ফলাফল নিশ্চিত করে এবং আনস্ট্রাকচার্ড টেক্সট থেকে স্ট্রাকচার্ড ডেটা এক্সট্র্যাক্ট করার প্রসেসকে সহজ করে তোলে।

স্ট্রাকচার্ড আউটপুট ব্যবহার করা এগুলির জন্য আদর্শ:

- **ডেটা এক্সট্র্যাকশন:** টেক্সট থেকে নাম ও তারিখের মতো নির্দিষ্ট তথ্য বের করে আনা।
- **স্ট্রাকচার্ড ক্লাসিফিকেশন:** পূর্বনির্ধারিত বিভাগে টেক্সট ক্লাসিফাই করুন।
- **এজেন্টিক ওয়ার্কফ্লো:** টুল বা API-এর জন্য স্ট্রাকচার্ড ইনপুট তৈরি করুন।

REST API-তে JSON স্কিমা সাপোর্ট করার পাশাপাশি, Google GenAI SDK
[Pydantic](https://docs.pydantic.dev/latest/) (Python) এবং
[Zod](https://zod.dev/) (JavaScript) ব্যবহার করে
সহজেই স্কিমা নির্ধারণ করতে সাহায্য করে।

## স্ট্রাকচার্ড আউটপুটের উদাহরণ

### রেসিপি এক্সট্র্যাক্টর

এই উদাহরণে দেখানো হয়েছে যে কীভাবে `object`, `array`, `string` ও `integer`-এর মতো বেসিক JSON স্কিমা টাইপ ব্যবহার করে টেক্সট থেকে স্ট্রাকচার্ড ডেটা এক্সট্র্যাক্ট করা যায়।

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

### জাভাস্ক্রিপ্ট

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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(recipeSchema),
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### খুলুন

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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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
        }
      }
    }'
```

**উদাহরণস্বরূপ উত্তর:**

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

### কন্টেন্ট মডারেশন

এই উদাহরণে কন্ডিশনাল স্কিমার জন্য `anyOf` এবং শ্রেণীবিন্যাসের জন্য `enum` দেখানো হয়েছে, যা কন্টেন্টের উপর ভিত্তি করে আউটপুট স্ট্রাকচার পরিবর্তন করার অনুমতি দেয়।

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": ModerationResult.model_json_schema(),
    },
)

result = ModerationResult.model_validate_json(response.text)
print(result)
```

### জাভাস্ক্রিপ্ট

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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(moderationResultSchema),
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
```

### খুলুন

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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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

### স্ট্রাকচারের পুনরাবৃত্তি

এই উদাহরণে দেখানো হয়েছে যে কীভাবে একটি রিকার্সিভ স্কিমা যেমন একটি প্রতিষ্ঠানের চার্ট
সংজ্ঞায়িত করা যায়।

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Employee.model_json_schema(),
    },
)

employee = Employee.model_validate_json(response.text)
print(employee)
```

### জাভাস্ক্রিপ্ট

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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(employeeSchema),
  },
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
```

### খুলুন

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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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
              },
              "required": ["name", "employee_id", "reports"]
            }
          }
        }
      }
    }'
```

**উদাহরণস্বরূপ উত্তর:**

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

## স্ট্রিমিং

আপনি স্ট্রাকচার্ড আউটপুট স্ট্রিম করতে পারেন, যা আপনাকে সম্পূর্ণ আউটপুট সম্পূর্ণ হওয়ার জন্য অপেক্ষা না করেই, জেনারেট হওয়ার সাথে সাথে উত্তর প্রসেস করা শুরু করতে দেয়। এটি আপনার অ্যাপ্লিকেশনের পারফর্ম্যান্স উন্নত করতে পারে।

স্ট্রিম করা চাঙ্কগুলি সঠিক আংশিক JSON স্ট্রিং হবে, যা
চূড়ান্ত, সম্পূর্ণ JSON অবজেক্ট তৈরি করতে কনক্যাটিনেট করা যেতে পারে।

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Feedback.model_json_schema(),
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

### জাভাস্ক্রিপ্ট

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
  model: "gemini-3.8-flash",
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

## টুলের মাধ্যমে স্ট্রাকচার্ড আউটপুট

Gemini 3 আপনাকে বিল্ট-ইন টুলের সাথে স্ট্রাকচার্ড আউটপুট একত্রিত করতে দেয়, যার মধ্যে রয়েছে
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn),
[URL কন্টেক্সট](https://ai.google.dev/gemini-api/docs/url-context?hl=bn),
[কোড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn),
[ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn#structured-output) এবং
[ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)।

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
    model="gemini-4-argon",
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

### জাভাস্ক্রিপ্ট

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
    model: "gemini-4-argon",
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

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
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
          "mimeType": "APPLICATION_JSON",
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
      }
    }
  }'
```

## JSON স্কিমা সংক্রান্ত সহায়তা

JSON অবজেক্ট তৈরি করতে, জেনারেশন কনফিগারেশনে `response_json_schema` (অথবা REST-এ `responseFormat.text.schema`) সেট করুন। স্কিমাটি অবশ্যই একটি সঠিক [JSON স্কিমা](https://json-schema.org/) হতে হবে যা কাঙ্ক্ষিত আউটপুট ফর্ম্যাট বর্ণনা করে।

মডেলটি তখন একটি উত্তর তৈরি করবে যা প্রদত্ত স্কিমার সাথে মিলে যায় এমন একটি সিনট্যাক্টিক্যালি সঠিক JSON স্ট্রিং। স্ট্রাকচার্ড আউটপুট ব্যবহার করার সময়, মডেলটি স্কিমার কীগুলির মতো একই ক্রমে আউটপুট তৈরি করবে।

Gemini-র স্ট্রাকচার্ড আউটপুট মোড [JSON স্কিমা](https://json-schema.org) স্পেসিফিকেশনের সাবসেট সাপোর্ট করে।

`type`-এর নিম্নলিখিত ভ্যালু কাজ করে:

- **`string`**: টেক্সটের জন্য।
- **`number`**: ফ্লোটিং-পয়েন্ট সংখ্যার জন্য।
- **`integer`**: পূর্ণ সংখ্যার জন্য।
- **`boolean`**: সত্য/মিথ্যা মানের জন্য।
- **`object`**: কী-ভ্যালু পেয়ার সহ স্ট্রাকচার্ড ডেটার জন্য।
- **`array`**: আইটেমের তালিকার জন্য।
- **`null`**: কোনও প্রপার্টিকে ফাঁকা রাখার অনুমতি দিতে, টাইপ অ্যারেতে `"null"` অন্তর্ভুক্ত করুন (যেমন, `{"type": ["string", "null"]}`)।

এইসব বর্ণনামূলক প্রপার্টি মডেলকে নির্দেশ দিতে সাহায্য করে:

- **`title`**: কোনও প্রপার্টির সংক্ষিপ্ত বিবরণ।
- **`description`**: কোনও প্রপার্টির আরও দীর্ঘ ও বিস্তারিত বিবরণ।

### ধরন-নির্দিষ্ট প্রপার্টি

**`object` ভ্যালুর জন্য:**

- **`properties`**: এমন একটি অবজেক্ট যেখানে প্রতিটি কী হল একটি প্রপার্টির নাম এবং প্রতিটি ভ্যালু হল সেই প্রপার্টির জন্য একটি স্কিমা।
- **`required`**: স্ট্রিংয়ের একটি অ্যারে, কোন কোন প্রপার্টি বাধ্যতামূলক তা তালিকাভুক্ত করে।
- **`additionalProperties`**: `properties`-এ তালিকাভুক্ত নয় এমন প্রপার্টি অনুমোদিত কিনা তা নিয়ন্ত্রণ করে। বুলিয়ান বা স্কিমা হতে পারে।

**`string` ভ্যালুর জন্য:**

- **`enum`**: ক্লাসিফিকেশন টাস্কের জন্য সম্ভাব্য স্ট্রিংয়ের নির্দিষ্ট সেট তালিকাভুক্ত করে।
- **`format`**: স্ট্রিংয়ের জন্য সিনট্যাক্স নির্দিষ্ট করে, যেমন `date-time`, `date`, `time`।

**`number` এবং `integer` ভ্যালুর জন্য:**

- **`enum`**: সম্ভাব্য সংখ্যাসূচক মানের একটি নির্দিষ্ট সেট তালিকাভুক্ত করে।
- **`minimum`**: ন্যূনতম ইনক্লুসিভ ভ্যালু।
- **`maximum`**: সর্বাধিক ইনক্লুসিভ ভ্যালু।

**`array` ভ্যালুর জন্য:**

- **`items`**: অ্যারের সব আইটেমের জন্য স্কিমা নির্ধারণ করে।
- **`prefixItems`**: প্রথম N আইটেমের জন্য স্কিমার তালিকা নির্ধারণ করে, যা টিউপলের মতো স্ট্রাকচারের অনুমতি দেয়।
- **`minItems`**: অ্যারেতে আইটেমের ন্যূনতম সংখ্যা।
- **`maxItems`**: অ্যারেতে আইটেমের সর্বাধিক সংখ্যা।

## মডেল সহায়তা

নিম্নলিখিত মডেলগুলি স্ট্রাকচার্ড আউটপুট সমর্থন করে:

| মডেল | স্ট্রাকচার্ড আউটপুট |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro প্রিভিউ | ✔️ |
| Gemini 3.1 Flash-Lite প্রিভিউ | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* মনে রাখবেন যে Gemini 2.0-এর ক্ষেত্রে পছন্দের স্ট্রাকচার নির্ধারণ করার জন্য JSON ইনপুটের মধ্যে একটি স্পষ্ট `propertyOrdering` তালিকা প্রয়োজন। আপনি এই [কুকবুক](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb)-এ একটি উদাহরণ দেখতে পাবেন।*

## স্ট্রাকচার্ড আউটপুট বনাম ফাংশন কলিং

স্ট্রাকচার্ড আউটপুট এবং ফাংশন কলিং, উভয় ক্ষেত্রেই JSON স্কিমা ব্যবহার করা হয়, তবে এগুলি আলাদা আলাদা উদ্দেশ্যে ব্যবহার করা হয়:

| ফিচার | প্রাথমিক ব্যবহারিক ক্ষেত্র |
| --- | --- |
| **স্ট্রাকচার্ড আউটপুট** | **ব্যবহারকারীর জন্য চূড়ান্ত উত্তর ফর্ম্যাট করা হচ্ছে।** মডেলের *উত্তর* নির্দিষ্ট কোনও ফর্ম্যাটে পেতে চাইলে এটি ব্যবহার করুন (যেমন, ডেটাবেসে সেভ করার জন্য কোনও ডকুমেন্ট থেকে ডেটা এক্সট্র্যাক্ট করা)। |
| **ফাংশন কলিং** | **কথোপকথন চলাকালীন অ্যাকশন নেওয়া।** মডেলকে কোনও চূড়ান্ত উত্তর দেওয়ার আগে কোনও টাস্ক (যেমন, "বর্তমান আবহাওয়ার তথ্য পাওয়া") সম্পূর্ণ করার জন্য *আপনাকে জিজ্ঞাসা* করতে হলে এটি ব্যবহার করুন। |

## পেশাদার পদ্ধতি

- **স্পষ্ট বিবরণ:** প্রতিটি প্রপার্টি কী উপস্থাপন করে সেই সম্পর্কে মডেলকে স্পষ্ট নির্দেশাবলী প্রদান করতে আপনার স্কিমার `description` ফিল্ড ব্যবহার করুন। মডেলের আউটপুটকে গাইড করার জন্য এটি অত্যন্ত গুরুত্বপূর্ণ।
- **স্ট্রং টাইপিং:** যখনই সম্ভব নির্দিষ্ট টাইপ (`integer`, `string`, `enum`) ব্যবহার করুন। কোনও প্যারামিটারে সীমিত সংখ্যক সঠিক ভ্যালু থাকলে, `enum` ব্যবহার করুন।
- **প্রম্পট ইঞ্জিনিয়ারিং:** আপনি মডেলকে দিয়ে কী করাতে চান তা আপনার প্রম্পটে স্পষ্টভাবে উল্লেখ করুন। যেমন, "টেক্সট থেকে নিম্নলিখিত তথ্য এক্সট্র্যাক্ট করুন..." বা "প্রদত্ত স্কিমা অনুযায়ী এই মতামত শ্রেণীবদ্ধ করুন..."।
- **যাচাইকরণ:** স্ট্রাকচার্ড আউটপুট সিনট্যাক্সগতভাবে সঠিক JSON-এর গ্যারেন্টি দিলেও, এটি ভ্যালুগুলি শব্দার্থগতভাবে সঠিক হওয়ার গ্যারেন্টি দেয় না। আপনার অ্যাপ্লিকেশন কোড ব্যবহার করার আগে সবসময় চূড়ান্ত আউটপুট যাচাই করুন।
- **সমস্যা ম্যানেজ করা:** আপনার অ্যাপ্লিকেশনে সমস্যা ম্যানেজ করার জন্য শক্তিশালী ব্যবস্থা প্রয়োগ করুন যাতে মডেলের আউটপুট স্কিমা-সম্মত হলেও আপনার ব্যবসার লজিক সংক্রান্ত প্রয়োজনীয়তা পূরণ না করলে, সেই পরিস্থিতি সুন্দরভাবে ম্যানেজ করা যায়।

## সীমাবদ্ধতা

- **স্কিমা সাবসেট:** JSON স্কিমা স্পেসিফিকেশনের সব ফিচার কাজ করে না। মডেলটি কাজ করে না এমন প্রপার্টি উপেক্ষা করে।
- **স্কিমার জটিলতা:** API খুব বড় বা গভীরভাবে নেস্ট করা স্কিমা প্রত্যাখ্যান করতে পারে। আপনি কোনও সমস্যার সম্মুখীন হলে, প্রপার্টির নাম ছোট করে, নেস্টিং কমিয়ে বা সীমাবদ্ধতার সংখ্যা সীমিত করে আপনার স্কিমা সহজ করার চেষ্টা করুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-19 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-19 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
