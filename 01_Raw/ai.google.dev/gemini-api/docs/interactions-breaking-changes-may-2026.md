---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pl
fetched_at: 2026-10-12T07:08:01.782735+00:00
title: "Interfejs API interakcji: przewodnik po migracji w zwi\u0105zku ze zmianami powoduj\u0105cymi niezgodno\u015b\u0107 (maj 2026\u00a0r.) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interfejs API interakcji: przewodnik po migracji w związku ze zmianami powodującymi niezgodność (maj 2026 r.)

W interfejsie Interactions API `v1beta` wprowadzamy istotne zmiany, które restrukturyzują kształt interfejsu API, aby obsługiwać przyszłe funkcje, takie jak sterowanie w trakcie działania i asynchroniczne wywołania narzędzi. Na tej stronie wyjaśniamy, co się zmienia, i podajemy przykłady kodu przed i po zmianach, aby ułatwić Ci migrację. Wyróżniamy 2 kategorie zmian:

1. [**Schemat kroków**](#steps-schema): nowa tablica `steps` zastępuje tablicę
   `outputs`, zapewniając uporządkowaną oś czasu każdej interakcji.
2. [**Konfiguracja formatu wyjściowego**](#output-format-config): nowy polimorficzny
   `response_format` łączy wszystkie elementy sterujące formatem wyjściowym i usuwa
   `response_mime_type`.

Aby zaktualizować integrację, wykonaj czynności opisane w artykule [Jak przeprowadzić migrację do nowego schematu](#how-to-migrate) w celu
aktualizacji integracji.

## Główna zmiana: `outputs` na `steps`

Nowy schemat zastępuje tablicę `outputs` tablicą `steps`.

- **Starsza wersja**: odpowiedzi zwracały płaską tablicę `outputs` zawierającą tylko wygenerowaną przez model treść.
- **Nowy schemat**: odpowiedzi zwracają tablicę `steps` zawierającą uporządkowane kroki z dyskryminatorami typu.

`POST /interactions` zwraca tylko kroki wyjściowe. `GET /interactions/{id}`
zwraca pełną oś czasu kroków, w tym początkowy krok `user_input`.

### Podstawowe dane wejściowe/wyjściowe (unarne)

#### Przed (starsza wersja)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

#### Po (nowy schemat)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

### Wywoływanie funkcji

Struktura żądania pozostaje bez zmian, ale odpowiedź zastępuje płaską zawartość `outputs` uporządkowanymi krokami.

#### Przed (starsza wersja)

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

#### Po (nowy schemat)

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

### Narzędzia po stronie serwera

Narzędzia po stronie serwera (takie jak wyszukiwarka Google czy wykonywanie kodu) zwracają teraz określone typy kroków w tablicy `steps`. Starsza wersja schematu zwracała te operacje jako określone typy treści w tablicy `outputs`, a nowy schemat przenosi je do tablicy `steps`. W podanych niżej przykładach użyto wyszukiwarki Google.

#### Przed (starsza wersja)

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
    "model": "gemini-3.6-flash",
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

#### Po (nowy schemat)

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
    "model": "gemini-3.6-flash",
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

### Streaming

Streaming udostępnia nowe typy zdarzeń:

#### Nowe typy zdarzeń

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Wycofane typy zdarzeń

Te starsze typy zdarzeń zostały zastąpione nowymi typami zdarzeń wymienionymi powyżej:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → zastąpiony przez `interaction.in_progress`, `interaction.requires_action` itp.

**Wywołania funkcji przesyłane strumieniowo**: gdy używasz przesyłania strumieniowego z wywoływaniem funkcji,
zdarzenie `step.start` dostarcza nazwę funkcji, a zdarzenia `step.delta`
przesyłają argumenty jako częściowe ciągi JSON (za pomocą `arguments_delta`). Aby
uzyskać pełne argumenty, musisz zgromadzić te delty. Różni się to od wywołań unarnych, w których od razu otrzymujesz pełny obiekt wywołania funkcji.

#### Przykłady

##### Przed (starsza wersja)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

##### Po (nowy schemat)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
     "model": "gemini-3.6-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.6-flash"}, "event_type": "interaction.created"}
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

### Historia rozmowy bezstanowej

Jeśli zarządzasz historią rozmowy ręcznie po stronie klienta (przypadek użycia bezstanowy), musisz zaktualizować sposób łączenia poprzednich tur.

- **Starsza wersja**: deweloperzy często zbierali tablicę `outputs` z odpowiedzi i wysyłali ją z powrotem w polu `input` w następnej turze.
- **Nowy schemat**: teraz musisz zbierać tablicę `steps` z odpowiedzi i przekazywać ją w polu `input` następnego żądania, dołączając nową turę użytkownika jako krok `user_input`.

## Konfiguracja formatu wyjściowego: zmiany w `response_format`

Zaktualizowany interfejs API łączy wszystkie elementy sterujące formatem wyjściowym w ujednolicone, polimorficzne pole `response_format`. Centralizuje to konfigurację wyjściową na najwyższym poziomie i sprawia, że `generation_config` skupia się na zachowaniu modelu (np. temperatura, top\_p i myślenie).

### Najważniejsze zmiany

- **Interfejs API usuwa `response_mime_type`.** Teraz typ MIME określasz w przypadku każdego wpisu formatu w `response_format`.
- **`response_format` jest teraz obiektem polimorficznym (lub tablicą).** Każdy wpis ma dyskryminator `type` (`text`, `audio`, `image`) i pola specyficzne dla typu. Aby poprosić o wiele modalności wyjściowych, przekaż tablicę wpisów formatu.
- **`image_config` przenosi się z `generation_config` do `response_format`**.
  Ustawienia wyjściowe obrazu, takie jak `aspect_ratio` i `image_size`
  określasz teraz we wpisie `response_format` z parametrem `"type": "image"`.

### Uporządkowane dane wyjściowe (JSON)

Nowy schemat usuwa pole `response_mime_type`. Zamiast tego określ typ
MIME i schemat JSON w obiekcie `response_format` z
`"type": "text"`.

#### Przed (starsza wersja)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

#### Po (nowy schemat)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
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

### Konfiguracja obrazu

Nowy schemat usuwa `image_config` z `generation_config`. Ustawienia wyjściowe obrazu określasz teraz we wpisie `response_format` z parametrem `"type": "image"`.

#### Przed (starsza wersja)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Po (nowy schemat)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Konfiguracja dźwięku

Nowy schemat zastępuje `response_modalities: ["audio"]` wpisem `response_format` z parametrem `"type": "audio"`.

#### Przed (starsza wersja)

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

#### Po (nowy schemat)

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

Aby poprosić o wiele modalności wyjściowych (np. tekst i dźwięk), przekaż do `response_format` tablicę wpisów formatu zamiast pojedynczego obiektu.

## Jak przeprowadzić migrację do nowego schematu

### Użytkownicy pakietu SDK

Uaktualnij pakiet SDK do najnowszej wersji (Python ≥2.0.0, JavaScript ≥2.0.0). Pakiet SDK automatycznie włącza nowy schemat – nie musisz wprowadzać żadnych zmian w kodzie poza aktualizacją sposobu odczytywania odpowiedzi (patrz przykłady powyżej). Pamiętaj, że w tych wersjach pakietu SDK obsługiwany jest tylko nowy schemat. Starsze wersje pakietu SDK (Python 1.x.x, JavaScript 1.x.x) będą działać do momentu usunięcia starszej wersji schematu **8 czerwca 2026 r.**

### Użytkownicy interfejsu REST API

Aby teraz włączyć nowy schemat, dodaj do żądań nagłówek `Api-Revision: 2026-05-20`. Po **26 maja** nowy schemat stanie się domyślny dla wszystkich
żądań. Do **8 czerwca** możesz tymczasowo zrezygnować z nowego schematu, używając nagłówka `Api-Revision: 2026-05-07`
. Po tej dacie interfejs API trwale usunie starszą wersję schematu.

### Oś czasu

| Data | Faza | Użytkownicy pakietu SDK | Użytkownicy interfejsu REST API |
| --- | --- | --- | --- |
| **7 maja** | Zaakceptuj | Dostępna jest nowa wersja pakietu SDK (Python ≥2.0.0, JS ≥2.0.0). Uaktualnij pakiet SDK, aby automatycznie uzyskać nowy schemat. | Aby włączyć nowy schemat, dodaj nagłówek `Api-Revision: 2026-05-20`. Domyślnie nadal używana jest starsza wersja. |
| **26 maja** | Domyślne odwrócenie | Jeśli pakiet SDK został już uaktualniony, nie musisz nic robić. Starsze wersje pakietu SDK (Python 1.x.x, JS 1.x.x) nadal działają, ale zwracają odpowiedzi w starszej wersji. | Nowy schemat jest teraz domyślny. Aby zrezygnować z nowego schematu, wyślij nagłówek `Api-Revision: 2026-05-07`. |
| **8 czerwca** | Zachód słońca | Wersje pakietu SDK Python 1.x.x i JS 1.x.x przestaną działać w przypadku wywołań interfejsu Interactions API. | Starsza wersja schematu została usunięta z interfejsu Interactions API. Nagłówek `Api-Revision` jest ignorowany. |

## Lista kontrolna migracji

### Schemat kroków (`steps`)

- Zaktualizuj kod, aby odczytywać treść odpowiedzi z tablicy `steps` zamiast z `outputs`. [Zobacz przykłady](#basic-unary).
- Sprawdź, czy Twój kod obsługuje typy kroków `user_input` i `model_output`. [Zobacz przykłady](#basic-unary).
- (Wywoływanie funkcji) Zaktualizuj kod, aby znajdować kroki `function_call` w tablicy `steps`. [Zobacz przykłady](#function-calling).
- (Narzędzia po stronie serwera) Zaktualizuj kod, aby obsługiwać kroki specyficzne dla narzędzia (np. `google_search_call`, `google_search_result`). [Zobacz przykłady](#server-side-tools).
- (Historia bez stanu) Zaktualizuj zarządzanie historią, aby przekazywać tablicę `steps` w polu `input` następnego żądania. [Zobacz szczegóły](#stateless-history).
- (Tylko streaming) Zaktualizuj klienta, aby nasłuchiwał nowych typów zdarzeń SSE (`interaction.created`, `step.delta` itp.). [Zobacz przykłady](#streaming).

### Konfiguracja formatu wyjściowego (`response_format`)

- Zastąp `response_mime_type` polem `mime_type` w `response_format`. [Zobacz przykłady](#structured-output).
- Owiń istniejący `response_format` schemat JSON w obiekt `{"type": "text", "schema": ...}`. [Zobacz przykłady](#structured-output).
- (Generowanie obrazów) Przenieś `image_config` z `generation_config` do wpisu `{"type": "image", ...}` w `response_format`. [Zobacz przykłady](#image-config).
- (Generowanie mowy) Zastąp `response_modalities=["audio"]` wpisem `{"type": "audio"}` w `response_format`. [Zobacz przykłady](#audio-config).
- (Wielomodowość) Podczas wysyłania żądania wielu modalności wyjściowych zmień `response_format` z pojedynczego obiektu na tablicę.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-12 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-12 UTC."],[],[]]
