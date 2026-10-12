---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=it
fetched_at: 2026-10-12T06:52:22.589652+00:00
title: "Novit\u00e0 di Gemini 3.8 Flash \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Novità di Gemini 3.8 Flash

[3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=it)
[Altri modelli](#other-models)

Gemini 3.8 Flash (`gemini-3.8-flash`) è in disponibilità generale (GA) e pronto per l'utilizzo in produzione. È il nostro modello Flash più intelligente, progettato per l'ingegneria del software a lungo termine, gli agenti autonomi e i workflow aziendali complessi.

Questa guida spiega le novità di Gemini 3.8 Flash, le modifiche all'API, gli esempi di codice e le indicazioni per la migrazione.

## Nuovo modello

| Modello | ID modello | Livello di ragionamento predefinito | Prezzi | Descrizione |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash è disponibile fino alla fine dell'anno a un prezzo di lancio di 0,75 $per 1 milione di token di input e 3,75 $per 1 milione di token di output. Per saperne di più, consulta i [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it). | Il nostro modello Flash più intelligente, progettato per l'ingegneria del software a lungo termine, gli agenti autonomi e i workflow aziendali complessi. |

Gemini 3.8 Flash supporta una finestra contestuale di 1 milione di token, 64.000 token di output massimi, livelli di pensiero regolabili (`low`, `medium`, `high`) e la stessa suite di strumenti integrati.

Per le specifiche complete, consulta la [pagina del modello Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=it). Per i dettagli sui prezzi introduttivi, consulta la [sezione Prezzi](#pricing) di seguito o la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-3.8-flash).

## Guida rapida

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a three.js script that renders a realistic 3D black hole."
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole."}]
    }]
  }'
```

## Novità di Gemini 3.8 Flash

- **Ingegneria software a lungo termine**:offre risultati eccellenti nei benchmark di programmazione del mondo reale, nel refactoring complesso di più file e nell'esecuzione deterministica degli strumenti. Per i dettagli, consulta la [metodologia di valutazione](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=it).
- **Agenti autonomi:** ti consente di creare workflow di pianificazione e orchestrazione degli strumenti in più fasi resilienti, riducendo notevolmente i loop e gli errori non riusciti.
- **Flussi di lavoro aziendali complessi**:offre un'accuratezza superiore, un ragionamento approfondito e un'elevata rigorosità fattuale in attività di dominio impegnative e pipeline di dati su larga scala.
- **Modello predefinito per gli agenti gestiti**: l'agente predefinito per gli agenti gestiti, l'[agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it), ora utilizza Gemini 3.8 Flash. L'[SDK Antigravity](https://antigravity.google/docs/sdk/overview/?hl=it) utilizza anche Gemini 3.8 Flash per impostazione predefinita.
- **Prezzi introduttivi:** Gemini 3.8 Flash è disponibile a una tariffa introduttiva di 0,75 $per 1 milione di token di input e 3,75 $per 1 milione di token di output fino al 31 dicembre 2026. I prezzi standard di 1,50 $per 1 milione di token di input e 7,50 $per 1 milione di token di output entreranno in vigore il 1° gennaio 2027.

Gemini 3.8 Flash può utilizzare più token per attività più lunghe e complesse, per progettazione. Per fornire risultati di qualità superiore per obiettivi difficili e in più passaggi, il modello esegue passaggi di ragionamento più piccoli, chiama gli strumenti in modo iterativo e verifica il suo lavoro man mano. Non tutti i workflow richiedono questo livello di verifica. Per le attività quotidiane, puoi ridurre lo sforzo di [ragionamento](#understanding-reasoning-levels) per diminuire il consumo di token. In alternativa, Gemini 3.6 Flash continua a essere supportato.

## Informazioni sui livelli di ragionamento

Gemini 3.8 Flash ti offre un controllo flessibile su latenza e intelligenza regolando il livello di ragionamento del modello:

- **Impegno di ragionamento ridotto**: riduce il tempo di risposta per le attività sensibili alla latenza come le pipeline di risposta agli incidenti, la chat in tempo reale, la stesura di bozze e l'analisi rapida dei dati.
- **Media (predefinita)**: la migliore qualità per la maggior parte delle attività. Consigliato per casi d'uso complessi di codice e agentici, in quanto offre una maggiore precisione al primo passaggio.
- **Impegno di ragionamento elevato**: massimizza le capacità di ragionamento e di orchestrazione degli strumenti del modello. Ideale per ragionamenti approfonditi, matematica e attività multi-step difficili.

Il seguente esempio imposta `thinking_level` su `medium` per una richiesta di analisi del codice complessa:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="medium"  # Balanced reasoning effort for complex tasks
        ),
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  config: {
    thinkingConfig: {
      thinkingLevel: "medium", // Balanced reasoning effort for complex tasks
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Agente Antigravity aggiornato

## Elenco di controllo per la migrazione

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Esegui la migrazione a gemini-3.8-flash

- **Aggiorna ID modello**:modifica la stringa del modello target in `gemini-3.8-flash`.
- **Configura il livello di pensiero**:sostituisci `thinking_budget` con l'enumerazione di stringa `thinking_level`. Tieni presente che `minimal` non è supportato su Gemini 3.8 Flash; scegli `low`, `medium` (impostazione predefinita) o `high`.
- **Applica le modifiche ai parametri dell'API Gemini 3:** rimuovi i parametri di campionamento ritirati (`temperature`, `top_p`, `top_k`), `candidate_count` (non supportato in Gemini 3 e versioni successive) e i turni del modello precompilati. Consulta
  [Modifiche all'API Gemini 3.6 e aggiornamenti dei parametri](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=it#api-changes-and-parameter-updates).
- **Applica regole di convalida dei turni**:rimuovi i turni del modello precompilati e assicurati che il turno finale dell'utente contenga testo non vuoto.
- **Audit function calling:**
  - Inserisci gli asset multimodali all'interno del payload della risposta.
  - Formatta le istruzioni in linea utilizzando `\n\n`.
  - Se visualizzi errori `Malformed_Function_Call` relativi al testo pre-strumento, consulta [Soluzioni alternative per i requisiti del testo pre-strumento](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=it#workarounds-for-pre-tool-text-requirements).
  - Solo se utilizzi l'API generateContent: assicurati che tutti gli oggetti `FunctionResponse` includano `call_id` e `name`.
- **Requisiti di base di Gemini 3**:per gli aggiornamenti dell'SDK e la conservazione della firma del pensiero, consulta [Firme del pensiero](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it).

## Prezzi

Approfitta dei prezzi di lancio in Google AI Studio e Gemini Enterprise Agent Platform fino al 31 dicembre 2026 per Gemini 3.8 Flash e Gemini 3.6 Flash. I prezzi standard entreranno in vigore il 1° gennaio 2027. Per i livelli di prezzo completi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-3.8-flash).

## Altri modelli

- [Gemini 3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=it)
- [Visualizza tutti i modelli](https://ai.google.dev/gemini-api/docs/models?hl=it)

## Passaggi successivi

- Consulta le specifiche dell'API nella [panoramica dei modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).
- Esplora l'orchestrazione multi-agente nella [panoramica dell'API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it).
- Testa e perfeziona i prompt in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-09 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-09 UTC."],[],[]]
