---
source_url: https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=tr
fetched_at: 2026-05-25T05:25:44.167607+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yapılandırılmış çıkışlar

Gemini modellerini, sağlanan bir JSON şemasına uygun yanıtlar oluşturacak şekilde yapılandırabilirsiniz. Bu sayede tahmin edilebilir ve tür açısından güvenli sonuçlar elde edilir. Ayrıca, yapılandırılmamış metinlerden yapılandırılmış verilerin ayıklanması kolaylaşır.

Yapılandırılmış çıkışlar şu durumlarda idealdir:

- **Veri ayıklama:** Metinden adlar ve tarihler gibi belirli bilgileri alın.
- **Yapılandırılmış sınıflandırma:** Metni önceden tanımlanmış kategorilere göre sınıflandırın.
- **Ajan tabanlı iş akışları:** Araçlar veya API'ler için yapılandırılmış girişler oluşturun.

Google GenAI SDK'ları, REST API'de JSON şemasını desteklemenin yanı sıra [Pydantic](https://docs.pydantic.dev/latest/) (Python) ve [Zod](https://zod.dev/) (JavaScript) kullanılarak şemaların tanımlanmasına da olanak tanır.

Yemek Tarifi Çıkarıcı
İçerik Denetleme
Özyinelemeli Yapılar

Bu örnekte, `object`, `array`, `string` ve `integer` gibi temel JSON şema türlerini kullanarak metinden yapılandırılmış verilerin nasıl ayıklanacağı gösterilmektedir.

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
    -H "Api-Revision: 2026-05-20" \
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

**Örnek Yanıt:**

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

## Yayın sonuçları

Yapılandırılmış çıkışları yayınlayarak yanıt oluşturulurken işlemeye başlamanıza olanak tanır. Yayınlanan parçalar, son JSON nesnesini oluşturmak için birleştirilebilen geçerli kısmi JSON dizeleridir.

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

## Araçlarla yapılandırılmış çıkışlar

Gemini 3, Yapılandırılmış Çıkışları [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=tr), [URL Bağlamı](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=tr), [Kod Yürütme](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=tr), [Dosya Arama](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=tr#structured-output) ve [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=tr) gibi yerleşik araçlarla birleştirmenize olanak tanır.

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

## JSON şeması desteği

JSON nesnesi oluşturmak için `response_format` öğesini `text` türünde bir nesneyle (veya nesne içeren bir diziyle) yapılandırın ve `mime_type` özelliğini `application/json` olarak ayarlayın. Şema, `schema` alanında sağlanmalıdır.

Gemini'ın yapılandırılmış çıkış modu, [JSON şeması](https://json-schema.org/) spesifikasyonunun bir alt kümesini destekler.

`type` için aşağıdaki değerler desteklenir:

- **`string`**: Metin için.
- **`number`**: Kayan noktalı sayılar için.
- **`integer`**: Tam sayılar için.
- **`boolean`**: Doğru veya yanlış değerler için.
- **`object`**: Anahtar/değer çiftleri içeren yapılandırılmış veriler için.
- **`array`**: Öğe listeleri için.
- **`null`**: Bir özelliğin null olmasına izin vermek için tür dizisine `"null"` değerini ekleyin (ör. `{"type": ["string", "null"]}`).

Bu açıklayıcı özellikler, modele yol göstermeye yardımcı olur:

- **`title`**: Bir mülkün kısa açıklaması.
- **`description`**: Bir mülkün daha uzun ve ayrıntılı açıklaması.

### Türe özel özellikler

**`object` değerleri için:**

- **`properties`**: Her anahtarın bir özellik adı, her değerin ise söz konusu özelliğin şeması olduğu bir nesne.
- **`required`**: Hangi özelliklerin zorunlu olduğunu listeleyen bir dizeler dizisi.
- **`additionalProperties`**: `properties` içinde listelenmeyen özelliklere izin verilip verilmeyeceğini kontrol eder. Boole veya şema olabilir.

**`string` değerleri için:**

- **`enum`**: Sınıflandırma görevleri için olası dizelerin belirli bir kümesini listeler.
- **`format`**: Dize için `date-time`, `date`, `time` gibi bir söz dizimi belirtir.

**`number` ve `integer` değerleri için:**

- **`enum`**: Olası sayısal değerlerin belirli bir kümesini listeler.
- **`minimum`**: Minimum dahil edilen değer.
- **`maximum`**: Maksimum dahil değer.

**`array` değerleri için:**

- **`items`**: Dizideki tüm öğelerin şemasını tanımlar.
- **`prefixItems`**: İlk N öğe için bir şema listesi tanımlar ve demet benzeri yapılara izin verir.
- **`minItems`**: Dizideki minimum öğe sayısı.
- **`maxItems`**: Dizideki maksimum öğe sayısı.

## Yapılandırılmış çıkışlar ve işlev çağrısı

| Özellik | Birincil Kullanım Alanı |
| --- | --- |
| **Yapılandırılmış Çıkışlar** | **Son yanıtı biçimlendirme** Modelin *yanıtını* belirli bir biçimde almak istediğinizde kullanın. |
| **İşlev Çağırma** | **Sohbet sırasında işlem yapma** Modelin nihai yanıtı vermeden önce bir görevi *yapmanızı istemesi* gerektiğinde kullanılır. |

## En iyi uygulamalar

- **Net açıklamalar:** Modeli yönlendirmek için `description` alanını kullanın.
- **Güçlü tür:** Belirli türleri (`integer`, `string`, `enum`) kullanın.
- **İstem mühendisliği:** Modelin ne yapmasını istediğinizi açıkça belirtin.
- **Doğrulama:** Çıkış söz dizimi açısından doğru JSON olsa da uygulamanızdaki değerleri her zaman doğrulayın.
- **Hata yönetimi:** Şemaya uygun ancak semantik olarak yanlış çıktılar için etkili hata yönetimi uygulayın.

## Sınırlamalar

- **Şema alt kümesi:** Tüm JSON şema özellikleri desteklenmez.
- **Şema karmaşıklığı:** Çok büyük veya derin iç içe yerleştirilmiş şemalar reddedilebilir.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
