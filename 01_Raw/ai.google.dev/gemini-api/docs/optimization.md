---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=de
fetched_at: 2026-10-19T05:34:56.132803+00:00
title: "Gemini API\u00a0\u2013 Optimierung und Inferenz \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API – Optimierung und Inferenz

Die Gemini API bietet eine Vielzahl von Optimierungsmechanismen, mit denen Sie Geschwindigkeit, Kosten und Zuverlässigkeit entsprechend den Anforderungen Ihrer Arbeitslasten ausbalancieren können.
Ob Sie nun Konversationsbots in Echtzeit entwickeln oder umfangreiche Pipelines zur Offline-Datenverarbeitung ausführen – die Wahl des richtigen Paradigmas kann die Kosten erheblich senken oder die Leistung steigern.

| Funktion | Standard | Flex | Priorität | Batch | Caching |
| --- | --- | --- | --- | --- | --- |
| **Preise** | Standardpreis | 50% Rabatt | 75% bis 100% mehr als Standard | 50% Rabatt | 90% Rabatt + anteilige Speicherung von Tokens |
| **Latenz** | Sekunden bis Minuten | Minuten (Ziel: 1–15 Minuten) | Sekunden | Bis zu 24 Stunden | Schnellere Zeit bis zum ersten Token |
| **Zuverlässigkeit** | Hoch / Mittel bis hoch | Best-Effort-Ansatz (kann verworfen werden) | Hoch (kann nicht verworfen werden) | Hoch (für Durchsatz) | – |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron | Gespeicherter Status |
| **Bester Anwendungsfall** | Allgemeine Anwendungs-Workflows | Nicht dringende sequenzielle Ketten | Produktions- und für Nutzer sichtbare Apps | Umfangreiche Datasets, Offline-Bewertungen | Wiederkehrende Abfragen derselben Datei |

## Service Tiers für die Inferenz (synchron)

Sie können zwischen zuverlässigkeitsoptimiertem und kostenoptimiertem synchronem Traffic wechseln, indem Sie den Parameter `service_tier` in Ihren Standardgenerierungsaufrufen übergeben.

### Standard-Inferenz (Standardeinstellung)

Die Standard-Tier ist die Standardoption für die sequenzielle Content-Generierung.
Sie bietet normale Reaktionszeiten ohne zusätzliche Aufschläge oder lange Warteschlangen.

- **Zuverlässigkeit**:Standard-Kritikalität
- **Preis**:Standardpreise
- **Am besten geeignet für**:Die meisten interaktiven Alltagsanwendungen

### Prioritäts-Inferenz (latenzoptimiert)

[Prioritätsverarbeitung](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) leitet Ihre Anfragen
an Rechenwarteschlangen mit hoher Kritikalität weiter.
Dieser Traffic kann nicht verworfen werden (wird nie von anderen Tiers unterbrochen) und bietet die höchste Zuverlässigkeit. Wenn Sie die dynamischen Prioritätslimits überschreiten, wird die Anfrage vom System auf die Standardverarbeitung herabgestuft, anstatt dass ein Fehler auftritt.

- **Zuverlässigkeit**:Höchste Kritikalität
- **Preis**:75% bis 100% über den Standardpreisen
- **Am besten geeignet für**:Kunden-Chatbots, Betrugserkennung in Echtzeit und geschäftskritische Copiloten

### Flex-Inferenz (kostenoptimiert)

[Die Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) bietet einen Rabatt von 50% im Vergleich zu den Standardpreisen, da
opportunistische Rechenkapazität außerhalb der Spitzenzeiten genutzt wird. Anfragen werden synchron verarbeitet. Sie müssen also keinen Code umschreiben, um Batchobjekte zu verwalten.
Da es sich um „verwerfbaren“ Traffic handelt, können Anfragen unterbrochen werden, wenn im System Standard-Traffic-Spitzen auftreten.

- **Zuverlässigkeit**:Nicht garantierte, verwerfbare Kritikalität
- **Preis**:50% der Standardpreise (Abrechnung pro Token)
- **Am besten geeignet für**:Mehrstufige Agenten-Workflows, bei denen der Aufruf N+1 von der Ausgabe des Aufrufs N abhängt, CRM-Updates im Hintergrund und Offline-Bewertungen

