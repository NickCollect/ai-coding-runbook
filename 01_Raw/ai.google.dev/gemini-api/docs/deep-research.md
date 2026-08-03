---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=it
fetched_at: 2026-08-03T04:33:44.045893+00:00
title: "Agente Gemini Deep Research \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Agente Gemini Deep Research

L'agente Gemini Deep Research pianifica, esegue e sintetizza autonomamente
attività di ricerca in più fasi. Basato su Gemini, esplora paesaggi informativi complessi per produrre report dettagliati e citati. Le nuove
funzionalità ti consentono di pianificare in collaborazione con l'agente, connetterti a
strumenti esterni utilizzando i server MCP, includere
visualizzazioni (come grafici e diagrammi) e fornire documenti direttamente
come input.

Le attività di ricerca comportano la ricerca e la lettura iterative e possono richiedere diversi minuti per essere completate. Devi utilizzare l'[esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it) (imposta `background=true`)
per eseguire l'agente in modo asincrono e cercare i risultati o trasmettere in streaming gli aggiornamenti. Per saperne di più, consulta [Gestione delle attività a lunga esecuzione](#long-running-tasks).

L'esempio seguente mostra come avviare un'attività di ricerca in background
e eseguire il polling dei risultati.

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

## Versioni supportate

L'agente Deep Research è disponibile in due versioni:

- **Deep Research** (`deep-research-preview-04-2026`): progettato per velocità ed efficienza, ideale per essere trasmesso in streaming a una UI client.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): massima completezza per la raccolta e la sintesi automatizzate del contesto.

## Pianificazione collaborativa

La pianificazione collaborativa ti consente di controllare la direzione della ricerca prima che l'agente inizi il suo lavoro, permettendoti di rivedere e perfezionare il piano di ricerca prima dell'esecuzione. Se questa opzione è abilitata, l'agente restituisce un piano di ricerca proposto anziché
eseguirlo immediatamente. Puoi quindi rivedere, modificare o approvare il piano tramite
interazioni in più passaggi.

### Passaggio 1: richiedi un piano

Imposta `collaborative_planning=True` nella prima interazione. L'agente
restituisce un piano di ricerca anziché un report completo.

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

### Passaggio 2: perfeziona il piano (facoltativo)

Utilizza `previous_interaction_id` per continuare la conversazione e perfezionare il piano. Mantieni `collaborative_planning=True` per rimanere in modalità
pianificazione.

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

### Passaggio 3: approva ed esegui

Imposta `collaborative_planning=False` (o omettilo) per approvare il piano e
avviare la ricerca.

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

## Visualizzazione

Quando `visualization` è impostato su `"auto"`, l'agente può generare grafici e altri elementi visivi per supportare i risultati della ricerca.
Le immagini generate sono incluse nei passaggi della risposta e vengono trasmesse in streaming come
delta `image`. Per ottenere risultati ottimali, chiedi esplicitamente immagini nella tua
query, ad esempio "Includi grafici che mostrano le tendenze nel tempo" o
"Genera grafici che confrontano la quota di mercato". L'impostazione di `visualization` su
`"auto"` attiva la funzionalità, ma l'agente genera immagini solo
quando il prompt le richiede.

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

## Strumenti supportati

Deep Research supporta più strumenti integrati ed esterni. Per impostazione predefinita
(quando non viene fornito alcun parametro `tools`), l'agente ha accesso a Google
Search, al contesto URL e all'esecuzione di codice. Puoi specificare
in modo esplicito gli strumenti per limitare o estendere le funzionalità dell'agente.

| Strumento | Tipo di valore | Descrizione |
| --- | --- | --- |
| Ricerca Google | `google_search` | Ricerca sul web pubblico. Abilitato per impostazione predefinita. |
| Contesto URL | `url_context` | Leggere e riassumere i contenuti di una pagina web. Abilitato per impostazione predefinita. |
| Esecuzione del codice | `code_execution` | Esegui il codice per eseguire calcoli e analisi dei dati. Abilitato per impostazione predefinita. |
| Server MCP | `mcp_server` | Connettiti ai server MCP remoti per l'accesso a strumenti esterni. |
| Ricerca file | `file_search` | Cerca nei corpora di documenti caricati. |

### Ricerca Google

Abilita esplicitamente la Ricerca Google come unico strumento:

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

### Contesto URL

Concedi all'agente la possibilità di leggere e riassumere pagine web specifiche:

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

### Esecuzione del codice

Consenti all'agente di eseguire codice per calcoli e analisi dei dati:

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

### Server MCP

Connettiti a server MCP remoti per consentire all'agente di accedere a strumenti e
servizi esterni.

