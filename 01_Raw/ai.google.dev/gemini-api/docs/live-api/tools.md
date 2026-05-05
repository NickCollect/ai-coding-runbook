---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=pl
fetched_at: 2026-05-05T13:28:19.357670+00:00
title: "Tool use with Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/live-api/Gemini Deep Research) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/gemini-api/docs/live-api/Strona główna)
- [Gemini API](https://ai.google.dev/gemini-api/docs/live-api/Gemini API)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/live-api/Dokumenty)

Prześlij opinię

# Tool use with Live API

Korzystanie z narzędzi pozwala interfejsowi Live API wyjść poza zwykłą rozmowę, umożliwiając mu wykonywanie działań w świecie rzeczywistym i pobieranie kontekstu zewnętrznego przy jednoczesnym utrzymaniu połączenia w czasie rzeczywistym.
Za pomocą interfejsu Live API możesz definiować narzędzia, takie jak [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/live-api/wywoływanie funkcji)
i [wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/live-api/wyszukiwarka Google).

## Omówienie obsługiwanych narzędzi

Oto krótkie omówienie narzędzi dostępnych w modelach interfejsu Live API:

| Narzędzie | Gemini 3.1 Flash Live (wersja testowa) | Gemini 2.5 Flash Live (wersja testowa) |
| --- | --- | --- |
| **Szukaj** | Obsługiwane | Obsługiwane |
| **Wywoływanie funkcji** | Obsługiwane (tylko synchroniczne) | Obsługiwane (synchroniczne i [asynchroniczne](https://ai.google.dev/gemini-api/docs/live-api/asynchroniczne)) |
| **Mapy Google** | Nieobsługiwane | Nieobsługiwane |
| **Wykonywanie kodu** | Nieobsługiwane | Nieobsługiwane |
| **Kontekst adresu URL** | Nieobsługiwane | Nieobsługiwane |

## Wywoływanie funkcji

Interfejs Live API obsługuje wywoływanie funkcji, podobnie jak zwykłe żądania generowania treści. Wywoływanie funkcji umożliwia interfejsowi Live API interakcję z danymi i programami zewnętrznymi, co znacznie zwiększa możliwości aplikacji.

Deklaracje funkcji możesz zdefiniować w ramach konfiguracji sesji.
Po otrzymaniu wywołań narzędzi klient powinien odpowiedzieć listą obiektów `FunctionResponse` za pomocą metody `session.send_tool_response`.

Więcej informacji znajdziesz w [samouczku dotyczącym wywoływania funkcji](https://ai.google.dev/gemini-api/docs/live-api/samouczku dotyczącym wywoływania funkcji).

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

Na podstawie jednego prompta model może wygenerować wiele wywołań funkcji i kod niezbędny do łączenia ich wyników. Ten kod jest wykonywany w środowisku piaskownicy, co powoduje generowanie kolejnych [BidiGenerateContentToolCall](https://ai.google.dev/gemini-api/docs/live-api/BidiGenerateContentToolCall).

## Asynchroniczne wywoływanie funkcji

Domyślnie wywoływanie funkcji odbywa się sekwencyjnie, co oznacza, że wykonywanie jest wstrzymywane do momentu, aż będą dostępne wyniki każdego wywołania funkcji. Zapewnia to sekwencyjne przetwarzanie, co oznacza, że nie będziesz mieć możliwości dalszej interakcji z modelem podczas wykonywania funkcji.

Jeśli nie chcesz blokować rozmowy, możesz poinformować model, aby uruchamiał funkcje asynchronicznie. Aby to zrobić, musisz najpierw dodać `behavior` do definicji funkcji:

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

`NON-BLOCKING` zapewnia, że funkcja będzie działać asynchronicznie, a Ty będziesz mieć możliwość dalszej interakcji z modelem.

Następnie musisz poinformować model, jak ma się zachowywać, gdy otrzyma `FunctionResponse`, za pomocą parametru `scheduling`. Może on:

- przerwać wykonywanie bieżącego zadania i od razu poinformować Cię o otrzymanej odpowiedzi
  (`scheduling="INTERRUPT"`),
- poczekać, aż skończy wykonywać bieżące zadanie
  (`scheduling="WHEN_IDLE"`),
- lub nic nie robić i wykorzystać tę wiedzę później w dyskusji
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

## Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google

W ramach konfiguracji sesji możesz włączyć powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google. Zwiększa to dokładność interfejsu Live API i zapobiega halucynacjom. Więcej informacji znajdziesz w [samouczku dotyczącym powiązania ze źródłem informacji](https://ai.google.dev/gemini-api/docs/live-api/samouczku dotyczącym powiązania ze źródłem informacji).

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

## Łączenie wielu narzędzi

W ramach interfejsu Live API możesz łączyć wiele narzędzi, co jeszcze bardziej zwiększa możliwości aplikacji:

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

## Co dalej?

- Więcej przykładów używania narzędzi z interfejsem Live API znajdziesz w
  [przewodniku Tool use cookbook](https://ai.google.dev/gemini-api/docs/live-api/przewodniku Tool use cookbook).
- Więcej informacji o funkcjach i konfiguracjach znajdziesz w
  [przewodniku Live API Capabilities guide](https://ai.google.dev/gemini-api/docs/live-api/przewodniku Live API Capabilities guide).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://ai.google.dev/gemini-api/docs/live-api/licencją Creative Commons – uznanie autorstwa 4.0), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://ai.google.dev/gemini-api/docs/live-api/licencji Apache 2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://ai.google.dev/gemini-api/docs/live-api/zasady dotyczące witryny Google Developers). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-01 UTC.

Chcesz przekazać coś jeszcze?
