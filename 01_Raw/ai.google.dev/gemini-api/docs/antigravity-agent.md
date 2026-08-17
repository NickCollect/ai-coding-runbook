---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419
fetched_at: 2026-08-17T02:24:21.222004+00:00
title: "Agente de Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de Antigravity

El agente de Antigravity es un agente administrado de uso general en la API de Gemini. Una sola llamada a la API te proporciona un agente que razona, ejecuta código, administra archivos y navega por la Web dentro de tu propia zona de pruebas segura de Linux, alojada por Google.

Cuenta con la tecnología de Gemini 3.6 Flash y usa el mismo arnés que el IDE de Antigravity. Puedes configurar el modelo de Gemini subyacente con `agent_config`. Disponible a través de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) y [Google AI Studio](https://aistudio.google.com?hl=es-419).

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

Cada llamada puede aprovisionar una zona de pruebas de Linux y comenzar un bucle de uso de herramientas. El agente planifica, actúa, observa los resultados y repite el proceso hasta que se completa la tarea.

- **Ejecución de código:** Ejecuta comandos de Bash, Python y Node.js. Instalar paquetes, ejecutar pruebas y compilar apps
- **Administración de archivos:** Lee, escribe, edita, busca y enumera archivos en el sandbox. Los archivos persisten en todas las interacciones.
- **Acceso a la Web:** Búsqueda de Google y recuperación de URLs para obtener datos
- **Compactación del contexto:** Compactación automática del contexto (se activa con alrededor de 135, 000 tokens) para admitir sesiones de varios turnos y de larga duración sin perder el contexto ni alcanzar los límites de tokens.

Consulta la [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419) para obtener información sobre el uso en varios turnos y la transmisión.

## Herramientas compatibles

De forma predeterminada, el agente tiene acceso a `code_execution`, `google_search` y `url_context`. Las herramientas del sistema de archivos se habilitan automáticamente cuando especificas el parámetro `environment`. También puedes definir **funciones personalizadas** para conectar el agente a tus propias APIs y herramientas. Solo necesitas especificar el parámetro `tools` cuando personalizas o restringes el conjunto predeterminado, o cuando agregas funciones personalizadas.

| Herramienta | Valor del tipo | Descripción |
| --- | --- | --- |
| Ejecución de código | `code_execution` | Ejecuta comandos de shell (bash, Python, Node) con captura de stdout/stderr. |
| Búsqueda de Google | `google_search` | Buscar en la Web pública |
| Contexto de URL | `url_context` | Recuperar y leer páginas web |
| Sistema de archivos | *(se habilita a través de `environment`)* | Leer, escribir, editar, buscar y enumerar archivos en el entorno de pruebas El sistema habilita estas herramientas automáticamente cuando configuras `environment`. |
| Funciones personalizadas | `function` | Define funciones personalizadas que el agente puede solicitar ejecutar. Consulta [Llamadas a funciones](#function-calling). |
| Servidor de MCP remoto | `mcp_server` | Registrar servidores externos del Protocolo de contexto del modelo (MCP) como herramientas Consulta [Servidores de MCP](#mcp-servers). |

Puedes interceptar y validar la ejecución de las herramientas `code_execution` y `filesystem` directamente en la zona de pruebas remota con [enlaces](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=es-419) síncronos.

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

El agente de Antigravity admite entradas multimodales. Actualmente, solo se admiten las entradas `text` y `image`. Las imágenes se deben proporcionar como cadenas intercaladas codificadas en base64 (`data`).

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

La llamada a funciones te permite conectar el agente de Antigravity a APIs y bases de datos externas definiendo herramientas personalizadas que el agente puede invocar. Para conocer los conceptos generales, consulta [Llamada a funciones con la API de Gemini](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=es-419).

En el siguiente ejemplo, se muestra una interacción de 2 turnos. Primero, el agente solicita una llamada a la función `get_weather` personalizada, y el cliente la ejecuta y devuelve el resultado en el segundo turno.

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

Puedes conectar el agente de Antigravity a herramientas externas registrando servidores remotos del Protocolo de contexto del modelo (MCP). El agente admite servidores MCP remotos a través de HTTP con capacidad de transmisión.

Cuando registres un servidor de MCP, debes especificar los siguientes campos en el array `tools`:

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `type` | string | Sí | Debe ser `"mcp_server"`. |
| `name` | string | Sí | Es un identificador único del servidor. Debe ser estrictamente alfanumérico y en minúsculas (coincidir con `^[a-z0-9_-]+$`). |
| `url` | string | Sí | Es la URL del extremo del servidor de MCP remoto. |
| `headers` | objeto | No | Encabezados personalizados (p.ej., de autenticación) que se envían con las solicitudes. |
| `allowed_tools` | array | No | Es la lista de nombres de herramientas que se pueden ejecutar. Si se omite, se permiten todas las herramientas. |

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

## Selección del modelo

En el caso de `antigravity-preview-05-2026`, el modelo predeterminado es **Gemini 3.6 Flash** (`gemini-3.6-flash`). Si omites `agent_config`, el agente usará `gemini-3.6-flash` de forma predeterminada.

Puedes configurar el modelo subyacente de Gemini con `agent_config` para optimizar la velocidad, el costo o la capacidad de razonamiento.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
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
      "agent": "antigravity-preview-05-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

Estos son los valores admitidos para `agent_config.model`:

| Modelo | Valor en `agent_config.model` | Descripción |
| --- | --- | --- |
| **Gemini 3.6 Flash** (predeterminado) | `gemini-3.6-flash` | Modelo equilibrado predeterminado para el razonamiento, la programación y el uso de herramientas. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Modelo Flash de generación anterior para flujos de trabajo generales de agentes. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Modelo ligero optimizado para tareas sensibles a la latencia y el costo. |

Cuando creas un agente administrado con `agents.create`, configuras el modelo de la misma manera pasando `base_agent` y `agent_config`. Ten en cuenta que no puedes anular el modelo en el momento de la interacción para un agente administrado creado con `agents.create`. El modelo está bloqueado según lo que se configuró cuando se creó el agente. Esto garantiza un comportamiento predecible de las llamadas a herramientas, una depuración coherente y el cumplimiento de los límites de seguridad.

## Personaliza el agente

Puedes extender el agente de Antigravity personalizando sus instrucciones, herramientas y entorno. El agente admite un enfoque de personalización nativo del sistema de archivos: puedes montar archivos como `AGENTS.md` para obtener instrucciones y habilidades en `.agents/skills/` directamente en el entorno de pruebas, o pasar la configuración intercalada en el momento de la interacción. Puedes iterar tu configuración intercalada y, luego, guardarla como un agente administrado cuando esté todo listo.

Para obtener todos los detalles sobre cómo compilar agentes personalizados, consulta [Compila agentes administrados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419).

## Ejecución en segundo plano

Las tareas del agente que implican razonamiento de varios pasos, ejecución de código o operaciones de archivos pueden tardar minutos en completarse. Usa `background=True` para ejecutar la interacción de forma asíncrona. La API devuelve de inmediato un ID de interacción que sondea hasta que el estado sea `completed` o `failed`.

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

La ejecución en segundo plano requiere `store=True`, que es el valor predeterminado. Para obtener actualizaciones de progreso en tiempo real durante la ejecución en segundo plano, consulta [Interacciones en segundo plano de transmisión](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=es-419#streaming-background).

Puedes cancelar una interacción en segundo plano en ejecución con el método `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Interacción de varios turnos con ejecución en segundo plano**

Cuando una interacción en segundo plano involucre herramientas con estado (como la ejecución de código en un sandbox), usa el `environment_id` de la interacción completada para continuar en el mismo entorno. Esto garantiza que el agente continúe donde lo dejó con todos los archivos y el estado intactos.

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

| Formulario | Descripción |
| --- | --- |
| `"remote"` | Aprovisiona un entorno de pruebas nuevo con la configuración predeterminada. |
| `"env_abc123"` | Reutiliza un entorno existente por ID y conserva todos los archivos y el estado. |
| `{...}` | `EnvironmentConfig` completo con fuentes personalizadas y reglas de red |

Consulta [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) para obtener detalles sobre las fuentes (Git, GCS, intercaladas), las redes, el ciclo de vida y los límites de recursos.

## Activadores

Los activadores te permiten programar un agente para que se ejecute automáticamente según un programa cron. Un activador vincula un agente, un entorno, una instrucción y una programación en un recurso persistente que se activa sin intervención manual. Cada ejecución reutiliza el mismo entorno, por lo que los archivos creados en una ejecución persisten y son visibles para la siguiente.

### Crear un activador

Crea un activador especificando un programa de cron, una zona horaria y la configuración de interacción. El activador comienza en estado `active` y se activará en el siguiente horario de cron que coincida. Guarda el `id` que se devolvió para administrar el activador en llamadas posteriores.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

La solicitud `CreateTrigger` acepta los siguientes campos:

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `schedule` | string | Sí | Expresión cron (p. ej., `0 * * * *` para cada hora, `0 9 * * 1-5` para las mañanas de los días laborables) |
| `time_zone` | string | Sí | Zona horaria de IANA (p.ej., `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | string | No | Es el nombre legible del activador. |
| `max_consecutive_failures` | integer | No | Es la cantidad máxima de fallas antes de que se pause automáticamente el activador. Valor predeterminado: 5. |
| `execution_timeout_seconds` | integer | No | Tiempo de espera por ejecución en segundos. El valor predeterminado es 600. |
| `interaction` | objeto | Sí | Un `CreateInteractionRequest` que define el agente, la entrada, las herramientas y el entorno. |

La respuesta incluye los siguientes campos clave:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | string | Es el identificador único del activador. Úsala en todas las operaciones posteriores. |
| `status` | string | Estado actual: `active`, `paused` o `disabled`. |
| `next_run_time` | string | Es la marca de tiempo ISO 8601 de la próxima ejecución programada. |
| `consecutive_failure_count` | integer | Cantidad de ejecuciones fallidas consecutivas desde la última ejecución exitosa. |

### Enumera activadores

Recupera todos los activadores asociados con tu proyecto.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Obtén un activador

Recupera la configuración completa y el estado actual de un solo activador.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Cómo detener y reanudar propuestas y líneas de pedido propuestas

Puedes pausar un activador para detener las ejecuciones programadas y reanudarlo para reactivar el programa. La detención no afecta las ejecuciones manuales.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Borra un activador

Quita un activador de forma permanente. No se borra el historial de ejecuciones anteriores.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Cómo ejecutar un activador de inmediato

Activa un disparador a pedido sin esperar la próxima hora programada. Esto funciona incluso si el activador está en pausa.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Enumerar ejecuciones

Consulta el historial de ejecución de un activador. Cada ejecución incluye un `status`, marcas de tiempo, un `interaction_id` que puedes usar para recuperar el resultado completo de la interacción y un `environment_id` que confirma que todas las ejecuciones comparten el mismo sandbox.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Disponibilidad y precios

El agente de Antigravity está disponible en versión preliminar a través de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) en Google AI Studio y la API de Gemini para proyectos de nivel gratuito y de nivel pagado.

Los precios siguen un [modelo de pago por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing-for-agents) basado en los tokens del modelo de Gemini subyacente y las herramientas que usa el agente. A diferencia de una solicitud de chat estándar que produce un solo resultado, una interacción de Antigravity es un flujo de trabajo de agente. Una sola solicitud activa un bucle autónomo de razonamiento, ejecución de herramientas, ejecución de código y administración de archivos. Los proyectos del nivel gratuito incluyen un límite de frecuencia y una cuota de uso gratuitos.

Las interacciones de antigravedad ejecutan bucles autónomos de varios turnos y pueden consumir una cantidad significativa de tokens. Establece [controles de presupuesto](#budget-controls) en tu solicitud para limitar el uso de tokens. También puedes supervisar el progreso en tiempo real con la [transmisión de SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=es-419) o cancelar las solicitudes en ejecución.

### Controles de presupuesto

Además de la [selección del modelo](#model-selection), establece `max_total_tokens` dentro de `agent_config` (con `"type": "antigravity"`) para limitar la cantidad total de tokens (entrada + salida + pensamiento) que puede consumir una interacción.
Los tokens almacenados en caché no se consideran en este límite. Cuando el agente alcanza el límite, la interacción se detiene y se devuelve con `status: "incomplete"`. El límite es el mejor esfuerzo posible: El uso real puede superarlo ligeramente según el momento en que el agente verifique el presupuesto entre los pasos.

Establece el presupuesto en la solicitud de interacción en `agent_config` junto con `agent` y `input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Cómo continuar una interacción incompleta

Cuando una interacción devuelve `status: "incomplete"`, se conservan el trabajo y el contexto del agente. Envía una nueva interacción que haga referencia a la interacción original `id` y `environment_id` para continuar donde se dejó. La nueva interacción obtiene su propio presupuesto de `max_total_tokens`.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Costos estimados

Los costos varían según la complejidad de la tarea. El agente determina de forma autónoma cuántas llamadas a herramientas, ejecuciones de código y operaciones de archivos se necesitan. Las siguientes estimaciones se basan en las ejecuciones.

| Categoría de la tarea | Tokens de entrada | Tokens de salida | Costo habitual |
| --- | --- | --- | --- |
| **Investigación y síntesis de información** | De 100,000 a 500,000 | De 10,000 a 40,000 | USD 0.30 a USD 1.00 |
| **Generación de documentos y contenido** | De 100,000 a 500,000 | De 15,000 a 50,000 | USD 0.30 a USD 1.30 |
| **Diseño de procesos y sistemas** | De 100,000 a 400,000 | De 10,000 a 30,000 | USD 0.25 a USD 0.80 |
| **Procesamiento y análisis de datos** | 300,000 a 3 millones | De 30,000 a 150,000 | USD 0.70 a USD 3.25 |

Por lo general, se almacenan en caché entre el 50% y el 70% de los tokens de entrada. Los flujos de trabajo complejos con muchos llamados a herramientas pueden acumular entre 3 y 5 millones de tokens en una sola interacción, con costos de hasta USD 5.

El **cómputo del entorno** (CPU, memoria, ejecución en zona de pruebas) **no se factura** durante el período de vista previa.

## Limitaciones

- **Estado de la versión preliminar:** El agente de Antigravity y la API de Interactions. Las funciones y los esquemas pueden cambiar.
- **Configuración de generación no admitida:** Los siguientes parámetros no se admiten y devuelven un error 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Salida estructurada:** El agente de Antigravity no admite salidas estructuradas.
- **Herramientas no disponibles:** `file_search`, `computer_use` y `google_maps` aún no son compatibles.
- **Limitaciones de MCP remoto:** No se admite el transporte de eventos enviados por el servidor (SSE) (usa HTTP transmisible). Además, el servidor `name` debe ser estrictamente alfanumérico y en minúsculas (el uso de letras mayúsculas activa un error genérico `400 Bad Request`).
- **Herramienta del sistema de archivos:** No hay una herramienta del sistema de archivos en este momento. Es parte de `environment`.
- **Requisito de la tienda:** La ejecución del agente con `background=True` requiere `store=True`.
- **Llamada a función solo con estado:** La llamada a función solo se admite en el modo con estado. Debes usar `previous_interaction_id` para continuar el turno. No se admite la reconstrucción manual del historial (modo sin estado).
- **Tipos multimodales no admitidos.** Por el momento, no se admiten entradas de audio, video ni documentos. Solo se permiten texto e imágenes.

## ¿Qué sigue?

- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419): Conversaciones de varios turnos y transmisión.
- [Crea agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419): Instrucciones personalizadas, habilidades y guardado de agentes
- [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419): Configuración de zona de pruebas, fuentes y redes
- [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=es-419): Aplican barreras de seguridad y validación de efectos secundarios dentro de la zona de pruebas.
- [Agente de Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419): Tareas de investigación de formato largo.
- [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419): Es la API subyacente.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
