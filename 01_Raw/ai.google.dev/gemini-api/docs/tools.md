---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=de
fetched_at: 2026-05-05T20:03:40.604041+00:00
title: "Tools mit der Gemini API verwenden \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tools mit der Gemini API verwenden

Tools erweitern die Funktionen von Gemini-Modellen und ermöglichen es ihnen, Aktionen in der realen Welt auszuführen, auf Echtzeitinformationen zuzugreifen und komplexe Berechnungsaufgaben zu erledigen. Modelle können Tools sowohl bei Standard-Anfrage-Antwort-Interaktionen als auch bei Echtzeit-Streaming-Sitzungen über die [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) verwenden.

Tools sind bestimmte Funktionen (z. B. Google Suche oder Codeausführung), die ein Modell verwenden kann, um Anfragen zu beantworten. Die Gemini API bietet eine Reihe von vollständig verwalteten, integrierten Tools. Sie können aber auch benutzerdefinierte Tools mit [Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) definieren.

Informationen zum Erstellen von mehrstufigen, zielorientierten Systemen finden Sie in der [Übersicht über Agents](https://ai.google.dev/gemini-api/docs/agents?hl=de).

## Verfügbare integrierte Tools

| Tool | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) | Antworten auf aktuelle Ereignisse und Fakten aus dem Web stützen, um Halluzinationen zu reduzieren. | \- Fragen zu aktuellen Ereignissen beantworten   \- Fakten mit verschiedenen Quellen abgleichen |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) | Erstellen Sie standortbezogene Assistenten, die Orte finden, Wegbeschreibungen abrufen und umfassende lokale Informationen bereitstellen können. | – Reisepläne mit mehreren Zwischenstopps erstellen   – Lokale Unternehmen anhand von Nutzerkriterien finden |
| [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) | Das Modell darf Python-Code schreiben und ausführen, um mathematische Probleme zu lösen oder Daten genau zu verarbeiten. | \- Komplexe mathematische Gleichungen lösen   \- Textdaten präzise verarbeiten und analysieren |
| [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) | Weisen Sie das Modell an, Inhalte von bestimmten Webseiten oder Dokumenten zu lesen und zu analysieren. | – Fragen basierend auf bestimmten URLs oder Dokumenten beantworten   – Informationen von verschiedenen Webseiten abrufen |
| [Computernutzung (Vorschau)](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) | Gemini kann einen Bildschirm ansehen und Aktionen generieren, um mit Webbrowser-Benutzeroberflächen zu interagieren (clientseitige Ausführung). | – Automatisieren von sich wiederholenden webbasierten Workflows   – Testen von Benutzeroberflächen von Webanwendungen |
| [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de) | Sie können Ihre eigenen Dokumente indexieren und durchsuchen, um Retrieval-Augmented Generation (RAG) zu ermöglichen. | – Suche in technischen Handbüchern   – Question Answering über proprietäre Daten |

Weitere Informationen zu den Kosten für bestimmte Tools finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing_for_tools).

## So funktioniert die Toolausführung

Mithilfe von Tools kann das Modell während einer Unterhaltung Aktionen anfordern. Der Ablauf hängt davon ab, ob das Tool integriert (von Google verwaltet) oder benutzerdefiniert (von Ihnen verwaltet) ist.

### Ablauf integrierter Tools

Bei integrierten Tools (Google Suche, Google Maps, URL-Kontext, Dateisuche, Codeausführung) erfolgt der gesamte Prozess in einem API-Aufruf:

1. **Sie** senden einen Prompt: „Was ist die Quadratwurzel des aktuellen Aktienkurses von GOOG?“
2. **Gemini** entscheidet, dass Tools benötigt werden, und führt sie auf den Servern von Google aus (z.B. wird nach dem Aktienkurs gesucht und dann Python-Code ausgeführt, um die Quadratwurzel zu berechnen).
3. **Gemini** sendet die endgültige Antwort zurück, die auf den Tool-Ergebnissen basiert.

