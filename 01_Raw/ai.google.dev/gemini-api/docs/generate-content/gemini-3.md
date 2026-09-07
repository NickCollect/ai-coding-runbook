---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=es-419
fetched_at: 2026-09-07T05:43:56.929924+00:00
title: "Gu\u00eda para desarrolladores de Gemini 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)

Enviar comentarios

# Guía para desarrolladores de Gemini 3

Gemini 3 es nuestra familia de modelos más inteligente hasta la fecha, creada sobre una base de razonamiento de vanguardia. Está diseñado para hacer realidad cualquier idea, ya que domina los flujos de trabajo basados en agentes, la programación autónoma y las tareas multimodales complejas.
En esta guía, se describen las funciones clave de la familia de modelos Gemini 3 y cómo aprovecharlas al máximo.

[Prueba la versión preliminar de Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=es-419)
[Prueba la versión preliminar de Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=es-419)
[Prueba Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=es-419)
[Prueba Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=es-419)

Explora nuestra [colección de apps de Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=es-419) para ver cómo el modelo maneja el razonamiento avanzado, la programación autónoma y las tareas multimodales complejas.

Comienza con algunas líneas de código:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Conoce la serie Gemini 3

Gemini 3.1 Pro es el mejor modelo para tareas complejas que requieren un amplio conocimiento del mundo y un razonamiento avanzado en todas las modalidades.

Gemini 3 Flash es nuestro modelo más reciente de la serie 3, con inteligencia de nivel Pro a la velocidad y el precio de Flash.

Nano Banana Pro (también conocido como Gemini 3 Pro Image) es nuestro modelo de generación de imágenes de mayor calidad, y Nano Banana 2 (también conocido como Gemini 3.1 Flash Image) es el equivalente de alto volumen, alta eficiencia y menor precio.

Gemini 3.1 Flash-Lite es nuestro modelo de trabajo diseñado para ofrecer rentabilidad y realizar tareas de alto volumen.

| ID de modelo | Ventana de contexto (entrada / salida) | Fecha límite de conocimiento | Precios (entrada y salida)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 millón / 64,000 | Enero de 2025 | USD 0.25 (texto, imagen, video), USD 0.50 (audio) / USD 1.50 |
| **gemini-3.1-flash-image-preview** | 128 k / 32 k | Enero de 2025 | USD 0.25 (entrada de texto) / USD 0.067 (salida de imagen)\*\* |
| **gemini-3.1-pro-preview** | 1 millón / 64,000 | Enero de 2025 | USD 2 / USD 12 (menos de 200 000 tokens)   USD 4 / USD 18 (más de 200,000 tokens) |
| **gemini-3-flash-preview** | 1 millón / 64,000 | Enero de 2025 | USD 0.50 / USD 3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | Enero de 2025 | USD 2 (entrada de texto) / USD 0.134 (salida de imagen)\*\* |

*\* Los precios son por 1 millón de tokens, a menos que se indique lo contrario.*
*\*\* Los precios de las imágenes varían según la resolución. Consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles.*

Para obtener información detallada sobre los límites, los precios y otros datos, consulta la [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419).

## Nuevas funciones de la API en Gemini 3

Gemini 3 introduce nuevos parámetros diseñados para brindarles a los desarrolladores más control sobre la latencia, el costo y la fidelidad multimodal.

### Nivel de pensamiento

Los modelos de la serie Gemini 3 usan el pensamiento dinámico de forma predeterminada para razonar las instrucciones. Puedes usar el parámetro `thinking_level`, que controla la profundidad **máxima** del proceso de razonamiento interno del modelo antes de que produzca una respuesta. Gemini 3 trata estos niveles como asignaciones relativas para el razonamiento en lugar de garantías estrictas de tokens.

Si no se especifica `thinking_level`, Gemini 3 usará `high` de forma predeterminada. Para obtener respuestas más rápidas y con menor latencia cuando no se requiere un razonamiento complejo, puedes restringir el nivel de pensamiento del modelo a `low`.

