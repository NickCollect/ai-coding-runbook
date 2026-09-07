---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=tr
fetched_at: 2026-09-07T05:48:03.079018+00:00
title: "Interactions API'ye ge\u00e7i\u015f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Interactions API'ye geçiş

Bu kılavuz, `generateContent` API'den Interactions API'ye geçiş yapmanıza yardımcı olur.

Etkileşimler API'si, Gemini modelleri ve aracılarıyla uygulama geliştirmenin en basit ve en iyi yoludur. `generateContent` tam olarak desteklenmeye devam etse de tüm yeni geliştirmeler için Interactions API'sini kullanmanızı öneririz.

### Neden taşıma işlemi yapmalısınız?

Etkileşimler API'si, Gemini modelleri ve aracılarıyla geliştirme yapmanın en basit ve en iyi yoludur:

- **Sunucu tarafı geçmiş yönetimi**: `previous_interaction_id` aracılığıyla basitleştirilmiş çok aşamalı etkileşim akışları. Sunucu, durumu varsayılan olarak etkinleştirir (`store=true`), ancak `store=false`'yi ayarlayarak durumsuz davranışı etkinleştirebilirsiniz.
- **Gözlemlenebilir yürütme adımları**: Yazılan adımlar, karmaşık akışlarda hata ayıklamayı ve ara etkinlikler (ör. düşünceler veya arama widget'ları) için kullanıcı arayüzü oluşturmayı kolaylaştırır.
- **Araç kullanımı ve asenkron iş akışları**: Çok adımlı araç kullanımı, düzenleme ve karmaşık akıl yürütme akışları için yazılı yürütme adımları aracılığıyla yerel destek.
- **Uzun süren ve arka plan görevleri**: `background=true` kullanarak Deep Think ve Deep Research gibi zaman alan işlemlerin arka plan süreçlerine aktarılmasını destekler.

## Temel giriş/çıkış

Bu bölümde, basit bir metin oluşturma isteğinin nasıl taşınacağı gösterilmektedir.

### Önce (`generateContent`)

`generateContent` API'si durum bilgisi içermez ve yanıtı doğrudan döndürür. Yanıt yapısı, çıkışı `candidates` listesi içinde sarmalar. Bu listedeki her öğe, ayrıştırılacak `parts` listesini içeren `content` öğesini içerir.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash-lite",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

Interactions API'si, `steps` zaman çizelgesiyle birlikte depolanmış bir etkileşim kaynağı döndürür. Ara etkinlikleri bulmak için `steps` dizisini manuel olarak inceleyebilirsiniz ancak Google üretken yapay zeka SDK'ları, nihai çıkışa erişmek için doğrudan döndürülen `Interaction` nesnesinde kolaylık özellikleri sağlar.

En yaygın kolaylık özelliği, modelin yanıtının sonundaki ardışık `TextContent` bloklarını otomatik olarak ayıklayıp birleştiren **`.output_text`** (Dize) özelliğidir. Bu yöntem basit yanıtlar için mükemmel olsa da metin dışı içeriklerle (ör. düşünceler, resimler, ses veya araç çağrıları) ayrılmış önceki metin bloklarını içermez. Karmaşık veya iç içe geçmiş çok formatlı yanıtlarda bunun yerine `steps` üzerinde manuel olarak yineleme yapmanız gerekir.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## Çok aşamalı etkileşimli görüşmeler

Etkileşimler API'si, etkileşimleri varsayılan olarak depolar ve çok adımlı görüşmeler için sunucu tarafında durum yönetimi sağlar.

### Önce (`generateContent`)

`generateContent`'da, `contents` dizisini veya istemci tarafı sohbet yardımcısını kullanarak sohbet geçmişini manuel olarak yönetmeniz gerekir.

### Python

**Sohbet yardımcısını kullanma (önerilir)**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash-lite")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**Geçmişi manuel olarak yönetme**

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text(text="Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text(text="Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text(text="What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**Sohbet yardımcısını kullanma (önerilir)**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash-lite' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

**Geçmişi manuel olarak yönetme**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### REST

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### Sonra (Interactions API)

Etkileşimler API'si, sunucudaki durumu yönetir. `previous_interaction_id` referansını vererek sohbete devam edebilirsiniz.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.8-flash", input="Hi, my name is Phil."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Hi, my name is Phil.'
});
console.log("Response 1:", interaction.output_text);

interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log("Response 2:", interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## Çok formatlı girişler

Her iki API de çok formatlı girişleri (metin, resim, video vb.) destekler.

### Önce (`generateContent`)

`generateContent` içinde, `contents` dizisinde bir `parts` listesi iletirsiniz. Yanıt, ilk adayda `parts` çıkışını döndürüyor.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        {
            inlineData: {
                data: imageBytes,
                mimeType: 'image/jpeg',
            },
        },
        'Describe this image.',
    ],
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### Sonra (Interactions API)

Etkileşimler API'sinde, `input` alanına bir dizi iletirsiniz. Zaman çizelgesinde `model_output` adımını bularak çıkış içeriğini alırsınız.

### Python

```
import base64
from google import genai

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## Yapılandırılmış çıkış

Modelin belirli bir şemaya uygun JSON döndürmesini sağlamak için yanıt biçimini yapılandırın.

### Önce (`generateContent`)

`generateContent` içinde, çıkış biçimini `config` (veya `generationConfig`) nesnesinin içine yerleştirilmiş `response_mime_type` ve `response_schema` alanlarını kullanarak yapılandırırsınız.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Give me a recipe for chocolate chip cookies.',
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                recipe_name: { type: Type.STRING },
                ingredients: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING },
                },
            },
            required: ['recipe_name', 'ingredients'],
        },
    },
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseSchema": {
            "type": "OBJECT",
            "properties": {
                "recipe_name": { "type": "STRING" },
                "ingredients": {
                    "type": "ARRAY",
                    "items": { "type": "STRING" }
                }
            },
            "required": ["recipe_name", "ingredients"]
        }
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### Sonra (Interactions API)

Interactions API'de çıkış biçimi kontrolleri üst düzey bir `response_format` dizisine taşınır.

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for chocolate chip cookies.",
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe.model_json_schema(),
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: [
        {
            type: 'text',
            mime_type: 'application/json',
            schema: {
                type: 'object',
                properties: {
                    recipe_name: { type: 'string' },
                    ingredients: {
                        type: 'array',
                        items: { type: 'string' }
                    }
                },
                required: ['recipe_name', 'ingredients']
            }
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "OBJECT",
                "properties": {
                    "recipe_name": { "type": "STRING" },
                    "ingredients": {
                        "type": "ARRAY",
                        "items": { "type": "STRING" }
                    }
                },
                "required": ["recipe_name", "ingredients"]
            }
        }
    ]
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## Çok formatlı üretim

Metin dışındaki formatlarda (ör. resim veya ses) içerik oluştururken temel fark, yanıtın oluşturulan medyayı nasıl yapılandırdığıdır.

### Önce (`generateContent`)

`generateContent` içinde, yanıt oluşturulan medyayı doğrudan aday `parts` içinde döndürür. Bu medya genellikle `inlineData` içinde base64 verileri olarak bulunur.

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### Sonra (Interactions API)

Etkileşimler API'sinde, oluşturulan medya, etkileşimin kronolojik akışını koruyarak zaman çizelgesindeki bir `model_output` adımının `content` dizisinde ayrı öğeler olarak görünür.

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

Bu sayede, yanıt ayrıştırma işlemi girişlerin ve metin çıkışlarının işlenme şekliyle tutarlı olur. Her şey zaman çizelgesinde bir adım olarak değerlendirilir.

## Sunucu tarafı araçlar

Gemini, Google Arama bağlama uydurma gibi yerleşik sunucu tarafı araçlarını destekler. Temel fark, yanıtın araç yürütmeyi nasıl temsil ettiğidir.

### Önce (`generateContent`)

`generateContent`'da sunucu tarafı araçlar büyük ölçüde opak durumdadır. Aracı etkinleştirirsiniz ve ayrı bir `groundingMetadata` nesnesiyle nihai yanıtı alırsınız. En önemlisi, alıntılar satır içi değildir. `groundingSupports`, metin segmentlerini `groundingChunks` içindeki web kaynaklarıyla yeniden eşlemek için karakter dizinlerini kullanır.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

### Sonra (Interactions API)

Etkileşimler API'sinde sunucu tarafı araçlar, zaman çizelgesiyle ilgili tam şeffaflık sağlar. API, çağrıyı ve sonucu ayrı yürütmeler `steps` (`google_search_call` ve `google_search_result`) olarak kaydeder ve modelin tam olarak hangi verileri aldığını gösterir.

Ayrıca API, alıntıları **satır içi** olarak döndürür. Ayrı bir meta veri nesnesindeki dizinleri eşlemek yerine, `model_output` adımındaki metin öğesi, doğrudan kaynağa bağlanan kendi `annotations` dizisini içerir.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.result[0].search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.result[0].search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## İşlev çağırma

İşlev çağrılarının ve sonuçların yapısı da Steps şemasına uyacak şekilde değiştirildi.

### Önce (`generateContent`)

`generateContent` içinde yanıt, adaylar içindeki işlev çağrılarını döndürür.\* {Python}

```
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content,
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### Sonra (Interactions API)

Araç çağrıları ve sonuçları artık zaman çizelgesinde ayrı adımlar olarak gösteriliyor.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        result = "52°F and rain"

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        const nextInteraction = await client.interactions.create({
            model: 'gemini-3.8-flash',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        console.log(nextInteraction.output_text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## Canlı Yayın

Akışla ilgili önemli bir fark, Interactions API'nin istek gövdesinde `"stream": true` ile aynı uç noktayı kullanmasıdır. `generateContent` API ise özel bir uç noktanın (`:streamGenerateContent`) çağrılmasını gerektiriyordu.

Ayrıca, yayın etkinlikleri artık etkileşim yaşam döngüsünü izlemek ve zaman çizelgesindeki yürütme adımlarını takip etmek için özel türler kullanıyor.

### Önce (`generateContentStream`)

`generateContent` ile yanıt parçaları akışını tüketirsiniz.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### Sonra (Interactions API)

Etkileşimler API'sinde akış, yürütme adımlarını gerçekleşirken temsil etmek için sunucu tarafından gönderilen etkinlikleri (SSE) ve özel delta türlerini kullanır.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

# Örnek SSE akışı çıkışı
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### Akış araçları ve işlev çağrıları

Akışta araçların davranış şekli, daha ayrıntılı kontrol ve görünürlük sağlamak için `generateContent` önemli ölçüde değişti.

#### Önce (`generateContent`)

`generateContent` ile akış işlevi çağrıları tek bir parça halinde tamamlanmış olarak geliyordu. Oluşturulan bağımsız değişkenleri gerçek zamanlı olarak göremediğiniz için işleyici yalnızca eksiksiz bir `functionCall` nesnesi olup olmadığını kontrol ediyordu.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What is the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### Sonra (Interactions API)

Etkileşimler API'si, işlev çağrısı bağımsız değişkenlerini `arguments` etkinlikleri olarak karakter karakter yayınlar. Aracın tüm yaşam döngüsü (düşünme, görüşme, sonuç ve çıkış) bir dizi farklı adım olarak gerçekleşir.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start" and event.step:
        if getattr(event.step, "type", None) == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
        elif getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start' && event.step) {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'arguments' && event.delta.partial_arguments) {
            console.log(`  args: ${event.delta.partial_arguments}`);
        } else if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What is the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-04 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-04 UTC."],[],[]]
