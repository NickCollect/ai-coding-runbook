---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419
fetched_at: 2026-06-22T06:28:06.468667+00:00
title: "Gu\u00eda de inicio r\u00e1pido de Managed Agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Guía de inicio rápido de Managed Agents

En esta guía, se explica cómo crear y usar agentes administrados en la API de Gemini con el [agente Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=es-419). Realizarás tu primera llamada al agente, continuarás una conversación de varios turnos, transmitirás la respuesta, descargarás archivos del sandbox y trabajarás con el agente administrado Antigravity.

## Ejecuta tu primera interacción con el agente

Una sola llamada a la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419) aprovisiona una zona de pruebas de Linux, ejecuta el bucle del agente y devuelve el resultado. Definirás tres parámetros:

- Pasa `agent` como `"antigravity-preview-05-2026",`, que es la versión actual de nuestro agente administrado predefinido y de uso general.
- Define `environment="remote"` para aprovisionar un entorno de zona de pruebas nuevo y actualizado.
- Crea una entrada que defina lo que quieres que haga el agente.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

La respuesta devuelve un objeto `Interaction`. Almacena `interaction.id` y `interaction.environment_id` para continuar la conversación en el mismo entorno de pruebas. Usa `interaction.output_text` para acceder a la respuesta final del agente. `interaction.steps` enumera cada paso que siguió el agente (razonamiento, llamadas a herramientas, ejecución de código).

## Continuar la conversación (varios turnos)

La API hace un seguimiento de dos dimensiones de estado independientes:

- **Contexto de la conversación:** Historial de chat, registro de razonamiento, uso de herramientas y uso de `previous_interaction_id`.
- [**Estado del entorno:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) archivos, paquetes instalados y estado de la zona de pruebas, con `environment`.

Pasa ambos en su lugar respectivo para reanudar:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Los archivos del turno 1 (`fibonacci.txt`) persisten en el turno 2. El agente también retiene el contexto de la conversación.

Puedes combinar estas opciones de forma independiente:

- **Borrar conversación y conservar archivos:** Omite `previous_interaction_id` y solo pasa el ID del entorno con `environment` para una conversación nueva en el mismo espacio de trabajo.
- **Mantener la conversación, lugar de trabajo nuevo:** Pasa `previous_interaction_id` y establece `environment="remote"` para un entorno de pruebas nuevo.

### Compactación automática del contexto

En las conversaciones de varios turnos y de larga duración, el historial sin procesar de los pasos de razonamiento, las llamadas a herramientas y el contenido de archivos grandes puede crecer rápidamente y consumir una gran cantidad de espacio de contexto. Para evitar errores de límite de tokens y mantener el enfoque del agente (evitar la "pérdida de contexto"), la API de Managed Agents incluye un paso de compactación de contexto nativo de alrededor de 135 000 tokens. Esto ocurre de forma automática.

## Transmite la respuesta

En el caso de las tareas de larga duración, puedes transmitir la respuesta para ver el trabajo del agente en tiempo real:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

La transmisión devuelve un iterable de deltas de pasos, que son actualizaciones incrementales de texto, tokens de razonamiento y llamadas a herramientas. Obtén más información para transmitir respuestas en la [guía de transmisión](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=es-419).

## Descarga archivos del entorno

Cuando el agente crea archivos dentro del sandbox. Descárgalos con la API de Files a través de una solicitud HTTP directa (aún no hay un método del SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Cómo guardar un agente administrado

En los pasos anteriores, usamos el agente Antigravity predeterminado y lo personalizamos de forma intercalada. Una vez que hayas iterado en tu configuración (instrucciones, habilidades y entorno), puedes guardarla como un agente administrado. Esto te permite invocarlo por ID sin repetir la configuración.

Cuando guardas un agente, defines un `base_environment` (ya sea desde fuentes o bifurcando un entorno existente). El agente usará este entorno para cada interacción nueva.

**Desde fuentes:** Define fuentes intercaladas o desde otras fuentes, como GitHub o Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Invoca el agente administrado

Una vez que guardes un agente administrado, podrás invocarlo por ID. Cada invocación bifurca el entorno base, por lo que cada ejecución comienza de forma limpia:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## ¿Qué sigue?

- [Agente de antigravedad](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419): Capacidades, herramientas compatibles, entrada multimodal, precios y limitaciones.
- [Cómo crear agentes administrados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419): Extiende Antigravity con tus propias instrucciones, habilidades y datos.
- [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419): Fuentes, redes, ciclo de vida y límites de recursos
- [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419): Es la API subyacente para los modelos y los agentes.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-19 (UTC)"],[],[]]
