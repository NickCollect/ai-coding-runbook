---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=it
fetched_at: 2026-08-10T03:26:18.213362+00:00
title: "Pensiero di Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Pensiero di Gemini

I modelli della serie [Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=it) utilizzano un
"processo di pensiero" che migliora notevolmente le loro capacità di ragionamento e pianificazione in più passaggi,
rendendoli altamente efficaci per attività complesse come la
programmazione, la matematica avanzata e l'analisi dei dati.

Quando utilizzi un modello di ragionamento, Gemini ragiona internamente prima di rispondere. L'API Interactions mostra questo ragionamento tramite passaggi `thought`, passaggi dedicati che vengono visualizzati in ordine cronologico insieme alle chiamate di funzione, agli input dell'utente o agli output del modello nell'array `steps`.

Ogni passaggio di pensiero contiene due campi:

| Campo | Obbligatorio | Descrizione |
| --- | --- | --- |
| `signature` | ✅ Sì | Una rappresentazione criptata dello stato di ragionamento interno del modello. È sempre presente, anche quando il modello esegue un ragionamento minimo. |
| `summary` | ❌ No | Un array di contenuti (testo e/o immagini) che riassume il ragionamento. Può essere vuoto a seconda della configurazione [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=it), se il modello ha eseguito un ragionamento sufficiente o del tipo di contenuto (ad esempio, i latenti delle immagini potrebbero non avere riepiloghi di testo). |

## Interazioni con il pensiero

L'avvio di un'interazione con un modello di ragionamento è simile a qualsiasi altra richiesta di interazione. Specifica uno dei [modelli con supporto per il pensiero](#thinking-levels) nel campo `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Riepiloghi del pensiero

I riepiloghi del pensiero forniscono insight sul processo di ragionamento interno del modello.
Per impostazione predefinita, viene restituito solo l'output finale. Puoi attivare i riepiloghi del pensiero con `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Un blocco di pensiero può contenere **solo una firma senza riepilogo** nei seguenti casi:

- Richieste semplici, in cui il modello non ha ragionato abbastanza per generare un riepilogo
- `thinking_summaries: "none"`, dove i riepiloghi sono disattivati in modo esplicito
- Alcuni tipi di contenuti di pensiero, come le immagini, potrebbero non avere riepiloghi di testo

Il codice deve sempre gestire i blocchi di pensiero in cui `summary` è vuoto o assente.

## Streaming con il pensiero

Utilizza lo streaming per ricevere riepiloghi di pensiero incrementali durante la generazione.
I blocchi di pensiero vengono forniti utilizzando Server-Sent Events (SSE) con due tipi di delta distinti:

| Tipo di delta | Contiene | Tempi di invio |
| --- | --- | --- |
| `thought_summary` | Contenuti di riepilogo di testo o immagini | Uno o più delta con riepilogo incrementale |
| `thought_signature` | La firma crittografica | L'ultimo delta prima di `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

La risposta di streaming utilizza Server-Sent Events (SSE) ed è composta da passaggi ed eventi, ad esempio:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Controllo del pensiero

Per impostazione predefinita, i modelli Gemini utilizzano il pensiero dinamico, regolando automaticamente la quantità di ragionamento in base alla complessità della richiesta. Puoi controllare questo comportamento utilizzando il parametro `thinking_level`.

| Modello | Pensiero predefinito | Livelli supportati |
| --- | --- | --- |
| gemini-3.6-flash | On (medio) | minimal, low, medium, high |
| gemini-3.5-flash-lite | On (minimal) | minimal, low, medium, high |
| gemini-3.1-pro-preview | On (high) | low, medium, high |
| gemini-3.1-flash-lite-image | On (minimal) | minimal, high |
| gemini-3-flash-preview | On (high) | minimal, low, medium, high |
| gemini-3-pro-preview | On (high) | low, high |
| gemini-3.5-flash | On (medium) | minimal, low, medium, high |
| gemini-2.5-pro | On | low, medium, high |
| gemini-2.5-flash | On | low, medium, high |
| gemini-2.5-flash-lite | Off | low, medium, high |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Firme del pensiero

Le firme del pensiero sono rappresentazioni criptate del ragionamento interno del modello. Sono necessarie per mantenere la continuità del ragionamento nelle interazioni multi-turno.

L'API Interactions semplifica notevolmente la gestione delle firme del pensiero rispetto all'API `generateContent`.

### Modalità con stato (consigliata)

Per impostazione predefinita, quando utilizzi l'API Interactions in modalità con stato (impostando `store: true` e passando `previous_interaction_id` nei turni successivi), il server gestisce automaticamente lo stato della conversazione, inclusi tutti i blocchi di pensiero e le firme. In questa modalità non devi fare nulla per quanto riguarda le firme. Vengono gestite interamente sul lato server.

### Modalità senza stato

Se gestisci autonomamente lo stato della conversazione (modalità senza stato) e passi la cronologia completa di input e output in ogni richiesta:

- Devi **SEMPRE** inviare di nuovo tutti i blocchi `thought` esattamente come li hai ricevuti dal modello.
- Non devi **rimuovere o modificare** i blocchi di pensiero dalla cronologia, in quanto contengono le firme necessarie al modello per continuare il ragionamento.
- Quando cambi modello all'interno di una sessione, devi comunque inviare di nuovo i blocchi di pensiero del modello precedente. Il backend gestisce la compatibilità.

## Prezzi

Quando il pensiero è attivo, il prezzo della risposta è la somma dei token di output e dei token di pensiero. Puoi ottenere il numero totale di token di pensiero generati dal campo `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

I modelli di pensiero generano pensieri completi per migliorare la qualità della risposta finale
e poi restituiscono [riepiloghi](#summaries) per fornire insight sul
processo di pensiero. Il prezzo si basa sui token di pensiero completi che il modello deve generare, anche se dall'API viene restituito solo il riepilogo.

Scopri di più sui token nella guida al [conteggio dei token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

## Best practice

Utilizza i modelli di pensiero in modo efficiente seguendo queste linee guida.

- **Esamina il ragionamento**: analizza i riepiloghi del pensiero per comprendere gli errori e migliorare i prompt.
- **Controlla il budget di pensiero**: chiedi al modello di pensare meno per gli output lunghi per risparmiare token.
- **Attività semplici**: utilizza il pensiero minimo o basso per il recupero o la classificazione dei fatti (ad es. "Dove è stata fondata DeepMind?").
- **Attività moderate**: utilizza il pensiero predefinito per confrontare concetti o ragionamenti creativi (ad es. confronta auto elettriche e ibride).
- **Attività complesse**: utilizza il pensiero massimo per la programmazione avanzata, la matematica o la pianificazione in più passaggi (ad es. risolvi i problemi di matematica AIME).

## Passaggi successivi

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it): risposte di testo di base
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it): connettiti agli strumenti
- [Guida a Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=it): funzionalità specifiche del modello

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