| Nivel de pensamiento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descripción |
| --- | --- | --- | --- | --- |
| **`minimal`** | No compatible | Supported (predeterminado) | Admitido | Coincide con el parámetro de configuración "sin razonamiento" para la mayoría de las búsquedas. El modelo puede pensar de forma muy mínima para tareas de programación complejas. Minimiza la latencia para aplicaciones de chat o de alta capacidad de procesamiento. Ten en cuenta que `minimal` no garantiza que el pensamiento esté desactivado. |
| **`low`** | Admitido | Admitido | Admitido | Minimiza la latencia y el costo. Es ideal para seguir instrucciones simples, chatear o usar aplicaciones de alta capacidad de procesamiento. |
| **`medium`** | Admitido | Admitido | Admitido | Pensamiento equilibrado para la mayoría de las tareas |
| **`high`** | Admitida (predeterminada, dinámica) | Compatible (dinámico) | Admitida (predeterminada, dinámica) | Maximiza la profundidad del razonamiento. Es posible que el modelo tarde mucho más en generar el primer token de salida (sin pensar), pero la salida se razonará con más cuidado. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Resolución de contenido multimedia

Gemini 3 introduce un control detallado sobre el procesamiento de visión multimodal con el parámetro `media_resolution`. Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles, pero aumentan el uso de tokens y la latencia.
El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**

Ahora puedes establecer la resolución en `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` o `media_resolution_ultra_high` para cada parte de contenido multimedia individual o de forma global (a través de `generation_config`, la opción global no está disponible para la resolución ultra alta). Si no se especifica, el modelo usa valores predeterminados óptimos según el tipo de medio.

**Configuración recomendada**

| Tipo de medio | Configuración recomendada | Tokens máx. | Orientación sobre el uso |
| --- | --- | --- | --- |
| **Imágenes** | `media_resolution_high` | 1120 | Se recomienda para la mayoría de las tareas de análisis de imágenes para garantizar la máxima calidad. |
| **PDFs** | `media_resolution_medium` | 560 | Es óptimo para la comprensión de documentos; la calidad suele saturarse en `medium`. Aumentar a `high` rara vez mejora los resultados del OCR para documentos estándar. |
| **Video** (general) | `media_resolution_low` (o `media_resolution_medium`) | 70 (por fotograma) | **Nota:** En el caso de los videos, la configuración de `low` y `medium` se trata de forma idéntica (70 tokens) para optimizar el uso del contexto. Esto es suficiente para la mayoría de las tareas de reconocimiento y descripción de acciones. |
| **Video** (con mucho texto) | `media_resolution_high` | 280 (por fotograma) | Solo se requiere cuando el caso de uso implica leer texto denso (OCR) o detalles pequeños dentro de los fotogramas de video. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatura

Para todos los modelos de Gemini 3, te recomendamos que mantengas el parámetro de temperatura en su valor predeterminado de `1.0`.

Si bien los modelos anteriores a menudo se beneficiaban de ajustar la temperatura para controlar la creatividad en comparación con el determinismo, las capacidades de razonamiento de Gemini 3 están optimizadas para el parámetro de configuración predeterminado. Cambiar la temperatura (establecerla por debajo de 1.0) puede generar un comportamiento inesperado, como bucles o un rendimiento degradado, en especial en tareas complejas de razonamiento o matemáticas.

### Firmas de razonamiento

Gemini 3 usa [firmas de pensamiento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=es-419) para mantener el contexto de razonamiento en las llamadas a la API. Estas firmas son representaciones encriptadas del proceso de pensamiento interno del modelo. Para garantizar que el modelo mantenga sus capacidades de razonamiento, debes devolver estas firmas al modelo en tu solicitud exactamente como las recibiste:

- **Llamada a función (estricta):** La API aplica una validación estricta en el "turno actual". Si faltan firmas, se generará un error 400.
- **Texto/Chat:** La validación no se aplica de forma estricta, pero omitir las firmas degradará la calidad del razonamiento y las respuestas del modelo.
- **Generación o edición de imágenes (estricta)**: La API aplica una validación estricta en todas las partes del modelo, incluido un `thoughtSignature`. Si faltan firmas, se generará un error 400.

#### Llamada a funciones (validación estricta)

Cuando Gemini genera un `functionCall`, se basa en el `thoughtSignature` para procesar correctamente el resultado de la herramienta en el siguiente turno. El "turno actual" incluye todos los pasos del Modelo (`functionCall`) y del Usuario (`functionResponse`) que ocurrieron desde el último mensaje estándar de **Usuario** `text`.

