---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it
fetched_at: 2026-06-08T05:29:19.856128+00:00
title: "Guida rapida di Managed Agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida rapida di Managed Agents

Questa guida ti illustra come creare e utilizzare gli agenti gestiti nell'API Gemini utilizzando l'agente [Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=it). Eseguirai la tua prima chiamata all'agente, continuerai una conversazione a più turni, visualizzerai in streaming la risposta, scaricherai i file dalla sandbox e lavorerai con l'agente gestito Antigravity.

## Esegui la tua prima interazione con l'agente

Una singola chiamata all'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it) esegue il provisioning di una sandbox Linux, esegue il loop dell'agente e restituisce il risultato. Definirai tre parametri:

- Trasmetti il `agent` come `"antigravity-preview-05-2026",` che è la versione attuale del nostro agente gestito predefinito e per uso generico.
- Definisci `environment="remote"` per eseguire il provisioning di un nuovo ambiente sandbox.
- Crea un input che definisca cosa vuoi che faccia l'agente.

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

La risposta restituisce un oggetto `Interaction`. Memorizza `interaction.id` e `interaction.environment_id` per continuare la conversazione nella stessa sandbox. Utilizza `interaction.output_text` per accedere alla risposta finale dell'agente. `interaction.steps` elenca ogni passaggio eseguito dall'agente (ragionamento, chiamate di strumenti, esecuzione del codice).

## Continua la conversazione (più turni)

L'API tiene traccia di due dimensioni di stato indipendenti:

- **Contesto della conversazione:** cronologia chat, traccia del ragionamento, utilizzo degli strumenti, utilizzo di `previous_interaction_id`.
- [**Stato dell'ambiente:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it) file, pacchetti installati e stato della sandbox, utilizzando `environment`.

Trasmetti entrambi nel rispettivo posto per riprendere:

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

I file del turno 1 (`fibonacci.txt`) persistono nel turno 2. L'agente conserva anche il contesto della conversazione.

Puoi combinarli e abbinarli in modo indipendente:

- **Cancella conversazione, conserva i file:** ometti `previous_interaction_id`, trasmetti solo l'ID ambiente utilizzando `environment` per una nuova conversazione nella stessa area di lavoro.
- **Conserva la conversazione, nuova area di lavoro:** trasmetti `previous_interaction_id`, imposta `environment="remote"` per una nuova sandbox.

### Compattazione automatica del contesto

Nelle conversazioni a più turni di lunga durata, la cronologia non elaborata dei passaggi di ragionamento, delle chiamate di strumenti e dei contenuti di file di grandi dimensioni può crescere rapidamente e consumare uno spazio di contesto significativo. Per evitare errori di limite di token e mantenere l'attenzione dell'agente (prevenendo il "deterioramento del contesto"), l'API Managed Agents include un passaggio di compattazione del contesto nativo a circa 135.000 token. Ciò avviene automaticamente.

## Visualizza in streaming la risposta

Per le attività di lunga durata, puoi visualizzare in streaming la risposta per vedere l'agente lavorare in tempo reale:

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

Lo streaming restituisce un oggetto iterabile di delta di passaggi, ovvero testo incrementale, token di ragionamento e aggiornamenti delle chiamate di strumenti. Scopri di più su come visualizzare in streaming le risposte nella [guida allo streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=it).

## Scarica i file dall'ambiente

Quando l'agente crea file all'interno della sandbox. Scaricali utilizzando l'API Files con una richiesta HTTP diretta (non è ancora disponibile alcun metodo SDK):

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

## Salva un agente gestito

Nei passaggi precedenti, abbiamo utilizzato l'agente Antigravity predefinito e lo abbiamo personalizzato in linea. Una volta eseguite le iterazioni sulla configurazione (istruzioni, competenze e ambiente), puoi salvarla come agente gestito. In questo modo, puoi richiamarlo per ID senza ripetere la configurazione.

Quando salvi un agente, definisci un `base_environment` (da origini o eseguendo il fork di un ambiente esistente). L'agente utilizzerà questo ambiente per ogni nuova interazione.

**Da origini:** definisci le origini in linea o da altre origini come GitHub o Cloud Storage.

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

## Richiama l'agente gestito

Una volta salvato un agente gestito, puoi richiamarlo per ID. Ogni chiamata esegue il fork dell'ambiente di base, quindi ogni esecuzione inizia da zero:

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

## Passaggi successivi

- [Agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it): funzionalità, strumenti supportati, input multimodale, prezzi e limitazioni.
- [Creazione di agenti gestiti](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it): estendi Antigravity con le tue istruzioni, competenze e dati.
- [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it): origini, networking, ciclo di vita, limiti delle risorse.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it): l'API sottostante per modelli e agenti.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-20 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-20 UTC."],[],[]]
