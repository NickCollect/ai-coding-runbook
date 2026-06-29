---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=de
fetched_at: 2026-06-29T05:40:03.139846+00:00
title: "Sitzungsverwaltung mit der Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Sitzungsverwaltung mit der Live API

In der Live API bezieht sich eine Sitzung auf eine dauerhafte Verbindung, über die Ein- und Ausgaben kontinuierlich über dieselbe Verbindung gestreamt werden. [Weitere Informationen](https://ai.google.dev/gemini-api/docs/live?hl=de)
Dieses einzigartige Sitzungsdesign ermöglicht eine geringe Latenz und unterstützt einzigartige Funktionen, kann aber auch zu Problemen wie Sitzungszeitlimits und vorzeitiger Beendigung führen.
In dieser Anleitung werden Strategien zur Bewältigung der Herausforderungen bei der Sitzungsverwaltung beschrieben, die bei der Verwendung der Live API auftreten können.

## Sitzungsdauer

Ohne Komprimierung sind reine Audio-Sitzungen auf 15 Minuten und Audio-Video-Sitzungen auf 2 Minuten begrenzt. Wenn Sie diese Limits überschreiten, wird die Sitzung (und damit die Verbindung) beendet. Sie können jedoch die [Kontextfensterkomprimierung](#context-window-compression) verwenden, um Sitzungen unbegrenzt zu verlängern.

Die Lebensdauer einer Verbindung ist ebenfalls auf etwa 10 Minuten begrenzt. Wenn die Verbindung beendet wird, wird auch die Sitzung beendet. In diesem Fall können Sie eine einzelne Sitzung so konfigurieren, dass sie über mehrere Verbindungen hinweg aktiv bleibt. Verwenden Sie dazu die [Sitzungswiederaufnahme](#session-resumption).
Sie erhalten außerdem eine [GoAway-Nachricht](#goaway-message), bevor die Verbindung beendet wird. So können Sie weitere Maßnahmen ergreifen.

## Komprimierung des Kontextfensters

Wenn Sie längere Sitzungen ermöglichen und ein abruptes Beenden der Verbindung vermeiden möchten, können Sie die Kontextfensterkomprimierung aktivieren, indem Sie das Feld [contextWindowCompression](https://ai.google.dev/api/live?hl=de#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) als Teil der Sitzungskonfiguration festlegen.

In der [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=de#contextwindowcompressionconfig) können Sie einen [Sliding-Window-Mechanismus](https://ai.google.dev/api/live?hl=de#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window) und die [Anzahl der Tokens](https://ai.google.dev/api/live?hl=de#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens) konfigurieren, die die Komprimierung auslösen.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Sitzungswiederaufnahme

Um zu verhindern, dass die Sitzung beendet wird, wenn der Server die WebSocket-Verbindung regelmäßig zurücksetzt, konfigurieren Sie das Feld [sessionResumption](https://ai.google.dev/api/live?hl=de#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) in der [Einrichtungskonfiguration](https://ai.google.dev/api/live?hl=de#BidiGenerateContentSetup).

Wenn diese Konfiguration übergeben wird, sendet der Server [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=de#SessionResumptionUpdate)-Nachrichten, die verwendet werden können, um die Sitzung fortzusetzen. Dazu muss das letzte Fortsetzungstoken als [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=de#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) der nachfolgenden Verbindung übergeben werden.

Fortsetzungstokens sind nach dem Beenden der letzten Sitzung 2 Stunden lang gültig.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

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

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
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
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Eine Nachricht erhalten, bevor die Verbindung zur Sitzung getrennt wird

Der Server sendet eine [GoAway](https://ai.google.dev/api/live?hl=de#GoAway)-Nachricht, die signalisiert, dass die aktuelle Verbindung bald beendet wird. Diese Nachricht enthält die [timeLeft](https://ai.google.dev/api/live?hl=de#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left), die die verbleibende Zeit angibt. So können Sie weitere Maßnahmen ergreifen, bevor die Verbindung als „ABORTED“ beendet wird.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Benachrichtigung erhalten, wenn die Generierung abgeschlossen ist

Der Server sendet eine [generationComplete](https://ai.google.dev/api/live?hl=de#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)-Nachricht, die signalisiert, dass das Modell die Antwort generiert hat.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## Nächste Schritte

Weitere Informationen zur Verwendung der Live API finden Sie im vollständigen [Leitfaden zu den Funktionen](https://ai.google.dev/gemini-api/docs/live?hl=de), auf der Seite [Tool-Verwendung](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) oder im [Live API-Kochbuch](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
