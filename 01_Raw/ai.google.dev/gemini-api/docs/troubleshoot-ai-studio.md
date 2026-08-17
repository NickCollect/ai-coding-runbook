---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=de
fetched_at: 2026-08-17T02:22:29.010306+00:00
title: "Fehlerbehebung bei Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Fehlerbehebung bei Google AI Studio

Auf dieser Seite finden Sie Vorschläge zur Fehlerbehebung in Google AI Studio, falls Probleme auftreten.

## Fehler vom Typ „403 Access Restricted“

Wenn Sie den Fehler „403 Access Restricted“ sehen, verwenden Sie Google AI Studio auf eine Weise, die nicht den [Nutzungsbedingungen](https://ai.google.dev/terms?hl=de) entspricht. Ein häufiger Grund ist, dass Sie sich nicht in einer [unterstützten Region](https://ai.google.dev/available_regions?hl=de) befinden.

## „Kein Inhalt“-Antworten in Google AI Studio beheben

In Google AI Studio wird die Meldung warning **Kein Inhalt** angezeigt, wenn der Inhalt aus irgendeinem Grund blockiert ist. Wenn Sie weitere Details sehen möchten, bewegen Sie den Mauszeiger auf **Keine Inhalte** und klicken Sie auf warning **Sicherheit**.

Wenn die Antwort aufgrund von [Sicherheitseinstellungen](https://ai.google.dev/docs/safety_setting?hl=de) blockiert wurde und Sie die [Sicherheitsrisiken](https://ai.google.dev/docs/safety_guidance?hl=de) für Ihren Anwendungsfall berücksichtigt haben, können Sie die [Sicherheitseinstellungen](https://ai.google.dev/docs/safety_setting?hl=de#safety_settings_in_makersuite) ändern, um die zurückgegebene Antwort zu beeinflussen.

Wenn die Antwort blockiert wurde, aber nicht aufgrund der Sicherheitseinstellungen, verstößt die Anfrage oder Antwort möglicherweise gegen die [Nutzungsbedingungen](https://ai.google.dev/terms?hl=de) oder wird anderweitig nicht unterstützt.

## Tokennutzung und ‑limits prüfen

Wenn Sie einen Prompt geöffnet haben, wird unten auf dem Bildschirm mit der Schaltfläche **Textvorschau** die aktuelle Anzahl der Tokens für den Inhalt Ihres Prompts und die maximale Anzahl der Tokens für das verwendete Modell angezeigt.

## Google Cloud IAM-Berechtigungen für AI Studio

Mitglieder eines Google Cloud-Projekts benötigen bestimmte IAM-Berechtigungen (Identity and Access Management), um Aktionen in Google AI Studio auszuführen. Weitere Informationen zu diesen Identitäten finden Sie in der [Übersicht über IAM-Hauptkonten](https://cloud.google.com/iam/docs/principals?hl=de).

Nutzer mit der Rolle **Bearbeiter** oder **Inhaber** im zugehörigen Google Cloud-Projekt haben die vollständigen Berechtigungen zum Aufrufen von Dashboards und zum Verwalten von Gemini API-Schlüsseln. Nutzer mit der Rolle **Betrachter** können Dashboards und API-Schlüssel ansehen, aber nicht erstellen, aktualisieren oder löschen.

Eine detailliertere Steuerung finden Sie in der folgenden Tabelle, in der die spezifischen Berechtigungen aufgeführt sind, die für die einzelnen AI Studio-Funktionen erforderlich sind. Eine Anleitung zum Zuweisen dieser Berechtigungen finden Sie in der Google Cloud-Dokumentation unter [Zugriff auf Ressourcen erteilen, ändern und entziehen](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=de).

| AI Studio-Funktion | Erforderliche IAM-Berechtigungen | Zusätzliche Anforderungen |
| --- | --- | --- |
| **Projekt suchen** (Projekte importieren) | `resourcemanager.projects.get` |  |
| **Projekt umbenennen** | `resourcemanager.projects.update` |  |
| **Kontingentstufe anzeigen** | – |  |
| **API-Schlüssel erstellen** | Sie haben die Berechtigung **Projekt durchsuchen** und:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **API-Schlüssel auflisten** | Sie haben die Berechtigung **Projekt durchsuchen** und:  `apikeys.keys.list` `serviceusage.services.get` | Für das Google Cloud-Projekt muss die [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=de) aktiviert sein. |
| **API-Schlüssel umbenennen** | `apikeys.keys.update` |  |
| **API-Schlüssel löschen** | `apikeys.keys.delete` |  |
| **Nutzungs-Dashboard** | Sie haben die Berechtigung **Projekt durchsuchen** und:  `monitoring.timeSeries.list` |  |
| **Dashboard für Ratenbegrenzungen** | Sie haben Berechtigungen für das **Dashboard zur Nutzung** und:  `cloudquotas.quotas.get` |  |
| **Ausgaben (Abrechnungsobergrenze)** | `billing.resourceCosts.get` (Ausgaben ansehen) `billing.resourcebudgets.read` (Obergrenze ansehen) `billing.resourcebudgets.write` (Obergrenze festlegen) |  |
| **Abrechnungsdashboard** | `billing.accounts.get` |  |

### Andere Zugriffsprüfungen

Zusätzlich zu Google Cloud IAM-Berechtigungen werden in AI Studio auch Sicherheits- und Compliance-Prüfungen durchgeführt. Wenn Sie die folgenden Anforderungen nicht erfüllen, kann es sein, dass in der AI Studio-Benutzeroberfläche oder in API-Antworten ein `PERMISSION_DENIED`-Fehler oder ein Fehler aufgrund von Zugriffsbeschränkungen angezeigt wird:

- **Sicherheitsprüfungen**:Ihre Anfrage muss automatisierte Sicherheitsprüfungen bestehen.
- **Nutzungsbedingungen**:Sie müssen die Google-Nutzungsbedingungen und die Zusatzbedingungen für generative KI akzeptieren.
- **Unterstützte Region**:Sie müssen sich in einer [unterstützten Region](https://ai.google.dev/gemini-api/docs/available-regions?hl=de) befinden.
- **Vertrauen und Sicherheit**:Das Google Cloud-Projekt darf nicht als missbräuchlich gekennzeichnet sein.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-29 (UTC)."],[],[]]
