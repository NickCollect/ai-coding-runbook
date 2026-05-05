---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=de
fetched_at: 2026-05-05T19:49:59.539537+00:00
title: "Datenerfassung und \u2011freigabe \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Datenerfassung und ‑freigabe

Auf dieser Seite werden die Speicherung und Verwaltung von
[Gemini API-Logs](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) beschrieben. Dabei handelt es sich um API-Daten von Entwicklern aus unterstützten Gemini API-Aufrufen für Projekte mit aktivierter Abrechnung. Logs umfassen den gesamten Prozess von der Anfrage eines Nutzers bis zur Antwort des Modells.

## 1. Daten, die freigegeben werden können

Als Projektinhaber haben Sie die Möglichkeit, das Logging von Gemini API-Aufrufen zu aktivieren. Sie können die Logs für eigene Zwecke verwenden oder Google Feedback geben und die Logs mit Google teilen, damit wir unsere Modelle kontinuierlich verbessern können.

Wenn das Logging aktiviert ist, können Sie uns helfen, KI-Systeme zu entwickeln, die für Entwickler in verschiedenen Bereichen und Anwendungsfällen weiterhin wertvoll sind. Dazu können Sie die folgenden Daten zur Produktverbesserung und zum Modelltraining beitragen:

- **Datasets**:Über die Benutzeroberfläche „Logs und Datasets“ von Google AI Studio können Sie Logs (Anfragen, Antworten, Metadaten usw.) aus unterstützten Gemini API-Aufrufen auswählen. Diese werden durch die Aufnahme in Datasets beigetragen. Sie haben die Möglichkeit, die Teilnahme bei der Dataset-Erstellung abzulehnen.
- **Feedback**:Wenn Sie Logs überprüfen, können Sie Feedback geben, z. B. mit „Mag ich“/„Mag ich nicht“-Bewertungen und schriftlichen Kommentaren.

Wenn Sie ein Dataset mit Google teilen, werden Ihre Logs in diesem Dataset, einschließlich
Anfragen und Antworten, gemäß unseren
[Nutzungsbedingungen](https://developers.google.com/terms?hl=de) für
„[Kostenlose Dienste](https://ai.google.dev/gemini-api/terms?hl=de#data-use-unpaid)“
verarbeitet. Das Dataset kann also verwendet werden, um Google
Produkte, ‑Dienste und Technologien für maschinelles Lernen zu entwickeln und zu verbessern, einschließlich der Verbesserung und des
Trainings unserer Modelle. **Geben Sie keine personenbezogenen oder vertraulichen Informationen an.**

## 2. So verwenden wir Ihre Daten

Standardmäßig laufen Logs nach 55 Tagen ab. Nach diesem Zeitraum sind sie nicht mehr verfügbar. Datasets können erstellt werden, um Logs, die über diesen Zeitraum hinaus von Interesse oder Wert sind, für nachgelagerte Anwendungsfälle aufzubewahren und optional zur Verbesserung von Modellen beizutragen. Für Logs, die in Datasets gespeichert sind,gibt es keine festgelegten Ablaufdaten. Für jedes Projekt gilt jedoch ein Standardspeicherlimit von bis zu 1.000 Logs.

Standardmäßig werden Prompts und Antworten in Logs nicht zur Produktverbesserung oder
‑entwicklung verwendet, da das Logging nur für Projekte mit aktivierter Abrechnung verfügbar ist. Dies entspricht unseren [Nutzungsbedingungen](https://developers.google.com/terms?hl=de)
zur Datennutzung.

Wenn Sie Datasets Ihrer Logs mit Google teilen, werden diese Datasets als Demonstrationsdaten aus der Praxis verwendet, um die Vielfalt der Bereiche und Kontexte besser zu verstehen, in denen KI-Systeme und ‑Anwendungen eingesetzt werden. Diese Daten können verwendet werden, um die Modellqualität zu verbessern und das Training und die Bewertung zukünftiger Modelle und Dienste zu unterstützen. Diese Daten werden gemäß unseren Nutzungsbedingungen für die Datennutzung für [kostenlose Dienste](https://ai.google.dev/gemini-api/terms?hl=de#data-use-unpaid) verarbeitet.
Dementsprechend können Prüfer die von Ihnen freigegebenen API-Eingaben und ‑Ausgaben lesen, mit Anmerkungen versehen und verarbeiten. Bevor Daten zur Modellverbesserung verwendet werden, ergreift Google im Rahmen dieses Prozesses Maßnahmen, um die Privatsphäre der Nutzer zu schützen. Dazu wird unter anderem dafür gesorgt, dass entsprechende Daten nicht mit Ihrem Google-Konto, API-Schlüssel und Cloud-Projekt in Verbindung gebracht werden können, bevor sie von Prüfern eingesehen oder mit Vermerken versehen werden.

## 3. Datenberechtigungen

Wenn Sie API-Daten beitragen, bestätigen Sie, dass Sie die erforderlichen Berechtigungen haben, damit Google die Daten wie in dieser Dokumentation beschrieben verarbeiten und verwenden kann. **Bitte tragen Sie keine Logs bei, die sensible, vertrauliche oder geschützte Informationen enthalten, die über den kostenpflichtigen Dienst erhalten wurden.**
Die Befugnis, die Sie Google unter dem Abschnitt „[Einreichung von Inhalten](https://developers.google.com/terms?hl=de#b_submission_of_content)“ der API-Bedingungen erteilen, erstreckt sich auch auf alle Inhalte (z.B. Prompts, einschließlich zugehöriger Systemanweisungen, im Cache gespeicherter Inhalte und Dateien wie Bilder, Videos oder Dokumente), die Sie an die Dienste senden, und auf alle generierten Antworten, soweit dies nach geltendem Recht für deren Nutzung durch uns erforderlich ist.

## 4. Datenfreigabe und Feedback

Sie können uns helfen, die KI-Forschung, die Gemini API und Google AI Studio weiterzuentwickeln, indem Sie Ihre Daten als Beispiele freigeben. So können wir unsere Modelle in verschiedenen Kontexten kontinuierlich verbessern und KI-Systeme entwickeln, die für Entwickler in verschiedenen Bereichen und Anwendungsfällen weiterhin wertvoll sind.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