Fornisci il server `name` e `url` nella configurazione degli strumenti. Puoi anche
trasferire le credenziali di autenticazione e limitare gli strumenti che l'agente può chiamare.

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `type` | `string` | Sì | Deve essere `"mcp_server"`. |
| `name` | `string` | No | Un nome visualizzato per il server MCP. |
| `url` | `string` | No | L'URL completo dell'endpoint del server MCP. |
| `headers` | `object` | No | Coppie chiave-valore inviate come intestazioni HTTP con ogni richiesta al server (ad esempio, token di autenticazione). |
| `allowed_tools` | `array` | No | Limita gli strumenti del server che l'agente può chiamare. |

#### Utilizzo di base

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

### Ricerca file

Concedi all'agente l'accesso ai tuoi dati utilizzando lo strumento [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it).

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

## Orientabilità e formattazione

Puoi controllare l'output dell'agente fornendo istruzioni di formattazione specifiche nel prompt. In questo modo puoi strutturare i report in sezioni e sottosezioni specifiche, includere tabelle di dati o regolare il tono per diversi segmenti di pubblico (ad es. "tecnico", "dirigenziale", "informale").

Definisci esplicitamente il formato di output desiderato nel testo di input.

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

## Input multimodali

Deep Research supporta input multimodali, tra cui immagini e documenti (PDF), consentendo
all'agente di analizzare i contenuti visivi e condurre ricerche basate sul web
contestualizzate dagli input forniti.

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

### Document understanding

La comprensione dei documenti consente di passare i documenti direttamente come input multimodali.
L'agente analizza i
documenti forniti e conduce ricerche basate sui loro contenuti.

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

## Gestione di attività di lunga durata

Deep Research è un processo in più passaggi che prevede pianificazione, ricerca, lettura
e scrittura. Questo ciclo in genere supera i limiti di timeout standard delle
chiamate API sincrone.

Gli agenti sono tenuti a utilizzare `background=True`. L'API restituisce immediatamente un oggetto
`Interaction` parziale. Puoi utilizzare la proprietà `id` per recuperare un'interazione per il polling. Lo stato dell'interazione passerà da
`in_progress` a `completed` o `failed`. Per una guida completa alla gestione delle attività in background, consulta [Esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it).

### Streaming

Deep Research supporta lo streaming per ricevere aggiornamenti in tempo reale sull'avanzamento della ricerca, inclusi riepiloghi dei pensieri, output di testo e immagini generate.
Devi impostare `stream=True` e `background=True`.

Per ricevere passaggi di ragionamento intermedi (pensieri) e aggiornamenti sullo stato di avanzamento,
devi attivare i **riepiloghi del pensiero** impostando `thinking_summaries` su
`"auto"` in `agent_config`. Senza questo, lo stream potrebbe fornire solo i risultati finali.

#### Tipi di eventi di stream

| Tipo di evento | Tipo di delta | Descrizione |
| --- | --- | --- |
| `step.delta` | `thought` | Passaggio di ragionamento intermedio dell'agente. |
| `step.delta` | `text` | Parte dell'output di testo finale. |
| `step.delta` | `image` | Un'immagine generata (con codifica base64). |

L'esempio seguente avvia un'attività di ricerca ed elabora lo stream con
la riconnessione automatica. Monitora `interaction_id` e `last_event_id` in modo che, se la connessione si interrompe (ad esempio, dopo il timeout di 600 secondi), possa riprendere da dove era stata interrotta.

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

## Domande aggiuntive e interazioni

Puoi continuare la conversazione dopo che l'agente ha restituito il report finale
utilizzando `previous_interaction_id`. In questo modo puoi chiedere chiarimenti,
riepiloghi o approfondimenti su sezioni specifiche della ricerca senza
dover ricominciare l'intera attività.

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

## Quando utilizzare l'agente Gemini Deep Research

Deep Research è un **agente**, non solo un modello. È più adatta ai workload
che richiedono un approccio "analista in una scatola" anziché una chat a bassa latenza.

| Funzionalità | Modelli Gemini standard | Agente Gemini Deep Research |
| --- | --- | --- |
| **Latenza** | Secondi | Minuti (asincrono/in background) |
| **Procedura** | Genera -> Output | Pianificazione -> Ricerca -> Lettura -> Iterazione -> Output |
| **Output** | Testo conversazionale, codice, riepiloghi brevi | Report dettagliati, analisi in formato lungo, tabelle comparative |
| **Ideale per** | Chatbot, estrazione, scrittura creativa | Analisi di mercato, due diligence, revisioni della letteratura, panorama competitivo |

## Configurazione dell'agente

Deep Research utilizza il parametro `agent_config` per controllare il comportamento.
Trasmettilo come dizionario con i seguenti campi:

