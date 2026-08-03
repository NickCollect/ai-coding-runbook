---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de
fetched_at: 2026-08-03T04:35:00.174752+00:00
title: "Antigravity-Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Antigravity-Agent

Der Antigravity-Agent ist ein verwalteter Mehrzweck-Agent in der Gemini API. Mit einem einzigen API-Aufruf erhalten Sie einen Agenten, der in Ihrer eigenen sicheren Linux-Sandbox, die von Google gehostet wird, Schlussfolgerungen zieht, Code ausführt, Dateien verwaltet und im Web surft.

Es basiert auf Gemini 3.6 Flash und verwendet dieselbe Harness wie die Antigravity IDE. Sie können das zugrunde liegende Gemini-Modell mit `agent_config` konfigurieren. Über die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) und [Google AI Studio](https://aistudio.google.com?hl=de) verfügbar.

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

Bei jedem Aufruf kann eine Linux-Sandbox bereitgestellt und ein Tool-Nutzungszyklus gestartet werden. Der Agent plant, handelt, beobachtet die Ergebnisse und wiederholt den Vorgang, bis die Aufgabe erledigt ist.

- **Code-Ausführung**:Bash-, Python- und Node.js-Befehle ausführen. Pakete installieren, Tests ausführen, Apps erstellen
- **Dateiverwaltung**:Dateien in der Sandbox lesen, schreiben, bearbeiten, suchen und auflisten. Dateien bleiben über Interaktionen hinweg erhalten.
- **Webzugriff**:Google Suche und Abrufen von URLs für Daten.
- **Kontextverdichtung**:Automatische Kontextverdichtung (wird bei etwa 135.000 Tokens ausgelöst), um lange Mehrfachdialog-Sitzungen zu unterstützen, ohne dass der Kontext verloren geht oder Tokenlimits erreicht werden.

Informationen zur Verwendung in mehreren Durchgängen und zum Streaming finden Sie in der [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de).

## Unterstützte Tools

Standardmäßig hat der Agent Zugriff auf `code_execution`, `google_search` und `url_context`. Dateisystemtools werden automatisch aktiviert, wenn Sie den Parameter `environment` angeben. Sie können auch **benutzerdefinierte Funktionen** definieren, um den Agent mit Ihren eigenen APIs und Tools zu verbinden. Sie müssen den Parameter `tools` nur angeben, wenn Sie den Standardsatz anpassen oder einschränken oder benutzerdefinierte Funktionen hinzufügen möchten.

| Tool | Typwert | Beschreibung |
| --- | --- | --- |
| Codeausführung | `code_execution` | Shell-Befehle (Bash, Python, Node) mit stdout/stderr-Erfassung ausführen. |
| Google Suche | `google_search` | Im öffentlichen Web suchen |
| URL-Kontext | `url_context` | Webseiten abrufen und lesen |
| Dateisystem | *(über `environment` aktiviert)* | Dateien in der Sandbox lesen, schreiben, bearbeiten, suchen und auflisten Das System aktiviert diese Tools automatisch, wenn Sie `environment` festlegen. |
| Benutzerdefinierte Funktionen | `function` | Definieren Sie benutzerdefinierte Funktionen, die der Agent ausführen kann. [Weitere Informationen](#function-calling) |
| Remote-MCP-Server | `mcp_server` | Externe MCP-Server (Model Context Protocol) als Tools registrieren [Weitere Informationen](#mcp-servers) |

Sie können die Ausführung von `code_execution`- und `filesystem`-Tools direkt in der Remote-Sandbox mit synchronen [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=de) abfangen und validieren.

Wenn Sie den Agent auf bestimmte Tools beschränken möchten, übergeben Sie nur die benötigten:

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

Der Antigravity-Agent unterstützt multimodale Eingaben. Derzeit werden nur `text`- und `image`-Eingaben unterstützt. Bilder müssen als Inline-Base64-codierte Strings (`data`) angegeben werden.

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

Mit Funktionsaufrufen können Sie den Antigravity-Agenten mit externen APIs und Datenbanken verbinden, indem Sie benutzerdefinierte Tools definieren, die der Agent aufrufen kann. Allgemeine Konzepte finden Sie unter [Funktionsaufrufe mit der Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de).

Das folgende Beispiel zeigt eine Interaktion mit zwei Zügen. Der Agent fordert zuerst einen benutzerdefinierten `get_weather`-Funktionsaufruf an. Der Client führt ihn aus und gibt das Ergebnis im zweiten Zug zurück.

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

Sie können den Antigravity-Agent mit externen Tools verbinden, indem Sie Remote-MCP-Server (Model Context Protocol) registrieren. Der Agent unterstützt Remote-MCP-Server über streamfähiges HTTP.

Wenn Sie einen MCP-Server registrieren, müssen Sie die folgenden Felder im `tools`-Array angeben:

| Feld | Typ | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| `type` | String | Ja | Muss `"mcp_server"` lauten. |
| `name` | String | Ja | Eine eindeutige Kennung für den Server. Muss ausschließlich aus Kleinbuchstaben und alphanumerischen Zeichen bestehen (entsprechend `^[a-z0-9_-]+$`). |
| `url` | String | Ja | Die Endpunkt-URL des Remote-MCP-Servers. |
| `headers` | Objekt | Nein | Benutzerdefinierte Header (z.B. zur Authentifizierung), die mit Anfragen gesendet werden. |
| `allowed_tools` | Array | Nein | Liste der Toolnamen, die ausgeführt werden dürfen. Wenn weggelassen, sind alle Tools zulässig. |

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

## Modellauswahl

Für `antigravity-preview-05-2026` ist das Standardmodell **Gemini 3.6 Flash** (`gemini-3.6-flash`). Wenn Sie `agent_config` weglassen, wird standardmäßig `gemini-3.6-flash` verwendet.

Sie können das zugrunde liegende Gemini-Modell mit `agent_config` konfigurieren, um es für Geschwindigkeit, Kosten oder logische Schlussfolgerungen zu optimieren.

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

Folgende Werte werden für `agent_config.model` unterstützt:

| Modell | Wert in `agent_config.model` | Beschreibung |
| --- | --- | --- |
| **Gemini 3.6 Flash** (Standard) | `gemini-3.6-flash` | Standardmodell für logisches Denken, Programmieren und die Verwendung von Tools. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Flash-Modell der vorherigen Generation für allgemeine agentische Workflows. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Leichtgewichtiges Modell, das für Aufgaben mit niedriger Latenz und kostensensitive Aufgaben optimiert ist. |

Wenn Sie einen verwalteten Agenten mit `agents.create` erstellen, konfigurieren Sie das Modell auf genau dieselbe Weise, indem Sie `base_agent` und `agent_config` übergeben. Hinweis: Sie können das Modell bei der Interaktion nicht für einen verwalteten Agenten überschreiben, der mit `agents.create` erstellt wurde. Das Modell ist auf die Einstellungen festgelegt, die beim Erstellen des Agents festgelegt wurden. So wird ein vorhersehbares Verhalten beim Aufrufen von Tools, eine konsistente Fehlersuche und die Einhaltung von Sicherheitsgrenzen gewährleistet.

## Agent anpassen

Sie können den Antigravity-Agent erweitern, indem Sie seine Anweisungen, Tools und Umgebung anpassen. Der Agent unterstützt einen dateisystemnativen Ansatz für die Anpassung: Sie können Dateien wie `AGENTS.md` für Anweisungen und Skills unter `.agents/skills/` direkt in die Sandbox einbinden oder die Konfiguration zur Interaktionszeit inline übergeben. Sie können Ihre Konfiguration direkt bearbeiten und sie dann als verwalteten Agenten speichern, wenn Sie fertig sind.

Ausführliche Informationen zum Erstellen benutzerdefinierter KI-Agenten finden Sie unter [Verwaltete KI-Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de).

## Ausführung im Hintergrund

Agent-Tasks, die mehrstufige Problemlösung, Code-Ausführung oder Dateioperationen umfassen, können mehrere Minuten dauern. Verwenden Sie `background=True`, um die Interaktion asynchron auszuführen. Die API gibt sofort eine Interaktions-ID zurück, die Sie abfragen, bis der Status `completed` oder `failed` ist.

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

Für die Ausführung im Hintergrund ist `store=True` erforderlich. Dies ist die Standardeinstellung. Informationen zu Echtzeit-Fortschrittsaktualisierungen während der Hintergrundausführung finden Sie unter [Hintergrundinteraktionen streamen](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=de#streaming-background).

Sie können eine laufende Hintergrundinteraktion mit der Methode `cancel` abbrechen.

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

**Mehrfachdialog mit Hintergrundausführung**

Wenn bei einer Hintergrundinteraktion zustandsbehaftete Tools (z. B. die Codeausführung in einer Sandbox) verwendet werden, verwenden Sie die `environment_id` aus der abgeschlossenen Interaktion, um in derselben Umgebung fortzufahren. So kann der KI-Agent mit allen Dateien und dem gesamten Status dort weitermachen, wo er aufgehört hat.

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

Bei jedem Aufruf wird eine Linux-Sandbox erstellt oder wiederverwendet. Der Parameter `environment` kann drei Formen annehmen:

| Formular | Beschreibung |
| --- | --- |
| `"remote"` | Stellen Sie eine neue Sandbox mit Standardeinstellungen bereit. |
| `"env_abc123"` | Eine vorhandene Umgebung anhand der ID wiederverwenden, wobei alle Dateien und der Status beibehalten werden. |
| `{...}` | Vollständige `EnvironmentConfig` mit benutzerdefinierten Quellen und Netzwerkregeln. |

Weitere Informationen zu Quellen (Git, GCS, Inline), Netzwerken, Lebenszyklus und Ressourcenlimits finden Sie unter [Umgebungen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de).

## Trigger

Mit Triggern können Sie einen Agent so planen, dass er automatisch nach einem Cron-Zeitplan ausgeführt wird. Ein Trigger verknüpft einen Agent, eine Umgebung, einen Prompt und einen Zeitplan zu einer persistenten Ressource, die ohne manuellen Eingriff ausgelöst wird. Bei jeder Ausführung wird dieselbe Umgebung wiederverwendet. Dateien, die in einem Lauf erstellt werden, bleiben also erhalten und sind für den nächsten Lauf sichtbar.

### Trigger erstellen

Erstellen Sie einen Trigger, indem Sie einen Cronjob-Zeitplan, eine Zeitzone und die Interaktionskonfiguration angeben. Der Trigger beginnt im Status `active` und wird bei der nächsten passenden Cron-Zeit ausgelöst. Speichern Sie die zurückgegebene `id`, um den Trigger in nachfolgenden Aufrufen zu verwalten.

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

Die `CreateTrigger`-Anfrage akzeptiert die folgenden Felder:

| Feld | Typ | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| `schedule` | String | Ja | Cron-Ausdruck (z.B. `0 * * * *` für stündlich, `0 9 * * 1-5` für Wochentagmorgens). |
| `time_zone` | String | Ja | IANA-Zeitzone (z.B. `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | String | Nein | Für Menschen lesbarer Name des Triggers. |
| `max_consecutive_failures` | integer | Nein | Maximale Anzahl von Fehlern, bevor der Trigger automatisch pausiert wird. Standard: 5. |
| `execution_timeout_seconds` | integer | Nein | Zeitlimit pro Ausführung in Sekunden. Standardwert: 600 |
| `interaction` | Objekt | Ja | Ein `CreateInteractionRequest`, das den KI-Agenten, die Eingabe, die Tools und die Umgebung definiert. |

Die Antwort umfasst die folgenden Schlüsselfelder:

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `id` | String | Eindeutige Kennung für den Trigger. Verwenden Sie diese in allen nachfolgenden Vorgängen. |
| `status` | String | Aktueller Status: `active`, `paused` oder `disabled`. |
| `next_run_time` | String | ISO 8601-Zeitstempel der nächsten geplanten Ausführung. |
| `consecutive_failure_count` | integer | Anzahl der aufeinanderfolgenden fehlgeschlagenen Ausführungen seit dem letzten Erfolg. |

### Trigger auflisten

Alle Trigger abrufen, die mit Ihrem Projekt verknüpft sind.

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

### Trigger erhalten

Ruft die vollständige Konfiguration und den aktuellen Status eines einzelnen Triggers ab.

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

### Pausieren und fortsetzen

Sie können einen Trigger pausieren, um geplante Ausführungen zu beenden, und ihn fortsetzen, um den Zeitplan zu reaktivieren. Das Pausieren hat keine Auswirkungen auf manuelle Ausführungen.

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

### Trigger löschen

Trigger endgültig entfernen Der bisherige Ausführungsverlauf wird nicht gelöscht.

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

### Trigger sofort ausführen

Sie können einen Trigger bei Bedarf auslösen, ohne auf den nächsten geplanten Zeitpunkt warten zu müssen. Das funktioniert auch dann, wenn der Trigger pausiert ist.

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

### Ausführungen auflisten

Ausführungsverlauf für einen Trigger ansehen Jede Ausführung enthält eine `status`, Zeitstempel, eine `interaction_id`, mit der Sie die vollständige Interaktionsausgabe abrufen können, und eine `environment_id`, die bestätigt, dass alle Ausführungen dieselbe Sandbox verwenden.

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

## Verfügbarkeit und Preisgestaltung

Der Antigravity-Agent ist in der Vorabversion über die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) in Google AI Studio und die Gemini API für Projekte mit kostenlosem und kostenpflichtigem Abo verfügbar.

Die Preise basieren auf einem [Pay-as-you-go-Modell](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing-for-agents), das auf den zugrunde liegenden Gemini-Modelltokens und den vom Agent verwendeten Tools basiert. Im Gegensatz zu einer Standard-Chatanfrage, die eine einzelne Ausgabe erzeugt, ist eine Antigravity-Interaktion ein agentenbasierter Workflow. Eine einzelne Anfrage löst einen autonomen Zyklus aus, der aus Schlussfolgerungen, Ausführung von Tools, Ausführung von Code und Dateiverwaltung besteht. Projekte der kostenlosen Stufe haben ein kostenloses Ratenlimit und Nutzungskontingent.

Antigravity-Interaktionen werden in autonomen Schleifen mit mehreren Zügen ausgeführt und können eine erhebliche Anzahl von Tokens verbrauchen. Legen Sie [Budgetkontrollen](#budget-controls) für Ihre Anfrage fest, um die Tokennutzung zu begrenzen. Sie können den Fortschritt auch in Echtzeit mit [SSE-Streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=de) verfolgen oder laufende Anfragen abbrechen.

### Budgetkontrollen

Zusätzlich zur [Modellauswahl](#model-selection) können Sie `max_total_tokens` in `agent_config` (mit `"type": "antigravity"`) festlegen, um die Gesamtzahl der Tokens (Eingabe + Ausgabe + Thinking-Modus) zu begrenzen, die für eine Interaktion verwendet werden können.
Zwischengespeicherte Tokens werden nicht auf dieses Limit angerechnet. Wenn der Agent das Limit erreicht, wird die Interaktion beendet und mit `status: "incomplete"` zurückgegeben. Das Limit ist eine Schätzung. Die tatsächliche Nutzung kann es geringfügig überschreiten, je nachdem, wann der Agent das Budget zwischen den Schritten prüft.

Legen Sie das Budget für die Interaktionsanfrage in `agent_config` zusammen mit `agent` und `input` fest.

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

#### Unvollständige Interaktion fortsetzen

Wenn bei einer Interaktion `status: "incomplete"` zurückgegeben wird, bleiben die Arbeit und der Kontext des Agenten erhalten. Senden Sie eine neue Interaktion, die sich auf die ursprüngliche Interaktion `id` und `environment_id` bezieht, um dort fortzufahren, wo sie aufgehört hat. Die neue Interaktion erhält ein eigenes `max_total_tokens`-Budget.

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

### Geschätzte Kosten

Die Kosten variieren je nach Komplexität der Aufgabe. Der Agent bestimmt autonom, wie viele Tool-Aufrufe, Codeausführungen und Dateivorgänge erforderlich sind. Die folgenden Schätzungen basieren auf Läufen.

| Aufgabenkategorie | Eingabetokens | Ausgabetokens | Normalpreis |
| --- | --- | --- | --- |
| **Recherche und Informationssynthese** | 100.000–500.000 | 10.000–40.000 | 0,30 $ bis 1,00 $ |
| **Dokument- und Inhaltserstellung** | 100.000–500.000 | 15.000–50.000 | 0,30 $ bis 1,30 $ |
| **Prozess- und Systemdesign** | 100.000–400.000 | 10.000–30.000 | 0,25 $ bis 0,80 $ |
| **Datenverarbeitung und -analyse** | 300.000–3 Mio. | 30.000–150.000 | 0,70 $ bis 3,25 $ |

In der Regel werden 50–70% der Eingabetokens im Cache gespeichert. Bei komplexen Agent-Workflows mit vielen Tool-Aufrufen können sich in einer einzelnen Interaktion 3 bis 5 Millionen Tokens ansammeln, was Kosten von bis zu 5 $ verursacht.

**Umgebungsberechnung** (CPU, Arbeitsspeicher, Sandbox-Ausführung) wird während des Vorschauzeitraums **nicht in Rechnung gestellt**.

## Beschränkungen

- **Status der Vorabversion**:Der Antigravity-Agent und die Interactions API. Funktionen und Schemas können sich ändern.
- **Nicht unterstützte Generierungskonfiguration**:Die folgenden Parameter werden nicht unterstützt und geben einen 400-Fehler zurück: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Strukturierte Ausgabe**:Der Antigravity-Agent unterstützt keine strukturierte Ausgabe.
- **Nicht verfügbare Tools**:`file_search`, `computer_use` und `google_maps` werden noch nicht unterstützt.
- **Einschränkungen für Remote-MCP:** Der Transport von Server-Sent Events (SSE) wird nicht unterstützt. Verwenden Sie Streamable HTTP. Außerdem muss der Server `name` ausschließlich aus Kleinbuchstaben und alphanumerischen Zeichen bestehen. Bei Verwendung von Großbuchstaben wird ein allgemeiner `400 Bad Request`-Fehler ausgelöst.
- **Dateisystemtool**:Derzeit ist kein Dateisystemtool verfügbar. Sie ist Teil der `environment`.
- **Store-Anforderung**:Für die Agent-Ausführung mit `background=True` ist `store=True` erforderlich.
- **Funktionsaufrufe nur im zustandsbehafteten Modus**:Funktionsaufrufe werden nur im zustandsbehafteten Modus unterstützt. Sie müssen `previous_interaction_id` verwenden, um den Zug fortzusetzen. Das manuelle Rekonstruieren des Verlaufs (statusloser Modus) wird nicht unterstützt.
- **Nicht unterstützte multimodale Typen**: Audio-, Video- und Dokumenteingaben werden derzeit nicht unterstützt. Es sind nur Text und Bild zulässig.

## Nächste Schritte

- [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de): Mehrfachdialoge und Streaming.
- [Benutzerdefinierte KI-Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de): benutzerdefinierte Anweisungen, Skills und das Speichern von KI-Agenten.
- [Umgebungen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de): Sandbox-Konfiguration, Quellen, Netzwerk.
- [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=de): Erzwingen Sie Sicherheitsgates und die Validierung von Nebeneffekten in der Sandbox.
- [Deep Research-Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=de): Rechercheaufgaben in Langform.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de): die zugrunde liegende API.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
