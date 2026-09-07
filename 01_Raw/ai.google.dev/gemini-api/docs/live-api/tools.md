---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=fr
fetched_at: 2026-09-07T05:35:33.139015+00:00
title: "Utilisation de l'outil avec l'API\u00a0Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Utilisation de l'outil avec l'API Live

L'utilisation d'outils permet à l'API Live d'aller au-delà de la simple conversation en lui permettant d'effectuer des actions dans le monde réel et d'extraire un contexte externe tout en maintenant une connexion en temps réel.
Vous pouvez définir des outils tels que [l'appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr)
et [la recherche Google](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) avec l'API Live.

## Présentation des outils compatibles

Voici un bref aperçu des outils disponibles pour les modèles d'API Live :

| Outil | Preview Gemini 3.1 Flash-Live | Preview Gemini 2.5 Flash-Live |
| --- | --- | --- |
| **Rechercher** | Compatible | Compatible |
| **Appel de fonction** | Compatible (synchrone uniquement) | Compatible (synchrone et [asynchrone](#async-function-calling)) |
| **Google Maps** | Non compatible | Non compatible |
| **Exécution de code** | Non compatible | Non compatible |
| **Contexte d'URL** | Non compatible | Non compatible |

## Appel de fonction

L'API Live est compatible avec l'appel de fonction, tout comme les requêtes de génération de contenu classiques. L'appel de fonction permet à l'API Live d'interagir avec des données et des programmes externes, ce qui augmente considérablement les possibilités de vos applications.

Vous pouvez définir des déclarations de fonction dans la configuration de la session.
Après avoir reçu des appels d'outil, le client doit répondre avec une liste d'objets `FunctionResponse` à l'aide de la méthode `session.send_tool_response`.

Pour en savoir
plus, consultez le [tutoriel sur l'appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr).

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.1-flash-live-preview"

# Simple function definitions
turn_on_the_lights = {"name": "turn_on_the_lights"}
turn_off_the_lights = {"name": "turn_off_the_lights"}

tools = [{"function_declarations": [turn_on_the_lights, turn_off_the_lights]}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "Turn on the lights please"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for response in session.receive():
            if response.data is not None:
                wf.writeframes(response.data)
            elif response.tool_call:
                print("The tool was called")
                function_responses = []
                for fc in response.tool_call.function_calls:
                    function_response = types.FunctionResponse(
                        id=fc.id,
                        name=fc.name,
                        response={ "result": "ok" } # simple, hard-coded function response
                    )
                    function_responses.append(function_response)

                await session.send_tool_response(function_responses=function_responses)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

// Simple function definitions
const turn_on_the_lights = { name: "turn_on_the_lights" } // , description: '...', parameters: { ... }
const turn_off_the_lights = { name: "turn_off_the_lights" }

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Turn on the lights please';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  for (const turn of turns) {
    if (turn.toolCall) {
      console.debug('A tool was called');
      const functionResponses = [];
      for (const fc of turn.toolCall.functionCalls) {
        functionResponses.push({
          id: fc.id,
          name: fc.name,
          response: { result: "ok" } // simple, hard-coded function response
        });
      }

      console.debug('Sending tool response...\n');
      session.sendToolResponse({ functionResponses: functionResponses });
    }
  }

  // Check again for new messages
  turns = await handleTurn();

  // Combine audio data strings and save as wave file
  const combinedAudio = turns.reduce((acc, turn) => {
      if (turn.data) {
          const buffer = Buffer.from(turn.data, 'base64');
          const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);
          return acc.concat(Array.from(intArray));
      }
      return acc;
  }, []);

  const audioBuffer = new Int16Array(combinedAudio);

  const wf = new WaveFile();
  wf.fromScratch(1, 24000, '16', audioBuffer);  // output is 24kHz
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

À partir d'un seul prompt, le modèle peut générer plusieurs appels de fonction et le code nécessaire pour chaîner leurs sorties. Ce code s'exécute dans un environnement de bac à sable, générant par la suite des messages [BidiGenerateContentToolCall](https://ai.google.dev/api/live?hl=fr#bidigeneratecontenttoolcall).

## Appel de fonction asynchrone

Par défaut, l'appel de fonction s'exécute de manière séquentielle, ce qui signifie que l'exécution est interrompue jusqu'à ce que les résultats de chaque appel de fonction soient disponibles. Cela garantit un traitement séquentiel, ce qui signifie que vous ne pourrez pas continuer à interagir avec le modèle pendant l'exécution des fonctions.

Si vous ne souhaitez pas bloquer la conversation, vous pouvez demander au modèle d'exécuter les fonctions de manière asynchrone. Pour ce faire, vous devez d'abord ajouter un `behavior` aux définitions de fonction :

### Python

```
# Non-blocking function definitions
turn_on_the_lights = {"name": "turn_on_the_lights", "behavior": "NON_BLOCKING"} # turn_on_the_lights will run asynchronously
turn_off_the_lights = {"name": "turn_off_the_lights"} # turn_off_the_lights will still pause all interactions with the model
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior } from '@google/genai';

// Non-blocking function definitions
const turn_on_the_lights = {name: "turn_on_the_lights", behavior: Behavior.NON_BLOCKING}

// Blocking function definitions
const turn_off_the_lights = {name: "turn_off_the_lights"}

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]
```

`NON-BLOCKING` garantit que la fonction s'exécute de manière asynchrone pendant que vous pouvez continuer à interagir avec le modèle.

Vous devez ensuite indiquer au modèle comment se comporter lorsqu'il reçoit le `FunctionResponse` à l'aide du paramètre `scheduling`. Il peut :

- interrompre ce qu'il est en train de faire et vous informer immédiatement de la réponse qu'il a reçue
  (`scheduling="INTERRUPT"`),
- attendre qu'il ait terminé ce qu'il est en train de faire
  (`scheduling="WHEN_IDLE"`),
- ou ne rien faire et utiliser ces connaissances plus tard dans la discussion
  (`scheduling="SILENT"`)

### Python

```
# for a non-blocking function definition, apply scheduling in the function response:
  function_response = types.FunctionResponse(
      id=fc.id,
      name=fc.name,
      response={
          "result": "ok",
          "scheduling": "INTERRUPT" # Can also be WHEN_IDLE or SILENT
      }
  )
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior, FunctionResponseScheduling } from '@google/genai';

// for a non-blocking function definition, apply scheduling in the function response:
const functionResponse = {
  id: fc.id,
  name: fc.name,
  response: {
    result: "ok",
    scheduling: FunctionResponseScheduling.INTERRUPT  // Can also be WHEN_IDLE or SILENT
  }
}
```

## Ancrage avec la recherche Google

Vous pouvez activer l'ancrage avec la recherche Google dans la configuration de la session. Cela augmente la précision de l'API Live et évite les hallucinations. Pour en savoir plus, consultez le [tutoriel sur l'ancrage](https://ai.google.dev/gemini-api/docs/grounding?hl=fr) pour
en savoir plus.

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.1-flash-live-preview"

tools = [{'google_search': {}}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "When did the last Brazil vs. Argentina soccer match happen?"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for chunk in session.receive():
            if chunk.server_content:
                if chunk.data is not None:
                    wf.writeframes(chunk.data)

                # The model might generate and execute Python code to use Search
                model_turn = chunk.server_content.model_turn
                if model_turn:
                    for part in model_turn.parts:
                        if part.executable_code is not None:
                            print(part.executable_code.code)

                        if part.code_execution_result is not None:
                            print(part.code_execution_result.output)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const tools = [{ googleSearch: {} }]
const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'When did the last Brazil vs. Argentina soccer match happen?';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  let combinedData = '';
  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.modelTurn && turn.serverContent.modelTurn.parts) {
      for (const part of turn.serverContent.modelTurn.parts) {
        if (part.executableCode) {
          console.debug('executableCode: %s\n', part.executableCode.code);
        }
        else if (part.codeExecutionResult) {
          console.debug('codeExecutionResult: %s\n', part.codeExecutionResult.output);
        }
        else if (part.inlineData && typeof part.inlineData.data === 'string') {
          combinedData += atob(part.inlineData.data);
        }
      }
    }
  }

  // Convert the base64-encoded string of bytes into a Buffer.
  const buffer = Buffer.from(combinedData, 'binary');

  // The buffer contains raw bytes. For 16-bit audio, we need to interpret every 2 bytes as a single sample.
  const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);

  const wf = new WaveFile();
  // The API returns 16-bit PCM audio at a 24kHz sample rate.
  wf.fromScratch(1, 24000, '16', intArray);
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Combiner plusieurs outils

Vous pouvez combiner plusieurs outils dans l'API Live, ce qui augmente encore les capacités de votre application :

### Python

```
prompt = """
Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
"""

tools = [
    {"google_search": {}},
    {"function_declarations": [turn_on_the_lights, turn_off_the_lights]},
]

config = {"response_modalities": ["AUDIO"], "tools": tools}

# ... remaining model call
```

### JavaScript

```
const prompt = `Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
`

const tools = [
  { googleSearch: {} },
  { functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }
]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

// ... remaining model call
```

## Étape suivante

- Consultez d'autres exemples d'utilisation d'outils avec l'API Live dans le
  [guide pratique sur l'utilisation d'outils](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=fr).
- Pour en savoir plus sur les fonctionnalités et les configurations, consultez le
  [guide sur les fonctionnalités de l'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/04 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/04 (UTC)."],[],[]]
