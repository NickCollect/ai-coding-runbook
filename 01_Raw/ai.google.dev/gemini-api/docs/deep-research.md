---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419
fetched_at: 2026-08-10T03:10:43.930933+00:00
title: "Agente de Deep Research de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de Deep Research de Gemini

El agente de Deep Research de Gemini planifica, ejecuta y sintetiza de forma autónoma tareas de investigación de varios pasos. Con la tecnología de Gemini, navega por entornos de información complejos para producir informes detallados con citas. Las nuevas capacidades te permiten planificar de forma colaborativa con el agente, conectarte a herramientas externas con servidores de MCP, incluir visualizaciones (como gráficos) y proporcionar documentos directamente como entrada.

Las tareas de investigación implican búsquedas y lecturas iterativas, y pueden tardar varios minutos en completarse. Debes usar la [ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419) (establece `background=true`) para ejecutar el agente de forma asíncrona y sondear los resultados o transmitir actualizaciones. Consulta [Cómo controlar tareas de larga duración](#long-running-tasks) para obtener más detalles.

En el siguiente ejemplo, se muestra cómo iniciar una tarea de investigación en segundo plano y sondear los resultados.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Versiones compatibles

El agente de Deep Research está disponible en dos versiones:

- **Deep Research** (`deep-research-preview-04-2026`): Se diseñó para ser rápido y eficiente, y es ideal para transmitirlo a la IU del cliente.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Máxima exhaustividad para la recopilación y síntesis automatizadas de contexto.

## Planificación colaborativa

La planificación colaborativa te permite controlar la dirección de la investigación antes de que el agente comience su trabajo, ya que te permite revisar y definir mejor el plan de investigación antes de la ejecución. Cuando se habilita, el agente devuelve un plan de investigación propuesto en lugar de ejecutar la investigación de inmediato. Luego, puedes revisar, modificar o aprobar el plan a través de interacciones de varios turnos.

### Paso 1: Solicita un plan

Establece `collaborative_planning=True` en la primera interacción. El agente devuelve un plan de investigación en lugar de un informe completo.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Paso 2: Define mejor el plan (opcional)

Usa `previous_interaction_id` para continuar la conversación y realizar iteraciones en el plan. Mantén presionado `collaborative_planning=True` para permanecer en el modo de planificación.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Paso 3: Aprueba y ejecuta

Establece `collaborative_planning=False` (o omítelo) para aprobar el plan y comenzar la investigación.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Visualización

Cuando `visualization` se establece en `"auto"`, el agente puede generar gráficos y otros elementos visuales para respaldar los resultados de su investigación.
Las imágenes generadas se incluyen en los pasos de la respuesta y se transmiten como deltas de `image`. Para obtener mejores resultados, pide explícitamente imágenes en tu búsqueda, por ejemplo, "Incluye gráficos que muestren las tendencias a lo largo del tiempo" o "Genera gráficos que comparen la participación de mercado". Si configuras `visualization` como `"auto"`, se habilita la capacidad, pero el agente genera elementos visuales solo cuando la instrucción los solicita.

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Herramientas compatibles

Deep Research admite varias herramientas integradas y externas. De forma predeterminada (cuando no se proporciona ningún parámetro `tools`), el agente tiene acceso a la Búsqueda de Google, al contexto de URL y a la ejecución de código. Puedes especificar de forma explícita las herramientas para restringir o extender las capacidades del agente.

| Herramienta | Valor del tipo | Descripción |
| --- | --- | --- |
| Búsqueda de Google | `google_search` | Buscar en la Web pública Habilitada de forma predeterminada. |
| Contexto de URL | `url_context` | Leer y resumir el contenido de páginas web Habilitada de forma predeterminada. |
| Ejecución de código | `code_execution` | Ejecutar código para realizar cálculos y análisis de datos Habilitada de forma predeterminada. |
| Servidor MCP | `mcp_server` | Conectarse a servidores MCP remotos para acceder a herramientas externas |
| Búsqueda de archivos | `file_search` | Busca en los corpus de documentos que subiste. |

### Búsqueda de Google

Habilita explícitamente la Búsqueda de Google como la única herramienta:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Contexto de URL

Permite que el agente lea y resuma páginas web específicas:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Ejecución de código

Permite que el agente ejecute código para realizar cálculos y análisis de datos:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Servidores de MCP

Conéctate a servidores de MCP remotos para darle al agente acceso a herramientas y servicios externos.

Proporciona el servidor `name` y `url` en la configuración de herramientas. También puedes pasar credenciales de autenticación y restringir las herramientas a las que puede llamar el agente.

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `type` | `string` | Sí | Debe ser `"mcp_server"`. |
| `name` | `string` | No | Es un nombre visible para el servidor de MCP. |
| `url` | `string` | No | Es la URL completa del extremo del servidor de MCP. |
| `headers` | `object` | No | Pares clave-valor enviados como encabezados HTTP con cada solicitud al servidor (por ejemplo, tokens de autenticación). |
| `allowed_tools` | `array` | No | Restringe las herramientas del servidor a las que puede llamar el agente. |

#### Uso básico

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Búsqueda de archivos

Otorga acceso al agente a tus propios datos con la herramienta [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Capacidad de dirección y formato

Puedes guiar la respuesta del agente proporcionando instrucciones de formato específicas en tu instrucción. Esto te permite estructurar los informes en secciones y subsecciones específicas, incluir tablas de datos o ajustar el tono para diferentes públicos (p.ej., "técnico", "ejecutivo" o "informal").

Define el formato de salida deseado de forma explícita en el texto de entrada.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Entradas multimodales

Deep Research admite entradas multimodales, incluidas imágenes y documentos (PDFs), lo que permite que el agente analice contenido visual y realice investigaciones basadas en la Web contextualizadas por las entradas proporcionadas.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Comprensión de documentos

La comprensión de documentos permite pasar documentos directamente como entrada multimodal.
El agente analiza los documentos proporcionados y realiza investigaciones basadas en su contenido.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Cómo controlar tareas de larga duración

Deep Research es un proceso de varios pasos que incluye planificación, búsqueda, lectura y escritura. Por lo general, este ciclo supera los límites de tiempo de espera estándar de las llamadas a la API síncronas.

Se requieren agentes para usar `background=True`. La API devuelve un objeto `Interaction` parcial de inmediato. Puedes usar la propiedad `id` para recuperar una interacción para la votación. El estado de interacción pasará de `in_progress` a `completed` o `failed`. Para obtener una guía completa sobre la administración de tareas en segundo plano, consulta [Ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419).

### Transmisión

Deep Research admite la transmisión para recibir actualizaciones en tiempo real sobre el progreso de la investigación, incluidos resúmenes de pensamientos, texto generado e imágenes.
Debes configurar `stream=True` y `background=True`.

Para recibir pasos de razonamiento intermedios (pensamientos) y actualizaciones de progreso, debes habilitar los **resúmenes de pensamiento** configurando `thinking_summaries` en `"auto"` en `agent_config`. Sin esto, es posible que la transmisión solo proporcione los resultados finales.

#### Tipos de eventos de transmisión

| Tipo de evento | Tipo de delta | Descripción |
| --- | --- | --- |
| `step.delta` | `thought` | Es un paso de razonamiento intermedio del agente. |
| `step.delta` | `text` | Es parte del texto final. |
| `step.delta` | `image` | Imagen generada (codificada en base64). |

En el siguiente ejemplo, se inicia una tarea de investigación y se procesa la transmisión con reconexión automática. Realiza un seguimiento de `interaction_id` y `last_event_id` para que, si se interrumpe la conexión (por ejemplo, después del tiempo de espera de 600 segundos), pueda reanudarse desde donde se interrumpió.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Preguntas y conversaciones de seguimiento

Puedes continuar la conversación después de que el agente devuelva el informe final con `previous_interaction_id`. Esto te permite pedir aclaraciones, resúmenes o explicaciones sobre secciones específicas de la investigación sin tener que reiniciar toda la tarea.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Cuándo usar el agente de Deep Research de Gemini

Deep Research es un **agente**, no solo un modelo. Es más adecuado para cargas de trabajo que requieren un enfoque de "analista en una caja" en lugar de un chat de baja latencia.

| Función | Modelos de Gemini estándar | Agente de Deep Research de Gemini |
| --- | --- | --- |
| **Latencia** | Segundos | Minutos (asíncrono/en segundo plano) |
| **Proceso** | Generar -> Resultado | Planificar > Buscar > Leer > Iterar > Generar |
| **Resultado** | Texto conversacional, código y resúmenes breves | Informes detallados, análisis de formato largo y tablas comparativas |
| **Ideal para** | Chatbots, extracción, escritura creativa | Análisis de mercado, diligencia debida, revisiones bibliográficas y análisis de la competencia |

## Configuración del agente

La Investigación profunda usa el parámetro `agent_config` para controlar el comportamiento.
Pásalo como un diccionario con los siguientes campos:

| Campo | Tipo | Predeterminado | Descripción |
| --- | --- | --- | --- |
| `type` | `string` | Obligatorio | Debe ser `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Se establece en `"auto"` para recibir pasos de razonamiento intermedios durante la transmisión. Configúralo en `"none"` para inhabilitarlo. |
| `visualization` | `string` | `"auto"` | Se establece en `"auto"` para habilitar los gráficos y las imágenes generados por el agente. Configúralo en `"off"` para inhabilitarlo. |
| `collaborative_planning` | `boolean` | `false` | Se establece en `true` para habilitar la revisión del plan de varios turnos antes de que comience la investigación. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Disponibilidad y precios

Puedes acceder al agente de Deep Research de Gemini con la API de Interactions en Google AI Studio y la API de Gemini.

Los precios siguen un [modelo de pago por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing-for-agents) basado en los modelos subyacentes de Gemini y las herramientas específicas que utiliza el agente. A diferencia de las solicitudes de chat estándar, en las que una solicitud genera una respuesta, una tarea de Deep Research es un flujo de trabajo de agente. Una sola solicitud activa un bucle autónomo de planificación, búsqueda, lectura y razonamiento.

### Costos estimados

Los costos varían según la profundidad de la investigación requerida. El agente determina de forma autónoma cuánta lectura y búsqueda son necesarias para responder tu instrucción.

- **Deep Research** (`deep-research-preview-04-2026`): Para una búsqueda típica que requiere un análisis moderado, el agente puede usar alrededor de 80 búsquedas, 250,000 tokens de entrada (entre el 50 y el 70% almacenados en caché) y 60,000 tokens de salida.
  - **Total estimado:** De USD 1.00 a USD 3.00 por tarea
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Para un análisis profundo del panorama competitivo o una diligencia debida exhaustiva, el agente puede usar hasta 160 búsquedas, 900,000 tokens de entrada (entre el 50 y el 70% en caché) y 80,000 tokens de salida.
  - **Total estimado:** De USD 3.00 a USD 7.00 por tarea

## Consideraciones de seguridad

Darle acceso a un agente a la Web y a tus archivos privados requiere una consideración cuidadosa de los riesgos de seguridad.

- **Inyección de instrucciones con archivos:** El agente lee el contenido de los archivos que proporcionas. Asegúrate de que los documentos subidos (PDFs, archivos de texto) provengan de fuentes confiables. Un archivo malicioso podría contener texto oculto diseñado para manipular la salida del agente.
- **Riesgos del contenido web:** El agente busca en la Web pública. Si bien implementamos filtros de seguridad sólidos, existe el riesgo de que el agente encuentre y procese páginas web maliciosas. Te recomendamos que revises el `citations` que se proporciona en la respuesta para verificar las fuentes.
- **Exfiltración:** Ten cuidado cuando le pidas al agente que resuma datos internos sensibles si también le permites navegar por la Web.

## Prácticas recomendadas

- **Mensaje para desconocidos:** Indica al agente cómo controlar los datos faltantes.
  Por ejemplo, agrega *"Si no hay cifras específicas disponibles para el 2025, indica explícitamente que son proyecciones o que no están disponibles en lugar de hacer una estimación"* a tu instrucción.
- **Proporciona contexto:** Fundamenta la investigación del agente proporcionando información de antecedentes o restricciones directamente en la instrucción de entrada.
- **Usa la planificación colaborativa:** Para las preguntas complejas, habilita la planificación colaborativa para revisar y definir mejor el plan de investigación antes de la ejecución.
- **Entradas multimodales:** El agente de Deep Research admite entradas multimodales.
  Úsala con precaución, ya que aumenta los costos y el riesgo de desbordamiento de la ventana de contexto.

## Limitaciones

- **Herramientas personalizadas:** Actualmente, no puedes proporcionar herramientas personalizadas de Llamada a funciones, pero puedes usar servidores remotos de MCP (Protocolo de contexto del modelo) con el agente de Investigación profunda.
- **Resultados estructurados:** Actualmente, el agente de Deep Research no admite resultados estructurados.
- **Tiempo máximo de investigación:** El agente de Deep Research tiene un tiempo máximo de investigación de 60 minutos. La mayoría de las tareas deberían completarse en un plazo de 20 minutos.
- **Requisito de la tienda:** La ejecución del agente con `background=True` requiere `store=True`.
- **Búsqueda de Google:** La [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) está habilitada de forma predeterminada y se aplican [restricciones específicas](https://ai.google.dev/gemini-api/terms?hl=es-419#use-restrictions2) a los resultados fundamentados.

## ¿Qué sigue?

- Obtén más información sobre la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419).
- Obtén información para usar tus propios datos con la herramienta [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-14 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-14 (UTC)"],[],[]]
