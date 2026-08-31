---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de
fetched_at: 2026-08-31T06:35:16.679337+00:00
title: "Videos verstehen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Videos verstehen

Gemini Robotics ER 2 kann den Aufgabenfortschritt anhand von kontinuierlichen Video-Feeds mit zwei Funktionen verfolgen:

- Momenterkennung: Ermittelt den genauen Zeitstempel, an dem ein Schlüsselereignis eintritt.
- Fortschrittsklassifizierung: Weist jedes Video einer von fünf Abschlusskategorien zu (0–20%, 20–40%, 40–60%, 60–80%, 80–100%).

## Momenterkennung

Bei der Momenterkennung wird der genaue Videoframe ermittelt, in dem ein kritisches Ereignis eintritt, z. B. wenn eine Tasse voll ist oder ein Knoten gebunden wird. Roboter verwenden diese Funktion, um den Erfolg zu überprüfen, Schritte zu sequenzieren und Korrekturen auszulösen.

Im folgenden Beispiel wird das Modell aufgefordert, den Zeitpunkt des Abschlusses einer bestimmten Aufgabe in einem Video zu ermitteln:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Das folgende Beispiel zeigt Frames aus einem Video zur Momenterkennung, wobei das Modell den Zeitstempel für den Abschluss der Aufgabe ermittelt:

![Beispiel für Videoframes mit der Ausgabe der Moment-Erkennung und einem Zeitstempel-Overlay](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=de)

## Fortschrittsklassifizierung

Bei der Fortschrittsklassifizierung wird ein Video einer von fünf Abschlusskategorien zugewiesen: 0–20%, 20–40%, 40–60%, 60–80 % oder 80–100%. So erhalten Roboter in Echtzeit Informationen zur jeweiligen Situation, damit sie Aktionen anpassen oder fehlgeschlagene Schritte wiederholen können, ohne einen gesamten Workflow neu starten zu müssen.

Im folgenden Beispiel wird das Modell aufgefordert, den aktuellen Fortschritt anhand eines Videos zu klassifizieren:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Das folgende Beispiel zeigt Frames aus einem Video zur Fortschrittsklassifizierung, wobei das Modell eine Fortschrittskategorie zuweist:

![Beispiel für Videoframes mit der Ausgabe der Fortschrittsklassifizierung und einem Label für die Fortschrittskategorie](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=de)

## Beispiele

Vollständige ausführbare Beispiele, einschließlich der Verfolgung von Aufgaben mit mehreren Schritten, finden Sie im
[Robotics-Kochbuch](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Nächste Schritte

- [Live API für Robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de) – bidirektionales Streaming in Echtzeit
- [Aufgabenorchestrierung](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de) – Aufgaben mit langer Laufzeit und räumlicher Argumentation
- [Übersicht über Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de) – Modellvergleich und Funktionen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
