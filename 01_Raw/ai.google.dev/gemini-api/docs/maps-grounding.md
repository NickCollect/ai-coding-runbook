---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it
fetched_at: 2026-05-25T05:27:12.149228+00:00
title: "Messa a terra con Google Maps \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Messa a terra con Google Maps

Grounding con Google Maps collega le funzionalità generative di Gemini ai dati ricchi, reali e aggiornati di Google Maps. Questa funzionalità consente
agli sviluppatori di incorporare facilmente funzionalità basate sulla posizione nelle loro
applicazioni. Quando una query utente ha un contesto correlato ai dati di Maps, il modello Gemini sfrutta Google Maps per fornire risposte oggettive e aggiornate pertinenti alla posizione o all'area generale specificata dall'utente.

- **Risposte accurate e basate sulla posizione**:sfrutta i dati estesi e
  aggiornati di Google Maps per le query geograficamente specifiche.
- **Personalizzazione avanzata:** personalizza consigli e informazioni in base alle località fornite dagli utenti.
- **Informazioni e widget contestuali**:token contestuali per visualizzare widget interattivi di Google Maps insieme ai contenuti generati.

## Inizia

Questo esempio mostra come integrare Grounding con Google Maps nella tua
applicazione per fornire risposte accurate e basate sulla posizione alle query degli utenti. Il
prompt chiede consigli locali con una posizione utente facoltativa, consentendo
al modello Gemini di utilizzare i dati di Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: "gemini-3.5-flash",
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

La grounding con Google Maps integra l'API Gemini con l'ecosistema Google Geo utilizzando l'API di Google Maps come fonte di grounding. Quando la query di un utente
contiene un contesto geografico, il modello Gemini può richiamare lo strumento Grounding con
Google Maps. Il modello può quindi generare risposte basate sui dati di Google Maps pertinenti alla posizione fornita.

La procedura in genere prevede:

