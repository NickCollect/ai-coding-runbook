---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=it
fetched_at: 2026-08-17T02:33:17.136540+00:00
title: "Esecuzione in background \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Esecuzione in background

Per le attività a lunga esecuzione come la ricerca approfondita, il ragionamento complesso o le esecuzioni di agenti in più passaggi, i timeout di connessione possono interrompere le richieste HTTP standard (che in genere si chiudono dopo 60 secondi). L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) fornisce l'**esecuzione in background** per eseguire queste attività in modo asincrono.

Per consentire all'interazione di essere eseguita fino al completamento dell'attività sul server, imposta `"background": true` quando crei l'interazione. L'API restituisce immediatamente un ID di interazione, che le applicazioni client possono utilizzare per eseguire il polling dello stato, lo streaming dei progressi o la riconnessione a uno stream disconnesso.

L'esecuzione in background è supportata per i modelli Gemini standard (ad esempio `gemini-3.6-flash` e `gemini-3.1-pro-preview`) e gli agenti gestiti (ad esempio `antigravity-preview-05-2026`).

## Creare un'interazione in background

Per avviare un'interazione in background, imposta il parametro `background` su `true` quando crei la risorsa.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Come funziona l'esecuzione in background

Quando crei un'interazione in background, l'attività viene eseguita in modo asincrono sul server. L'interazione passa attraverso vari stati di esecuzione:

- `in_progress`: il server sta eseguendo attivamente l'interazione (ad esempio, eseguendo codice o effettuando ricerche).
- `requires_action`: l'interazione è stata messa in pausa ed è in attesa dell'input del client (ad esempio, la conferma dell'esecuzione di uno strumento o la risposta a una domanda).
- `completed`: l'interazione è stata completata correttamente e l'output è disponibile.
- `failed`: si è verificato un errore durante l'esecuzione (ad esempio, un errore dello strumento o limiti di frequenza).
- `cancelled`: una richiesta del client ha interrotto l'esecuzione.

### Casi d'uso

Utilizza l'esecuzione in background per:

- **Esecuzioni di agenti:** attività che richiedono l'esecuzione di codice, la navigazione web o l'orchestrazione di sub-agenti (ad esempio `antigravity-preview-05-2026`).
- **Ricerca approfondita:** esecuzioni che utilizzano `deep-research-preview-04-2026` o `deep-research-max-preview-04-2026` e che richiedono diversi minuti.
- **Ragionamento lungo:** attività in cui i passaggi di pensiero del modello superano i limiti di connessione HTTP standard.

## Recuperare i risultati

Ottieni i risultati dell'interazione in background utilizzando il **polling** o lo **streaming**.

### Sequenza di polling (non bloccante)

Il polling controlla periodicamente lo stato dell'interazione utilizzando richieste GET non bloccanti finché non raggiunge uno stato terminale.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Sequenza di streaming

Se un'interruzione della rete disconnette uno stream, lo streaming può riprendere dall'ultimo evento ricevuto. Ogni delta contiene un `event_id` univoco nel relativo payload. Se passi questo ID come `last_event_id`, lo stream riprende da quell'evento.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Conversazioni multi-turno

Le interazioni successive possono essere concatenate a una conversazione in background utilizzando `previous_interaction_id`, soggetta a questi vincoli:

1. **Le esecuzioni attive sono bloccate:** la concatenazione di un'interazione successiva a una con stato `in_progress` restituisce un errore `400 Bad Request`. Attendi che l'interazione raggiunga lo stato `completed` prima di iniziare la successiva.
2. **Parametro dell'ambiente per gli agenti gestiti:** quando concateni le interazioni per gli agenti gestiti (ad esempio `antigravity-preview-05-2026`), le richieste devono includere sia `previous_interaction_id` sia `environment`.

Gli esempi seguenti mostrano come concatenare le interazioni:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Annullamento ed eliminazione

Controlla le esecuzioni in corso e gestisci lo spazio di archiviazione utilizzando le richieste di annullamento ed eliminazione:

- **Annulla (`POST /interactions/{id}/cancel`):** interrompe l'attività in esecuzione. Lo stato passa a `cancelled`. Le azioni di pulizia sul server possono causare un leggero ritardo prima che lo stato venga aggiornato nelle richieste GET.
- **Elimina (`DELETE /interactions/{id}`):** rimuove i record di interazione dal server. Le richieste GET successive restituiscono un errore `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Passaggi successivi

- Leggi la [panoramica dell'API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) per comprendere la gestione di sessioni e stati.
- Consulta la guida [Interazioni di streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=it) per i dettagli sugli aggiornamenti degli eventi in tempo reale.
- Esplora la [guida rapida Agenti gestiti](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it) per creare agenti a più turni con stato.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
