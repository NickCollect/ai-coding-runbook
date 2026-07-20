---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419
fetched_at: 2026-07-20T04:47:01.829790+00:00
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

Gemini permite combinar [herramientas integradas](https://ai.google.dev/gemini-api/docs/tools?hl=es-419), como `google_search`, y [llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) (también conocidas como *herramientas personalizadas*) en una sola interacción, ya que conserva y expone el historial de contexto de las llamadas a herramientas. Las combinaciones de herramientas integradas y personalizadas permiten flujos de trabajo complejos y basados en agentes en los que, por ejemplo, el modelo puede fundamentarse en datos web en tiempo real antes de llamar a tu lógica de negocios específica.

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

Los modelos de Gemini 3 usan la *circulación de contexto de herramientas* para habilitar combinaciones de herramientas integradas y personalizadas. La circulación del contexto de la herramienta permite conservar y exponer el contexto de las herramientas integradas, y compartirlo con las herramientas personalizadas en la misma interacción.

### Habilita la combinación de herramientas

- Incluye el [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#function-declarations), junto con las herramientas integradas que deseas usar, para activar el comportamiento de combinación.

### Devoluciones de pasos de la API

En una respuesta de interacción, la API devuelve pasos separados para las llamadas a herramientas integradas y las llamadas a funciones (herramientas personalizadas):

- **Pasos de herramientas integradas**: La API administra estos pasos automáticamente y conserva el contexto en cada turno.
- **Pasos de la llamada a función**: La API devuelve pasos `function_call` para tus funciones personalizadas. Ejecutas la función y proporcionas el resultado.

### Campos críticos en los pasos devueltos

Algunos campos de los pasos devueltos son fundamentales para mantener el contexto de la herramienta y habilitar combinaciones de herramientas:

- **`id`**: Se encuentra en los pasos `function_call` y `function_response`. Es un identificador único que asigna una llamada a su respuesta.
- **`signature`**: Se encuentra en los pasos de `thought`, así como en todos los pasos de llamada a herramientas (p.ej., `function_call`) y de resultados (p.ej., `function_response`) para los modelos de Gemini 3+. Este contexto encriptado permite la **circulación del contexto de la herramienta** en las interacciones.

**Administra estos campos:**

- **Modo con estado (recomendado)**: Cuando usas `previous_interaction_id`, el servidor controla automáticamente los campos `id` y `signature`.
- **Modo sin estado**: Cuando administras el historial de conversaciones de forma manual, debes asegurarte de pasar los campos `id` y `signature` al modelo en las solicitudes posteriores para validar la autenticidad y mantener el contexto. Los SDKs oficiales controlan esto automáticamente si pasas el objeto de respuesta completo al historial.

### Datos específicos de la herramienta

Algunas herramientas integradas devuelven argumentos de datos visibles para el usuario que son específicos del tipo de herramienta.

| Herramienta | Argumentos de la llamada a la herramienta visibles para el usuario (si hay alguno) | Respuesta de la herramienta visible para el usuario (si corresponde) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URLs que se explorarán | `status`: Estado de navegación `retrieved_url`: URLs navegadas |
| **file\_search** | Ninguno | Ninguno |

## Tokens y precios

Ten en cuenta que las partes de llamadas a herramientas integradas en las solicitudes se incluyen en `prompt_token_count`. Como ahora estos pasos intermedios de la herramienta son visibles y se te devuelven, forman parte del historial de la conversación. Esto solo se aplica a las *solicitudes*, no a las *respuestas*.

La herramienta de la Búsqueda de Google es una excepción a esta regla. La Búsqueda de Google ya aplica su propio modelo de precios a nivel de la búsqueda, por lo que no se cobran tokens dos veces (consulta la página [Precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419)).

Lee la página [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) para obtener más información.

## Limitaciones

- Se establece de forma predeterminada en el modo `validated` (no se admite el modo `auto`) cuando se habilita la circulación del contexto de la herramienta.
- Las herramientas integradas, como `google_search`, dependen de la información de la ubicación y la hora actual, por lo que, si tu `system_instruction` o `function_declaration.description` tienen información de ubicación y hora contradictoria, es posible que la función de combinación de herramientas no funcione bien.

## Herramientas compatibles

La circulación estándar del contexto de la herramienta se aplica a las herramientas del servidor (integradas).
La Ejecución de código también es una herramienta del servidor, pero tiene su propia solución integrada para la circulación del contexto. El uso de la computadora y la llamada a funciones son herramientas del cliente y también tienen soluciones integradas para la circulación del contexto.

| Herramienta | Lado de la ejecución | Asistencia para la circulación de contexto |
| --- | --- | --- |
| [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) | Del lado del servidor | Compatible |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) | Del lado del servidor | Compatible |
| [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) | Del lado del servidor | Compatible |
| [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419) | Del lado del servidor | Compatible |
| [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) | Del lado del servidor | Compatible (integrado, usa los pasos `code_execution` y `code_execution_result`) |
| [Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419) | Del lado del cliente | Compatible (integrado, usa los pasos `function_call` y `function_response`) |
| [Funciones personalizadas](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) | Del lado del cliente | Compatible (integrado, usa los pasos `function_call` y `function_response`) |

## ¿Qué sigue?

- Obtén más información sobre la [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la API de Gemini.
- Explora las herramientas compatibles:
  - [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)
  - [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)
  - [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-06 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-06 (UTC)"],[],[]]
