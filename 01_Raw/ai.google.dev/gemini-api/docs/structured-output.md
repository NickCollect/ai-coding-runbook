---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=ar
fetched_at: 2026-05-05T19:47:23.093447+00:00
title: "\u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u0646\u0638\u064e\u0651\u0645\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# النتائج المنظَّمة

يمكنك ضبط نماذج Gemini لإنشاء ردود تتوافق مع JSON Schema الذي تقدّمه. يضمن ذلك الحصول على نتائج متوقّعة وآمنة من ناحية النوع، ويُسهّل استخراج البيانات المنظَّمة من النصوص غير المنظَّمة.

يُعد استخدام المُخرجات المنظَّمة مثاليًا في الحالات التالية:

- **استخراج البيانات:** استخراج معلومات محدّدة، مثل الأسماء والتواريخ، من النص
- **التصنيف المنظَّم:** تصنيف النص ضِمن فئات محدَّدة مسبقًا
- **سير عمل الذكاء الاصطناعي الوكيل:** إنشاء مدخلات منظَّمة للأدوات أو واجهات برمجة التطبيقات

بالإضافة إلى إتاحة JSON Schema في REST API، تُسهّل حِزم Google GenAI SDK
تحديد المخطّطات باستخدام
[Pydantic](https://docs.pydantic.dev/latest/) (لغة Python) و
[Zod](https://zod.dev/) (لغة JavaScript).

Recipe Extractor
Content Moderation
Recursive Structures

يوضّح هذا المثال كيفية استخراج البيانات المنظَّمة من النص باستخدام أنواع JSON Schema الأساسية، مثل `object` و`array` و`string` و`integer`.

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

### انتقال

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

### راحة

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

**مثال على الردّ:**

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

## البث

يمكنك بث المُخرجات المنظَّمة، ما يسمح لك ببدء معالجة الردّ أثناء إنشائه، بدون الحاجة إلى انتظار اكتمال الإخراج بالكامل. يمكن أن يؤدي ذلك إلى تحسين الأداء المتصوَّر لتطبيقك.

ستكون الأجزاء التي يتم بثها عبارة عن سلاسل JSON جزئية صالحة، ويمكن ربطها لتشكيل كائن JSON النهائي الكامل.

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

## المُخرجات المنظَّمة مع الأدوات

يتيح لك Gemini 3 الجمع بين المُخرجات المنظَّمة والأدوات المضمّنة، بما في ذلك
[تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)،
[URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)،
[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)،
[File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=ar#structured-output)، و
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).

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

### راحة

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

## إتاحة JSON Schema

لإنشاء كائن JSON، اضبط `response_mime_type` في إعدادات الإنشاء على `application/json` وقدِّم `response_json_schema`. يجب أن يكون المخطّط [JSON Schema](https://json-schema.org/) صالحًا يصف تنسيق الإخراج المطلوب.

سينشئ النموذج بعد ذلك ردًا عبارة عن سلسلة JSON صالحة من الناحية النحوية وتتطابق مع المخطّط المقدَّم. عند استخدام المُخرجات المنظَّمة، سينتج النموذج مُخرجات بالترتيب نفسه الذي تظهر به المفاتيح في المخطّط.

يتيح وضع المُخرجات المنظَّمة في Gemini مجموعة فرعية من مواصفات [JSON Schema](https://json-schema.org).

القيم التالية لـ `type` متاحة:

- **`string`**: للنص
- **`number`**: لأرقام النقطة العائمة.
- **`integer`**: للأرقام الصحيحة
- **`boolean`**: لقيم "صحيح/خطأ"
- **`object`**: للبيانات المنظَّمة التي تتضمّن أزواجًا من القيم والمفاتيح
- **`array`**: لقوائم العناصر
- **`null`**: للسماح بأن تكون السمة فارغة، أدرِج `"null"` في مصفوفة النوع (مثل `{"type": ["string", "null"]}`).

تساعد هذه السمات الوصفية في توجيه النموذج:

- **`title`**: وصف قصير للسمة
- **`description`**: وصف أطول وأكثر تفصيلاً للسمة

### السمات الخاصة بالنوع

**لقيم `object`:**

- **`properties`**: كائن يكون فيه كل مفتاح اسم سمة وكل قيمة مخطّطًا لتلك السمة
- **`required`**: مصفوفة من السلاسل، تسرد السمات الإلزامية
- **`additionalProperties`**: تتحكّم في ما إذا كان يُسمح بالسمات غير المدرَجة في `properties` يمكن أن تكون قيمة منطقية أو مخطّطًا.

**لقيم `string`:**

- **`enum`**: تسرد مجموعة محدّدة من السلاسل المحتمَلة لمهام التصنيف
- **`format`**: تحدّد بنية السلسلة، مثل `date-time` أو `date` أو `time`

**لقيم `number` و`integer` القيم:**

- **`enum`**: تسرد مجموعة محدّدة من القيم الرقمية المحتمَلة
- **`minimum`**: الحد الأدنى للقيمة الشاملة
- **`maximum`**: الحد الأقصى للقيمة الشاملة

**لقيم `array`:**

- **`items`**: تحدّد المخطّط لجميع العناصر في المصفوفة
- **`prefixItems`**: تحدّد قائمة بالمخطّطات لأول N عنصر، ما يسمح ببُنى تشبه الصفوف
- **`minItems`**: الحد الأدنى لعدد العناصر في المصفوفة
- **`maxItems`**: الحد الأقصى لعدد العناصر في المصفوفة

## النماذج المتاحة

تتيح النماذج التالية المُخرجات المنظَّمة:

| الطراز | المُخرجات المنظَّمة |
| --- | --- |
| ‫Gemini 3.1 Pro (معاينة) | ✔️ |
| ‫Gemini 3 Flash (معاينة) | ✔️ |
| ‫Gemini 2.5 Pro | ✔️ |
| ‫Gemini 2.5 Flash | ✔️ |
| ‫Gemini 2.5 Flash-Lite | ✔️ |
| ‫Gemini 2.0 Flash | ‫✔️\* |
| ‫Gemini 2.0 Flash-Lite | ‫✔️\* |

*\* ملاحظة: يتطلّب Gemini 2.0 قائمة `propertyOrdering` صريحة ضِمن إدخال JSON لتحديد البنية المفضّلة. يمكنك الاطّلاع على مثال في دليل الطبخ هذا* .

## المُخرجات المنظَّمة مقابل استدعاء الدوال

يستخدم كلٌّ من المُخرجات المنظَّمة واستدعاء الدوال JSON Schema، ولكنّهما يخدمان أغراضًا مختلفة:

| الميزة | حالة الاستخدام الأساسية |
| --- | --- |
| **المُخرجات المنظَّمة** | **تنسيق الردّ النهائي للمستخدم** استخدِم هذه الميزة عندما تريد أن يكون *ردّ* النموذج بتنسيق معيّن (مثل استخراج البيانات من مستند لحفظها في قاعدة بيانات). |
| **استدعاء الدوال** | **اتخاذ إجراء أثناء المحادثة** استخدِم هذه الميزة عندما يحتاج النموذج إلى *أن يطلب منك* تنفيذ مهمة (مثل "الحصول على حالة الطقس الحالية") قبل أن يتمكّن من تقديم إجابة نهائية. |

## أفضل الممارسات

- **أوصاف واضحة:** استخدِم الحقل `description` في المخطّط لتقديم تعليمات واضحة للنموذج بشأن ما تمثله كل سمة. هذا أمر بالغ الأهمية لتوجيه إخراج النموذج.
- **التحقق من النوع:** استخدِم أنواعًا محدّدة (`integer` و`string` و`enum`) كلما أمكن ذلك. إذا كانت إحدى المَعلمات تتضمّن مجموعة محدودة من القيم الصالحة، استخدِم `enum`.
- **هندسة الطلبات:** وضِّح في طلبك ما تريد أن يفعله النموذج. على سبيل المثال، "استخرِج المعلومات التالية من النص..." أو "صنِّف هذه الملاحظات وفقًا للمخطّط المقدَّم...".
- **التحقّق من الصحة:** على الرغم من أنّ المُخرجات المنظَّمة تضمن أن يكون JSON صحيحًا من الناحية النحوية، فإنّها لا تضمن أن تكون القيم صحيحة من الناحية الدلالية. يجب دائمًا التحقّق من صحة الإخراج النهائي في الرمز البرمجي لتطبيقك قبل استخدامه.
- **التعامل مع الأخطاء:** نفِّذ عملية قوية للتعامل مع الأخطاء في تطبيقك لإدارة الحالات التي قد لا يفي فيها إخراج النموذج، على الرغم من امتثاله للمخطّط، بمتطلبات منطق عملك.

## القيود

- **مجموعة فرعية من المخطّطات:** لا تتوفّر جميع ميزات مواصفات JSON Schema. يتجاهل النموذج السمات غير المتاحة.
- **تعقيد المخطّط:** قد ترفض واجهة برمجة التطبيقات المخطّطات الكبيرة جدًا أو المتداخلة بشكل كبير. إذا واجهتك أخطاء، حاوِل تبسيط المخطّط من خلال تقصير أسماء السمات أو تقليل التداخل أو الحدّ من عدد القيود.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
