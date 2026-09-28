---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=de
fetched_at: 2026-09-28T06:27:58.834709+00:00
title: "Gemini Robotics\u00a0ER\u00a02-Streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini Robotics ER 2-Streaming

Gemini Robotics ER 2 Streaming ist ein Vision-Language-Modell (VLM) für Robotik, das für das Echtzeit-Textstreaming mit der Live API optimiert ist. Sie akzeptiert Text-, Bild-, Video- und Audioeingaben und unterstützt bidirektionales Streaming mit Funktionsaufrufen.

[In Google AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=de)

## Dokumentation

Auf der Seite [Live API for robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de) finden Sie eine vollständige Übersicht über die Funktionen.

## gemini-robotics-er-2-streaming-preview

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

### Gemini Robotics ER 2 – Streaming-Vorabversion

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

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-08-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-08-19 (UTC)."],[],[]]
