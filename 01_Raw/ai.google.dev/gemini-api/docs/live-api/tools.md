---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=es-419
fetched_at: 2026-05-05T20:49:10.865434+00:00
title: "Tool use with Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Tool use with Live API

El uso de herramientas permite que la API de Live vaya más allá de la conversación, ya que le permite realizar acciones en el mundo real y extraer contexto externo mientras mantiene una conexión en tiempo real.
Puedes definir herramientas como la [llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
y la [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419) con la API de Live.

## Descripción general de las herramientas compatibles

A continuación, se incluye una breve descripción general de las herramientas disponibles para los modelos de la API de Live:

| Herramienta | Versión preliminar de Gemini 3.1 Flash Live | Versión preliminar de Gemini 2.5 Flash Live |
| --- | --- | --- |
| **Búsqueda** | Admitido | Admitido |
| **Llamada a función** | Admitido (solo síncrono) | Admitido (síncrono y [asíncrono](#async-function-calling)) |
| **Google Maps** | No admitido | No admitido |
| **Ejecución de código** | No admitido | No admitido |
| **Contexto de URL** | No admitido | No admitido |

## Llamada a función

La API de Live admite la llamada a función, al igual que las solicitudes de generación de contenido normales. La llamada a función permite que la API de Live interactúe con datos y programas externos, lo que aumenta en gran medida lo que pueden lograr tus aplicaciones.

Puedes definir declaraciones de funciones como parte de la configuración de la sesión.
Después de recibir llamadas a herramientas, el cliente debe responder con una lista de objetos `FunctionResponse` mediante el método `session.send_tool_response`.

Consulta el [instructivo de llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) para obtener
más información.

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

A partir de una sola instrucción, el modelo puede generar varias llamadas a funciones y el código necesario para encadenar sus resultados. Este código se ejecuta en un entorno de pruebas, lo que genera mensajes [BidiGenerateContentToolCall](https://ai.google.dev/api/live?hl=es-419#bidigeneratecontenttoolcall) posteriores.

## Llamada a función asíncrona

La llamada a función se ejecuta de forma secuencial de forma predeterminada, lo que significa que la ejecución se detiene hasta que estén disponibles los resultados de cada llamada a función. Esto garantiza el procesamiento secuencial, lo que significa que no podrás seguir interactuando con el modelo mientras se ejecutan las funciones.

Si no quieres bloquear la conversación, puedes indicarle al modelo que ejecute las funciones de forma asíncrona. Para ello, primero debes agregar un `behavior` a las definiciones de función:

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

`NON-BLOCKING` garantiza que la función se ejecute de forma asíncrona mientras puedes seguir interactuando con el modelo.

Luego, debes indicarle al modelo cómo debe comportarse cuando reciba el `FunctionResponse` con el parámetro `scheduling`. Puede hacer lo siguiente:

- Interrumpir lo que está haciendo y contarte sobre la respuesta que obtuvo de inmediato
  (`scheduling="INTERRUPT"`)
- Esperar hasta que termine lo que está haciendo
  (`scheduling="WHEN_IDLE"`)
- No hacer nada y usar ese conocimiento más adelante en la conversación
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

## Fundamentación con la Búsqueda de Google

Puedes habilitar la fundamentación con la Búsqueda de Google como parte de la configuración de la sesión. Esto aumenta la precisión de la API de Live y evita las alucinaciones. Consulta el [instructivo de fundamentación](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419) para
obtener más información.

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

## Combinación de varias herramientas

Puedes combinar varias herramientas dentro de la API de Live, lo que aumenta aún más las capacidades de tu aplicación:

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

## ¿Qué sigue?

- Consulta más ejemplos del uso de herramientas con la API de Live en el
  [libro de recetas de uso de herramientas](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=es-419).
- Obtén la historia completa sobre las funciones y configuraciones en la
  [guía de capacidades de la API de Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-01 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-01 (UTC)"],[],[]]
