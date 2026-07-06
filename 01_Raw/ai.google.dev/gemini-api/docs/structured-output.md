---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=hi
fetched_at: 2026-07-06T05:20:55.220302+00:00
title: "\u0938\u094d\u091f\u094d\u0930\u0915\u094d\u091a\u0930\u094d\u0921 \u0906\u0909\u091f\u092a\u0941\u091f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# स्ट्रक्चर्ड आउटपुट

Gemini मॉडल को कॉन्फ़िगर करके, दिए गए JSON स्कीमा के मुताबिक जवाब जनरेट किए जा सकते हैं. इससे, टाइप-सेफ़ और अनुमान के मुताबिक नतीजे मिलते हैं. साथ ही, बिना स्ट्रक्चर वाले टेक्स्ट से स्ट्रक्चर्ड डेटा को आसानी से निकाला जा सकता है.

स्ट्रक्चर्ड आउटपुट का इस्तेमाल इन कामों के लिए किया जा सकता है:

- **डेटा निकालना:** टेक्स्ट से नाम और तारीख जैसी खास जानकारी निकालना.
- **स्ट्रक्चर्ड क्लासिफ़िकेशन:** टेक्स्ट को पहले से तय की गई कैटगरी में बांटना.
- **एजेंटिक वर्कफ़्लो:** टूल या एपीआई के लिए स्ट्रक्चर्ड इनपुट जनरेट करना.

