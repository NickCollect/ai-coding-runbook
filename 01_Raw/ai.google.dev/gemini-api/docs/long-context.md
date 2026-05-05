---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=de
fetched_at: 2026-05-05T20:45:48.326738+00:00
title: "Langer Kontext \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Langer Kontext

Viele Gemini-Modelle haben große Kontextfenster mit 1 Million oder mehr Tokens.
Bisher war die Menge an Text (oder Tokens), die dem Modell gleichzeitig übergeben werden konnte, bei Large Language Models (LLMs) erheblich begrenzt.
Das große Kontextfenster von Gemini eröffnet viele neue Anwendungsfälle und Entwicklerparadigmen.

Der Code, den Sie bereits für Fälle wie die [Text
generierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de) oder [multimodale
Eingaben](https://ai.google.dev/gemini-api/docs/vision?hl=de) verwenden, funktioniert ohne Änderungen mit langem Kontext.

In diesem Dokument erhalten Sie einen Überblick darüber, was Sie mit Modellen mit Kontextfenstern von 1 Million und mehr Tokens erreichen können. Auf der Seite finden Sie eine kurze Übersicht über das Kontextfenster und Informationen dazu, wie Entwickler mit langem Kontext umgehen sollten, verschiedene Anwendungsfälle für langen Kontext in der Praxis und Möglichkeiten zur Optimierung der Nutzung von langem Kontext.

Die Kontextfenstergrößen bestimmter Modelle finden Sie auf der
[Seite Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de).

## Was ist das Kontextfenster?

Die grundlegende Verwendung der Gemini-Modelle besteht darin, dem Modell Informationen (Kontext) zu übergeben, woraufhin das Modell eine Antwort generiert. Eine Analogie für das Kontextfenster ist das Kurzzeitgedächtnis. Die Menge an Informationen, die im Kurzzeitgedächtnis einer Person gespeichert werden kann, ist begrenzt. Das gilt auch für generative Modelle.

Weitere Informationen zur Funktionsweise von Modellen finden Sie in unserem [Leitfaden zu generativen Modellen](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de#under-the-hood).

## Erste Schritte mit langem Kontext

Ältere Versionen generativer Modelle konnten nur 8.000 Tokens gleichzeitig verarbeiten. Neuere Modelle haben diese Grenze auf 32.000 oder sogar 128.000 Tokens erhöht. Gemini ist das erste Modell, das 1 Million Tokens verarbeiten kann.

In der Praxis würden 1 Million Tokens so aussehen:

- 50.000 Codezeilen (mit den üblichen 80 Zeichen pro Zeile)
- Alle Textnachrichten, die Sie in den letzten 5 Jahren gesendet haben
- 8 englische Romane durchschnittlicher Länge
- Transkripte von über 200 Podcastfolgen durchschnittlicher Länge

Bei den kleineren Kontextfenstern, die bei vielen anderen Modellen üblich sind, sind oft Strategien erforderlich, z. B. das willkürliche Löschen alter Nachrichten, das Zusammenfassen von Inhalten, die Verwendung von RAG mit Vektordatenbanken oder das Filtern von Prompts, um Tokens zu sparen.

Diese Techniken sind in bestimmten Szenarien zwar weiterhin wertvoll, aber das große Kontextfenster von Gemini ermöglicht einen direkteren Ansatz: alle relevanten Informationen im Voraus bereitzustellen. Da Gemini-Modelle speziell für umfangreiche Kontextfunktionen entwickelt wurden, zeigen sie ein leistungsstarkes In-Context-Learning. Beispiel: Wenn nur Lehrmaterialien im Kontext bereitgestellt werden (eine 500-seitige Referenz
grammatik, ein Wörterbuch und ≈ 400 parallele Sätze), kann Gemini
[vom Englischen nach Kalamang übersetzen](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)
– eine Papua-Sprache mit
weniger als 200 Sprechern – mit einer Qualität, die der einer Person ähnelt, die aus denselben
Materialien gelernt hat. Dies veranschaulicht den Paradigmenwechsel, der durch den langen Kontext von Gemini ermöglicht wird, und eröffnet neue Möglichkeiten durch robustes In-Context-Learning.

## Anwendungsfälle für langen Kontext

Der Standardanwendungsfall für die meisten generativen Modelle ist zwar immer noch die Texteingabe, aber die Gemini-Modellfamilie ermöglicht ein neues Paradigma multimodaler Anwendungsfälle. Diese Modelle können Text, Video, Audio und Bilder nativ verstehen. Sie werden
von der [Gemini API begleitet, die multimodale Datei
typen](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=de) verarbeitet.

### Text im Langformat

Text hat sich als die Ebene der Intelligenz erwiesen, die einen Großteil der Dynamik rund um LLMs untermauert. Wie bereits erwähnt, war ein Großteil der praktischen Einschränkungen von LLMs darauf zurückzuführen, dass kein ausreichend großes Kontextfenster für bestimmte Aufgaben vorhanden war. Dies führte zur schnellen Einführung von Retrieval Augmented Generation (RAG) und anderen Techniken, die dem Modell dynamisch relevante Kontextinformationen zur Verfügung stellen. Mit immer größeren Kontextfenstern stehen jetzt neue Techniken zur Verfügung, die neue Anwendungsfälle ermöglichen.

Einige neue und Standardanwendungsfälle für textbasierten langen Kontext:

- Zusammenfassen großer Textmengen
  - Bei früheren Zusammenfassungsoptionen mit kleineren Kontextmodellen war ein gleitendes Fenster oder eine andere Technik erforderlich, um den Status der vorherigen Abschnitte beizubehalten, während dem Modell neue Tokens übergeben wurden.
- Fragen und Antworten
  - Bisher war dies aufgrund der begrenzten Menge an Kontext und der geringen faktischen Erinnerung der Modelle nur mit RAG möglich.
- Agentische Workflows
  - Text ist die Grundlage dafür, wie Agents den Status ihrer Aufgaben beibehalten. Wenn nicht genügend Informationen über die Welt und das Ziel des Agents vorhanden sind, wird die Zuverlässigkeit der Agents eingeschränkt.

[Many-shot in-context learning](https://arxiv.org/pdf/2404.11018) ist eine der einzigartigsten Funktionen, die durch lange Kontextmodelle ermöglicht werden. Untersuchungen haben gezeigt, dass die üblichen Paradigmen für „Single-Shot“- oder „Multi-Shot“-Beispiele, bei denen dem Modell ein oder mehrere Beispiele für eine Aufgabe präsentiert werden, auf Hunderte, Tausende oder sogar Hunderttausende von Beispielen skaliert werden können, was zu neuen Modellfunktionen führen kann. Es hat sich gezeigt, dass dieser Many-Shot-Ansatz ähnlich wie Modelle funktioniert, die für eine bestimmte Aufgabe optimiert wurden. Für Anwendungsfälle, in denen die Leistung eines Gemini-Modells für einen Produktions-Roll-out noch nicht ausreicht, können Sie den Many-Shot-Ansatz ausprobieren. Wie Sie später im Abschnitt zur Optimierung des langen Kontexts noch einmal untersuchen werden, ist diese Art von Arbeitslast mit hoher Eingabetoken durch Kontext-Caching in einigen Fällen wesentlich wirtschaftlicher und hat sogar eine geringere Latenz.

### Videos im Langformat

Der Nutzen von Videoinhalten war lange Zeit durch die mangelnde Zugänglichkeit des Mediums selbst eingeschränkt. Es war schwierig, die Inhalte zu überfliegen, Transkripte konnten die Nuancen eines Videos oft nicht erfassen und die meisten Tools verarbeiten Bilder, Text und Audio nicht zusammen. Mit Gemini führen die Textfunktionen mit langem Kontext dazu, dass Fragen zu multimodalen Eingaben mit gleichbleibender Leistung beantwortet werden können.

Einige neue und Standardanwendungsfälle für langen Videokontext:

- Fragen und Antworten zu Videos
- Videospeicher, wie bei [Google's Project Astra](https://deepmind.google/technologies/gemini/project-astra/?hl=de) gezeigt
- Videountertitel
- Videoempfehlungssysteme durch Anreicherung vorhandener Metadaten mit neuem multimodalen Verständnis
- Videoanpassung durch Analyse einer Datenmenge und der zugehörigen Videometadaten und anschließendes Entfernen von Teilen von Videos, die für den Zuschauer nicht relevant sind
- Moderation von Videoinhalten
- Videoverarbeitung in Echtzeit

Bei der Arbeit mit Videos ist es wichtig zu berücksichtigen, wie die [Videos in
Tokens verarbeitet werden](https://ai.google.dev/gemini-api/docs/tokens?hl=de#media-token), da dies sich auf die
Abrechnung und die Nutzungslimits auswirkt. Weitere Informationen zum Prompting mit Videodateien finden Sie in
dem [Leitfaden
zum Prompting](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=de#prompting-with-videos).

### Audioinhalte im Langformat

Die Gemini-Modelle waren die ersten nativ multimodalen Large Language Models, die Audio verstehen konnten. Bisher umfasste der typische Entwicklerworkflow die Verknüpfung mehrerer domänenspezifischer Modelle, z. B. eines Speech-to-Text-Modells und eines Text-zu-Text-Modells, um Audio zu verarbeiten. Dies führte zu einer zusätzlichen Latenz, die durch mehrere Round-Trip-Anfragen erforderlich war, und zu einer geringeren Leistung, die in der Regel auf die nicht verbundene Architektur der Einrichtung mit mehreren Modellen zurückzuführen ist.

Einige neue und Standardanwendungsfälle für Audiokontext:

- Sprache-zu-Text und Übersetzung in Echtzeit
- Fragen und Antworten zu Podcasts / Videos
- Transkription und Zusammenfassung von Besprechungen
- Sprachassistenten

Weitere Informationen zum Prompting mit Audiodateien finden Sie im [Leitfaden zum Prompting](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=de#prompting-with-videos).

## Optimierungen für langen Kontext

Die wichtigste Optimierung bei der Arbeit mit langem Kontext und den Gemini
Modellen ist die Verwendung von [Kontext
Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de). Neben der bisherigen Unmöglichkeit, viele Tokens in einer einzigen Anfrage zu verarbeiten, war die andere Haupteinschränkung der Preis. Wenn Sie eine App "Mit Ihren Daten chatten" haben, bei der ein Nutzer 10 PDFs, ein Video und einige Arbeitsdokumente hochlädt, müssten Sie in der Vergangenheit mit einem komplexeren RAG-Tool (Retrieval Augmented Generation) / Framework arbeiten, um diese Anfragen zu verarbeiten und einen erheblichen Betrag für in das Kontextfenster verschobene Tokens zu bezahlen. Jetzt können Sie die vom Nutzer hochgeladenen Dateien im Cache speichern und stundenweise bezahlen. Die Kosten für Eingabe / Ausgabe pro Anfrage sind bei Gemini Flash beispielsweise etwa viermal niedriger als die Standardkosten für Eingabe / Ausgabe. Wenn der Nutzer also ausreichend mit seinen Daten chattet, können Sie als Entwickler erhebliche Kosten sparen.

## Einschränkungen für langen Kontext

In verschiedenen Abschnitten dieses Leitfadens ging es darum, wie Gemini-Modelle eine hohe Leistung bei verschiedenen "Nadel im Heuhaufen"-Evaluationsvorgängen erzielen. Bei diesen Tests wird die einfachste Einrichtung berücksichtigt, bei der Sie nach einer einzelnen „Nadel“ suchen. Wenn Sie nach mehreren „Nadeln“ oder bestimmten Informationen suchen, ist die Leistung des Modells nicht so genau. Die Leistung kann je nach Kontext stark variieren. Das ist wichtig, da es einen inhärenten Kompromiss zwischen dem Abrufen der richtigen Informationen und den Kosten gibt. Sie können bei einer einzelnen Abfrage etwa 99% erreichen, müssen aber jedes Mal die Kosten für Eingabetokens bezahlen, wenn Sie diese Abfrage senden. Wenn also 100 Informationen abgerufen werden sollen und Sie eine Leistung von 99% benötigen, müssen Sie wahrscheinlich 100 Anfragen senden. Dies ist ein gutes Beispiel dafür, wie Kontext-Caching die Kosten für die Verwendung von Gemini-Modellen erheblich senken und gleichzeitig die Leistung hoch halten kann.

## Häufig gestellte Fragen

### Wo ist der beste Ort, um meine Abfrage in das Kontextfenster einzufügen?

In den meisten Fällen, insbesondere wenn der gesamte Kontext lang ist, ist die Leistung des Modells besser, wenn Sie Ihre Abfrage / Frage am Ende des Prompts platzieren (nach dem gesamten anderen Kontext).

### Verringert sich die Leistung des Modells, wenn ich einer Abfrage weitere Tokens hinzufüge?

Wenn Tokens nicht an das Modell übergeben werden müssen, ist es im Allgemeinen am besten, sie nicht zu übergeben. Wenn Sie jedoch eine große Menge an Tokens mit einigen Informationen haben und Fragen zu diesen Informationen stellen möchten, kann das Modell diese Informationen sehr gut extrahieren (in vielen Fällen mit einer Genauigkeit von bis zu 99 %).

### Wie kann ich die Kosten für Abfragen mit langem Kontext senken?

Wenn Sie eine ähnliche Gruppe von Tokens / Kontext haben, die Sie mehrmals verwenden möchten, kann [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) dazu beitragen, die Kosten für das Stellen von Fragen zu diesen Informationen zu senken.

### Wirkt sich die Kontextlänge auf die Latenz des Modells aus?

Bei jeder Anfrage gibt es eine bestimmte Latenz, unabhängig von der Größe. Im Allgemeinen haben längere Abfragen jedoch eine höhere Latenz (Zeit bis zum ersten Token).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
