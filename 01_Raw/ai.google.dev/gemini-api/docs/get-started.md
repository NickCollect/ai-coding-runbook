---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=it
fetched_at: 2026-09-07T05:39:59.448862+00:00
title: "Guida introduttiva \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida introduttiva

Questa guida ti aiuta a iniziare a utilizzare l'API Gemini utilizzando l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it). Eseguirai la tua prima chiamata API in meno di un minuto ed esplorerai la generazione di testo, la comprensione multimodale, la generazione di immagini, l'output strutturato, gli strumenti, la chiamata di funzione, gli agenti e l'esecuzione in background.

L'API Interactions è disponibile tramite gli SDK [Python](https://github.com/googleapis/python-genai) e [JavaScript](https://github.com/googleapis/js-genai), nonché tramite REST.

## 1. Ottieni una chiave API

Per utilizzare l'API Gemini, devi disporre di una chiave API per autenticare le richieste, applicare limiti di sicurezza e monitorare l'utilizzo del tuo account.

- Google AI Studio crea automaticamente un progetto e una chiave API per i nuovi utenti.
  Puoi copiarla dalla [pagina Chiavi API](https://aistudio.google.com/api-keys?hl=it).
- Se hai bisogno di una nuova chiave, fai clic su **Crea chiave API** in AI Studio e segui la
  finestra di dialogo per aggiungere una nuova coppia chiave-progetto.

[Crea una chiave API Gemini](https://aistudio.google.com/apikey?hl=it)

Imposta la chiave come variabile di ambiente:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Eseguire l'upgrade al livello a pagamento

L'upgrade al livello a pagamento aumenta i limiti di frequenza e richiede la configurazione
di fatturazione Cloud.

- Fai clic su **Configura la fatturazione** nelle pagine [Chiavi API](https://aistudio.google.com/api-keys?hl=it) o [Progetti](https://aistudio.google.com/projects?hl=it) di AI Studio.
- Segui la finestra di dialogo Fatturazione Cloud per creare o collegare un account di fatturazione, aggiungere un metodo di pagamento e pagare in anticipo un minimo di 10 $ (o l'equivalente in valuta) in crediti a pagamento.
- Visualizza l'utilizzo dell'API in [Google AI Studio](https://aistudio.google.com/usage?hl=it)
  in **Dashboard** > **Utilizzo**.

Per ulteriori informazioni, consulta la [pagina Fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it).

## 2. Installa l'SDK ed effettua la tua prima chiamata

Installa l'SDK e genera il testo con una singola chiamata API.

### Python

Installa l'SDK:

```
pip install -U google-genai
```

Inizializza il client ed effettua una richiesta:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

Installa l'SDK:

```
npm install @google/genai
```

Inizializza il client ed effettua una richiesta:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**Risposta:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Quando utilizzi REST, l'API restituisce la risorsa `Interaction` completa contenente metadati, statistiche di utilizzo e la cronologia passo passo della svolta.

Sebbene gli SDK espongano la risposta completa, forniscono anche proprietà pratiche come `interaction.output_text` e `interaction.output_image` per accedere direttamente agli output finali. Scopri di più sulla struttura della risposta nella [Panoramica delle interazioni](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) o leggi la [guida alla generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it) per informazioni dettagliate sulle istruzioni di sistema e sulla configurazione della generazione.

## 3. Visualizzare in streaming la risposta

Per interazioni più fluide, riproduci in streaming la risposta man mano che viene generata. Ogni evento `step.delta` fornisce un blocco di testo che puoi visualizzare immediatamente.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

Durante lo streaming, il server risponde con un flusso di eventi inviati dal server (SSE). Ogni evento include un tipo e dati JSON.

**Risposta:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

Per un'analisi dettagliata della gestione degli eventi di streaming e dei tipi di delta, consulta la [guida alle interazioni di streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=it).

## 4. Conversazioni a più turni

L'API Interactions supporta le conversazioni multi-turno con due approcci:

- **Stateful (consigliato)**: continua una conversazione sul server utilizzando `previous_interaction_id`. Ideale per la maggior parte dei workflow di chat e agentici in cui vuoi che il server gestisca la cronologia e ottimizzi la memorizzazione nella cache.
- **Senza stato**: gestisci la cronologia della conversazione sul client passando tutti i turni precedenti (inclusi i passaggi intermedi del modello e degli strumenti) in ogni richiesta.

### Stateful (consigliato)

Concatenare le interazioni passando `previous_interaction_id`. Il server gestisce l'intera cronologia delle conversazioni per te.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### Stateless

Imposta `store=false` e gestisci la cronologia delle conversazioni sul lato client. Devi conservare e inviare nuovamente tutti i passaggi generati dal modello (inclusi i passaggi `thought` e `function_call`) esattamente come li hai ricevuti.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**Risposta:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

La seconda interazione restituisce un oggetto di risposta completo che include solo i nuovi passaggi, ma si basa sul contesto del turno precedente. Scopri di più sul mantenimento dello stato nella [guida alle conversazioni multi-turn](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#multi-turn-conversations) o esplora la [modalità stateless](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#stateless-conversations) per la gestione della cronologia lato client.

## 5. Comprensione multimodale

I modelli Gemini comprendono immagini, audio, video e documenti in modo nativo. Trasmetti contenuti multimediali insieme al testo in un'unica richiesta.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**Risposta:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Scopri come passare immagini, video e file audio nella [guida alla comprensione delle immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it).

[hearing

Comprensione dell'audio

Trascrivi, riassumi o rispondi a domande sui file audio.](https://ai.google.dev/gemini-api/docs/audio?hl=it)
[videocam

Comprensione dei video

Analizza i contenuti video, individua gli eventi e descrivi le azioni.](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it)
[description

Elaborazione di documenti

Estrai informazioni da PDF e altri formati di documenti.](https://ai.google.dev/gemini-api/docs/document-processing?hl=it)

## 6. Generazione multimodale

Gemini può generare immagini in modo nativo utilizzando i modelli di immagini [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=it).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**Risposta:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

Quando il modello genera un'immagine, restituisce i dati dell'immagine codificati in base64 in un passaggio all'interno dell'array `steps`, nonché tramite la proprietà di convenienza `output_image`. Consulta la [guida alla generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) per scoprire di più su proporzioni, modifica delle immagini e riferimenti.

[record\_voice\_over

Generazione di voce

Genera una voce espressiva con più relatori con Gemini 3.1 Flash TTS.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)
[music\_note

Generazione di musica

Crea clip e brani completi con Lyria 3.](https://ai.google.dev/gemini-api/docs/music-generation?hl=it)

## 7. Utilizzare l'output strutturato

Configura il modello in modo che restituisca JSON che corrisponda a uno schema che definisci. L'output strutturato funziona con [Pydantic](https://docs.pydantic.dev/latest/) (Python) e [Zod](https://zod.dev/) (JavaScript).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**Risposta:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Il blocco di testo di output contiene una stringa JSON valida conforme esattamente allo schema richiesto. Per scoprire come definire strutture più complesse e schemi ricorsivi, consulta la [guida all'output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it).

## 8. Utilizzare gli strumenti

Basare la risposta del modello su informazioni in tempo reale con la Ricerca Google. L'API esegue automaticamente la ricerca, elabora i risultati e restituisce le citazioni.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**Risposta:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

I passaggi della ricerca sono descritti in dettaglio nella cronologia delle interazioni e l'output finale include citazioni in linea che rimandano a fonti web.

Puoi scoprire come estrarre le citazioni della ricerca nella [guida alla base della Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) o vedere come combinare più strumenti nella [guida alla combinazione di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

[code

Eseguire il codice

Esegui il codice Python in un ambiente Borg sandbox sicuro.](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)
[link

Contesto URL

Trasmetti gli URL web pubblici direttamente per basare le risposte sui contenuti delle pagine web.](https://ai.google.dev/gemini-api/docs/url-context?hl=it)
[search

Ricerca di file

Indicizza ed esegui ricerche nei documenti e nei file multimediali caricati.](https://ai.google.dev/gemini-api/docs/file-search?hl=it)
[map

Google Maps

Basare le risposte su dati geospaziali e di posizione reali.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)
[computer

Uso del computer

Automazione del browser e interazione con lo schermo.](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)

## 9. Chiamare le proprie funzioni

La chiamata di funzione consente di connettere il modello al codice. Dichiari il nome e i parametri di una funzione, il modello decide quando chiamarla e restituisce argomenti strutturati, tu la esegui localmente e invii il risultato.

### Stateful (consigliato)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Stateless

Puoi anche utilizzare la chiamata di funzioni in modalità stateless gestendo la cronologia della conversazione sul lato client e impostando `store=false`. In modalità stateless, devi trasmettere la cronologia completa della conversazione nel campo `input` di ogni richiesta successiva. Questa cronologia deve includere:

1. Il passaggio iniziale `user_input`.
2. Tutti i passaggi generati dal modello restituiti nel Turno 1 (inclusi i passaggi `thought` e `function_call`) esattamente come ricevuti.
3. Il passaggio `function_result` contenente l'output della funzione eseguita.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**Risposta:**

Durante il Turn 1, il modello restituisce una risposta con lo stato `requires_action` e il passaggio `function_call`:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Dopo aver eseguito la funzione in locale e inviato il risultato (Turno 2), viene restituita l'interazione finale completata:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Per funzionalità avanzate come la chiamata di funzione parallela o le modalità di scelta della funzione, consulta la [guida alla chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).

## 10. Eseguire un agente gestito

Gli agenti gestiti vengono eseguiti in una sandbox remota con accesso a strumenti come l'esecuzione di codice e la gestione dei file. Passa un `agent` anziché un `model` e imposta `environment="remote"`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

Puoi anche definire e salvare [agenti personalizzati](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it) con istruzioni, competenze e origini dati personalizzate.

[rocket\_launch

Guida rapida

Effettua la tua prima chiamata con l'agente, trasmetti in streaming le risposte e crea un agente personalizzato.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it)
[smart\_toy

Agente Antigravity

Funzionalità, strumenti, input multimodale e prezzi per l'agente predefinito.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it)
[experiment

Agent in AI Studio

Playground visivo per la prototipazione di agenti senza scrivere codice.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it)

## 11. Eseguire attività in background

Imposta `background=True` per eseguire attività di lunga durata in modo asincrono. Sondaggio per i risultati con `interactions.get()`. Per maggiori dettagli, consulta la [Guida all'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**Risposta:**

La risposta iniziale viene restituita immediatamente con lo stato `in_progress`:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

Una volta eseguita completamente l'attività in background, il controllo dello stato dell'interazione restituisce:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.6-flash",
}
```

Scopri di più sull'esecuzione asincrona di modelli e agenti nella [guida all'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it).

## Passaggi successivi

- [Esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it): esegui attività di lunga durata in modo asincrono e gestisci lo stato.
- [Generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it): istruzioni di sistema, configurazione della generazione e pattern di testo avanzati.
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it): proporzioni, modifica delle immagini e riferimenti di stile.
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it): classificazione, rilevamento di oggetti e domande e risposte visive.
- [Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it): utilizza il chain-of-thought per attività complesse.
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it): modalità di funzione parallela, compositiva e vincolata.
- [Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it): grounding, citazioni e suggerimenti di ricerca.
- [Agenti gestiti](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it): agenti predefiniti con esecuzione del codice e gestione dei file.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it): ricerca autonoma in più passaggi con pianificazione e sintesi.
- [Output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it): schemi JSON, enumerazioni e definizioni di tipi ricorsivi.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