REST API में JSON स्कीमा के साथ-साथ, Google GenAI SDK की मदद से
[Pydantic](https://docs.pydantic.dev/latest/) (Python) और
[Zod](https://zod.dev/) (JavaScript) का इस्तेमाल करके स्कीमा तय किए जा सकते हैं.

## स्ट्रक्चर्ड आउटपुट के उदाहरण

### रेसिपी निकालने वाला टूल

इस उदाहरण में, JSON स्कीमा के बुनियादी टाइप, जैसे कि `object`, `array`, `string`, और `integer` का इस्तेमाल करके, टेक्स्ट से स्ट्रक्चर्ड डेटा निकालने का तरीका बताया गया है.

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
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

**जवाब का उदाहरण:**

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

### कॉन्टेंट को मॉडरेट करना

इस उदाहरण में, शर्तों के हिसाब से स्कीमा के लिए `anyOf` और क्लासिफ़िकेशन के लिए `enum` का इस्तेमाल दिखाया गया है. इससे, कॉन्टेंट के आधार पर आउटपुट स्ट्रक्चर में बदलाव किया जा सकता है.

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
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

**जवाब का उदाहरण:**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### रिकर्सिव स्ट्रक्चर

इस उदाहरण में, संगठन चार्ट जैसे रिकर्सिव स्कीमा को तय करने का तरीका बताया गया है.

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
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

**जवाब का उदाहरण:**

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

## नतीजों को स्ट्रीम करना

स्ट्रक्चर्ड आउटपुट को स्ट्रीम किया जा सकता है. इससे, जवाब जनरेट होने के दौरान ही उसे प्रोसेस किया जा सकता है. स्ट्रीम किए गए चंक, JSON स्ट्रिंग के मान्य हिस्से होते हैं. इन्हें जोड़कर, फ़ाइनल JSON ऑब्जेक्ट बनाया जा सकता है.

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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

## टूल के साथ स्ट्रक्चर्ड आउटपुट

Gemini 3 की मदद से, स्ट्रक्चर्ड आउटपुट को इन-बिल्ट टूल के साथ जोड़ा जा सकता है. इनमें
[Google Search के साथ ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/google-search?hl=hi),
[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi),
[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi),
[फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/file-search?hl=hi#structured-output), और
[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) शामिल हैं.

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

## JSON स्कीमा के लिए सहायता

JSON ऑब्जेक्ट जनरेट करने के लिए, `response_format` को `text` टाइप के ऑब्जेक्ट (या ऑब्जेक्ट वाले कलेक्शन) के साथ कॉन्फ़िगर करें. साथ ही, इसका `mime_type` को `application/json` पर सेट करें. `schema` फ़ील्ड में स्कीमा की जानकारी देनी चाहिए.

Gemini का स्ट्रक्चर्ड आउटपुट मोड,
[JSON स्कीमा](https://json-schema.org/) की खास जानकारी के सबसेट के साथ काम करता है.

`type` की ये वैल्यू इस्तेमाल की जा सकती हैं:

- **`string`**: टेक्स्ट के लिए.
- **`number`**: फ़्लोटिंग-पॉइंट नंबर के लिए.
- **`integer`**: पूर्णांक के लिए.
- **`boolean`**: सही या गलत वैल्यू के लिए.
- **`object`**: कुंजी-वैल्यू पेयर वाले स्ट्रक्चर्ड डेटा के लिए.
- **`array`**: आइटम की सूचियों के लिए.
- **`null`**: किसी प्रॉपर्टी को नल के तौर पर सेट करने के लिए, टाइप कलेक्शन में `"null"` शामिल करें. उदाहरण के लिए, `{"type": ["string", "null"]}`.

जानकारी देने वाली इन प्रॉपर्टी से, मॉडल को गाइड करने में मदद मिलती है:

- **`title`**: किसी प्रॉपर्टी का छोटा ब्यौरा.
- **`description`**: किसी प्रॉपर्टी का लंबा और ज़्यादा जानकारी वाला ब्यौरा.

### टाइप के हिसाब से प्रॉपर्टी

**`object` वैल्यू के लिए:**

- **`properties`**: एक ऑब्जेक्ट, जिसमें हर कुंजी एक प्रॉपर्टी का नाम होती है और हर वैल्यू उस प्रॉपर्टी के लिए एक स्कीमा होती है.
- **`required`**: स्ट्रिंग का एक कलेक्शन, जिसमें यह बताया जाता है कि कौनसी प्रॉपर्टी ज़रूरी हैं.
- **`additionalProperties`**: इससे यह कंट्रोल किया जाता है कि `properties` में शामिल नहीं की गई प्रॉपर्टी इस्तेमाल की जा सकती हैं या नहीं. यह बूलियन या स्कीमा हो सकता है.

**`string` वैल्यू के लिए:**

- **`enum`**: क्लासिफ़िकेशन टास्क के लिए, संभावित स्ट्रिंग का एक खास सेट दिखाता है.
- **`format`**: स्ट्रिंग के लिए एक सिंटैक्स तय करता है. जैसे, `date-time`, `date`, `time`.

**`number` और `integer` वैल्यू के लिए:**

- **`enum`**: संभावित संख्या वाली वैल्यू का एक खास सेट दिखाता है.
- **`minimum`**: शामिल की जा सकने वाली कम से कम वैल्यू.
- **`maximum`**: शामिल की जा सकने वाली ज़्यादा से ज़्यादा वैल्यू.

**`array` वैल्यू के लिए:**

- **`items`**: कलेक्शन में मौजूद सभी आइटम के लिए स्कीमा तय करता है.
- **`prefixItems`**: पहले N आइटम के लिए स्कीमा की एक सूची तय करता है. इससे, टपल जैसे स्ट्रक्चर बनाए जा सकते हैं.
- **`minItems`**: कलेक्शन में मौजूद आइटम की कम से कम संख्या.
- **`maxItems`**: कलेक्शन में मौजूद आइटम की ज़्यादा से ज़्यादा संख्या.

## स्ट्रक्चर्ड आउटपुट बनाम फ़ंक्शन कॉलिंग

| सुविधा | इस्तेमाल का मुख्य उदाहरण |
| --- | --- |
| **स्ट्रक्चर्ड आउटपुट** | **फ़ाइनल जवाब को फ़ॉर्मैट करना.** इसका इस्तेमाल तब करें, जब आपको मॉडल का *जवाब* किसी खास फ़ॉर्मैट में चाहिए. |
| **फ़ंक्शन कॉलिंग** | **बातचीत के दौरान कार्रवाई करना.** इसका इस्तेमाल तब करें, जब मॉडल को फ़ाइनल जवाब देने से पहले, आपसे कोई टास्क *पूछना* हो. |

## सबसे सही तरीके

- **साफ़ तौर पर जानकारी देना:** मॉडल को गाइड करने के लिए, `description` फ़ील्ड का इस्तेमाल करें.
- **टाइपिंग:** खास टाइप (`integer`, `string`, `enum`) का इस्तेमाल करें.
- **प्रॉम्प्ट इंजीनियरिंग:** साफ़ तौर पर बताएं कि आपको मॉडल से क्या काम कराना है.
- **पुष्टि करना:** भले ही, आउटपुट सिंटैक्टिक तौर पर सही JSON हो, लेकिन हमेशा अपने ऐप्लिकेशन में वैल्यू की पुष्टि करें.
- **गड़बड़ी को ठीक करना:** स्कीमा के मुताबिक, लेकिन सिमैंटिक तौर पर गलत आउटपुट के लिए, गड़बड़ी को ठीक करने की मज़बूत सुविधा लागू करें.

## सीमाएं

- **स्कीमा का सबसेट:** JSON स्कीमा की सभी सुविधाएं उपलब्ध नहीं हैं.
- **स्कीमा की जटिलता:** बहुत बड़े या डीपली नेस्ट किए गए स्कीमा अस्वीकार किए जा सकते हैं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
