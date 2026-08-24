---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=de
fetched_at: 2026-08-24T02:24:49.660538+00:00
title: "Agentische Vision-Funktionen \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Agentische Vision-Funktionen

Gemini Robotics ER-Modelle können Python-Code schreiben und ausführen, um Bilder zu bearbeiten und Logik anzuwenden, bevor sie antworten. Auf dieser Seite finden Sie Beispiele für die Code-Ausführung: Objekterkennung mit Zoom und Zuschneiden, Instrumentenablesung, Flüssigkeitsmessung, Lesen von Leiterplatten und Bildannotation.

Wenn Sie diese Beispiele an Ihren eigenen Anwendungsfall anpassen möchten, ersetzen Sie den Prompt-Text und die hochgeladene Bilddatei durch Ihre eigenen. Sie können auch das angeforderte JSON-Schema im Prompt an die Ausgabestruktur anpassen, die Ihre Anwendung benötigt, oder eine `system_instruction` hinzufügen, um das Ausgabeformat und die Genauigkeit zu erzwingen.

Vollständigen ausführbaren Code finden Sie im
[Robotics-Kochbuch](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Denkaufwand

Sie können den Denkaufwand steuern, um Latenz gegen Genauigkeit abzuwägen. Räumliche Aufgaben wie die Objekterkennung funktionieren gut mit einem niedrigen Denkaufwand. Komplexe Aufgaben wie das Zählen oder die Gewichtsschätzung profitieren von einem höheren Denkaufwand.

Im folgenden Beispiel wird der Denkaufwand für eine komplexe Zählaufgabe auf `high` gesetzt:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

Weitere Informationen finden Sie unter [Denkaufwand](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=de).

## Objekterkennung (Zoom und Zuschneiden)

Im folgenden Beispiel wird gezeigt, wie Sie die Codeausführung verwenden, um ein Bild zu zoomen und zuzuschneiden, um eine klarere Ansicht zu erhalten, wenn Sie Objekte erkennen und Begrenzungsrahmen zurückgeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Die Modellausgabe würde in etwa so aussehen:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

Das folgende Bild zeigt die vom Modell zurückgegebenen Rahmen.

![Beispiel für Begrenzungsrahmen für gefundene Objekte](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=de)

## Analoges Messgerät ablesen und Logik anwenden

Im folgenden Beispiel wird gezeigt, wie Sie das Modell verwenden, um ein analoges Messgerät abzulesen und Zeitberechnungen durchzuführen. Dabei wird eine Systemanweisung verwendet, um eine JSON-Ausgabe zu erzwingen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Flüssigkeit in einem Behälter messen

Im folgenden Beispiel wird gezeigt, wie Sie die Codeausführung verwenden, um den Flüssigkeitsstand in einem Behälter zu messen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Markierungen auf einer Leiterplatte lesen

Im folgenden Beispiel wird gezeigt, wie Sie die Codeausführung verwenden, um die Markierungen auf einer Leiterplatte zu lesen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![Beispiel für Markierungen auf einer Leiterplatte](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=de)

## Bildannotation

Im folgenden Beispiel wird gezeigt, wie Sie die Codeausführung verwenden, um ein Bild zu annotieren (z.B. Pfeile für Entsorgungsanweisungen zu zeichnen) und das geänderte Bild zurückzugeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Im Folgenden finden Sie ein Beispiel für eine Bildeingabe.

![Beispiel für eine Uhr zum Ablesen](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=de)

Die Modellausgabe würde in etwa so aussehen:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Nächste Schritte

- [Aufgabenorchestrierung](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de) – Aufgaben mit langer Laufzeit mit benutzerdefinierten Roboter-APIs.
- [Robotik mit Streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de) – bidirektionales Streaming in Echtzeit (nur Gemini Robotics ER 2).
- [Videoanalyse](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de) – Momente finden und Fortschritt klassifizieren (nur Gemini Robotics ER 2).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
