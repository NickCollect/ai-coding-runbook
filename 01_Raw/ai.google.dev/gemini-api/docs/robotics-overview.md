---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de
fetched_at: 2026-09-14T05:42:45.068127+00:00
title: "Gemini Robotics\u00a0ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini Robotics ER

Gemini Robotics ER-Modelle (Embodied Reasoning) sind Vision-Language-Modelle (VLMs), mit denen Roboter die physische Welt wahrnehmen und mit ihr interagieren können. Sie interpretieren visuelle Daten, führen räumliche und zeitliche Schlussfolgerungen durch, planen mehrstufige Aufgaben und koordinieren Roboter und Tools.

## Modelle

Das Gemini Robotics ER 2-Modell ist das neueste Modell von Gemini Robotics.
Es ist unser aktualisiertes Logikmodell, das es Robotern ermöglicht, ihre Umgebung genau zu erfassen. Es ist auf Funktionen für verkörpertes Denken spezialisiert, z. B. die Orchestrierung von Robotern durch Agenten (z. B. mit VLAs), das Verständnis von Robotervideos, einschließlich des Fortschritts und der Erkennung von Erfolgen, das Lesen von Instrumenten, das Zeigen und das räumliche Denken.

Das Gemini Robotics ER2-Modell bietet zwei Modellendpunkte:

- **`gemini-robotics-er-2-preview`**: Das Standardmodell für erweiterte Reichweite 2. Basiert auf Gemini 3.5 Flash und bietet verbessertes räumliches Denken, das Auffinden von Videomomenten, die Klassifizierung des Videofortschritts, die Orchestrierung mehrerer Roboter und die Nutzung von Tools in mehreren Schritten.
- **`gemini-robotics-er-2-streaming-preview`**: Optimiert für Echtzeit-Streaming über die [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de). Verwenden Sie dieses Modell für Roboter-Agents mit niedriger Latenz, die kontinuierliche Audio- und Videoeingaben verarbeiten.

