---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=he
fetched_at: 2026-09-28T06:28:24.055501+00:00
title: "\u05e4\u05dc\u05d8\u05d9\u05dd \u05de\u05d5\u05d1\u05b0\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# פלטים מובְנים

אתם יכולים להגדיר את מודלי Gemini כך שיפיקו תשובות לפי סכימת JSON שסיפקתם. כך אפשר להבטיח תוצאות צפויות ובטוחות מבחינת סוג הנתונים, ולפשט את תהליך החילוץ של נתונים מובנים מטקסט לא מובנה.

שימוש בפלט מובנה מתאים במיוחד למקרים הבאים:

- **חילוץ נתונים:** חילוץ מידע ספציפי כמו שמות ותאריכים מטקסט.
- **סיווג מובנה:** סיווג טקסט לקטגוריות מוגדרות מראש.
- **תהליכי עבודה מבוססי-סוכן:** יצירת קלט מובנה לכלים או לממשקי API.

בנוסף לתמיכה בסכימת JSON ב-API בארכיטקטורת REST, ערכות ה-SDK של Google GenAI מאפשרות להגדיר סכימות באמצעות [Pydantic](https://docs.pydantic.dev/latest/) (Python) ו-[Zod](https://zod.dev/) (JavaScript).

## דוגמאות לפלט מובנה

### חילוץ מתכונים

בדוגמה הזו מוסבר איך לחלץ נתונים מובְנים מטקסט באמצעות סוגים בסיסיים של סכימת JSON, כמו `object`, `array`, `string` ו-`integer`.

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

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> ingredientProps = new HashMap<>();
Map<String, Object> nameProp = new HashMap<>();
nameProp.put("type", "string");
nameProp.put("description", "Name of the ingredient.");
ingredientProps.put("name", nameProp);

Map<String, Object> quantityProp = new HashMap<>();
quantityProp.put("type", "string");
quantityProp.put("description", "Quantity of the ingredient, including units.");
ingredientProps.put("quantity", quantityProp);

Map<String, Object> ingredientItemSchema = new HashMap<>();
ingredientItemSchema.put("type", "object");
ingredientItemSchema.put("properties", ingredientProps);
ingredientItemSchema.put("required", Arrays.asList("name", "quantity"));

Map<String, Object> properties = new HashMap<>();

Map<String, Object> recipeNameProp = new HashMap<>();
recipeNameProp.put("type", "string");
recipeNameProp.put("description", "The name of the recipe.");
properties.put("recipe_name", recipeNameProp);

Map<String, Object> prepTimeProp = new HashMap<>();
prepTimeProp.put("type", "integer");
prepTimeProp.put("description", "Optional time in minutes to prepare the recipe.");
properties.put("prep_time_minutes", prepTimeProp);

Map<String, Object> ingredientsProp = new HashMap<>();
ingredientsProp.put("type", "array");
ingredientsProp.put("items", ingredientItemSchema);
properties.put("ingredients", ingredientsProp);

Map<String, Object> instructionsProp = new HashMap<>();
instructionsProp.put("type", "array");
Map<String, Object> stringItem = new HashMap<>();
stringItem.put("type", "string");
instructionsProp.put("items", stringItem);
properties.put("instructions", instructionsProp);

Map<String, Object> recipeJsonSchema = new HashMap<>();
recipeJsonSchema.put("type", "object");
recipeJsonSchema.put("properties", properties);
recipeJsonSchema.put("required", Arrays.asList("recipe_name", "ingredients", "instructions"));

String prompt =
    "Please extract the recipe from the following text.\n"
        + "The user wants to make delicious chocolate chip cookies.\n"
        + "They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n"
        + "1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n"
        + "3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\n"
        + "For the best part, they'll need 2 cups of semisweet chocolate chips.\n"
        + "First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\n"
        + "baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\n"
        + "until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\n"
        + "ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\n"
        + "onto ungreased baking sheets and bake for 9 to 11 minutes.";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(recipeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    recipeJsonSchema := map[string]any{
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
                "type": "array",
                "items": map[string]any{
                    "type": "string",
                },
            },
        },
        "required": []string{"recipe_name", "ingredients", "instructions"},
    }

    prompt := `Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.`

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   recipeJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

### ניהול תוכן

בדוגמה הזו מוצגות התכונות `anyOf` לסכימות מותנות ו-`enum` לסיווג, שמאפשרות לשנות את מבנה הפלט בהתאם לתוכן.

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

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": ModerationResult.model_json_schema()
    },
)

result = ModerationResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const moderationResultJsonSchema = {
  type: "object",
  properties: {
    decision: {
      anyOf: [
        {
          type: "object",
          title: "SpamDetails",
          description: "Details for content classified as spam.",
          properties: {
            reason: { type: "string", description: "The reason why the content is considered spam." },
            spam_type: { type: "string", enum: ["phishing", "scam", "unsolicited promotion", "other"], description: "The type of spam." }
          },
          required: ["reason", "spam_type"]
        },
        {
          type: "object",
          title: "NotSpamDetails",
          description: "Details for content classified as not spam.",
          properties: {
            summary: { type: "string", description: "A brief summary of the content." },
            is_safe: { type: "boolean", description: "Whether the content is safe for all audiences." }
          },
          required: ["summary", "is_safe"]
        }
      ]
    }
  },
  required: ["decision"]
};

const moderationResultSchema = z.fromJSONSchema(moderationResultJsonSchema);

const client = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: moderationResultJsonSchema
  },
});

const result = moderationResultSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> spamProps = new HashMap<>();
Map<String, Object> reasonProp = new HashMap<>();
reasonProp.put("type", "string");
reasonProp.put("description", "The reason why the content is considered spam.");
spamProps.put("reason", reasonProp);

Map<String, Object> spamTypeProp = new HashMap<>();
spamTypeProp.put("type", "string");
spamTypeProp.put("enum", Arrays.asList("phishing", "scam", "unsolicited promotion", "other"));
spamTypeProp.put("description", "The type of spam.");
spamProps.put("spam_type", spamTypeProp);

Map<String, Object> spamDetailsSchema = new HashMap<>();
spamDetailsSchema.put("type", "object");
spamDetailsSchema.put("title", "SpamDetails");
spamDetailsSchema.put("properties", spamProps);
spamDetailsSchema.put("required", Arrays.asList("reason", "spam_type"));

Map<String, Object> notSpamProps = new HashMap<>();
Map<String, Object> summaryProp = new HashMap<>();
summaryProp.put("type", "string");
summaryProp.put("description", "A brief summary of the content.");
notSpamProps.put("summary", summaryProp);

Map<String, Object> isSafeProp = new HashMap<>();
isSafeProp.put("type", "boolean");
isSafeProp.put("description", "Whether the content is safe for all audiences.");
notSpamProps.put("is_safe", isSafeProp);

Map<String, Object> notSpamDetailsSchema = new HashMap<>();
notSpamDetailsSchema.put("type", "object");
notSpamDetailsSchema.put("title", "NotSpamDetails");
notSpamDetailsSchema.put("properties", notSpamProps);
notSpamDetailsSchema.put("required", Arrays.asList("summary", "is_safe"));

Map<String, Object> decisionProp = new HashMap<>();
decisionProp.put("anyOf", Arrays.asList(spamDetailsSchema, notSpamDetailsSchema));

Map<String, Object> properties = new HashMap<>();
properties.put("decision", decisionProp);

Map<String, Object> moderationResultJsonSchema = new HashMap<>();
moderationResultJsonSchema.put("type", "object");
moderationResultJsonSchema.put("properties", properties);
moderationResultJsonSchema.put("required", Arrays.asList("decision"));

String prompt =
    "Please moderate the following content and provide a decision.\n"
        + "Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(moderationResultJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    spamDetailsSchema := map[string]any{
        "type":  "object",
        "title": "SpamDetails",
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
    }

    notSpamDetailsSchema := map[string]any{
        "type":  "object",
        "title": "NotSpamDetails",
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
    }

    moderationResultJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "decision": map[string]any{
                "anyOf": []any{spamDetailsSchema, notSpamDetailsSchema},
            },
        },
        "required": []string{"decision"},
    }

    prompt := "Please moderate the following content and provide a decision.\n" +
        "Content: 'Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'"

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   moderationResultJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Please moderate the following content and provide a decision.\nContent: '\''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'\''",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
    }'
