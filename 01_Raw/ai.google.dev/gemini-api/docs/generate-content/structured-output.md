---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=tr
fetched_at: 2026-10-19T05:51:56.610751+00:00
title: "Yap\u0131land\u0131r\u0131lm\u0131\u015f \u00e7\u0131k\u0131\u015flar \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Yapılandırılmış çıkışlar

Gemini modellerini, sağlanan JSON şemasına uygun yanıtlar üretecek şekilde yapılandırabilirsiniz. Bu sayede, tahmin edilebilir ve tip güvenliği olan sonuçlar elde edilir ve yapılandırılmamış metinlerden yapılandırılmış verilerin ayıklanması kolaylaşır.

Yapılandırılmış çıkışlar aşağıdaki durumlarda idealdir:

- **Veri ayıklama:** Metinden ad ve tarih gibi belirli bilgileri ayıklayın.
- **Yapılandırılmış sınıflandırma:** Metni önceden tanımlanmış kategorilere göre sınıflandırın.
- **Temsilci tabanlı iş akışları:** Araçlar veya API'ler için yapılandırılmış girişler oluşturun.

Google GenAI SDK'ları, REST API'de JSON şemasını desteklemenin yanı sıra [Pydantic](https://docs.pydantic.dev/latest/) (Python) ve [Zod](https://zod.dev/) (JavaScript) kullanarak şema tanımlamayı kolaylaştırır.

## Yapılandırılmış çıkış örnekleri

### Yemek Tarifi Ayıklayıcı

Bu örnekte, `object`, `array`, `string` ve `integer` gibi temel JSON şeması türleri kullanılarak metinden yapılandırılmış verilerin nasıl çıkarılacağı gösterilmektedir.

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

### REST

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

**Örnek yanıt:**

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

### İçerik Denetimi

Bu örnekte, koşullu şemalar için `anyOf` ve sınıflandırma için `enum` kullanılarak çıkış yapısının içeriğe göre değişmesi sağlanır.

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

### REST

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

### Yinelemeli Yapılar

Bu örnekte, kuruluş şeması gibi özyinelemeli bir şemanın nasıl tanımlanacağı gösterilmektedir.

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

### REST

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

**Örnek yanıt:**

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

## Canlı Yayın

Yapılandırılmış çıktıları akış olarak alabilirsiniz. Bu sayede, tüm çıktının tamamlanmasını beklemeden yanıtı oluşturulurken işlemeye başlayabilirsiniz. Bu sayede uygulamanızın algılanan performansını artırabilirsiniz.

Akışla aktarılan parçalar, geçerli kısmi JSON dizeleri olur ve bunlar birleştirilerek nihai, eksiksiz JSON nesnesi oluşturulabilir.

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

## Araçlarla yapılandırılmış çıkışlar

Gemini 3, yapılandırılmış çıkışları yerleşik araçlarla birleştirmenize olanak tanır. Bu araçlar arasında şunlar bulunur:
[Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr),
[URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr),
[Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr),
[Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr#structured-output) ve
[İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr).

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

### REST

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

## JSON şeması desteği

JSON nesnesi oluşturmak için oluşturma yapılandırmasında `response_json_schema` (veya REST'te `responseFormat.text.schema`) değerini ayarlayın. Şema, istenen çıkış biçimini açıklayan geçerli bir [JSON şeması](https://json-schema.org/) olmalıdır.

Ardından model, sağlanan şemayla eşleşen ve söz dizimi açısından geçerli bir JSON dizesi olan bir yanıt oluşturur. Yapılandırılmış çıkışlar kullanıldığında model, şemadaki anahtarlarla aynı sırada çıkışlar üretir.

Gemini'ın yapılandırılmış çıkış modu, [JSON Şeması](https://json-schema.org) spesifikasyonunun bir alt kümesini destekler.

`type` için aşağıdaki değerler desteklenir:

- **`string`**: Metin için.
- **`number`**: Kayan noktalı sayılar için.
- **`integer`**: Tam sayılar için.
- **`boolean`**: Doğru/yanlış değerleri için.
- **`object`**: Anahtar/değer çiftleri içeren yapılandırılmış veriler için.
- **`array`**: Öğe listeleri için kullanılır.
- **`null`**: Bir özelliğin boş olmasına izin vermek için tür dizisine `"null"` değerini ekleyin (ör. `{"type": ["string", "null"]}`).

Bu açıklayıcı özellikler, modele yol gösterir:

- **`title`**: Bir mülkün kısa açıklaması.
- **`description`**: Bir mülkün daha uzun ve daha ayrıntılı açıklaması.

### Türe özel özellikler

**`object` değerleri için:**

- **`properties`**: Her anahtarın bir özellik adı ve her değerin bu özelliğin şeması olduğu bir nesne.
- **`required`**: Hangi özelliklerin zorunlu olduğunu listeleyen bir dize dizisi.
- **`additionalProperties`**: `properties` içinde listelenmeyen mülklere izin verilip verilmeyeceğini kontrol eder. Boole veya şema olabilir.

**`string` değerleri için:**

- **`enum`**: Sınıflandırma görevleri için olası dizelerin belirli bir grubunu listeler.
- **`format`**: Dize için `date-time`, `date`, `time` gibi bir söz dizimi belirtir.

**`number` ve `integer` değerleri için:**

- **`enum`**: Belirli bir olası sayısal değerler kümesini listeler.
- **`minimum`**: Minimum dahil edilen değer.
- **`maximum`**: Maksimum dahil edilen değer.

**`array` değerleri için:**

- **`items`**: Dizideki tüm öğelerin şemasını tanımlar.
- **`prefixItems`**: İlk N öğe için şema listesi tanımlayarak tuple benzeri yapılara olanak tanır.
- **`minItems`**: Dizideki minimum öğe sayısı.
- **`maxItems`**: Dizideki maksimum öğe sayısı.

## Model desteği

Aşağıdaki modeller yapılandırılmış çıkışı destekler:

| Model | Yapılandırılmış Çıkışlar |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* Gemini 2.0'ın, tercih edilen yapıyı tanımlamak için JSON girişinde açık bir `propertyOrdering` listesi gerektirdiğini unutmayın. Bu [yemek kitabında](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb) bir örnek bulabilirsiniz.*

## Yapılandırılmış çıkışlar ve işlev çağrısı

Hem yapılandırılmış çıkışlar hem de işlev çağrısı JSON şemalarını kullanır ancak farklı amaçlara hizmet eder:

| Özellik | Birincil Kullanım Alanı |
| --- | --- |
| **Yapılandırılmış çıkışlar** | **Kullanıcıya verilecek son yanıtı biçimlendirme** Modelin *yanıtının* belirli bir biçimde olmasını istediğinizde (ör. bir belgeden veri ayıklayıp veritabanına kaydetme) bu yöntemi kullanın. |
| **İşlev Çağırma** | **Görüşme sırasında harekete geçme** Modelin nihai bir yanıt verebilmesi için bir görevi yerine getirmenizi *istemesi* gerektiğinde (ör. "mevcut hava durumunu öğren") bu seçeneği kullanın. |

## En iyi uygulamalar

- **Net açıklamalar:** Modele her bir özelliğin neyi temsil ettiğiyle ilgili net talimatlar vermek için şemanızdaki `description` alanını kullanın. Bu, modelin çıkışını yönlendirmek için çok önemlidir.
- **Güçlü yazma:** Mümkün olduğunda belirli türleri (`integer`, `string`, `enum`) kullanın. Bir parametrenin sınırlı sayıda geçerli değeri varsa `enum` kullanın.
- **İstem mühendisliği:** İsteminizde modelin ne yapmasını istediğinizi açıkça belirtin. Örneğin, "Metinden aşağıdaki bilgileri çıkarın..." veya "Bu geri bildirimi sağlanan şemaya göre sınıflandırın...".
- **Doğrulama:** Yapılandırılmış çıkış, söz dizimi açısından doğru JSON'u garanti etse de değerlerin anlamsal olarak doğru olduğunu garanti etmez. Uygulama kodunuzdaki nihai çıkışı kullanmadan önce her zaman doğrulayın.
- **Hata işleme:** Modelin çıkışının şemaya uygun olsa da iş mantığı gereksinimlerinizi karşılamadığı durumları sorunsuz bir şekilde yönetmek için uygulamanızda güçlü hata işleme özellikleri uygulayın.

## Sınırlamalar

- **Şema alt kümesi:** JSON Şeması spesifikasyonunun tüm özellikleri desteklenmez. Model, desteklenmeyen özellikleri yoksayar.
- **Şema karmaşıklığı:** API, çok büyük veya derinlemesine iç içe yerleştirilmiş şemaları reddedebilir. Hatalarla karşılaşırsanız özellik adlarını kısaltarak, iç içe yerleştirmeyi azaltarak veya kısıtlama sayısını sınırlayarak şemanızı basitleştirmeyi deneyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-19 UTC."],[],[]]
