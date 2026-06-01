---
source_url: https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=it
fetched_at: 2026-06-01T05:58:23.044619+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=it)

Invia feedback

# Guida per gli sviluppatori di Gemini 3

Gemini 3 è la nostra famiglia di modelli più intelligente di sempre, basata su un ragionamento all'avanguardia. È progettato per dare vita a qualsiasi idea
padroneggiando workflow agentici, programmazione autonoma e attività multimodali complesse.
Questa guida illustra le funzionalità principali della famiglia di modelli Gemini 3 e come ottenere il massimo.

Esplora la nostra [raccolta di app Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=it) per
vedere come il modello gestisce il ragionamento avanzato, la programmazione autonoma e le attività
multimodali complesse.

Inizia con poche righe di codice:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Scopri la serie Gemini 3

Gemini 3.1 Pro è ideale per le attività complesse che
richiedono un'ampia conoscenza del mondo e un ragionamento avanzato tra le varie modalità.

Gemini 3 Flash è il nostro ultimo modello della serie 3, con intelligenza di livello Pro alla velocità e al prezzo di Flash.

Nano Banana Pro (noto anche come Gemini 3 Pro Image) è il nostro modello di generazione di immagini di qualità più elevata, mentre Nano Banana 2 (noto anche come Gemini 3.1 Flash Image) è l'equivalente ad alto volume, alta efficienza e prezzo più basso.

Gemini 3.1 Flash-Lite è il nostro modello più efficiente, progettato per attività a costi contenuti e
con volumi elevati.

Al momento, tutti i modelli Gemini 3 sono in anteprima.

| ID modello | Finestra contestuale (in entrata / in uscita) | Knowledge Cutoff | Prezzi (input / output)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 milione / 64.000 | Gennaio 2025 | 0,25 $ (testo, immagine, video), 0,50 $ (audio) / 1,50 $ |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Gennaio 2025 | 0,25 $ (input di testo) / 0,067 $ (output di immagine)\*\* |
| **gemini-3.1-pro-preview** | 1 milione / 64.000 | Gennaio 2025 | $2 / $12 (<200.000 token)   $4 / $18 (>200.000 token) |
| **gemini-3-flash-preview** | 1 milione / 64.000 | Gennaio 2025 | 0,50 $ / 3 $ |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Gennaio 2025 | 2 $ (input di testo) / 0,134 $ (output di immagine)\*\* |

*\* I prezzi si riferiscono a 1 milione di token, se non diversamente indicato.*
*\*\* Il prezzo delle immagini varia in base alla risoluzione. Per maggiori dettagli, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).*