```

**דוגמה לתשובה:**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### מבנים רקורסיביים

בדוגמה הזו אפשר לראות איך מגדירים סכימה רקורסיבית כמו תרשים ארגוני.

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

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Employee.model_json_schema()
    },
)

employee = Employee.model_validate_json(interaction.output_text)
print(employee)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const employeeJsonSchema = {
  type: "object",
  properties: {
    name: { type: "string" },
    employee_id: { type: "integer" },
    reports: {
      type: "array",
      description: "A list of employees reporting to this employee.",
      items: {
        "$ref": "#"
      }
    }
  },
  required: ["name", "employee_id", "reports"]
};

const employeeSchema = z.fromJSONSchema(employeeJsonSchema);

const client = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: employeeJsonSchema
  },
});

const employee = employeeSchema.parse(JSON.parse(interaction.output_text));
console.log(employee);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> nameProp = new HashMap<>();
nameProp.put("type", "string");
properties.put("name", nameProp);

Map<String, Object> idProp = new HashMap<>();
idProp.put("type", "integer");
properties.put("employee_id", idProp);

Map<String, Object> reportsProp = new HashMap<>();
reportsProp.put("type", "array");
reportsProp.put("description", "A list of employees reporting to this employee.");
reportsProp.put("items", Collections.singletonMap("$ref", "#"));
properties.put("reports", reportsProp);

Map<String, Object> employeeJsonSchema = new HashMap<>();
employeeJsonSchema.put("type", "object");
employeeJsonSchema.put("properties", properties);
employeeJsonSchema.put("required", Arrays.asList("name", "employee_id", "reports"));

String prompt =
    "Generate an organization chart for a small team.\n"
        + "The manager is Alice, who manages Bob and Charlie. Bob manages David.";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(employeeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    employeeJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "name": map[string]any{
                "type": "string",
            },
            "employee_id": map[string]any{
                "type": "integer",
            },
            "reports": map[string]any{
                "type":        "array",
                "description": "A list of employees reporting to this employee.",
                "items": map[string]any{
                    "$ref": "#",
                },
            },
        },
        "required": []string{"name", "employee_id", "reports"},
    }

    prompt := "Generate an organization chart for a small team.\n" +
        "The manager is Alice, who manages Bob and Charlie. Bob manages David."

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   employeeJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David.",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
    }'
```

**דוגמה לתשובה:**

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

## תוצאות סטרימינג

אפשר להזרים פלט מובנה, וכך להתחיל לעבד את התשובה בזמן שהיא נוצרת. החלקים שמועברים בסטרימינג הם מחרוזות JSON חלקיות תקינות שאפשר לשרשר כדי ליצור את אובייקט ה-JSON הסופי.

### Python

```
from google import genai
from pydantic import BaseModel
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Feedback.model_json_schema()
    },
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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
  model: "gemini-3.8-flash",
  input: "The new UI is incredibly intuitive. Add a very long summary!",
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: feedbackJsonSchema
  },
  stream: true,
});

for await (const event of stream) {
  if (event.event_type === "step.delta") {
    if (event.delta.type === "text") {
      process.stdout.write(event.delta.text);
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> sentimentProp = new HashMap<>();
sentimentProp.put("type", "string");
sentimentProp.put("enum", Arrays.asList("positive", "neutral", "negative"));
properties.put("sentiment", sentimentProp);

Map<String, Object> summaryProp = new HashMap<>();
summaryProp.put("type", "string");
properties.put("summary", summaryProp);

Map<String, Object> feedbackJsonSchema = new HashMap<>();
feedbackJsonSchema.put("type", "object");
feedbackJsonSchema.put("properties", properties);
feedbackJsonSchema.put("required", Arrays.asList("sentiment", "summary"));

String prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(feedbackJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> events = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : events) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta) {
      StepDeltaData data = ((StepDelta) event).delta().orElse(null);
      if (data instanceof TextDelta) {
        ((TextDelta) data).text().ifPresent(System.out::print);
      }
    }
  }
}
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

    feedbackJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "sentiment": map[string]any{
                "type": "string",
                "enum": []string{"positive", "neutral", "negative"},
            },
            "summary": map[string]any{
                "type": "string",
            },
        },
        "required": []string{"sentiment", "summary"},
    }

    prompt := "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   feedbackJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
                Stream:         genai.Ptr(true),
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    defer resp.InteractionSSEStreamEvent.Close()

    for resp.InteractionSSEStreamEvent.Next() {
        event := resp.InteractionSSEStreamEvent.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
}
```

### REST

```
curl -N -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "The new UI is incredibly intuitive. Add a very long summary!",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
          "type": "object",
          "properties": {
            "sentiment": { "type": "string", "enum": ["positive", "neutral", "negative"] },
            "summary": { "type": "string" }
          },
          "required": ["sentiment", "summary"]
        }
      },
      "stream": true
    }'
```

## פלט מובנה באמצעות כלים

