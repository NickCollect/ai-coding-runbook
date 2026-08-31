---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it
fetched_at: 2026-08-31T06:33:47.180173+00:00
title: "Agente Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Agente Antigravity

L'agente Antigravity è un agente gestito per uso generico nell'API Gemini. Una singola chiamata API ti fornisce un agente che ragiona, esegue codice, gestisce file e naviga sul web all'interno del tuo sandbox Linux sicuro, ospitato da Google.

È basato su Gemini 3.7 Flash e utilizza lo stesso harness dell'IDE Antigravity. Puoi configurare il modello Gemini sottostante utilizzando `agent_config`. Disponibile tramite l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) e [Google AI Studio](https://aistudio.google.com?hl=it).

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

## Funzionalità

Ogni chiamata può eseguire il provisioning di una sandbox Linux e avvia un ciclo di utilizzo degli strumenti. L'agente pianifica, agisce, osserva i risultati e ripete l'operazione finché l'attività non è completata.

- **Esecuzione del codice**:esegui comandi Bash, Python e Node.js. Installa pacchetti, esegui test, crea app.
- **Gestione dei file**:leggi, scrivi, modifica, cerca ed elenca i file nel sandbox. I file vengono mantenuti durante le interazioni.
- **Accesso al web**:Ricerca Google e recupero di URL per i dati.
- **Compattazione del contesto**:compattazione automatica del contesto (attivata a circa 135.000 token) per supportare sessioni multi-turno di lunga durata senza perdere il contesto o raggiungere i limiti di token.

Consulta la [guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it) per l'utilizzo multi-turno e lo streaming.

## Strumenti supportati

Per impostazione predefinita, l'agente ha accesso a `code_execution`, `google_search` e `url_context`. Gli strumenti del file system vengono attivati automaticamente quando specifichi il parametro `environment`. Puoi anche definire **funzioni personalizzate** per connettere l'agente alle tue API e ai tuoi strumenti. Devi specificare il parametro `tools` solo quando personalizzi o limiti il set predefinito oppure quando aggiungi funzioni personalizzate.

