---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=de
fetched_at: 2026-09-14T05:53:55.945835+00:00
title: "\u00dcber Google\u00a0AI Studio bereitstellen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Über Google AI Studio bereitstellen

Mit Google AI Studio können Sie Ihre Full-Stack-Anwendungen direkt über den Build-Modus bereitstellen. So können Sie schnell von einem Prototyp zu einer verwalteten, skalierbaren Produktionsumgebung wechseln.

## Optionen der Bereitstellung

Die Anforderungen für die Bereitstellung Ihrer Anwendung über den AI Studio Build-Modus hängen von der verwendeten Stufe ab:

- [**Google Cloud-Starterpaket**](https://docs.cloud.google.com/docs/starter-tier?hl=de): Damit können Sie bis zu zwei Full-Stack-Anwendungen veröffentlichen, ohne ein Google Cloud-Projekt oder ein Abrechnungskonto einzurichten.
- **Standardbereitstellung**: Hierfür ist ein Google Cloud-Projekt erforderlich, das mit Ihrem AI Studio-Konto verknüpft ist und für das die Abrechnung aktiviert ist.

## Starter-Stufe

Der Google Cloud Starter Tier bietet einen einfachen Weg, Anwendungen direkt aus Google AI Studio in Google Cloud bereitzustellen, ohne eine vollständige Google Cloud-Umgebung oder ein Abrechnungskonto einrichten zu müssen.

Bei jeder Google AI Studio-Bereitstellung wird ein entsprechender Dienst in Cloud Run erstellt. Für Dienste, die in Google AI Studio mit dem Starter-Abo bereitgestellt werden, gelten die folgenden Einschränkungen:

- Sie können bis zu zwei Dienste bereitstellen.
- Ihre Dienste werden in einer [einzigen Cloud Run-Region](https://docs.cloud.google.com/run/docs/locations?hl=de) bereitgestellt.

## Bereitstellungsschritte für die Starter-Stufe

Nachdem Sie Ihre App im Build-Modus entworfen haben, können Sie sie mit dem Starter-Tarif bereitstellen:

1. Klicken Sie rechts oben auf die Schaltfläche **Veröffentlichen**.
2. Klicken Sie auf **Jetzt starten**.
3. Klicken Sie auf **App veröffentlichen**.

Nach Abschluss der Bereitstellung stellt AI Studio eine Cloud Run-URL bereit, über die Sie auf Ihre Live-Anwendung zugreifen können.

## Benutzerdefinierte URLs für AI Studio

Wenn Sie eine Anwendung über Google AI Studio veröffentlichen, können Sie unter `ai.studio` eine benutzerdefinierte, einprägsame Subdomain festlegen, z. B. `https://your-app-name.ai.studio`.

Für Google AI Studio müssen Subdomains in allen Projekten global eindeutig sein. Sie werden nach dem Prinzip „First come, first served“ zugewiesen. Wenn ein anderer Name bereits in einem anderen Projekt verwendet wird, werden Sie in AI Studio aufgefordert, einen anderen Namen auszuwählen. Wenn Sie eine Anwendung aus dem Play Store entfernen oder löschen, wird die benutzerdefinierte URL freigegeben und kann von anderen Nutzern beansprucht werden.

### Benutzerdefinierte URL festlegen

So legen Sie eine benutzerdefinierte URL für Ihre Anwendung fest oder aktualisieren sie:

1. Öffnen Sie Ihre Anwendung in Google AI Studio im Modus **Build** (Erstellen).
2. Klicken Sie rechts oben auf **Veröffentlichen**.
3. Geben Sie in der Bereitstellungskonfiguration im Feld **Benutzerdefinierte URL** die gewünschte Subdomain ein oder übernehmen Sie die vorgeschlagene URL.
4. Klicken Sie auf **App veröffentlichen**.

Wenn Sie eine vorhandene benutzerdefinierte URL auf eine andere Anwendung übertragen möchten, müssen Sie zuerst die Anwendung, der diese benutzerdefinierte URL zugewiesen ist, aus dem Play Store entfernen oder die Veröffentlichung aufheben. Anschließend können Sie Ihre neue Anwendung mit der ausgewählten Subdomain veröffentlichen.

### Marken- oder Urheberrechtsprobleme melden

Benutzerdefinierte Subdomains müssen den [Google-Nutzungsbedingungen](https://policies.google.com/terms?hl=de) entsprechen. Wenn Sie eine benutzerdefinierte URL sehen, die gegen das Markenrecht verstößt oder einen urheberrechtlich geschützten Namen ohne Erlaubnis verwendet, können Sie sie über die [Google-Fehlerbehebung für rechtliche Probleme](https://support.google.com/legal/troubleshooter/1114905?hl=de) melden.

## Standardmäßige Bereitstellung

Wenn sich Ihre Anwendungen weiterentwickeln, benötigen Sie möglicherweise Funktionen, die über den Einstiegstarif hinausgehen, z. B. höhere Kontingente, mehr Rechenressourcen oder andere Google Cloud-Produkte, die im Einstiegstarif nicht verfügbar sind. Wenn Sie diese Funktionen nutzen möchten, können Sie Ihr vollständig verwaltetes Projekt im Einstiegstarif in ein Standard-Google Cloud-Projekt umwandeln.

So können Sie nahtlos skalieren, ohne Ihren Fortschritt zu verlieren. Folgen Sie der Anleitung zum [Erstellen eines Cloud-Rechnungskontos](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=de#create-new-billing-account), akzeptieren Sie die standardmäßigen Google Cloud-Nutzungsbedingungen und [führen Sie ein Upgrade auf ein standardmäßiges Google Cloud-Projekt durch](https://docs.cloud.google.com/docs/starter-tier?hl=de#upgradee).
Weitere Informationen finden Sie unter [Einrichtung für kostenpflichtige Konten](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de#paid-setup).

Weitere Informationen zu Abrechnungsstufen finden Sie unter [Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de).

## Anwendung löschen

Wenn Sie Ihre App nicht mehr benötigen, können Sie sie in Google AI Studio löschen. Gehen Sie dazu so vor:

1. Rufen Sie in Google AI Studio die Seite [Apps](https://aistudio.google.com/app/apps?hl=de) auf.
2. Wählen Sie im Menü auf der linken Seite **Apps** aus.
3. Bewegen Sie den Mauszeiger auf die App, die Sie löschen möchten.
4. Klicken Sie rechts neben der Zeile auf das Papierkorbsymbol, um die App zu löschen.

## Nächste Schritte

- [Weitere Informationen zur Google Cloud Starter-Stufe](https://docs.cloud.google.com/docs/starter-tier?hl=de)
- [Weitere Informationen zur Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-10 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-10 (UTC)."],[],[]]