## Batch API (Bulk, asynchron)

[Die Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) wurde entwickelt, um große Mengen
von Anfragen asynchron zu verarbeiten und dabei
50% der Standardkosten zu verursachen. Sie können Anfragen entweder als Inline-Wörterbücher oder mit einer JSONL-Eingabedatei (bis zu 2 GB) senden. Anfragen werden über Warteschlangen für den Hintergrunddurchsatz mit einer Zielbearbeitungszeit von 24 Stunden verarbeitet.

- **Zuverlässigkeit**:Verwerfbar, aber mit automatischen Wiederholungen und Warteschlangensystem nach 24 Stunden
- **Preis**:50% der Standardpreise
- **Am besten geeignet für**:Vorverarbeitung großer Datasets, Ausführung regelmäßiger Regressionstest-Suites und Generierung großer Mengen von Bildern oder Einbettungen

## Kontext-Caching (Einsparungen bei der Eingabe)

[Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) wird verwendet, wenn in kürzeren Anfragen wiederholt auf einen umfangreichen anfänglichen
Kontext verwiesen wird.

- **Implizites Caching**:Automatisch für Gemini 2.5 und neuere Modelle aktiviert
  Das System gibt Kosteneinsparungen weiter, wenn Ihre Anfrage vorhandene Caches auf Grundlage gängiger Prompt-Präfixe trifft.
- **Explizites Caching**:Sie können manuell ein Cache-Objekt mit einer bestimmten Gültigkeitsdauer (Time-To-Live, TTL) erstellen. Nach der Erstellung verweisen Sie für nachfolgende Anfragen auf die im Cache gespeicherten Tokens, um nicht wiederholt dieselbe Corpus-Nutzlast zu übergeben. Explizites Caching wird für Gemini 4 Argon und höher nicht unterstützt.
- **Preis**:Die Abrechnung erfolgt auf Grundlage der Anzahl der Cache-Tokens und der Speicherdauer (TTL).
- **Am besten geeignet für**:Chatbots mit ausführlichen Systemanweisungen, wiederholte Analysen langer Videodateien oder Abfragen großer Dokumentgruppen

## Kosten für Videoeingaben mit Agentenverarbeitung senken

Bei langen Videoinhalten (über 5–10 Minuten) oder gezielten Abfragen kann die Agentenverarbeitung die Kosten für Eingabetokens um bis zu 88% senken und gleichzeitig die Antwortqualität verbessern. Standardmäßig verwenden alle Modelle (einschließlich Gemini 4) die [statische Verarbeitung](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#agentic-video-understanding), um Frames mit 1 FPS zu extrahieren. Bei der Agentenverarbeitung für das Videoverständnis prüft das Modell zuerst das Videotranskript und lädt visuelle Segmente mit höheren Frameraten und Auflösungen nur bei Bedarf dynamisch. Bei kurzen Clips (unter 5 Minuten) oder umfassenden Zusammenfassungen von Videos sollten Sie den Standardmodus für die statische Verarbeitung beibehalten, um eine schnellere Zeit bis zum ersten Token (Time to First Token, TTFT) und einen geringeren Token-Overhead zu erzielen. Im Agentenmodus fallen während der Zeitachsen-Navigation interne Schlussfolgerungen (`total_thought_tokens`) und Tool-Roundtrips (`total_tool_use_tokens`) an.

Wenn Sie die Agentenverarbeitung mit Gemini 4 Argon, 3.8 Flash, 3.6 Flash oder 3.5 Flash Lite verwenden möchten,
legen Sie für Ihre Videoeingabe `processing: "agentic"` (Interactions API) oder
`media_processing: "AGENTIC"` (GenerateContent API) fest. Wenn das Modell die Agentenverarbeitung nicht unterstützt, wird ein Fehler zurückgegeben.

Weitere Informationen finden Sie unter
[Agentic video understanding](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#agentic-video-understanding).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-13 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-13 (UTC)."],[],[]]
