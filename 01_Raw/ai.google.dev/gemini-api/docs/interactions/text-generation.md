---
source_url: https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=es-419
fetched_at: 2026-05-18T05:17:19.918285+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Generación de texto

La API de Gemini puede generar texto a partir de entradas de texto, imágenes, video y audio.

Este es un ejemplo básico:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How does AI work?"
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How does AI work?",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How does AI work?"
  }'
```

## Pensar con Gemini

Los modelos de Gemini suelen tener la ["función de pensamiento"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=es-419) habilitada de forma predeterminada, lo que permite que el modelo razone antes de responder a una solicitud.

Cada modelo admite diferentes configuraciones de pensamiento, lo que te brinda control sobre el costo, la latencia y la inteligencia. Para obtener más detalles, consulta la [guía de pensamiento](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=es-419#set-budget).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Instrucciones del sistema y otros parámetros de configuración

Puedes guiar el comportamiento de los modelos de Gemini con instrucciones del sistema. Pasa un parámetro `system_instruction` para configurar el comportamiento del modelo.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

También puedes anular los parámetros de generación predeterminados, como la temperatura, con el parámetro `generation_config`.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

Consulta la [referencia de la API de Interactions](https://ai.google.dev/api/interactions-api?hl=es-419) para obtener una lista completa de los parámetros configurables y sus descripciones.

## Entradas multimodales

La API de Gemini admite entradas multimodales, lo que te permite combinar texto con archivos multimedia. En el siguiente ejemplo, se muestra cómo proporcionar una imagen:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
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

Para conocer otros métodos para proporcionar imágenes y obtener información sobre el procesamiento de imágenes más avanzado, consulta nuestra [guía de comprensión de imágenes](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=es-419).
La API también admite entradas y comprensión de [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=es-419), [videos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=es-419) y [audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=es-419).

## Respuestas de transmisión

De forma predeterminada, el modelo devuelve una respuesta solo después de que se completa todo el proceso de generación.

Para lograr interacciones más fluidas, usa la transmisión para controlar los fragmentos de respuesta a medida que se generan. Para obtener una guía completa sobre los tipos de eventos, la transmisión con herramientas, el pensamiento, los agentes y la generación de imágenes, consulta la guía específica sobre [Interacciones de transmisión](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=es-419).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
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
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3-flash-preview",
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## Conversaciones de varios turnos

La API de Interactions admite conversaciones de varios turnos encadenando interacciones con `previous_interaction_id`. Cada turno es una interacción independiente, y la API administra automáticamente el historial de conversaciones.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="I have 2 dogs in my house.",
)
print(interaction1.steps[-1].content[0].text)

interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

La transmisión también se puede usar para conversaciones de varios turnos combinando `previous_interaction_id` con los métodos de transmisión.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="I have 2 dogs in my house.",
)
print(interaction1.steps[-1].content[0].text)

stream = client.interactions.create(
    model="gemini-3-flash-preview",
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
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  const stream = await ai.interactions.create({
    model: "gemini-3-flash-preview",
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
# Specifies the API revision to avoid breaking changes when they become default
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Conversaciones sin estado

De forma predeterminada, la API de Interactions administra el estado de la conversación del servidor cuando usas `previous_interaction_id`. Sin embargo, también puedes operar en modo sin estado administrando el historial de conversaciones por tu cuenta en el cliente.

Para usar el modo sin estado, sigue estos pasos:
1. Establece `store=false` en tu solicitud para inhabilitar el almacenamiento del servidor.
2. Mantén el historial de conversaciones como un array de **pasos** en el cliente.
3. En las solicitudes posteriores, pasa los pasos acumulados en el campo `input` y agrega tu nuevo turno como un paso `user_input`.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

# Initialize history with the first user turn
history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

# Turn 1: Send request with store=False
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

# Append the model's response steps to history
for step in interaction1.steps:
    # Convert the SDK Step object to a dictionary
    history.append(step.model_dump())

# Append the next user turn as a user_input step
history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

# Turn 2: Send full history with store=False
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  // Initialize history with the first user turn
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  // Turn 1: Send request with store: false
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    store: false,
    input: history
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  // Append model response steps to history
  history.push(...interaction1.steps);

  // Append the next user turn
  history.push({
    type: "user_input",
    content: [{ type: "text", text: "How many paws are in my house?" }]
  });

  // Turn 2: Send full history with store: false
  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
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
# Specifies the API revision to avoid breaking changes when they become default
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
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
  --argjson first_input '[{"type": "user_input", "content": [{"type": "text", "text": "I have 2 dogs in my house."}]}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": [{"type": "text", "text": "How many paws are in my house?"}]}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## Sugerencias para escribir instrucciones

Consulta nuestra [guía de ingeniería de instrucciones](https://ai.google.dev/gemini/docs/prompting-strategies?hl=es-419) para obtener sugerencias sobre cómo aprovechar al máximo Gemini.

## ¿Qué sigue?

- Prueba [Gemini en Google AI Studio](https://aistudio.google.com?hl=es-419).
- Experimenta con [resultados estructurados](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=es-419) para obtener respuestas similares a JSON.
- Explora las capacidades de comprensión de [imágenes](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=es-419), [videos](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=es-419), [audios](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=es-419) y [documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=es-419) de Gemini.
- Obtén información sobre las [estrategias de instrucciones de archivos](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419#prompt-guide) multimodales.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-16 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-16 (UTC)"],[],[]]
