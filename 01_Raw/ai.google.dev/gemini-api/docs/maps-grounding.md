---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it
fetched_at: 2026-09-07T05:43:46.469826+00:00
title: "Grounding con Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Grounding con Google Maps

Grounding con Google Maps collega le funzionalità generative di Gemini ai dati ricchi, fattuali e aggiornati di Google Maps. Questa funzionalità consente agli sviluppatori di incorporare facilmente funzionalità basate sulla località nelle loro applicazioni. Quando una query utente ha un contesto correlato ai dati di Maps, il modello Gemini utilizza Google Maps per fornire risposte fattualmente accurate e aggiornate pertinenti alla località o all'area generale specificata dall'utente.

- **Risposte accurate e basate sulla località:** sfrutta i dati estesi e attuali di Google Maps per le query geograficamente specifiche.
- **Personalizzazione avanzata:** personalizza consigli e informazioni in base alle località fornite dall'utente.

## Inizia

Questo esempio mostra come integrare Grounding con Google Maps nella tua applicazione per fornire risposte accurate e basate sulla località alle query degli utenti. Il prompt richiede consigli locali con una località utente facoltativa, consentendo al modello Gemini di utilizzare i dati di Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Come funziona Grounding con Google Maps

Grounding con Google Maps integra l'API Gemini con l'ecosistema Google Geo utilizzando l'API di Google Maps come origine di grounding. Quando la query di un utente contiene un contesto geografico, il modello Gemini può richiamare lo strumento Grounding con Google Maps. Il modello può quindi generare risposte basate sui dati di Google Maps pertinenti alla località fornita.

In genere, la procedura prevede i seguenti passaggi:

1. **Query utente:** un utente invia una query alla tua applicazione, che potrebbe includere un contesto geografico (ad es. "bar nelle vicinanze", "musei a San Francisco").
2. **Richiamo dello strumento:** il modello Gemini, riconoscendo l'intento geografico, richiama lo strumento Grounding con Google Maps. Questo strumento può essere fornito facoltativamente con la `latitude` e la `longitude` dell'utente. Lo strumento è uno strumento di ricerca testuale e si comporta in modo simile alla ricerca su Maps, in quanto le query locali ("nelle vicinanze") utilizzeranno le coordinate, mentre è improbabile che le query specifiche o non locali siano influenzate dalla località esplicita.
3. **Recupero dei dati:** il servizio Grounding con Google Maps esegue una query su Google Maps per informazioni pertinenti (ad es. luoghi, recensioni, foto, indirizzi, orari di apertura).
4. **Generazione basata su dati di fatto:** i dati di Maps recuperati vengono utilizzati per informare la risposta del modello Gemini, garantendo accuratezza e pertinenza fattuali.
5. **Risposta e annotazioni:** il modello restituisce una risposta di testo con annotazioni in linea che rimandano alle fonti di Google Maps, consentendo agli sviluppatori di visualizzare le citazioni.

## Perché e quando utilizzare Grounding con Google Maps

Grounding con Google Maps è ideale per le applicazioni che richiedono informazioni accurate, aggiornate e specifiche per la località. Migliora l'esperienza utente fornendo contenuti pertinenti e personalizzati supportati dall'ampio database di Google Maps di oltre 250 milioni di luoghi in tutto il mondo.

Devi utilizzare Grounding con Google Maps quando la tua applicazione deve:

- Fornire risposte complete e accurate a domande specifiche per la località.
- Creare pianificatori di viaggi conversazionali e guide locali.
- Consigliare punti di interesse in base alla località e alle preferenze dell'utente, come ristoranti o negozi.
- Creare esperienze basate sulla località per servizi social, di vendita al dettaglio o di consegna di cibo.

Grounding con Google Maps eccelle nei casi d'uso in cui la prossimità e i dati fattuali attuali sono fondamentali, ad esempio per trovare il "miglior bar nelle vicinanze" o ottenere indicazioni stradali.

## Casi d'uso

Grounding con Google Maps supporta una serie di casi d'uso basati sulla località.

### Gestire le domande specifiche per il luogo

Poni domande dettagliate su un luogo specifico per ottenere risposte basate sulle recensioni degli utenti di Google e su altri dati di Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Fornire personalizzazione basata sulla località

Ricevi consigli personalizzati in base alle preferenze di un utente e a un'area geografica specifica.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Aiutare con la pianificazione dell'itinerario

Genera piani di più giorni con indicazioni stradali e informazioni su varie località, perfetti per le applicazioni di viaggio.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Requisiti per l'utilizzo del servizio