- **Llamada a una sola función:** La parte `functionCall` contiene una firma. Debes devolverlo.
- **Llamadas a funciones paralelas:** Solo la primera parte de `functionCall` en la lista contendrá la firma. Debes devolver las piezas en el mismo orden en que las recibiste.
- **Multi-Step (Sequential):** Si el modelo llama a una herramienta, recibe un resultado y llama a *otra* herramienta (en el mismo turno), **ambas** llamadas a función tienen firmas. Debes devolver **todas** las firmas acumuladas en el historial.

#### Texto y transmisión

En el caso de la generación de texto o chat estándar, no se garantiza la presencia de una firma.

- **Non-Streaming**: La parte final del contenido de la respuesta puede contener un `thoughtSignature`, aunque no siempre está presente. Si se devuelve uno, debes enviarlo de vuelta para mantener el mejor rendimiento.
- **Transmisión**: Si se genera una firma, es posible que llegue en un fragmento final que contenga una parte de texto vacía. Asegúrate de que tu analizador de transmisiones verifique las firmas incluso si el campo de texto está vacío.

#### Generación y edición de imágenes

En el caso de `gemini-3-pro-image-preview` y `gemini-3.1-flash-image-preview`, las firmas de pensamiento son fundamentales para la edición conversacional. Cuando le pides al modelo que modifique una imagen, se basa en el `thoughtSignature` del turno anterior para comprender la composición y la lógica de la imagen original.

- **Edición:** Las firmas se garantizan en la primera parte después de las reflexiones de la respuesta (`text` o `inlineData`) y en cada parte posterior de `inlineData`. Debes devolver todas estas firmas para evitar errores.

#### Ejemplos de código

#### Llamada a funciones de varios pasos (secuencial)

El usuario hace una pregunta que requiere dos pasos separados (verificar el vuelo -> reservar un taxi) en un solo turno.   
  
