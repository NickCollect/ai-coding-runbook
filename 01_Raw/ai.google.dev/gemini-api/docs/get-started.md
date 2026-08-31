---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=tr
fetched_at: 2026-08-31T06:37:47.417388+00:00
title: "Ba\u015flang\u0131\u00e7 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Başlangıç

Bu kılavuz, [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)'yi kullanarak Gemini API'yi kullanmaya başlamanıza yardımcı olur. Bir dakikadan kısa sürede ilk API çağrınızı yapacak ve metin üretme, çok formatlı anlama, görüntü üretme, yapılandırılmış çıkış, araçlar, işlev çağrısı, ajanlar ve arka planda yürütme özelliklerini keşfedeceksiniz.

Etkileşimler API'si [Python](https://github.com/googleapis/python-genai) ve [JavaScript](https://github.com/googleapis/js-genai) SDK'ları ile REST aracılığıyla kullanılabilir.

## 1. API anahtarı alma

Gemini API'yi kullanmak için isteklerinizin kimliğini doğrulamak, güvenlik sınırlarını zorunlu kılmak ve hesabınızdaki kullanımı izlemek üzere bir API anahtarınızın olması gerekir.

- Google AI Studio, yeni kullanıcılar için otomatik olarak bir proje ve API anahtarı oluşturur.
  Bu anahtarı [API anahtarları sayfasından](https://aistudio.google.com/api-keys?hl=tr) kopyalayabilirsiniz.
- Yeni bir anahtara ihtiyacınız varsa AI Studio'da **API anahtarı oluştur**'u tıklayın ve yeni bir anahtar-proje çifti eklemek için iletişim kutusunu takip edin.

[Gemini API anahtarı oluşturma](https://aistudio.google.com/apikey?hl=tr)

Anahtarınızı ortam değişkeni olarak ayarlayın:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Ücretli katmana yükseltme

Ücretli katmana yükseltme, hız sınırlarınızı artırır ve Cloud Billing'in ayarlanmasını gerektirir.

- AI Studio [API anahtarları](https://aistudio.google.com/api-keys?hl=tr) veya [Projeler](https://aistudio.google.com/projects?hl=tr) sayfalarında **Faturalandırma ayarlarını yap**'ı tıklayın.
- Faturalandırma hesabı oluşturmak veya bağlamak, ödeme yöntemi eklemek ve ücretli kredilerle en az 10 ABD doları (veya eşdeğeri) tutarında ön ödeme yapmak için Cloud Billing iletişim kutusundaki talimatları uygulayın.
- API kullanımınızı [Google AI Studio](https://aistudio.google.com/usage?hl=tr)'da **Kontrol Paneli** > **Kullanım** bölümünde görüntüleyebilirsiniz.

Daha fazla bilgi için [Faturalandırma sayfası](https://ai.google.dev/gemini-api/docs/billing?hl=tr)'na bakın.

## 2. SDK'yı yükleme ve ilk görüşmenizi yapma

SDK'yı yükleyin ve tek bir API çağrısıyla metin oluşturun.

### Python

SDK'yı yükleyin:

```
pip install -U google-genai
```

İstemciyi başlatın ve istekte bulunun:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

SDK'yı yükleyin:

```
npm install @google/genai
```

İstemciyi başlatın ve istekte bulunun:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**Yanıt:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

REST kullanılırken API, meta verileri, kullanım istatistiklerini ve dönüşün adım adım geçmişini içeren tam `Interaction` kaynağını döndürür.

SDK'lar tam yanıtı kullanıma sunarken nihai çıktılara doğrudan erişmek için `interaction.output_text` ve `interaction.output_image` gibi kolaylık sağlayan özellikler de sunar. Yanıt yapısı hakkında daha fazla bilgi edinmek için [Etkileşime genel bakış](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) başlıklı makaleyi inceleyin veya sistem talimatları ve oluşturma yapılandırmasıyla ilgili ayrıntılar için [metin oluşturma kılavuzunu](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr) okuyun.

## 3. Yanıtı akış şeklinde gösterme

Daha akıcı etkileşimler için yanıtı oluşturulurken yayınlayın. Her `step.delta` etkinliği, hemen gösterebileceğiniz bir metin parçası sunar.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

Akış sırasında sunucu, sunucu tarafından gönderilen etkinlikler (SSE) akışıyla yanıt verir. Her etkinlikte bir tür ve JSON verileri bulunur.

**Yanıt:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

Yayın etkinliklerinin ve delta türlerinin işlenmesiyle ilgili ayrıntılı bilgi için [yayın etkileşimleri kılavuzuna](https://ai.google.dev/gemini-api/docs/streaming?hl=tr) bakın.

## 4. Çok aşamalı etkileşimli görüşmeler

Interactions API'si, iki yaklaşımla çok aşamalı etkileşimleri destekler:

- **Durum bilgili (önerilir)**: `previous_interaction_id` kullanarak sunucudaki bir görüşmeye devam edin. Sunucunun geçmişi yönetmesini ve önbelleğe almayı optimize etmesini istediğiniz çoğu sohbet ve aracı iş akışı için idealdir.
- **Durumsuz**: Önceki tüm aşamaları (ara model düşüncesi ve araç adımları dahil) her isteğe ileterek istemcideki sohbet geçmişini yönetin.

### Durumlu (önerilen)

`previous_interaction_id` ileterek etkileşimleri zincirleyin. Sunucu, görüşme geçmişinin tamamını sizin için yönetir.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### Durum bilgisiz

İstemci tarafında `store=false` ve etkileşim geçmişini yönetin. Model tarafından oluşturulan tüm adımları (`thought` ve `function_call` adımları dahil) olduğu gibi koruyup yeniden göndermeniz gerekir.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**Yanıt:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

İkinci etkileşim, yalnızca yeni adımları içeren ancak önceki dönüşün bağlamına dayanan eksiksiz bir yanıt nesnesi döndürür. [Çok aşamalı etkileşimler kılavuzunda](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#multi-turn-conversations) durumu koruma hakkında daha fazla bilgi edinin veya istemci taraflı geçmiş yönetimi için [durum bilgisiz modu](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#stateless-conversations) keşfedin.

## 5. Çok formatlı anlama

Gemini modelleri, görüntüleri, sesleri, videoları ve dokümanları doğal olarak anlar. Tek bir istekte metinle birlikte medya geçirin.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**Yanıt:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Resim, video ve ses dosyalarını nasıl ileteceğinizi öğrenmek için [görüntü anlama kılavuzu](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr)'nu inceleyin.

[hearing

Ses yorumlama

Ses dosyalarını metne dönüştürme, özetleme veya ses dosyalarıyla ilgili soruları yanıtlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr)
[videocam

Video anlama

Video içeriğini analiz etme, etkinlikleri bulma ve işlemleri açıklama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr)
[description

Belge işleme

PDF'lerden ve diğer belge biçimlerinden bilgi ayıklama](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr)

## 6. Çok formatlı üretim

Gemini, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) görüntü modellerini kullanarak yerel olarak görüntü oluşturabilir.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**Yanıt:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

Model bir resim oluşturduğunda, base64 olarak kodlanmış resim verilerini `steps` dizisindeki bir adımda ve `output_image` kolaylık özelliği aracılığıyla döndürür. En boy oranları, resim düzenleme ve referanslar hakkında bilgi edinmek için [görüntü üretme kılavuzuna](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) göz atın.

[record\_voice\_over

Konuşma üretme

Gemini 3.1 Flash TTS ile etkileyici ve çok konuşmacılı konuşmalar üretin.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)
[music\_note

Müzik üretme

Lyria 3 ile klipler ve tam uzunlukta şarkılar oluşturun.](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr)

## 7. Yapılandırılmış çıkış kullanma

Modeli, tanımladığınız bir şemayla eşleşen JSON döndürecek şekilde yapılandırın. Yapılandırılmış çıkış, [Pydantic](https://docs.pydantic.dev/latest/) (Python) ve [Zod](https://zod.dev/) (JavaScript) ile çalışır.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me a recipe for banana bread",
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

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
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
    "model": "gemini-3.6-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**Yanıt:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Çıkış metin bloğu, istenen şemaya tam olarak uyan geçerli bir JSON dizesi içeriyor. Daha karmaşık yapıları ve yinelemeli şemaları nasıl tanımlayacağınızı öğrenmek için [yapılandırılmış çıkış kılavuzuna](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) bakın.

## 8. Araçları kullanma

Modelin yanıtını Google Arama ile gerçek zamanlı bilgilerle temellendirin. API, otomatik olarak arama yapar, sonuçları işler ve alıntıları döndürür.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**Yanıt:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Arama adımları, etkileşim geçmişinde ayrıntılı olarak açıklanır. Son çıktı, web kaynaklarına işaret eden satır içi alıntılar içerir.

Arama alıntılarını nasıl çıkaracağınızı [Google Arama'da temellendirme kılavuzundan](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), birden fazla aracı nasıl birleştireceğinizi ise [araç kombinasyonu kılavuzundan](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) öğrenebilirsiniz.

[code

Kod yürütme

Güvenli bir korumalı alan Borg ortamında Python kodu çalıştırın.](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)
[link

URL bağlamı

Yanıtları doğrudan web sayfası içeriğine dayandırmak için herkese açık web URL'lerini iletin.](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)
[search

Dosya arama

Yüklenen dokümanlar ve medya dosyalarında dizine ekleme ve arama yapma](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)
[map

Google Haritalar

Yanıtları gerçek dünyadaki coğrafi ve konum verileriyle temellendirin.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)
[computer

Bilgisayar kullanımı

Tarayıcı otomasyonu ve ekran etkileşimi.](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)

## 9. Kendi işlevlerinizi çağırma

İşlev çağrısı, modeli kodunuza bağlamanıza olanak tanır. Bir işlevin adını ve parametrelerini tanımlarsınız, model ne zaman çağrılacağına karar verir ve yapılandırılmış bağımsız değişkenler döndürür. Siz de işlevi yerel olarak yürütür ve sonucu geri gönderirsiniz.

### Durumlu (önerilen)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Durum bilgisiz

Ayrıca, istemci tarafında sohbet geçmişini yönetip `store=false` ayarını yaparak işlev çağrısını durumsuz modda da kullanabilirsiniz. Durum bilgisiz modda, görüşmenin tam geçmişini sonraki her isteğin `input` alanına iletmeniz gerekir. Bu geçmişte şunlar yer almalıdır:

1. İlk `user_input` adım.
2. 1. dönüşte döndürülen tüm model tarafından oluşturulan adımlar (`thought` ve `function_call` adımları dahil) alındığı gibi.
3. Çalıştırılan işlevinizin çıkışını içeren `function_result` adımı.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**Yanıt:**

1. turda model, `requires_action` durumuna ve `function_call` adımına sahip bir yanıt döndürür:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

İşlevi yerel olarak çalıştırıp sonucu gönderdikten sonra (2. adım) son tamamlanmış etkileşim döndürülür:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Paralel işlev çağrısı veya işlev seçimi modları gibi ileri seviye özellikler için [işlev çağırma kılavuzuna](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) bakın.

## 10. Yönetilen bir temsilciyi çalıştırma

Yönetilen aracılar, kod yürütme ve dosya yönetimi gibi araçlara erişimi olan uzak bir sanal alanda çalışır. `model` yerine `agent` iletin ve `environment="remote"` değerini ayarlayın.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

Ayrıca kendi talimatlarınız, becerileriniz ve veri kaynaklarınızla [özel aracıları](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr) tanımlayıp kaydedebilirsiniz.

[rocket\_launch

Hızlı başlangıç kılavuzu

İlk temsilci çağrınızı yapın, yanıtları yayınlayın ve özel bir temsilci oluşturun.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr)
[smart\_toy

Antigravity Agent

Varsayılan aracının özellikleri, araçları, çok formatlı girişi ve fiyatlandırması.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr)
[experiment

AI Studio'daki temsilciler

Kod yazmadan aracı prototipi oluşturmak için görsel deneme alanı.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr)

## 11. Görevleri arka planda çalıştırma

Uzun görevleri eşzamansız olarak çalıştırmak için `background=True`'ı ayarlayın. `interactions.get()` ile sonuçlar için anket yapın. Daha fazla bilgi için [Arka planda yürütme kılavuzu](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr)'na bakın.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**Yanıt:**

İlk yanıt, `in_progress` durumuyla hemen döndürülür:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Arka plan görevi tamamen yürütüldüğünde, etkileşim durumunu kontrol etmek şu sonucu verir:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Modelleri ve aracıları eşzamansız olarak çalıştırma hakkında bilgi edinmek için [arka planda yürütme kılavuzunu](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr) inceleyin.

## Sırada ne var?

- [Arka planda yürütme](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr): Uzun süren görevleri eşzamansız olarak çalıştırın ve durumu yönetin.
- [Metin oluşturma](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr): Sistem talimatları, oluşturma yapılandırması ve gelişmiş metin kalıpları.
- [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr): En-boy oranları, görüntü düzenleme ve stil referansları.
- [Görüntü anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr): Sınıflandırma, nesne tespit etme ve görsel Soru-Cevap.
- [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr): Karmaşık görevler için zincirleme düşünme yöntemini kullanın.
- [İşlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr): Paralel, bileşik ve sınırlı işlev modları.
- [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr): Temellendirme, alıntılar ve arama önerileri.
- [Yönetilen Ajanlar](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Kod yürütme ve dosya yönetimi özelliklerine sahip, önceden oluşturulmuş ajanlar.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr): Planlama ve sentezleme özellikleriyle çok adımlı otonom araştırma.
- [Yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr): JSON şemaları, numaralandırmalar ve yinelemeli tür tanımları.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
