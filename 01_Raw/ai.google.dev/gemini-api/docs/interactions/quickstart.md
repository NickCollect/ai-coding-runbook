---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=it
fetched_at: 2026-05-25T05:26:09.654405+00:00
title: "Guida rapida all'API Gemini \u00a0|\u00a0 Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida rapida all'API Gemini

Questa guida rapida mostra come installare le nostre [librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it)
ed effettuare la prima richiesta, trasmettere in streaming le risposte, creare conversazioni multi-turno
e utilizzare gli strumenti.

Esistono due modi per inviare una richiesta all'API Gemini:

- ***(Consigliato)*** L'[API Interactions](https://ai.google.dev/api/interactions-api?hl=it) è una nuova
  primitiva con supporto integrato per l'utilizzo di strumenti in più passaggi, l'orchestrazione e
  flussi di ragionamento complessi tramite passaggi di esecuzione digitati. In futuro, i nuovi
  modelli oltre alla famiglia principale di base, insieme a nuove capacità agentiche
  e strumenti, verranno lanciati esclusivamente sull'API Interactions.
- [`generateContent`](https://ai.google.dev/gemini-api/docs/quickstart?hl=it) fornisce un modo per generare
  una risposta stateless da un modello. Sebbene consigliamo di utilizzare l'API
  Interactions, `generateContent` è completamente supportata.

Questa versione della guida rapida utilizza l'API Interactions per inviare una richiesta all'API Gemini.

## Prima di iniziare

Per utilizzare l'API Gemini, devi disporre di una chiave API per autenticare le richieste, applicare limiti di sicurezza e monitorare l'utilizzo del tuo account.

Per iniziare, creane uno su AI Studio senza costi:

[Crea una chiave API Gemini](https://aistudio.google.com/app/apikey?hl=it)

## Installa l'SDK Google GenAI

### Python

Utilizzando [Python 3.9+](https://www.python.org/downloads/), installa il
[pacchetto `google-genai`](https://pypi.org/project/google-genai/)
utilizzando il seguente
[comando pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Utilizzando [Node.js v18+](https://nodejs.org/en/download/package-manager),
installa
[SDK Google Gen AI per TypeScript e JavaScript](https://www.npmjs.com/package/@google/genai)
utilizzando il seguente
[comando npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Genera testo

Utilizza il metodo `interactions.create` per
[generare una risposta di testo](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Risposte dinamiche

Per impostazione predefinita, il modello restituisce una risposta solo dopo il completamento dell'intero processo di generazione. Per un'esperienza più rapida e interattiva, puoi
[trasmettere in streaming i blocchi della risposta](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=it) man mano che
vengono generati.

### Python

```
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in detail",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in detail",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

main();
```

### REST

```
# Use alt=sse for streaming
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in detail",
    "stream": true
  }'
```

## Conversazioni a più turni

L'API Gemini supporta la creazione di
[conversazioni multi-turno](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it#multi-turn-conversations).
Basta passare il valore `id` restituito dall'interazione precedente come parametro `previous_interaction_id` e il server gestisce automaticamente la cronologia delle conversazioni.

### Python

```
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

main();
```

### REST

```
# Turn 1: Start the conversation
RESPONSE1=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

# Extract the interaction ID
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Turn 2: Continue the conversation
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"input\": \"How many paws are in my house?\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

## Utilizzare gli strumenti

Estendi le funzionalità del modello
[basando le risposte sulla Ricerca Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it)
per accedere a contenuti web in tempo reale. Il modello decide automaticamente quando
eseguire ricerche, esegue query e sintetizza una risposta con citazioni.

Il seguente esempio mostra come attivare la Ricerca Google:

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  - [{annotation.title}]({annotation.url})")
```

### JavaScript

```
async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
  });

  console.log(interaction.output_text);

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text' && contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              console.log(`  - [${annotation.title}](${annotation.url})`);
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
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

L'API Gemini supporta anche altri strumenti integrati:

- **[Esecuzione del codice](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=it)**:
  Consente al modello di scrivere ed eseguire codice Python per risolvere problemi matematici complessi.
- **[Contesto URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=it)**: consente di
  basare le risposte su URL di pagine web specifici che fornisci.
- **[Ricerca di file](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=it)**: ti consente di
  caricare file e basare le risposte sui loro contenuti utilizzando la ricerca semantica.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=it)**: ti consente di
  basare le risposte sui dati sulla posizione e cercare luoghi, indicazioni e
  mappe.
- **[Utilizzo del computer](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=it)**: consente al modello di interagire con uno schermo, una tastiera e un mouse virtuali per eseguire attività.

## Chiamare funzioni personalizzate

Utilizza le **[chiamate di funzione](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it)**
per connettere i modelli alle tue API e ai tuoi strumenti personalizzati. Il modello determina quando chiamare la funzione e restituisce un passaggio `function_call` con gli argomenti da eseguire per l'applicazione.

Questo esempio dichiara una funzione di temperatura simulata e verifica se il modello
vuole chiamarla.

### Python

```
import json

weather_function = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the temperature in London?",
    tools=[weather_function],
)

fc_step = None
for step in interaction.steps:
    if step.type == "function_call":
        fc_step = step
        break

if fc_step:
    print(f"Model requested function: {fc_step.name} with args {fc_step.arguments}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {
                "type": "function_result",
                "name": fc_step.name,
                "call_id": fc_step.id,
                "result": [{"type": "text", "text": json.dumps(mock_result)}],
            }
        ],
        tools=[weather_function],
        previous_interaction_id=interaction.id,
    )
    print("Final Response:", final_interaction.output_text)
```

### JavaScript

```
async function main() {
  const weatherFunction = {
    type: 'function',
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const interaction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the temperature in London?",
    tools: [weatherFunction],
  });

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  if (fcStep) {
    console.log(`Model requested function: ${fcStep.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    const finalInteraction = await ai.interactions.create({
      model: 'gemini-3-flash-preview',
      input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: 'text', text: JSON.stringify(mockResult) }]
      }],
      tools: [weatherFunction],
      previous_interaction_id: interaction.id,
    });

    console.log("Final Response:", finalInteraction.output_text);
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

## Passaggi successivi

Ora che hai iniziato a utilizzare l'API Gemini, esplora le seguenti guide per creare applicazioni più avanzate:

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it)
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=it)
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=it)
- [Pensiero](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=it)
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it)
- [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=it)
- [Contesto lungo](https://ai.google.dev/gemini-api/docs/long-context?hl=it)
- [Incorporamenti](https://ai.google.dev/gemini-api/docs/embeddings?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