Wenn Sie Gemini Robotics ER 1.6 verwenden, führen Sie ein Upgrade auf Gemini Robotics ER 2 durch, indem Sie in Ihren API-Aufrufen `model="gemini-robotics-er-1.6-preview"` durch `model="gemini-robotics-er-2-preview"` oder `model="gemini-robotics-er-2-streaming-preview"` ersetzen. Das Modell Gemini Robotics ER 1.6 wird [Ende August](https://ai.google.dev/gemini-api/docs/deprecations?hl=de#robotics-models) eingestellt.

[Gemini Robotics ER 2 in Google AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=de)

## Robotikfunktionen

Gemini Robotics ER unterstützt eine Reihe von Funktionen für verkörpertes Denken.
Wählen Sie eine Funktion aus, um mehr zu erfahren:

| Funktion | Beschreibung | Leitfaden |
| --- | --- | --- |
| Räumliches Denken | Auf Objekte zeigen, sie in Videos verfolgen, mit Begrenzungsrahmen erkennen und Trajektorien planen. | [Räumliches Denken](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=de) |
| Agentic Vision | Code-Ausführung nutzen, um andere Funktionen mithilfe von Bildbearbeitungstools zu optimieren | [Agentic Vision](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=de) |
| Aufgabenorchestrierung | Kombinieren Sie räumliches Denken mit benutzerdefinierten Roboter-APIs, um Aufgaben mit langer Zeitspanne zu erledigen. | [Aufgaben-Orchestrierung](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de) |
| Streaming (nur Gemini Robotics ER 2-Streamingendpunkt) | Bidirektionales Streaming für Echtzeit-Roboter-Agents mit Funktionsaufrufen mit niedriger Latenz. | [Streaming für Robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de) |
| Videofortschritt (nur Gemini Robotics ER 2) | Momentsuche und Fortschrittsklassifizierung aus kontinuierlichen Videofeeds. | [Video-Understanding](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de) |

## Erste Schritte

Im folgenden Beispiel werden Objekte in einem Bild gesucht und ihre normalisierten 2D-Koordinaten und Labels zurückgegeben. Sie können diese Ausgabe direkt an eine Robotics API oder ein VLA-Modell übergeben, um Roboteraktionen zu generieren.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

Die Ausgabe ist ein JSON-Array mit Objekten, die jeweils ein `point` (normalisierte `[y, x]`-Koordinaten) und ein `label` zur Identifizierung des Objekts enthalten.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Das folgende Bild zeigt ein Beispiel dafür, wie diese Punkte dargestellt werden können:

![Beispiel für die Darstellung der Punkte von Objekten in einem Bild](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=de)

## Funktionsweise

Gemini Robotics ER verarbeitet Bild-, Video- oder Audioeingaben mit Prompts in natürlicher Sprache. Es werden Objekte identifiziert, der Szenenkontext und räumliche Beziehungen werden analysiert und strukturierte Ausgaben wie Koordinaten oder Begrenzungsrahmen werden zurückgegeben.

Gemini Robotics ER ist auch agentisch: Es zerlegt komplexe Aufgaben in Teilaufgaben und führt sie aus, indem es Ihre Roboterfunktionen aufruft oder generierten Code ausführt. Beispiel: „Lege den Apfel in die Schüssel“ wird zu einer Folge von Schritten zum Lokalisieren, Greifen und Platzieren.

Weitere Informationen dazu, wie Gemini Tool-Aufrufe ausführt, finden Sie unter [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=de#how-it-works).

## Sicherheit

Gemini Robotics ER wurde zwar mit Blick auf die Sicherheit entwickelt, es liegt jedoch in Ihrer Verantwortung, für eine sichere Umgebung rund um den Roboter zu sorgen. Generative KI-Modelle können Fehler machen und physische Roboter können Schäden verursachen. Weitere Informationen finden Sie auf der [Google DeepMind-Seite zur Robotersicherheit](https://deepmind.google/models/gemini-robotics/safety?hl=de).

## Best Practices

1. Verwenden Sie eine einfache, natürliche Sprache. Beschreiben Sie, was der Roboter tun soll, so, als würden Sie mit einer Person sprechen. Wenn ein Begriff nicht funktioniert, versuchen Sie es mit einem gängigen Synonym.
2. Visuelle Eingabe optimieren Schneiden Sie kleine oder unklare Objekte zu oder zoomen Sie sie heran, bevor Sie das Bild senden. Die Beleuchtung und ein geringer Farbkontrast können sich auf die Erkennung auswirken.
3. Teilen Sie komplexe Aufgaben in Schritte auf. Senden Sie jeden Schritt als separaten Prompt, damit das Modell fokussiert bleibt und die Genauigkeit verbessert wird.
4. Führen Sie die Abfrage mehrmals aus und bilden Sie den Durchschnitt der Ergebnisse für Aufgaben, die eine hohe Präzision erfordern. Dieser Konsensansatz reduziert die Varianz bei räumlichen Ausgaben.

## Beschränkungen

Beachten Sie beim Entwickeln mit Gemini Robotics ER die folgenden Einschränkungen:

- **Einschränkungen für API-Schlüssel**:Die Gemini API akzeptiert keine Anfragen von uneingeschränkten API-Schlüsseln und gibt einen `403 Forbidden`-Fehler zurück. Sichern Sie Ihren API-Schlüssel, indem Sie in [AI Studio](https://aistudio.google.com/api-keys?hl=de) Einschränkungen hinzufügen.
  Weitere Informationen finden Sie unter [Uneingeschränkte API-Schlüssel sichern](https://ai.google.dev/gemini-api/docs/api-key?hl=de#secure-unrestricted-keys).
- **Latenz im Vergleich zur Leistung**:Komplexe Anfragen, Eingaben mit hoher Auflösung oder ein hohes Maß an Denkleistung können zu längeren Verarbeitungszeiten führen. Verwenden Sie für die Denkebene „Mittel“, um ein gutes Gleichgewicht zwischen Latenz und Leistung zu erzielen.
- **Halluzinationen**:Wie alle Large Language Models können Gemini Robotics ER-Modelle gelegentlich „halluzinieren“ oder falsche Informationen liefern, insbesondere bei mehrdeutigen Prompts oder Out-of-Distribution-Eingaben.
- **Abhängigkeit von der Promptqualität**:Die Qualität der Ausgabe hängt von der Klarheit des Eingabe-Prompts ab. Verwenden Sie spezifische, gut strukturierte Prompts.
- **Rechenkosten**:Die Ausführung des Modells, insbesondere mit Videoeingaben oder hohem `thinking_budget`, verbraucht Rechenressourcen und verursacht Kosten.
  Weitere Informationen finden Sie auf der Seite [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=de).
- **Eingabetypen**:In den folgenden Abschnitten finden Sie Details zu den Einschränkungen für die einzelnen Modi.
  - [Bildeingaben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#technical-details-image)
  - [Videoeingänge](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#supported-formats)
  - [Audioeingänge](https://ai.google.dev/gemini-api/docs/audio?hl=de#supported-formats)

## Datenschutzhinweise

Sie bestätigen, dass die in diesem Dokument genannten Modelle (die „Robotikmodelle“) Video- und Audiodaten verwenden, um Ihre Hardware gemäß Ihren Anweisungen zu betreiben und zu bewegen. Sie dürfen die Robotikmodelle daher so betreiben, dass Daten von identifizierbaren Personen, z. B. Sprach-, Bild- und Ähnlichkeitsdaten („personenbezogene Daten“), von den Robotikmodellen erhoben werden. Wenn Sie die Robotikmodelle so betreiben, dass personenbezogene Daten erhoben werden, stimmen Sie zu, dass Sie keine identifizierbaren Personen mit den Robotikmodellen interagieren lassen oder sich in der Umgebung der Robotikmodelle aufhalten lassen, es sei denn, diese identifizierbaren Personen wurden ausreichend darüber informiert und haben zugestimmt, dass ihre personenbezogenen Daten an Google weitergegeben und von Google verwendet werden dürfen, wie in den zusätzlichen Nutzungsbedingungen für Gemini API unter [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=de) (den „Nutzungsbedingungen“) beschrieben, einschließlich gemäß dem Abschnitt „Wie Google Ihre Daten verwendet“. Sie sorgen dafür, dass diese Mitteilung die Erhebung und Nutzung personenbezogener Daten gemäß den Nutzungsbedingungen erlaubt, und unternehmen in wirtschaftlich angemessener Weise Anstrengungen, um die Erhebung und Weitergabe personenbezogener Daten zu minimieren, indem Sie Techniken wie das Unkenntlichmachen von Gesichtern verwenden und die Robotikmodelle nach Möglichkeit in Bereichen betreiben, in denen sich keine identifizierbaren Personen aufhalten.

## Preise

Detaillierte Informationen zu Preisen und verfügbaren Regionen finden Sie auf der Seite [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Modellendpunkte

### Gemini Robotics ER 2 (Vorabversion)

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | `gemini-robotics-er-2-preview` |
| saveUnterstützte Datentypen | **Eingaben**  Text, Bilder, Video, Audio  **Ausgabe**  Text |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  131.072  **Tokenausgabelimit**  65.536 |
| handymanFunktionen | **[Audiogenerierung](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)**  Nicht unterstützt  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de)**  Unterstützt  **[Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de)**  Unterstützt  **[Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)**  Unterstützt  **[Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)**  Unterstützt  **[Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)**  Unterstützt  **[Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)**  Unterstützt  **[Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)**  Nicht unterstützt  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)**  Nicht unterstützt  **[Suchfundierung](https://ai.google.dev/gemini-api/docs/google-search?hl=de)**  Unterstützt  **[Strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de)**  Unterstützt  **[Antwort wird generiert](https://ai.google.dev/gemini-api/docs/thinking?hl=de)**  Unterstützt  **[URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)**  Unterstützt |
| speedNutzungsoptionen | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)**  Unterstützt  **[Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de)**  Nicht unterstützt  **[Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de)**  Nicht unterstützt |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Vorschau für: `gemini-robotics-er-2-preview` |
| calendar\_monthLetzte Aktualisierung | Juli 2026 |
| id\_cardModellkarte | [Modellkarte](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=de) |

### Gemini Robotics ER 2 – Streaming-Vorabversion

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | `gemini-robotics-er-2-streaming-preview` |
| saveUnterstützte Datentypen | **Eingaben**  Text, Bilder, Video, Audio  **Ausgabe**  Text |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  131.072  **Tokenausgabelimit**  65.536 |
| handymanFunktionen | **[Audiogenerierung](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)**  Nicht unterstützt  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de)**  Nicht unterstützt  **[Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de)**  Nicht unterstützt  **[Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)**  Nicht unterstützt  **[Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)**  Nicht unterstützt  **[Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)**  Unterstützt  **[Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)**  Nicht unterstützt  **[Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)**  Nicht unterstützt  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)**  Unterstützt  **[Suchfundierung](https://ai.google.dev/gemini-api/docs/google-search?hl=de)**  Unterstützt  **[Strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de)**  Nicht unterstützt  **[Antwort wird generiert](https://ai.google.dev/gemini-api/docs/thinking?hl=de)**  Unterstützt  **[URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)**  Nicht unterstützt |
| speedNutzungsoptionen | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)**  Nicht unterstützt  **[Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de)**  Nicht unterstützt  **[Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de)**  Nicht unterstützt |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Vorschau für: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthLetzte Aktualisierung | Juli 2026 |
| id\_cardModellkarte | [Modellkarte](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=de) |

### Gemini Robotics ER 1.6 (Vorabversion)

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | `gemini-robotics-er-1.6-preview` |
| saveUnterstützte Datentypen | **Eingaben**  Text, Bilder, Video, Audio  **Ausgabe**  Text |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  131.072  **Tokenausgabelimit**  65.536 |
| handymanFunktionen | **[Audiogenerierung](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)**  Nicht unterstützt  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de)**  Unterstützt  **[Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de)**  Unterstützt  **[Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)**  Unterstützt  **[Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)**  Unterstützt  **[Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)**  Unterstützt  **[Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)**  Unterstützt  **[Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)**  Nicht unterstützt  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)**  Nicht unterstützt  **[Suchfundierung](https://ai.google.dev/gemini-api/docs/google-search?hl=de)**  Unterstützt  **[Strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de)**  Unterstützt  **[Antwort wird generiert](https://ai.google.dev/gemini-api/docs/thinking?hl=de)**  Unterstützt  **[URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)**  Unterstützt |
| speedNutzungsoptionen | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)**  Unterstützt  **[Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de)**  Nicht unterstützt  **[Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de)**  Nicht unterstützt |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Vorschau für: `gemini-robotics-er-1.6-preview` |
| calendar\_monthLetzte Aktualisierung | Dezember 2025 |
| cognition\_2Wissensstichtag | Januar 2025 |

## Nächste Schritte

- [Räumliches Denken](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=de): Zeigen, Tracking, Begrenzungsrahmen, Trajektorien.
- [Agentische Funktionen](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=de): Code-Ausführung, Instrumentenablesung, Bildanmerkungen.
- [Aufgabenorchestration](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de): Aufgaben mit langer Zeitspanne mit benutzerdefinierten Roboter-APIs.
- [Robotik mit Streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de): bidirektionales Streaming in Echtzeit (nur Gemini Robotics ER 2).
- [Videoanalyse](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de): Suche nach Momenten und Fortschrittsklassifizierung (nur Gemini Robotics ER 2).
- [Google DeepMind Robotics Safety](https://deepmind.google/models/gemini-robotics/safety?hl=de) – Sicherheitsforschung hinter der Modellfamilie.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-08 (UTC)."],[],[]]
