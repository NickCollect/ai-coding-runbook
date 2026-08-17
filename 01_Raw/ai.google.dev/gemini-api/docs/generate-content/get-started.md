---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it
fetched_at: 2026-08-17T02:29:38.450842+00:00
title: "Guida introduttiva \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida introduttiva

Questa guida ti aiuterà a iniziare a utilizzare l'API **generateContent** legacy.
Per i nuovi progetti e le nuove applicazioni, consigliamo vivamente di utilizzare la nuova **API Interactions**, che è il modo più semplice e migliore per creare con i modelli e gli agenti Gemini.

Questa guida rapida mostra come installare le nostre
[librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it) ed effettuare la prima richiesta, trasmettere
le risposte, creare conversazioni a più turni e utilizzare gli strumenti utilizzando il metodo standard
`generateContent`.

## Ottieni una chiave API

Per utilizzare l'API Gemini, devi avere una chiave API per autenticare le richieste, applicare i limiti di sicurezza e monitorare l'utilizzo del tuo account.

- Google AI Studio crea automaticamente un progetto e una chiave API per i nuovi utenti.
  Puoi copiarla dalla pagina [Chiavi API](https://aistudio.google.com/api-keys?hl=it).
- Se hai bisogno di una nuova chiave, fai clic su **Crea chiave API** in AI Studio e segui la finestra di dialogo per aggiungere una nuova coppia chiave-progetto.

[Crea una chiave API Gemini](https://aistudio.google.com/apikey?hl=it)

Imposta la chiave come variabile di ambiente:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Esegui l'upgrade al livello a pagamento

L'upgrade al livello a pagamento aumenta i limiti di frequenza e richiede la configurazione della fatturazione Cloud.

- Fai clic su **Configura la fatturazione** nelle pagine Chiavi API
   o
  [Progetti](https://aistudio.google.com/projects?hl=it) di AI Studio.
- Segui la finestra di dialogo Fatturazione Cloud per creare o collegare un account di fatturazione, aggiungere un metodo di pagamento e pagare in anticipo un minimo di 10 $ (o l'equivalente in valuta locale) in crediti a pagamento.
- Visualizza l'utilizzo dell'API in [Google AI Studio](https://aistudio.google.com/usage?hl=it)
  in **Dashboard** > **Utilizzo**.

Per ulteriori informazioni, consulta la pagina [Fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it).

## Installa l'SDK Google GenAI

### Python

Utilizzando [Python 3.9 o versioni successive](https://www.python.org/downloads/), installa il
[`google-genai` pacchetto](https://pypi.org/project/google-genai/)
utilizzando il seguente
[comando pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Utilizzando [Node.js v18+](https://nodejs.org/en/download/package-manager),
installa l'
[SDK Google Gen AI per TypeScript e JavaScript](https://www.npmjs.com/package/@google/genai)
utilizzando il seguente
[comando npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Genera testo

Utilizza il metodo `models.generate_content` per
[generare una risposta di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Risposte dinamiche

Per impostazione predefinita, il modello restituisce una risposta solo al termine dell'intero processo di generazione. Per un'esperienza più rapida e interattiva, puoi
[trasmettere in streaming i blocchi di risposta](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#stream) man mano che
vengono generati.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Conversazioni multi-turno

Per le conversazioni multi-turno, gli SDK forniscono un helper `chats` stateful per
creare un'esperienza di [chat a più turni](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#chat)
che gestisce automaticamente la cronologia delle conversazioni.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Utilizzare gli strumenti

[Estendi le funzionalità del modello basando le risposte sulla Ricerca Google per accedere ai contenuti web in tempo reale.](https://ai.google.dev/gemini-api/docs/google-search?hl=it) Il modello decide automaticamente quando eseguire la ricerca, esegue le query e sintetizza una risposta.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

L'API Gemini supporta anche altri strumenti integrati:

- **[Esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**:
  consente al modello di scrivere ed eseguire codice Python per risolvere problemi matematici complessi.
- **[Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**: consente di
  basare le risposte su URL di pagine web specifici forniti dall'utente.
- **[Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**: consente di
  caricare file e basare le risposte sui relativi contenuti utilizzando la ricerca semantica.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**: consente di
  basare le risposte sui dati di località e cercare luoghi, indicazioni stradali e
  mappe.
- **[Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**: consente al
  modello di interagire con lo schermo, la tastiera e il mouse di un computer virtuale per
  eseguire attività.

## Chiamare funzioni personalizzate

Utilizza **[la chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)** per collegare
i modelli ai tuoi strumenti e alle tue API personalizzati. Il modello determina quando chiamare la funzione e restituisce un `functionCall` nella risposta che l'applicazione deve eseguire.

Questo esempio dichiara una funzione di temperatura fittizia e verifica se il modello vuole chiamarla.

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Passaggi successivi

Ora che hai iniziato a utilizzare l'API Gemini, esplora le seguenti guide per creare applicazioni più avanzate:

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it)
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it)
- [Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it)
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
- [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it)
- [Contesto lungo](https://ai.google.dev/gemini-api/docs/long-context?hl=it)
- [Incorporamenti](https://ai.google.dev/gemini-api/docs/embeddings?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
