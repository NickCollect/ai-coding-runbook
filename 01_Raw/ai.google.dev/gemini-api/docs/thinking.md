---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=es-419
fetched_at: 2026-08-17T02:17:43.918708+00:00
title: "Pensamiento de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Pensamiento de Gemini

Los modelos de las series [Gemini 3 y 2.5](https://ai.google.dev/gemini-api/docs/models?hl=es-419) usan un
"proceso de razonamiento" que mejora significativamente sus capacidades de razonamiento y planificación de varios pasos, lo que los hace muy eficaces para tareas complejas, como la
codificación, las matemáticas avanzadas y el análisis de datos.

Cuando usas un modelo de razonamiento, Gemini razona internamente antes de responder. La API de Interactions muestra este razonamiento a través de pasos `thought`, que son pasos dedicados que aparecen de forma cronológica junto con las llamadas a funciones, las entradas del usuario o los resultados del modelo en el array `steps`.

Cada paso de razonamiento contiene dos campos:

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| `signature` | ✅ Sí | Es una representación encriptada del estado de razonamiento interno del modelo. Siempre está presente, incluso cuando el modelo realiza un razonamiento mínimo. |
| `summary` | ❌ No | Es un array de contenido (texto o imágenes) que resume el razonamiento. Puede estar vacío según la configuración de [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=es-419), si el modelo realizó suficiente razonamiento o el tipo de contenido (por ejemplo, es posible que las imágenes latentes no tengan resúmenes de texto). |

## Interacciones con el razonamiento

Iniciar una interacción con un modelo de razonamiento es similar a cualquier otra solicitud de interacción. Especifica uno de los [modelos con compatibilidad de razonamiento](#thinking-levels) en el campo `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Resúmenes de razonamiento

Los resúmenes de razonamiento proporcionan información sobre el proceso de razonamiento interno del modelo.
De forma predeterminada, solo se muestra el resultado final. Puedes habilitar los resúmenes de razonamiento con `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Un bloque de razonamiento puede contener **solo una firma sin resumen** en los siguientes casos:

- Solicitudes simples, en las que el modelo no razonó lo suficiente para generar un resumen
- `thinking_summaries: "none"`, en las que los resúmenes están inhabilitados de forma explícita
- Es posible que ciertos tipos de contenido de razonamiento, como las imágenes, no tengan resúmenes de texto

Tu código siempre debe controlar los bloques de razonamiento en los que `summary` está vacío o ausente.

## Transmisión con razonamiento

Usa la transmisión para recibir resúmenes de razonamiento incrementales durante la generación.
Los bloques de razonamiento se entregan mediante eventos enviados por el servidor (SSE) con dos tipos de delta distintos:

| Tipo de delta | Contiene | Cuándo se envía |
| --- | --- | --- |
| `thought_summary` | Contenido de resumen de texto o imagen | Uno o más deltas con resumen incremental |
| `thought_signature` | La firma criptográfica | el último delta antes de `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

La respuesta de transmisión usa eventos enviados por el servidor (SSE) y se compone de pasos y eventos, por ejemplo:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Control del razonamiento

Los modelos de Gemini realizan un razonamiento dinámico de forma predeterminada, y ajustan automáticamente la cantidad de esfuerzo de razonamiento según la complejidad de la solicitud. Puedes controlar este comportamiento con el parámetro `thinking_level`.

| Modelo | Razonamiento predeterminado | Niveles admitidos |
| --- | --- | --- |
| gemini-3.6-flash | Activado (medio) | minimal, low, medium, high |
| gemini-3.5-flash-lite | Activado (mínimo) | minimal, low, medium, high |
| gemini-3.1-pro-preview | Activado (alto) | low, medium, high |
| gemini-3.1-flash-lite-image | Activado (mínimo) | minimal, high |
| gemini-3-flash-preview | Activado (alto) | minimal, low, medium, high |
| gemini-3-pro-preview | Activado (alto) | low, high |
| gemini-3.5-flash | Activado (medio) | minimal, low, medium, high |
| gemini-2.5-pro | Activado | low, medium, high |
| gemini-2.5-flash | Activado | low, medium, high |
| gemini-2.5-flash-lite | Desactivado | low, medium, high |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Firmas de razonamiento

Las firmas de razonamiento son representaciones encriptadas del razonamiento interno del modelo. Son necesarias para mantener la continuidad del razonamiento en las interacciones de varios turnos.

La API de Interactions facilita el manejo de las firmas de razonamiento en comparación con la API de `generateContent`.

### Modo con estado (recomendado)

De forma predeterminada, cuando usas la API de Interactions en modo con estado (si configuras `store: true` y pasas el `previous_interaction_id` en los turnos posteriores), el servidor administra automáticamente el estado de la conversación, incluidos todos los bloques de razonamiento y las firmas. En este modo, no necesitas hacer nada con respecto a las firmas. Se controlan por completo en el servidor.

### Modo sin estado

Si administras el estado de la conversación por tu cuenta (modo sin estado) y pasas el historial completo de entradas y salidas en cada solicitud:

- **DEBES** volver a enviar todos los bloques `thought` exactamente como se recibieron del modelo.
- **NO** debes quitar ni modificar los bloques de razonamiento del historial, ya que contienen las firmas necesarias para que el modelo continúe con su razonamiento.
- Cuando cambies de modelo dentro de una sesión, debes volver a enviar los bloques de razonamiento del modelo anterior. El backend administra la compatibilidad.

## Precios

Cuando el razonamiento está activado, el precio de la respuesta es la suma de los tokens de salida y los tokens de razonamiento. Puedes obtener la cantidad total de tokens de razonamiento generados en el campo `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Los modelos de razonamiento generan razonamientos completos para mejorar la calidad de la respuesta final
y, luego, muestran [resúmenes](#summaries) para proporcionar información sobre el
proceso de razonamiento. El precio se basa en los tokens de razonamiento completos que el modelo necesita generar, a pesar de que solo se muestra el resumen de la API.

Puedes obtener más información sobre los tokens en la guía de [conteo de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419).

## Prácticas recomendadas

Sigue estos lineamientos para usar los modelos de razonamiento de manera eficiente.

- **Revisa el razonamiento**: Analiza los resúmenes de razonamiento para comprender las fallas y mejorar las instrucciones.
- **Controla el presupuesto de razonamiento**: Solicita al modelo que razone menos para obtener resultados extensos y ahorrar tokens.
- **Tareas simples**: Usa un razonamiento mínimo o bajo para la recuperación o clasificación de hechos (p.ej., "¿Dónde se fundó DeepMind?").
- **Tareas moderadas**: Usa el razonamiento predeterminado para comparar conceptos o razonamientos creativos (p.ej., compara autos eléctricos e híbridos).
- **Tareas complejas**: Usa el razonamiento máximo para la codificación avanzada, las matemáticas o la planificación de varios pasos (p.ej., resuelve problemas matemáticos de AIME).

## ¿Qué sigue?

- [Generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419): Respuestas de texto básicas
- [Llamadas a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419): Conexión con las herramientas
- [Guía de Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=es-419): Funciones específicas del modelo

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
