---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it
fetched_at: 2026-10-26T05:47:07.447601+00:00
title: "API Interactions: guida alla migrazione delle modifiche che causano interruzioni (maggio 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# API Interactions: guida alla migrazione delle modifiche che causano interruzioni (maggio 2026)

L'API Interactions `v1beta` introduce modifiche che causano interruzioni e che ristrutturano la forma dell'API per supportare funzionalità future come lo steering in volo e le chiamate di strumenti asincrone. Questa pagina spiega cosa sta cambiando e fornisce esempi di codice prima e dopo per aiutarti a eseguire la migrazione. Esistono due categorie di modifiche:

1. [**Schema dei passaggi**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#steps-schema):
   Un nuovo array `steps` sostituisce l'array `outputs`, fornendo una sequenza temporale strutturata
   di ogni turno di interazione.
2. [**Configurazione del formato di output**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#output-format-config):
   Un nuovo `response_format` polimorfico consolida tutti i controlli del formato di output
   e rimuove `response_mime_type`.

Segui i passaggi descritti in
[Come eseguire la migrazione al nuovo schema](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#how-to-migrate)
per aggiornare l'integrazione.

## Modifica principale: da `outputs` a `steps`

Il nuovo schema sostituisce l'array `outputs` con un array `steps`.

- **Legacy**: le risposte restituivano un array flat `outputs` contenente solo i contenuti generati dal modello.
- **Nuovo schema**: le risposte restituiscono un array `steps` contenente passaggi strutturati con discriminatori di tipo.

`POST /interactions` restituisce solo i passaggi di output. `GET /interactions/{id}`
restituisce la sequenza temporale completa dei passaggi, incluso il passaggio `user_input` iniziale.

### Input/output di base (unario)

#### Prima (legacy)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
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

#### Dopo (nuovo schema)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
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

### Chiamata di funzione

La struttura della richiesta rimane invariata, ma la risposta sostituisce i contenuti `outputs` flat con passaggi strutturati.

#### Prima (legacy)

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

#### Dopo (nuovo schema)

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

### Strumenti lato server

Gli strumenti lato server (come la Ricerca Google o l'esecuzione di codice) ora generano tipi di passaggi specifici nell'array `steps`. Mentre lo schema legacy restituiva queste operazioni come tipi di contenuti specifici all'interno dell'array `outputs`, il nuovo schema li sposta nell'array `steps`. Gli esempi seguenti utilizzano la Ricerca Google.

#### Prima (legacy)

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
    "model": "gemini-3.8-flash",
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

#### Dopo (nuovo schema)

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
    "model": "gemini-3.8-flash",
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

Lo streaming espone nuovi tipi di eventi:

#### Nuovi tipi di eventi

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Tipi di eventi deprecati

I seguenti tipi di eventi legacy vengono sostituiti dai nuovi eventi elencati sopra:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → sostituito da `interaction.in_progress`, `interaction.requires_action` e così via.

**Chiamate di funzioni di streaming**: quando utilizzi lo streaming con le chiamate di funzioni,
l'evento `step.start` fornisce il nome della funzione e gli eventi `step.delta`
trasmettono gli argomenti come stringhe JSON parziali (utilizzando `arguments_delta`). Devi
accumulare questi delta per ottenere gli argomenti completi. Questo è diverso dalle chiamate unarie in cui ricevi immediatamente l'oggetto di chiamata di funzione completo.

#### Esempi

##### Prima (legacy)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
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

##### Dopo (nuovo schema)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
     "model": "gemini-3.8-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.8-flash"}, "event_type": "interaction.created"}
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

### Cronologia delle conversazioni stateless

Se gestisci manualmente la cronologia delle conversazioni sul lato client (caso d'uso senza stato), devi aggiornare il modo in cui concateni i turni precedenti.

- **Legacy**: gli sviluppatori spesso raccoglievano l'array `outputs` dalle risposte e lo inviavano di nuovo nel campo `input` al turno successivo.
- **Nuovo schema**: ora devi raccogliere l'array `steps` dalla risposta e passarlo nel campo `input` della richiesta successiva, aggiungendo il nuovo turno utente come passaggio `user_input`.

## Configurazione del formato di output: modifiche a `response_format`

L'API aggiornata consolida tutti i controlli del formato di output in un campo `response_format` polimorfico unificato. In questo modo, la configurazione dell'output viene centralizzata a livello superiore e `generation_config` si concentra sul comportamento del modello (come temperatura, top\_p e thinking).

### Modifiche principali

- **L'API rimuove `response_mime_type`.** Ora devi specificare il tipo MIME per ogni voce di formato all'interno di `response_format`.
- **`response_format` è ora un oggetto (o array) polimorfico.** Ogni voce ha un discriminatore `type` (`text`, `audio`, `image`) e campi specifici per il tipo. Per richiedere più modalità di output, passa un array di voci di formato.
- **`image_config` viene spostato da `generation_config` a `response_format`.**
  Ora devi specificare le impostazioni di output dell'immagine, come `aspect_ratio` e `image_size`
  in una voce `response_format` con `"type": "image"`.

### Output strutturato (JSON)

Il nuovo schema rimuove il campo `response_mime_type`. In alternativa, specifica il
tipo MIME e lo schema JSON all'interno di un `response_format` oggetto con
`"type": "text"`.

#### Prima (legacy)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
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

#### Dopo (nuovo schema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
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

### Configurazione delle immagini

Il nuovo schema rimuove `image_config` da `generation_config`. Ora devi specificare
le impostazioni di output dell'immagine in una voce `response_format` con `"type": "image"`.

#### Prima (legacy)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Dopo (nuovo schema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Configurazione audio

Il nuovo schema sostituisce `response_modalities: ["audio"]` con una voce `response_format` di `"type": "audio"`.

#### Prima (legacy)

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

#### Dopo (nuovo schema)

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

Per richiedere più modalità di output (ad esempio, testo e audio insieme), passa un array di voci di formato a `response_format` anziché un singolo oggetto.

## Come eseguire la migrazione al nuovo schema

### Utenti dell'SDK

Esegui l'upgrade all'ultima versione dell'SDK (Python ≥2.0.0, JavaScript ≥2.0.0). L'SDK attiva automaticamente il nuovo schema, senza bisogno di modifiche al codice oltre all'aggiornamento della modalità di lettura delle risposte (vedi gli esempi sopra). Tieni presente che in queste versioni dell'SDK è supportato solo il nuovo schema. Le versioni precedenti dell'SDK (Python 1.x.x, JavaScript 1.x.x) continueranno a funzionare fino alla rimozione dello schema legacy l'**8 giugno 2026**.

### Utenti dell'API REST

Aggiungi l'intestazione `Api-Revision: 2026-05-20` alle richieste per attivare subito il nuovo schema. Dopo il **26 maggio**, il nuovo schema diventerà quello predefinito per tutte le
richieste. Puoi disattivarlo temporaneamente con `Api-Revision: 2026-05-07`
fino all'**8 giugno**, quando l'API rimuoverà definitivamente lo schema legacy.

### Cronologia

| Data | Fase | Utenti dell'SDK | Utenti dell'API REST |
| --- | --- | --- | --- |
| **7 maggio** | Attiva | Nuova versione dell'SDK disponibile (Python ≥2.0.0, JS ≥2.0.0). Esegui l'upgrade per ottenere automaticamente il nuovo schema. | Aggiungi l'intestazione `Api-Revision: 2026-05-20` per attivare. Il valore predefinito rimane legacy. |
| **26 maggio** | Inversione predefinita | Non è necessaria alcuna azione se hai già eseguito l'upgrade. Gli SDK precedenti (Python 1.x.x, JS 1.x.x) continuano a funzionare, ma restituiscono risposte legacy. | Il nuovo schema è ora quello predefinito. Invia l'intestazione `Api-Revision: 2026-05-07` per disattivare. |
| **8 giugno** | Tramonto | Le versioni dell'SDK Python 1.x.x e JS 1.x.x non funzioneranno per le chiamate all'API Interactions. | Schema legacy rimosso per l'API Interactions. Intestazione `Api-Revision` ignorata. |

## Elenco di controllo per la migrazione

### Schema dei passaggi (`steps`)

- Aggiorna il codice per leggere i contenuti della risposta dall'array `steps` anziché da `outputs`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#basic-unary).
- Verifica che il codice gestisca i tipi di passaggi `user_input` e `model_output`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#basic-unary).
- (Chiamata di funzione) Aggiorna il codice per trovare i passaggi `function_call` nell'array `steps`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#function-calling).
- (Strumenti lato server) Aggiorna il codice per gestire i passaggi specifici dello strumento (ad es. `google_search_call`, `google_search_result`).
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#server-side-tools).
- (Cronologia senza stato) Aggiorna la gestione della cronologia per passare l'array `steps` nel campo `input` della richiesta successiva.
  [Vedi dettagli](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#stateless-history).
- (Solo streaming) Aggiorna il client per ascoltare i nuovi tipi di eventi SSE (`interaction.created`, `step.delta` e così via).
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#streaming).

### Configurazione del formato di output (`response_format`)

- Sostituisci `response_mime_type` con un campo `mime_type` all'interno di `response_format`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#structured-output).
- Inserisci lo schema JSON `response_format` esistente all'interno di un oggetto `{"type": "text", "schema": ...}`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#structured-output).
- (Generazione di immagini) Sposta `image_config` da `generation_config` a una voce `{"type": "image", ...}` in `response_format`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#image-config).
- (Generazione vocale) Sostituisci `response_modalities=["audio"]` con una voce `{"type": "audio"}` in `response_format`.
  [Guarda gli esempi](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it#audio-config).
- (Multimodale) Converti `response_format` da un singolo oggetto a un array quando richiedi più modalità di output.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-15 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-15 UTC."],[],[]]