Per limiti, prezzi e informazioni aggiuntive dettagliati, consulta la
[pagina dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

## Nuove funzionalità dell'API in Gemini 3

Gemini 3 introduce nuovi parametri progettati per offrire agli sviluppatori un maggiore controllo su
latenza, costi e fedeltà multimodale.

### Livello di pensiero

I modelli della serie Gemini 3 utilizzano per impostazione predefinita il ragionamento dinamico per analizzare i prompt. Puoi utilizzare il parametro `thinking_level`, che controlla la
**profondità massima** del processo di ragionamento interno del modello prima che produca una
risposta. Gemini 3 tratta questi livelli come quote relative per il ragionamento
piuttosto che come garanzie di token rigorose.

Se `thinking_level` non è specificato, Gemini 3 utilizzerà `high` come valore predefinito. Per
risposte più rapide e a bassa latenza quando non è necessario un ragionamento complesso, puoi
limitare il livello di pensiero del modello a `low`.

| Livello di pensiero | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrizione |
| --- | --- | --- | --- | --- |
| **`minimal`** | Non supportato | Supportato (valore predefinito) | Supportato | Corrisponde all'impostazione "Nessun pensiero" per la maggior parte delle query. Il modello potrebbe pensare in modo molto minimale per attività di programmazione complesse. Riduce al minimo la latenza per le applicazioni di chat o a throughput elevato. Tieni presente che `minimal` non garantisce che la funzionalità di pensiero sia disattivata. |
| **`low`** | Supportato | Supportato | Supportato | Riduce al minimo la latenza e i costi. Ideale per applicazioni semplici di follow-up delle istruzioni, chat o ad alto rendimento. |
| **`medium`** | Supportato | Supportato | Supportato | Pensiero equilibrato per la maggior parte delle attività. |
| **`high`** | Supportato (predefinito, dinamico) | Supportato (dinamico) | Supportato (predefinito, dinamico) | Massimizza la profondità del ragionamento. Il modello potrebbe impiegare molto più tempo per raggiungere un primo token di output (non di pensiero), ma l'output sarà più ragionato. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Per tutti i modelli Gemini 3, ti consigliamo vivamente di mantenere il parametro di temperatura
sul valore predefinito di `1.0`.

Mentre i modelli precedenti spesso traevano vantaggio dalla regolazione della temperatura per controllare
la creatività rispetto al determinismo, le capacità di ragionamento di Gemini 3 sono ottimizzate
per l'impostazione predefinita. La modifica della temperatura (impostandola su un valore inferiore a 1.0) potrebbe
comportare un comportamento imprevisto, ad esempio un ciclo o un rendimento ridotto,
in particolare in attività matematiche o di ragionamento complesse.

### Firme dei ragionamenti

I modelli Gemini 3 utilizzano le firme del pensiero per mantenere il contesto del ragionamento tra le chiamate API. Queste firme sono rappresentazioni criptate del processo di pensiero interno del modello.

- **Modalità con stato (consigliata)**: quando utilizzi l'API Interactions in modalità con stato (fornendo `previous_interaction_id`), il server gestisce automaticamente la cronologia delle conversazioni e le firme dei pensieri.
- **Modalità stateless**: se gestisci manualmente la cronologia delle conversazioni, devi includere i blocchi di pensiero con le relative firme nelle richieste successive per convalidare l'autenticità.

Per informazioni dettagliate, consulta la pagina [Thought Signatures](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=it).

### Output strutturati con strumenti

I modelli Gemini 3 ti consentono di combinare gli [output strutturati](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=it) con strumenti integrati, tra cui
[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it), [Contesto URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=it), [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it) e [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Generazione di immagini

Gemini 3.1 Flash Image e Gemini 3 Pro Image ti consentono di generare e modificare immagini
a partire da prompt di testo. Utilizza
il ragionamento per "pensare" a un prompt e può recuperare dati in tempo reale, come
previsioni meteo o grafici azionari, prima di utilizzare la [Ricerca Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it) per la generazione di immagini
ad alta fedeltà.

**Funzionalità nuove e migliorate:**

- **Rendering di testo e 4K:** genera testo e diagrammi nitidi e leggibili con risoluzioni fino a 2K e 4K.
- **Generazione fondata:** utilizza lo strumento `google_search` per verificare i fatti e
  generare immagini basate su informazioni del mondo reale. Grounding con la Ricerca *Immagini*
  Google disponibile per Gemini 3.1 Flash Image.
- **Modifica conversazionale**:modifica di immagini in più passaggi semplicemente chiedendo
  di apportare modifiche (ad es. "Crea uno sfondo con un tramonto"). Questo flusso di lavoro si basa sulle
  **Firme del pensiero** per preservare il contesto visivo tra i turni.

Per informazioni dettagliate su proporzioni, flussi di lavoro di modifica e opzioni di configurazione, consulta la [guida alla generazione di immagini](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=it).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Risposta di esempio**

![Meteo Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=it)

### Esecuzione del codice con immagini

Gemini 3 Flash può trattare la visione come un'indagine attiva, non solo come uno sguardo statico. Combinando il ragionamento con l'[esecuzione del codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it), il modello formula un piano, quindi scrive ed esegue codice Python per ingrandire, ritagliare, annotare o manipolare in altro modo le immagini passo dopo passo per basare visivamente le sue risposte.

**Casi d'uso:**

- **Zoom e ispezione**:il modello rileva implicitamente quando i dettagli sono troppo
  piccoli (ad es. la lettura di un indicatore o di un numero di serie distante) e scrive codice per ritagliare
  e riesaminare l'area a una risoluzione più elevata.
- **Matematica visiva e grafici**:il modello può eseguire calcoli in più passaggi utilizzando
  il codice (ad es. la somma delle voci di una ricevuta o la generazione di un grafico Matplotlib
  dai dati estratti).
- **Annotazione delle immagini:** il modello può disegnare frecce, rettangoli di selezione o altre annotazioni direttamente sulle immagini per rispondere a domande spaziali come "Dove va questo oggetto?".

Per attivare il pensiero visivo, configura [Esecuzione del codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it) come strumento. Il modello utilizzerà automaticamente
il codice per manipolare le immagini quando necessario.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Per ulteriori dettagli sull'esecuzione del codice con le immagini, vedi [Esecuzione del codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it#images).

### Risposte della funzione multimodale

[Chiamata di funzione multimodale](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it#multimodal)
consente agli utenti di avere risposte di funzione contenenti
oggetti multimodali, consentendo un migliore utilizzo delle funzionalità
di chiamata di funzione del modello. La chiamata di funzione standard supporta solo risposte di funzione basate su testo:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -H "Api-Revision: 2026-05-20" \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combinare strumenti integrati e chiamata di funzione

Gemini 3 consente l'utilizzo di strumenti integrati (come la Ricerca Google, il contesto dell'URL e [altro](https://ai.google.dev/gemini-api/docs/tools?hl=it)) e di strumenti di [chiamata di funzione](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it) personalizzati nella stessa chiamata API, consentendo workflow più complessi.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Migrazione da Gemini 2.5

Gemini 3 è la nostra famiglia di modelli più potente finora e offre un miglioramento graduale rispetto a Gemini 2.5. Quando esegui la migrazione, tieni presente quanto segue:

- **Ragionamento**:se in precedenza utilizzavi l'ingegneria dei prompt complessa (come
  la catena di pensiero) per forzare Gemini 2.5 a ragionare, prova Gemini 3 con
  `thinking_level: "high"` e prompt semplificati.
- **Impostazioni della temperatura**:se il codice esistente imposta esplicitamente la temperatura
  (soprattutto su valori bassi per output deterministici), ti consigliamo di rimuovere questo
  parametro e utilizzare il valore predefinito di Gemini 3 pari a 1,0 per evitare potenziali problemi di loop
  o un peggioramento delle prestazioni per attività complesse.
- **Comprensione di PDF e documenti**:se ti affidavi a un comportamento specifico per l'analisi dei documenti densi, testa la nuova
  impostazione `media_resolution_high` per garantire una precisione continua.
- **Utilizzo dei token**:la migrazione alle impostazioni predefinite di Gemini 3 potrebbe **aumentare** l'utilizzo dei token per i PDF, ma **diminuirlo** per i video. Se le richieste ora superano
  la finestra contestuale a causa di risoluzioni predefinite più elevate, ti consigliamo di
  ridurre esplicitamente la risoluzione dei contenuti multimediali.
- **Segmentazione delle immagini**:le funzionalità di segmentazione delle immagini (che restituiscono maschere a livello di pixel per gli oggetti) non sono supportate in Gemini 3 Pro o Gemini 3 Flash. Per i
  carichi di lavoro che richiedono la segmentazione delle immagini integrata, consigliamo di continuare a
  utilizzare Gemini 2.5 Flash con la funzionalità di ragionamento disattivata o [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it).
- **Utilizzo del computer**:Gemini 3 Pro e Gemini 3 Flash supportano l'[utilizzo del computer](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=it). A differenza della serie 2.5, non è necessario
  utilizzare un modello separato per accedere allo strumento Utilizzo del computer.
- **Supporto degli strumenti**: [la combinazione di strumenti integrati con la chiamata di funzione](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=it) è ora supportata per i modelli Gemini 3. Ora è supportato anche il [grounding di Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=it) per i modelli Gemini 3.

## Compatibilità con OpenAI

Per gli utenti che utilizzano il [livello di compatibilità OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it),
i parametri standard (`reasoning_effort` di OpenAI) vengono mappati automaticamente
agli equivalenti di Gemini (`thinking_level`).

## Best practice per la creazione di prompt

Gemini 3 è un modello di ragionamento che cambia il modo in cui devi formulare i prompt.

- **Istruzioni precise:** sii conciso nei prompt di input. Gemini 3 risponde
  meglio a istruzioni dirette e chiare. Potrebbe analizzare in modo eccessivo tecniche di prompt engineering complesse o troppo dettagliate utilizzate per i modelli precedenti.
- **Livello di dettaglio dell'output:** per impostazione predefinita, Gemini 3 è meno prolisso e preferisce
  fornire risposte dirette ed efficienti. Se il tuo caso d'uso richiede una persona più
  conversazionale o "loquace", devi indirizzare esplicitamente il modello nel
  prompt (ad es. "Spiega questo come un assistente amichevole e loquace").
- **Gestione del contesto**:quando lavori con set di dati di grandi dimensioni (ad es. libri interi, codebase o video lunghi), inserisci le istruzioni o le domande specifiche alla fine del prompt, dopo il contesto dei dati. Ancora il ragionamento del modello ai
  dati forniti iniziando la domanda con una frase come "In base alle
  informazioni precedenti...".

Scopri di più sulle strategie di progettazione dei prompt nella [guida all'ingegneria dei prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it).

## Domande frequenti

1. **Qual è il knowledge cutoff per Gemini 3?** I modelli Gemini 3 hanno un knowledge cutoff di gennaio 2025. Per informazioni più recenti, utilizza lo strumento
   [Search Grounding](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it).
2. **Quali sono i limiti della finestra contestuale?** I modelli Gemini 3 supportano una finestra contestuale di input di 1 milione di token e fino a 64.000 token di output.
3. **Esiste un livello senza costi per Gemini 3?** Gemini 3 Flash
   `gemini-3-flash-preview` ha un livello senza costi nell'API Gemini. Puoi provare
   Gemini 3.1 Pro e 3 Flash senza costi in Google AI Studio, ma non
   è disponibile un livello senza costi per `gemini-3.1-pro-preview` nell'API Gemini.
4. **Il mio vecchio codice `thinking_budget` continuerà a funzionare?** Sì, `thinking_budget` è
   ancora supportato per la compatibilità con le versioni precedenti, ma ti consigliamo di eseguire la migrazione a
   `thinking_level` per un rendimento più prevedibile. Non utilizzare entrambi nella stessa
   richiesta.
5. **Gemini 3 supporta l'API Batch?** Sì, Gemini 3 supporta l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it).
6. **La memorizzazione nella cache del contesto è supportata?** Sì, la [memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=it) è supportata per Gemini 3.
7. **Quali strumenti sono supportati in Gemini 3?** Gemini 3 supporta
   [Ricerca Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it),
   [Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=it),
   [Ricerca file](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=it),
   [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it) e
   [Contesto URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=it). Supporta anche
   la [chiamata di funzioni](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it) standard per
   i tuoi strumenti personalizzati e in
   [combinazione con strumenti integrati](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=it).
8. **Che cos'è `gemini-3.1-pro-preview-customtools`?** Se utilizzi
   `gemini-3.1-pro-preview` e il modello ignora i tuoi strumenti personalizzati a favore dei
   comandi bash, prova invece il modello `gemini-3.1-pro-preview-customtools`.
   Scopri di più [qui][customtools-model].

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-29 UTC."],[],[]]