| Strumento | Tipo di valore | Descrizione |
| --- | --- | --- |
| Esecuzione del codice | `code_execution` | Esegui comandi della shell (bash, Python, Node) con acquisizione di stdout/stderr. |
| Ricerca Google | `google_search` | Ricerca sul web pubblico. |
| Contesto URL | `url_context` | Recuperare e leggere pagine web. |
| Filesystem | *(attivato tramite `environment`)* | Leggere, scrivere, modificare, cercare ed elencare i file nella sandbox. Il sistema attiva automaticamente questi strumenti quando imposti `environment`. |
| Funzioni personalizzate | `function` | Definisci funzioni personalizzate che l'agente può richiedere di eseguire. Vedi [Chiamata di funzione](#function-calling). |
| Server MCP remoto | `mcp_server` | Registra server Model Context Protocol (MCP) esterni come strumenti. Vedi [Server MCP](#mcp-servers). |

Puoi intercettare e convalidare l'esecuzione degli strumenti `code_execution` e `filesystem` direttamente all'interno della sandbox remota utilizzando gli [hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=it) sincroni.

Per limitare l'agente a strumenti specifici, trasmetti solo quelli che ti servono:

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

## Input multimodale

L'agente Antigravity supporta input multimodali. Al momento sono supportati solo gli input `text` e `image`. Le immagini devono essere fornite come stringhe incorporate con codifica base64 (`data`).

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

## Chiamata di funzione

La chiamata di funzione ti consente di connettere l'agente Antigravity ad API e database esterni definendo strumenti personalizzati che l'agente può richiamare. Per i concetti generali, vedi [Chiamata di funzione con l'API Gemini](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it).

L'esempio seguente mostra un'interazione di due turni. L'agente richiede prima una chiamata di funzione `get_weather` personalizzata, che il client esegue e restituisce il risultato nel secondo turno.

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

## Server MCP

Puoi connettere l'agente Antigravity a strumenti esterni registrando server Model Context Protocol (MCP) remoti. L'agente supporta i server MCP remoti tramite HTTP trasmissibile.

Quando registri un server MCP, devi specificare i seguenti campi nell'array `tools`:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `type` | stringa | Sì | Deve essere `"mcp_server"`. |
| `name` | stringa | Sì | Un identificatore univoco per il server. Deve essere rigorosamente minuscolo e alfanumerico (corrispondente a `^[a-z0-9_-]+$`). |
| `url` | stringa | Sì | L'URL dell'endpoint del server MCP remoto. |
| `headers` | oggetto | No | Intestazioni personalizzate (ad es. autenticazione) inviate con le richieste. |
| `allowed_tools` | matrice | No | Elenco dei nomi degli strumenti che possono essere eseguiti. Se omesso, sono consentiti tutti gli strumenti. |

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

## Selezione del modello

Per `antigravity-preview-05-2026`, il modello predefinito è **Gemini 3.7 Flash** (`gemini-3.7-flash`). Se ometti `agent_config`, l'agente utilizza `gemini-3.7-flash` per impostazione predefinita.

Puoi configurare il modello Gemini sottostante utilizzando `agent_config` per ottimizzare la velocità, i costi o la capacità di ragionamento.

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

I valori supportati per `agent_config.model` sono:

| Modello | Valore in `agent_config.model` | Descrizione |
| --- | --- | --- |
| **Gemini 3.7 Flash** (predefinito) | `gemini-3.7-flash` | Modello bilanciato predefinito per ragionamento, programmazione e utilizzo di strumenti. |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | Modello Flash di generazione precedente per flussi di lavoro agentici generali. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Modello leggero per workflow generali. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Modello leggero ottimizzato per attività a bassa latenza e sensibili ai costi. |

Quando crei un agente gestito con `agents.create`, configuri il modello esattamente nello stesso modo passando `base_agent` e `agent_config`. Tieni presente che non puoi ignorare il modello al momento dell'interazione per un agente gestito creato con `agents.create`. Il modello è bloccato su ciò che è stato impostato al momento della creazione dell'agente. Ciò garantisce un comportamento prevedibile di chiamata degli strumenti, un debug coerente e il rispetto dei limiti di sicurezza.

## Personalizzazione dell'agente

Puoi estendere l'agente Antigravity personalizzando le sue istruzioni, i suoi strumenti e il suo ambiente. L'agente supporta un approccio nativo al file system per la personalizzazione: puoi montare file come `AGENTS.md` per istruzioni e competenze in `.agents/skills/` direttamente nella sandbox o passare la configurazione in linea al momento dell'interazione. Puoi iterare la configurazione in linea e salvarla come agente gestito quando è pronta.

Per informazioni dettagliate su come creare agenti personalizzati, consulta [Creazione di agenti gestiti](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it).

## Esecuzione in background

Le attività dell'agente che comportano ragionamento multi-step, esecuzione di codice o operazioni sui file possono richiedere minuti per essere completate. Utilizza `background=True` per eseguire l'interazione in modo asincrono. L'API restituisce immediatamente un ID interazione che esegui il polling finché lo stato non è `completed` o `failed`.

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

L'esecuzione in background richiede `store=True`, che è l'impostazione predefinita. Per gli aggiornamenti in tempo reale sullo stato di avanzamento durante l'esecuzione in background, vedi [Interazioni in background in streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=it#streaming-background).

Puoi annullare un'interazione in background in esecuzione utilizzando il metodo `cancel`.

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

**Multi-turn con esecuzione in background**

Quando un'interazione in background coinvolge strumenti stateful (come l'esecuzione di codice in una sandbox), utilizza `environment_id` dall'interazione completata per continuare nello stesso ambiente. In questo modo, l'agente riprende da dove aveva interrotto l'elaborazione, con tutti i file e lo stato intatti.

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

## Ambienti

Ogni chiamata crea o riutilizza una sandbox Linux. Il parametro `environment` assume tre forme:

| Modulo | Descrizione |
| --- | --- |
| `"remote"` | Esegui il provisioning di una nuova sandbox con le impostazioni predefinite. |
| `"env_abc123"` | Riutilizza un ambiente esistente per ID, conservando tutti i file e lo stato. |
| `{...}` | `EnvironmentConfig` completo con origini e regole di rete personalizzate. |

Consulta [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it) per informazioni dettagliate su origini (Git, GCS, inline), networking, ciclo di vita e limiti delle risorse.

## Trigger

I trigger consentono di programmare l'esecuzione automatica di un agente in base a una pianificazione cron. Un trigger associa un agente, un ambiente, un prompt e una pianificazione a una risorsa persistente che viene attivata senza intervento manuale. Ogni esecuzione riutilizza lo stesso ambiente, quindi i file creati in un'esecuzione vengono mantenuti e sono visibili nella successiva.

### Crea un trigger

Crea un trigger specificando una pianificazione cron, un fuso orario e la configurazione dell'interazione. Il trigger inizia con lo stato `active` e verrà attivato alla successiva corrispondenza dell'ora cron. Salva il `id` restituito per gestire il trigger nelle chiamate successive.

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

La richiesta `CreateTrigger` accetta i seguenti campi:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `schedule` | stringa | Sì | Espressione cron (ad es. `0 * * * *` per ogni ora, `0 9 * * 1-5` per le mattine dei giorni feriali). |
| `time_zone` | stringa | Sì | Fuso orario IANA (ad es. `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | stringa | No | Nome leggibile dell'attivatore. |
| `max_consecutive_failures` | integer | No | Numero massimo di errori prima che il trigger venga messo in pausa automaticamente. Valore predefinito: 5. |
| `execution_timeout_seconds` | integer | No | Timeout per esecuzione in secondi. Valore predefinito: 600. |
| `interaction` | oggetto | Sì | Un `CreateInteractionRequest` che definisce l'agente, l'input, gli strumenti e l'ambiente. |

klimafreundlich

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `id` | stringa | Identificatore univoco del trigger. Utilizzalo in tutte le operazioni successive. |
| `status` | stringa | Stato attuale: `active`, `paused` o `disabled`. |
| `next_run_time` | stringa | Timestamp ISO 8601 della prossima esecuzione pianificata. |
| `consecutive_failure_count` | integer | Numero di esecuzioni non riuscite consecutive dall'ultima riuscita. |

### Elenca trigger

Recupera tutti i trigger associati al tuo progetto.

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

### Recuperare un trigger

Recupera la configurazione completa e lo stato attuale di un singolo trigger.

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

### Mettere in pausa e riprendere

Puoi mettere in pausa un trigger per interrompere le esecuzioni pianificate e riprenderlo per riattivare la pianificazione. La sospensione non influisce sulle esecuzioni manuali.

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

### Elimina un trigger

Rimuovere definitivamente un trigger. La cronologia delle esecuzioni passate non viene eliminata.

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

### Eseguire un trigger immediatamente

Attiva un trigger on demand senza attendere il successivo orario programmato. Funziona anche se il trigger è in pausa.

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

### Recupero elenco esecuzioni

Visualizza la cronologia di esecuzione di un trigger. Ogni esecuzione include un `status`, timestamp, un `interaction_id` che puoi utilizzare per recuperare l'output completo dell'interazione e un `environment_id` che conferma che tutte le esecuzioni condividono la stessa sandbox.

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

## Disponibilità e prezzi

L'agente Antigravity è disponibile in anteprima tramite l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) in Google AI Studio e l'API Gemini per i progetti sia del Livello senza costi sia del Livello a pagamento.

I prezzi seguono un [modello di pagamento a consumo](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing-for-agents)
basato sui token del modello Gemini sottostante e sugli strumenti utilizzati dall'agente. A differenza di una
richiesta di chat standard che produce un singolo output, un'interazione Antigravity è un
flusso di lavoro autonomo. Una singola richiesta attiva un ciclo autonomo di ragionamento, esecuzione di strumenti, esecuzione di codice e gestione dei file. I progetti del livello senza costi includono un limite di frequenza
e una quota di utilizzo senza costi.

Le interazioni antigravità eseguono loop autonomi multi-turn e possono consumare
un numero significativo di token. Imposta [controlli del budget](#budget-controls) nella richiesta per
limitare l'utilizzo dei token. attenuation Puoi anche monitorare l'avanzamento in tempo reale con lo
[streaming SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=it) o annullare le richieste in esecuzione.

### Controlli del budget

Oltre alla [selezione del modello](#model-selection), imposta `max_total_tokens` all'interno di `agent_config` (con `"type": "antigravity"`) per limitare
il numero totale di token (input + output + pensiero) che un'interazione può consumare.
I token memorizzati nella cache non vengono conteggiati ai fini di questo limite. Quando l'agente raggiunge il limite, l'interazione si interrompe e restituisce `status: "incomplete"`. Il limite è il migliore possibile:
l'utilizzo effettivo potrebbe superarlo leggermente a seconda di quando l'agente controlla il budget
tra i passaggi.

Imposta il budget nella richiesta di interazione in `agent_config` insieme a `agent` e `input`.

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

#### Continuare un'interazione incompleta

Quando un'interazione restituisce `status: "incomplete"`, il lavoro e il contesto dell'agente
vengono conservati. Invia una nuova interazione che faccia riferimento all'interazione originale `id` e
`environment_id` per riprendere da dove era stata interrotta. La nuova interazione ha un proprio
budget `max_total_tokens`.

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

### Costi stimati

I costi variano in base alla complessità dell'attività. L'agente determina autonomamente il numero di chiamate agli strumenti, esecuzioni di codice e operazioni sui file necessari. Le seguenti stime si basano sulle corse.

| Categoria attività | Token di input | Token di output | Costo tipico |
| --- | --- | --- | --- |
| **Ricerca e sintesi delle informazioni** | 100.000 - 500.000 | 10.000 - 40.000 | 0,30 $-1 $ |
| **Generazione di documenti e contenuti** | 100.000 - 500.000 | 15.000 - 50.000 | 0,30 $-1,30 $ |
| **Progettazione di processi e sistemi** | 100.000 - 400.000 | 10.000 - 30.000 | 0,25 $-0,80 $ |
| **Elaborazione e analisi dei dati** | 300.000 - 3 milioni | 30.000 - 150.000 | 0,70 $-3,25 $ |

In genere, il 50-70% dei token di input viene memorizzato nella cache. I workflow complessi con molti richiami di strumenti possono accumulare 3-5 milioni di token in una singola interazione, con costi fino a circa 5 $.

Il **calcolo dell'ambiente** (CPU, memoria, esecuzione sandbox) **non viene fatturato** durante il periodo di anteprima.

## Limitazioni

- **Stato dell'anteprima**:l'agente Antigravity e l'API Interactions. Funzionalità e schemi possono cambiare.
- **Configurazione della generazione non supportata**:i seguenti parametri non sono supportati e restituiscono un errore 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Output strutturato**:l'agente Antigravity non supporta gli output strutturati.
- **Strumenti non disponibili**:`file_search`, `computer_use` e `google_maps` non sono ancora supportati.
- **Limitazioni MCP remote**:il trasporto Server-Sent Events (SSE) non è supportato (utilizza HTTP trasmissibile). Inoltre, il server `name` deve essere rigorosamente minuscolo e alfanumerico (l'utilizzo di lettere maiuscole attiva un errore `400 Bad Request` generico).
- **Strumento per il file system**:al momento non esiste uno strumento per il file system. Fa parte di `environment`.
- **Requisito dello store**:l'esecuzione dell'agente utilizzando `background=True` richiede `store=True`.
- **Chiamata di funzioni stateful only**:la chiamata di funzioni è supportata solo in modalità stateful. Devi utilizzare `previous_interaction_id` per continuare il turno; la ricostruzione manuale della cronologia (modalità stateless) non è supportata.
- **Tipi multimodali non supportati.** Al momento, gli input audio, video e di documenti non sono supportati. Sono consentiti solo testo e immagini.

## Passaggi successivi

- [Guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it): conversazioni multi-turn e streaming.
- [Creazione di agenti personalizzati](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it): istruzioni, competenze e salvataggio degli agenti personalizzati.
- [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it): configurazione sandbox, origini, networking.
- [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=it): applica i controlli di sicurezza e la convalida degli effetti collaterali all'interno della sandbox.
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it): attività di ricerca a lungo termine.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it): l'API sottostante.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-08-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-08-19 UTC."],[],[]]
