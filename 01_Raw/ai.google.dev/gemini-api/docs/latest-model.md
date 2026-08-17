---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=it
fetched_at: 2026-08-17T02:35:02.262525+00:00
title: "Utilizzo dei modelli Gemini pi\u00f9 recenti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo dei modelli Gemini più recenti

[Questa pagina](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=it)

Gemini 3.6 Flash (`gemini-3.6-flash`) e Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) sono in disponibilità generale e pronti per l'utilizzo in produzione.

- **Gemini 3.6 Flash**: prestazioni migliori per attività agentiche e multimodali complesse, con un utilizzo ridotto dei token e un prezzo inferiore rispetto a 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: il modello più veloce ed economico della famiglia 3.5. Supera le generazioni precedenti di Flash-Lite per l'esecuzione ad alto throughput.

Questa guida spiega le novità di ogni modello, le modifiche all'API che interessano il tuo codice e come eseguire la migrazione.

### Gemini 3.6 Flash

1. Installa la skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Applica la skill:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Installa la skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Applica la skill:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Nuovi modelli

| Modello | ID modello | Livello di pensiero predefinito | Prezzi | Descrizione |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1,50 $ per 1 milione di token di input e 7,50 $per 1 milione di token di output | Bilancia velocità e intelligenza per attività agentiche e multimodali. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0,30 $ per 1 milione di token di input e 2,50 $per 1 milione di token di output | Il modello 3.5 più veloce ed economico per l'esecuzione ad alto throughput. |

