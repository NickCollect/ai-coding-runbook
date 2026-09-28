---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=de
fetched_at: 2026-09-28T06:32:16.308544+00:00
title: "Ratenlimits \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Ratenlimits

Ratenlimits regeln die Anzahl der Anfragen, die Sie innerhalb eines bestimmten Zeitraums an die Gemini API senden können. Diese Limits tragen dazu bei, dass die Nutzung fair bleibt, schützen vor Missbrauch und sorgen dafür, dass die Systemleistung für alle Nutzer erhalten bleibt.

[Aktive Ratenbeschränkungen in AI Studio ansehen](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=de)

## So funktionieren Ratenbegrenzungen

Ratenbegrenzungen werden in der Regel anhand von drei Dimensionen gemessen:

- Anfragen pro Minute (**RPM**)
- Tokens pro Minute (Eingabe) (**TPM**)
- Anfragen pro Tag (**RPD**)

Ihre Nutzung wird anhand der einzelnen Limits bewertet. Wenn Sie eines der Limits überschreiten, wird ein Ratenbegrenzungsfehler ausgelöst. Wenn Ihr RPM-Limit beispielsweise 20 beträgt, führt das Senden von 21 Anfragen innerhalb einer Minute zu einem Fehler, auch wenn Sie Ihr TPM- oder andere Limits nicht überschritten haben.

Ratenbegrenzungen gelten pro Projekt, nicht pro API-Schlüssel. Kontingente für **RPD** werden um Mitternacht (Pacific Time) zurückgesetzt.

Die Limits variieren je nach verwendetem Modell. Einige Limits gelten nur für bestimmte Modelle. „Bilder pro Minute“ (Images per minute, IPM) wird beispielsweise nur für Modelle berechnet, die Bilder generieren können (Nano Banana), ist aber konzeptionell ähnlich wie TPM. Bei anderen Modellen gilt möglicherweise ein Tokenlimit pro Tag.

Die Ratenbegrenzungen für experimentelle Modelle und Vorschauversionen sind strenger.

### Ausgabenbasierte Ratenlimits

