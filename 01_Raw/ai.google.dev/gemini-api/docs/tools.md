---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=de
fetched_at: 2026-09-14T05:41:00.769873+00:00
title: "Tools mit der Gemini API verwenden \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tools mit der Gemini API verwenden

Tools erweitern die Funktionen von Gemini-Modellen und ermöglichen es ihnen, in der Welt zu agieren, auf Echtzeitinformationen zuzugreifen und komplexe Berechnungsaufgaben auszuführen. Modelle können Tools sowohl in Standardinteraktionen mit Anfragen und Antworten als auch in
Echtzeit-Streamingsitzungen mit der [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) verwenden.

Tools sind bestimmte Funktionen (z. B. Google Suche oder Codeausführung), die ein Modell verwenden kann, um Anfragen zu beantworten. Die Gemini API bietet eine Reihe vollständig
verwalteter, integrierter Tools. Sie können aber auch benutzerdefinierte Tools mit [Funktions
aufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) definieren.

Informationen zum Erstellen mehrstufiger, zielorientierter Systeme finden Sie in der [Übersicht zu Agents](https://ai.google.dev/gemini-api/docs/agents?hl=de).

## Verfügbare integrierte Tools

| Tool | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) | Antworten mit aktuellen Ereignissen und Fakten aus dem Web untermauern, um Halluzinationen zu reduzieren. | Fragen zu aktuellen Ereignissen beantworten, Fakten mit verschiedenen Quellen überprüfen. |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) | Standortbezogene Assistenten erstellen, die Orte finden, Wegbeschreibungen abrufen und umfassende lokale Informationen bereitstellen können. | Reisepläne mit mehreren Stationen erstellen, lokale Unternehmen anhand von Nutzerkriterien finden. |
| [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) | Das Modell kann Python-Code schreiben und ausführen, um mathematische Probleme zu lösen oder Daten genau zu verarbeiten. | Komplexe mathematische Gleichungen lösen, Textdaten präzise verarbeiten und analysieren. |
| [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) | Das Modell kann Inhalte von bestimmten Webseiten oder aus bestimmten Dokumenten lesen und analysieren. | Fragen basierend auf bestimmten URLs oder Dokumenten beantworten, Informationen auf verschiedenen Webseiten abrufen. |
| [Computernutzung (Vorschau)](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) | Gemini kann einen Bildschirm anzeigen und Aktionen generieren, um mit Webbrowser-UIs zu interagieren (clientseitige Ausführung). | Wiederholte webbasierte Workflows automatisieren, Benutzeroberflächen von Webanwendungen testen. |
| [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de) | Eigene Dokumente indexieren und durchsuchen, um Retrieval-Augmented Generation (RAG) zu ermöglichen. | Technische Handbücher durchsuchen, Fragen zu proprietären Daten beantworten. |

Auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing_for_tools) finden Sie Details
zu den Kosten für bestimmte Tools.

## Funktionsweise der Toolausführung

Mit Tools kann das Modell während einer Unterhaltung Aktionen anfordern. Der Ablauf unterscheidet sich je nachdem, ob das Tool integriert (von Google verwaltet) oder benutzerdefiniert (von Ihnen verwaltet) ist.

### Ablauf für integrierte Tools

Bei integrierten Tools (Google Suche, Google Maps, URL-Kontext, Dateisuche, Codeausführung) erfolgt der gesamte Prozess in einem API-Aufruf:

1. **Sie** senden einen Prompt: „Was ist die Quadratwurzel des aktuellen Aktienkurses von GOOG?“
2. **Gemini** entscheidet, dass Tools erforderlich sind, und führt sie auf den Google-Servern aus (z.B. wird nach dem Aktienkurs gesucht und dann Python-Code ausgeführt, um die Quadratwurzel zu berechnen).
3. **Gemini** sendet die endgültige Antwort zurück, die auf den Toolergebnissen basiert.

### Ablauf für benutzerdefinierte Tools (Funktionsaufrufe)

Bei benutzerdefinierten Tools und der Computernutzung wird die Ausführung von Ihrer Anwendung übernommen:

1. **Sie** senden einen Prompt zusammen mit Funktionsdeklarationen (Tools).
2. **Gemini** sendet möglicherweise strukturiertes JSON zurück, um eine bestimmte Funktion aufzurufen
   (z. B. `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   immer mit einer eindeutigen `id`.
3. **Sie** führen die Funktion in Ihrer Anwendung oder Umgebung aus.
4. **Sie** senden die Funktionsergebnisse mit derselben `id` wie der Funktionsaufruf an Gemini zurück.
5. **Gemini** verwendet die Ergebnisse, um eine endgültige Antwort oder einen weiteren Toolaufruf zu generieren.

Weitere Informationen finden Sie im [Leitfaden zu Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

### Ablauf für die Kombination von integrierten und benutzerdefinierten Tools

Bei Anfragen, die integrierte und benutzerdefinierte Tools (Funktionsaufrufe) kombinieren, verwendet das
Modell die [Toolkontextzirkulation](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de), um die
Ausführung in verschiedenen Umgebungen zu koordinieren:

1. **Sie** senden einen Prompt und deklarieren die integrierten Tools und benutzerdefinierten Funktionen, die Sie aktivieren möchten. Legen Sie ein Flag fest, um die Kombinationsunterstützung zu aktivieren.
2. **Gemini** führt integrierte Tools aus und übergibt die Steuerung an den Nutzer, wenn clientseitige Funktionsaufrufe generiert werden (welche zuerst ausgeführt werden, hängt vom Prompt und der Entscheidung des Modells ab). Es wird eine Antwort mit Folgendem zurückgesendet:
   - Bestätigung des Toolaufrufs
   - Ergebnisse der Toolantwort (können nach dem JSON-Code kommen, wenn das Modell zwei parallele Funktionsaufrufe generiert hat)
   - Strukturiertes JSON zum Aufrufen Ihrer Funktion
   - Verschlüsselte Gedankensignaturen, um den Kontext beizubehalten
3. **Sie** führen die Funktion in Ihrer Anwendung oder Umgebung aus.
4. **Sie** geben alle Teile der Gemini-Antwort sowie die Ergebnisse des Funktionsaufrufs zurück.
5. **Gemini** generiert die endgültige Antwort mit dem kombinierten Kontext.

Lesen Sie den [Leitfaden zur Toolkombination](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de), um zu erfahren,
wie Sie die Unterstützung für die Kombination von integrierten und benutzerdefinierten Tools aktivieren, und finden Sie Beispiele für die
Kontextzirkulation.

## Strukturierte Ausgaben im Vergleich zu Funktionsaufrufen

Gemini bietet zwei Methoden zum Generieren strukturierter Ausgaben. Verwenden Sie [Funktions
aufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de), wenn das Modell einen
Zwischenschritt ausführen muss, indem es eine Verbindung zu Ihren eigenen Tools oder Datensystemen herstellt. Verwenden Sie
[strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de), wenn die endgültige Antwort des Modells unbedingt einem bestimmten Schema entsprechen muss, z. B. zum Rendern
einer benutzerdefinierten Benutzeroberfläche.

## Strukturierte Ausgaben mit Tools

Sie können [strukturierte Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) mit
integrierten Tools kombinieren, um sicherzustellen, dass Modellantworten, die auf externen Daten oder
Berechnungen basieren, weiterhin einem strengen Schema entsprechen.

Codebeispiele finden Sie unter [Strukturierte Ausgaben mit Tools](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=de#structured_outputs_with_tools).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-11 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-11 (UTC)."],[],[]]