**Paso 1: El modelo llama a la herramienta de vuelos.**  
El modelo devuelve una firma `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Paso 2: El usuario envía el resultado de vuelo**  
Debemos enviar `<Sig_A>` para mantener el hilo de pensamiento del modelo.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Paso 3: El modelo llama a la herramienta de taxis**  
El modelo recuerda la demora del vuelo a través de `<Sig_A>` y ahora decide reservar un taxi. Genera una *nueva* firma `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Paso 4: El usuario envía el resultado de Taxi**  
Para completar el turno, debes enviar toda la cadena: `<Sig_A>` Y `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Llamada a función paralela

El usuario pregunta: "Consulta el clima en París y Londres". El modelo devuelve dos llamadas a funciones en una respuesta.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Texto o razonamiento en contexto (sin validación)

El usuario hace una pregunta que requiere razonamiento contextual sin herramientas externas. Si bien no se valida estrictamente, incluir la firma ayuda al modelo a mantener la cadena de razonamiento para las preguntas de seguimiento.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Generación y edición de imágenes

En el caso de la generación de imágenes, las firmas se validan de forma estricta. Aparecen en la **primera parte** (texto o imagen) y en **todas las partes de imágenes posteriores**. Todas deben devolverse en el próximo turno.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migración desde otros modelos

Si transfieres un registro de conversación de otro modelo (p.ej., Gemini 2.5) o insertas una llamada a función personalizada que no generó Gemini 3, no tendrás una firma válida.

Para omitir la validación estricta en estas situaciones específicas, completa el campo con esta cadena de texto ficticia específica: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Resultados estructurados con herramientas

Los modelos de Gemini 3 te permiten combinar [salidas estructuradas](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) con herramientas integradas, como la [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), el [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419), la [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y la [Llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Generación de imágenes

Gemini 3.1 Flash Image y Gemini 3 Pro Image te permiten generar y editar imágenes a partir de instrucciones de texto. Utiliza el razonamiento para "pensar" en una instrucción y puede recuperar datos en tiempo real, como pronósticos del clima o gráficos de acciones, antes de usar la fundamentación de la [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) para generar imágenes de alta fidelidad.

**Capacidades nuevas y mejoradas:**

- **Renderización de texto y 4K:** Genera texto y diagramas nítidos y legibles con resoluciones de hasta 2K y 4K.
- **Generación fundamentada:** Usa la herramienta `google_search` para verificar hechos y generar imágenes basadas en información del mundo real. La fundamentación con la Búsqueda de *Imágenes* de Google está disponible para Gemini 3.1 Flash Image.
- **Edición conversacional:** Edición de imágenes de varios turnos con solo pedir cambios (p.ej., "Haz que el fondo sea un atardecer"). Este flujo de trabajo se basa en las **firmas de pensamiento** para conservar el contexto visual entre turnos.

Para obtener detalles completos sobre las relaciones de aspecto, los flujos de trabajo de edición y las opciones de configuración, consulta la [guía de generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Ejemplo de respuesta**

![Clima en Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=es-419)

### Ejecución de código con imágenes

Gemini 3 Flash puede tratar la visión como una investigación activa, no solo como una mirada estática. Al combinar el razonamiento con la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419), el modelo formula un plan y, luego, escribe y ejecuta código de Python para acercar, recortar, anotar o manipular imágenes de otra manera paso a paso para fundamentar visualmente sus respuestas.

**Casos de uso:**

- **Acercar y revisar:** El modelo detecta de forma implícita cuando los detalles son demasiado pequeños (p.ej., leer un medidor o un número de serie distantes) y escribe código para recortar y volver a examinar el área con una resolución más alta.
- **Cálculos y gráficos visuales:** El modelo puede ejecutar cálculos de varios pasos con código (p.ej., sumar los artículos de una factura o generar un gráfico de Matplotlib a partir de datos extraídos).
- **Anotación de imágenes:** El modelo puede dibujar flechas, cuadros delimitadores o cualquier otra anotación directamente en las imágenes para responder preguntas espaciales como "¿Dónde debería ir este elemento?".

Para habilitar el pensamiento visual, configura [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) como herramienta. El modelo usará código automáticamente para manipular imágenes cuando sea necesario.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Para obtener más detalles sobre la ejecución de código con imágenes, consulta [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419#images).

### Respuestas de funciones multimodales

La [llamada a función multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#multimodal) permite que los usuarios obtengan respuestas de funciones que contienen objetos multimodales, lo que mejora el uso de las capacidades de llamada a función del modelo. Las llamadas a funciones estándar solo admiten respuestas de funciones basadas en texto:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Combina herramientas integradas y llamadas a funciones

Gemini 3 permite el uso de herramientas integradas (como la Búsqueda de Google, el contexto de URL y [más](https://ai.google.dev/gemini-api/docs/tools?hl=es-419)) y herramientas personalizadas de [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la misma llamada a la API, lo que permite flujos de trabajo más complejos. Obtén más información en la página de [combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: Type.OBJECT,
        properties: {
            location: {
                type: Type.STRING,
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Migración desde Gemini 2.5

Gemini 3 es nuestra familia de modelos más potente hasta la fecha y ofrece una mejora gradual con respecto a Gemini 2.5. Cuando realices la migración, ten en cuenta lo siguiente:

- **Pensar:** Si antes usabas ingeniería de instrucciones compleja (como la cadena de pensamiento) para obligar a Gemini 2.5 a razonar, prueba Gemini 3 con `thinking_level: "high"` y con instrucciones simplificadas.
- **Configuración de temperatura:** Si tu código existente establece explícitamente la temperatura (en especial, en valores bajos para obtener resultados determinísticos), te recomendamos que quites este parámetro y uses el valor predeterminado de Gemini 3, que es 1.0, para evitar posibles problemas de bucles o degradación del rendimiento en tareas complejas.
- **Comprensión de documentos y PDFs:**
  Si dependías de un comportamiento específico para el análisis de documentos densos, prueba el nuevo parámetro de configuración de `media_resolution_high` para garantizar la precisión continua.
- **Consumo de tokens:** La migración a los valores predeterminados de Gemini 3 puede **aumentar** el uso de tokens para los PDFs, pero **disminuir** el uso de tokens para los videos. Si las solicitudes ahora superan la ventana de contexto debido a resoluciones predeterminadas más altas, te recomendamos que reduzcas explícitamente la resolución de los medios.
- **Segmentación de imágenes:** Las capacidades de segmentación de imágenes (que devuelven máscaras a nivel de píxel para los objetos) no son compatibles con Gemini 3 Pro ni Gemini 3 Flash. Para las cargas de trabajo que requieren segmentación de imágenes nativa, recomendamos seguir utilizando Gemini 2.5 Flash con la función de pensamiento desactivada.
- **Uso de la computadora:** Gemini 3 Pro y Gemini 3 Flash admiten el [uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419). A diferencia de la serie 2.5, no necesitas usar un modelo independiente para acceder a la herramienta Uso de la computadora.
- **Compatibilidad con herramientas**: Ahora se admite la [combinación de herramientas integradas con llamadas a funciones](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419) para los modelos de Gemini 3. También se admite el [anclaje a tierra de Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) para los modelos de Gemini 3.
- **Cantidad de candidatos**: Los modelos de Gemini 3 no admiten `candidateCount > 1`.
  Si se establece este parámetro en un valor mayor que `1`, se mostrará un error 400.

## Compatibilidad con OpenAI

Para los usuarios que utilizan la [capa de compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419), los parámetros estándar (`reasoning_effort` de OpenAI) se asignan automáticamente a los equivalentes de Gemini (`thinking_level`).

## Prácticas recomendadas para escribir instrucciones

Gemini 3 es un modelo de razonamiento, lo que cambia la forma en que debes darle instrucciones.

- **Instrucciones precisas:** Sé conciso en tus instrucciones. Gemini 3 responde mejor a las instrucciones directas y claras. Es posible que analice en exceso las técnicas de ingeniería de instrucciones detalladas o demasiado complejas que se usaban para los modelos anteriores.
- **Detalle de la respuesta:** De forma predeterminada, Gemini 3 es menos detallado y prefiere proporcionar respuestas directas y eficientes. Si tu caso de uso requiere un asistente más conversacional o "parlanchín", debes dirigir explícitamente el modelo en la instrucción (p.ej., "Explica esto como un asistente amigable y parlanchín").
- **Administración del contexto:** Cuando trabajes con conjuntos de datos grandes (p.ej., libros completos, bases de código o videos largos), coloca tus instrucciones o preguntas específicas al final de la instrucción, después del contexto de los datos. Ancla el razonamiento del modelo a los datos proporcionados comenzando tu pregunta con una frase como "Según la información anterior…".

Obtén más información sobre las estrategias de diseño de instrucciones en la [guía de ingeniería de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419).

## Preguntas frecuentes

1. **¿Cuál es la fecha límite de conocimiento de Gemini 3?** Los modelos de Gemini 3 tienen una fecha límite de conocimiento de enero de 2025. Para obtener información más reciente, usa la herramienta [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419).
2. **¿Cuáles son los límites de la ventana de contexto?** Los modelos de Gemini 3 admiten una ventana de contexto de entrada de 1 millón de tokens y hasta 64,000 tokens de salida.
3. **¿Existe un nivel gratuito para Gemini 3?** Gemini 3 Flash`gemini-3-flash-preview` y 3.1 Flash-Lite `gemini-3.1-flash-lite` tienen niveles gratuitos en la API de Gemini. Puedes probar Gemini 3.1 Pro y 3 Flash de forma gratuita en Google AI Studio, pero no hay un nivel gratuito disponible para `gemini-3.1-pro-preview` en la API de Gemini.
4. **¿Mi código `thinking_budget` anterior seguirá funcionando?** Sí, `thinking_budget` sigue siendo compatible con versiones anteriores, pero recomendamos migrar a `thinking_level` para obtener un rendimiento más predecible. No uses ambos en la misma solicitud.
5. **¿Gemini 3 admite la API de Batch?** Sí, Gemini 3 admite la [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419).
6. **¿Se admite el almacenamiento en caché de contexto?** Sí, [Context Caching](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) es compatible con Gemini 3.
7. **¿Qué herramientas son compatibles con Gemini 3?** Gemini 3 admite la [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), la [Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419), la [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419), la [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y el [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419). También admite la [Llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) estándar para tus propias herramientas personalizadas y en [combinación con herramientas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).
8. **¿Qué es `gemini-3.1-pro-preview-customtools`?** Si usas `gemini-3.1-pro-preview` y el modelo ignora tus herramientas personalizadas en favor de los comandos de bash, prueba el modelo `gemini-3.1-pro-preview-customtools`. Obtén más información [aquí](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419#gemini-31-pro-preview-customtools).

## Próximos pasos

- Comienza a usar la [guía de soluciones de Gemini 3](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=es-419#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Consulta la guía específica de Cookbook sobre los [niveles de pensamiento](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=es-419#gemini3) y cómo migrar del presupuesto de pensamiento a los niveles de pensamiento.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-08-26 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-08-26 (UTC)"],[],[]]
