---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=it
fetched_at: 2026-07-06T05:14:44.205200+00:00
title: "Impostazioni di sicurezza \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Impostazioni di sicurezza

L'API Gemini fornisce impostazioni di sicurezza che puoi regolare durante la fase di prototipazione per determinare se la tua applicazione richiede una configurazione di sicurezza più o meno restrittiva. Puoi regolare queste impostazioni in quattro categorie di filtri per limitare o consentire determinati tipi di contenuti.

Questa guida spiega come l'API Gemini gestisce le impostazioni di sicurezza e il filtraggio e come puoi modificare le impostazioni di sicurezza per la tua applicazione.

## Filtri di sicurezza

I filtri di sicurezza regolabili dell'API Gemini coprono le seguenti categorie:

| Categoria | Descrizione |
| --- | --- |
| Molestie | Commenti negativi o dannosi che prendono di mira l'identità e/o gli attributi protetti |
| Incitamento all'odio | Contenuti scortesi, irrispettosi o blasfemi. |
| Contenuti sessualmente espliciti | Contiene riferimenti ad atti sessuali o altri contenuti osceni. |
| Contenuti pericolosi | Promuove, facilita o incoraggia atti dannosi. |

Queste categorie sono definite in [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=it). Puoi utilizzare questi filtri per regolare ciò che è appropriato per il tuo caso d'uso. Ad esempio, se stai creando dialoghi di videogiochi, potresti ritenere accettabile consentire più contenuti classificati come *Contenuti pericolosi* per via della natura del gioco.

Oltre ai filtri di sicurezza regolabili, l'API Gemini dispone di protezioni integrate contro i danni principali, come i contenuti che mettono a repentaglio la sicurezza dei bambini.
Questi tipi di danni vengono sempre bloccati e non possono essere regolati.

### Livello di filtraggio della sicurezza dei contenuti

L'API Gemini classifica il livello di probabilità che i contenuti non siano sicuri come `HIGH`, `MEDIUM`, `LOW` o `NEGLIGIBLE`.

L'API Gemini blocca i contenuti in base alla probabilità che non siano sicuri e non alla gravità. È importante tenerlo presente perché alcuni contenuti possono avere una bassa probabilità di non essere sicuri, anche se la gravità del danno potrebbe essere elevata. Ad esempio, confronta le seguenti frasi:

1. Il robot mi ha dato un pugno.
2. Il robot mi ha tagliato.

La prima frase potrebbe avere una probabilità maggiore di non essere sicura, ma potresti considerare la seconda frase più grave in termini di violenza.
Per questo motivo, è importante testare attentamente e valutare il livello di blocco appropriato necessario per supportare i casi d'uso principali, riducendo al minimo i danni agli utenti finali.

### Filtraggio di sicurezza per richiesta

Puoi regolare le impostazioni di sicurezza per ogni richiesta che invii all'API. Quando invii una richiesta, i contenuti vengono analizzati e viene assegnata una valutazione di sicurezza. La valutazione di sicurezza include la categoria e la probabilità della classificazione del danno. Ad esempio, se i contenuti sono stati bloccati perché la categoria delle molestie ha una probabilità elevata, la valutazione di sicurezza restituita avrà la categoria uguale a `HARASSMENT` e la probabilità di danno impostata su `HIGH`.

A causa della sicurezza intrinseca del modello, i filtri aggiuntivi sono **disattivati** per impostazione predefinita.
Se scegli di attivarli, puoi configurare il sistema in modo che blocchi i contenuti in base alla probabilità che non siano sicuri. Il comportamento predefinito del modello copre la maggior parte dei casi d'uso, quindi dovresti regolare queste impostazioni solo se è un requisito costante per la tua applicazione.

La tabella seguente descrive le impostazioni di blocco che puoi regolare per ogni categoria. Ad esempio, se imposti l'impostazione di blocco su **Blocco ridotto** per la categoria **Incitamento all'odio**, tutto ciò che ha un'alta probabilità di essere un contenuto di incitamento all'odio viene bloccato. Tuttavia, tutto ciò che ha una probabilità inferiore è consentito.