1. **Query dell'utente**:un utente invia una query alla tua applicazione, potenzialmente
   incluso il contesto geografico (ad es. "bar nelle vicinanze", "musei a
   San Francisco").
2. **Richiamo dello strumento**:il modello Gemini, riconoscendo l'intento geografico,
   richiama lo strumento Grounding con Google Maps. Questo strumento può essere fornito facoltativamente con `latitude` e `longitude` dell'utente. Lo strumento è uno strumento di ricerca
   testuale e si comporta in modo simile alla ricerca su Maps, in quanto le query
   locali ("vicino a me") utilizzano le coordinate, mentre è improbabile che le query specifiche o non locali
   siano influenzate dalla posizione esplicita.
3. **Recupero dei dati**:il servizio Grounding con Google Maps esegue query su Google
   Maps per informazioni pertinenti (ad es. luoghi, recensioni, foto, indirizzi,
   orari di apertura).
4. **Generazione fondata**:i dati di Maps recuperati vengono utilizzati per informare la risposta del modello Gemini, garantendo accuratezza e pertinenza.
5. **Token di risposta e widget**:il modello restituisce una risposta di testo che include citazioni di fonti di Google Maps. Facoltativamente, la risposta dell'API può
   contenere anche un `google_maps_widget_context_token`, che consente agli sviluppatori di
   visualizzare un widget contestuale di Google Maps nella propria applicazione per l'interazione
   visiva.

## Perché e quando utilizzare Grounding con Google Maps

Grounding con Google Maps è ideale per le applicazioni che richiedono informazioni accurate,
aggiornate e specifiche per la posizione. Migliora l'esperienza utente
fornendo contenuti pertinenti e personalizzati supportati dall'ampio
database di Google Maps di oltre 250 milioni di luoghi in tutto il mondo.

Devi utilizzare Grounding con Google Maps quando la tua applicazione deve:

- Fornisci risposte complete e accurate alle domande specifiche per area geografica.
- Crea pianificatori di viaggi conversazionali e guide locali.
- Consiglia punti di interesse in base alla posizione e alle preferenze dell'utente, come ristoranti o negozi.
- Crea esperienze basate sulla posizione per servizi di social media, vendita al dettaglio o consegna di cibo.

Grounding con Google Maps eccelle nei casi d'uso in cui la vicinanza e i dati oggettivi attuali sono fondamentali, ad esempio per trovare il "miglior bar vicino a me" o ricevere indicazioni stradali.

## Metodi e parametri API

Il grounding con Google Maps viene esposto tramite l'API Gemini come strumento all'interno del metodo [`generateContent`](https://ai.google.dev/api/generate-content?hl=it). Puoi attivare e configurare
Grounding con Google Maps includendo un
oggetto [`googleMaps`](https://ai.google.dev/api/caching?hl=it#GoogleMaps) nel parametro `tools` della tua
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

Lo strumento [`googleMaps`](https://ai.google.dev/api/caching?hl=it#GoogleMaps) può accettare anche un parametro booleano `enableWidget`, che viene utilizzato per controllare se il campo [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=it#GroundingMetadata) viene restituito nella risposta. Può essere utilizzato per visualizzare un
[widget contestuale di Places](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=it).

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
}
```

Inoltre, lo strumento supporta il passaggio della posizione contestuale come `toolConfig`.

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

Quando una risposta viene generata correttamente con i dati di Google Maps, la risposta
include un campo [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=it#GroundingMetadata).
Questi dati strutturati sono essenziali per verificare le rivendicazioni e creare un'esperienza di citazione avanzata nella tua applicazione, nonché per soddisfare i requisiti di utilizzo del servizio.

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
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

L'API Gemini restituisce le seguenti informazioni con
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=it#GroundingMetadata):

- `groundingChunks`: array di oggetti contenenti le origini `maps` (`uri`,
  `placeId` e `title`).
- `groundingSupports`: Array di blocchi per collegare il testo della risposta del modello alle fonti in `groundingChunks`. Ogni blocco collega un intervallo di testo (definito da
  `startIndex` e `endIndex`) a uno o più `groundingChunkIndices`. Questa è
  la chiave per creare citazioni in linea.
- `googleMapsWidgetContextToken`: un token di testo che può essere utilizzato per eseguire il rendering di un
  [widget contestuale di Places](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=it).

Per uno snippet di codice che mostra come eseguire il rendering delle citazioni in linea nel testo, consulta [l'esempio](https://ai.google.dev/gemini-api/docs/google-search?hl=it#attributing_sources_with_inline_citations) nella documentazione di Grounding con la Ricerca Google.

### Visualizzare il widget contestuale di Google Maps

Per utilizzare `googleMapsWidgetContextToken` restituito, devi [caricare l'API Google Maps JavaScript](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=it).

## Casi d'uso

Grounding con Google Maps supporta una serie di casi d'uso basati sulla posizione. Gli esempi seguenti mostrano come diversi prompt e parametri possono sfruttare
Grounding con Google Maps. Le informazioni nei risultati basati su dati reali di Google Maps potrebbero
differire dalle condizioni effettive.

### Gestione delle domande specifiche per un luogo

Poni domande dettagliate su un luogo specifico per ricevere risposte basate sulle recensioni degli utenti di Google e su altri dati di Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

### Fornire personalizzazione basata sulla posizione

Ricevi consigli personalizzati in base alle preferenze di un utente e a una specifica area geografica.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

### Assistenza per la pianificazione dell'itinerario

Genera piani di più giorni con indicazioni stradali e informazioni su varie
località, perfetti per le applicazioni di viaggio.

In questo esempio, `googleMapsWidgetContextToken` è stato richiesto
attivando il widget nello strumento Google Maps. Se attivato, il token restituito
può essere utilizzato per eseguire il rendering di un widget contestuale Places utilizzando
`<gmp-places-contextual> component`
dall'API Maps JavaScript.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
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

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
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

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

Quando viene eseguito il rendering del widget, avrà un aspetto simile al seguente:

![Esempio di widget di Maps dopo il rendering](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=it)

## Requisiti per l'utilizzo del servizio

Questa sezione descrive i requisiti di utilizzo del servizio per Grounding con Google Maps.

### Informare l'utente sull'utilizzo delle fonti di Google Maps

Per ogni risultato di Google Maps Grounded, riceverai fonti in
`groundingChunks` che supportano ogni risposta. Vengono restituiti anche i seguenti metadati:

- source uri
- titolo
- ID

Quando presenti i risultati di Grounding con Google Maps, devi specificare le fonti di Google Maps associate e informare gli utenti di quanto segue:

- Le fonti di Google Maps devono seguire immediatamente i contenuti generati che
  supportano le fonti. Questi contenuti generati sono anche chiamati risultato basato su Google Maps.
- Le fonti di Google Maps devono essere visualizzabili con una sola interazione dell'utente.

### Visualizzare le fonti di Google Maps con i link di Google Maps

Per ogni origine in `groundingChunks` e in
`grounding_chunks.maps.placeAnswerSources.reviewSnippets`, deve essere generata
un'anteprima del link in base ai seguenti requisiti:

- Attribuisci ogni fonte a Google Maps seguendo le [linee guida per l'attribuzione](#maps-attribution-guidelines) del testo di Google Maps.
- Mostra il titolo della fonte fornito nella risposta.
- Link alla fonte utilizzando `uri` o `googleMapsUri` dalla risposta.

Queste immagini mostrano i requisiti minimi per la visualizzazione delle fonti e dei link di Google Maps.

![Prompt con risposta che mostra le fonti](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=it)

Puoi comprimere la visualizzazione delle fonti.

![Prompt con risposta e fonti compresse](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=it)

(Facoltativo) Migliora l'anteprima del link con contenuti aggiuntivi, ad esempio:

- Un [favicon di Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=it)
  viene inserito prima del testo di attribuzione di Google Maps.
- Una foto dall'URL di origine (`og:image`).

Per ulteriori informazioni su alcuni dei nostri fornitori di dati di Google Maps e sui relativi termini di licenza, consulta le [note legali di Google Maps e Google Earth](https://www.google.com/help/legalnotices_maps/?hl=it).

### Linee guida per l'attribuzione di testo di Google Maps

Quando attribuisci le fonti a Google Maps nel testo, segui queste linee guida:

- Non modificare in alcun modo il testo Google Maps:
  - Non modificare le maiuscole di Google Maps.
  - Non mandare a capo Google Maps.
  - Non localizzare Google Maps in un'altra lingua.
  - Impedisci ai browser di tradurre Google Maps utilizzando l'attributo HTML
    translate="no".
- Formatta il testo di Google Maps come descritto nella tabella seguente:

| Proprietà | Stile |
| --- | --- |
| `Font family` | Roboto. Il caricamento del carattere è facoltativo. |
| `Fallback font family` | Qualsiasi carattere del corpo sans-serif già utilizzato nel tuo prodotto o "Sans-Serif" per richiamare il carattere di sistema predefinito |
| `Font style` | Normale |
| `Font weight` | 400 |
| `Font color` | Bianco, nero (#1F1F1F) o grigio (#5E5E5E). Mantenere un contrasto accessibile (4,5:1) rispetto allo sfondo. |
| `Font size` | - Dimensione minima del carattere: 12 sp - Dimensioni carattere massime: 16 sp - Per scoprire di più su sp, consulta Unità di misura delle dimensioni del carattere sul [sito web di Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
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

### Token di contesto, ID luogo e ID recensione

I dati di Google Maps includono token di contesto, ID luogo e ID recensione. Potresti
memorizzare nella cache, archiviare ed esportare i seguenti dati delle risposte:

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Le limitazioni alla memorizzazione nella cache previste dai Termini del grounding con Google Maps non
si applicano.

### Attività e territorio vietati

La funzionalità di grounding con Google Maps prevede ulteriori limitazioni per determinati contenuti e
attività per mantenere una piattaforma sicura e affidabile. Oltre alle limitazioni
all'utilizzo riportate nei [Termini](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-maps):

- Non utilizzerai Grounding con Google Maps per attività ad alto rischio, inclusi i servizi di risposta alle emergenze.
- Non distribuirai né commercializzerai la tua applicazione che offre Grounding con
  Google Maps in un Territorio vietato. Per ulteriori informazioni, consulta la pagina
  [Territori vietati di Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=it).
  L'elenco dei Territori non ammessi potrebbe essere aggiornato di tanto in tanto.

## Best practice

- **Fornisci la posizione dell'utente**:per ottenere risposte più pertinenti e personalizzate,
  includi sempre `user_location` (latitudine e longitudine) nella configurazione
  `googleMapsGrounding` quando la posizione dell'utente è nota.
- **Esegui il rendering del widget contestuale di Google Maps:** il widget contestuale viene
  eseguito il rendering utilizzando il token di contesto, `googleMapsWidgetContextToken`, che viene
  restituito nella risposta dell'API Gemini e può essere utilizzato per eseguire il rendering di contenuti visivi
  da Google Maps. Per saperne di più sul widget contestuale, consulta la sezione
  [Widget di grounding con Google Maps](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=it)
  nella Guida per gli sviluppatori Google.
- **Informa gli utenti finali:** informa chiaramente gli utenti finali che i dati di Google Maps vengono utilizzati per rispondere alle loro query, soprattutto quando lo strumento è abilitato.
- **Monitora la latenza**:per le applicazioni conversazionali, assicurati che la latenza P95
  per le risposte basate su dati reali rimanga entro le soglie accettabili per
  mantenere un'esperienza utente fluida.
- **Disattiva quando non è necessario:** il grounding con Google Maps è disattivato per impostazione predefinita. Attivala (`"tools": [{"googleMaps": {}}]`) solo quando una query ha un contesto geografico chiaro, per ottimizzare prestazioni e costi.

## Limitazioni

- **Ambito geografico:** il grounding con Google Maps è disponibile a livello globale
- **Supporto del modello**:consulta la sezione [Modelli supportati](#supported-models).
- **Input/output multimodali**:il grounding con Google Maps non supporta attualmente
  input o output multimodali oltre a testo e widget di mappe contestuali.
- **Stato predefinito**:lo strumento Grounding con Google Maps è disattivato per impostazione predefinita.
  Devi abilitarla esplicitamente nelle richieste API.

## Prezzi e limiti di frequenza

Il prezzo di Grounding con Google Maps si basa sulle query. La tariffa attuale è
**25$per 1000 prompt con grounding**. Il Livello senza costi offre anche fino a 500 richieste al giorno. Una richiesta viene conteggiata ai fini della quota solo quando
un prompt restituisce correttamente almeno un risultato con grounding di Google Maps (ovvero
risultati contenenti almeno una fonte di Google Maps). Se vengono inviate più query a Google Maps da una singola richiesta, viene conteggiata come una richiesta ai fini del limite di frequenza.

Per informazioni più dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

I seguenti modelli supportano Grounding con Google Maps:

| Modello | Grounding con Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Pro (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=it) | ✔️ |

## Combinazioni di strumenti supportate

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come Grounding con Google Maps) con strumenti personalizzati (chiamata di funzioni). Scopri di più nella pagina
[Combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Passaggi successivi

- Prova la funzionalità [Grounding con la Ricerca Google nel cookbook dell'API Gemini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=it).
- Scopri di più sugli altri [strumenti disponibili](https://ai.google.dev/gemini-api/docs/tools?hl=it).
- Per saperne di più sulle best practice per l'AI responsabile e sui filtri di sicurezza dell'API Gemini, consulta la [guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
