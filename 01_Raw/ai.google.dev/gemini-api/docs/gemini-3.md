---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=it
fetched_at: 2026-05-18T05:18:07.169138+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida per gli sviluppatori di Gemini 3

Gemini 3 è la nostra famiglia di modelli più intelligente di sempre, basata su un ragionamento all'avanguardia. È progettato per dare vita a qualsiasi idea
padroneggiando i workflow agentici, la programmazione autonoma e le attività multimodali complesse.
Questa guida illustra le funzionalità principali della famiglia di modelli Gemini 3 e come ottenere il massimo.

[Prova l'anteprima di Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=it)
[Prova l'anteprima di Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=it)
[Prova Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=it)
[Prova Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=it)

Esplora la nostra [raccolta di app Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=it) per
vedere come il modello gestisce il ragionamento avanzato, la programmazione autonoma e le attività
multimodali complesse.

Inizia con poche righe di codice:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Scopri la serie Gemini 3

Gemini 3.1 Pro è ideale per le attività complesse che
richiedono un'ampia conoscenza del mondo e un ragionamento avanzato tra le varie modalità.

Gemini 3 Flash è il nostro ultimo modello della serie 3, con intelligenza di livello Pro alla velocità e al prezzo di Flash.

Nano Banana Pro (noto anche come Gemini 3 Pro Image) è il nostro modello di generazione di immagini di qualità più elevata, mentre Nano Banana 2 (noto anche come Gemini 3.1 Flash Image) è l'equivalente ad alto volume, alta efficienza e prezzo più basso.

Gemini 3.1 Flash-Lite è il nostro modello più efficiente, progettato per attività a costi contenuti e
con volumi elevati.

| ID modello | Finestra contestuale (in entrata / in uscita) | Knowledge Cutoff | Prezzi (input / output)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 milione / 64.000 | Gennaio 2025 | 0,25 $ (testo, immagine, video), 0,50 $ (audio) / 1,50 $ |
| **gemini-3.1-flash-lite-preview** | 1 milione / 64.000 | Gennaio 2025 | 0,25 $ (testo, immagine, video), 0,50 $ (audio) / 1,50 $ |
| **gemini-3.1-flash-image-preview** | 128.000 / 32.000 | Gennaio 2025 | 0,25 $ (input di testo) / 0,067 $ (output di immagine)\*\* |
| **gemini-3.1-pro-preview** | 1 milione / 64.000 | Gennaio 2025 | 2 $ / 12 $ (<200.000 token)   4 $ / 18 $ (>200.000 token) |
| **gemini-3-flash-preview** | 1 milione / 64.000 | Gennaio 2025 | 0,50 $ / 3 $ |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Gennaio 2025 | 2 $ (input di testo) / 0,134 $ (output di immagine)\*\* |

*\* I prezzi si riferiscono a 1 milione di token, se non diversamente indicato.*
*\*\* Il prezzo delle immagini varia in base alla risoluzione. Per maggiori dettagli, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).*

Per limiti, prezzi e informazioni aggiuntive dettagliati, consulta la
[pagina dei modelli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

## Nuove funzionalità dell'API in Gemini 3

Gemini 3 introduce nuovi parametri progettati per offrire agli sviluppatori un maggiore controllo su
latenza, costi e fedeltà multimodale.

### Livello di ragionamento

I modelli della serie Gemini 3 utilizzano per impostazione predefinita il ragionamento dinamico per analizzare i prompt. Puoi utilizzare il parametro `thinking_level`, che controlla la
**profondità massima** del processo di ragionamento interno del modello prima che produca una
risposta. Gemini 3 tratta questi livelli come quote relative per il ragionamento
piuttosto che come garanzie di token rigorose.

Se `thinking_level` non è specificato, Gemini 3 utilizzerà `high` come valore predefinito. Per
risposte più rapide e a bassa latenza quando non è necessario un ragionamento complesso, puoi
limitare il livello di pensiero del modello a `low`.

| Livello di ragionamento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrizione |
| --- | --- | --- | --- | --- |
| **`minimal`** | Non supportato | Supportato (valore predefinito) | Supportato | Corrisponde all'impostazione "nessun pensiero" per la maggior parte delle query. Il modello potrebbe pensare in modo molto minimale per attività di programmazione complesse. Riduce al minimo la latenza per le applicazioni di chat o a throughput elevato. Tieni presente che `minimal` non garantisce che il pensiero sia disattivato. |
| **`low`** | Supportato | Supportato | Supportato | Riduce al minimo la latenza e i costi. Ideale per applicazioni semplici di follow-up delle istruzioni, chat o ad alto throughput. |
| **`medium`** | Supportato | Supportato | Supportato | Pensiero equilibrato per la maggior parte delle attività. |
| **`high`** | Supportato (predefinito, dinamico) | Supportato (dinamico) | Supportato (predefinito, dinamico) | Massimizza la profondità del ragionamento. Il modello potrebbe impiegare molto più tempo per raggiungere un primo token di output (non di pensiero), ma l'output sarà più ragionato. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Risoluzione dei contenuti multimediali

Gemini 3 introduce un controllo granulare sull'elaborazione della visione multimodale tramite il parametro
`media_resolution`. Risoluzioni più elevate migliorano la capacità del modello di
leggere testi piccoli o identificare piccoli dettagli, ma aumentano l'utilizzo di token e la latenza.
Il parametro `media_resolution` determina il **numero massimo di token
allocati per ogni immagine di input o frame video.**

Ora puoi impostare la risoluzione su `media_resolution_low`,
`media_resolution_medium`, `media_resolution_high` o
`media_resolution_ultra_high` per ogni parte multimediale o a livello globale (tramite
`generation_config`, globale non disponibile per l'ultra definizione). Se non specificato, il modello utilizza i valori predefiniti ottimali in base al tipo di media.

**Impostazioni consigliate**

| Tipo di media | Impostazione consigliata | Token massimi | Indicazioni per l'utilizzo |
| --- | --- | --- | --- |
| **Immagini** | `media_resolution_high` | 1120 | Consigliato per la maggior parte delle attività di analisi delle immagini per garantire la massima qualità. |
| **PDF** | `media_resolution_medium` | 560 | Ottimale per la comprensione dei documenti; la qualità in genere satura a `medium`. L'aumento a `high` raramente migliora i risultati dell'OCR per i documenti standard. |
| **Video** (Generale) | `media_resolution_low` (o `media_resolution_medium`) | 70 (per frame) | **Nota**:per i video, le impostazioni `low` e `medium` vengono trattate in modo identico (70 token) per ottimizzare l'utilizzo del contesto. Questo è sufficiente per la maggior parte delle attività di riconoscimento e descrizione delle azioni. |
| **Video** (con molto testo) | `media_resolution_high` | 280 (per frame) | Obbligatorio solo quando il caso d'uso prevede la lettura di testo denso (OCR) o piccoli dettagli all'interno dei fotogrammi video. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatura

Per tutti i modelli Gemini 3, ti consigliamo vivamente di mantenere il parametro di temperatura
sul valore predefinito di `1.0`.

Mentre i modelli precedenti spesso traevano vantaggio dalla regolazione della temperatura per controllare
la creatività rispetto al determinismo, le capacità di ragionamento di Gemini 3 sono ottimizzate
per l'impostazione predefinita. La modifica della temperatura (impostandola su un valore inferiore a 1,0) può
comportare un comportamento imprevisto, come loop o prestazioni ridotte,
in particolare in attività matematiche o di ragionamento complesse.

### Firme dei pensieri

Gemini 3 utilizza le [firme del pensiero](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it) per
mantenere il contesto del ragionamento tra le chiamate API. Queste firme sono rappresentazioni
criptate del processo di pensiero interno del modello. Per garantire che il modello
mantenga le sue capacità di ragionamento, devi restituire queste firme al
modello nella tua richiesta esattamente come sono state ricevute:

- **Chiamata di funzioni (rigorosa)**: l'API applica una convalida rigorosa al
  "Current Turn". Le firme mancanti genereranno un errore 400.
- **Testo/Chat**:la convalida non è rigorosamente applicata, ma l'omissione delle firme peggiorerà la qualità del ragionamento e delle risposte del modello.
- **Generazione/modifica di immagini (rigorosa)**: l'API applica una convalida rigorosa a tutte le parti del modello, inclusa una `thoughtSignature`. Le firme mancanti genereranno un errore 400.

#### Chiamata di funzione (convalida rigorosa)

Quando Gemini genera un `functionCall`, si basa su `thoughtSignature` per
elaborare correttamente l'output dello strumento nel turno successivo. La sezione "Turno attuale"
include tutti i passaggi del modello (`functionCall`) e dell'utente (`functionResponse`)
che si sono verificati dall'ultimo messaggio standard **Utente** `text`.

- **Chiamata di una singola funzione**:la parte `functionCall` contiene una firma. Devi restituirlo.
- **Chiamate di funzioni parallele**:solo la prima parte `functionCall` dell'elenco conterrà la firma. Devi restituire le parti nell'ordine esatto in cui le hai ricevute.
- **Multistep (sequenziale):** se il modello chiama uno strumento, riceve un risultato e chiama *un altro* strumento (nello stesso turno), **entrambe** le chiamate di funzione hanno firme. Devi restituire **tutte** le firme accumulate nella cronologia.

#### Testo e streaming

Per la generazione di chat o testo standard, la presenza di una firma non è
garantita.

- **Non in streaming**: l'ultima parte dei contenuti della risposta potrebbe contenere un
  `thoughtSignature`, anche se non è sempre presente. Se viene restituito, devi
  rimandarlo indietro per mantenere le migliori prestazioni.
- **Streaming**: se viene generata una firma, potrebbe arrivare in un blocco finale
  che contiene una parte di testo vuota. Assicurati che l'analizzatore di stream controlli le firme anche se il campo di testo è vuoto.

#### Generazione e modifica di immagini

Per `gemini-3-pro-image-preview` e `gemini-3.1-flash-image-preview`, le firme
del pensiero sono fondamentali
per la modifica conversazionale. Quando chiedi al modello di modificare un'immagine, si basa sul `thoughtSignature` del turno precedente per comprendere la composizione e la logica dell'immagine originale.

- **Modifica**:le firme sono garantite nella prima parte dopo i pensieri
  della risposta (`text` o `inlineData`) e in ogni parte `inlineData`
  successiva. Per evitare errori, devi restituire tutte queste firme.

#### Esempi di codice

#### Chiamate di funzione a più passaggi (sequenziali)

L'utente pone una domanda che richiede due passaggi separati (Controlla volo -> Prenota taxi) in un solo turno.   
  
**Passaggio 1: simula le chiamate allo strumento di volo.**  
Il modello restituisce una firma `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Passaggio 2: l'utente invia il risultato del volo**  
Dobbiamo inviare di nuovo `<Sig_A>` per mantenere il filo logico del modello.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  { 
    "role": "model", 
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} }, 
        "thoughtSignature": "<Sig_A>" // REQUIRED
      } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Passaggio 3: il modello chiama lo strumento per i taxi**  
Il modello ricorda il ritardo del volo tramite `<Sig_A>` e ora decide di prenotare un taxi. Genera una *nuova* firma `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Passaggio 4: l'utente invia il risultato del taxi**  
Per completare il turno, devi inviare di nuovo l'intera catena: `<Sig_A>` E `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Chiamata di funzione parallela

L'utente chiede: "Controlla il meteo a Parigi e Londra". Il modello restituisce due chiamate di funzioni in una sola risposta.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Testo/Ragionamento nel contesto (nessuna convalida)

L'utente pone una domanda che richiede un ragionamento contestuale senza strumenti esterni. Sebbene non sia convalidata rigorosamente, l'inclusione della firma aiuta il modello a mantenere la catena di ragionamento per le domande successive.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Generazione e modifica di immagini

Per la generazione di immagini, le firme vengono convalidate rigorosamente. Vengono visualizzati nella **prima parte** (testo o immagine) e in **tutte le parti successive dell'immagine**. Tutte le carte devono essere restituite nel turno successivo.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Eseguire la migrazione da altri modelli

Se trasferisci una traccia di conversazione da un altro modello (ad es. Gemini
2.5) o inserisci una chiamata di funzione personalizzata che non è stata generata da Gemini 3,
non avrai una firma valida.

Per ignorare la convalida rigorosa in questi scenari specifici, compila il campo con
questa stringa fittizia specifica: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Output strutturati con strumenti

I modelli Gemini 3 ti consentono di combinare gli [output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) con strumenti integrati, tra cui
[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it), [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it), [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
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
  }
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
previsioni meteo o grafici azionari, prima di utilizzare la [Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) per la verifica prima di generare immagini
ad alta fedeltà.

**Funzionalità nuove e migliorate:**

- **Rendering di testo e 4K:** genera testo e diagrammi nitidi e leggibili con risoluzioni fino a 2K e 4K.
- **Generazione fondata:** utilizza lo strumento `google_search` per verificare i fatti e
  generare immagini basate su informazioni del mondo reale. Grounding con la Ricerca *Immagini*
  Google disponibile per Gemini 3.1 Flash Image.
- **Modifica conversazionale**:modifica di immagini in più passaggi semplicemente chiedendo
  di apportare modifiche (ad es. "Crea uno sfondo con un tramonto"). Questo flusso di lavoro si basa sulle
  **Firme del pensiero** per preservare il contesto visivo tra i turni.

Per informazioni dettagliate su proporzioni, flussi di lavoro di modifica e opzioni di configurazione, consulta la [guida alla generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Risposta di esempio**

![Meteo Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=it)

### Esecuzione del codice con immagini

Gemini 3 Flash può trattare la visione come un'indagine attiva, non solo come uno sguardo statico. Combinando il ragionamento con l'[esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it), il modello formula un piano, quindi scrive ed esegue codice Python per ingrandire, ritagliare, annotare o manipolare in altro modo le immagini passo dopo passo per basare visivamente le sue risposte.

**Casi d'uso:**

- **Zoom e ispezione**:il modello rileva implicitamente quando i dettagli sono troppo
  piccoli (ad es. la lettura di un indicatore o di un numero di serie distante) e scrive codice per ritagliare
  e riesaminare l'area a una risoluzione più elevata.
- **Matematica visiva e grafici**:il modello può eseguire calcoli in più passaggi utilizzando
  il codice (ad es. la somma delle voci di una ricevuta o la generazione di un grafico Matplotlib
  dai dati estratti).
- **Annotazione delle immagini:** il modello può disegnare frecce, rettangoli di selezione o altre annotazioni direttamente sulle immagini per rispondere a domande spaziali come "Dove va questo oggetto?".

Per attivare il pensiero visivo, configura [Esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) come strumento. Il modello utilizzerà automaticamente
il codice per manipolare le immagini quando necessario.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Per maggiori dettagli sull'esecuzione del codice con le immagini, vedi [Esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it#images).

### Risposte delle funzioni multimodali

[Chiamata di funzione multimodale](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#multimodal)
consente agli utenti di avere risposte di funzione contenenti
oggetti multimodali, consentendo un migliore utilizzo delle funzionalità
di chiamata di funzione del modello. La chiamata di funzione standard supporta solo risposte di funzione basate su testo:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Combinare strumenti integrati e chiamata di funzione

Gemini 3 consente l'utilizzo di strumenti integrati (come la Ricerca Google, il contesto dell'URL e [altro](https://ai.google.dev/gemini-api/docs/tools?hl=it)) e di strumenti di [chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) personalizzati nella stessa chiamata API, consentendo workflow più complessi. Scopri di più nella pagina [Combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Migrazione da Gemini 2.5

Gemini 3 è la nostra famiglia di modelli più potente finora e offre un miglioramento graduale rispetto a Gemini 2.5. Quando esegui la migrazione, tieni presente quanto segue:

- **Ragionamento**:se in precedenza utilizzavi tecniche di ingegneria dei prompt complesse (come
  la catena di pensiero) per forzare Gemini 2.5 a ragionare, prova Gemini 3 con
  `thinking_level: "high"` e prompt semplificati.
- **Impostazioni della temperatura**:se il codice esistente imposta esplicitamente la temperatura
  (soprattutto su valori bassi per output deterministici), ti consigliamo di rimuovere questo
  parametro e utilizzare il valore predefinito di Gemini 3 pari a 1,0 per evitare potenziali problemi di loop
  o un peggioramento delle prestazioni per attività complesse.
- **Comprensione di PDF e documenti**:se ti affidavi a un comportamento specifico per l'analisi di documenti densi, prova la nuova
  impostazione `media_resolution_high` per garantire una precisione continua.
- **Utilizzo dei token**:la migrazione alle impostazioni predefinite di Gemini 3 potrebbe **aumentare** l'utilizzo dei token
  per i PDF, ma **diminuire** l'utilizzo dei token per i video. Se le richieste ora superano
  la finestra contestuale a causa di risoluzioni predefinite più elevate, ti consigliamo di
  ridurre esplicitamente la risoluzione dei contenuti multimediali.
- **Segmentazione delle immagini**:le funzionalità di segmentazione delle immagini (che restituiscono maschere a livello di pixel per gli oggetti) non sono supportate in Gemini 3 Pro o Gemini 3 Flash. Per i carichi di lavoro che richiedono la segmentazione dell'immagine nativa, ti consigliamo di continuare a utilizzare Gemini 2.5 Flash con la funzionalità di ragionamento disattivata o [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it).
- **Utilizzo del computer**:Gemini 3 Pro e Gemini 3 Flash supportano l'[utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it). A differenza della serie 2.5, non è necessario
  utilizzare un modello separato per accedere allo strumento Utilizzo del computer.
- **Supporto degli strumenti**: [la combinazione di strumenti integrati e chiamate di funzione](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it) è ora supportata per i modelli Gemini 3. Ora è supportato anche il [grounding di Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) per i modelli Gemini 3.

## Compatibilità con OpenAI

Per gli utenti che utilizzano il [livello di compatibilità OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it),
i parametri standard (`reasoning_effort` di OpenAI) vengono mappati automaticamente agli equivalenti
di Gemini (`thinking_level`).

## Best practice per la creazione di prompt

Gemini 3 è un modello di ragionamento che cambia il modo in cui devi creare i prompt.

- **Istruzioni precise**:sii conciso nei prompt di input. Gemini 3 risponde
  meglio a istruzioni dirette e chiare. Potrebbe analizzare in modo eccessivo tecniche di prompt engineering complesse o troppo
  verbose utilizzate per i modelli precedenti.
- **Livello di dettaglio dell'output:** per impostazione predefinita, Gemini 3 è meno prolisso e preferisce
  fornire risposte dirette ed efficienti. Se il tuo caso d'uso richiede una persona più
  conversazionale o "loquace", devi indirizzare esplicitamente il modello nel
  prompt (ad es. "Spiega questo come un assistente amichevole e loquace").
- **Gestione del contesto**:quando lavori con set di dati di grandi dimensioni (ad es. libri interi, codebase o video lunghi), inserisci le istruzioni o le domande specifiche alla fine del prompt, dopo il contesto dei dati. Ancora il ragionamento del modello ai
  dati forniti iniziando la domanda con una frase come "In base alle
  informazioni riportate sopra…".

Scopri di più sulle strategie di progettazione dei prompt nella [guida all'ingegneria dei prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it).

## Domande frequenti

1. **Qual è il knowledge cutoff per Gemini 3?** I modelli Gemini 3 hanno un knowledge cutoff di gennaio 2025. Per informazioni più recenti, utilizza lo strumento
   [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=it).
2. **Quali sono i limiti della finestra contestuale?** I modelli Gemini 3 supportano una finestra contestuale di input di 1 milione di token e fino a 64.000 token di output.
3. **Esiste un livello senza costi per Gemini 3?** Gemini 3 Flash
   `gemini-3-flash-preview` e 3.1 Flash-Lite `gemini-3.1-flash-lite` hanno
   livelli senza costi nell'API Gemini. Puoi provare Gemini 3.1 Pro e 3 Flash senza costi in
   Google AI Studio, ma non è disponibile alcun livello senza costi per
   `gemini-3.1-pro-preview` nell'API Gemini.
4. **Il mio vecchio codice `thinking_budget` continuerà a funzionare?** Sì, `thinking_budget` è
   ancora supportato per la compatibilità con le versioni precedenti, ma ti consigliamo di eseguire la migrazione a
   `thinking_level` per un rendimento più prevedibile. Non utilizzare entrambi nella stessa
   richiesta.
5. **Gemini 3 supporta l'API Batch?** Sì, Gemini 3 supporta l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it).
6. **La memorizzazione nella cache del contesto è supportata?** Sì, la [memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it) è supportata per Gemini 3.
7. **Quali strumenti sono supportati in Gemini 3?** Gemini 3 supporta la [Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it), il [Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it), la [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it),
   l'[esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e il [contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it). Supporta anche la [chiamata di funzioni](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) standard per i tuoi strumenti personalizzati,
   e in [combinazione con strumenti integrati](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).
8. **Che cos'è `gemini-3.1-pro-preview-customtools`?** Se utilizzi `gemini-3.1-pro-preview` e il modello ignora i tuoi strumenti personalizzati a favore dei comandi bash, prova invece il modello `gemini-3.1-pro-preview-customtools`. Scopri di più [qui](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it#gemini-31-pro-preview-customtools).

## Passaggi successivi

- Inizia a usare il [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=it#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Consulta la guida dedicata del Cookbook sui [livelli di pensiero](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=it#gemini3) e su come eseguire la migrazione dal budget di pensiero ai livelli di pensiero.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-13 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-13 UTC."],[],[]]