‫Gemini 3 מאפשר לכם לשלב פלט מובנה עם כלים מובנים, כולל [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he),‏ [URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=he),‏ [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he),‏ [File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=he#structured-output) ו-[קריאה להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

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

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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

const match = matchSchema.parse(JSON.parse(interaction.output_text));
console.log(match);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> winnerProp = new HashMap<>();
winnerProp.put("type", "string");
winnerProp.put("description", "The name of the winner.");
properties.put("winner", winnerProp);

Map<String, Object> scoreProp = new HashMap<>();
scoreProp.put("type", "string");
scoreProp.put("description", "The final match score.");
properties.put("final_match_score", scoreProp);

Map<String, Object> scorersProp = new HashMap<>();
scorersProp.put("type", "array");
scorersProp.put("description", "The name of the scorer.");
scorersProp.put("items", Collections.singletonMap("type", "string"));
properties.put("scorers", scorersProp);

Map<String, Object> matchJsonSchema = new HashMap<>();
matchJsonSchema.put("type", "object");
matchJsonSchema.put("properties", properties);
matchJsonSchema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(matchJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    matchJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "description": "The name of the scorer.",
                "items": map[string]any{
                    "type": "string",
                },
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   matchJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.1-pro-preview"),
                Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                    interactions.NewTool(interactions.URLContext{}),
                },
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
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

הערכים הבאים של `type` נתמכים:

- ‫**`string`**: לטקסט.
- ‫**`number`**: למספרים בשיטת נקודה צפה.
- ‫**`integer`**: למספרים שלמים.
- ‫**`boolean`**: לערכים true או false.
- ‫**`object`**: לנתונים מובְנים עם צמדי מפתח/ערך.
- ‫**`array`**: לרשימות של פריטים.
- ‫**`null`**: כדי לאפשר שמאפיין יהיה null, צריך לכלול את `"null"` במערך הסוגים (לדוגמה, `{"type": ["string", "null"]}`).

מאפייני התיאור האלה עוזרים להנחות את המודל:

- ‫**`title`**: תיאור קצר של מאפיין.
- **`description`**: תיאור ארוך ומפורט יותר של נכס.

### מאפיינים שספציפיים לסוג

**לערכים של `object`:**

- ‫**`properties`**: אובייקט שבו כל מפתח הוא שם מאפיין וכל ערך הוא סכימה של המאפיין הזה.
- ‫**`required`**: מערך של מחרוזות, שבו מפורטות התכונות שהן חובה.
- ‫**`additionalProperties`**: קובע אם מותר להשתמש בנכסים שלא מופיעים ב-`properties`. יכול להיות ערך בוליאני או סכמה.

**לערכים של `string`:**

- ‫**`enum`**: רשימה של קבוצה ספציפית של מחרוזות אפשריות למשימות סיווג.
- ‫**`format`**: מציין תחביר למחרוזת, כמו `date-time`, ‏ `date`, ‏ `time`.

**לערכים `number` ו-`integer`:**

- ‫**`enum`**: רשימה של קבוצה ספציפית של ערכים מספריים אפשריים.
- ‫**`minimum`**: ערך המינימום כולל.
- ‫**`maximum`**: הערך המקסימלי כולל.

**לערכים של `array`:**

- ‫**`items`**: מגדיר את הסכימה של כל הפריטים במערך.
- ‫**`prefixItems`**: מגדיר רשימה של סכימות עבור הפריטים הראשונים, ומאפשר מבנים דמויי-tuple.
- ‫**`minItems`**: המספר המינימלי של פריטים במערך.
- ‫**`maxItems`**: המספר המקסימלי של פריטים במערך.

## פלט מובנה לעומת קריאה להפעלת פונקציות

| תכונה | תרחיש ראשי לדוגמה |
| --- | --- |
| **תשובות מובנות** | **עיצוב התשובה הסופית.** משתמשים בה כשרוצים ש*התשובה* של המודל תהיה בפורמט מסוים. |
| **בקשה להפעלת פונקציה** | **ביצוע פעולות במהלך שיחה** משתמשים בה כשצריך שהמודל *ישאל אתכם* לבצע משימה לפני שהוא מספק תשובה סופית. |

## שיטות מומלצות

- **תיאורים ברורים:** השתמשו בשדה `description` כדי להנחות את המודל.
- **הקלדה חזקה:** שימוש בסוגים ספציפיים (`integer`, ‏`string`, ‏`enum`).
- **הנדסת פרומפטים:** חשוב לציין בבירור מה רוצים שהמודל יעשה.
- **אימות:** למרות שהפלט הוא JSON עם תחביר תקין, תמיד צריך לאמת את הערכים באפליקציה.
- **טיפול בשגיאות:** הטמיעו טיפול בשגיאות כדי לטפל בפלט שעומד בדרישות הסכימה אבל לא נכון מבחינה סמנטית.

## מגבלות

- **קבוצת משנה של סכימה:** לא כל התכונות של סכימת JSON נתמכות.
- **מורכבות הסכימה:** יכול להיות שסכימות גדולות מאוד או כאלה עם קינון עמוק יידחו.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-24 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-24 (שעון UTC)."],[],[]]