Entrambi i modelli supportano la finestra contestuale di 1 milione di token, un massimo di 64.000 token di output, il ragionamento e la suite completa di strumenti integrati, incluso [l'utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it).

Per le specifiche complete, consulta le pagine dei modelli:

- [Pagina del modello Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it)
- [Pagina del modello Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it)

Per informazioni dettagliate sui prezzi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Guida rapida

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## Novità di Gemini 3.6 Flash

- **Riduzione dei token e dei turni**:completa i workflow in più passaggi con meno passaggi di ragionamento, turni di conversazione e chiamate di strumenti rispetto a Gemini 3.5. Riduce anche la spirale del ciclo di esecuzione.
- **Generazione di codice migliorata**:produce codice di qualità superiore pronto per la produzione con meno modifiche indesiderate e meno cicli di debug.
- **Migliore rispetto delle istruzioni**: riduce le modifiche indesiderate ai file durante le attività di diagnostica.
- **Ragionamento multimodale e spaziale avanzato**:prestazioni migliorate nell'interpretazione dei grafici, nella conversione di progetti visivi e nella generazione di layout web multi-elemento.
- **Ispezione programmatica anticipata**:preferisce eseguire script di codice di diagnostica prima di apportare modifiche più frequentemente rispetto a Gemini 3.5 Flash. Ciò migliora la precisione delle attività complesse, ma può aggiungere passaggi esplorativi aggiuntivi al semplice lavoro di frontend.
- **Supporto per l'utilizzo del computer**:supportato come strumento nativo per l'automazione dell'interfaccia utente agentica.
- **Preferenza per lo stile dell'interfaccia utente**: più efficace nella creazione di codice funzionale, anche se i valutatori umani hanno preferito i modelli precedenti per il layout grafico e lo stile. Puoi mitigare questo problema fornendo linee guida di progettazione esplicite.
- **Impegno di pensiero predefinito (medio)** : utilizza lo stesso livello di pensiero predefinito `medium` di Gemini 3.5 Flash.
- **Prezzi ridotti**: costi dei token di output inferiori (7,50 $ per 1 milione rispetto a 9,00 $ per 1 milione per 3.5 Flash). I token di input rimangono a 1,50 $per 1 milione.

## Novità di Gemini 3.5 Flash-Lite

- **Latenza di esecuzione delle attività ridotta**:throughput più elevato nella famiglia 3.5 per l'analisi dei dati ad alto volume e l'estrazione dei documenti.
- **Prestazioni di ragionamento e multimodali migliorate**:percorso di migrazione efficace da Gemini 2.5 Flash, con punteggi più elevati nelle attività di ragionamento come HLE (18,0% rispetto a 11,0%) e nei benchmark multimodali come CharXIV (74,5% rispetto a 63,7%).
- **Orchestrazione di subagenti e affidabilità degli strumenti**:migliora l'affidabilità dell'esecuzione degli strumenti per l'esecuzione del codice, la ricerca e i workflow MCP. Aumenta il livello di pensiero per la pianificazione autonoma e le attività complesse dei subagenti.
- **Comprensione dei documenti migliorata**:migliora l'accuratezza dell'analisi dei documenti e dell'estrazione dei dati strutturati. Sperimenta con i livelli di pensiero minimo e alto a seconda della complessità del documento.
- **Programmazione web interattiva ed elaborazione di dati tabulari**:prestazioni elevate nell'elaborazione di JavaScript frontend e dati tabulari tramite la pianificazione tramite l'esecuzione di codice leggero.
- **Persistenza di chatbot e persona**:migliore rispetto delle istruzioni multi-turno e coerenza della persona rispetto a Gemini 3.1 Flash-Lite.
- **Supporto per l'utilizzo del computer**:supportato come strumento nativo per l'automazione dell'interfaccia utente agentica.

## Scegliere il modello Flash o Flash-Lite giusto

Utilizza questa tabella per selezionare il modello e il percorso di migrazione giusti per i tuoi carichi di lavoro.

Entrambi i modelli richiedono la rimozione dei parametri di campionamento deprecati (`temperature`, `top_p`, `top_k`) e dei turni di modello precompilati. Per maggiori dettagli, consulta [Modifiche all'API](#api-changes-and-parameter-updates).

| Modello | Casi d'uso principali | Target di migrazione consigliato |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Generazione di codice, ragionamento spaziale/multimodale, workflow agentici in più passaggi | **Gemini 3.5 Flash**, **Gemini 3 Flash (anteprima)** o **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | Esecuzione autonoma di subagenti, analisi dei dati ad alto volume ed estrazione dei documenti, analisi JSON strutturata | **Gemini 3.1 Flash-Lite** o **Gemini 2.5 Flash** |

## Agente Antigravity aggiornato

Grazie alle prestazioni migliorate, Gemini 3.6 Flash è ora il nuovo modello predefinito che alimenta l'[agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it) in Gemini Managed Agents. Puoi modificare questa impostazione impostando un nuovo campo nell'API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Modifiche all'API e aggiornamenti dei parametri

A partire da Gemini 3.6 Flash e Gemini 3.5 Flash-Lite, le seguenti modifiche all'API si applicano a questi modelli e a tutte le future release dei modelli Gemini.

- **Deprecazione dei parametri di campionamento**: `temperature`, `top_p` e `top_k` sono deprecati. L'API ignora questi parametri e restituisce un errore nelle future generazioni di modelli.
- **Convalida del turno del modello precompilato**: la precompilazione dei turni del modello non è più supportata. Se l'ultimo turno non vuoto nella richiesta è un turno `model`, l'API restituisce un errore `400`.

Di seguito sono riportate spiegazioni dettagliate ed esempi di codice per ogni modifica all'API.

### 1. Deprecazione dei parametri di campionamento (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` e `top_k` sono deprecati e ignorati. Nelle future generazioni di modelli, la fornitura di questi parametri restituisce un errore HTTP 400. **Rimuovi questi parametri da tutte le richieste.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Per migliorare il determinismo, definisci un'istruzione di sistema con regole esplicite per il tuo caso d'uso specifico.

### 2. Convalida del turno del modello precompilato

Le richieste API che terminano con un turno di ruolo del modello non vuoto non sono consentite e restituiscono un **errore HTTP 400**.

#### ⚠️ Evita

Nei payload REST `generateContent` o non elaborati precedenti, la fine con un turno di ruolo del modello non è più consentita:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Migrazione consigliata (API Interactions)

Nell'API Interactions, i turni del modello non vengono precompilati manualmente. Se in precedenza l'applicazione precompilava un turno del modello per eliminare i preamboli o forzare la formattazione JSON, utilizza system\_instruction o [output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) invece.

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## Elenco di controllo per la migrazione

### Gemini 3.6 Flash

1. Installa la skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Applica la skill:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Installa la skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Applica la skill:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Eseguire la migrazione a gemini-3.6-flash

- **Aggiorna l'ID modello**:modifica la stringa del modello di destinazione in `gemini-3.6-flash`.
- **Rimuovi i parametri di campionamento deprecati:**
  - Rimuovi `temperature`, `top_p` e `top_k` dalle configurazioni di generazione.
  - Sostituisci `thinking_budget` con l'enumerazione di stringhe `thinking_level` impostata su `"medium"` o `"high"`.
  - Rimuovi `candidate_count` (non supportato in Gemini 3.x).
- **Applica le regole di convalida dei turni**
  - Standardizza le conversazioni multi-turno su `previous_interaction_id` lato server.
  - Rimuovi i turni del modello precompilati.
- **Controlla la chiamata di funzione**
  - Inserisci gli asset multimodali nel payload della risposta.
  - Formatta le istruzioni in linea utilizzando `\n\n`.
  - Se visualizzi errori `Malformed_Function_Call` associati al testo pre-strumento, consulta [Soluzioni alternative per i requisiti del testo pre-strumento](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#workarounds-for-pre-tool-text-requirements).
  - Solo se utilizzi l'API generateContent: assicurati che tutti gli oggetti `FunctionResponse` includano `call_id` e `name`.
- **Requisiti di base di Gemini 3.x**:per gli aggiornamenti dell'SDK e la conservazione della firma del pensiero, consulta l'[elenco di controllo per la migrazione di Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=it#migration).

### Eseguire la migrazione a gemini-3.5-flash-lite

- **Aggiorna l'ID modello**:modifica la stringa del modello di destinazione in `gemini-3.5-flash-lite`.
- **Configura il livello di impegno di pensiero:**
  - Per l'estrazione, il routing o la classificazione ad alto volume: lascia `thinking_level` su `"minimal"` (impostazione predefinita) per il massimo throughput.
  - Per i subagenti autonomi con chiamate di strumenti, esecuzione di codice o ragionamento multi-step: imposta `thinking_level` su `"medium"` o `"high"` per evitare la chiusura prematura dello strumento.
- **Rimuovi i parametri deprecati e convalida la chiamata di funzione:** Applica le [stesse regole di 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **Requisiti di base di Gemini 3.x**:consulta l'[elenco di controllo per la migrazione di Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=it#migration).

## Passaggi successivi

- Esamina le specifiche dell'API nella [panoramica dei modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).
- Esplora l'orchestrazione multi-agente nella [Guida all'API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it).
- Testa e perfeziona i prompt in [Google AI Studio](https://aistudio.google.com/?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
