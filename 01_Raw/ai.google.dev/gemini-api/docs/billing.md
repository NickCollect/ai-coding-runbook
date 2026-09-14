---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=de
fetched_at: 2026-09-14T05:43:07.310425+00:00
title: "Abrechnung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Abrechnung

In diesem Leitfaden finden Sie einen Überblick über die verschiedenen Abrechnungsoptionen für die Gemini API. Außerdem wird erläutert, wie Sie die Abrechnung aktivieren und die Nutzung im Blick behalten können. Darüber hinaus werden häufig gestellte Fragen zur Abrechnung beantwortet.

## Abrechnung und Stufen

Die Abrechnung für die Gemini API basiert auf Ihrem Zahlungsverlauf.

| Nutzungsstufe | Qualifikation | [Obergrenze für Abrechnungsstufe](#spend-caps) |
| --- | --- | --- |
| **Kostenlos** | [Aktives Projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects) oder kostenloser Testzeitraum | – |
| **Stufe 1** | [Aktives Rechnungskonto einrichten und verknüpfen](#setup-billing) | 250 $ |
| **Tier 2** | 100 $ + 3 Tage seit erster eingegangener Zahlung | 2.000 $ |
| **Stufe 3** | 1.000 $ bezahlt + 30 Tage seit erster erfolgreicher Zahlung | 20.000 $ bis 100.000 $ und mehr |

Neue Konten beginnen mit der Kostenlosen Stufe, die den Zugriff auf [bestimmte Modelle](https://ai.google.dev/gemini-api/docs/pricing?hl=de) in der Gemini API und AI Studio ermöglicht, bis zu den [Ratenbeschränkungen](https://aistudio.google.com/rate-limit?hl=de) der Kostenlosen Stufe der Modelle.

Wenn Sie Ihre Anwendungen direkt über den Build-Modus bereitstellen möchten, können Sie die **Google Cloud-Starter-Stufe** verwenden. Mit dieser Stufe können Sie bis zu zwei Full-Stack-Anwendungen veröffentlichen, ohne ein Google Cloud-Projekt oder ein Rechnungskonto einzurichten.
Weitere Informationen finden Sie unter [Über Google AI Studio bereitstellen](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=de) und in der [Dokumentation zum Google Cloud-Starter-Tier](https://docs.cloud.google.com/docs/starter-tier?hl=de).

Wenn Sie auf höhere Ratenbegrenzungen zugreifen, erweiterte Modelle verwenden und dafür sorgen möchten, dass Ihre Prompts und Antworten **nicht** zur Verbesserung von Google-Produkten verwendet werden\*, können Sie [ein Rechnungskonto verknüpfen](#setup-billing) und [Vorauszahlung](#prepay), um zu den kostenpflichtigen Stufen zu wechseln.
Anschließend steigen Sie basierend auf den kumulativen Ausgaben und dem Kontoalter in höhere Stufen auf.

Stufen, Ratenbeschränkungen und Abrechnungskontolimits werden alle auf [Rechnungskontoebene](#cloud-billing) festgelegt.

\* *Datenschutz auf Unternehmensniveau: Weitere Informationen zur Datennutzung für kostenpflichtige Dienste finden Sie in den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de#data-use-paid).*

## Abrechnung einrichten, um auf das kostenpflichtige Abo zuzugreifen

Sie können ein Projekt erstellen und die Abrechnung einrichten oder ein vorhandenes Projekt importieren, um in [Google AI Studio](https://aistudio.google.com/projects?hl=de) ein Upgrade auf die kostenpflichtige Version durchzuführen.
Wenn Sie von der kostenlosen Stufe auf die kostenpflichtige Stufe upgraden, müssen Sie ein Rechnungskonto verknüpfen und [Vorauszahlungen](#prepay) leisten, um Ihrem Konto ein Guthaben von mindestens 5 $ (oder dem entsprechenden Betrag in anderen Währungen) hinzuzufügen.

1. Rufen Sie in AI Studio die Seite [API-Schlüssel](https://aistudio.google.com/api-keys?hl=de), die Seite [Projekte](https://aistudio.google.com/projects?hl=de) oder eine andere Seite auf, auf der die Schaltfläche **Abrechnung einrichten** angezeigt wird.
   - Für neue Nutzer werden standardmäßig ein [Projekt und ein API-Schlüssel](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects) erstellt.
   - Wenn Sie einen neuen Schlüssel benötigen, klicken Sie auf [**API-Schlüssel erstellen**](https://aistudio.google.com/api-keys?hl=de) und folgen Sie dem Dialogfeld, um der Tabelle ein Schlüssel-Projekt-Paar hinzuzufügen.
2. Suchen Sie das Kostenlose Stufe-Projekt, das Sie auf das Paid Tier upgraden möchten, und klicken Sie in der Spalte *Billing Tier* (Abrechnungsstufe) auf **Set up billing** (Abrechnung einrichten).
3. Wenn Sie noch nie ein Google-Rechnungskonto eingerichtet haben:
   - Sie werden aufgefordert, Ihr Land auszuwählen, um den Nutzungsbedingungen zuzustimmen.
   - Geben Sie dann Ihre Kontaktdaten und Zahlungsmethode ein oder bestätigen Sie sie, um fortzufahren.
4. Wenn Sie in der Vergangenheit Google-Rechnungskonten eingerichtet haben:
   - Sie werden aufgefordert, eines Ihrer bestehenden Rechnungskonten auszuwählen.
   - Wenn Sie keines Ihrer bestehenden Konten verwenden möchten, klicken Sie auf **Neues Abrechnungskonto hinzufügen** und geben Sie Ihre Kontaktinformationen und Zahlungsmethode ein oder bestätigen Sie sie, um fortzufahren.
5. Als Nächstes haben Sie folgende Möglichkeiten:
   - Sie werden aufgefordert, eine Vorauszahlung von mindestens 5 $ zu leisten, um die Abrechnung einzurichten. Das bedeutet, dass Ihrem Konto automatisch der Abrechnungsplan [Vorauszahlung](#prepay) zugewiesen wird.
   - Sie haben die Wahl zwischen den Abrechnungsmodellen [Vorauszahlung](#prepay) und [Nachträgliche Zahlung](#postpay) für Ihr Konto.
   - Für einen Übergangszeitraum bis zur Einführung des neuen Prepay-Systems für alle Nutzer (ab dem 23. März 2026) wird ein [Postpay](#postpay)-Abrechnungsmodell zugewiesen.
6. Nachdem Sie eine Vorauszahlung geleistet oder die nachträgliche Zahlung ausgewählt haben, ist die Kontoeinrichtung abgeschlossen.

### Upgrade auf die nächste kostenpflichtige Stufe durchführen

Wenn Sie bereits ein kostenpflichtiges Abo haben und die [Kriterien](#about-billing) für eine Aboänderung erfüllen, werden Sie automatisch auf das nächste Abo hochgestuft (vorbehaltlich der [Verarbeitungszeiten](#processing-times)).

## Abrechnungsstatus prüfen

Nachdem Sie ein [Rechnungskonto mit Ihrem Projekt verknüpft](#setup-billing) haben, können Sie den Status auf der [Abrechnungsseite für AI Studio](https://aistudio.google.com/billing?hl=de) einsehen. Im Gegensatz zur kostenlosen Stufe ist der Status der kostenpflichtigen Stufe dynamisch. Ihre Nutzungsstufe wird zwar durch Ihren Konto-Verlauf bestimmt, die Gemini API verarbeitet Anfragen jedoch nur, wenn Sie ein positives [Prepay](#prepay)-Guthaben haben.

Auf der Seite [Projekte](https://aistudio.google.com/projects?hl=de) können Sie in der Spalte *Abrechnungsstufe* die Stufe und den Abrechnungsplan Ihres Projekts sehen. Alle Abrechnungsstatusaktionen, die Sie für ein Projekt ausführen müssen, werden in den Spalten *Abrechnungsstufe* oder *Status* angezeigt:

- ***Abrechnung einrichten***, wenn dem Projekt kein Rechnungskonto zugewiesen ist.
- ***Vorauszahlung einrichten***: Das Projekt hat ein verknüpftes Rechnungskonto, muss aber ein [Vorauszahlungsmodell](#prepay) verwenden, das eingerichtet werden muss.
- ***Keine Guthabenpunkte***: Das Rechnungskonto ist erforderlich, um Guthabenpunkte zu kaufen, aber das Zahlungskonto für Vorauszahlungen ist nicht eingerichtet oder das verfügbare Guthaben ist aufgebraucht.

Klicken Sie auf eine der Meldungen, um die erforderlichen Maßnahmen zu ergreifen.

## Nutzung überwachen

Sie können Ihre Nutzung der Gemini API in [Google AI Studio](https://aistudio.google.com/usage?hl=de) unter **Dashboard** > **Nutzung** überwachen.

## Abrechnungsoptionen

Abrechnungsmodelle für die Gemini API und AI Studio fallen in zwei Kategorien, die bestimmen, wann Sie für die Nutzung bezahlen: Vorauszahlung und Nachträgliche Zahlung. Auf der Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) können Sie Ihren zugewiesenen Abrechnungsplan einsehen und Zahlungsmethoden verwalten.

### Vorauszahlung

Beim Prepaid-Abrechnungsmodell kaufen Sie Guthaben für Ihr Prepaidguthaben im Voraus für die Nutzung der Gemini API. Die Kosten für die API-Nutzung werden [in Echtzeit](#processing-times) von Ihrem Prepaidguthaben abgezogen.
Sie können im Voraus bezahlen, indem Sie [Guthaben auf Ihr Konto einzahlen](#buy-credits) oder [das automatische Aufladen einrichten](#auto-reload). Nach dem Kauf von Guthabenpunkten verfallen nicht verwendete Guthabenpunkte nach 12 Monaten und sind [nicht erstattungsfähig](#refunds), außer nach dem [Wechsel zu einem Postpay-Konto](#postpay).

Wenn das Guthaben auf dem Rechnungskonto 0 $ erreicht, funktionieren alle API-Schlüssel in allen Projekten, die mit diesem Rechnungskonto verknüpft sind, nicht mehr.
Vorauszahlungsguthaben gilt nur für die Nutzungskosten der Gemini API. Sie können damit nicht für andere Google Cloud-Dienste bezahlen.

Für neue Nutzer wird standardmäßig das Preismodell mit Vorauszahlung verwendet. Bei Projekten, die vor der Einführung von Preismodellen mit Vorauszahlung und Nachträglicher Zahlung erstellt wurden, müssen möglicherweise die [Abrechnungsdetails des Projekts aktualisiert](#verify-billing) werden, bevor die Gemini API weiterhin verwendet werden kann.

*Hinweis: Die Vorauszahlung ist für [Konten mit Rechnungsstellung (Offlinekonten)](https://docs.cloud.google.com/billing/docs/concepts?hl=de#billing_account_types)
nicht verfügbar.*

#### Einem bestehenden Konto mit nachträglicher Zahlung ein Konto mit Vorauszahlung hinzufügen

Wenn für Ihr bestehendes Cloud-Rechnungskonto ein **Postpay**-Tarif verwendet wird, können Sie **Prepay**-Funktionen hinzufügen, um Guthaben im Voraus zu kaufen. Mit diesem Guthaben können Sie die Gemini API nutzen, ohne ein neues Cloud-Rechnungskonto zu erstellen.

Wenn Sie die Zahlungseinstellung **Vorauszahlung** einem bestehenden Konto hinzufügen, wird ein obligatorischer Bestätigungsbildschirm angezeigt, auf dem erläutert wird, dass das ausgewählte Cloud-Rechnungskonto geändert wird.

Der Kontostatus muss vom System geändert werden, *bevor* Sie die Vorauszahlung einreichen.
Wenn Sie den Vorgang also nach der Bestätigung der Änderung, aber vor Abschluss der Einrichtung der Vorauszahlung abbrechen, kann es zu vorübergehenden Dienstunterbrechungen für Projekte kommen, die bereits mit diesem Cloud-Rechnungskonto verknüpft sind. Stellen Sie sicher, dass Sie bereit sind, die Vorauszahlung abzuschließen, bevor Sie die Umstellung bestätigen. Bei Problemen lesen Sie den Hilfeartikel [Dienste werden nach dem Abbrechen einer **Vorauszahlung** unterbrochen](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de#prepay-issue).

Wenn Sie berechtigt sind und manuell von einem **Prepay**-Abrechnungszeitraum zu einem **Postpay**-Abrechnungszeitraum wechseln, wird ein verbleibendes Guthaben automatisch über die ursprüngliche Zahlungsmethode erstattet, die für die Vorauszahlung verwendet wurde. Wenn Sie Ihr Cloud-Rechnungskonto jedoch aus einem anderen Grund schließen, verfällt das verbleibende Guthaben und wird nicht erstattet.

#### Guthabenpunkte erwerben

Sie können Guthaben manuell im Voraus kaufen, bevor Sie die Gemini API nutzen, um es in Ihr Prepaid-Konto einzuzahlen.

Wenn Sie Guthaben kaufen möchten, rufen Sie die Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) auf und wählen Sie **Guthaben kaufen** aus.
Der Mindestkaufbetrag beträgt 5 $. Sie können maximal 5.000 $ im Voraus bezahlen.

#### Automatische Aktualisierung

Das automatische Aufladen ist eine optionale Funktion, mit der Ihr Prepaid-Guthaben automatisch aufgeladen wird, wenn es fast aufgebraucht ist. Das ist nützlich, um Dienstunterbrechungen zu vermeiden.

Sie können das automatische Aufladen einrichten und den Status des automatischen Aufladens auf der Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) auf der Karte *Verfügbare Guthabenpunkte* einsehen. Klicken Sie auf **Automatisches Aufladen einrichten** oder **Automatisches Aufladen verwalten**, um Ihre Zahlungsmethode, den Aufladebetrag und den Mindestguthabenstand festzulegen, bei dem eine Aufladezahlung ausgelöst wird.

#### Monatliches Limit für automatisches Aufladen

Das monatliche Limit für das automatische Aufladen ist für Nutzer mit Vorauszahlung verfügbar und hilft, unerwartete Kosten durch häufige automatische Guthabenaufladungen zu vermeiden.
Mit dieser Funktion können Sie ein maximales Limit für automatische Guthabenaufladungen innerhalb eines einzelnen Abrechnungszeitraums festlegen. Sobald der Gesamtbetrag der automatischen Aufladungen in einem Abrechnungszeitraum dieses Limit erreicht, wird die automatische Aufladung bis zum Beginn des nächsten Monats deaktiviert. Einmalzahlungen, die Sie manuell veranlassen, werden nicht auf dieses Limit angerechnet.

So legen Sie das monatliche Limit für die automatische Aufladung fest, wenn das automatische Aufladen aktiviert ist:

1. Rufen Sie die Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) auf.
2. Klicken Sie auf **Automatisches Aufladen verwalten**.
3. Maximieren Sie den Bereich **Monatliches Limit** und geben Sie das maximale monatliche Limit für das automatische Aufladen ein.
4. Klicken Sie auf **Speichern**.

### Nachträgliche Zahlung

Beim Abrechnungsmodell mit nachträglicher Zahlung fallen auf Ihrem Cloud-Rechnungskonto Kosten an. Sie werden automatisch am Monatsende oder wenn Ihre Kosten einen [automatisch zugewiesenen Ausgabenlimit](#tier-spend-caps) basierend auf Ihrer Kontostufe erreichen, belastet.
Die Zahlung wird über die Zahlungsmethode abgerechnet, die mit Ihrem Postpay-Zahlungskonto verknüpft ist. Sie können sie auf der Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) verwalten. Auf der Seite **Rechnungs** können Sie Ihren Kontostand, Fälligkeitstermine und vergangene Zahlungen einsehen sowie Zahlungen vornehmen und Zahlungsmethoden verwalten.

Wenn Sie [die Abrechnung für ein neues Projekt einrichten](#setup-billing) und die Voraussetzungen für die nachträgliche Zahlung erfüllen, können Sie im Dialogfeld [Abrechnungseinrichtung](#setup-billing) zwischen Vorauszahlung und nachträglicher Zahlung wählen.

Sobald Sie ein Cloud-Abrechnungskonto auf den Postpay-Abrechnungsplan umgestellt haben, werden alle mit diesem Abrechnungskonto verknüpften Projekte auf den Postpay-Plan umgestellt. Sie können ein berechtigtes Konto auf Vorauszahlung umstellen, indem Sie der Anleitung unter [Auf Vorauszahlung umstellen](#migrate-to-prepay) folgen. Sie können ein Projekt auch in ein Rechnungskonto mit einem anderen Abrechnungsmodell verschieben, um den Abrechnungszyklus für dieses Projekt zu ändern. Weitere Informationen finden Sie in der Cloud-Dokumentation unter [Abrechnung für Projekte verwalten](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de).

Weitere Informationen zum Abrechnungszeitraum für die nachträgliche Zahlung finden Sie im [Cloud Billing-Leitfaden](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=de).

### Auf Vorauszahlung umstellen

Google AI Studio stellt die Abrechnung für die Nutzung der Gemini API für Entwicklerkonten von Postpaid auf Prepaid um. Diese Änderung gilt nur für die Gemini API. Für andere Google Cloud-Dienste, die mit Ihrem Rechnungskonto verknüpft sind, gilt weiterhin die Nachzahlung.

Stellen Sie auf Vorauszahlung um und fügen Sie Guthaben hinzu, bevor das Umstellungsdatum in Ihrer Kontobenachrichtigung erreicht ist, um Dienstunterbrechungen zu vermeiden. Für Konten, in denen nur Funktionen der kostenlosen Stufe verwendet werden, sind keine Maßnahmen erforderlich.

So stellen Sie ein vorhandenes Konto mit nachträglicher Zahlung auf Vorauszahlung um:

1. Rufen Sie die Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) auf.
2. Wählen Sie für Ihr Rechnungskonto **Auf Vorauszahlung umstellen** aus.
3. [Guthabenpunkte kaufen](#buy-credits) (mindestens 5 $), um Ihr Startguthaben aufzuladen.

Um Dienstunterbrechungen nach dem Wechsel zu vermeiden, konfigurieren Sie das [automatische Aufladen](#auto-reload), damit Ihr Guthaben automatisch aufgeladen wird, wenn es niedrig ist.

## Ausgabenobergrenzen

Die Gemini API unterstützt monatliche Ausgabenlimits sowohl auf Rechnungskonto- als auch auf Projektebene. Diese Kontrollen sollen Ihr Konto vor unerwarteten Überschreitungen und das Ökosystem vor Beeinträchtigungen der Dienstverfügbarkeit schützen.

*Ausgabenobergrenzen sind nicht für [Konten mit Rechnungsstellung (Offlinekonten)](https://docs.cloud.google.com/billing/docs/concepts?hl=de#billing_account_types) verfügbar.*

### Ausgabenobergrenzen für Projekte

Sie können in AI Studio eigene [Ausgabenlimits auf Projektebene](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects) festlegen.
Das ist nützlich, wenn Sie mehrere Projekte unter demselben Abrechnungskonto haben und sicherstellen möchten, dass jedes Projekt Zugriff auf einen ausreichenden Teil der kumulativen Ausgabengrenze hat.

Konten mit den [Rollen](https://docs.cloud.google.com/iam/docs/roles-overview?hl=de) „Projektbearbeiter“, „Inhaber“ oder „Administrator“ können in AI Studio auf der Seite [Ausgaben](https://aistudio.google.com/spend?hl=de) unter **Monatliches Ausgabenlimit** > **Ausgabenlimit bearbeiten** Ausgabenlimits pro Projekt festlegen.

Details zu den spezifischen Google Cloud IAM-Berechtigungen, die zum Aufrufen oder Bearbeiten von Ausgabenlimits und Abrechnungsinformationen in AI Studio erforderlich sind, finden Sie in der [Fehlerbehebung für AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=de#iam-permissions).

Wenn Sie ein [Projekt in ein anderes Rechnungskonto verschieben](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de#change_the_billing_account_for_a_project), bleibt das für dieses Projekt festgelegte Ausgabenlimit bestehen. Die angefallenen Ausgaben werden für den neuen Abrechnungszeitraum jedoch auf 0 $ zurückgesetzt.

Bei zeitaufwendigen Aufgaben wie [Batchmodus](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)-Vervollständigungen und Agentsitzungen können Überschreitungen des Ausgabenlimits Ihres Projekts anfallen.

Die Verarbeitungszeiten für Abrechnungsdaten können in AI Studio um bis zu 10 Minuten verzögert sein. Wenn Abrechnungsdaten nicht verarbeitet werden, bevor weitere Kosten anfallen, können Überschreitungen über das Projektlimit hinaus auftreten.

### Ausgabenobergrenzen für Rechnungskontostufen

Für jede [Stufe](#about-billing) gilt eine maximale monatliche Ausgabengrenze:

| Nutzungsstufe | Ausgabenobergrenze |
| --- | --- |
| **Kostenlos** | – |
| **Stufe 1** | 250 $ |
| **Tier 2** | 2.000 $ |
| **Stufe 3** | 20.000–100.000 $ |

Für die Gemini API gelten monatliche Nutzungslimits auf [Rechnungskontoebene](#cloud-billing). Die Standardlimits sind zwar voreingestellt, Sie können jedoch eine [Erhöhung beantragen](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=de), um eine höhere Nutzung zu ermöglichen. Die Gesamtausgaben werden für alle verknüpften Projekte mit aktiviertem Gemini API-Dienst zusammengefasst. Sobald die kumulative Gesamtsumme des Kontos das Stufenlimit erreicht, wird der Dienst für alle Projekte, die mit diesem Rechnungskonto verknüpft sind, bis zum Beginn des nächsten Abrechnungszeitraums (dem 1. eines jeden Monats) pausiert.

#### Ausgaben für das Rechnungskonto analysieren

So prüfen Sie anhand Ihrer bisherigen monatlichen Ausgaben, ob sich die neuen [Ausgabenlimits für Abrechnungskonten](#tier-spend-caps) auf Ihre laufenden Projekte auswirken:

1. Rufen Sie in der Google Cloud Console die Seite [Berichte zum Cloud-Rechnungskonto](https://console.cloud.google.com/billing/reports?hl=de) auf.
   - Wenn Sie mehr als ein Rechnungskonto haben, wählen Sie das Cloud-Rechnungskonto aus, für das Sie Kostenberichte aufrufen möchten.
2. Im Bericht ist standardmäßig „Nach Dienst gruppieren“ für den aktuellen Monat festgelegt. In der Spalte **Dienst** der Tabelle wird **Gemini API** angezeigt und in der Spalte **Nutzungskosten** die Gesamtausgaben.
3. Wenn Sie detaillierte Kosten sehen möchten, die auf die Nutzung der Gemini API beschränkt sind, legen Sie den Filter **Gruppieren nach** auf **SKU** und den Filter **Dienste** auf **Gemini API** fest.
4. Passen Sie den Filter **Zeitraum nach Nutzungsdatum** an den gewünschten Zeitraum an, um Ihre bisherigen Ausgaben in einem Zeitraum zu analysieren.

## Verarbeitungszeit

Abrechnungssignale und ‑Updates werden nicht immer in Echtzeit gesendet.

- **Guthabenverbrauch**: Nutzungskosten werden in der Regel innerhalb von Minuten von Ihrem Guthaben abgebucht.
- **Zahlungsbestätigung**: Die meisten Kartenzahlungen erfolgen sofort. Bei einigen Zahlungsmethoden (z. B. Banküberweisungen) kann es jedoch mehrere Tage dauern, bis die Zahlung erfolgt. Dienste werden erst fortgesetzt oder aktualisiert, wenn der Kauf von Guthabenpunkten offiziell bestätigt wurde.
- **Stufen-Upgrades**: Nach einer erfolgreichen Zahlung oder wenn du die [Upgrade-Kriterien](#about-billing) erfüllst, werden Stufen-Upgrades in der Regel innerhalb von 10 Minuten angezeigt.
- **Diagramme zur Aufschlüsselung der Gesamtkosten**: Die Diagramme zur Aufschlüsselung der Gesamtkosten auf der Seite [Abrechnung](https://aistudio.google.com/billing?hl=de) und der Seite [Ausgaben](https://aistudio.google.com/spend?hl=de) werden möglicherweise erst nach 24 Stunden aktualisiert.

In den Cloud Billing-Anleitungen zu [Abrechnungszeitraum](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=de#delayed-billing) und [Transaktionslatenzen](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=de#missing-transactions) finden Sie weitere Informationen zu potenziellen Abrechnungsverzögerungen.

## Erstattungen

Erstattungen sind für **Prepay**-Abrechnungskonten nicht zulässig, außer beim Wechsel des Kontotyps.

**Wenn ein Konto mit Vorauszahlung zum Kontotyp „Nachträgliche Zahlung“ wechselt** (nachdem Sie die [Kriterien](#about-billing) erfüllt und Ihr Konto [manuell aktualisiert](#postpay) haben), wird das Konto mit Vorauszahlung geschlossen und alle verbleibenden Prepaid-Guthaben werden automatisch auf die hinterlegte Zahlungsmethode erstattet.

Wenn Sie Ihr Konto mit Vorauszahlung aus einem anderen Grund als einem Upgrade auf ein Konto mit nachträglicher Zahlung [schließen](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=de#close-a-billing-account), verfällt das verbleibende Guthaben.

Guthabenpunkte verfallen nach einem Jahr. Nach Ablauf verfallen die Gutschriften und können nicht mehr abgerufen werden.

Für **Postpay-Konten** gilt die [Google Cloud-Richtlinie für Erstattungen](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=de#request_a_refund).

## Cloud-Rechnungskonten

Für die Abrechnung von Diensten wird in der Gemini API [Cloud Billing-Konten](https://cloud.google.com/billing/docs/concepts?hl=de) verwendet, die Sie [direkt in AI Studio einrichten](#setup-billing) können.
Mit AI Studio können Sie Ausgaben im Blick behalten, Kosten nachvollziehen und Zahlungen vornehmen.

Stufen, Ratenbeschränkungen und Obergrenzen für Rechnungskonten werden alle auf Ebene des Rechnungskontos festgelegt.

### Projekte und API-Schlüssel

Alle [Projekte](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects), die mit einem Cloud-Rechnungskonto verknüpft sind, übernehmen die Nutzungsebene des Rechnungskontos sowie die zugehörigen Ratenlimits und Kontolimits. Wenn Sie ein [Projekt von einem Rechnungskonto in ein anderes verschieben](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de#change_the_billing_account_for_a_project), wird die Stufe des Projekts und damit auch die Ratenbeschränkungen und Kontolimits auf die Stufe des neuen Rechnungskontos umgestellt.

Die kumulativen Ausgaben (für alle Google Cloud-Produkte) und das Kontoalter für alle Projekte, die mit einem Rechnungskonto verknüpft sind, werden auf die [Stufenanforderungen](#about-billing) dieses Rechnungskontos angerechnet.

Sie können die [Verknüpfung eines Projekts mit dem Rechnungskonto aufheben](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de#disable_billing_for_a_project), um zur kostenlosen Stufe zurückzukehren.

[API-Schlüssel](https://ai.google.dev/gemini-api/docs/api-key?hl=de) sind Anmeldedaten, die in einem Projekt generiert werden.
Sie haben keine unabhängigen Abrechnungseinstellungen, sondern übernehmen die Stufenlimits und den Abrechnungsstatus des Projekts. Die kumulative Nutzung aller Schlüssel in einem Projekt wird auf die Ausgabenobergrenze des Projekts und die Gesamtausgaben des Rechnungskontos angerechnet.

## Häufig gestellte Fragen

In den folgenden Abschnitten finden Sie Antworten auf häufig gestellte Fragen.

### Was wird mir in Rechnung gestellt?

Die Preise für die Gemini API basieren auf Folgendem:

- Anzahl der Eingabetokens
- Anzahl der Ausgabetokens
- Anzahl der im Cache gespeicherten Tokens
- Speicherdauer für im Cache gespeicherte Tokens

Informationen zu den Preisen finden Sie auf der [Preisseite](https://ai.google.dev/pricing?hl=de).

### Wo kann ich mein Kontingent einsehen?

Sie können Ihr Kontingent und Ihre Systemlimits in [AI Studio](https://aistudio.google.com/usage?hl=de) einsehen.

### Wie wechsle ich zu einer höheren Ratenbegrenzung oder fordere mehr Kontingent an?

Sie erhalten automatisch mehr Kontingent, wenn Ihr Konto die [Anforderungen für die nächste Stufe](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de#usage-tiers) erfüllt.

### Kann ich die Gemini API im EWR (einschließlich der EU), im Vereinigten Königreich und in der Schweiz kostenlos verwenden?

Ja, wir bieten das kostenlose und das kostenpflichtige Abo in [vielen Regionen](https://ai.google.dev/gemini-api/docs/available-regions?hl=de) an.

### Wenn ich die Abrechnung für die Gemini API einrichte, werden mir dann die Gebühren für die Nutzung von Google AI Studio in Rechnung gestellt?

Die Nutzung von AI Studio ist weiterhin kostenlos, sofern Nutzer keinen kostenpflichtigen API-Schlüssel verknüpfen, um auf kostenpflichtige Funktionen zuzugreifen.
Wenn Sie einen kostenpflichtigen API-Schlüssel im Rahmen eines kostenpflichtigen Projekts in AI Studio verknüpfen, werden Ihnen die AI Studio-Nutzungsgebühren für diesen Schlüssel in Rechnung gestellt. Sie können bei Bedarf zwischen Projekten der kostenpflichtigen Stufe und Projekten der kostenlosen Stufe wechseln, indem Sie die entsprechenden API-Schlüssel verwenden, die mit den einzelnen Typen verknüpft sind.

### Wie führe ich ein Upgrade auf höhere Stufen durch, wenn ich die Kostenlose Stufe nutze?

Wenn Sie auf höhere Stufen zugreifen möchten, müssen Sie die Abrechnung für Ihr Projekt einrichten. Klicken Sie in Google AI Studio auf [**Abrechnung einrichten**](#setup-billing). Hier wird beschrieben, wie Sie ein Cloud-Rechnungskonto auswählen oder erstellen. Wenn Sie das Prepaid-Abrechnungsmodell verwenden müssen, werden Sie beim **Einrichten der Abrechnung** durch den Prozess zum Erstellen Ihres Prepaid-Kontos geführt, das mit Ihrem Cloud-Rechnungskonto verknüpft ist.

### Kann ich in der kostenlosen Stufe 1 Million Tokens verwenden?

Die kostenlose Stufe für die Gemini API variiert je nach ausgewähltem Modell. Derzeit können Sie das Kontextfenster mit 1 Million Tokens auf folgende Weise testen:

- In Google AI Studio
- Kostenlose Tarife für ausgewählte Modelle
- Mit Tarifen mit nachträglicher Zahlung

### Kann ich zur kostenlosen Stufe zurückkehren, nachdem ich auf höhere (kostenpflichtige) Stufen umgestellt habe?

Wenn Sie ein Downgrade auf das kostenlose Kontingent durchführen möchten, können Sie die [Abrechnung für jedes Projekt deaktivieren](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de#disable_billing_for_a_project), für das Sie ein Downgrade durchführen möchten.

### Wie kann ich die Anzahl der verwendeten Tokens berechnen?

Verwenden Sie die Methode [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=de#count_tokens), um die Anzahl der Tokens zu zählen. Weitere Informationen zu Tokens finden Sie im [Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

### Wenn ich mich über AI Studio für mein erstes Cloud-Rechnungskonto registriere, erhalte ich dann trotzdem einen kostenlosen Testzeitraum für Google Cloud?

Wenn Sie sich für Ihr erstes Cloud-Rechnungskonto registrieren, beginnt Ihr [kostenloser Testzeitraum für Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=de#free-trial) und Sie erhalten ein [Startguthaben](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de#welcome-credits) in Höhe von 300 $.
Diese Guthaben können jedoch nicht zur Bezahlung der AI Studio-Nutzung verwendet werden. Sie können das Willkommensguthaben für die Bezahlung anderer berechtigter Dienste in Google Cloud verwenden. Wenn das Guthaben aufgebraucht ist oder innerhalb von 90 Tagen abläuft, werden alle zusätzlichen Nutzungskosten automatisch über die von Ihnen angegebene Zahlungsmethode abgerechnet.

### Kann ich mein Google Cloud-Startguthaben für die Gemini API verwenden?

Nein, das [Startguthaben](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de#welcome-credits) oder das Guthaben für den kostenlosen Testzeitraum von Google Cloud kann nicht für die Gemini API oder AI Studio verwendet werden.

Wenn Sie vor dem Ausschluss ein Google Cloud-Startguthaben erhalten haben, dürfen Sie Ihr verbleibendes Guthaben bis zum Ablauf (nach 90 Tagen) für die Gemini API und AI Studio ausgeben.

### Gilt die kostenlose Testversion von Google Cloud für die Nutzung der Gemini API?

Nein. Ab März 2026 sind die Nutzungskosten für die Gemini API ausdrücklich vom Programm [Google Cloud-Testversion mit einem Guthaben von 300 $](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=de#free-trial) ausgeschlossen.

### Wie funktioniert Google Cloud-Guthaben mit Vorauszahlungen?

Nutzer mit Prepaid-Guthaben müssen zuerst [Prepaid-Guthaben kaufen](#buy-credits), bevor infrage kommende Google Cloud-Guthaben auf die Nutzung der Gemini API angewendet werden können. Wenn Sie ein aktives Prepay-Guthaben haben, werden Google Cloud-Guthaben, die für die Gemini API infrage kommen, vor Ihrem Prepay-Guthaben aufgebraucht. Wenn das Guthaben Ihres Vorauszahlungskontos im Rechnungskonto 0 $ erreicht, werden keine Google Cloud-Guthaben mehr verwendet.

Nicht alle Google Cloud-Guthaben, z. B. das [Google Cloud-Startguthaben](#cloud-credits), können für die Gemini API und AI Studio verwendet werden.

### Wie erfolgt die Abrechnung?

Die Abrechnung für die Gemini API erfolgt über das [Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=de)-System. Informationen zur Abrechnungseinrichtung in Cloud Billing im Produkt finden Sie in der [Cloud Billing-Dokumentation](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de).

### Werden mir fehlgeschlagene Anfragen in Rechnung gestellt?

Wenn Ihre Anfrage mit einem 400- oder 500-Fehler fehlschlägt, werden Ihnen die verwendeten Tokens nicht in Rechnung gestellt. Die Anfrage wird jedoch weiterhin auf Ihr Kontingent angerechnet.

### Wird `GetTokens` in Rechnung gestellt?

Anfragen an die `GetTokens` API werden nicht in Rechnung gestellt und nicht auf das Inferenzkontingent angerechnet.

### Wie werden meine Google AI Studio-Daten verarbeitet, wenn ich ein kostenpflichtiges API-Konto habe?

Weitere Informationen zum Umgang mit Daten, wenn die Cloud-Abrechnung aktiviert ist, finden Sie in den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de#paid-services) unter „Nutzung Ihrer Daten durch Google“ im Abschnitt „Kostenpflichtige Dienste“. Ihre Google AI Studio-Prompts unterliegen denselben Bedingungen für „kostenpflichtige Dienste“, sofern für mindestens ein API-Projekt die Abrechnung aktiviert ist. Sie können dies auf der [Seite mit den Gemini API-Schlüsseln](https://aistudio.google.com/api-keys?hl=de) überprüfen, wenn unter „Plan“ Projekte als „Kostenpflichtig“ gekennzeichnet sind.

### Was ist die Prepay-Abrechnung und wer muss sie verwenden?

Mit der Prepaid-Abrechnung können Nutzer der Gemini API in AI Studio Guthaben im Voraus kaufen.
Ab dem 23. März 2026 müssen neue AI Studio-Nutzer möglicherweise den Prepaid-Abrechnungsplan verwenden. Während des Prozesses [Abrechnung einrichten](#setup-billing) in AI Studio werden Sie durch den Abrechnungseinrichtungsprozess geführt und es wird angegeben, ob Sie im Voraus bezahlen müssen.

### Wie kaufe ich Prepay-Guthabenpunkte und gibt es einen Mindest- oder Höchstbetrag?

Sie können [Guthabenpunkte auf der Abrechnungsseite von AI Studio kaufen](#buy-credits). Während des Kaufvorgangs wird in der Benutzeroberfläche der für deine Region und Stufe erforderliche Mindestbetrag für die Vorabzahlung sowie der Höchstbetrag angezeigt, der sich jeweils in deinem Konto befinden darf.

### Kann ich mein Prepay-Konto so konfigurieren, dass bei Bedarf automatisch zusätzliches Guthaben gekauft wird?

Ja, wir empfehlen, in den Abrechnungseinstellungen von AI Studio [automatisches Aufladen](#auto-reload) zu konfigurieren. Sie geben ein „Trigger“-Guthaben an (z.B. „wenn mein Guthaben unter 30 $ fällt“) und einen „Aufladewert“ (z.B. „100 $ hinzufügen“).

### Kann ich die Anzahl der automatischen Aufladungen begrenzen?

Ja, Nutzer mit Prepaid-Tarif können im Widget **Automatisches Aufladen** ein [monatliches Limit für das automatische Aufladen](#monthly-auto-charge-limit) festlegen. Wenn der Gesamtbetrag der automatischen Aufladungen in einem Abrechnungszeitraum dieses Limit erreicht, wird die automatische Aufladung bis zum nächsten Monat deaktiviert. Manuelle Gutschriften werden nicht auf dieses Limit angerechnet.

### Kann ich eine Erstattung für meine nicht genutzten Credits erhalten?

Alle Prepaid-API-Guthaben verfallen nach einem Jahr und können nicht erstattet werden. [Erstattungsrichtlinie für Konten mit Vorauszahlung](#refunds)

### Verfällt mein Vorauszahlungsguthaben irgendwann?

Ja, Guthabenpunkte verfallen 12 Monate nach dem Kaufdatum.

### Was passiert, wenn mein Prepaid-Guthaben 0 $ erreicht?

Alle Gemini API-Dienste in allen Projekten, die über dieses Cloud Billing-Konto mit Vorauszahlung bezahlt werden, werden sofort beendet, um weitere Gebühren zu vermeiden. Ihre Projekte werden nicht automatisch auf die Kostenlose Stufe herabgestuft.

Wenn Sie den Dienst auf Ihrer aktuellen kostenpflichtigen Stufe wiederherstellen möchten, müssen Sie [zusätzliche Credits kaufen](#buy-credits). Nachdem Sie Guthaben gekauft haben, sollten Sie die Gemini API verwenden können. Es kann zu einer [Verzögerung](#processing-times) kommen, bis dein Guthaben in unseren Systemen aktualisiert wird.

Optional können Sie ein Downgrade auf das kostenlose Kontingent durchführen, indem Sie die [Abrechnung für die Projekte deaktivieren](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=de#disable_billing_for_a_project), für die Sie ein Downgrade durchführen möchten.

### Warum wurde die Nutzung eingestellt, obwohl mein Guthaben für die Vorauszahlung mehr als 0 € beträgt?

Möglicherweise haben Sie das [Nutzungslimit](#tier-spend-caps) für Ihr aktuelles Abo erreicht.
Die Nutzungslimits werden automatisch erhöht, wenn Sie in höhere Stufen aufsteigen. Die Nutzung der Gemini APIs in AI Studio kann auch durch den [Status Ihres Cloud-Rechnungskontos](#missed-payment) beeinträchtigt werden.

### Warum ist das Guthaben meines Kontos mit Vorauszahlung negativ?

Aufgrund der Komplexität unserer Abrechnungs- und Verarbeitungssysteme kann es zu [Verzögerungen](#processing-times) kommen, bis die Nutzung beendet wird, nachdem Sie alle Ihre Guthaben aufgebraucht haben. Diese zusätzliche Nutzung wird möglicherweise als negatives Guthaben in Ihrem Abrechnungsdashboard für AI Studio angezeigt. In diesem Fall wird Ihr Dienst pausiert und Ihr negatives Guthaben wird von Ihrem nächsten Guthabenkauf abgezogen.

Damit Ihr Gemini API-Dienst nicht pausiert wird, empfehlen wir, [automatisches Aufladen](#auto-reload) einzurichten. So werden automatisch weitere Guthabenpunkte gekauft, wenn Ihr Guthaben unter einen von Ihnen angegebenen Wert sinkt.

### Kann ich mein Prepaid-Guthaben für andere Google Cloud-Dienste wie die Gemini Enterprise Agent Platform verwenden?

Nein. Prepaid-Guthaben kann nur für die Nutzung der Gemini API verwendet werden. Alle anderen Google Cloud-Dienste, die Sie verwenden (Compute, Storage, Gemini Enterprise Agent Platform), werden über den standardmäßigen [Cloud-Abrechnungszeitraum](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=de) abgerechnet.

### Kann ich von der Vorauszahlung zur nachträglichen Zahlung wechseln?

Nein, ein Wechsel von einem Abrechnungstarif mit Vorauszahlung zu einem Abrechnungstarif mit Nachträglicher Zahlung wird nicht unterstützt.

### Kann ich von der Abrechnung mit nachträglicher Zahlung zur Abrechnung mit Vorauszahlung wechseln?

Ja, Sie können ein bestehendes Postpay-Konto auf der Seite [AI Studio-Abrechnung](https://aistudio.google.com/billing?hl=de) umstellen. Eine Anleitung finden Sie unter [Auf Vorauszahlung umstellen](#migrate-to-prepay).

### Was passiert mit meinem Prepaid-Guthaben, wenn ich zu einem Postpay-Tarif wechsle?

Wenn Sie ein Upgrade auf [Nachträgliche Zahlung](#postpay) durchführen, schließt Cloud Billing Ihr Vorauszahlungs-Zahlungskonto, deaktiviert das [automatische Aufladen](#auto-reload) und erstattet Ihnen automatisch alle nicht verwendeten Vorauszahlungs-Guthaben (vorbehaltlich der standardmäßigen Bearbeitungszeit für Erstattungen).

### Wo kann ich mein aktuelles Prepay-Guthaben und meinen Transaktionsverlauf einsehen?

Die gesamte Guthabenverwaltung und der Transaktionsverlauf für die Gemini API müssen direkt über den Tab „Abrechnung“ in Google AI Studio erfolgen.

### Warum wird die Meldung „Der Typ des Rechnungskontos ist inaktiv oder wird nicht unterstützt“ angezeigt?

Zahlungsinteraktionen auf der [Abrechnungsseite für AI Studio](https://aistudio.google.com/billing?hl=de) werden möglicherweise blockiert und durch die Meldung „Der Abrechnungskontotyp ist inaktiv oder wird nicht unterstützt“ ersetzt, wenn der ausgewählte Abrechnungskontotyp oder der Abrechnungskontostatus nicht für die kostenpflichtige Version von AI Studio infrage kommt.

Prüfen Sie den Status Ihres Abrechnungskontos in der [Cloud Console](https://console.cloud.google.com/billing/?hl=de). Ein nicht berechtigter Typ könnte *Konto für kostenlosen Testzeitraum* sein. In diesem Fall können Sie die [Abrechnung in AI Studio aktivieren](#setup-billing), um die Berechtigung zu erhalten. Ein inaktiver Status kann *Geschlossen* sein. In diesem Fall können Sie [das Konto wieder öffnen](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=de).

### Werden die Kosten für die Nutzung der Gemini API in der Google Cloud Console angezeigt?

Ja. Die Kosten für die Gemini API sowie die Kosten für alle anderen Google Cloud-Dienste, die über Ihr Cloud-Rechnungskonto bezahlt werden, können auf den [Seiten zur Kostenverwaltung](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=de#cost-reports) in der [Cloud Billing Console](https://console.cloud.google.com/billing?hl=de) eingesehen werden. Hinweis: Sie können Ihr Prepaid-Guthaben nur in AI Studio verwalten.

### Warum wird meine Gemini API-Nutzung nicht in der Cloud Billing Console angezeigt, obwohl ich sie zusammen mit dem Verbrauch meiner Guthaben in der AI Studio-Abrechnung sehen kann?

Google Cloud und AI Studio melden Nutzungsdaten in unterschiedlichen Intervallen an Cloud Billing. Aufgrund der Komplexität unserer Abrechnungs- und Verarbeitungssysteme kann es zu einer Verzögerung zwischen der Nutzung von Diensten und der Nutzung und Kosten kommen, die in Cloud Billing angezeigt werden. In der Regel sind Ihre Kostendetails innerhalb eines Tages verfügbar, manchmal kann es aber auch mehr als 24 Stunden dauern.
Weitere Informationen zur verzögerten Abrechnung finden Sie in der [Dokumentation zu Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=de#delayed-billing).

### Was passiert, wenn ich eine Zahlung verpasse, wenn ich andere Google Cloud-Dienste mit Kosten verwende, die einem Postpay-Abrechnungszyklus unterliegen?

Wenn Sie eine Zahlung für andere Google Cloud-Dienste versäumt haben, kann Ihr Zugriff auf die Gemini API in AI Studio gesperrt werden, **unabhängig davon, wie viel Prepaid-Guthaben Sie haben**. Die Nutzung von AI Studio wird über ein Google Cloud-Rechnungskonto abgerechnet, das sowohl die Vorauszahlungsabrechnung für AI Studio als auch die Abrechnung im Nachhinein für andere Cloud-Dienste nutzen kann. Wenn es ein Problem mit Ihrem Postpay-Guthaben gibt, werden alle mit diesem Konto verknüpften Dienste eingestellt. Ihre Gemini API-Nutzung wird ausgesetzt, wenn Ihr Cloud-Rechnungskonto aufgrund von Problemen wie den folgenden gekennzeichnet ist:

- Ein überfälliger Betrag
- Eine abgelehnte Zahlung
- Eine ungültige oder abgelaufene Zahlungsmethode

Um den Dienst wiederherzustellen, müssen Sie das [Problem mit dem Postpay-Konto](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=de#resolving-declined-payments) in der Google Cloud Billing Console beheben. Sobald Sie das Problem behoben haben, erhalten Sie wieder Zugriff auf Ihr Prepaid-Guthaben für die Gemini API und auf die Dienste.

### Warum werden meine Projekte unterbrochen, nachdem ich eine Vorauszahlung eingerichtet habe?

**Problem**:Sie haben den Vorgang zum Hinzufügen von Vorauszahlungsfunktionen zu einem bestehenden Rechnungskonto mit nachträglicher Zahlung gestartet, das Fenster jedoch geschlossen oder den Vorgang abgebrochen, bevor Sie die Einrichtung der Vorauszahlung abgeschlossen haben. Andere mit diesem Rechnungskonto verknüpfte Projekte haben den Zugriff auf die Gemini API verloren.

**Ursache**:Während der Umstellung wird die Infrastruktur zur Unterstützung von Vorauszahlungen in Ihrem Abrechnungskonto erstellt, sobald Sie das Bestätigungsdialogfeld akzeptieren. Wenn Sie die Schritte für die Vorauszahlung nicht ausführen, bleibt die Konfiguration in einem nicht abrechenbaren Status. Da dieser Status auf Rechnungskontoebene gilt, wird der Zugriff für alle Projekte eingeschränkt, die mit diesem Rechnungskonto verknüpft sind und auf Prepay-Dienste angewiesen sind.

**Lösung**:Da sich der Kontostatus bereits geändert hat, gibt es keine automatische Möglichkeit, den Status zurückzusetzen, wenn Sie den Zahlungsvorgang abbrechen. So stellen Sie den Dienst für Ihre verknüpften Projekte wieder her:

- **Einrichtung abschließen**:Kehren Sie zu Google AI Studio zurück, starten Sie den Abrechnungseinrichtungsvorgang neu und schließen Sie die Vorauszahlung ab. Nachdem die Zahlung verarbeitet wurde, wird der Abrechnungsplan mit Vorauszahlung aktiviert und der Dienst wird wiederhergestellt.
- **Support kontaktieren**:Wenn Sie das Prepay-Abrechnungsmodell nicht verwenden und Ihr Rechnungskonto wieder auf Postpay zurücksetzen möchten, [wenden Sie sich an den Cloud Billing-Support](https://cloud.google.com/support/billing?hl=de), um den Kontostatus manuell zurücksetzen zu lassen.

### Wo erhalte ich Hilfe bei der Abrechnung?

Hilfe bei der Abrechnung erhalten Sie unter [Cloud Billing-Support erhalten](https://cloud.google.com/support/billing?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-08 (UTC)."],[],[]]