### Benutzerdefinierter Toolablauf (Funktionsaufrufe)

Bei benutzerdefinierten Tools und der Computerverwendung übernimmt Ihre Anwendung die Ausführung:

1. **Sie** senden einen Prompt zusammen mit Funktionsdeklarationen (Tools).
2. **Gemini** kann strukturiertes JSON zurückgeben, um eine bestimmte Funktion aufzurufen (z. B. `{"name": "get_order_status", "args": {"order_id": "123"}}`), immer mit einer eindeutigen `id`.
3. **Sie** führen die Funktion in Ihrer Anwendung oder Umgebung aus.
4. **Sie** senden die Funktionsergebnisse mit demselben `id` wie beim Funktionsaufruf zurück an Gemini.
5. **Gemini** verwendet die Ergebnisse, um eine endgültige Antwort oder einen weiteren Tool-Aufruf zu generieren.

Weitere Informationen finden Sie im [Leitfaden zu Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

### Ablauf zum Kombinieren integrierter und benutzerdefinierter Tools

Bei Anfragen, in denen integrierte und benutzerdefinierte Tools (Funktionsaufrufe) kombiniert werden, verwendet das Modell [Tool-Kontextzirkulation](https://ai.google.dev/gemini-api/docs/toold-combination?hl=de), um die Ausführung in verschiedenen Umgebungen zu koordinieren:

1. **Sie** senden einen Prompt und deklarieren die integrierten Tools und benutzerdefinierten Funktionen, die Sie aktivieren möchten. Dabei legen Sie ein Flag fest, um die Unterstützung von Kombinationen zu aktivieren.
2. **Gemini** führt integrierte Tools aus und übergibt die Kontrolle an den Nutzer, wenn clientseitige Funktionsaufrufe generiert werden. Welche Aktion zuerst ausgeführt wird, hängt vom Prompt und der Entscheidung des Modells ab. Es wird eine Antwort mit Folgendem zurückgesendet:
   - Bestätigung des Tool-Aufrufs
   - Ergebnisse der Tool-Antwort (diese können nach dem JSON-Code stehen, wenn das Modell zwei parallele Funktionsaufrufe generiert hat)
   - Strukturierter JSON-Code zum Aufrufen Ihrer Funktion
   - Verschlüsselte Gedanken-Signaturen, um den Kontext beizubehalten
3. **Sie** führen die Funktion in Ihrer Anwendung oder Umgebung aus.
4. **Sie** geben alle Teile der Antwort von Gemini sowie die Ergebnisse Ihres Funktionsaufrufs zurück.
5. **Gemini** generiert die endgültige Antwort anhand des gesamten kombinierten Kontexts.

Im [Leitfaden zur Kombination von Tools](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) erfahren Sie, wie Sie die Unterstützung für die Kombination von integrierten und benutzerdefinierten Tools aktivieren und wie der Kontext weitergegeben wird.

## Strukturierte Ausgaben im Vergleich zu Funktionsaufrufen

Gemini bietet zwei Methoden zum Generieren strukturierter Ausgaben. Verwenden Sie [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de), wenn das Modell einen Zwischenschritt ausführen muss, indem es eine Verbindung zu Ihren eigenen Tools oder Datensystemen herstellt. Verwenden Sie [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de), wenn die endgültige Antwort des Modells unbedingt einem bestimmten Schema entsprechen muss, z. B. zum Rendern einer benutzerdefinierten Benutzeroberfläche.

## Strukturierte Ausgaben mit Tools

Sie können [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) mit integrierten Tools kombinieren, um sicherzustellen, dass Modellantworten, die auf externen Daten oder Berechnungen basieren, einem strengen Schema entsprechen.

Codebeispiele finden Sie unter [Strukturierte Ausgaben mit Tools](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=de#structured_outputs_with_tools).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
