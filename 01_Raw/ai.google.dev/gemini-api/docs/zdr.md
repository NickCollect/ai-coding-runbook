---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=de
fetched_at: 2026-05-05T20:01:14.182994+00:00
title: "Keine Datenspeicherung in der Gemini Developer API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Keine Datenspeicherung in der Gemini Developer API

Auf dieser Seite werden Details zu dem beschrieben, was in der Gemini Developer API allgemein als „keine Datenaufbewahrung“ bezeichnet wird.

## Einschränkung für Training

Wie in den [Nutzungsbedingungen für die Gemini API](https://ai.google.dev/gemini-api/terms?hl=de) beschrieben, verwendet Google bei der Nutzung kostenpflichtiger Dienste Ihre Prompts (einschließlich zugehöriger Systemanweisungen, zwischengespeicherter Inhalte und Dateien wie Bilder, Videos oder Dokumente) oder Antworten nicht, um unsere Produkte zu verbessern. Kostenpflichtige Dienste werden
[hier](https://ai.google.dev/gemini-api/terms?hl=de#paid-services) definiert.

## Aufbewahrung von Kundendaten und keine Datenaufbewahrung

Kundendaten werden in den folgenden Szenarien und unter den folgenden Bedingungen in der Regel für einen begrenzten Zeitraum aufbewahrt. Um keine Daten aufzubewahren, müssen Kunden in jedem dieser Bereiche bestimmte Maßnahmen ergreifen oder bestimmte Funktionen vermeiden:

- **Prompt-Protokollierung zur Missbrauchsüberwachung**: Wie in den [Zusatzbedingungen für die
  Gemini API](https://ai.google.dev/gemini-api/terms?hl=de) beschrieben, protokolliert Google bei kostenpflichtigen Diensten Prompts und Antworten für einen begrenzten Zeitraum ausschließlich, um Verstöße gegen die [Richtlinie zur unzulässigen Nutzung](https://policies.google.com/terms/generative-ai/use-policy?hl=de) zu erkennen. Wenn Ihre Anfrage zur Datenaufbewahrung für ein bestimmtes Projekt genehmigt wird, werden alle Nutzerinhalte (Prompts und Antworten) und identifizierbaren Metadaten (z. B. IP-Adressen und Google-Konto-IDs) vor der Protokollierung gelöscht. Der resultierende Datensatz wird als bereinigt gekennzeichnet und enthält keine identifizierbaren Nutzerdaten. So wird die Parität mit der Gemini Enterprise Agent Platform-Funktion „Keine Datenaufbewahrung“ gewährleistet.
- **Fundierung mit der Google Suche**: Wie in den [Zusatzbedingungen für die Gemini API](https://ai.google.dev/gemini-api/terms?hl=de#grounding-with-google-search) beschrieben, speichert Google Prompts, Kontextinformationen und generierte Ausgaben 30 Tage lang, um fundierte Ergebnisse und Suchvorschläge zu erstellen.
  Diese gespeicherten Informationen können für das Debugging und Testen von Systemen verwendet werden, die die Fundierung unterstützen. **Die Speicherung dieser Informationen kann nicht deaktiviert werden, wenn Sie die Fundierung mit der Google Suche verwenden.**
- **Fundierung mit Google Maps**: Wie in den [Zusatzbedingungen für die Gemini API](https://ai.google.dev/gemini-api/terms?hl=de) beschrieben, speichert Google Prompts, Kontextinformationen und generierte Ausgaben 30 Tage lang, um fundierte Ergebnisse zu erstellen. Diese gespeicherten Informationen dürfen nur für die Zuverlässigkeitstechnik verwendet werden, z. B. für das Debugging bei Dienstproblemen.
  **Die Speicherung dieser Informationen kann nicht deaktiviert werden, wenn Sie die Fundierung mit Google Maps verwenden.**
- **Interactions API**: Die Interactions API verwaltet den aktiven Status einer
  Unterhaltung, um mehrere Gesprächsrunden zu ermöglichen. **Standardmäßig aktiviert die Interactions API die Statusspeicherung.** Um keine Daten zu hinterlassen, müssen Sie den Parameter `store` in Ihren API-Anfragen explizit auf `false` setzen, um die standardmäßige Statusaufbewahrung zu deaktivieren.
- **Live API**: Diese zustandsbehaftete API ermöglicht die Wiederverbindung in Echtzeit, indem der Unterhaltungsstatus gespeichert wird. Um keine Daten aufzubewahren, **konfigurieren Sie SessionResumptionConfig nicht**. Wenn ein Sitzungshandle generiert wird, wird der Unterhaltungsstatus (einschließlich Text, Audio und Video) bis zu 24 Stunden lang aufbewahrt.
- **File API Storage**: Mit der File API können Nutzer große Assets hochladen.
  Dateien werden im Ruhezustand gespeichert, bis sie vom Nutzer gelöscht werden oder ablaufen.
  Die Nutzung der File API ist unabhängig von der ZDR-Protokollierung. Nutzer müssen Dateien manuell löschen, um keine Daten zu hinterlassen.
- **Explizites Kontext-Caching**: Nutzer können große Datensätze (z.B.
  lange Videos oder Dokumentbibliotheken) manuell mit dem `cached_content` Feld im Cache speichern. Die Protokolle dieser Anfragen folgen zwar den ZDR-Löschrichtlinien, der zwischengespeicherte Kontext selbst wird jedoch mit einer nutzerdefinierten `ttl` oder `expire_time` gespeichert. Um absolut keine Daten zu hinterlassen, verwenden Sie die Funktion „cached\_content“ nicht.
- **Implizites In-Memory-Caching**: Standardmäßig speichern Gemini-Modelle Daten
  im Arbeitsspeicher, um die Latenz und die Kosten für Entwickler zu reduzieren. Diese Daten befinden sich ausschließlich im RAM (nicht im Ruhezustand), sind auf Projektebene isoliert und haben eine TTL von 24 Stunden.
  **Dies verstößt nicht gegen die Datenaufbewahrung.**

## Nächste Schritte

- Weitere Informationen zur Richtlinie zur unzulässigen Nutzung von [generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de)
- Die [Zusatzbedingungen für die Gemini API](https://ai.google.dev/gemini-api/terms?hl=de) lesen
- Wenn Sie erweiterte ZDR-Steuerelemente für Unternehmen benötigen, lesen Sie den [Leitfaden Keine Datenaufbewahrung für die Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/models/vertex-ai-zero-data-retention?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
