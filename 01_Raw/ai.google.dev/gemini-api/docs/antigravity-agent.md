---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de
fetched_at: 2026-07-06T05:06:07.087473+00:00
title: "Antigravity-Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Antigravity-Agent

Der Antigravity-Agent ist ein verwalteter Agent für allgemeine Zwecke in der Gemini API. Mit einem einzigen API-Aufruf erhalten Sie einen Agenten, der Schlussfolgerungen zieht, Code ausführt, Dateien verwaltet und im Web surft – alles in Ihrer eigenen sicheren Linux-Sandbox, die von Google gehostet wird.

Er basiert auf Gemini 3.5 Flash und verwendet dieselbe Harness wie die Antigravity IDE. Verfügbar über die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) und [Google AI Studio](https://aistudio.google.com?hl=de).

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

## Leistungsspektrum

Bei jedem Aufruf kann eine Linux-Sandbox bereitgestellt und eine Toolnutzungsschleife gestartet werden. Der Agent plant, handelt, beobachtet die Ergebnisse und wiederholt den Vorgang, bis die Aufgabe erledigt ist.

- **Code-Ausführung**:Führen Sie Bash-, Python- und Node.js-Befehle aus. Installieren Sie Pakete, führen Sie Tests aus und erstellen Sie Apps.
- **Dateiverwaltung**:Lesen, schreiben, bearbeiten, suchen und listen Sie Dateien in der Sandbox auf. Dateien bleiben über Interaktionen hinweg erhalten.
- **Webzugriff**:Google Suche und URL-Abruf für Daten.
- **Kontextkomprimierung**:Automatische Kontextkomprimierung (bei ca. 135.000 Tokens ausgelöst) zur Unterstützung von langen Sitzungen mit mehreren Unterhaltungsrunden, ohne den Kontext zu verlieren oder Tokenlimits zu erreichen.

Weitere Informationen zur Verwendung mit mehreren Unterhaltungsrunden und zum Streaming finden Sie in der [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de).

## Unterstützte Tools

Standardmäßig hat der Agent Zugriff auf `code_execution`, `google_search` und `url_context`. Dateisystemtools werden automatisch aktiviert, wenn Sie den Parameter `environment` angeben. Sie können auch **benutzerdefinierte Funktionen** definieren, um den Agenten mit Ihren eigenen APIs und Tools zu verbinden. Sie müssen den Parameter `tools` nur angeben, wenn Sie die Standardeinstellungen anpassen oder einschränken oder benutzerdefinierte Funktionen hinzufügen.

| Tool | Typwert | Beschreibung |
| --- | --- | --- |
| Codeausführung | `code_execution` | Führen Sie Shell-Befehle (Bash, Python, Node) mit der Erfassung von stdout/stderr aus. |
| Google Suche | `google_search` | Im öffentlichen Web suchen. |
| URL-Kontext | `url_context` | Webseiten abrufen und lesen. |
| Dateisystem | *(über `environment` aktiviert)* | Lesen, schreiben, bearbeiten, suchen und listen Sie Dateien in der Sandbox auf. Kein separater Tooltyp. Wird automatisch aktiviert, wenn `environment` festgelegt ist. |
| Benutzerdefinierte Funktionen | `function` | Definieren Sie benutzerdefinierte Funktionen, die der Agent ausführen kann. Weitere Informationen finden Sie unter [Funktionsaufrufe](#function-calling). |
| Remote-MCP-Server | `mcp_server` | Registrieren Sie externe MCP-Server (Model Context Protocol) als Tools. Weitere Informationen finden Sie unter [MCP-Servern](#mcp-servers). |

Wenn Sie den Agenten auf bestimmte Tools beschränken möchten, übergeben Sie nur die benötigten Tools:

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

## Multimodale Eingabe

Der Antigravity-Agent unterstützt multimodale Eingaben. Derzeit werden nur `text`- und `image`-Eingaben unterstützt. Bilder müssen als Inline-Strings im Base64-Format (`data`) angegeben werden.

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

## Funktionsaufrufe

Mit Funktionsaufrufen können Sie den Antigravity-Agenten mit externen APIs und Datenbanken verbinden, indem Sie benutzerdefinierte Tools definieren, die der Agent aufrufen kann. Allgemeine Informationen finden Sie unter [Funktionsaufrufe mit der Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de).

Das folgende Beispiel zeigt eine Interaktion mit zwei Unterhaltungsrunden. Der Agent fordert zuerst einen benutzerdefinierten `get_weather`-Funktionsaufruf an. Der Client führt ihn aus und gibt das Ergebnis in der zweiten Unterhaltungsrunde zurück.

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

## MCP-Server

Sie können den Antigravity-Agenten mit externen Tools verbinden, indem Sie Remote-MCP-Server (Model Context Protocol) registrieren. Der Agent unterstützt Remote-MCP-Server über streamfähiges HTTP.

Wenn Sie einen MCP-Server registrieren, müssen Sie die folgenden Felder im Array `tools` angeben:

| Feld | Typ | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| `type` | String | Ja | Muss `"mcp_server"` sein. |
| `name` | String | Ja | Eine eindeutige Kennung für den Server. Muss ausschließlich Kleinbuchstaben und alphanumerische Zeichen enthalten (entsprechend `^[a-z0-9_-]+$`). |
| `url` | String | Ja | Die Endpunkt-URL des Remote-MCP-Servers. |
| `headers` | Objekt | Nein | Benutzerdefinierte Header (z.B. für die Authentifizierung), die mit Anfragen gesendet werden. |
| `allowed_tools` | Array | Nein | Liste der Toolnamen, die ausgeführt werden dürfen. Wenn nicht angegeben, sind alle Tools zulässig. |

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

## Agent anpassen

Sie können den Antigravity-Agenten erweitern, indem Sie seine Anweisungen, Tools und Umgebung anpassen. Der Agent unterstützt einen dateisystemnativen Ansatz für die Anpassung: Sie können Dateien wie `AGENTS.md` für Anweisungen und Fähigkeiten unter `.agents/skills/` direkt in die Sandbox einbinden oder die Konfiguration zur Interaktionszeit inline übergeben. Sie können Ihre Konfiguration inline durchgehen und sie dann als verwalteten Agenten speichern, wenn Sie bereit sind.

Ausführliche Informationen zum Erstellen benutzerdefinierter Agenten finden Sie unter [Verwaltete Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de).

## Ausführung im Hintergrund

Agentenaufgaben, die mehrstufige Problemlösung, Code-Ausführung oder Dateioperationen umfassen, können mehrere Minuten dauern. Verwenden Sie `background=True`, um die Interaktion asynchron auszuführen. Die API gibt sofort eine Interaktions-ID zurück, die Sie abfragen, bis der Status `completed` oder `failed` ist.

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

Für die Ausführung im Hintergrund ist `store=True` erforderlich. Dies ist die Standardeinstellung. Informationen zu Echtzeit-Fortschrittsaktualisierungen während der Ausführung im Hintergrund finden Sie unter [Streaming von Hintergrundinteraktionen](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=de#streaming-background).

Sie können eine laufende Hintergrundinteraktion mit der Methode `cancel` abbrechen.

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

**Mehrere Unterhaltungsrunden mit Ausführung im Hintergrund**

Wenn eine Hintergrundinteraktion zustandsbehaftete Tools (z. B. Code-Ausführung in einer Sandbox) umfasst, verwenden Sie die `environment_id` aus der abgeschlossenen Interaktion, um in derselben Umgebung fortzufahren. So kann der Agent mit allen Dateien und dem gesamten Zustand an der Stelle fortfahren, an der er aufgehört hat.

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

## Umgebungen

Bei jedem Aufruf wird eine Linux-Sandbox erstellt oder wiederverwendet. Der Parameter `environment` hat drei Formen:

| Formular | Beschreibung |
| --- | --- |
| `"remote"` | Eine neue Sandbox mit Standardeinstellungen bereitstellen. |
| `"env_abc123"` | Eine vorhandene Umgebung anhand der ID wiederverwenden, wobei alle Dateien und der gesamte Zustand beibehalten werden. |
| `{...}` | Vollständige `EnvironmentConfig` mit benutzerdefinierten Quellen und Netzwerkregeln. |

Weitere Informationen zu Quellen (Git, GCS, Inline), Netzwerken, Lebenszyklus und Ressourcenlimits finden Sie unter [Umgebungen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de).

## Verfügbarkeit und Preisgestaltung

Der Antigravity-Agent ist in der Vorabversion über die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) in Google AI Studio und der Gemini API verfügbar.

Die Preise basieren auf einem [Pay-as-you-go-Modell](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing-for-agents), das auf den zugrunde liegenden Gemini-Modelltokens und den vom Agenten verwendeten Tools basiert. Im Gegensatz zu einer Standard-Chatanfrage, die eine einzelne Ausgabe erzeugt, ist eine Antigravity-Interaktion ein Agentenworkflow. Eine einzelne Anfrage löst eine autonome Schleife aus Schlussfolgerungen, Toolausführung, Codeausführung und Dateiverwaltung aus.

### Geschätzte Kosten

Die Kosten variieren je nach Komplexität der Aufgabe. Der Agent bestimmt autonom, wie viele Toolaufrufe, Codeausführungen und Dateivorgänge erforderlich sind. Die folgenden Schätzungen basieren auf Ausführungen.

| Aufgabenkategorie | Eingabetokens | Ausgabetokens | Typische Kosten |
| --- | --- | --- | --- |
| **Recherche und Informationssynthese** | 100.000–500.000 | 10.000–40.000 | 0,30–1,00 $ |
| **Dokument- und Content-Generierung** | 100.000–500.000 | 15.000–50.000 | 0,30–1,30 $ |
| **Prozess- und Systemdesign** | 100.000–400.000 | 10.000–30.000 | 0,25–0,80 $ |
| **Datenverarbeitung und ‑analyse** | 300.000–3.000.000 | 30.000–150.000 | 0,70–3,25 $ |

50–70% der Eingabetokens werden in der Regel im Cache gespeichert. Bei komplexen Agentenworkflows mit vielen Toolaufrufen können in einer einzigen Interaktion 3–5 Millionen Tokens anfallen, was Kosten von bis zu ca. 5 $ verursachen kann.

Die **Umgebungsberechnung** (CPU, Arbeitsspeicher, Sandbox-Ausführung) wird während des Vorabzeitraums **nicht in Rechnung gestellt**.

## Beschränkungen

- **Vorabstatus**:Der Antigravity-Agent und die Interactions API. Funktionen und Schemas können sich ändern.
- **Nicht unterstützte Generierungskonfiguration**:Die folgenden Parameter werden nicht unterstützt und geben einen 400-Fehler zurück: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Strukturierte Ausgabe**:Der Antigravity-Agent unterstützt keine strukturierten Ausgaben.
- **Nicht verfügbare Tools**:`file_search`, `computer_use` und `google_maps` werden noch nicht unterstützt.
- **Beschränkungen für Remote-MCP**:Der Transport von Server-Sent Events (SSE) wird nicht unterstützt. Verwenden Sie stattdessen streamfähiges HTTP. Außerdem muss der Server `name` ausschließlich Kleinbuchstaben und alphanumerische Zeichen enthalten. Wenn Sie Großbuchstaben verwenden, wird ein generischer Fehler `400 Bad Request` ausgelöst.
- **Dateisystemtool**:Derzeit ist kein Dateisystemtool verfügbar. Es ist Teil der `environment`.
- **Speicheranforderung**:Für die Agentenausführung mit `background=True` ist `store=True` erforderlich.
- **Funktionsaufrufe nur mit Zustand**:Funktionsaufrufe werden nur im zustandsbehafteten Modus unterstützt. Sie müssen `previous_interaction_id` verwenden, um die Unterhaltungsrunde fortzusetzen. Das manuelle Rekonstruieren des Verlaufs (zustandslose Modus) wird nicht unterstützt.
- **Nicht unterstützte multimodale Typen** Audio-, Video- und Dokumenteingaben werden derzeit nicht unterstützt. Nur Text und Bilder sind zulässig.

## Nächste Schritte

- [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de): Unterhaltungen mit mehreren Unterhaltungsrunden und Streaming.
- [Benutzerdefinierte Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de): benutzerdefinierte Anweisungen, Fähigkeiten und Agenten speichern.
- [Umgebungen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de): Sandbox-Konfiguration, Quellen, Netzwerke.
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=de): Aufgaben für umfangreiche Recherchen.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de): die zugrunde liegende API.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-26 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-26 (UTC)."],[],[]]
