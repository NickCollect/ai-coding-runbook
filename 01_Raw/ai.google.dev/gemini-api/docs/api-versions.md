---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=it
fetched_at: 2026-07-20T04:44:58.995793+00:00
title: "Spiegazione delle versioni API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Riferimento API](https://ai.google.dev/api?hl=it)

Invia feedback

# Spiegazione delle versioni API

Questo documento fornisce una panoramica generale delle differenze tra le versioni `v1`
e `v1beta` dell'API Gemini.

- **v1**: versione stabile dell'API. Le funzionalità nella versione stabile sono
  completamente supportate per tutta la durata della versione principale. Se vengono apportate
  modifiche che causano interruzioni, verrà creata la successiva versione principale dell'API e
  la versione esistente verrà ritirata dopo un periodo di tempo ragionevole.
  Nell'API possono essere introdotte modifiche non sostanziali senza modificare la
  versione principale. A partire da giugno 2026, l'**API Interactions** è disponibile
  e supportata in `v1`.
- **v1beta**: questa versione include funzionalità e capacità iniziali in fase di sviluppo attivo. Sebbene le funzionalità in `v1beta` possano essere soggette a modifiche man mano che le perfezioniamo in base al feedback, ti consentono di provare nuove funzionalità prima che vengano promosse alla versione stabile.

| Funzionalità | v1 | v1beta |
| --- | --- | --- |
| API Interactions |  |  |
| Generare contenuti: input solo testo |  |  |
| Genera contenuti - Input di testo e immagini |  |  |
| Genera contenuti - Output di testo |  |  |
| Generare contenuti - Conversazioni multi-turno (chat) |  |  |
| Genera contenuti - Chiamate di funzione |  |  |
| Genera contenuti - Streaming |  |  |
| Incorporare contenuti - Input solo testo |  |  |
| Genera risposta |  |  |
| Semantic retriever |  |  |

- - Supportato
- - Non sarà mai supportato

## Configurare la versione dell'API in un SDK

Per impostazione predefinita, gli SDK dell'API Gemini utilizzano `v1beta`, ma puoi specificare esplicitamente le versioni
impostando la versione dell'API come mostrato nel seguente esempio di codice:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-22 UTC."],[],[]]
