---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=it
fetched_at: 2026-08-24T02:23:53.843525+00:00
title: "Spiegazione delle versioni API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Riferimento API](https://ai.google.dev/api?hl=it)

Invia feedback

# Spiegazione delle versioni API

Questo documento fornisce una panoramica generale delle differenze tra le versioni `v1`
e `v1beta` dell'API Gemini.

- **v1**: versione stabile dell'API. Le funzionalità della versione stabile sono completamente supportate per l'intero ciclo di vita della versione principale. In caso di modifiche che causano interruzioni, verrà creata una nuova versione principale dell'API e la versione esistente verrà ritirata dopo un periodo di tempo ragionevole.
  Le modifiche che non causano interruzioni possono essere introdotte nell'API senza modificare la versione principale. L'**API Interactions** e le relative funzionalità principali sono generalmente disponibili in `v1`.
- **v1beta**: questa versione include funzionalità e funzionalità iniziali in fase di sviluppo
  attivo. Sebbene le funzionalità di `v1beta` possano essere soggette a modifiche man mano che le perfezioniamo in base al feedback, ti consentono di provare nuove funzionalità prima che vengano promosse alla versione stabile.

## Supporto di funzionalità e funzionalità

La tabella seguente descrive in dettaglio la disponibilità delle funzionalità in `v1` (GA)
e `v1beta` (beta). Le funzionalità e gli strumenti principali dell'API si applicano sia all'API Interactions sia a `generateContent`, se non diversamente specificato:

| Funzionalità | v1 | v1beta |
| --- | --- | --- |
| **Funzionalità principali dell'API** |  |  |
| [API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=it) |  |  |
| [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) |  |  |
| [Output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) |  |  |
| [Pensiero / ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it) |  |  |
| [Istruzioni di sistema](https://ai.google.dev/gemini-api/docs/system-instructions?hl=it) |  |  |
| [Output audio (configurazione vocale)](https://ai.google.dev/gemini-api/docs/audio?hl=it) |  |  |
| [Livello di servizio (priorità / flessibilità)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it) |  |  |
| **Strumenti** |  |  |
| [Strumento di esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) |  |  |
| [Grounding della Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) |  |  |
| [Grounding di Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) |  |  |
| [Strumento di contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) |  |  |
| [Strumento di ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) |  |  |
| [Strumento di utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) |  |  |
| [Strumento dei server MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=it) |  |  |
| **API in tempo reale** |  |  |
| [API Live (WebSocket)](https://ai.google.dev/gemini-api/docs/live-api?hl=it) |  |  |
| [API Live Music](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=it) |  |  |
| [Token effimeri (API Live)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=it) |  |  |
| **API della piattaforma** |  |  |
| [API Models](https://ai.google.dev/gemini-api/docs/models?hl=it) |  |  |
| [Route del servizio File](https://ai.google.dev/gemini-api/docs/files?hl=it) |  |  |
| [Route degli archivi di ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) |  |  |
| [API Agents](https://ai.google.dev/gemini-api/docs/agents?hl=it) |  |  |
| [API Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=it) |  |  |
| [Memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it) |  |  |

- - Supportato

## Configurare la versione dell'API in un SDK

Per impostazione predefinita, gli SDK dell'API Gemini utilizzano `v1beta`, ma puoi specificare esplicitamente le versioni impostando la versione dell'API come mostrato nel seguente esempio di codice:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
  }'
```

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-28 UTC."],[],[]]
