---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=he
fetched_at: 2026-05-18T05:14:08.580124+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פלטים מובנים

אתם יכולים להגדיר מודלים של Gemini כדי ליצור תשובות שתואמות לסכימת JSON שסיפקתם. כך אפשר להבטיח תוצאות צפויות ובטוחות מבחינת סוג הנתונים, ולפשט את תהליך החילוץ של נתונים מובְנים מטקסט לא מובְנה.

שימוש בפלט מובנה מתאים במיוחד למקרים הבאים:

- **חילוץ נתונים:** חילוץ מידע ספציפי כמו שמות ותאריכים מטקסט.
- **סיווג מובנה:** סיווג טקסט לקטגוריות מוגדרות מראש.
- **תהליכי עבודה מבוססי-סוכן:** יצירת קלט מובנה לכלים או לממשקי API.

בנוסף לתמיכה בסכימת JSON ב-API בארכיטקטורת REST, ערכות ה-SDK של Google GenAI מאפשרות להגדיר סכימות בקלות באמצעות [Pydantic](https://docs.pydantic.dev/latest/) (Python) ו-[Zod](https://zod.dev/) (JavaScript).

Recipe Extractor
Content Moderation
Recursive Structures

בדוגמה הזו מוסבר איך לחלץ נתונים מוּבְנִים מטקסט באמצעות סוגים בסיסיים של סכימת JSON, כמו `object`, `array`, `string` ו-`integer`.

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
  model: "gemini-3-flash-preview",
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

**דוגמה לתשובה:**

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

## סטרימינג

אתם יכולים להזרים פלט מובנה, וכך להתחיל לעבד את התגובה בזמן שהיא נוצרת, בלי לחכות לסיום של כל הפלט. כך אפשר לשפר את הביצועים של האפליקציה.

החלקים שמוזרמים יהיו מחרוזות JSON חלקיות ותקינות, שאפשר לשרשר כדי ליצור את אובייקט ה-JSON הסופי והמלא.

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
  model: "gemini-3-flash-preview",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## פלט מובנה עם כלים

‫Gemini 3 מאפשר לכם לשלב פלט מובנה עם כלים מובנים, כולל [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he), [הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he), [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he), [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he#structured-output) ו[קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

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

## תמיכה בסכימת JSON

כדי ליצור אובייקט JSON, מגדירים את `response_format` בהגדרות היצירה. הסכימה צריכה להיות [סכימת JSON](https://json-schema.org/) תקינה שמתארת את פורמט הפלט הרצוי.

המודל ייצור תגובה שהיא מחרוזת JSON תקינה מבחינת התחביר, שתואמת לסכימה שצוינה. כשמשתמשים בפלט מובנה, המודל יפיק פלט באותו סדר של המפתחות בסכימה.

מצב הפלט המובנה של Gemini תומך בחלק ממפרט [JSON Schema](https://json-schema.org).

יש תמיכה בערכים הבאים של `type`:

- ‫**`string`**: לטקסט.
- ‫**`number`**: למספרים בשיטת נקודה צפה.
- ‫**`integer`**: למספרים שלמים.
- ‫**`boolean`**: לערכים מסוג true/false.
- ‫**`object`**: לנתונים מובְנים עם צמדי מפתח/ערך.
- ‫**`array`**: לרשימות של פריטים.
- ‫**`null`**: כדי לאפשר שמאפיין יהיה null, צריך לכלול את `"null"` במערך הסוגים (לדוגמה, `{"type": ["string", "null"]}`).

מאפייני התיאור האלה עוזרים להנחות את המודל:

- ‫**`title`**: תיאור קצר של מאפיין.
- ‫**`description`**: תיאור ארוך ומפורט יותר של נכס.

### מאפיינים ספציפיים לסוג

**לערכים של `object`:**

- ‫**`properties`**: אובייקט שבו כל מפתח הוא שם מאפיין וכל ערך הוא סכימה של המאפיין הזה.
- ‫**`required`**: מערך של מחרוזות, שבו מפורטות המאפיינים שהם חובה.
- ‫**`additionalProperties`**: קובעת אם מותר להשתמש בנכסים שלא מופיעים ב-`properties`. יכול להיות ערך בוליאני או סכמה.

**לערכים של `string`:**

- ‫**`enum`**: רשימה של קבוצה ספציפית של מחרוזות אפשריות למשימות סיווג.
- ‫**`format`**: מציין תחביר למחרוזת, כמו `date-time`, ‏`date`, ‏`time`.

**לערכים `number` ו-`integer`:**

- ‫**`enum`**: רשימה של קבוצה ספציפית של ערכים נומריים אפשריים.
- ‫**`minimum`**: ערך המינימום כולל.
- ‫**`maximum`**: הערך המקסימלי כולל.

**לערכים של `array`:**

- ‫**`items`**: הגדרת הסכימה של כל הפריטים במערך.
- ‫**`prefixItems`**: מגדיר רשימה של סכימות עבור הפריטים הראשונים, ומאפשר מבנים דמויי-tuple.
- ‫**`minItems`**: המספר המינימלי של פריטים במערך.
- ‫**`maxItems`**: המספר המקסימלי של פריטים במערך.

## תמיכה במודלים

המודלים הבאים תומכים בפלט מובנה:

| מודל | פלט מובנה |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| ‫Gemini 3.1 Pro Preview | ✔️ |
| ‫Gemini 3 Flash Preview | ✔️ |
| גרסת טרום-השקה (Preview) של Gemini 3.1 Flash-Lite | ✔️ |
| Gemini ‎2.5 Pro | ✔️ |
| Gemini ‎2.5 Flash | ✔️ |
| Gemini ‎2.5 Flash-Lite | ✔️ |
| Gemini ‎2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* שימו לב: כדי להגדיר את המבנה המועדף ב-Gemini 2.0, צריך להוסיף רשימה מפורשת של `propertyOrdering` בקלט ה-JSON. דוגמה מופיעה ב[ספר המתכונים הזה](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb).*

## פלט מובנה לעומת בקשה להפעלת פונקציה

גם פלט מובנה וגם קריאה לפונקציה משתמשים בסכימות JSON, אבל הם משמשים למטרות שונות:

| תכונה | תרחיש שימוש ראשי |
| --- | --- |
| **פלט מובנה** | **עיצוב התשובה הסופית למשתמש.** משתמשים בזה כשרוצים ש*התשובה* של המודל תהיה בפורמט ספציפי (למשל, שליפת נתונים ממסמך כדי לשמור אותם במסד נתונים). |
| **בקשה להפעלת פונקציה** | **ביצוע פעולות במהלך השיחה** משתמשים בזה כשהמודל צריך *לשאול אתכם* לבצע משימה (למשל, 'קבלת נתוני מזג האוויר הנוכחי') לפני שהוא יכול לספק תשובה סופית. |

## שיטות מומלצות

- **תיאורים ברורים:** משתמשים בשדה `description` בסכימה כדי לספק למודל הוראות ברורות לגבי מה מייצג כל מאפיין. ההנחיה הזו חשובה מאוד כדי להנחות את הפלט של המודל.
- **הקלדה חזקה:** מומלץ להשתמש בסוגים ספציפיים (`integer`, `string`, `enum`) בכל הזדמנות. אם לפרמטר יש קבוצה מוגבלת של ערכים תקינים, משתמשים ב-`enum`.
- **הנדסת הנחיות:** בהנחיה צריך לציין בבירור מה רוצים שהמודל יעשה. לדוגמה: 'תמצת את המידע הבא מהטקסט...' או 'סווג את המשוב הזה לפי הסכימה שצוינה...'.
- **אימות:** למרות שהפלט המובנה מבטיח קובץ JSON עם תחביר תקין, הוא לא מבטיח שהערכים יהיו נכונים מבחינה סמנטית. תמיד צריך לאמת את הפלט הסופי בקוד האפליקציה לפני שמשתמשים בו.
- **טיפול בשגיאות:** כדאי להטמיע טיפול בשגיאות באפליקציה כדי לנהל בצורה תקינה מקרים שבהם הפלט של המודל תואם לסכימה, אבל לא עומד בדרישות של הלוגיקה העסקית.

## מגבלות

- **קבוצת משנה של סכימה:** לא כל התכונות של מפרט סכימת ה-JSON נתמכות. המודל מתעלם ממאפיינים שלא נתמכים.
- **מורכבות הסכימה:** יכול להיות שממשק ה-API ידחה סכימות גדולות מאוד או סכימות עם קינון עמוק. אם נתקלים בשגיאות, כדאי לפשט את הסכימה על ידי קיצור שמות המאפיינים, צמצום הקינון או הגבלת מספר האילוצים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-13 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-13 (שעון UTC)."],[],[]]
