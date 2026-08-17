---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=de
fetched_at: 2026-08-17T02:21:47.239311+00:00
title: "Kontext-Caching \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Kontext-Caching

In einem typischen KI-Workflow werden dieselben Eingabetokens immer wieder an ein Modell übergeben. Die Gemini API bietet implizites Caching, um Leistung und Kosten zu optimieren.

## Implizites Caching

Implizites Caching ist standardmäßig für alle Gemini 2.5-Modelle und neuere Modelle aktiviert. Es wird
sowohl für [zustandsorientierte](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#multi-turn-conversations) (mit `previous_interaction_id`)
als auch für [zustandslose](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#stateless-conversations) Konversationsmodi unterstützt.
Wir geben Kosteneinsparungen automatisch weiter, wenn Ihre Anfrage auf Caches trifft. Sie müssen nichts tun, um diese Funktion zu aktivieren. Die Mindestanzahl an Eingabetokens für das Kontext-Caching ist in der folgenden Tabelle für jedes Modell aufgeführt:

| Modell | Mindestanzahl an Tokens |
| --- | --- |
| Gemini 3.5 Flash | 4.096 |
| Gemini 3.1 Pro (Vorabversion) | 4.096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

So erhöhen Sie die Wahrscheinlichkeit eines impliziten Cache-Treffers:

- Platzieren Sie große und häufig verwendete Inhalte am Anfang Ihrer Eingabeaufforderung.
- Senden Sie Anfragen mit ähnlichem Präfix in kurzer Zeit.

Die Anzahl der Tokens, die Cache-Treffer waren, finden Sie im Feld `usage.total_cached_tokens` des Antwortobjekts (Python und JavaScript).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
