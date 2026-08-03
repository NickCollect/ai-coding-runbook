---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de
fetched_at: 2026-08-03T04:38:06.596969+00:00
title: "Erste Schritte mit der Gemini Live API mit dem Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Erste Schritte mit der Gemini Live API mit dem Google GenAI SDK

Die Gemini Live API ermöglicht die bidirektionale Interaktion mit Gemini-Modellen in Echtzeit und unterstützt Audio-, Video- und Texteingaben sowie native Audioausgaben. In diesem Leitfaden wird erläutert, wie Sie die API mithilfe des Google GenAI SDK auf Ihrem Server einbinden.

[Live API in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?hl=de)
[Beispiel-App von GitHub klonencode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Coding-Agent-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de)

## Übersicht

Die Gemini Live API verwendet WebSockets für die Echtzeitkommunikation. Das `google-genai` SDK bietet eine asynchrone Schnittstelle auf hoher Ebene für die Verwaltung dieser Verbindungen.

Wichtige Konzepte:

- **Sitzung**: Eine persistente Verbindung zum Modell.
- **Konfiguration**: Einrichten von Modalitäten (Audio/Text), Stimme und Systemanweisungen.
- **Echtzeiteingabe**: Audio- und Videoframes werden als Blobs gesendet.

## Verbindung zur Live API herstellen

So starten Sie eine Live API-Sitzung mit einem API-Schlüssel:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

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

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
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

## SMS wird gesendet

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

## Audio senden

Audio muss als rohe PCM-Daten gesendet werden (rohes 16‑Bit-PCM-Audio, 16 kHz, Little Endian).

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

Ein Beispiel dafür, wie Sie die Audioausgabe vom Clientgerät (z.B. dem Browser) abrufen, finden Sie im End-to-End-Beispiel auf [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Video wird gesendet

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

Ein Beispiel dafür, wie Sie das Video vom Clientgerät (z.B. dem Browser) abrufen, finden Sie im End-to-End-Beispiel auf [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Audio empfangen

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

In der Beispiel-App auf GitHub erfahren Sie, wie Sie [Audio auf Ihrem Server empfangen](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) und [im Browser wiedergeben](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## SMS wird empfangen

Transkriptionen für Nutzereingaben und Modellausgaben sind im Serverinhalt verfügbar.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Toolaufrufe verarbeiten

Die API unterstützt Tool-Aufrufe (Funktionsaufrufe). Wenn das Modell einen Tool-Aufruf anfordert, müssen Sie die Funktion ausführen und die Antwort zurücksenden.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## Nächste Schritte

- Im vollständigen Leitfaden zu den [Funktionen der Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) findest du wichtige Funktionen und Konfigurationen, darunter die Spracherkennung und native Audiofunktionen.
- Im [Leitfaden zur Tool-Nutzung](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) erfahren Sie, wie Sie die Live API in Tools und Funktionsaufrufe einbinden.
- Im Leitfaden [Sitzungsverwaltung](https://ai.google.dev/gemini-api/docs/live-session?hl=de) finden Sie Informationen zum Verwalten von Unterhaltungen mit langer Ausführungszeit.
- Lesen Sie den Leitfaden zu [Einmal-Tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=de) für die sichere Authentifizierung in [Client-zu-Server](https://ai.google.dev/gemini-api/docs/live-api?hl=de#implementation-approach)-Anwendungen.
- Weitere Informationen zur zugrunde liegenden WebSockets API finden Sie in der [WebSockets API-Referenz](https://ai.google.dev/api/live?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-08 (UTC)."],[],[]]
