---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=es-419
fetched_at: 2026-08-31T06:39:24.126203+00:00
title: "Gu\u00eda para desarrolladores de Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)

Enviar comentarios

# Guía para desarrolladores de Gemini 3

Gemini 3 es nuestra familia de modelos más inteligente hasta la fecha, creada sobre una base de razonamiento de vanguardia. Está diseñada para dar vida a cualquier idea mediante el dominio de flujos de trabajo de agentes, la codificación autónoma y las tareas multimodales complejas.
En esta guía, se abarcan las funciones clave de la familia de modelos de Gemini 3 y cómo aprovecharla al máximo.

Explora nuestra [colección de apps de Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=es-419) para
ver cómo el modelo controla el razonamiento avanzado, la codificación autónoma y las tareas multimodales
complejas.

Comienza con algunas líneas de código:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Descubre la serie Gemini 3

Gemini 3.1 Pro es la mejor opción para tareas complejas que requieren un amplio conocimiento del mundo y un razonamiento avanzado en todas las modalidades.

Gemini 3 Flash es nuestro modelo más reciente de la serie 3, con inteligencia de nivel Pro a la velocidad y el precio de Flash.

Nano Banana Pro (también conocido como Gemini 3 Pro Image) es nuestro modelo de generación de imágenes de mayor calidad, y Nano Banana 2 (también conocido como Gemini 3.1 Flash Image) es el equivalente de alto volumen, alta eficiencia y menor precio.

Gemini 3.1 Flash-Lite es nuestro modelo de caballo de batalla creado para el modelo de rentabilidad y las tareas de alto volumen.

Actualmente, todos los modelos de Gemini 3 están en versión preliminar.

| ID de modelo | Ventana de contexto (entrada / salida) | Fecha límite de conocimiento | Precios (entrada / salida)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 M / 64,000 | Enero de 2025 | $0.25 (texto, imagen, video), $0.50 (audio) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | Enero de 2025 | $0.25 (entrada de texto) / $0.067 (salida de imagen)\*\* |
| **gemini-3.1-pro-preview** | 1 M / 64,000 | Enero de 2025 | $2 / $12 (<200,000 tokens)   $4 / $18 (>200,000 tokens) |
| **gemini-3-flash-preview** | 1 M / 64,000 | Enero de 2025 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | Enero de 2025 | $2 (entrada de texto) / $0.134 (salida de imagen)\*\* |

*\* Los precios son por 1 millón de tokens, a menos que se indique lo contrario.*
*\*\* Los precios de las imágenes varían según la resolución. Consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles.*

Para obtener información detallada sobre los límites, los precios y la información adicional, consulta la
[página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419).

## Nuevas funciones de la API en Gemini 3

Gemini 3 presenta parámetros nuevos diseñados para brindar a los desarrolladores más control sobre la latencia, el costo y la fidelidad multimodal.

### Nivel de razonamiento

Los modelos de la serie Gemini 3 usan el razonamiento dinámico de forma predeterminada para razonar a través de las instrucciones. Puedes usar el parámetro `thinking_level`, que controla la profundidad **máxima** del proceso de razonamiento interno del modelo antes de que produzca una respuesta. Gemini 3 trata estos niveles como asignaciones relativas para el razonamiento en lugar de garantías estrictas de tokens.

Si no se especifica `thinking_level`, Gemini 3 usará `high` de forma predeterminada. Para obtener respuestas más rápidas y de menor latencia cuando no se requiere un razonamiento complejo, puedes restringir el nivel de razonamiento del modelo a `low`.

| Nivel de razonamiento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descripción |
| --- | --- | --- | --- | --- |
| **`minimal`** | No admitido | Admitido (predeterminado) | Admitido | Coincide con la configuración "sin razonamiento" para la mayoría de las consultas. El modelo puede razonar de forma muy mínima para tareas de codificación complejas. Minimiza la latencia para el chat o las aplicaciones de alta capacidad de procesamiento. Ten en cuenta que `minimal` no garantiza que el razonamiento esté desactivado. |
| **`low`** | Admitido | Admitido | Admitido | Minimiza la latencia y el costo. Es la mejor opción para seguir instrucciones simples, chatear o aplicaciones de alta capacidad de procesamiento. |
| **`medium`** | Admitido | Admitido | Admitido | Razonamiento equilibrado para la mayoría de las tareas. |
| **`high`** | Admitido (predeterminado, dinámico) | Admitido (dinámico) | Admitido (predeterminado, dinámico) | Maximiza la profundidad del razonamiento. El modelo puede tardar mucho más en alcanzar un primer token de salida (sin razonamiento), pero el resultado se razonará con más cuidado. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Para todos los modelos de Gemini 3, te recomendamos que mantengas el parámetro de temperatura en su valor predeterminado de `1.0`.

Si bien los modelos anteriores a menudo se beneficiaban de la temperatura de ajuste para controlar la creatividad en comparación con el determinismo, las capacidades de razonamiento de Gemini 3 están optimizadas para la configuración predeterminada. Cambiar la temperatura (establecerla por debajo de 1.0) puede provocar un comportamiento inesperado, como bucles o un rendimiento degradado, en especial en tareas matemáticas o de razonamiento complejas.

