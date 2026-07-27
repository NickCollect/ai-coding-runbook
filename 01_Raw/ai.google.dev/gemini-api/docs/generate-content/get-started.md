---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419
fetched_at: 2026-07-27T04:46:12.063902+00:00
title: "C\u00f3mo empezar \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo empezar

Esta guía te ayudará a comenzar a usar la API heredada de **generateContent**. Para los proyectos y las aplicaciones nuevos, te recomendamos que uses la nueva **API de Interactions**, que es la mejor y más sencilla forma de compilar con los modelos y los agentes de Gemini.

En esta guía de inicio rápido, se muestra cómo instalar nuestras [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) y realizar tu primera solicitud, transmitir respuestas, crear conversaciones de varios turnos y usar herramientas con el método `generateContent` estándar.

## Obtén una clave de API

Para usar la API de Gemini, debes tener una clave de API para autenticar tus solicitudes, aplicar límites de seguridad y hacer un seguimiento del uso de tu cuenta.

- Google AI Studio crea automáticamente un proyecto y una clave de API para los usuarios nuevos.
  Puedes copiarla desde la [página Claves de API](https://aistudio.google.com/api-keys?hl=es-419).
- Si necesitas una clave nueva, haz clic en **Crear clave de API** en AI Studio y sigue el diálogo para agregar un nuevo par clave-proyecto.

[Crea una clave de la API de Gemini](https://aistudio.google.com/apikey?hl=es-419)

Configura tu clave como una variable de entorno:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Actualiza al nivel pagado

Si actualizas a la versión pagada, aumentarán tus límites de frecuencia y deberás configurar la Facturación de Cloud.

- Haz clic en **Configurar facturación** en las páginas [Claves de API](https://aistudio.google.com/api-keys?hl=es-419) o [Proyectos](https://aistudio.google.com/projects?hl=es-419) de AI Studio.
- Sigue el diálogo de Facturación de Cloud para crear o vincular una cuenta de facturación, agregar una forma de pago y pagar por adelantado un mínimo de USD 10 (o el equivalente en la moneda local) en créditos pagados.
- Consulta el uso de la API en [Google AI Studio](https://aistudio.google.com/usage?hl=es-419) en **Panel** > **Uso**.

Consulta la [página Facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419) para obtener más información.

## Instala el SDK de IA generativa de Google

### Python

Con [Python 3.9 o versiones posteriores](https://www.python.org/downloads/), instala el [paquete `google-genai`](https://pypi.org/project/google-genai/) con el siguiente [comando pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Con [Node.js v18 o versiones posteriores](https://nodejs.org/en/download/package-manager), instala el [SDK de IA generativa de Google para TypeScript y JavaScript](https://www.npmjs.com/package/@google/genai) con el siguiente [comando npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Generar texto

Usa el método `models.generate_content` para [generar una respuesta de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Cómo mostrar las respuestas en tiempo real

De forma predeterminada, el modelo devuelve una respuesta solo después de que se completa todo el proceso de generación. Para una experiencia más rápida e interactiva, puedes [transmitir los fragmentos de respuesta](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#stream) a medida que se generan.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Conversaciones de varios turnos

En el caso de las conversaciones de varios turnos, los SDKs proporcionan un asistente `chats` con estado para crear una [experiencia de chat de varios turnos](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#chat) que administra automáticamente el historial de conversaciones.

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Usar herramientas

Extiende las capacidades del modelo [fundamentando las respuestas con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) para acceder a contenido web en tiempo real. El modelo decide automáticamente cuándo buscar, ejecuta las consultas y sintetiza una respuesta.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

La API de Gemini también admite otras herramientas integradas:

- **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**:
  Permite que el modelo escriba y ejecute código de Python para resolver problemas matemáticos complejos.
- **[Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**: Te permite fundamentar las respuestas en URLs de páginas web específicas que proporciones.
- **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**: Te permite subir archivos y fundamentar las respuestas en su contenido con la búsqueda semántica.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**: Te permite fundamentar las respuestas en datos de ubicación y buscar lugares, instrucciones sobre cómo llegar y mapas.
- **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**: Permite que el modelo interactúe con una pantalla, un teclado y un mouse virtuales para realizar tareas.

## Llama a funciones personalizadas

Usa la **[llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)** para conectar modelos a tus herramientas y APIs personalizadas. El modelo determina cuándo llamar a tu función y devuelve un `functionCall` en la respuesta para que tu aplicación lo ejecute.

En este ejemplo, se declara una función de temperatura simulada y se verifica si el modelo quiere llamarla.

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## ¿Qué sigue?

Ahora que comenzaste a usar la API de Gemini, explora las siguientes guías para compilar aplicaciones más avanzadas:

- [Generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419)
- [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)
- [Comprensión de imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419)
- [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)
- [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
- [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)
- [Contexto largo](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-08 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-08 (UTC)"],[],[]]
