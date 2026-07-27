---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=it
fetched_at: 2026-07-27T04:33:37.642207+00:00
title: "Combinare strumenti integrati e chiamata di funzione \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Combinare strumenti integrati e chiamata di funzione

Gemini consente la combinazione di [strumenti integrati](https://ai.google.dev/gemini-api/docs/tools?hl=it), come `google_search`, e [chiamata di funzioni](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) (nota anche come *strumenti personalizzati*) in una singola interazione conservando ed esponendo la cronologia del contesto delle chiamate agli strumenti. Le combinazioni di strumenti integrati e personalizzati consentono
workflow complessi e basati su agenti in cui, ad esempio, il modello può basarsi
su dati web in tempo reale prima di richiamare la logica di business specifica.

Ecco un esempio che consente combinazioni di strumenti integrati e personalizzati con
`google_search` e una funzione personalizzata `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Come funziona

I modelli Gemini 3 utilizzano la *circolazione del contesto degli strumenti* per consentire combinazioni di strumenti integrati e personalizzati. La circolazione del contesto degli strumenti consente di preservare ed
esporre il contesto degli strumenti integrati e condividerlo con gli strumenti personalizzati nella stessa
interazione.

### Abilitare la combinazione di strumenti

- Includi [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#function-declarations), insieme
  agli strumenti integrati che vuoi utilizzare, per attivare il comportamento di combinazione.

### Passaggi per i resi API

In una risposta all'interazione, l'API restituisce passaggi separati per le chiamate allo strumento integrato
e le chiamate di funzione (strumento personalizzato):

- **Passaggi dello strumento integrato**: l'API li gestisce automaticamente, preservando
  il contesto tra i turni.
- **Passaggi di chiamata della funzione**: l'API restituisce `function_call` passaggi per le tue funzioni personalizzate. Esegui la funzione e fornisci il risultato.

### Campi critici nei passaggi restituiti

Alcuni campi nei passaggi restituiti sono fondamentali per mantenere il contesto dello strumento e consentire le combinazioni di strumenti:

- **`id`**: si trova nei passaggi `function_call` e `function_response`. Un identificatore univoco che associa una chiamata alla relativa risposta.
- **`signature`**: presente nei passaggi `thought`, nonché in tutti i passaggi di chiamata dello strumento (ad es. `function_call`) e dei risultati (ad es. `function_response`) per i modelli Gemini 3+. Questo contesto criptato consente la **circolazione del contesto dello strumento** tra le interazioni.

**Gestione di questi campi:**

- **Modalità con stato (consigliata)**: quando utilizzi `previous_interaction_id`, il server gestisce automaticamente i campi `id` e `signature`.
- **Modalità stateless**: quando gestisci manualmente la cronologia delle conversazioni, devi assicurarti di trasmettere i campi `id` e `signature` al modello nelle richieste successive per convalidare l'autenticità e mantenere il contesto. Gli SDK ufficiali gestiscono questa operazione automaticamente se passi l'oggetto della risposta completo alla cronologia.

### Dati specifici dello strumento

Alcuni strumenti integrati restituiscono argomenti di dati visibili agli utenti specifici per il tipo di strumento.

| Strumento | Argomenti della chiamata allo strumento visibili all'utente (se presenti) | Risposta dello strumento visibile all'utente (se presente) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL da visitare | `status`: Stato della scansione `retrieved_url`: URL scansionati |
| **file\_search** | Nessuno | Nessuno |

## Token e prezzi

Tieni presente che le parti di chiamata dello strumento integrate nelle richieste vengono conteggiate ai fini di
`prompt_token_count`. Poiché questi passaggi intermedi dello strumento sono ora visibili e
ti vengono restituiti, fanno parte della cronologia della conversazione. Questo vale solo per le *richieste*, non per le *risposte*.

Lo strumento Ricerca Google è un'eccezione a questa regola. La Ricerca Google applica già il proprio modello di prezzi a livello di query, pertanto i token non vengono addebitati due volte (consulta la pagina [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it)).

Per saperne di più, consulta la pagina [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

## Limitazioni

- Impostazione predefinita della modalità `validated` (la modalità `auto` non è supportata) quando
  è attivata la circolazione del contesto dello strumento.
- Gli strumenti integrati come `google_search` si basano su informazioni relative alla posizione e all'ora corrente, quindi se `system_instruction` o `function_declaration.description` hanno informazioni su posizione e ora in conflitto, la funzionalità di combinazione degli strumenti potrebbe non funzionare correttamente.

## Strumenti supportati

La circolazione del contesto degli strumenti standard si applica agli strumenti lato server (integrati).
Code Execution è anche uno strumento lato server, ma ha una propria soluzione integrata per la circolazione del contesto. L'utilizzo del computer e la chiamata di funzioni sono strumenti lato client
e dispongono anche di soluzioni integrate per la circolazione del contesto.

| Strumento | Lato esecuzione | Supporto per la circolazione del contesto |
| --- | --- | --- |
| [la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) | Lato server | Supportato |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) | Lato server | Supportato |
| [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) | Lato server | Supportato |
| [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) | Lato server | Supportato |
| [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) | Lato server | Supportato (integrato, utilizza i passaggi `code_execution` e `code_execution_result`) |
| [Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) | Lato client | Supportato (integrato, utilizza i passaggi `function_call` e `function_response`) |
| [Funzioni personalizzate](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) | Lato client | Supportato (integrato, utilizza i passaggi `function_call` e `function_response`) |

## Passaggi successivi

- Scopri di più sulla [chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) nell'API Gemini.
- Esplora gli strumenti supportati:
  - [la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)
  - [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)
  - [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-06 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-06 UTC."],[],[]]
