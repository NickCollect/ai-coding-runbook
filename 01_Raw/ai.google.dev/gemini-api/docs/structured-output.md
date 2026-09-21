---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=ko
fetched_at: 2026-09-21T05:48:54.746768+00:00
title: "\uad6c\uc870\ud654\ub41c \ucd9c\ub825 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 구조화된 출력

제공된 JSON 스키마를 준수하는 응답을 생성하도록 Gemini 모델을 구성할 수 있습니다. 이렇게 하면 예측 가능하고 유형이 안전한 결과를 얻을 수 있으며 구조화되지 않은 텍스트에서 구조화된 데이터를 추출하는 작업이 간소화됩니다.

구조화된 출력은 다음 작업에 적합합니다.

- **데이터 추출:** 텍스트에서 이름, 날짜와 같은 특정 정보를 가져옵니다.
- **구조화된 분류:** 텍스트를 사전 정의된 카테고리로 분류합니다.
- **에이전트 워크플로:** 도구 또는 API의 구조화된 입력을 생성합니다.

REST API에서 JSON 스키마를 지원하는 것 외에도 Google GenAI SDK를 사용하면
다음과 같이 스키마를 정의할 수 있습니다.
[Pydantic](https://docs.pydantic.dev/latest/) (Python) 및
[Zod](https://zod.dev/) (JavaScript).

## 구조화된 출력 예

### 레시피 추출기

이 예에서는 `object`, `array`, `string`, `integer`와 같은 기본 JSON 스키마 유형을 사용하여 텍스트에서 구조화된 데이터를 추출하는 방법을 보여줍니다.

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

### 자바

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

**응답 예:**

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

### 콘텐츠 검토

이 예에서는 조건부 스키마의 `anyOf`와 분류의 `enum`을 보여주며, 이를 통해 콘텐츠에 따라 출력 구조를 다르게 지정할 수 있습니다.

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

### 자바

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

**응답 예:**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### 재귀 구조

이 예에서는 조직도와 같은 재귀 스키마를 정의하는 방법을 보여줍니다.

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

### 자바

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

**응답 예:**

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

## 스트리밍 결과

구조화된 출력을 스트리밍하여 응답이 생성되는 즉시 처리를 시작할 수 있습니다. 스트리밍된 청크는 최종 JSON 객체를 형성하기 위해 연결할 수 있는 유효한 부분 JSON 문자열입니다.

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

### 자바

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

## 도구를 사용한 구조화된 출력

Gemini 3를 사용하면 Google 검색을 사용한 그라운딩
, URL 컨텍스트
, 코드 실행
, 파일 검색
, 함수 호출
을 비롯한 기본 제공 도구와 구조화된 출력을 결합할 수 있습니다.

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

### 자바

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

## JSON 스키마 지원

JSON 객체를 생성하려면 `text` 유형의 객체 (또는 객체를 포함하는 배열)로 `response_format`을 구성하고 `mime_type`을 `application/json`으로 설정합니다. 스키마는 `schema` 필드에 제공되어야 합니다.

Gemini의 구조화된 출력 모드는
[JSON 스키마](https://json-schema.org/) 사양의 하위 집합을 지원합니다.

다음 `type` 값이 지원됩니다.

- **`string`**: 텍스트용
- **`number`**: 부동 소수점 수용
- **`integer`**: 정수용
- **`boolean`**: true 또는 false 값용
- **`object`**: 키-값 쌍이 있는 구조화된 데이터용
- **`array`**: 항목 목록용
- **`null`**: 속성이 null이 되도록 허용하려면 유형 배열에 `"null"`을 포함합니다 (예: `{"type": ["string", "null"]}`).

이러한 설명 속성은 모델을 안내하는 데 도움이 됩니다.

- **`title`**: 속성에 대한 간단한 설명입니다.
- **`description`**: 속성에 대한 더 길고 자세한 설명입니다.

### 유형별 속성

**`object` 값의 경우:**

- **`properties`**: 각 키가 속성 이름이고 각 값이 해당 속성의 스키마인 객체입니다.
- **`required`**: 필수 속성을 나열하는 문자열 배열입니다.
- **`additionalProperties`**: `properties`에 나열되지 않은 속성이 허용되는지 여부를 제어합니다. 불리언 또는 스키마일 수 있습니다.

**`string` 값의 경우:**

- **`enum`**: 분류 작업에 사용할 수 있는 특정 문자열 집합을 나열합니다.
- **`format`**: `date-time`, `date`, `time`과 같은 문자열의 구문을 지정합니다.

**`number` 및 `integer` 값의 경우:**

- **`enum`**: 가능한 숫자 값의 특정 집합을 나열합니다.
- **`minimum`**: 최소 포함 값입니다.
- **`maximum`**: 최대 포함 값입니다.

**`array` 값의 경우:**

- **`items`**: 배열의 모든 항목에 대한 스키마를 정의합니다.
- **`prefixItems`**: 첫 번째 N개 항목의 스키마 목록을 정의하여 튜플과 같은 구조를 허용합니다.
- **`minItems`**: 배열의 최소 항목 수입니다.
- **`maxItems`**: 배열의 최대 항목 수입니다.

## 구조화된 출력과 함수 호출 비교

| 기능 | 주된 사용 사례 |
| --- | --- |
| **구조화된 출력** | **최종 응답의 형식을 지정합니다.** 모델의 *답변* 을 특정 형식으로 지정하려는 경우에 사용합니다. |
| **함수 호출** | **대화 중에 작업을 실행합니다.** 모델이 최종 답변을 제공하기 전에 작업을 실행하도록 *요청* 해야 하는 경우에 사용합니다. |

## 권장사항

- **명확한 설명:** `description` 필드를 사용하여 모델을 안내합니다.
- **강력한 유형 지정:** 특정 유형 (`integer`, `string`, `enum`)을 사용합니다.
- **프롬프트 엔지니어링:** 모델이 수행해야 하는 작업을 명확하게 명시합니다.
- **유효성 검사:** 출력은 구문상 올바른 JSON이지만 항상 애플리케이션에서 값을 검증합니다.
- **오류 처리:** 스키마를 준수하지만 의미상 올바르지 않은 출력에 대해 강력한 오류 처리를 구현합니다.

## 제한사항

- **스키마 하위 집합:** 일부 JSON 스키마 기능은 지원되지 않습니다.
- **스키마 복잡성:** 매우 크거나 깊게 중첩된 스키마는 거부될 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-18(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-18(UTC)"],[],[]]
