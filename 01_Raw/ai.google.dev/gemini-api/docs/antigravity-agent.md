---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it
fetched_at: 2026-06-15T06:29:50.163471+00:00
title: "Agente Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Agente Antigravity

L'agente Antigravity è un agente gestito per uso generico sull'API Gemini. Una singola chiamata API ti fornisce un agente che ragiona, esegue codice, gestisce file e naviga sul web all'interno della tua sandbox Linux sicura, ospitata da Google.

È basato su Gemini 3.5 Flash e utilizza lo stesso harness dell'IDE Antigravity. Disponibile tramite l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it) e [Google AI Studio](https://aistudio.google.com?hl=it).

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Funzionalità

Ogni chiamata può eseguire il provisioning di una sandbox Linux e avvia un loop di utilizzo degli strumenti. L'agente pianifica, agisce, osserva i risultati e ripete l'operazione finché l'attività non è completata.

- **Esecuzione del codice:** esegui comandi Bash, Python e Node.js. Installa pacchetti, esegui test, crea app.
- **Gestione dei file:** leggi, scrivi, modifica, cerca ed elenca i file nella sandbox. I file vengono mantenuti tra le interazioni.
- **Accesso web:** Ricerca Google e recupero di URL per i dati.
- **Compattazione del contesto:** compattazione automatica del contesto (attivata a circa 135.000 token) per supportare sessioni a più turni di lunga durata senza perdere il contesto o raggiungere i limiti di token.

Per informazioni sull'utilizzo a più turni e sullo streaming, consulta la [Guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it).

## Strumenti supportati

Per impostazione predefinita, l'agente ha accesso a `code_execution`, `google_search` e `url_context`. Gli strumenti del filesystem vengono attivati automaticamente quando specifichi il parametro `environment`. Devi specificare il parametro `tools` solo quando personalizzi o limiti l'insieme predefinito.

| Strumento | Valore del tipo | Descrizione |
| --- | --- | --- |
| Esecuzione del codice | `code_execution` | Esegui i comandi della shell (bash, Python, Node) con acquisizione di stdout/stderr. |
| Ricerca Google | `google_search` | Cerca sul web pubblico. |
| Contesto URL | `url_context` | Recupera e leggi le pagine web. |
| Filesystem | *(attivato tramite `environment`)* | Leggi, scrivi, modifica, cerca ed elenca i file nella sandbox. Nessun tipo di strumento separato; attivato automaticamente quando è impostato `environment`. |

Per limitare l'agente a strumenti specifici, trasmetti solo quelli di cui hai bisogno:

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
-H "Api-Revision: 2026-05-20" \
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

L'agente Antigravity supporta gli input multimodali. Al momento sono supportati solo gli input `text` e `image`. Le immagini devono essere fornite come stringhe con codifica base64 in linea (`data`).

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
-H "Api-Revision: 2026-05-20" \
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

## Personalizzare l'agente

Puoi estendere l'agente Antigravity personalizzando le istruzioni, gli strumenti e l'ambiente. L'agente supporta un approccio di personalizzazione nativo del filesystem: puoi montare file come `AGENTS.md` per istruzioni e competenze in `.agents/skills/` direttamente nella sandbox o trasmettere la configurazione in linea al momento dell'interazione. Puoi eseguire l'iterazione sulla configurazione in linea e poi salvarla come agente gestito quando è tutto pronto.

Per informazioni dettagliate su come creare agenti personalizzati, consulta [Creare agenti gestiti](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it).

## Ambienti

Ogni chiamata crea o riutilizza una sandbox Linux. Il parametro `environment` assume tre forme:

| Postura | Descrizione |
| --- | --- |
| `"remote"` | Esegui il provisioning di una nuova sandbox con le impostazioni predefinite. |
| `"env_abc123"` | Riutilizza un ambiente esistente per ID, conservando tutti i file e lo stato. |
| `{...}` | `EnvironmentConfig` completo con origini personalizzate e regole di rete. |

Per informazioni dettagliate su origini (Git, GCS, in linea), networking, ciclo di vita e limiti di risorse, consulta [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it).

## Disponibilità e prezzi

L'agente Antigravity è disponibile in anteprima tramite l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it) in Google AI Studio e l'API Gemini.

I prezzi seguono un [modello con pagamento a consumo](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing-for-agents) basato sui token del modello Gemini sottostante e sugli strumenti utilizzati dall'agente. A differenza di una richiesta di chat standard che produce un singolo output, un'interazione Antigravity è un workflow agentico. Una singola richiesta attiva un loop autonomo di ragionamento, esecuzione di strumenti, esecuzione di codice e gestione dei file.

### Costi stimati

I costi variano in base alla complessità dell'attività. L'agente determina autonomamente il numero di chiamate di strumenti, esecuzioni di codice e operazioni sui file necessari. Le seguenti stime si basano sulle esecuzioni.

| Categoria di attività | Token di input | Token di output | Costo tipico |
| --- | --- | --- | --- |
| **Ricerca e sintesi delle informazioni** | 100.000-500.000 | 10.000-40.000 | 0,30-1,00 $ |
| **Generazione di documenti e contenuti** | 100.000-500.000 | 15.000-50.000 | 0,30-1,30 $ |
| **Progettazione di processi e sistemi** | 100.000-400.000 | 10.000-30.000 | 0,25-0,80 $ |
| **Elaborazione e analisi dei dati** | 300.000-3.000.000 | 30.000-150.000 | 0,70-3,25 $ |

In genere, il 50-70% dei token di input viene memorizzato nella cache. I workflow di agenti complessi con molte chiamate di strumenti possono accumulare 3-5 milioni di token in una singola interazione, con costi fino a circa 5 $.

Il **calcolo dell'ambiente** (CPU, memoria, esecuzione della sandbox) **non viene fatturato** durante il periodo di anteprima.

## Limitazioni

- **Stato di anteprima:** l'agente Antigravity e l'API Interactions sono in anteprima. Le funzionalità e gli schemi potrebbero cambiare.
- **Configurazione di generazione non supportata:** i seguenti parametri non sono supportati e restituiscono un errore 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Output strutturato:** l'agente Antigravity non supporta gli output strutturati.
- **Strumenti non disponibili:** `file_search`, `computer_use`, `google_maps`, `function_calling` e `mcp` non sono ancora supportati.
- **Strumento del filesystem:** al momento non è disponibile alcuno strumento del filesystem. Fa parte di `environment`.
- **Sfondo:** l'agente non supporta l'utilizzo di `background=True` e richiede `store=True`.
- **Tipi multimodali non supportati.** Al momento gli input audio, video e documenti non sono supportati. Sono consentiti solo testo e immagini.

## Passaggi successivi

- [Guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it): conversazioni a più turni e streaming.
- [Creare agenti personalizzati](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it): istruzioni, competenze e salvataggio degli agenti personalizzati.
- [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it): configurazione della sandbox, origini, networking.
- [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=it): attività di ricerca di lunga durata.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it): l'API sottostante.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-20 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-20 UTC."],[],[]]