### Firmas de razonamiento

Los modelos de Gemini 3 usan firmas de razonamiento para mantener el contexto de razonamiento en las llamadas a la API. Estas firmas son representaciones encriptadas del proceso de razonamiento interno del modelo.

- **Modo con estado (recomendado)**: Cuando se usa la API de Interactions en modo con estado (que proporciona `previous_interaction_id`), el servidor administra automáticamente el historial de conversaciones y las firmas de razonamiento.
- **Modo sin estado**: Si administras el historial de conversaciones de forma manual, debes incluir bloques de razonamiento con sus firmas en las solicitudes posteriores para validar la autenticidad.

Para obtener información detallada, consulta la página [Firmas de razonamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

### Resultados estructurados con herramientas

Los modelos de Gemini 3 te permiten combinar [resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) con herramientas integradas, incluidas
[la fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), [el contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419), [la ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y [la llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Generación de imágenes

Gemini 3.1 Flash Image y Gemini 3 Pro Image te permiten generar y editar imágenes a partir de instrucciones de texto. Usa
el razonamiento para "pensar" a través de una instrucción y puede recuperar datos en tiempo real, como
pronósticos del tiempo o gráficos de acciones, antes de usar [la fundamentación de la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) antes de generar imágenes de alta fidelidad.

**Funciones nuevas y mejoradas:**

- **Renderización de texto y 4K:** Genera texto y diagramas nítidos y legibles con resoluciones de hasta 2K y 4K.
- **Generación fundamentada:** Usa la herramienta `google_search` para verificar hechos y generar imágenes basadas en información del mundo real. Fundamentación con la Búsqueda de *imágenes* de Google disponible para Gemini 3.1 Flash Image.
- **Edición conversacional:** Edición de imágenes de varios turnos con solo solicitar cambios (p.ej., "Haz que el fondo sea un atardecer"). Este flujo de trabajo se basa en **firmas de razonamiento** para preservar el contexto visual entre turnos.

Para obtener detalles completos sobre las relaciones de aspecto, los flujos de trabajo de edición y las opciones de configuración
, consulta la [guía Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Respuesta de ejemplo**

![Clima en Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=es-419)

### Ejecución de código con imágenes

Gemini 3 Flash puede tratar la visión como una investigación activa, no solo como una mirada estática. Si combina el razonamiento con [la ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419), el modelo formula un plan y, luego, escribe y
ejecuta código de Python para acercar, recortar, anotar o manipular imágenes
paso a paso para fundamentar visualmente sus respuestas.

**Casos de uso:**

- **Acercar y examinar:** El modelo detecta de forma implícita cuando los detalles son demasiado pequeños (p.ej., leer un indicador o un número de serie distantes) y escribe código para recortar y volver a examinar el área con una resolución más alta.
- **Matemáticas y trazado visuales:** El modelo puede ejecutar cálculos de varios pasos con código (p.ej., sumar partidas en un recibo o generar un gráfico de Matplotlib a partir de datos extraídos).
- **Anotación de imágenes:** El modelo puede dibujar flechas, cuadros delimitadores u otras anotaciones directamente en las imágenes para responder preguntas espaciales como "¿Dónde debería ir este elemento?".

Para habilitar el razonamiento visual, configura [la ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) como una herramienta. El modelo usará automáticamente el código para manipular imágenes cuando sea necesario.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Para obtener más detalles sobre la ejecución de código con imágenes, consulta [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419#images).

### Respuestas de funciones multimodales

[La llamada a función multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#multimodal)
permite a los usuarios tener respuestas de funciones que contienen
objetos multimodales, lo que permite mejorar el uso de las capacidades de llamada a función
del modelo. La llamada a función estándar solo admite respuestas de funciones basadas en texto:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combina herramientas integradas y llamadas a funciones

Gemini 3 permite el uso de herramientas integradas (como la Búsqueda de Google, el contexto de URL
y [mucho más](https://ai.google.dev/gemini-api/docs/tools?hl=es-419)) y herramientas de [llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) personalizadas en la misma llamada a la API, lo que permite flujos de trabajo
más complejos.

### Python

```
from google import genai
from google.genai import types

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Migración desde Gemini 2.5

Gemini 3 es nuestra familia de modelos más potente hasta la fecha y ofrece una mejora gradual con respecto a Gemini 2.5. Cuando realices la migración, ten en cuenta lo siguiente:

- **Razonamiento:** Si antes usabas ingeniería de instrucciones complejas (como la
  cadena de razonamiento) para obligar a Gemini 2.5 a razonar, prueba Gemini 3 con
  `thinking_level: "high"` y simplifica las instrucciones.
- **Configuración de temperatura:** Si tu código existente establece explícitamente la temperatura (en especial, en valores bajos para resultados deterministas), te recomendamos que quites este parámetro y uses el valor predeterminado de Gemini 3 de 1.0 para evitar posibles problemas de bucle o degradación del rendimiento en tareas complejas.
- **Comprensión de PDF y documentos:** Si dependías de un comportamiento específico para el análisis de documentos densos, prueba la nueva configuración `media_resolution_high` para garantizar la precisión continua.
- **Consumo de tokens:** La migración a los valores predeterminados de Gemini 3 puede **aumentar** el uso de tokens para archivos PDF, pero **disminuir** el uso de tokens para videos. Si las solicitudes ahora exceden la ventana de contexto debido a resoluciones predeterminadas más altas, te recomendamos que reduzcas explícitamente la resolución de los medios.
- **Segmentación de imágenes:** Las capacidades de segmentación de imágenes (que muestran máscaras a nivel de píxeles para objetos) no son compatibles con Gemini 3 Pro ni Gemini 3 Flash. Para las cargas de trabajo que requieren segmentación de imágenes integrada, te recomendamos que sigas usando Gemini 2.5 Flash con el razonamiento desactivado.
- **Uso de la computadora:** Gemini 3 Pro y Gemini 3 Flash admiten el [uso de la
  computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419). A diferencia de la serie 2.5, no necesitas usar un modelo independiente para acceder a la herramienta Uso de la computadora.
- **Compatibilidad con herramientas**: [Ahora se admite la combinación de herramientas integradas con la llamada a función](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419) para los modelos de Gemini 3. [La fundamentación de Maps
  también es compatible con los modelos de Gemini 3
  .](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)

## compatibilidad con OpenAI

Para los usuarios que utilizan la [capa de compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419),
los parámetros estándar (el `reasoning_effort` de OpenAI) se asignan automáticamente a los
equivalentes de Gemini (`thinking_level`).

## Prácticas recomendadas para escribir instrucciones

Gemini 3 es un modelo de razonamiento, lo que cambia la forma en que debes escribir instrucciones.

- **Instrucciones precisas:** Sé conciso en tus instrucciones de entrada. Gemini 3 responde mejor a las instrucciones directas y claras. Puede analizar en exceso las técnicas de ingeniería de instrucciones detalladas o demasiado complejas que se usan para modelos más antiguos.
- **Nivel de detalle de la salida:** De forma predeterminada, Gemini 3 es menos detallado y prefiere proporcionar respuestas directas y eficientes. Si tu caso de uso requiere una personalidad más conversacional o "parlanchina", debes dirigir explícitamente el modelo en la instrucción (p.ej., "Explica esto como un asistente amigable y conversador").
- **Administración del contexto:** Cuando trabajes con conjuntos de datos grandes (p.ej., libros completos, bases de código o videos largos), coloca tus instrucciones o preguntas específicas al final de la instrucción, después del contexto de los datos. Ancla el razonamiento del modelo a los datos proporcionados comenzando tu pregunta con una frase como "Según la información anterior...".

Obtén más información sobre las estrategias de diseño de instrucciones en la [guía de ingeniería de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419).

## Preguntas frecuentes

1. **¿Cuál es la fecha límite de conocimiento para Gemini 3?** Los modelos de Gemini 3 tienen una fecha límite de conocimiento de enero de 2025. Para obtener información más reciente, usa la
   [herramienta de fundamentación de la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419).
2. **¿Cuáles son los límites de la ventana de contexto?** Los modelos de Gemini 3 admiten una ventana de contexto de entrada de 1 millón de tokens y hasta 64,000 tokens de salida.
3. **¿Existe un nivel gratuito para Gemini 3?** Gemini 3 Flash `gemini-3-flash-preview` tiene un nivel gratuito en la API de Gemini. Puedes probar Gemini 3.1 Pro y 3 Flash sin costo en Google AI Studio, pero no hay un nivel gratuito disponible para `gemini-3.1-pro-preview` en la API de Gemini.
4. **¿Mi código `thinking_budget` antiguo seguirá funcionando?** Sí, `thinking_budget` aún es compatible con la retrocompatibilidad, pero te recomendamos que migres a `thinking_level` para obtener un rendimiento más predecible. No uses ambos en la misma solicitud.
5. **¿Gemini 3 admite la API de Batch?** Sí, Gemini 3 admite la
   [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419).
6. **¿Se admite el almacenamiento en caché de contexto?** Sí, el [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) es compatible con Gemini 3.
7. **¿Qué herramientas se admiten en Gemini 3?** Gemini 3 admite
   [la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419),
   [la fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419),
   [la búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419),
   [la ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y
   [el contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419). También admite
   la llamada a función [estándar](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) para
   tus propias herramientas personalizadas y en
   [combinación con herramientas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).
8. **¿Qué es `gemini-3.1-pro-preview-customtools`?** Si usas
   `gemini-3.1-pro-preview` y el modelo ignora tus herramientas personalizadas en favor de
   los comandos de bash, prueba el `gemini-3.1-pro-preview-customtools` modelo en su lugar.
   Más información [aquí][customtools-model].

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-08-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-08-19 (UTC)"],[],[]]
