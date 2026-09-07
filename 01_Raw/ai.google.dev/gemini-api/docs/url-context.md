---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=it
fetched_at: 2026-09-07T05:35:00.427594+00:00
title: "Contesto URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Contesto URL

[Lo strumento Contesto URL ti consente di fornire un contesto aggiuntivo ai modelli sotto forma di URL. Se includi gli URL nella richiesta, il modello accederà ai contenuti di queste pagine (purché non si tratti di un tipo di URL elencato nella sezione Limitazioni) per informare e migliorare la sua risposta.](#limitations)

Lo strumento Contesto URL è utile per attività come le seguenti:

- **Estrarre dati**: estrai informazioni specifiche come prezzi, nomi o risultati
  chiave da più URL.
- **Confrontare documenti**: analizza più report, articoli o PDF per
  identificare le differenze e monitorare le tendenze.
- **Sintetizzare e creare contenuti**: combina le informazioni di più URL di origine per generare riepiloghi, post di blog o report accurati.
- **Analizzare codice e documenti**: indica un repository GitHub o una documentazione tecnica per spiegare il codice, generare istruzioni di configurazione o rispondere a domande.

L'esempio seguente mostra come confrontare due ricette di siti web diversi.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Come funziona

Lo strumento Contesto URL utilizza una procedura di recupero in due passaggi per bilanciare velocità, costi e accesso ai dati aggiornati. Quando fornisci un URL, lo strumento tenta innanzitutto di recuperare i contenuti da una cache di indici interni. Questa funge da cache altamente ottimizzata. Se un URL non è disponibile nell'indice (ad esempio, se si tratta di una pagina molto recente), lo strumento esegue automaticamente il fallback a un recupero live.
In questo modo, l'URL viene acceduto direttamente per recuperare i relativi contenuti in tempo reale.

## Combinazione con altri strumenti

Puoi combinare lo strumento Contesto URL con altri strumenti per creare workflow più potenti.

[I modelli Gemini 3](#supported-models) supportano la combinazione di strumenti integrati
(come Contesto URL) con strumenti personalizzati (chiamata di funzioni). Scopri di più nella pagina delle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

### Grounding con la Ricerca

Se sono attivi sia Contesto URL sia
[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it),
il modello può utilizzare le sue funzionalità di ricerca per trovare
informazioni pertinenti online e poi utilizzare lo strumento Contesto URL per comprendere meglio le pagine che trova. Questo approccio è efficace per i prompt che richiedono sia una ricerca ampia sia un'analisi approfondita di pagine specifiche.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Comprendere la risposta

Quando il modello utilizza lo strumento Contesto URL, la risposta di testo include annotazioni `url_citation` in linea nel blocco di contenuti di testo. Ogni annotazione collega un segmento del testo di risposta (tramite `start_index` e `end_index`) all'URL di origine da cui è stato derivato. Questo è il modo principale per visualizzare le citazioni nella tua
applicazione. Per scoprire come estrarle, consulta l'[esempio principale riportato sopra](#get-started).

La risposta include anche un passaggio `url_context_result` con i metadati relativi a ogni tentativo di recupero dell'URL (stato, URL recuperato). Questo è utile soprattutto per il debug.

### Assegni assicurati

Il sistema esegue un controllo di moderazione dei contenuti sugli URL per verificare che soddisfino gli standard di sicurezza. Se un URL non supera questo controllo, il passaggio corrispondente
`url_context_result` mostrerà uno `status` di `"unsafe"`.

### Conteggio dei token

I contenuti recuperati dagli URL specificati nel prompt vengono conteggiati come parte dei token di input. Puoi visualizzare il conteggio dei token nell'oggetto `usage` dell'interazione. Di seguito è riportato un esempio:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Il prezzo per token dipende dal modello utilizzato. Per i dettagli, consulta la
[pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

| Modello | Contesto URL |
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

## Best practice

- **Fornisci URL specifici**: per ottenere risultati ottimali, fornisci URL diretti ai
  contenuti che vuoi che il modello analizzi. Il modello recupererà solo i contenuti degli URL che fornisci, non i contenuti dei link nidificati.
- **Verifica l'accessibilità**: verifica che gli URL che fornisci non rimandino a
  pagine che richiedono l'accesso o che siano protette da paywall.
- **Utilizza l'URL completo**: fornisci l'URL completo, incluso il protocollo
  (ad es. https://www.google.com anziché solo google.com).

## Limitazioni

- Limite delle richieste: lo strumento può elaborare fino a 20 URL per richiesta.
- Dimensioni dei contenuti dell'URL: la dimensione massima dei contenuti recuperati da un singolo URL è di 34 MB.
- Accessibilità pubblica: gli URL devono essere accessibili pubblicamente sul web.
  Gli indirizzi localhost (ad es. localhost, 127.0.0.1), le reti private e i servizi di tunneling (ad es. ngrok, pinggy) non sono supportati.

### Tipi di contenuti supportati e non supportati

Lo strumento può estrarre contenuti dagli URL con i seguenti tipi di contenuti:

- Testo (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Immagine (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

I seguenti tipi di contenuti **non** sono supportati:

- Contenuti protetti da paywall
- Video di YouTube (per scoprire
  [come elaborare gli URL di YouTube](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it#youtube), consulta la sezione
  Comprensione dei video)
- File di Google Workspace come Documenti o Fogli Google
- File video e audio

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-31 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-31 UTC."],[],[]]
