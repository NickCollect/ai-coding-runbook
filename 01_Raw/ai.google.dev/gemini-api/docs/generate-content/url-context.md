---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=it
fetched_at: 2026-10-05T06:51:05.908560+00:00
title: "Contesto URL \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Contesto URL

Lo strumento Contesto URL ti consente di fornire un contesto aggiuntivo ai modelli sotto forma di URL. Se includi gli URL nella richiesta, il modello accederà ai contenuti di queste pagine (purché non si tratti di un tipo di URL elencato nella sezione delle [limitazioni](#limitations)) per informare e migliorare la sua risposta.

Lo strumento Contesto URL è utile per attività come le seguenti:

- **Estrarre dati**: estrai informazioni specifiche come prezzi, nomi o risultati
  chiave da più URL.
- **Confrontare documenti**: analizza più report, articoli o PDF per
  identificare le differenze e monitorare le tendenze.
- **Sintetizzare e creare contenuti**: combina le informazioni di più URL di origine per generare riepiloghi, post di blog o report accurati.
- **Analizzare codice e documenti**: indica un repository GitHub o una documentazione tecnica per spiegare il codice, generare istruzioni di configurazione o rispondere alle domande.

L'esempio seguente mostra come confrontare due ricette di siti web diversi.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### Javascript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Come funziona

Lo strumento Contesto URL utilizza una procedura di recupero in due passaggi per bilanciare velocità, costi e accesso ai dati aggiornati. Quando fornisci un URL, lo strumento tenta innanzitutto di recuperare i contenuti da una cache di indici interni. Questa funge da cache altamente ottimizzata. Se un URL non è disponibile nell'indice (ad esempio, se si tratta di una pagina molto recente), lo strumento esegue automaticamente il fallback per eseguire un recupero in tempo reale.
In questo modo, l'URL viene acceduto direttamente per recuperare i relativi contenuti in tempo reale.

## Combinazione con altri strumenti

Puoi combinare lo strumento Contesto URL con altri strumenti per creare workflow più potenti.

[I modelli Gemini 3](#supported-models) supportano la combinazione di strumenti integrati
(come Contesto URL) con strumenti personalizzati (chiamata di funzione). Scopri di più nella pagina delle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

### Grounding con la ricerca

Se sono attivi sia Contesto URL sia
[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it),
il modello può utilizzare le sue funzionalità di ricerca per trovare
informazioni pertinenti online e poi utilizzare lo strumento Contesto URL per comprendere meglio le pagine che trova. Questo approccio è efficace per i prompt che richiedono sia una ricerca ampia sia un'analisi approfondita di pagine specifiche.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### Javascript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Comprendere la risposta

Quando il modello utilizza lo strumento Contesto URL, la risposta include un oggetto `url_context_metadata`. Questo oggetto elenca gli URL da cui il modello ha recuperato i contenuti e lo stato di ogni tentativo di recupero, il che è utile per la verifica e il debug.

Di seguito è riportato un esempio di questa parte della risposta (alcune parti della risposta sono state omesse per brevità):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Per informazioni dettagliate su questo oggetto , consulta il
[`UrlContextMetadata` riferimento API](https://ai.google.dev/api/generate-content?hl=it#UrlContextMetadata).

### Assegni assicurati

Il sistema esegue un controllo di moderazione dei contenuti sull'URL per verificare che soddisfi gli standard di sicurezza. Se l'URL fornito non supera questo controllo, riceverai un `url_retrieval_status` di `URL_RETRIEVAL_STATUS_UNSAFE`.

### Conteggio dei token

I contenuti recuperati dagli URL specificati nel prompt vengono conteggiati come parte dei token di input. Puoi visualizzare il conteggio dei token per l'utilizzo di prompt e
strumenti nell'oggetto [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=it#UsageMetadata)
dell'output del modello. Di seguito è riportato un esempio di output:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Il prezzo per token dipende dal modello utilizzato. Per maggiori dettagli, consulta la pagina dei
[prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

| Modello | Contesto URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Best practice

- **Fornisci URL specifici**: per ottenere risultati ottimali, fornisci URL diretti ai
  contenuti che vuoi che il modello analizzi. Il modello recupererà solo i contenuti degli URL forniti, non i contenuti dei link nidificati.
- **Verifica l'accessibilità**: verifica che gli URL forniti non rimandino a
  pagine che richiedono l'accesso o che siano protette da paywall.
- **Utilizza l'URL completo**: fornisci l'URL completo, incluso il protocollo
  (ad es. https://www.google.com anziché solo google.com).

## Limitazioni

- Chiamata di funzione: l'utilizzo di strumenti (Contesto URL, Grounding con la Ricerca Google e così via) con la chiamata di funzione non è attualmente supportato.
- Limite delle richieste: lo strumento può elaborare fino a 20 URL per richiesta.
- Dimensioni dei contenuti dell'URL: la dimensione massima dei contenuti recuperati da un singolo URL è di 34 MB.
- Accessibilità pubblica: gli URL devono essere accessibili pubblicamente sul web.
  Gli indirizzi localhost (ad es. localhost, 127.0.0.1), le reti private e i servizi di tunneling (ad es. ngrok, pinggy) non sono supportati.
- Solo API Gemini: Contesto URL è disponibile solo nell'API Gemini, non tramite Gemini Enterprise Agent Platform.

### Tipi di contenuti supportati e non supportati

Lo strumento può estrarre contenuti da URL con i seguenti tipi di contenuti:

- Testo (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Immagine (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

I seguenti tipi di contenuti **non** sono supportati:

- Contenuti protetti da paywall
- Video di YouTube (consulta la sezione
  [Comprensione dei video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it#youtube) per scoprire
  come elaborare gli URL di YouTube)
- File di Google Workspace come Documenti o Fogli Google
- File audio e video

## Passaggi successivi

- Esplora il [ricettario Contesto URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=it#url-context)
  per altri esempi.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
