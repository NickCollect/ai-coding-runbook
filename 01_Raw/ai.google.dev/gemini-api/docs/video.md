---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=de
fetched_at: 2026-09-28T06:23:48.031746+00:00
title: "Videogenerierung in der Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Videogenerierung in der Gemini API

Die Gemini API bietet zwei Modelle für die Videogenerierung:
[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=de) und [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=de).
Beide sind für unterschiedliche Arbeitsabläufe konzipiert.

Verwenden Sie Gemini Omni Flash als Standardmodell für die Videogenerierung. Es bietet eine bessere Videokohärenz, eine bessere Verarbeitung mehrerer Eingaben (Unterstützung von Text-, Bild-, Audio- und Videoeingaben gleichzeitig), eine bessere Konsistenz der Charaktere, eine höhere faktische Genauigkeit und eine mehrfache Bearbeitung per Prompt (z.B. Ersetzen von Elementen oder Ändern der Perspektive). Verwenden Sie Veo 3.1, wenn bestimmte Funktionen wie die Szenenerweiterung, die Steuerung des letzten Frames oder die Integration in ältere Pipelines erforderlich sind.

## Gemini Omni Flash

Gemini Omni Flash ist ein schnelles, multimodales Modell für die Videogenerierung und die Bearbeitung von Videos per Prompt. Es kann Text-Prompts und Bilder schnell in kurze Videos umwandeln und ermöglicht es Ihnen, die Ergebnisse mithilfe der Interactions API in mehreren Schritten zu optimieren.

[Erste Schritte mit Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=de)

## Veo 3.1

Veo 3.1 ist ein Modell für die Videogenerierung mit nativem Audio. Es unterstützt Funktionen wie die Videoerweiterung, die framespezifische Generierung und die bildbasierte Steuerung über die `generateContent` API.

[Erste Schritte mit Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=de)

## Videos verstehen

Wenn Sie vorhandene Videoinhalte aufnehmen und analysieren möchten, anstatt neue Videos zu generieren
, lesen Sie den Leitfaden [Videos verstehen](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-30 (UTC)."],[],[]]
