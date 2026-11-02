---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=es-419
fetched_at: 2026-11-02T07:07:18.534318+00:00
title: "Novedades de Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Novedades de Gemini 4 Argon

Gemini 4 Argon (`gemini-4-argon`) es nuestro modelo más reciente y capaz. Puede razonar durante más tiempo sobre problemas difíciles para obtener mejores resultados en tareas complejas de programación, agentes, matemáticas y ciencias. Gemini 4 Argon está disponible a través de la API de Gemini y en Google AI Studio.

Gemini 4 Argon admite una ventana de contexto unificada de 1 millón de tokens, una decodificación larga de hasta 1 millón de tokens y niveles de razonamiento ajustables (`low`, `medium` y `high`).

[experiment

Probar en AI Studio

Crea apps desde cero con Gemini 4 Argon y AI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=es-419)
[smart\_toy

Galería de aplicaciones

Prueba y modifica apps creadas con Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=es-419)
[rocket\_launch

Comenzar

Comienza a usar Gemini 4 Argon con instrucciones de inicio.](https://aistudio.google.com/learn/gemini-4-argon?hl=es-419)

En esta guía, se explican las novedades de Gemini 4 Argon, los cambios en la API, los ejemplos de código y las instrucciones para la migración.

## Modelo nuevo

| Modelo | ID de modelo | Nivel de pensamiento predeterminado | Precios | Descripción |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Disponible hasta el 30 de noviembre de 2026 a un precio de lanzamiento de USD 2 por 1 millón de tokens de entrada y USD 10 por 1 millón de tokens de salida (USD 4 por 1 millón de tokens de entrada y USD 20 por 1 millón de tokens de salida después de esa fecha). Consulta los [precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles. | Nuestro modelo más potente, creado para resolver los problemas más difíciles con profundidad y precisión en tareas de ingeniería de software y trabajo de conocimiento del mundo real. |

Para obtener todos los detalles, consulta la [página del modelo Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=es-419). Para obtener detalles sobre los precios de lanzamiento, consulta la [sección de precios](#pricing) más adelante en esta página o la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-4-argon).

## Guía de inicio rápido

Usa el siguiente ejemplo para enviar una solicitud a `gemini-4-argon` con el `thinking_level` predeterminado recomendado (`medium`) y un límite de tokens de salida de 64,000:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
  }'
```

## Novedades de Gemini 4 Argon

- **Límite unificado de 1 millón de tokens de entrada y salida:** La entrada, el razonamiento y la salida comparten una ventana de 1,048,576 tokens.
- **Decodificación larga:** Una sola respuesta ahora puede superar los 64,000 tokens, hasta 1 millón de tokens menos tu entrada. Consulta [Decodificación larga](https://ai.google.dev/gemini-api/docs/long-decode?hl=es-419).
- **La comprensión de video de agentes tiene disponibilidad general:** La [comprensión de video de agentes](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#agentic-video-understanding) ahora tiene disponibilidad general.
- **Compatibilidad con agentes administrados:** El [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419) en los agentes administrados de Gemini ahora es compatible con Gemini 4 Argon.

Para conocer las especificaciones completas, consulta la [página del modelo Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=es-419). Para obtener información sobre los precios, consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-4-argon).

## Resultados más grandes y decodificación larga

Gemini 4 Argon puede pensar más a fondo sobre problemas complejos de matemáticas, ciencias y programación.

- **Usa `thinking_level` para controlar la profundidad del razonamiento:** El nivel de razonamiento determina la profundidad con la que el modelo razona antes de responder. `max_output_tokens` es un límite estricto: la respuesta se detiene una vez que el pensamiento y el resultado juntos lo alcanzan, por lo que debes establecerlo lo suficientemente alto como para que no se corte la respuesta.
- **Genera hasta 1 millón de tokens con la ejecución en segundo plano:** Usa la ejecución en segundo plano con un `max_output_tokens` superior a 65,536 para permitir que una sola respuesta supere los 64,000 tokens, hasta 1 millón de tokens. El modelo genera respuestas largas en saltos de hasta 64,000 tokens, y cada salto continúa desde donde se detuvo el anterior. Con la ejecución en segundo plano, nuestros servidores ejecutan estos saltos de continuación por ti. Como cada salto agrega un paso `model_output` a `interaction.steps`, une el texto de todos los pasos `model_output` cuando se complete la interacción.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {
      "max_output_tokens": 262144,
      "thinking_level": "high"
    }
  }' | jq -r '.id')

while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    break
  fi
  sleep 5
done
```

La ejecución en segundo plano es la forma más sencilla de ejecutar una decodificación larga. Ejecuta el bucle de continuación del lado del servidor hasta que el modelo finaliza o alcanza `max_output_tokens`. Si necesitas un control más detallado de los reintentos, la retirada y el manejo de errores (o no quieres que se almacenen tus interacciones), puedes usar la continuación del cliente en la [API de GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=es-419). La continuación del cliente también llegará próximamente a la API de Interactions. Para obtener información sobre la transmisión, la reconexión, el recuento de tokens y cuándo usar la decodificación larga, consulta la [guía de decodificación larga](https://ai.google.dev/gemini-api/docs/long-decode?hl=es-419).

### Establece límites de tokens de salida

`max_output_tokens` establece el total de tokens de razonamiento y salida para una respuesta. Establécelo lo suficientemente alto como para que el pensamiento no corte la respuesta y lo suficientemente bajo como para limitar el gasto cuando una instrucción difícil lo use todo.

Usa estos valores como punto de partida:

- **Tareas estándar:** Mantén el valor predeterminado de 65,536 o no establezcas ningún valor.
- **Apps existentes con un límite inferior a 32,000:** Aumenta `max_output_tokens` a, al menos, 32,768. Gemini 4 Argon puede dedicar más tiempo del límite a pensar que los modelos anteriores. Para usar menos tokens, disminuye el nivel de pensamiento.
- **Razonamiento y programación complejos:** Establece `background: true` y `max_output_tokens` en 131,072 o 262,144, hasta 1,048,576 menos tus tokens de entrada.

## Información sobre los niveles de razonamiento

El [nivel de razonamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419) es tu control principal sobre la calidad, la latencia y el uso de tokens en Gemini 4 Argon:

| Nivel de pensamiento | Uso de tokens | Cuándo debe utilizarse |
| --- | --- | --- |
| `low` | Menos tokens, latencia más baja | Tareas más simples y trabajo sensible a los costos También funciona para tareas de análisis y escritura que requieren un pensamiento ligero. La calidad puede disminuir en las tareas difíciles. |
| `medium` (predeterminada) | Equilibrado | Se recomienda para la mayoría de las tareas, incluidos los casos de uso de código complejo y de agentes. |
| `high` | Mayor cantidad de tokens, primer token más lento | Razonamiento complejo, matemáticas y ciencias avanzadas, y las tareas de código o de agentes más difíciles. Se combina bien con la decodificación larga para resultados largos. |

Ejecuta tus evaluaciones en los tres niveles y, luego, elige el nivel más bajo que cumpla con tu estándar de calidad. Para obtener más información, consulta la [guía de pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium", // Balanced reasoning effort for complex tasks
  },
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Gemini 4 Argon en agentes administrados

El [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419) en Gemini Managed Agents admite Gemini 4 Argon. Para usarlo, configura el modelo en `agent_config`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input:
    "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
    "Check search indexing with Google Search for site:web.dev. " +
    "Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
  agent_config: {
    type: "antigravity",
    model: "gemini-4-argon",
  },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote",
    "agent_config": {
      "type": "antigravity",
      "model": "gemini-4-argon"
    }
  }'
```

Para obtener más opciones, consulta [Selección de modelos](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#model-selection) en la guía del agente de Antigravity.

## Lista de tareas para la migración

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Migra a gemini-4-argon

- **Actualiza el ID del modelo:** Cambia la cadena del modelo de destino a `gemini-4-argon`.
- **Revisa el parámetro `max_output_tokens`:** Si lo estableciste de forma explícita hoy, considera aumentarlo. Recomendamos al menos 32,768, ya que Gemini 4 Argon puede usar más del límite para pensar.
- **Configura el nivel de razonamiento:** Elige `low`, `medium` (predeterminado) o `high`, y prueba tu carga de trabajo en los tres.
- **Deja de usar el almacenamiento en caché de contexto explícito:** El almacenamiento en caché explícito (`cachedContents` / `caches.create`) no es compatible con Gemini 4 Argon. Quita las llamadas que crean o hacen referencia a `cached_content` de tus solicitudes. El [almacenamiento en caché implícito](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) está habilitado de forma predeterminada para las instrucciones de al menos 4,096 tokens y descuenta un 95% de los tokens de entrada almacenados en caché en los aciertos de caché.
- **Quita los parámetros de muestreo:** Quita `temperature`, `top_p` y `top_k` de tus solicitudes. Si se proporcionan, se ignoran.
- **Usa la ejecución en segundo plano para resultados largos:** En el caso de las tareas que necesitan más de 64,000 tokens, establece `background` como verdadero y `max_output_tokens` en un valor superior a 65,536.
- **Aumenta los tiempos de espera del cliente:** Las instrucciones fijas pueden tardar varios minutos. Usa la ejecución en segundo plano o establece tiempos de espera del cliente HTTP de al menos 15 minutos.
- **Mantén el estado de la conversación en el servidor:** Usa `previous_interaction_id` para las conversaciones de varios turnos y de llamada a funciones.
- **Revisa tus estimaciones de costos:** Se factura cada token que procesa el modelo, incluidas las instrucciones internas del sistema de herramientas y las declaraciones de funciones cuando se usa la fundamentación (consulta [Precios](#pricing)).

## Precios

Gemini 4 Argon está disponible con precios de lanzamiento hasta el 30 de noviembre de 2026:

- **Tokens de entrada:** USD 2.00 por cada millón de tokens (USD 4.00 a partir del 1 de diciembre de 2026)
  - **Tokens de entrada almacenados en caché:** El almacenamiento en caché implícito descuenta un 95% de la entrada almacenada en caché, a USD 0.10 por cada millón de tokens (USD 0.20 a partir del 1 de diciembre de 2026).
- **Tokens de salida, incluidos los tokens de razonamiento:** USD 10.00 por 1 millón de tokens (USD 20.00 a partir del 1 de diciembre de 2026)

Cada token que procesa el modelo se cuenta y se factura, incluidos los tokens de razonamiento, las instrucciones del sistema de herramientas internas y las declaraciones de funciones cuando se usa la fundamentación. La fundamentación con la Búsqueda de Google también se sigue facturando por consulta.

Gemini 4 Argon no está disponible en el nivel gratuito. Para conocer los niveles de precios completos, consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-4-argon).

## Otros modelos

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=es-419)
- [Gemini 3.6 Flash y 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=es-419)
- [Ver todos los modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419)

## ¿Qué sigue?

- Lee la [guía de decodificación larga](https://ai.google.dev/gemini-api/docs/long-decode?hl=es-419) para obtener información sobre la transmisión, la reconexión y el recuento de tokens.
- Obtén más información sobre cómo funcionan los niveles de razonamiento y los resúmenes de razonamiento en la [guía de razonamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).
- Obtén más información sobre los trabajos de larga duración en la [guía de ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419).
- Probar y definir mejor las instrucciones en [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-27 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-27 (UTC)"],[],[]]
