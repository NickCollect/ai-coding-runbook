---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de
fetched_at: 2026-08-24T02:34:39.716948+00:00
title: "Leitfaden zu den Live API-Funktionen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Leitfaden zu den Live API-Funktionen

Dieser umfassende Leitfaden behandelt die Funktionen und Konfigurationen, die mit der Live API verfügbar sind.
Auf der Seite [Erste Schritte mit der Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) finden Sie eine Übersicht und Beispielcode für gängige Anwendungsfälle.

## Hinweis

- **Mit den grundlegenden Konzepten vertraut machen**:Wenn Sie das noch nicht getan haben, lesen Sie zuerst die Seite [Erste Schritte mit der Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) .
  Hier erfahren Sie mehr über die grundlegenden Prinzipien der Live API, ihre Funktionsweise und die verschiedenen [Implementierungsansätze](https://ai.google.dev/gemini-api/docs/live?hl=de#implementation-approach).
- **Live API in AI Studio ausprobieren**:Es kann hilfreich sein, die Live API in [Google AI Studio](https://aistudio.google.com/app/live?hl=de) auszuprobieren, bevor Sie mit der Entwicklung beginnen. Wenn Sie die Live API in Google AI Studio verwenden möchten, wählen Sie **Stream** aus.

## Modellvergleich

In der folgenden Tabelle sind die wichtigsten Unterschiede zwischen den Modellen [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=de) und [Gemini 2.5 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=de) zusammengefasst:

| Funktion | Gemini 3.1 Flash Live Preview | Gemini 2.5 Flash Live Preview |
| --- | --- | --- |
| **[Antwort wird generiert](#native-audio-output-thinking)** | Verwendet `thinkingLevel`, um den Detailgrad des Denkprozesses mit Einstellungen wie `minimal`, `low`, `medium` und `high` zu steuern. Die Standardeinstellung ist `minimal`, um die Latenz zu minimieren. [Weitere Informationen zu Denkebenen und Budgets](https://ai.google.dev/gemini-api/docs/thinking?hl=de#levels-budgets) | Verwendet `thinkingBudget`, um die Anzahl der Tokens für den Thinking-Modus festzulegen. Die Funktion „Dynamisches Denken“ ist standardmäßig aktiviert. Setzen Sie `thinkingBudget` auf `0`, um die Funktion zu deaktivieren. [Weitere Informationen zu Denkebenen und Budgets](https://ai.google.dev/gemini-api/docs/thinking?hl=de#levels-budgets) |
| **[Antwort erhalten](https://ai.google.dev/api/live?hl=de#bidigeneratecontentservercontent)** | Ein einzelnes Serverereignis kann mehrere Inhaltsteile gleichzeitig enthalten, z. B. `inlineData` und ein Transkript. Achten Sie darauf, dass in Ihrem Code alle Teile jedes Ereignisses verarbeitet werden, damit keine Inhalte fehlen. | Jedes Serverereignis enthält nur einen Inhaltsteil. Teile werden in separaten Ereignissen bereitgestellt. |
| **[Kundeninhalte](#incremental-updates)** | `send_client_content` wird nur zum Erstellen des Verlaufs des ursprünglichen Kontexts unterstützt. Dazu muss `initial_history_in_client_content` in der Sitzungskonfiguration festgelegt werden. Wenn Sie während der Unterhaltung Textupdates senden möchten, verwenden Sie stattdessen `send_realtime_input`. | `send_client_content` wird während der gesamten Unterhaltung unterstützt, um inkrementelle Inhaltsaktualisierungen zu senden und Kontext zu schaffen. |
| **[Abdeckung für die Navigation](https://ai.google.dev/api/live?hl=de#turncoverage)** | Die Standardeinstellung ist `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. Der Zug des Modells umfasst erkannte Audioaktivitäten und alle Videoframes. | Die Standardeinstellung ist `TURN_INCLUDES_ONLY_ACTIVITY`. Der Zug des Modells umfasst nur die erkannte Aktivität. |
| **[Benutzerdefinierte VAD](#disable-automatic-vad)** (`activity_start`/`activity_end`) | Unterstützt. Deaktivieren Sie die automatische VAD und senden Sie `activityStart`- und `activityEnd`-Nachrichten manuell, um die Sprecherwechsel zu steuern. | Unterstützt. Deaktivieren Sie die automatische VAD und senden Sie `activityStart`- und `activityEnd`-Nachrichten manuell, um die Sprecherwechsel zu steuern. |
| **[Automatische VAD-Konfiguration](#configure-automatic-vad)** | Unterstützt. Konfigurieren Sie Parameter wie `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` und `silence_duration_ms`. | Unterstützt. Konfigurieren Sie Parameter wie `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` und `silence_duration_ms`. |
| **[Asynchrone Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/live-tools?hl=de#async-function-calling)** (`behavior: NON_BLOCKING`) | Nicht unterstützt. Funktionsaufrufe sind nur sequenziell möglich. Das Modell beginnt erst mit der Antwort, wenn Sie die Tool-Antwort gesendet haben. | Unterstützt. Legen Sie `behavior` für eine Funktionsdeklaration auf `NON_BLOCKING` fest, damit das Modell während der Ausführung der Funktion weiter interagieren kann. Mit dem Parameter `scheduling` (`INTERRUPT`, `WHEN_IDLE` oder `SILENT`) können Sie festlegen, wie das Modell Antworten verarbeitet. |
| **[Proaktive Audiofunktionen](#proactive-audio)** | Nicht unterstützt | Unterstützt. Wenn diese Option aktiviert ist, kann das Modell proaktiv entscheiden, nicht zu antworten, wenn die Eingabeinhalte nicht relevant sind. Legen Sie in der `proactivity`-Konfiguration `proactive_audio` auf `true` fest (erfordert `v1beta`). |
| **[Empathischer Dialog](#affective-dialog)** | Nicht unterstützt | Unterstützt. Das Modell passt seinen Antwortstil an die Ausdrucksweise und den Tonfall der Eingabe an. Legen Sie `enable_affective_dialog` in der Sitzungskonfiguration auf `true` fest (erfordert `v1beta`). |

Informationen zur Migration von Gemini 2.5 Flash Live zu Gemini 3.1 Flash Live finden Sie im [Migrationsleitfaden](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=de#migrating).

## Verbindung herstellen

Im folgenden Beispiel wird gezeigt, wie Sie eine Verbindung mit einem API-Schlüssel erstellen:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
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

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Interaktionsmodalitäten

In den folgenden Abschnitten finden Sie Beispiele und Kontext für die verschiedenen Eingabe- und Ausgabemodalitäten, die in der Live API verfügbar sind.

### Audio senden

Audio muss als rohe PCM-Daten gesendet werden (rohes 16-Bit-PCM-Audio, 16 kHz, Little Endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### Audioformate

Audiodaten in der Live API sind immer unkomprimiert, Little-Endian und 16-Bit-PCM. Die Audioausgabe erfolgt immer mit einer Abtastrate von 24 kHz. Die Eingabe-Audiodaten haben nativ eine Abtastrate von 16 kHz. Die Live API führt jedoch bei Bedarf ein Resampling durch, sodass jede Abtastrate gesendet werden kann. Um die Samplerate des eingegebenen Audiosignals anzugeben, legen Sie den MIME-Typ jedes [Blob](https://ai.google.dev/api/caching?hl=de#Blob), das Audio enthält, auf einen Wert wie `audio/pcm;rate=16000` fest.

### Audio empfangen

Die Audioantworten des Modells werden als Datenblöcke empfangen.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### SMS wird gesendet

Text kann mit `send_realtime_input` (Python) oder `sendRealtimeInput` (JavaScript) gesendet werden.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### Video wird gesendet

Videoframes werden als einzelne Bilder (z. B. JPEG oder PNG) mit einer bestimmten Framerate (max. 1 Frame pro Sekunde) gesendet.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### Inkrementelle Aktualisierungen von Inhalten

Verwenden Sie inkrementelle Updates, um Texteingaben zu senden, Sitzungskontext herzustellen oder wiederherzustellen. Bei kurzen Kontexten können Sie Turn-by-Turn-Interaktionen senden, um die genaue Abfolge der Ereignisse darzustellen:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

Bei längeren Kontexten empfiehlt es sich, eine Zusammenfassung der einzelnen Nachrichten bereitzustellen, um das Kontextfenster für nachfolgende Interaktionen freizugeben. Eine weitere Methode zum Laden des Sitzungskontexts finden Sie unter [Sitzungswiederaufnahme](https://ai.google.dev/gemini-api/docs/live-session?hl=de#session-resumption).

### Audiotranskripte

Zusätzlich zur Modellantwort können Sie auch Transkriptionen der Audioausgabe und der Audioeingabe erhalten.

Wenn Sie die Transkription der Audioausgabe des Modells aktivieren möchten, senden Sie `output_audio_transcription` in der Einrichtungskonfiguration. Die Sprache der Transkription wird aus der Antwort des Modells abgeleitet.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

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

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Wenn Sie die Transkription der Audioeingabe des Modells aktivieren möchten, senden Sie `input_audio_transcription` in der Einrichtungskonfiguration.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

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

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Stimme und Sprache ändern

[Modelle mit nativer Audioausgabe](#native-audio-output) unterstützen alle Stimmen, die für unsere [TTS-Modelle (Text-to-Speech)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#voices) verfügbar sind. Alle Stimmen sind in [AI Studio](https://aistudio.google.com/app/live?hl=de) verfügbar.

Wenn Sie eine Stimme angeben möchten, legen Sie den Namen der Stimme im `speechConfig`-Objekt als Teil der Sitzungskonfiguration fest:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Die Live API unterstützt [mehrere Sprachen](#supported-languages).
Bei Modellen mit [nativer Audioausgabe](#native-audio-output) wird die passende Sprache automatisch ausgewählt. Das explizite Festlegen des Sprachcodes wird nicht unterstützt.

## Native Audiofunktionen

Unsere neuesten Modelle bieten [native Audioausgabe](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=de), die für natürlich und realistisch klingende Sprache und eine verbesserte mehrsprachige Leistung sorgt.

### Thinking

Gemini 3.1-Modelle verwenden `thinkingLevel`, um die Tiefe der Überlegungen zu steuern. Dazu gibt es Einstellungen wie `minimal`, `low`, `medium` und `high`. Der Standardwert ist `minimal`, um die Latenz zu minimieren. Bei Gemini 2.5-Modellen wird stattdessen `thinkingBudget` verwendet, um die Anzahl der Tokens für den Thinking-Modus festzulegen. Weitere Informationen zu Ebenen und Budgets finden Sie unter [Ebenen und Budgets](https://ai.google.dev/gemini-api/docs/thinking?hl=de#levels-budgets).

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Außerdem können Sie Zusammenfassungen von Gedanken aktivieren, indem Sie in der Konfiguration `includeThoughts` auf `true` setzen. Weitere Informationen finden Sie unter [Zusammenfassungen von Gedanken](https://ai.google.dev/gemini-api/docs/thinking?hl=de#summaries):

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Empathischer Dialog

Mit dieser Funktion kann Gemini seinen Antwortstil an die Ausdrucksweise und den Tonfall der Eingabe anpassen.

Wenn Sie affektive Dialoge verwenden möchten, legen Sie die API-Version in der Einrichtungsnachricht auf `v1beta` und `enable_affective_dialog` auf `true` fest:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Proaktive Audioeingabe

Wenn diese Funktion aktiviert ist, kann Gemini proaktiv entscheiden, nicht zu antworten, wenn die Inhalte nicht relevant sind.

Wenn Sie die API verwenden möchten, legen Sie die API-Version auf `v1beta` fest, konfigurieren Sie das Feld `proactivity` in der Einrichtungsnachricht und legen Sie `proactive_audio` auf `true` fest:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Live-Übersetzung

Die Live API unterstützt die Übersetzung gesprochener Unterhaltungen in Echtzeit mit geringer Latenz. Damit können Sie Anwendungen für die Echtzeitübersetzung von Sprache in Sprache entwickeln.

Weitere Informationen und Beispiele finden Sie im [Leitfaden zur Live-Übersetzung](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=de).

## Erkennung von Sprachaktivität (Voice Activity Detection, VAD)

Mit der Spracherkennungsfunktion (Voice Activity Detection, VAD) kann das Modell erkennen, wann eine Person spricht. Das ist wichtig, um natürliche Unterhaltungen zu ermöglichen, da Nutzer das Modell jederzeit unterbrechen können.

Wenn VAD eine Unterbrechung erkennt, wird die laufende Generierung abgebrochen und verworfen. Im Sitzungsverlauf werden nur die Informationen gespeichert, die bereits an den Kunden gesendet wurden. Der Server sendet dann eine [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentservercontent)-Nachricht, um die Unterbrechung zu melden.

Der Gemini-Server verwirft dann alle ausstehenden Funktionsaufrufe und sendet eine `BidiGenerateContentServerContent`-Nachricht mit den IDs der abgebrochenen Aufrufe.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### Automatische VAD

Standardmäßig führt das Modell automatisch eine VAD für einen kontinuierlichen Audioeingabestream durch. VAD kann mit dem Feld [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=de#RealtimeInputConfig.AutomaticActivityDetection) der [Einrichtungskonfiguration](https://ai.google.dev/api/live?hl=de#BidiGenerateContentSetup) konfiguriert werden.

Wenn der Audiostream länger als eine Sekunde pausiert wird (z. B. weil der Nutzer das Mikrofon deaktiviert hat), sollte ein [`audioStreamEnd`](https://ai.google.dev/api/live?hl=de#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end)-Ereignis gesendet werden, um zwischengespeicherte Audiodaten zu leeren. Der Client kann das Senden von Audiodaten jederzeit fortsetzen.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

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

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Mit `send_realtime_input` reagiert die API automatisch auf Audio basierend auf VAD. Bei `send_client_content` werden Nachrichten in der richtigen Reihenfolge zum Modellkontext hinzugefügt, während `send_realtime_input` auf Reaktionsfähigkeit optimiert ist, was auf Kosten der deterministischen Reihenfolge geht.

### Automatische VAD-Konfiguration

Wenn Sie die VAD-Aktivität besser steuern möchten, können Sie die folgenden Parameter konfigurieren. Weitere Informationen finden Sie in der [API-Referenz](https://ai.google.dev/api/live?hl=de#automaticactivitydetection).

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### Automatische VAD deaktivieren

Alternativ kann die automatische VAD deaktiviert werden, indem Sie in der Einrichtungsnachricht `realtimeInputConfig.automaticActivityDetection.disabled` auf `true` setzen. In dieser Konfiguration ist der Client dafür verantwortlich, die Sprache des Nutzers zu erkennen und [`activityStart`](https://ai.google.dev/api/live?hl=de#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start)- und [`activityEnd`](https://ai.google.dev/api/live?hl=de#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end)-Nachrichten zum richtigen Zeitpunkt zu senden. In dieser Konfiguration wird kein `audioStreamEnd` gesendet. Stattdessen wird jede Unterbrechung des Streams durch eine `activityEnd`-Meldung gekennzeichnet.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### VAD-Parameter und ihre Auswirkungen auf die Qualität

Bei der automatischen VAD steuern zwei wichtige Parameter, wie Audio in Sprechabschnitte segmentiert wird, bevor es an das Modell gesendet wird:

- **`prefixPaddingMs`**: Die Menge an Audio, die *vor* der Erkennung von Sprache enthalten sein soll. Durch diesen „Rückblick“ wird sichergestellt, dass das Modell den vollständigen Beginn der Sprache erfasst, einschließlich der ersten Silbe, die möglicherweise vor dem Auslösen des VAD beginnt. Bei einem Wert von `0` werden möglicherweise die Anfänge von Wörtern abgeschnitten.
- **`silenceDurationMs`**: Wie lange der Server bei Stille wartet, bevor er einen Sprachabschnitt beendet. Damit wird festgelegt, wie tolerant das System gegenüber natürlichen Pausen mitten im Satz ist (z.B. zum Nachdenken, Atmen oder an Satzgrenzen).

#### Auswirkungen von `silenceDurationMs` auf die Audioqualität

Der Wert `silenceDurationMs` wirkt sich direkt auf die Größe und Vollständigkeit der Audio-Chunks aus, die das Modell zur Verarbeitung erhält:

- **Empfohlen (500–800 ms)**: Bietet ein gutes Gleichgewicht. Das Modell erhält vollständige, kontextreiche Audioblöcke, während die Latenz angemessen bleibt. Der interne Standardwert des Servers beträgt etwa 800 ms.
- **Zu niedrig (z.B. 100–200 ms)**: Das System beendet Sprechrunden während natürlicher Pausen und teilt eine einzelne Äußerung in mehrere kleine Audiofragmente auf. Das Modell empfängt diese Fragmente einzeln, wodurch der fragmentübergreifende Kontext verloren geht und die Qualität der Transkription und Antwort sinkt.
- **Zu hoch (z. B. 2.000 ms oder mehr)**: Das System wartet lange, nachdem der Nutzer aufgehört hat zu sprechen. Dadurch wird die wahrgenommene Latenz erhöht, bevor das Modell antwortet.

#### Best Practices für die manuelle (clientseitige) VAD

Wenn Sie die automatische VAD deaktivieren und `activityStart`/`activityEnd`-Signale über Ihre eigene clientseitige Spracherkennung verwalten, werden die integrierten Audio-Puffermechanismen des Servers umgangen. Das bedeutet:

1. **Kein Pre-Speech-Puffer**:Der Server fügt kein Audio mehr vor dem erkannten Sprachbeginn ein. Ihr Kunde sollte vor dem Senden von `activityStart` ausreichend Audio-Kontext bereitstellen.
2. **Keine Stille-Toleranz**:Der Server reagiert sofort auf Ihr `activityEnd`-Signal, ohne zusätzliche Wartezeit. Wenn Ihr clientseitiges VAD einen aggressiven End-of-Speech-Schwellenwert verwendet (z.B. 200 ms Stille), kann es sein, dass die Sprache während natürlicher Pausen mitten im Satz unterbrochen wird.

Damit die Audioqualität bei der manuellen VAD erhalten bleibt, sollten Sie in der Spracherkennung des Clients einen Stille-Grenzwert für das Ende der Sprache von mindestens **500 ms** verwenden.
Schwellenwerte unter diesem Wert führen häufig zu fragmentierten Audioinhalten, was die Qualität der Transkription und der Modellantworten beeinträchtigt.

## Tokenanzahl

Die Gesamtzahl der verbrauchten Tokens finden Sie im Feld [usageMetadata](https://ai.google.dev/api/live?hl=de#usagemetadata) der zurückgegebenen Servernachricht.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Auflösung von Medien

Sie können die Media-Auflösung für die Eingabemedien festlegen, indem Sie das Feld `mediaResolution` als Teil der Sitzungskonfiguration festlegen:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## Beschränkungen

Beachten Sie beim Planen Ihres Projekts die folgenden Einschränkungen der Live API.

### Antwortmodalitäten

Die nativen Audiomodelle unterstützen nur den Antworttyp „AUDIO“. Wenn Sie die Modellantwort als Text benötigen, verwenden Sie die Funktion [output audio transcription](#audio-transcription).

### Clientauthentifizierung

Die Live API bietet standardmäßig nur die Server-zu-Server-Authentifizierung. Wenn Sie Ihre Live API-Anwendung mit einem [Client-zu-Server-Ansatz](https://ai.google.dev/gemini-api/docs/live?hl=de#implementation-approach) implementieren, müssen Sie [ephemere Tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=de) verwenden, um Sicherheitsrisiken zu minimieren.

### Sitzungsdauer

Sitzungen mit nur Audio sind auf 15 Minuten begrenzt, Sitzungen mit Audio und Video auf 2 Minuten.
Sie können jedoch verschiedene [Methoden zur Sitzungsverwaltung](https://ai.google.dev/gemini-api/docs/live-session?hl=de) konfigurieren, um die Sitzungsdauer unbegrenzt zu verlängern.

### Kontextfenster

Eine Sitzung hat ein Kontextfensterlimit von:

- 128.000 Tokens für Modelle mit [nativer Audioausgabe](#native-audio-output)
- 32.000 Tokens für andere Live API-Modelle

## Unterstützte Sprachen

Die Live API unterstützt die folgenden 97 Sprachen.

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Afrikaans | `af` | Lettisch | `lv` |
| Akan | `ak` | Litauisch | `lt` |
| Albanisch | `sq` | Mazedonisch | `mk` |
| Amharisch | `am` | Malaiisch | `ms` |
| Arabisch | `ar` | Malayalam | `ml` |
| Armenisch | `hy` | Maltesisch | `mt` |
| Assamesisch | `as` | Maori | `mi` |
| Aserbaidschanisch | `az` | Marathi | `mr` |
| Baskisch | `eu` | Mongolisch | `mn` |
| Belarussisch | `be` | Nepalesisch | `ne` |
| Bengalisch | `bn` | Norwegisch | `no` |
| Bosnisch | `bs` | Oriya | `or` |
| Bulgarisch | `bg` | Oromo | `om` |
| Burmesisch | `my` | Paschtu | `ps` |
| Katalanisch | `ca` | Persisch | `fa` |
| Cebuano | `ceb` | Polnisch | `pl` |
| Chinesisch | `zh` | Portugiesisch | `pt` |
| Kroatisch | `hr` | Punjabi | `pa` |
| Tschechisch | `cs` | Quechua | `qu` |
| Dänisch | `da` | Rumänisch | `ro` |
| Niederländisch | `nl` | Rätoromanisch | `rm` |
| Englisch | `en` | Russisch | `ru` |
| Estnisch | `et` | Serbisch | `sr` |
| Färöisch | `fo` | Sindhi | `sd` |
| Filipino | `fil` | Singhalesisch | `si` |
| Finnisch | `fi` | Slowakisch | `sk` |
| Französisch | `fr` | Slowenisch | `sl` |
| Galizisch | `gl` | Somali | `so` |
| Georgisch | `ka` | Sesotho | `st` |
| Deutsch | `de` | Spanisch | `es` |
| Griechisch | `el` | Swahili | `sw` |
| Gujarati | `gu` | Schwedisch | `sv` |
| Hausa | `ha` | Tadschikisch | `tg` |
| Hebräisch | `iw` | Tamil | `ta` |
| Hindi | `hi` | Telugu | `te` |
| Ungarisch | `hu` | Thailändisch | `th` |
| Isländisch | `is` | Setswana | `tn` |
| Indonesisch | `id` | Türkisch | `tr` |
| Irisch | `ga` | Turkmenisch | `tk` |
| Italienisch | `it` | Ukrainisch | `uk` |
| Japanisch | `ja` | Urdu | `ur` |
| Kannada | `kn` | Usbekisch | `uz` |
| Kasachisch | `kk` | Vietnamesisch | `vi` |
| Khmer | `km` | Walisisch | `cy` |
| Kinyarwanda | `rw` | Westfriesisch | `fy` |
| Koreanisch | `ko` | Wolof | `wo` |
| Kurdisch | `ku` | Yoruba | `yo` |
| Kirgisisch | `ky` | Zulu | `zu` |
| Lao | `lo` |  |  |

## Nächste Schritte

- In den Anleitungen [Tool Use](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) (Tool-Nutzung) und [Session Management](https://ai.google.dev/gemini-api/docs/live-session?hl=de) (Sitzungsverwaltung) finden Sie wichtige Informationen zur effektiven Nutzung der Live API.
- Testen Sie die Live API in [Google AI Studio](https://aistudio.google.com/app/live?hl=de).
- Weitere Informationen zu den Live API-Modellen finden Sie auf der Seite „Modelle“ unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-native-audio).
- Weitere Beispiele finden Sie im [Live API-Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=de), im [Live API Tools-Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=de) und im [Live API-Script für die ersten Schritte](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-31 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-31 (UTC)."],[],[]]
