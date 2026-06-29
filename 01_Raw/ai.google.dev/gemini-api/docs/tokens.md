---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=tr
fetched_at: 2026-06-29T05:41:39.518869+00:00
title: "Jetonlar\u0131 anlama ve sayma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Jetonları anlama ve sayma

Gemini ve diğer üretken yapay zeka modelleri, giriş ve çıkışı *token* adı verilen bir ayrıntı düzeyinde işler.

**Gemini modellerinde bir jeton yaklaşık 4 karaktere eşittir.
100 jeton yaklaşık 60-80 İngilizce kelimeye eşittir.**

## Jetonlar hakkında

Jetonlar, `z` gibi tek karakterler veya `cat` gibi tam kelimeler olabilir. Uzun kelimeler
birkaç jetona ayrılır. Model tarafından kullanılan tüm jetonlar kümesine sözlük, metni jetonlara bölme işlemine ise *jetonlaştırma* adı verilir.

Faturalandırma etkinleştirildiğinde [Gemini API'ye yapılan bir çağrının maliyeti](https://ai.google.dev/pricing?hl=tr) kısmen giriş ve çıkış jetonlarının sayısına göre belirlenir. Bu nedenle, jetonları nasıl sayacağınızı bilmek faydalı olabilir.

## Parça sayma

Metin, resim dosyaları ve metin dışı diğer formatlar da dahil olmak üzere Gemini API'ye yapılan tüm girişler ve API'den alınan tüm çıkışlar jetonlaştırılır.

Jetonları aşağıdaki yöntemlerle sayabilirsiniz:

- **İsteği girerek `count_tokens` işlevini çağırın.** *Yalnızca girişteki* toplam jeton sayısını döndürür. İsteklerinizin boyutunu kontrol etmek için giriş göndermeden önce bu aramayı yapın.
- **Etkileşim yanıtında `usage` simgesini kullanın.** Giriş (`total_input_tokens`), çıkış (`total_output_tokens`), düşünme (`total_thought_tokens`), önbelleğe alınmış içerik (`total_cached_tokens`), araç kullanımı (`total_tool_use_tokens`) ve toplam (`total_tokens`) için jeton sayılarını döndürür.

### Metin jetonlarını sayma

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Çok aşamalı etkileşim parçalarını sayma

`previous_interaction_id` kullanarak sohbet geçmişindeki jetonları sayın:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Çok formatlı parçaları sayma

Resim, video ve ses dahil olmak üzere Gemini API'ye yapılan tüm girişler jetonlaştırılır.
Tokenleştirme hakkında önemli noktalar:

- **Resimler**: Her iki boyutta da ≤384 piksel olan resimler 258 jeton olarak sayılır. Daha büyük resimler, 768x768 piksellik parçalar halinde döşenir ve her parça 258 jeton olarak sayılır.
- **Video**: Saniyede 263 jeton
- **Ses**: Saniyede 32 parça

#### Resim jetonları

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**Satır içi veri örneği:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### Video jetonları

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Ses jetonları

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Sistem talimatı jetonlarını sayma

Sistem talimatları, giriş jetonları kapsamında sayılır:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Araç jetonlarını sayma

Araçlar (işlevler, kod yürütme, Google Arama) da sayılır:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Bağlam penceresi

Her Gemini modelinin işleyebileceği maksimum jeton sayısı vardır. Bağlam penceresi, giriş ve çıkış jetonlarının birleşik sınırını tanımlar.

### Bağlam penceresi boyutunu programatik olarak alma

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.5-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.5-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

Bağlam penceresi boyutlarını [modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasında bulabilirsiniz.

## Sırada ne var?

- [Metin üretme](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr): Üretimle ilgili temel bilgiler
- [Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr): Önbelleğe alma ile maliyetleri azaltma
- [Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr): Maliyetleri anlama

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