Zusätzlich zu den Limits für Anfragen pro Minute (RPM) und Tokens pro Minute (TPM) erzwingt die Gemini API ausgabenbasierte Ratenbegrenzungen, um vor unerwarteten Gebühren zu schützen. Ob diese Limits für Ihr Konto gelten, hängt von Ihrem Abrechnungsverlauf und Ihrer [Nutzungsstufe](#usage-tiers) ab.

In der folgenden Tabelle sind die ausgabenbasierten Ratenlimits für die einzelnen [Nutzungsstufen](#usage-tiers) aufgeführt. Diese Limits werden in einem gleitenden 10‑Minuten-Zeitraum ausgewertet. Ob diese Limits für Ihr Konto gelten, hängt von Ihrem Abrechnungsverlauf und dem Status Ihres Kontos ab.

| Nutzungsstufe | Ausgabenratenlimit (pro 10 Minuten) |
| --- | --- |
| **Kostenlos** | – |
| **Stufe 1** | 10 $ |
| **Tier 2** | 200 $ |
| **Stufe 3** | 200 $ |

Wenn Sie eine ausgabenbasierte Ratenbegrenzung erreichen, gibt die API einen `429 RESOURCE_EXHAUSTED`-Fehler zurück. So beheben Sie dies:

- **Warten Sie kurz und versuchen Sie es dann noch einmal.**
- **Reduzieren Sie die Rate teurer Anfragen**, indem Sie beispielsweise kleinere Kontextfenster oder kürzere Ausgaben verwenden.
- Wenn Sie dieses Limit bei normaler Nutzung regelmäßig erreichen, [beantragen Sie eine Erhöhung des Ratenlimits](#request-rate-limit-increase).

## Nutzungsstufen

Ratenbegrenzungen sind an die Nutzungsebene des Projekts gebunden. Wenn Ihre API-Nutzung und Ihre Ausgaben steigen, werden Sie automatisch auf eine höhere Stufe mit höheren Ratenbegrenzungen hochgestuft.

Die Voraussetzungen für die Stufen 2 und 3 basieren auf den kumulativen Gesamtausgaben für Google Cloud-Dienste (einschließlich, aber nicht beschränkt auf die Gemini API) für das mit Ihrem Projekt verknüpfte Abrechnungskonto.

| Nutzungsstufe | Qualifikation | [Obergrenze für Abrechnungsstufe](https://ai.google.dev/gemini-api/docs/billing?hl=de#tier-spend-caps) |
| --- | --- | --- |
| **Kostenlos** | [Aktives Projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects) oder kostenloser Testzeitraum | – |
| **Stufe 1** | [Aktives Rechnungskonto einrichten und verknüpfen](https://ai.google.dev/gemini-api/docs/billing?hl=de#setup-billing) | 250 $ |
| **Tier 2** | 100 $ + 3 Tage seit erster eingegangener Zahlung | 2.000 $ |
| **Stufe 3** | 1.000 $ bezahlt + 30 Tage seit erster erfolgreicher Zahlung | 20.000 $ bis 100.000 $ und mehr |

Die Erfüllung der angegebenen Qualifikationskriterien reicht in der Regel für die Genehmigung aus. In seltenen Fällen kann ein Antrag auf Upgrade jedoch aufgrund anderer Faktoren abgelehnt werden, die während der Überprüfung festgestellt wurden.

Dieses System trägt dazu bei, die Sicherheit und Integrität der Gemini API-Plattform für alle Nutzer aufrechtzuerhalten.

## Ratenbegrenzungen für die Gemini API

Ratenbeschränkungen hängen von verschiedenen Faktoren ab, z. B. von Ihrer Nutzungsstufe, und können in Google AI Studio eingesehen werden. Ihre Ratenbeschränkungen werden automatisch aktualisiert, wenn sich Ihr Tier und Ihr Kontostatus im Laufe der Zeit ändern.

[Aktive Ratenbeschränkungen in AI Studio ansehen](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=de)

Die angegebenen Ratenlimits sind nicht garantiert und die tatsächliche Kapazität kann variieren.

## Ratenlimits für Prioritätsinferenz

Für die Nutzung von [Priorität](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) gelten eigene Ratenbeschränkungen, auch wenn die Nutzung auf die Ratenbeschränkungen für den gesamten interaktiven Traffic angerechnet wird. **Die Standardratenbegrenzungen sind: 0,3-mal die [Standardratenbegrenzung](https://aistudio.google.com/rate-limit?hl=de) für jedes Modell und jede Stufe**

## Ratenlimits für die Batch API

Für [Batch-API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)-Anfragen gelten eigene Ratenbegrenzungen, die sich von denen für Nicht-Batch-API-Aufrufe unterscheiden.

- **Gleichzeitige Batchanfragen**:100
- **Maximale Größe der Eingabedatei**:2 GB
- **Dateispeicherlimit**:20 GB
- **In die Warteschlange gestellte Tokens pro Modell**:In der Tabelle **In die Warteschlange gestellte Batch-Tokens** wird die maximale Anzahl von Tokens aufgeführt, die für die Batchverarbeitung für alle Ihre aktiven Batchjobs für ein bestimmtes Modell in die Warteschlange gestellt werden können.

### Preisstufe 1

| Modell | In die Warteschlange gestellte Batch-Tokens |
| --- | --- |
| Textausgabemodelle | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Vorabversion) | 5.000.000 |
| Gemini 3.5 Flash-Lite | 10.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.1 Flash Lite (Vorabversion) | 10.000.000 |
| Gemini 3.6 Flash | 3.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Gemini 2.5 Flash (Vorabversion) | 3.000.000 |
| Gemini 2.5 Flash Image (Vorabversion) | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 10.000.000 |
| Gemini 2.5 Flash Lite (Vorabversion) | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Gemini 2.0 Flash Image | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Multimodale generative Modelle | | | | |
| Gemini 3.1 Flash Image (Vorabversion) 🍌 | 1.000.000 |
| Gemini 3.1 Flash Lite-Image 🍌 | 2.000.000 |
| Gemini 3 Pro Image (Vorabversion) 🍌 | 2.000.000 |
| Einbettungsmodelle | | | | |
| Gemini Embedding | 500.000 |

### Preisstufe 2

| Modell | In die Warteschlange gestellte Batch-Tokens |
| --- | --- |
| Textausgabemodelle | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Vorabversion) | 500.000.000 |
| Gemini 3.5 Flash-Lite | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.1 Flash Lite (Vorabversion) | 500.000.000 |
| Gemini 3.6 Flash | 400.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Gemini 2.5 Flash (Vorabversion) | 400.000.000 |
| Gemini 2.5 Flash Image (Vorabversion) | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 500.000.000 |
| Gemini 2.5 Flash Lite (Vorabversion) | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Image | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Multimodale generative Modelle | | | | |
| Gemini 3.1 Flash Image (Vorabversion) 🍌 | 250.000.000 |
| Gemini 3.1 Flash Lite-Image 🍌 | 270.000.000 |
| Gemini 3 Pro Image (Vorabversion) 🍌 | 270.000.000 |
| Einbettungsmodelle | | | | |
| Gemini Embedding | 5.000.000 |

### Ebene 3

| Modell | In die Warteschlange gestellte Batch-Tokens |
| --- | --- |
| Textausgabemodelle | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Vorabversion) | 1.000.000.000 |
| Gemini 3.5 Flash-Lite | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.1 Flash Lite (Vorabversion) | 1.000.000.000 |
| Gemini 3.6 Flash | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Gemini 2.5 Flash (Vorabversion) | 1.000.000.000 |
| Gemini 2.5 Flash Image (Vorabversion) | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash Lite | 1.000.000.000 |
| Gemini 2.5 Flash Lite (Vorabversion) | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Gemini 2.0 Flash Image | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Multimodale generative Modelle | | | | |
| Gemini 3.1 Flash Image (Vorabversion) 🍌 | 750.000.000 |
| Gemini 3.1 Flash Lite-Image 🍌 | 1.000.000.000 |
| Gemini 3 Pro Image (Vorabversion) 🍌 | 1.000.000.000 |
| Einbettungsmodelle | | | | |
| Gemini Embedding | 10.000.000 |

## So führst du ein Upgrade auf die nächste Stufe durch

Wenn Sie von der kostenlosen Stufe zu einer kostenpflichtigen Stufe wechseln möchten, müssen Sie zuerst [die Abrechnung in AI Studio einrichten](https://ai.google.dev/gemini-api/docs/billing?hl=de).

Sobald Ihr Projekt die [angegebenen Kriterien](#usage-tiers) erfüllt, wird es automatisch auf die nächste Stufe hochgestuft. Tier-Upgrades von der kostenlosen Stufe auf Tier 1 werden in der Regel sofort wirksam. Nachfolgende Tier-Upgrades werden innerhalb von 10 Minuten wirksam. Rufen Sie in AI Studio die [Seite „Projekte“](https://aistudio.google.com/projects?hl=de) auf, um Ihre Stufen zu prüfen.

## Erhöhung des Ratenlimits beantragen

Für jede Modellvariante gilt ein zugehöriges Ratenlimit (Anfragen pro Minute, RPM).
Weitere Informationen zu diesen Ratenlimits finden Sie auf der Seite [AI Studio-Ratenlimit](https://aistudio.google.com/rate-limit?hl=de).

[Erhöhung der Anfragenbeschränkung für kostenpflichtige Stufe beantragen](https://forms.gle/ETzX94k8jf7iSotH9)

Wir können nicht garantieren, dass Ihr Ratenlimit erhöht wird, werden aber unser Bestes tun, um Ihre Anfrage zu prüfen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
