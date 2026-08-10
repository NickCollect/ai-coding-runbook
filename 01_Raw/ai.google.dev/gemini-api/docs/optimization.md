---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=de
fetched_at: 2026-08-10T03:20:10.745225+00:00
title: "Gemini API\u00a0\u2013 Optimierung und Inferenz \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API – Optimierung und Inferenz

Die Gemini API bietet eine Vielzahl von Optimierungsmechanismen, mit denen Sie Geschwindigkeit, Kosten und Zuverlässigkeit je nach den spezifischen Anforderungen Ihrer Arbeitslasten ausbalancieren können.
Ob Sie nun Konversationsbots in Echtzeit entwickeln oder umfangreiche Pipelines zur Offline-Datenverarbeitung ausführen – die Wahl des richtigen Paradigmas kann die Kosten erheblich senken oder die Leistung steigern.

| Funktion | Standard | Flex | Priorität | Batch | Caching |
| --- | --- | --- | --- | --- | --- |
| **Preise** | Standardpreis | 50% Rabatt | 75% bis 100% mehr als Standard | 50% Rabatt | 90% Rabatt + anteilige Speicherung von Tokens |
| **Latenz** | Sekunden bis Minuten | Minuten (Ziel: 1–15 Minuten) | Sekunden | Bis zu 24 Stunden | Schnellere Zeit bis zum ersten Token |
| **Zuverlässigkeit** | Hoch / Mittel bis hoch | Best-Effort-Ansatz (kann verworfen werden) | Hoch (kann nicht verworfen werden) | Hoch (für Durchsatz) | – |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron | Gespeicherter Status |
| **Bester Anwendungsfall** | Allgemeine Anwendungs-Workflows | Nicht dringende sequenzielle Ketten | Produktions- und nutzerorientierte Apps | Umfangreiche Datasets, Offline-Bewertungen | Wiederkehrende Abfragen derselben Datei |

## Dienststufen für die Inferenz (synchron)

Sie können zwischen zuverlässigkeitsoptimiertem und kostenoptimiertem synchronem Traffic wechseln, indem Sie den Parameter `service_tier` in Ihren Standardgenerierungsaufrufen übergeben.

### Standardinferenz (Standardeinstellung)

Die Standardstufe ist die Standardoption für die sequenzielle Contentgenerierung.
Sie bietet normale Reaktionszeiten ohne zusätzliche Aufschläge oder lange Warteschlangen.

- **Zuverlässigkeit**:Standardkritikalität
- **Preis**:Standardpreise
- **Am besten geeignet für**:Die meisten interaktiven Alltagsanwendungen

### Prioritätsinferenz (latenzoptimiert)

[Prioritätsverarbeitung](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) leitet Ihre Anfragen
an Rechenwarteschlangen mit hoher Kritikalität weiter.
Dieser Traffic kann nicht verworfen werden (wird nie von anderen Stufen unterbrochen) und bietet die höchste Zuverlässigkeit. Wenn Sie die dynamischen Prioritätslimits überschreiten, wird die Anfrage vom System auf die Standardverarbeitung herabgestuft, anstatt dass ein Fehler auftritt.

- **Zuverlässigkeit**:Höchste Kritikalität
- **Preis**:75% bis 100% über den Standardpreisen
- **Am besten geeignet für**:Kunden-Chatbots, Betrugserkennung in Echtzeit und geschäftskritische Copiloten

### Flexible Inferenz (kostenoptimiert)

[Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) bietet einen Rabatt von 50% im Vergleich zu den Standardpreisen, da opportunistische Rechenkapazität außerhalb der Spitzenzeiten genutzt wird. Anfragen werden synchron verarbeitet. Sie müssen also keinen Code umschreiben, um Batchobjekte zu verwalten.
Da es sich um „verwerfbaren“ Traffic handelt, können Anfragen unterbrochen werden, wenn im System Standard-Trafficspitzen auftreten.

- **Zuverlässigkeit**:Nicht garantierte, verwerfbare Kritikalität
- **Preis**:50% der Standardpreise (Abrechnung pro Token)
- **Am besten geeignet für**:Mehrstufige Agenten-Workflows, bei denen der Aufruf N+1 von der Ausgabe des Aufrufs N abhängt, CRM-Updates im Hintergrund und Offline-Bewertungen

## Batch API (Bulk, asynchron)

[Die Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) wurde entwickelt, um große Mengen
von Anfragen asynchron zu
50% der Standardkosten zu verarbeiten. Sie können Anfragen entweder als Inline-Wörterbücher oder mit einer JSONL-Eingabedatei (bis zu 2 GB) senden. Anfragen werden mit Hintergrund-Durchsatzwarteschlangen mit einer Zielbearbeitungszeit von 24 Stunden verarbeitet.

- **Zuverlässigkeit**:Verwerfbar, aber mit automatischen Wiederholungen und Warteschlangensystem nach 24 Stunden
- **Preis**:50% der Standardpreise
- **Am besten geeignet für**:Vorverarbeitung großer Datasets, Ausführung regelmäßiger Regressionstest-Suites und Generierung großer Mengen von Bildern oder Einbettungen

## Kontext-Caching (Einsparungen bei der Eingabe)

[Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) wird verwendet, wenn in kürzeren Anfragen wiederholt auf einen umfangreichen anfänglichen
Kontext verwiesen wird.

- **Implizites Caching**:Automatisch für Gemini 2.5 und neuere Modelle aktiviert
  Das System gibt Kosteneinsparungen weiter, wenn Ihre Anfrage vorhandene Caches auf Grundlage gängiger Prompt-Präfixe trifft.
- **Explizites Caching**:Sie können manuell ein Cache-Objekt mit einer bestimmten Gültigkeitsdauer (Time-To-Live, TTL) erstellen. Nach der Erstellung können Sie für nachfolgende Anfragen auf die im Cache gespeicherten Tokens verweisen, um nicht immer wieder dieselbe Korpusnutzlast zu übergeben.
- **Preis**:Abrechnung basierend auf der Anzahl der Cache-Tokens und der Speicherdauer (TTL)
- **Am besten geeignet für**:Chatbots mit ausführlichen Systemanweisungen, wiederholte Analysen langer Videodateien oder Abfragen großer Dokumentgruppen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