| Campo | Tipo | Predefinito | Descrizione |
| --- | --- | --- | --- |
| `type` | `string` | Obbligatorio | Deve essere `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Imposta `"auto"` per ricevere i passaggi di ragionamento intermedi durante lo streaming. Imposta su `"none"` per disattivarlo. |
| `visualization` | `string` | `"auto"` | Imposta `"auto"` per attivare grafici e immagini generati dall'agente. Imposta su `"off"` per disattivarlo. |
| `collaborative_planning` | `boolean` | `false` | Imposta su `true` per attivare la revisione del piano in più turni prima dell'inizio della ricerca. |

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

## Disponibilità e prezzi

Puoi accedere all'agente Gemini Deep Research utilizzando l'API Interactions in Google AI Studio e l'API Gemini.

I prezzi seguono un [modello di pagamento a consumo](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing-for-agents) basato sui modelli Gemini sottostanti e sugli strumenti specifici utilizzati dall'agente. A differenza delle richieste di chat standard, in cui una richiesta porta a un output, un'attività Deep Research è un flusso di lavoro agentico. Una singola richiesta attiva un ciclo autonomo di pianificazione, ricerca, lettura e ragionamento.

### Costi stimati

I costi variano in base alla profondità della ricerca richiesta. L'agente determina autonomamente la quantità di lettura e ricerca necessaria per rispondere al prompt.

- **Deep Research** (`deep-research-preview-04-2026`): per una query tipica che richiede un'analisi moderata, l'agente potrebbe utilizzare circa 80 query di ricerca, circa 250.000 token di input (circa il 50-70% memorizzati nella cache) e circa 60.000 token di output.
  - **Totale stimato:** 1-3 € per attività
- **Deep Research Max** (`deep-research-max-preview-04-2026`): per un'analisi approfondita del panorama competitivo o una due diligence estesa, l'agente potrebbe utilizzare fino a circa 160 query di ricerca, circa 900.000 token di input (circa il 50-70% memorizzati nella cache) e circa 80.000 token di output.
  - **Totale stimato:** 3-7 € per attività

## Considerazioni sulla sicurezza

Concedere a un agente l'accesso al web e ai tuoi file privati richiede un'attenta
valutazione dei rischi per la sicurezza.

- **Prompt injection tramite file**:l'agente legge i contenuti dei file
  che fornisci. Assicurati che i documenti caricati (PDF, file di testo) provengano da
  fonti attendibili. Un file dannoso potrebbe contenere testo nascosto progettato per
  manipolare l'output dell'agente.
- **Rischi dei contenuti web**:l'agente esegue ricerche sul web pubblico. Sebbene implementiamo
  filtri di sicurezza robusti, esiste il rischio che l'agente possa incontrare ed
  elaborare pagine web dannose. Ti consigliamo di esaminare le `citations` fornite
  nella risposta per verificare le fonti.
- **Esfiltrazione**:fai attenzione quando chiedi all'agente di riassumere dati interni sensibili se gli consenti anche di navigare sul web.

## Best practice

- **Richiedi sconosciuti**:indica all'agente come gestire i dati mancanti.
  Ad esempio, aggiungi *"Se non sono disponibili cifre specifiche per il 2025,
  indica esplicitamente che si tratta di proiezioni o che non sono disponibili anziché
  stimarle"* al prompt.
- **Fornisci contesto**:basa la ricerca dell'agente fornendo informazioni di base o vincoli direttamente nel prompt di input.
- **Utilizza la pianificazione collaborativa**:per le query complesse, attiva la pianificazione collaborativa per rivedere e perfezionare il piano di ricerca prima dell'esecuzione.
- **Input multimodali:** l'agente Deep Research supporta input multimodali.
  Utilizza con cautela, in quanto aumenta i costi e il rischio di overflow della finestra contestuale.

## Limitazioni

- **Strumenti personalizzati**:al momento non puoi fornire strumenti di chiamata di funzioni personalizzati,
  ma puoi utilizzare server MCP (Model Context Protocol) remoti con l'agente Deep Research.
- **Output strutturato**:l'agente Deep Research attualmente
  non supporta gli output strutturati.
- **Tempo massimo di ricerca**:l'agente Deep Research ha un tempo massimo di ricerca di 60 minuti. La maggior parte delle attività dovrebbe essere completata entro 20 minuti.
- **Requisito dello store**:l'esecuzione dell'agente utilizzando `background=True` richiede
  `store=True`.
- **Ricerca Google**:la [Ricerca
  Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) è attivata per
  impostazione predefinita e ai risultati fondati si applicano [limitazioni
  specifiche](https://ai.google.dev/gemini-api/terms?hl=it#use-restrictions2).

## Passaggi successivi

- Scopri di più sull'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it).
- Scopri come utilizzare i tuoi dati con lo strumento [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-14 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-14 UTC."],[],[]]
