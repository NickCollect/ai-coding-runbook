---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=de
fetched_at: 2026-09-28T06:32:01.230851+00:00
title: "Bilder mit Imagen generieren \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)

Feedback geben

# Bilder mit Imagen generieren

Imagen ist das alte Modell zur Bildgenerierung von Google. Sie wurde jetzt eingestellt und ist nicht mehr in der Gemini API verfügbar.

## Zu Nano Banana migrieren

Auf Nano Banana für die Bildgenerierung umstellen:

- **Modellname**: Verwenden Sie `gemini-2.5-flash-image` (oder Nano Banana 2-Modelle wie `gemini-3.1-flash-image`) anstelle von Imagen-Modellnamen.
- **Methode**: Verwenden Sie `client.models.generate_content` anstelle von `client.models.generate_images`.
- **Antwortverarbeitung**: Nano Banana gibt Inhaltsteile mit Bilddaten anstelle eines bestimmten Bildantwortobjekts zurück.

Weitere Informationen und Beispiele finden Sie im [Leitfaden zur Bilderstellung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-18 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-18 (UTC)."],[],[]]
