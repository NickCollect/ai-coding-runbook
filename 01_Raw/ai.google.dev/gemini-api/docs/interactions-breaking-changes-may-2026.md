---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=tr
fetched_at: 2026-08-03T04:34:32.321080+00:00
title: "Etkile\u015fimler API'si: \u00d6nemli de\u011fi\u015fiklikler i\u00e7in ta\u015f\u0131ma k\u0131lavuzu (May\u0131s 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Etkileşimler API'si: Önemli değişiklikler için taşıma kılavuzu (Mayıs 2026)

`v1beta` Etkileşimler API'sinde, API şeklini yeniden yapılandırarak uçuş ortasında yönlendirme ve eşzamansız araç çağrıları gibi gelecekteki özellikleri destekleyen, uyumluluğu bozan değişiklikler yapılıyor. Bu sayfada, nelerin değiştiği açıklanmakta ve geçiş yapmanıza yardımcı olmak için öncesi ve sonrası kod örnekleri verilmektedir. İki değişiklik kategorisi vardır:

1. [**Adımlar şeması**](#steps-schema): `steps` dizisi, `outputs` dizisinin yerini alarak her etkileşim dönüşünün yapılandırılmış bir zaman çizelgesini sunar.
2. [**Çıkış biçimi yapılandırması**](#output-format-config): Yeni bir polimorfik
   `response_format`, tüm çıkış biçimi kontrollerini birleştirir ve kaldırır
   `response_mime_type`.

Entegrasyonunuzu güncellemek için [Yeni şemaya nasıl geçilir?](#how-to-migrate) başlıklı makaledeki adımları uygulayın.

## Temel değişiklik: `outputs` ile `steps` arasındaki fark

Yeni şema, `outputs` dizisini `steps` dizisiyle değiştirir.

- **Eski**: Yanıtlarda yalnızca modelin oluşturduğu içeriği içeren düz bir `outputs` dizisi döndürülüyordu.
- **Yeni şema**: Yanıtlarda, tür ayırıcıları içeren yapılandırılmış adımları içeren bir `steps` dizisi döndürülür.

`POST /interactions` yalnızca çıkış adımlarını döndürür. `GET /interactions/{id}`
İlk `user_input` adımı da dahil olmak üzere adım zaman çizelgesinin tamamını döndürür.

### Temel giriş/çıkış (tekli)

#### Önce (eski)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Sonra (yeni şema)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
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

### İşlev çağırma

İstek yapısı değişmeden kalır ancak yanıt, düz içerik yerine yapılandırılmış adımlar kullanır.`outputs`

#### Önce (eski)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Sonra (yeni şema)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Sunucu tarafı araçlar

Sunucu tarafı araçlar (ör. Google Arama veya Kod Yürütme) artık `steps` dizisinde belirli adım türleri oluşturuyor. Eski şema bu işlemleri `outputs` dizisindeki belirli içerik türleri olarak döndürürken yeni şema bunları `steps` dizisine taşır. Aşağıdaki örneklerde Google Arama kullanılmaktadır.

#### Önce (eski)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Sonra (yeni şema)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Canlı Yayın

Yayın, yeni etkinlik türleri sunar:

#### Yeni etkinlik türleri

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Desteği sonlandırılmış etkinlik türleri

Aşağıdaki eski etkinlik türlerinin yerini yukarıda listelenen yeni etkinlikler almıştır:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → `interaction.in_progress`, `interaction.requires_action` vb. ile değiştirildi.

**Akışla işlev çağrıları**: İşlev çağrısıyla akışı kullandığınızda `step.start` etkinliği işlev adını, `step.delta` etkinlikleri ise bağımsız değişkenleri kısmi JSON dizeleri olarak (`arguments_delta` kullanarak) aktarır. Tam bağımsız değişkenleri almak için bu deltaları biriktirmeniz gerekir. Bu, işlev çağrısı nesnesinin tamamını tek seferde aldığınız tekli çağrılardan farklıdır.

#### Örnekler

##### Önce (Eski)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Sonra (Yeni Şema)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Durum Bilgisiz Görüşme Geçmişi

İstemci tarafında (durum bilgisi içermeyen kullanım) görüşme geçmişini manuel olarak yönetiyorsanız önceki dönüşleri nasıl bir araya getirdiğinizi güncellemeniz gerekir.

- **Eski**: Geliştiriciler genellikle yanıtlardan `outputs` dizisini toplar ve sonraki dönüşte `input` alanında geri gönderirdi.
- **Yeni şema**: Artık yanıttan `steps` dizisini toplamanız ve bunu bir sonraki isteğin `input` alanına iletmeniz, yeni kullanıcı dönüşünüzü `user_input` adımı olarak eklemeniz gerekir.

## Çıkış biçimi yapılandırması: `response_format` değişiklik

Güncellenen API, tüm çıkış biçimi kontrollerini birleşik ve polimorfik bir `response_format` alanında birleştirir. Bu, çıkış yapılandırmasını üst düzeyde merkezileştirir ve `generation_config`'nın model davranışına (ör. sıcaklık, top\_p ve düşünme) odaklanmasını sağlar.

### Önemli değişiklikler

- **API, `response_mime_type` öğesini kaldırır.** Artık `response_format` içindeki biçim girişi başına MIME türünü belirtebilirsiniz.
- **`response_format` artık polimorfik bir nesne (veya dizi).** Her girişin bir `type` ayrıştırıcısı (`text`, `audio`, `image`) ve türe özgü alanları vardır. Birden fazla çıkış biçimi isteğinde bulunmak için bir biçim girişleri dizisi iletin.
- **`image_config`, `generation_config` konumundan `response_format` konumuna taşınıyor.**
  Artık `aspect_ratio` ve `image_size` gibi görüntü çıkışı ayarlarını `"type": "image"` ile birlikte `response_format` girişinde belirtiyorsunuz.

### Yapılandırılmış çıkış (JSON)

Yeni şema, `response_mime_type` alanını kaldırır. Bunun yerine, MIME türünü ve JSON şemasını `response_format` nesnesinin içinde `"type": "text"` ile belirtin.

#### Önce (eski)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Sonra (yeni şema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Resim yapılandırması

Yeni şema, `image_config` öğesini `generation_config` öğesinden kaldırır. Artık görüntü çıkışı ayarlarını `response_format` ile `"type": "image"` girişinde belirtiyorsunuz.

#### Önce (eski)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Sonra (yeni şema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Ses yapılandırması

Yeni şema, `response_modalities: ["audio"]` yerine `"type": "audio"` değerine sahip bir `response_format` girişi kullanır.

#### Önce (eski)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### Sonra (yeni şema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

Birden fazla çıkış biçimi (ör. metin ve ses birlikte) istemek için tek bir nesne yerine `response_format`'ya biçim girişlerinden oluşan bir dizi iletin.

## Yeni şemaya nasıl geçilir?

### SDK kullanıcıları

En son SDK sürümüne (Python ≥2.0.0, JavaScript ≥2.0.0) yükseltin. SDK, yanıtları okuma şeklinizi güncellemenin dışında herhangi bir kod değişikliği yapmanıza gerek kalmadan sizi otomatik olarak yeni şemaya kaydeder (yukarıdaki örneklere bakın). Bu SDK sürümlerinde yalnızca yeni şemanın desteklendiğini unutmayın. Eski SDK sürümleri (Python 1.x.x, JavaScript 1.x.x), eski şema **8 Haziran 2026**'da kaldırılana kadar çalışmaya devam edecek.

### REST API kullanıcıları

Yeni şemayı hemen etkinleştirmek için isteklerinize `Api-Revision: 2026-05-20` üstbilgisini ekleyin. **26 Mayıs**'tan sonra yeni şema, tüm istekler için varsayılan şema haline gelir. API'nin eski şemayı kalıcı olarak kaldıracağı **8 Haziran**'a kadar `Api-Revision: 2026-05-07` ile geçici olarak kapsam dışında kalabilirsiniz.

### Zaman çizelgesi

| Tarih | Faz | SDK kullanıcıları | REST API kullanıcıları |
| --- | --- | --- | --- |
| **7 Mayıs** | Etkinleştir | Yeni SDK sürümü kullanıma sunuldu (Python ≥2.0.0, JS ≥2.0.0). Yeni şemayı otomatik olarak almak için yükseltin. | Etkinleştirmek için `Api-Revision: 2026-05-20` üstbilgisini ekleyin. Varsayılan olarak eski sürüm kalır. |
| **26 Mayıs** | Varsayılan çevirme | Daha önce yükselttiyseniz herhangi bir işlem yapmanız gerekmez. Eski SDK'lar (Python 1.x.x, JS 1.x.x) çalışmaya devam eder ancak eski yanıtlar döndürür. | Yeni şema artık varsayılan olarak ayarlanmıştır. Kapsam dışında kalmayı seçmek için `Api-Revision: 2026-05-07` üstbilgisini gönderin. |
| **8 Haziran** | Gün batımı | Python 1.x.x ve JS 1.x.x SDK sürümleri, Etkileşimler API çağrıları için çalışmayacak. | Etkileşimler API'si için eski şema kaldırıldı. `Api-Revision` üstbilgisi yoksayıldı. |

## Taşıma Denetim Listesi

### Adımlar şeması (`steps`)

- Kodu, yanıt içeriğini `outputs` yerine `steps` dizisinden okuyacak şekilde güncelleyin. [Örnekleri inceleyin](#basic-unary).
- Kodunuzun hem `user_input` hem de `model_output` adım türlerini işlediğini doğrulayın. [Örnekleri inceleyin](#basic-unary).
- (İşlev Çağırma) `steps` dizisindeki `function_call` adımlarını bulmak için kodu güncelleyin. [Örnekleri inceleyin](#function-calling).
- (Sunucu Tarafı Araçlar) Kodu, araca özgü adımları (ör. `google_search_call`, `google_search_result`) işleyecek şekilde güncelleyin. [Örnekleri inceleyin](#server-side-tools).
- (Durum Bilgisiz Geçmiş) Geçmiş yönetimini, sonraki isteğin `input` alanında `steps` dizisini iletecek şekilde güncelleyin. [Ayrıntıları göster](#stateless-history).
- (Yalnızca akış) İstemciyi yeni SSE etkinlik türlerini (`interaction.created`, `step.delta` vb.) dinleyecek şekilde güncelleyin. [Örnekleri inceleyin](#streaming).

### Çıkış biçimi yapılandırması (`response_format`)

- `response_mime_type` değerini `response_format` içindeki bir `mime_type` alanı ile değiştirin. [Örnekleri inceleyin](#structured-output).
- Mevcut `response_format` JSON şemanızı `{"type": "text", "schema": ...}` nesnesi içine alın. [Örnekleri inceleyin](#structured-output).
- (Görüntü Üretme) `image_config`, `generation_config` öğesinden `response_format` içindeki `{"type": "image", ...}` girişine taşındı. [Örnekleri inceleyin](#image-config).
- (Konuşma Üretimi) `response_modalities=["audio"]` yerine `response_format`'deki `{"type": "audio"}` girişini kullanın. [Örnekleri inceleyin](#audio-config).
- (Çok formatlı) Birden fazla çıkış biçimi istenirken `response_format` öğesini tek bir nesneden diziye dönüştürün.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-07 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-07 UTC."],[],[]]
