---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419
fetched_at: 2026-06-29T05:29:21.826592+00:00
title: "Agente de Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de Antigravity

El agente de Antigravity es un agente administrado de uso general en la API de Gemini. Una sola llamada a la API te proporciona un agente que razona, ejecuta código, administra archivos y navega por la Web dentro de tu propia zona de pruebas segura de Linux, alojada por Google.

Funciona con Gemini 3.5 Flash y usa el mismo arnés que el IDE de Antigravity. Está disponible a través de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) y [Google AI Studio](https://aistudio.google.com?hl=es-419).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Funciones

Cada llamada puede aprovisionar una zona de pruebas de Linux y comienza un bucle de uso de herramientas. El agente planifica, actúa, observa los resultados y repite hasta que se completa la tarea.

- **Ejecución de código:** Ejecuta comandos de Bash, Python y Node.js. Instala paquetes, ejecuta pruebas y compila apps.
- **Administración de archivos:** Lee, escribe, edita, busca y enumera archivos en la zona de pruebas. Los archivos persisten en todas las interacciones.
- **Acceso web:** Búsqueda de Google y recuperación de URL para obtener datos.
- **Compresión de contexto:** Compresión de contexto automática (activada en ~135, 000 tokens) para admitir sesiones de varios turnos de larga duración sin perder el contexto ni alcanzar los límites de tokens.

Consulta la guía de [inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419) para obtener información sobre el uso de varios turnos y la transmisión.

## Herramientas compatibles

De forma predeterminada, el agente tiene acceso a `code_execution`, `google_search` y `url_context`. Las herramientas del sistema de archivos se habilitan automáticamente cuando especificas el parámetro `environment`. También puedes definir **funciones personalizadas** para conectar el agente a tus propias APIs y herramientas. Solo necesitas especificar el parámetro `tools` cuando personalizas o restringes el conjunto predeterminado, o cuando agregas funciones personalizadas.

| Herramienta | Valor del tipo | Descripción |
| --- | --- | --- |
| Ejecución de código | `code_execution` | Ejecuta comandos de shell (bash, Python, Node) con captura de stdout/stderr. |
| Búsqueda de Google | `google_search` | Busca en la Web pública. |
| Contexto de URL | `url_context` | Recupera y lee páginas web. |
| Sistema de archivos | *(habilitado a través de `environment`)* | Lee, escribe, edita, busca y enumera archivos en la zona de pruebas. No hay un tipo de herramienta independiente; se habilita automáticamente cuando se establece `environment`. |
| Funciones personalizadas | `function` | Define funciones personalizadas que el agente puede solicitar para ejecutar. Consulta [Llamadas a funciones](#function-calling). |
| Servidor de MCP remoto | `mcp_server` | Registra servidores externos del Protocolo de contexto del modelo (MCP) como herramientas. Consulta [Servidores de MCP](#mcp-servers). |

Para limitar el agente a herramientas específicas, pasa solo las que necesites:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Entrada multimodal

El agente de Antigravity admite entradas multimodales. Actualmente, solo se admiten las entradas `text` y `image`. Las imágenes deben proporcionarse como cadenas codificadas en base64 intercaladas (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Llamada a función

La llamada a función te permite conectar el agente de Antigravity a APIs y bases de datos externas mediante la definición de herramientas personalizadas que el agente puede invocar. Para obtener conceptos generales, consulta [Llamada a función con la API de Gemini](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=es-419).

En el siguiente ejemplo, se muestra una interacción de 2 turnos. Primero, el agente solicita una llamada a la función `get_weather` personalizada, y el cliente la ejecuta y muestra el resultado en el segundo turno.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Servidores de MCP

Puedes conectar el agente de Antigravity a herramientas externas registrando servidores remotos del Protocolo de contexto del modelo (MCP). El agente admite servidores remotos de MCP a través de HTTP transmitible.

Cuando registras un servidor de MCP, debes especificar los siguientes campos en el array `tools`:

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `type` | string | Sí | Debe ser `"mcp_server"`. |
| `name` | string | Sí | Un identificador único para el servidor. Debe ser estrictamente alfanumérico y en minúscula (que coincida con `^[a-z0-9_-]+$`). |
| `url` | string | Sí | La URL de extremo del servidor de MCP remoto. |
| `headers` | objeto | No | Encabezados personalizados (p.ej., autenticación) enviados con solicitudes. |
| `allowed_tools` | array | No | Lista de nombres de herramientas que se pueden ejecutar. Si se omite, se permiten todas las herramientas. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Personaliza el agente

Puedes extender el agente de Antigravity personalizando sus instrucciones, herramientas y entorno. El agente admite un enfoque nativo del sistema de archivos para la personalización: puedes activar archivos como `AGENTS.md` para obtener instrucciones y habilidades en `.agents/skills/` directamente en la zona de pruebas o pasar la configuración intercalada en el momento de la interacción. Puedes iterar en tu configuración intercalada y, luego, guardarla como un agente administrado cuando estés listo.

Para obtener detalles completos sobre cómo compilar agentes personalizados, consulta [Compila agentes administrados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419).

## Ejecución en segundo plano

Las tareas del agente que implican razonamiento de varios pasos, ejecución de código o operaciones de archivos pueden tardar minutos en completarse. Usa `background=True` para ejecutar la interacción de forma asíncrona. La API muestra de inmediato un ID de interacción que sondeas hasta que el estado sea `completed` o `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

La ejecución en segundo plano requiere `store=True`, que es el valor predeterminado. Para obtener actualizaciones de progreso en tiempo real durante la ejecución en segundo plano, consulta [Transmite interacciones en segundo plano](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=es-419#streaming-background).

Puedes cancelar una interacción en segundo plano en ejecución con el método `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel({ id: "INTERACTION_ID" });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Varios turnos con ejecución en segundo plano**

Cuando una interacción en segundo plano involucra herramientas con estado (como la ejecución de código en una zona de pruebas), usa el `environment_id` de la interacción completada para continuar en el mismo entorno. Esto garantiza que el agente continúe donde lo dejó con todos los archivos y el estado intactos.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Entornos

Cada llamada crea o reutiliza una zona de pruebas de Linux. El parámetro `environment` toma tres formas:

| Técnica | Descripción |
| --- | --- |
| `"remote"` | Aprovisiona una zona de pruebas nueva con la configuración predeterminada. |
| `"env_abc123"` | Reutiliza un entorno existente por ID, conservando todos los archivos y el estado. |
| `{...}` | `EnvironmentConfig` completo con fuentes personalizadas y reglas de red. |

Consulta [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) para obtener detalles sobre las fuentes (Git, GCS, intercaladas), las redes, el ciclo de vida y los límites de recursos.

## Disponibilidad y precios

El agente de Antigravity está disponible en versión preliminar a través de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) en Google AI Studio y la API de Gemini.

Los precios siguen un [modelo de pago por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing-for-agents) basado en los tokens del modelo de Gemini subyacente y las herramientas que usa el agente. A diferencia de una solicitud de chat estándar que produce una sola salida, una interacción de Antigravity es un flujo de trabajo basado en agentes. Una sola solicitud activa un bucle autónomo de razonamiento, ejecución de herramientas, ejecución de código y administración de archivos.

### Costos estimados

Los costos varían según la complejidad de la tarea. El agente determina de forma autónoma cuántas llamadas a herramientas, ejecuciones de código y operaciones de archivos son necesarias. Las siguientes estimaciones se basan en las ejecuciones.

| Categoría de tarea | Tokens de entrada | Tokens de salida | Costo habitual |
| --- | --- | --- | --- |
| **Investigación y síntesis de información** | 100,000–500,000 | 10,000–40,000 | $0.30–$1.00 |
| **Generación de documentos y contenido** | 100,000–500,000 | 15,000–50,000 | $0.30–$1.30 |
| **Diseño de procesos y sistemas** | 100,000–400,000 | 10,000–30,000 | $0.25–$0.80 |
| **Procesamiento y análisis de datos** | 300,000–3,000,000 | 30,000–150,000 | $0.70–$3.25 |

Por lo general, se almacenan en caché entre el 50% y el 70% de los tokens de entrada. Los flujos de trabajo complejos basados en agentes con muchas llamadas a herramientas pueden acumular entre 3 y 5 millones de tokens en una sola interacción, con costos de hasta ~$5.

**El procesamiento del entorno** (CPU, memoria, ejecución de zona de pruebas) **no se factura** durante el período de versión preliminar.

## Limitaciones

- **Estado de la versión preliminar:** El agente de Antigravity y la API de Interactions. Las funciones y los esquemas pueden cambiar.
- **Configuración de generación no compatible:** No se admiten los siguientes parámetros y muestran un error 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Salida estructurada:** El agente de Antigravity no admite salidas estructuradas.
- **Herramientas no disponibles:** Aún no se admiten `file_search`, `computer_use` y `google_maps`.
- **Limitaciones de MCP remoto:** No se admite el transporte de eventos enviados por el servidor (SSE) (usa HTTP transmitible). Además, el `name` del servidor debe ser estrictamente alfanumérico y en minúscula (el uso de letras mayúsculas activa un error genérico `400 Bad Request`).
- **Herramienta del sistema de archivos:** No hay ninguna herramienta del sistema de archivos en este momento. Forma parte del `environment`.
- **Requisito de almacenamiento:** La ejecución del agente con `background=True` requiere `store=True`.
- **Llamada a función solo con estado:** La llamada a función solo se admite en el modo con estado. Debes usar `previous_interaction_id` para continuar el turno; no se admite la reconstrucción manual del historial (modo sin estado).
- **Tipos multimodales no compatibles.** Por el momento, no se admiten las entradas de audio, video y documentos. Solo se permiten texto e imágenes.

## ¿Qué sigue?

- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419): Conversaciones y transmisión de varios turnos.
- [Compila agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419): Instrucciones, habilidades y agentes de guardado personalizados.
- [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419): Configuración de zona de pruebas, fuentes y redes.
- [Agente de Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419): Tareas de investigación de formato largo.
- [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419): La API subyacente.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-26 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-26 (UTC)"],[],[]]
