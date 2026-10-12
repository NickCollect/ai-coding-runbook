---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de
fetched_at: 2026-10-12T07:06:59.012026+00:00
title: "Robotik mit Streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Robotik mit Streaming

Der Modellendpunkt `gemini-robotics-er-2-streaming-preview` stellt einen dedizierten Streaming-Endpunkt bereit, der in die [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de) eingebunden ist und eine bidirektionale Echtzeitinteraktion zwischen Ihrer Anwendung und dem Roboter ermöglicht. Daher eignet es sich für Agents, die schnelle Feedbackschleifen und reaktive Antworten auf die Umgebung benötigen.

[In Google AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=de)
[Beispiel-Apps von GitHub klonen](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Anwendungsfälle

- **Koordination mehrerer Roboter**: Mehrere Roboter, die den Aufgabenstatus über eine gemeinsame Sitzung kommunizieren und Unteraufgaben delegieren.
- **Kontinuierliches Monitoring**: Roboter, die eine Szene beobachten und Aktionen auslösen, wenn bestimmte Ereignisse eintreten, z. B. wenn ein Container einen bestimmten Füllstand erreicht.
- **Lager und Logistik**: Kommissionierungs- und Verpackungs-Agents, die Artikel visuell prüfen, den Verpackungsfortschritt verfolgen und Fehler beheben.

## Technische Spezifikationen

In der folgenden Tabelle sind die technischen Spezifikationen für die Live API aufgeführt:

| Kategorie | Details |
| --- | --- |
| Eingabemodalitäten | Audio (rohes 16-Bit-PCM-Audio, 16 kHz, Little Endian), Bilder (JPEG <= 1 FPS), Text |
| Ausgabemodalitäten | Text |
| Protokoll | Statusbehaftete WebSocket-Verbindung (WSS) |

## Agentische Einrichtung erstellen

Jeder auf der Live API basierende Roboter-Agent durchläuft drei Schritte:

1. **Roboterfunktionen als Tools deklarieren**: Jede Aktion, die der Roboter ausführen kann (z. B. navigieren, greifen, sprechen), wird zu einer Funktionsdeklaration mit einem Namen, einer Beschreibung und einem Parameterschema. Bei physischen Aktionen muss `"behavior": "BLOCKING"` verwendet werden, damit das Modell wartet, bis der Roboter fertig ist, bevor es den nächsten Schritt auswählt.
2. **Multimodale Eingabe in eine persistente Sitzung streamen** Öffnen Sie eine `live.connect`-Sitzung und lassen Sie sie für die gesamte Dauer der Aufgabe geöffnet. Senden von Videobildern, Audio oder Text, sobald sie von den Sensoren des Roboters empfangen werden.
3. **Toolaufrufe in einer Empfangsschleife verarbeiten**: Jedes Mal, wenn das Modell eine Aktion auswählt, wird eine `tool_call`-Nachricht gesendet. In der Empfangsschleife wird die Funktion für Ihr Roboter-SDK ausgeführt und eine `tool_response` zurückgesendet. Die Sitzung bleibt geöffnet und das Modell wählt die nächste Aktion basierend auf dem Ergebnis aus.

In den folgenden Abschnitten wird gezeigt, wie Sie diese Schritte auf drei gängige Muster anwenden: einen Baseline-Agent-Loop, die proaktive Szenenüberwachung mit einem Heartbeat und das Weiterleiten von Sprache über TTS als Tool.

## Roboter über Funktionsaufrufe steuern

Im folgenden Beispiel sind alle drei Schritte in einem einzigen Python-Skript miteinander verbunden.

Schritt 1 – Tooldefinitionen – deklariert Roboterfunktionen als Funktionsdeklarationen. Die Funktion `navigate` verwendet `"behavior": "BLOCKING"`, sodass das Modell wartet, bis der Roboter den Wegpunkt erreicht hat, bevor ein anderes Tool aufgerufen wird.
Fügen Sie der Liste weitere Funktionsdeklarationen hinzu, um zusätzliche Roboterfunktionen verfügbar zu machen.

Schritt 2 – Eingabehilfen – zeigt drei Funktionen, mit denen verschiedene Modalitätseingaben in die Sitzung gestreamt werden: `send_text` für Befehle, `send_image` für Kamerabilder mit einem optionalen Text-Prompt und `send_audio` für rohes PCM-Audio von einem Mikrofon.

Schritt 3 – die Empfangsschleife – wird gleichzeitig ausgeführt und verarbeitet zwei Arten von Nachrichten: `server_content`-Nachrichten (die Textausgabe des Modells) und `tool_call`-Nachrichten (das Modell fordert eine Roboteraktion an). Wenn ein Tool-Aufruf eingeht, ruft die Schleife `execute_tool` auf – einen Stub, den Sie durch Ihr echtes Roboter-SDK ersetzen – und sendet dann `tool_response` zurück, damit das Modell die nächste Aktion auswählen kann.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

Der Empfangsvorgang bleibt nach jeder Tool-Antwort aktiv. Das Modell erstellt und überarbeitet einen Plan mit langem Horizont, ohne dass Sie die gesamte Aktionssequenz im Voraus codieren müssen.

## Proaktives räumlich-zeitliches Denken

Die Live API streamt Videoinhalte, aber Videoframes allein lösen keinen neuen Reasoning-Turn aus. Videoframes müssen von einem Text- oder Audio-Prompt begleitet werden, um eine Modellantwort auszulösen. Weitere Informationen finden Sie unter [Live API-Funktionen](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de).

Um proaktives Reasoning zu aktivieren, implementieren Sie einen **Heartbeat**: Senden Sie regelmäßig den letzten Kamerabild gefolgt von einem kurzen Text-Prompt, der das Modell dazu zwingt, die Szene zu untersuchen und eine explizite Entscheidung zu treffen. Die Videoeingabe ist auf ein Bild pro Sekunde begrenzt.

### Heartbeat implementieren

Die Heartbeat-Coroutine wird als separate `asyncio`-Aufgabe in derselben Sitzung ausgeführt.
Es wird opportunistisch auf eine Häufigkeit von 1 Hz ausgerichtet (entsprechend dem Ratenlimit für die Videoeingabe), während auf den Abschluss jeder Runde (`er_turn_done`) gewartet wird, um laufende Schlussfolgerungen nicht zu unterbrechen:

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### Empfangsschleife aktualisieren

Um zu signalisieren, wann das Modell seinen Zug beendet hat, aktualisieren Sie `receive_loop`, um `er_turn_done` festzulegen:

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## Audioausgabe über externe TTS

Gemini Robotics ER 2 gibt Text zurück. Ihre Anwendung leitet vollständige Antworten über einen eingefügten Callback an einen separaten TTS-Anbieter (z. B. [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)) weiter.
So behalten Sie die Kontrolle über die Sprachlatenz, die Auswahl der Stimme und das Unterbrechungsverhalten und können TTS-Back-Ends austauschen, ohne die Agentenlogik zu ändern.

Sie können die Sprachausgabe auch als Tool deklarieren, damit das Modell „Sag etwas“ genauso behandelt wie „Bewege den Arm“. Fügen Sie der Liste `tools` aus dem ersten Abschnitt die folgende Funktionsdeklaration hinzu:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

Durch das Einbetten von TTS in eine Funktionsdeklaration verarbeitet das Modell Sprache über denselben Tool-Aufruf-Pfad wie jede andere Roboteraktion. Ihre Anwendung führt den Aufruf mit einem eingefügten Callback aus.

## Beispiele auf GitHub

Vollständig funktionierende Beispiele, darunter die Spot-Roboter-Demo zum Holen von Snacks und die Tinybot-Schwenk-/Neige-Demo „Hello World“, finden Sie unter [Robotics Live API-Beispiele](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## Nächste Schritte

- [Videoanalyse](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de): Momente finden und Fortschritt klassifizieren.
- [Aufgabenorchestrierung](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de): Aufgaben mit langem Horizont ohne Streaming.
- [Live API – Übersicht](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de): Vollständige API-Dokumentation zur Live API.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-16 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-16 (UTC)."],[],[]]
