---
source_url: https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=he
fetched_at: 2026-05-18T05:11:01.355773+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פלטים מובנים

אתם יכולים להגדיר את מודלי Gemini כך שיפיקו תשובות בהתאם לסכימת JSON שסיפקתם. כך אפשר להבטיח תוצאות צפויות ובטוחות מבחינת סוג הנתונים, ולפשט את תהליך החילוץ של נתונים מובנים מטקסט לא מובנה.

שימוש בפלט מובנה מתאים במיוחד למקרים הבאים:

- **חילוץ נתונים:** חילוץ מידע ספציפי כמו שמות ותאריכים מטקסט.
- **סיווג מובנה:** סיווג טקסט לקטגוריות מוגדרות מראש.
- **תהליכי עבודה מבוססי-סוכן:** יצירת קלט מובנה לכלים או לממשקי API.

בנוסף לתמיכה בסכימת JSON ב-API בארכיטקטורת REST, ערכות ה-SDK של Google GenAI מאפשרות להגדיר סכימות באמצעות [Pydantic](https://docs.pydantic.dev/latest/) (Python) ו-[Zod](https://zod.dev/) (JavaScript).

Recipe Extractor
Content Moderation
Recursive Structures

בדוגמה הזו מוסבר איך לחלץ נתונים מוּבְנִים מטקסט באמצעות סוגים בסיסיים של סכימת JSON, כמו `object`, `array`, `string` ו-`integer`.

### Python

```
# This will only work for SDK newer than 2.0.0
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.steps[-1].content[0].text)
print(recipe)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: {
      type: "string",
      description: "The name of the recipe."
    },
    prep_time_minutes: {
        type: "integer",
        description: "Optional time in minutes to prepare the recipe."
    },
    ingredients: {
      type: "array",
      items: {
        type: "object",
        properties: {
          name: { type: "string", description: "Name of the ingredient."},
          quantity: { type: "string", description: "Quantity of the ingredient, including units."}
        },
        required: ["name", "quantity"]
      }
    },
    instructions: {
      type: "array",
      items: { type: "string" }
    }
  },
  required: ["recipe_name", "ingredients", "instructions"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const client = new GoogleGenAI({});

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

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(recipe);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes.",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
    }'
```

**דוגמה לתשובה:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    { "name": "all-purpose flour", "quantity": "2 and 1/4 cups" },
    { "name": "baking soda", "quantity": "1 teaspoon" },
    { "name": "salt", "quantity": "1 teaspoon" },
    { "name": "unsalted butter (softened)", "quantity": "1 cup" },
    { "name": "granulated sugar", "quantity": "3/4 cup" },
    { "name": "packed brown sugar", "quantity": "3/4 cup" },
    { "name": "vanilla extract", "quantity": "1 teaspoon" },
    { "name": "large eggs", "quantity": "2" },
    { "name": "semisweet chocolate chips", "quantity": "2 cups" }
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

## תוצאות סטרימינג

אפשר להזרים פלט מובנה, וכך להתחיל לעבד את התשובה בזמן שהיא נוצרת. החלקים שמועברים בסטרימינג הם מחרוזות JSON חלקיות תקינות שאפשר לשרשר כדי ליצור את אובייקט ה-JSON הסופי.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from pydantic import BaseModel
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Feedback.model_json_schema()
    },
    stream=True
)
for event in stream:
    if event.event_type == "step.delta" and event.delta.text:
        print(event.delta.text, end="")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const feedbackJsonSchema = {
  type: "object",
  properties: {
    sentiment: { type: "string", enum: ["positive", "neutral", "negative"] },
    summary: { type: "string" }
  },
  required: ["sentiment", "summary"]
};

const feedbackSchema = z.fromJSONSchema(feedbackJsonSchema);

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: "The new UI is incredibly intuitive. Add a very long summary!",
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: feedbackJsonSchema
  },
  stream: true,
});

for await (const event of stream) {
  if (event.type === "step.delta" && event.delta?.text) {
    process.stdout.write(event.delta.text);
  }
}
```

## פלט מובנה עם כלים

‫Gemini 3 מאפשר לכם לשלב פלט מובנה עם כלים מובנים, כולל [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he), [הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he), [הרצת קוד](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=he), [חיפוש קבצים](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=he#structured-output) ו[קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=he).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[{"type": "google_search"}, {"type": "url_context"}],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string" },
    final_match_score: { type: "string" },
    scorers: { type: "array", items: { type: "string" } }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.1-pro-preview",
  input: "Search for all details for the latest Euro.",
  tools: [{type: "google_search"}, {type: "url_context"}],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: matchJsonSchema
  },
});

const match = matchSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(match);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [{"type": "google_search"}, {"type": "url_context"}],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
            "winner": {"type": "string"},
            "final_match_score": {"type": "string"},
            "scorers": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["winner", "final_match_score", "scorers"]
      }
    }
  }'
```

## תמיכה בסכימת JSON

כדי ליצור אובייקט JSON, מגדירים את `response_format` עם אובייקט (או מערך שמכיל אובייקט) מהסוג `text` ומגדירים את `mime_type` שלו ל-`application/json`. צריך לספק את הסכימה בשדה `schema`.

מצב הפלט המובנה של Gemini תומך בחלק ממפרט [JSON Schema](https://json-schema.org/).

יש תמיכה בערכים הבאים של `type`:

- ‫**`string`**: לטקסט.
- ‫**`number`**: למספרים בשיטת נקודה צפה.
- ‫**`integer`**: למספרים שלמים.
- ‫**`boolean`**: לערכים True או False.
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

## פלט מובנה לעומת בקשה להפעלת פונקציה

| תכונה | תרחיש שימוש ראשי |
| --- | --- |
| **פלט מובנה** | **עיצוב התשובה הסופית.** משתמשים בה כשרוצים ש*התשובה* של המודל תהיה בפורמט מסוים. |
| **בקשה להפעלת פונקציה** | **ביצוע פעולות במהלך שיחה** משתמשים בה כשצריך שהמודל *יבקש מכם* לבצע משימה לפני שהוא מספק תשובה סופית. |

## שיטות מומלצות

- **תיאורים ברורים:** השתמשו בשדה `description` כדי להנחות את המודל.
- **הקלדה חזקה:** שימוש בסוגים ספציפיים (`integer`, ‏`string`, ‏`enum`).
- **הנדסת הנחיות:** חשוב להצהיר בבירור מה רוצים שהמודל יעשה.
- **אימות:** למרות שהפלט הוא JSON עם תחביר תקין, תמיד צריך לאמת את הערכים באפליקציה.
- **טיפול בשגיאות:** צריך להטמיע טיפול בשגיאות כדי לטפל בפלט שתואם לסכימה אבל לא נכון מבחינה סמנטית.

## מגבלות

- **קבוצת משנה של סכימה:** לא כל התכונות של סכימת JSON נתמכות.
- **מורכבות הסכימה:** יכול להיות שסכימות גדולות מאוד או כאלה עם קינון עמוק יידחו.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-12 (שעון UTC)."],[],[]]
