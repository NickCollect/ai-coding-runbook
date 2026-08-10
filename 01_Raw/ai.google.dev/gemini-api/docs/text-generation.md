---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=tr
fetched_at: 2026-08-10T03:14:47.671305+00:00
title: "Metin olu\u015fturma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Metin oluşturma

Gemini API, metin, resim, video ve ses girişlerinden metin çıkışı oluşturabilir.

Temel bir örnek:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?"
  }'
```

Google GenAI SDK'ları, modelin yanıtına erişmek için doğrudan döndürülen `Interaction` nesnesinde kolaylık özellikleri sağlar.

En yaygın yardımcı **`interaction.output_text`** (Dize) olup modelin yanıtındaki son metin bloklarını döndürür. Yanıt, birden fazla ardışık `TextContent` blok arasında bölünmüşse bu bloklar otomatik olarak birleştirilir.
`.output_text`, metin dışı içeriklerle (ör. düşünceler, resimler, ses veya araç çağrıları) ayrılmış önceki metin bloklarını kapsamaz. Karmaşık veya iç içe geçmiş çok formatlı yanıtlarda bunun yerine `steps` üzerinde manuel olarak yineleme yapmanız gerekir. Diğer medya kolaylığı özellikleri hakkında daha fazla bilgi edinmek için [Etkileşimlere genel bakış](https://ai.google.dev/gemini-api/docs/interactions?hl=tr#convenience-properties) başlıklı makaleyi inceleyin.

## Gemini ile düşünme

Gemini modellerinde genellikle ["düşünme"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=tr) özelliği varsayılan olarak etkindir. Bu özellik, modelin bir isteğe yanıt vermeden önce akıl yürütmesini sağlar.

Her model, maliyet, gecikme ve zeka üzerinde kontrol sahibi olmanızı sağlayan farklı düşünme yapılandırmalarını destekler. Daha fazla ayrıntı için [düşünme kılavuzuna](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=tr#set-budget) bakın.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Sistem talimatları ve diğer yapılandırmalar

Sistem talimatlarıyla Gemini modellerinin davranışını yönlendirebilirsiniz. Modelin davranışını yapılandırmak için `system_instruction` parametresini iletin.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

Ayrıca `generation_config` parametresini kullanarak sıcaklık gibi varsayılan oluşturma parametrelerini de geçersiz kılabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

Yapılandırılabilir parametrelerin ve açıklamalarının tam listesi için [Interactions API referansına](https://ai.google.dev/api/interactions-api?hl=tr) bakın.

## Çok formatlı girişler

Gemini API, çok formatlı girişleri destekler. Bu sayede metinleri medya dosyalarıyla birleştirebilirsiniz. Aşağıdaki örnekte resim sağlama gösterilmektedir:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

Resim sağlamanın alternatif yöntemleri ve daha gelişmiş resim işleme hakkında bilgi edinmek için [Görüntü Anlama Rehberimizi](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=tr) inceleyin.
API ayrıca [doküman](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=tr), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=tr) ve [ses](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=tr) girişlerini ve bu girişlerin anlaşılmasını da destekler.

## Yanıtları akış şeklinde gösterme

Varsayılan olarak, model yalnızca tüm oluşturma işlemi tamamlandıktan sonra yanıt verir.

Daha akıcı etkileşimler için, yanıt parçaları oluşturuldukça işlemek üzere akışı kullanın. Etkinlik türleri, araçlarla yayın yapma, düşünme, aracı kullanma ve görüntü oluşturma konularını kapsayan kapsamlı bir kılavuz için özel [Yayın etkileşimleri](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=tr) kılavuzuna bakın.

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
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
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

## Çok aşamalı etkileşimli görüşmeler

Etkileşimler API'si, `previous_interaction_id` kullanarak etkileşimleri zincirleme bağlayarak çok adımlı görüşmeleri destekler. Her dönüş ayrı bir etkileşimdir ve API, sohbet geçmişini otomatik olarak yönetir.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
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
}

await main();
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

Akış, akış yöntemleriyle `previous_interaction_id` birleştirilerek çok aşamalı etkileşimlerde de kullanılabilir.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
    stream: true,
  });
  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

await main();
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Durum bilgisiz görüşmeler

Varsayılan olarak, `previous_interaction_id` kullandığınızda Interactions API, görüşme durumunu sunucu tarafında yönetir. Ancak, istemci tarafında görüşme geçmişini kendiniz yöneterek durumsuz modda da çalışabilirsiniz.

Durumsuz modu kullanmak için:
1. Sunucu tarafı depolamayı devre dışı bırakma isteğinizde `store=false` değerini ayarlayın.
2. İstemci tarafında etkileşim geçmişini bir **adımlar** dizisi olarak tutun.
3. Sonraki isteklerde, `input` alanında birikmiş adımları iletin ve yeni dönüşünüzü `user_input` adımı olarak ekleyin.

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

async function main() {
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
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
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

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## İstem ipuçları

Gemini'dan en iyi şekilde yararlanmayla ilgili öneriler için [istem mühendisliği kılavuzumuza](https://ai.google.dev/gemini/docs/prompting-strategies?hl=tr) göz atın.

## Sırada ne var?

- [Google AI Studio'da Gemini](https://aistudio.google.com?hl=tr)'ı deneyin.
- JSON benzeri yanıtlar için [yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=tr) ile denemeler yapın.
- Gemini'ın [görüntü](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=tr), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=tr), [ses](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=tr) ve [doküman](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=tr) anlama özelliklerini keşfedin.
- Çok formatlı [dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/interactions/files?hl=tr#prompt-guide) hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
