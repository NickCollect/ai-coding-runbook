---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=it
fetched_at: 2026-09-28T06:35:44.596713+00:00
title: "Grounding con Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Grounding con Google Maps

Grounding con Google Maps collega le funzionalità generative di Gemini ai dati ricchi, fattuali e aggiornati di Google Maps. Questa funzionalità consente agli sviluppatori di incorporare facilmente funzionalità basate sulla località nelle loro applicazioni. Quando una query utente ha un contesto correlato ai dati di Maps, il modello Gemini utilizza Google Maps per fornire risposte fattualmente accurate e aggiornate pertinenti alla località o all'area generale specificata dall'utente.

- **Risposte accurate e basate sulla località:** sfrutta i dati estesi e attuali di Google Maps per le query geograficamente specifiche.
- **Personalizzazione avanzata:** personalizza i consigli e le informazioni in base alle località fornite dall'utente.

## Inizia

Questo esempio mostra come integrare Grounding con Google Maps nella tua applicazione per fornire risposte accurate e basate sulla località alle query degli utenti. Il prompt richiede consigli locali con una località utente facoltativa, consentendo al modello Gemini di utilizzare i dati di Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Come funziona Grounding con Google Maps

Grounding con Google Maps integra l'API Gemini con l'ecosistema Google Geo utilizzando l'API di Google Maps come origine di grounding. Quando la query di un utente contiene un contesto geografico, il modello Gemini può richiamare lo strumento Grounding con Google Maps. Il modello può quindi generare risposte basate sui dati di Google Maps pertinenti alla località fornita.

In genere, la procedura prevede i seguenti passaggi:

1. **Query utente:** un utente invia una query alla tua applicazione, che potrebbe includere un contesto geografico (ad es. "bar nelle vicinanze", "musei a San Francisco").
2. **Richiamo dello strumento:** il modello Gemini, riconoscendo l'intento geografico, richiama lo strumento Grounding con Google Maps. Questo strumento può essere fornito facoltativamente con la `latitude` e la `longitude` dell'utente. Lo strumento è uno strumento di ricerca testuale e si comporta in modo simile alla ricerca su Maps, in quanto le query locali ("nelle vicinanze") utilizzeranno le coordinate, mentre è improbabile che le query specifiche o non locali siano influenzate dalla località esplicita.
3. **Recupero dei dati:** il servizio Grounding con Google Maps esegue query su Google Maps per informazioni pertinenti (ad es. luoghi, recensioni, foto, indirizzi, orari di apertura).
4. **Generazione basata su dati di fatto:** i dati di Maps recuperati vengono utilizzati per informare la risposta del modello Gemini, garantendo accuratezza e pertinenza fattuali.
5. **Risposta:** il modello restituisce una risposta di testo, che include citazioni delle fonti di Google Maps.

## Perché e quando utilizzare Grounding con Google Maps

Grounding con Google Maps è ideale per le applicazioni che richiedono informazioni accurate, aggiornate e specifiche per la località. Migliora l'esperienza utente fornendo contenuti pertinenti e personalizzati supportati dall'ampio database di Google Maps di oltre 250 milioni di luoghi in tutto il mondo.

Devi utilizzare Grounding con Google Maps quando la tua applicazione deve:

- Fornire risposte complete e accurate a domande geograficamente specifiche.
- Creare agenti di viaggio conversazionali e guide locali.
- Consigliare punti di interesse in base alla località e alle preferenze dell'utente, come ristoranti o negozi.
- Creare esperienze basate sulla località per servizi social, di vendita al dettaglio o di consegna di cibo.

Grounding con Google Maps eccelle nei casi d'uso in cui la prossimità e i dati fattuali attuali sono fondamentali, ad esempio per trovare il "miglior bar nelle vicinanze" o ottenere indicazioni stradali.

## Metodi e parametri dell'API

