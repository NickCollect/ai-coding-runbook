---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=es-419
fetched_at: 2026-07-20T04:34:23.882808+00:00
title: "API de Interactions: Gu\u00eda de migraci\u00f3n de cambios rotundos (mayo de 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# API de Interactions: Guía de migración de cambios rotundos (mayo de 2026)

La API de `v1beta` Interactions presenta cambios rotundos que reestructuran la forma de la API para admitir capacidades futuras, como la dirección durante el vuelo y las llamadas a herramientas asíncronas. En esta página, se explica qué cambiará y se proporcionan ejemplos de código antes y después para ayudarte con la migración. Existen dos categorías de cambios:

1. [**Esquema de pasos**](#steps-schema): Un nuevo array `steps` reemplaza el array `outputs` y proporciona una cronología estructurada de cada turno de interacción.
2. [**Configuración del formato de salida**](#output-format-config): Un nuevo `response_format` polimórfico consolida todos los controles de formato de salida y quita `response_mime_type`.

Sigue los pasos que se indican en [Cómo migrar al nuevo esquema](#how-to-migrate) para actualizar tu integración.

## Cambio principal: De `outputs` a `steps`

El esquema nuevo reemplaza el array `outputs` por un array `steps`.

- **Heredado**: Las respuestas devolvían un array `outputs` simple que contenía solo el contenido generado por el modelo.
- **Nuevo esquema**: Las respuestas devuelven un array `steps` que contiene pasos estructurados con discriminadores de tipo.

`POST /interactions` solo devuelve pasos de salida. `GET /interactions/{id}`
devuelve el cronograma completo de pasos, incluido el paso inicial `user_input`.

### Entrada y salida básicas (unarias)

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

### Llamada a función

La estructura de la solicitud no cambia, pero la respuesta reemplaza el contenido `outputs` plano por pasos estructurados.

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

### Herramientas del servidor

Las herramientas del servidor (como la Búsqueda de Google o la Ejecución de código) ahora generan tipos de pasos específicos en el array `steps`. Si bien el esquema heredado devolvía estas operaciones como tipos de contenido específicos dentro del array `outputs`, el nuevo esquema las mueve al array `steps`. En los siguientes ejemplos, se usa la Búsqueda de Google.

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

### Transmisión

La transmisión expone nuevos tipos de eventos:

#### Nuevos tipos de eventos

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Tipos de eventos obsoletos

Los siguientes tipos de eventos heredados se reemplazan por los nuevos eventos que se mencionaron anteriormente:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → reemplazado por `interaction.in_progress`, `interaction.requires_action`, etcétera

**Llamadas a funciones de transmisión**: Cuando usas la transmisión con la llamada a función, el evento `step.start` entrega el nombre de la función y los eventos `step.delta` transmiten los argumentos como cadenas JSON parciales (con `arguments_delta`). Debes acumular estos deltas para obtener los argumentos completos. Esto difiere de las llamadas unarias, en las que recibes el objeto de llamada a la función completo de una vez.

#### Ejemplos

##### Antes (heredado)

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

##### Después (esquema nuevo)

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

### Historial de conversaciones sin estado

Si administras el historial de conversaciones de forma manual en el cliente (caso de uso sin estado), debes actualizar la forma en que encadenas los turnos anteriores.

- **Legado**: Los desarrolladores solían recopilar el array `outputs` de las respuestas y enviarlo de vuelta en el campo `input` en el siguiente turno.
- **Nuevo esquema**: Ahora debes recopilar el array `steps` de la respuesta y pasarlo en el campo `input` de la próxima solicitud, agregando tu nuevo turno de usuario como un paso `user_input`.

## Configuración del formato de resultado: cambios en `response_format`

La API actualizada consolida todos los controles de formato de salida en un campo `response_format` polimórfico unificado. Esto centraliza la configuración de salida en el nivel superior y mantiene `generation_config` enfocado en el comportamiento del modelo (como la temperatura, top\_p y el pensamiento).

### Cambios clave

- **La API quita `response_mime_type`.** Ahora especificas el tipo de MIME por entrada de formato dentro de `response_format`.
- **`response_format` ahora es un objeto polimórfico (o array).** Cada entrada tiene un discriminador `type` (`text`, `audio`, `image`) y campos específicos del tipo. Para solicitar varias modalidades de salida, pasa un array de entradas de formato.
- **`image_config` se mueve de `generation_config` a `response_format`.**
  Ahora puedes especificar la configuración de salida de la imagen, como `aspect_ratio` y `image_size`, en una entrada `response_format` con `"type": "image"`.

### Resultados estructurados (JSON)

El esquema nuevo quita el campo `response_mime_type`. En su lugar, especifica el tipo de MIME y el esquema JSON dentro de un objeto `response_format` con `"type": "text"`.

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

### Configuración de la imagen

El nuevo esquema quita `image_config` de `generation_config`. Ahora puedes especificar la configuración de salida de la imagen en una entrada `response_format` con `"type": "image"`.

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

### Configuración de audio

El esquema nuevo reemplaza `response_modalities: ["audio"]` por una entrada `response_format` de `"type": "audio"`.

#### Antes (heredado)

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

#### Después (esquema nuevo)

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

Para solicitar varias modalidades de salida (por ejemplo, texto y audio juntos), pasa un array de entradas de formato a `response_format` en lugar de un solo objeto.

## Cómo migrar al nuevo esquema

### Usuarios del SDK

Actualiza a la versión más reciente del SDK (Python ≥2.0.0, JavaScript ≥2.0.0). El SDK te habilita automáticamente para usar el nuevo esquema. No se necesitan cambios de código más allá de actualizar la forma en que lees las respuestas (consulta los ejemplos anteriores). Ten en cuenta que solo se admite el esquema nuevo en estas versiones del SDK. Las versiones anteriores del SDK (Python 1.x.x, JavaScript 1.x.x) seguirán funcionando hasta que se quite el esquema heredado el **8 de junio de 2026**.

### Usuarios de la API de REST

Agrega el encabezado `Api-Revision: 2026-05-20` a tus solicitudes para habilitar el nuevo esquema ahora. Después del **26 de mayo**, el esquema nuevo se convertirá en el predeterminado para todas las solicitudes. Puedes inhabilitar temporalmente la API con `Api-Revision: 2026-05-07` hasta el **8 de junio**, fecha en la que la API quitará de forma permanente el esquema heredado.

### Cronograma

| Fecha | Fase | Usuarios del SDK | Usuarios de la API de REST |
| --- | --- | --- | --- |
| **7 de mayo** | Habilitar | Hay una nueva versión del SDK disponible (Python ≥2.0.0, JS ≥2.0.0). Actualiza tu cuenta para obtener el nuevo esquema automáticamente. | Agrega el encabezado `Api-Revision: 2026-05-20` para habilitar la opción. El valor predeterminado sigue siendo el heredado. |
| **26 de mayo** | Volteo predeterminado | No es necesario que realices ninguna acción si ya realizaste la actualización. Los SDKs anteriores (Python 1.x.x, JS 1.x.x) aún funcionan, pero devuelven respuestas heredadas. | El nuevo esquema ahora es el predeterminado. Envía el encabezado `Api-Revision: 2026-05-07` para dejar de participar. |
| **8 de junio** | Atardecer | Las versiones 1.x.x de los SDKs de Python y JS dejarán de funcionar para las llamadas a la API de Interactions. | Se quitó el esquema heredado de la API de Interactions. Se ignoró el encabezado `Api-Revision`. |

## Lista de tareas para la migración

### Esquema de pasos (`steps`)

- Actualiza el código para leer el contenido de la respuesta del array `steps` en lugar de `outputs`. [Consulta ejemplos](#basic-unary).
- Verifica que tu código controle los tipos de pasos `user_input` y `model_output`. [Consulta ejemplos](#basic-unary).
- (Llamada a función) Actualiza el código para encontrar los pasos de `function_call` en el array `steps`. [Consulta ejemplos](#function-calling).
- (Herramientas del servidor) Actualiza el código para controlar los pasos específicos de la herramienta (p.ej., `google_search_call`, `google_search_result`). [Consulta ejemplos](#server-side-tools).
- (Historial sin estado) Actualiza la administración del historial para pasar el array `steps` en el campo `input` de la próxima solicitud. [Consulta los detalles](#stateless-history).
- (Solo para transmisión) Actualiza el cliente para que escuche los nuevos tipos de eventos de SSE (`interaction.created`, `step.delta`, etc.). [Consulta ejemplos](#streaming).

### Configuración del formato de salida (`response_format`)

- Reemplaza `response_mime_type` por un campo `mime_type` dentro de `response_format`. [Consulta ejemplos](#structured-output).
- Encapsula tu esquema JSON `response_format` existente dentro de un objeto `{"type": "text", "schema": ...}`. [Consulta ejemplos](#structured-output).
- (Generación de imágenes) Mueve `image_config` de `generation_config` a una entrada `{"type": "image", ...}` en `response_format`. [Consulta ejemplos](#image-config).
- (Generación de voz) Reemplaza `response_modalities=["audio"]` por una entrada `{"type": "audio"}` en `response_format`. [Consulta ejemplos](#audio-config).
- (Multimodal) Convierte `response_format` de un solo objeto a un array cuando se solicitan varias modalidades de salida.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-07 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-07 (UTC)"],[],[]]