| Soglia (Google AI Studio) | Soglia (API) | Descrizione |
| --- | --- | --- |
| Off | `OFF` | Disattiva il filtro di sicurezza |
| Nessun blocco | `BLOCK_NONE` | Mostra sempre, indipendentemente dalla probabilità che i contenuti non siano sicuri |
| Blocco ridotto | `BLOCK_ONLY_HIGH` | Blocca quando c'è un'alta probabilità che i contenuti non siano sicuri |
| Blocco limitato | `BLOCK_MEDIUM_AND_ABOVE` | Blocca quando c'è una probabilità media o alta che i contenuti non siano sicuri |
| Blocco esteso | `BLOCK_LOW_AND_ABOVE` | Blocca quando c'è una probabilità bassa, media o alta che i contenuti non siano sicuri |
| N/D | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | La soglia non è specificata, blocca utilizzando la soglia predefinita |

Se la soglia non è impostata, la soglia di blocco predefinita è **Off** per i modelli Gemini 2.5 e 3.

Puoi impostare queste impostazioni per ogni richiesta che invii al servizio generativo.
Per maggiori dettagli, consulta il riferimento API [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=it#harmblockthreshold).

### Feedback sulla sicurezza

[`generateContent`](https://ai.google.dev/api/generate-content?hl=it#method:-models.generatecontent)
restituisce un
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=it#generatecontentresponse) che
include il feedback sulla sicurezza.

Il feedback sui prompt è incluso in
[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=it#promptfeedback). Se `promptFeedback.blockReason` è impostato, i contenuti del prompt sono stati bloccati.

Il feedback sui candidati di risposta è incluso in
[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=it#candidate) e
[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=it#candidate). Se i contenuti della risposta sono stati bloccati e `finishReason` era `SAFETY`, puoi esaminare `safetyRatings` per maggiori dettagli. I contenuti bloccati non vengono restituiti.

## Regolare le impostazioni di sicurezza

Questa sezione spiega come regolare le impostazioni di sicurezza in Google AI Studio e nel codice.

### Google AI Studio

Puoi regolare le impostazioni di sicurezza in Google AI Studio.

Fai clic su **Impostazioni di sicurezza** in **Impostazioni avanzate** nel riquadro **Impostazioni di esecuzione** per aprire la finestra modale **Esegui impostazioni di sicurezza**. Nella finestra modale, puoi utilizzare i cursori per regolare il livello di filtraggio dei contenuti per categoria di sicurezza:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=it)

Quando invii una richiesta (ad esempio, ponendo una domanda al modello), viene visualizzato un messaggio warning
**Contenuti bloccati** se i contenuti della richiesta vengono bloccati. Per visualizzare maggiori dettagli, tieni il puntatore sopra il testo **Contenuti bloccati** per visualizzare la categoria e la probabilità della classificazione del danno.

### Esempi di codice

Il seguente snippet di codice mostra come impostare le impostazioni di sicurezza nella chiamata `GenerateContent`. Imposta la soglia per la categoria di incitamento all'odio (`HARM_CATEGORY_HATE_SPEECH`). Se imposti questa categoria su `BLOCK_LOW_AND_ABOVE`, vengono bloccati tutti i contenuti che hanno una probabilità bassa o superiore di essere di incitamento all'odio. Per comprendere le impostazioni della soglia, consulta [Filtraggio di sicurezza
per richiesta](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
```

### Vai

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,
    BlockThreshold.LOW_AND_ABOVE);

GenerativeModel gm = new GenerativeModel(
    "gemini-3.5-flash",
    BuildConfig.apiKey,
    null, // generation config is optional
    Arrays.asList(hateSpeechSafety)
);

GenerativeModelFutures model = GenerativeModelFutures.from(gm);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## Passaggi successivi

- Consulta il [riferimento API](https://ai.google.dev/api?hl=it) per scoprire di più sull'API completa.
- Consulta le [linee guida sulla sicurezza](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it) per una panoramica generale delle considerazioni sulla sicurezza
  durante lo sviluppo con i LLM.
- Scopri di più sulla valutazione della probabilità rispetto alla gravità dal team [Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score)
- Scopri di più sui prodotti che contribuiscono alle soluzioni di sicurezza, come l'
  [API
  Perspective](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).
  \* Puoi utilizzare queste impostazioni di sicurezza per creare un classificatore di tossicità
  Per iniziare, consulta l'esempio di [classificazione
  esempio](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=it) per
  iniziare.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-01 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-01 UTC."],[],[]]