Grounding con Google Maps viene esposto tramite l'API Gemini come strumento all'interno
del [`generateContent`](https://ai.google.dev/api/generate-content?hl=it) metodo. Per attivare e configurare
Grounding con Google Maps, includi un oggetto
[`googleMaps`](https://ai.google.dev/api/caching?hl=it#GoogleMaps) nel parametro `tools` della
richiesta.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Inoltre, lo strumento supporta il passaggio della località contestuale come `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Informazioni sulla risposta di grounding

Quando una risposta viene basata correttamente sui dati di Google Maps, la risposta
include un [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=it#GroundingMetadata) campo.
Questi dati strutturati sono essenziali per verificare le affermazioni e creare un'esperienza di citazione avanzata nella tua applicazione, nonché per soddisfare i requisiti di utilizzo del servizio.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

L'API Gemini restituisce le seguenti informazioni con le
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=it#GroundingMetadata):

- `groundingChunks`: array di oggetti contenenti le fonti `maps` (`uri`, `placeId` e `title`).
- `groundingSupports`: array di blocchi per collegare il testo della risposta del modello alle fonti in `groundingChunks`. Ogni blocco collega un intervallo di testo (definito da `startIndex` e `endIndex`) a uno o più `groundingChunkIndices`. Questa è la chiave per creare citazioni in linea.

Per uno snippet di codice che mostra come eseguire il rendering delle citazioni in linea nel testo, consulta [l'
esempio](https://ai.google.dev/gemini-api/docs/google-search?hl=it#attributing_sources_with_inline_citations)
nella documentazione di Grounding con la Ricerca Google.

## Casi d'uso

Grounding con Google Maps supporta una serie di casi d'uso basati sulla località. Gli esempi seguenti mostrano come diversi prompt e parametri possono sfruttare Grounding con Google Maps. Le informazioni nei Risultati fondati di Google Maps potrebbero differire dalle condizioni effettive.

### Gestire le domande specifiche per il luogo

Poni domande dettagliate su un luogo specifico per ottenere risposte basate sulle recensioni degli utenti di Google e su altri dati di Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Fornire personalizzazione basata sulla località

Ricevi consigli personalizzati in base alle preferenze di un utente e a un'area geografica specifica.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Aiutare con la pianificazione dell'itinerario

Genera piani di più giorni con indicazioni stradali e informazioni su varie località, perfetti per le applicazioni di viaggio.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Requisiti di utilizzo del servizio

Questa sezione descrive i requisiti di utilizzo del servizio per Grounding con Google Maps.

### Informa l'utente dell'utilizzo delle fonti di Google Maps

Con ogni risultato fondato di Google Maps, riceverai le fonti in `groundingChunks` che supportano ogni risposta. Vengono restituiti anche i seguenti metadati:

- URI di origine
- Titolo
- ID

Quando presenti i risultati di Grounding con Google Maps, devi specificare le fonti di Google Maps associate e informare gli utenti di quanto segue:

- Le fonti di Google Maps devono seguire immediatamente i contenuti generati che supportano. Questi contenuti generati sono anche chiamati Risultato fondato di Google Maps.
- Le fonti di Google Maps devono essere visualizzabili all'interno di un'interazione utente.

### Visualizzare le fonti di Google Maps con i link di Google Maps

Per ogni fonte in `groundingChunks` e in `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, è necessario generare un'anteprima del link in base ai seguenti requisiti:

- Attribuisci ogni fonte a Google Maps seguendo le linee guida per l'attribuzione del testo
  [di Google Maps](#maps-attribution-guidelines).
- Visualizza il titolo della fonte fornito nella risposta.
- Collega alla fonte utilizzando `uri` o `googleMapsUri` dalla risposta.

Queste immagini mostrano i requisiti minimi per la visualizzazione delle fonti e dei link di Google Maps.

![Prompt con risposta che mostra le fonti](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=it)

Puoi comprimere la visualizzazione delle fonti.

![Prompt con risposta e fonti compresse](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=it)

(Facoltativo) Migliora l'anteprima del link con contenuti aggiuntivi, ad esempio:

- Prima dell'attribuzione del testo di Google Maps viene inserita una [favicon di Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=it).
- Una foto dall'URL di origine (`og:image`).

Per ulteriori informazioni su alcuni dei nostri fornitori di dati di Google Maps e sui relativi
termini di licenza, consulta le [note legali di Google Maps e Google Earth](https://www.google.com/help/legalnotices_maps/?hl=it).

### Linee guida per l'attribuzione del testo di Google Maps

Quando attribuisci le fonti a Google Maps nel testo, segui queste linee guida:

- Non modificare in alcun modo il testo Google Maps:
  - Non modificare le maiuscole/minuscole di Google Maps.
  - Non mandare a capo Google Maps su più righe.
  - Non localizzare Google Maps in un'altra lingua.
  - Impedisci ai browser di tradurre Google Maps utilizzando l'attributo HTML translate="no".
- Applica lo stile al testo di Google Maps come descritto nella tabella seguente:

| Proprietà | Stile |
| --- | --- |
| `Font family` | Roboto. Il caricamento del carattere è facoltativo. |
| `Fallback font family` | Qualsiasi carattere del corpo sans-serif già utilizzato nel tuo prodotto o "Sans-Serif" per richiamare il carattere di sistema predefinito |
| `Font style` | Normale |
| `Font weight` | 400 |
| `Font color` | Bianco, nero (#1F1F1F) o grigio (#5E5E5E). Mantieni un contrasto accessibile (4,5:1) rispetto allo sfondo. |
| `Font size` | - Dimensioni minime del carattere: 12sp - Dimensioni massime del carattere: 16sp - Per scoprire di più su sp, consulta Unità di dimensioni dei caratteri sul sito web di [Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normale |

#### CSS di esempio

Il seguente CSS esegue il rendering di Google Maps con lo stile tipografico e il colore appropriati su uno sfondo bianco o chiaro.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### ID posizione e ID recensione

I dati di Google Maps includono l'ID posizione e l'ID recensione. Puoi memorizzare nella cache, archiviare ed esportare i seguenti dati di risposta:

- `placeId`
- `reviewId`

Le limitazioni alla memorizzazione nella cache nei Termini di Grounding con Google Maps non si applicano.

### Attività e territorio vietati

Grounding con Google Maps prevede ulteriori limitazioni per determinati contenuti e attività al fine di mantenere una piattaforma sicura e affidabile. Oltre alle limitazioni all'utilizzo
nei [Termini](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-maps):

- Non utilizzerai Grounding con Google Maps per attività ad alto rischio, inclusi i servizi di risposta alle emergenze.
- Non distribuirai né commercializzerai la tua applicazione che offre Grounding con Google Maps in un Territorio vietato. Per ulteriori informazioni, consulta la pagina
  [Territori vietati di Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=it).
  L'elenco dei Territori vietati potrebbe essere aggiornato di tanto in tanto.

## Best practice

- **Fornisci la località dell'utente:** per le risposte più pertinenti e personalizzate, includi sempre `user_location` (latitudine e longitudine) nella configurazione `googleMapsGrounding` quando la località dell'utente è nota.
- **Informa gli utenti finali:** informa chiaramente gli utenti finali che i dati di Google Maps vengono utilizzati per rispondere alle loro query, soprattutto quando lo strumento è attivato.
- **Monitora la latenza:** per le applicazioni conversazionali, assicurati che la latenza P95 per le risposte basate su dati di fatto rimanga entro le soglie accettabili per mantenere un'esperienza utente fluida.
- **Disattiva quando non è necessario:** Grounding con Google Maps è disattivato per impostazione predefinita. Attivalo solo (`"tools": [{"googleMaps": {}}]`) quando una query ha un
  contesto geografico chiaro, per ottimizzare il rendimento e i costi.

## Limitazioni

- **Ambito geografico:** Grounding con Google Maps è disponibile a livello globale
- **Supporto del modello:** consulta la sezione [Modelli supportati](#supported-models).
- **Input/output multimodali:** Grounding con Google Maps al momento non supporta input o output multimodali oltre al testo.
- **Stato predefinito:** lo strumento Grounding con Google Maps è disattivato per impostazione predefinita.
  Devi attivarlo esplicitamente nelle richieste API.

## Prezzi e limiti di frequenza

I prezzi di Grounding con Google Maps si basano sulle query. La tariffa attuale è di **25$per 1000 prompt basati su dati di fatto**. Il livello senza costi prevede anche fino a 500 richieste al giorno. Una richiesta viene conteggiata ai fini della quota solo quando un prompt restituisce correttamente almeno un risultato basato su dati di fatto di Google Maps (ovvero risultati contenenti almeno una fonte di Google Maps). Se vengono inviate più query a Google Maps da una singola richiesta, viene conteggiata come una richiesta ai fini del limite di frequenza.

Per informazioni dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

I seguenti modelli supportano Grounding con Google Maps:

| Modello | Grounding con Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Pro (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Combinazioni di strumenti supportate

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come Grounding con Google Maps) con strumenti personalizzati (chiamata di funzioni). Scopri di più nella pagina delle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Passaggi successivi

- Prova [Grounding con la Ricerca Google nell'API Gemini
  Ricettario](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=it).
- Scopri di più sugli altri [strumenti disponibili](https://ai.google.dev/gemini-api/docs/tools?hl=it).
- Per scoprire di più sulle best practice per l'AI responsabile e sui filtri di sicurezza dell'API Gemini, consulta [la guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
