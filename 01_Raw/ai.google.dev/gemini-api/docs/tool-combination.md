---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419
fetched_at: 2026-07-06T05:06:37.832191+00:00
title: "Combinar herramientas integradas y llamadas a funciones \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Combinar herramientas integradas y llamadas a funciones

Gemini permite la combinación de [herramientas integradas](https://ai.google.dev/gemini-api/docs/tools?hl=es-419), como
`google_search`, y [llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
(también conocidas como *herramientas personalizadas*) en una sola interacción preservando y exponiendo
el historial de contexto de las llamadas a herramientas. Las combinaciones de herramientas integradas y personalizadas permiten flujos de trabajo complejos y de agentes en los que, por ejemplo, el modelo puede basarse en datos web en tiempo real antes de llamar a tu lógica empresarial específica.

Este es un ejemplo que habilita combinaciones de herramientas integradas y personalizadas con `google_search` y una función personalizada `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Cómo funciona

Los modelos de Gemini 3 usan la *circulación de contexto de herramientas* para habilitar combinaciones de herramientas integradas y personalizadas. La circulación de contexto de herramientas permite preservar y exponer el contexto de las herramientas integradas y compartirlo con herramientas personalizadas en la misma interacción.

### Habilita la combinación de herramientas

- Incluye [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#function-declarations), junto
  con las herramientas integradas que deseas usar, para activar el comportamiento de combinación.

### Pasos que muestra la API

En una respuesta de interacción, la API muestra pasos separados para las llamadas a herramientas integradas y las llamadas a funciones (herramientas personalizadas):

- **Pasos de herramientas integradas**: La API los administra automáticamente y preserva
  el contexto en los turnos.
- **Pasos de llamadas a funciones**: La API muestra pasos `function_call` para tus
  funciones personalizadas. Ejecutas la función y proporcionas el resultado.

### Campos críticos en los pasos mostrados

Ciertos campos en los pasos mostrados son fundamentales para mantener el contexto de las herramientas y habilitar las combinaciones de herramientas:

- **`id`**: Se encuentra en los pasos `function_call` y `function_response`. Es un identificador único que asigna una llamada a su respuesta.
- **`signature`**: Se encuentra en los pasos `thought`, así como en todos los pasos de llamada a herramientas (p.ej., `function_call`) y de resultado (p.ej., `function_response`) para los modelos de Gemini 3 y versiones posteriores. Este contexto encriptado permite la **circulación de contexto de herramientas** en las interacciones.

**Administración de estos campos:**

- **Modo con estado (recomendado)**: Cuando usas `previous_interaction_id`, el servidor controla automáticamente los campos `id` y `signature`.
- **Modo sin estado**: Cuando administras el historial de conversaciones de forma manual, debes asegurarte de pasar los campos `id` y `signature` al modelo en las solicitudes posteriores para validar la autenticidad y mantener el contexto. Los SDK oficiales controlan esto automáticamente si pasas el objeto de respuesta completo al historial.

### Datos específicos de la herramienta

Algunas herramientas integradas muestran argumentos de datos visibles para el usuario que son específicos del tipo de herramienta.

| Herramienta | Argumentos de llamada a herramientas visibles para el usuario (si corresponde) | Respuesta de herramientas visible para el usuario (si corresponde) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URLs que se explorarán | `status`: Estado de exploración `retrieved_url`: URLs exploradas |
| **file\_search** | Ninguno | Ninguno |

## Tokens y precios

Ten en cuenta que las partes de la llamada a herramientas integradas en las solicitudes se cuentan para `prompt_token_count`. Dado que estos pasos de herramientas intermedios ahora son visibles y se te muestran, forman parte del historial de conversaciones. Este es solo el
caso de las *solicitudes*, no de las *respuestas*.

La herramienta Búsqueda de Google es una excepción a esta regla. La Búsqueda de Google ya
aplica su propio modelo de precios a nivel de la consulta, por lo que los tokens no se
cobran dos veces (consulta la página de [precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419)).

Lee la página [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) para obtener más información.

## Limitaciones

- Se establece el modo `validated` de forma predeterminada (no admitido el modo `auto`) cuando se habilita la circulación de contexto de herramientas.
- Las herramientas integradas, como `google_search`, dependen de la ubicación y la información de la hora actual, por lo que, si tu `system_instruction` o `function_declaration.description` tienen información de ubicación y hora en conflicto, es posible que la función de combinación de herramientas no funcione bien.

## Herramientas compatibles

La circulación de contexto de herramientas estándar se aplica a las herramientas del lado del servidor (integradas).
La ejecución de código también es una herramienta del lado del servidor, pero tiene su propia solución integrada para la circulación de contexto. El uso de la computadora y las llamadas a funciones son herramientas del lado del cliente y también tienen soluciones integradas para la circulación de contexto.

| Herramienta | Lado de ejecución | Compatibilidad con la circulación de contexto |
| --- | --- | --- |
| [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) | Del lado del servidor | Compatible |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) | Del lado del servidor | Compatible |
| [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) | Del lado del servidor | Compatible |
| [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419) | Del lado del servidor | Compatible |
| [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) | Del lado del servidor | Compatible (integrado, usa los pasos `code_execution` y `code_execution_result`) |
| [Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419) | Del lado del cliente | Compatible (integrado, usa los pasos `function_call` y `function_response`) |
| [Funciones personalizadas](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) | Del lado del cliente | Compatible (integrado, usa los pasos `function_call` y `function_response`) |

## ¿Qué sigue?

- Obtén más información sobre [las llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la API de Gemini.
- Explora las herramientas compatibles:
  - [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)
  - [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)
  - [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-22 (UTC)"],[],[]]