Questa sezione descrive i requisiti per l'utilizzo del servizio Grounding con Google Maps.

### Informa l'utente dell'utilizzo delle fonti di Google Maps

Con ogni risultato basato su Google Maps, riceverai annotazioni delle fonti nei blocchi di contenuti del passaggio `model_output` che supportano ogni risposta. Vengono restituiti i seguenti metadati:

- URL di origine
- nome

Quando presenti i risultati di Grounding con Google Maps, devi specificare le fonti di Google Maps associate e informare gli utenti di quanto segue:

- Le fonti di Google Maps devono seguire immediatamente i contenuti generati che supportano. Questi contenuti generati sono anche chiamati risultati basati su Google Maps.
- Le fonti di Google Maps devono essere visualizzabili all'interno di un'interazione utente.

### Visualizzare le fonti di Google Maps con i link di Google Maps

Per ogni annotazione della fonte, è necessario generare un'anteprima del link che soddisfi i seguenti requisiti:

- Attribuisci ogni fonte a Google Maps seguendo le linee guida per l'attribuzione del testo
  [di Google Maps](#maps-attribution-guidelines).
- Visualizza il nome della fonte fornito nella risposta.
- Collega alla fonte utilizzando l'`url` dell'annotazione.

### Linee guida per l'attribuzione del testo di Google Maps

Quando attribuisci le fonti a Google Maps nel testo, segui queste linee guida:

- Non modificare in alcun modo il testo Google Maps:
  - Non modificare le maiuscole/minuscole di Google Maps.
  - Non mandare a capo Google Maps su più righe.
  - Non localizzare Google Maps in un'altra lingua.
  - Impedisci ai browser di tradurre Google Maps utilizzando l'attributo HTML translate="no".

Per ulteriori informazioni su alcuni dei nostri fornitori di dati di Google Maps e sui relativi
termini di licenza, consulta le [note legali di Google Maps e Google Earth](https://www.google.com/help/legalnotices_maps/?hl=it).

## Best practice

- **Fornisci la località dell'utente:** per le risposte più pertinenti e personalizzate, includi sempre la `latitude` e la `longitude` nella configurazione dello strumento `google_maps` quando la località dell'utente è nota.
- **Informa gli utenti finali:** informa chiaramente gli utenti finali che i dati di Google Maps vengono utilizzati per rispondere alle loro query, soprattutto quando lo strumento è abilitato.
- **Disattiva quando non è necessario:** Grounding con Google Maps è disattivato per impostazione predefinita. Abilitalo (`"tools": [{"type": "google_maps"}]`) solo quando una query ha un
  contesto geografico chiaro, per ottimizzare il rendimento e i costi.

## Limitazioni

- Al momento, Grounding con Google Maps supporta solo prompt e risposte in lingua inglese.
- Lo strumento potrebbe non essere disponibile in tutte le regioni.
- I risultati possono variare in base all'accuratezza della località e ai dati di Maps disponibili.
- **Ambito geografico:** Grounding con Google Maps è disponibile a livello globale.
- **Stato predefinito:** lo strumento Grounding con Google Maps è disattivato per impostazione predefinita.
  Devi abilitarlo esplicitamente nelle richieste API.

## Prezzi e limiti di frequenza

I prezzi di Grounding con Google Maps variano in base alla generazione del modello:

- **Modelli Gemini 3:** il tuo progetto viene addebitato per ogni **query di ricerca** che il modello decide di eseguire. Un singolo **prompt di ricerca** (la tua richiesta API al modello) potrebbe comportare l'esecuzione di più query di ricerca da parte del modello per trovare le informazioni necessarie. Ognuna di queste query viene conteggiata come utilizzo fatturabile dello strumento.
- **Modelli Gemini 2.5 e precedenti:** il tuo progetto viene addebitato per **prompt di ricerca**.
  Una richiesta viene addebitata solo se il prompt restituisce correttamente almeno un risultato basato su Google Maps, indipendentemente dal numero di singole query di ricerca eseguite internamente dal modello per ottenere il risultato.

Per informazioni dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

I seguenti modelli supportano Grounding con Google Maps:

| Modello | Grounding con Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Combinazioni di strumenti supportate

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come Grounding con Google Maps) con strumenti personalizzati (chiamata di funzioni). Scopri di più nella pagina delle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Passaggi successivi

- Scopri di più sugli altri [strumenti disponibili](https://ai.google.dev/gemini-api/docs/tools?hl=it).
- Per scoprire di più sulle best practice per l'AI responsabile e sui filtri di sicurezza dell'API Gemini, consulta [la guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
