---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=de
fetched_at: 2026-05-25T05:20:42.911259+00:00
title: "Full-Stack-Apps in Google\u00a0AI Studio entwickeln \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Full-Stack-Apps in Google AI Studio entwickeln

Google AI Studio unterstützt jetzt die Full-Stack-Entwicklung. So können Sie Anwendungen erstellen, die über clientseitige Prototypen hinausgehen. Mit einer serverseitigen Laufzeit können Sie Secrets verwalten, eine Verbindung zu externen APIs herstellen und Echtzeit-Multiplayer-Erlebnisse entwickeln.

## Serverseitige Laufzeit

Google AI Studio-Anwendungen können jetzt eine serverseitige Komponente (Node.js) enthalten.
Damit können Sie

- **Serverseitige Logik ausführen**: Führen Sie Code aus, der nicht für den Client sichtbar sein soll.
- **Auf npm-Pakete zugreifen**: Der [Antigravity-Agent](https://antigravity.google/docs/agent?hl=de) kann Pakete aus dem umfangreichen npm-Ökosystem installieren und verwenden.
- **Secrets verwalten**: API-Schlüssel und Anmeldedaten sicher verwenden.

### npm-Pakete verwenden

Sie müssen `npm install` nicht manuell ausführen. Bitten Sie den Agent einfach, Funktionen hinzuzufügen, für die ein Paket erforderlich ist. Er kümmert sich dann um die Installation und den Import.

**Beispiel**: > „Verwende `axios`, um Daten aus der externen API abzurufen.“

## Secrets sicher verwalten

Mit serverseitigem Code und der Verwaltung von Secrets können Sie jetzt Apps entwickeln, die mit der Welt interagieren.

### Gemini API-Schlüssel

Wenn Sie eine neue App erstellen, die die Gemini API verwendet, konfiguriert AI Studio Ihren `GEMINI_API_KEY` automatisch als serverseitiges Secret. Eine manuelle Einrichtung ist nicht erforderlich. Sie können diesen Schlüssel in den Einstellungen im Bereich **Secrets** aufrufen. Die Gemini API-Aufrufe Ihrer App werden mit diesem Schlüssel über serverseitigen Code ausgeführt. Er wird also nie im Browser angezeigt.

### API-Schlüssel von Drittanbietern

Bei anderen Diensten können Sie API-Schlüssel manuell hinzufügen:

- **Drittanbieter-APIs**: Stellen Sie eine Verbindung zu Diensten wie Stripe, SendGrid oder benutzerdefinierten REST-APIs her.
- **Datenbanken**: Stellen Sie eine Verbindung zu externen Datenbanken her (z.B. über Supabase, Firebase oder MongoDB Atlas), um Daten über die Sitzung hinaus zu speichern.

Wenn Sie Apps für die reale Welt entwickeln, müssen Sie oft eine Verbindung zu Drittanbieterdiensten wie Twilio, Slack oder Datenbanken herstellen, für die API-Schlüssel erforderlich sind. Sie können Schlüssel manuell hinzufügen. Gehen Sie dazu so vor:

1. **Secret hinzufügen**: Rufen Sie in Google AI Studio das Menü **Einstellungen** auf und suchen Sie nach dem Bereich „Secrets“.
2. **Schlüssel speichern**: Fügen Sie hier Ihre API-Schlüssel oder geheimen Tokens hinzu.
3. **Zugriff im Code**: Der Agent kann serverseitigen Code schreiben, der sicher auf diese vertraulichen Informationen zugreift (in der Regel über Umgebungsvariablen). So wird sichergestellt, dass sie niemals im clientseitigen Browser offengelegt werden.

Bei Bedarf wird im Chat auch eine Karte angezeigt, in der Sie aufgefordert werden, Schlüssel hinzuzufügen, wenn ein neues Secret erforderlich ist oder wenn in den Umgebungsvariablen des Projekts ein neuer Schlüssel erkannt wird.

### Firebase-Integration für Datenbank und Authentifizierung

Mit Google AI Studio können Sie Ihrer App jetzt ganz einfach eine Datenbank oder Authentifizierung über eine [Firebase-Integration](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=de) hinzufügen.
Der Antigravity-Agent kann die folgenden Dienste automatisch für Sie bereitstellen und einrichten:

- **Firestore-Datenbank**: Eine flexible, skalierbare NoSQL-Cloud-Datenbank zum Speichern und Synchronisieren von Daten für die client- und serverseitige Entwicklung.
- **Firebase Authentication**: Ermöglichen Sie Ihren Nutzern, sich sicher in Ihrer Anwendung anzumelden, indem Sie die Abläufe für „Mit Google anmelden“ verwenden.

Bitten Sie den Agenten einfach, „meiner App eine Datenbank hinzuzufügen“ oder „Google-Anmeldung einzurichten“. Er übernimmt dann die erforderliche Konfiguration und Codegenerierung für Sie.

Mit Firebase können Sie kostenlos starten und optional mit einem kostenpflichtigen Konto skalieren, wenn Sie mehr Kontingent benötigen oder kostenpflichtige Funktionen nutzen möchten.

## Google Workspace APIs

Mit Google AI Studio können Sie Apps erstellen, die eine Verbindung zu Google Workspace-APIs herstellen, damit Ihre Nutzer in Ihrer App mit ihren echten Daten arbeiten können: E-Mails, Tabellen, Dokumente, Kalendertermine und mehr. Sie müssen kein Google Cloud-Projekt mehr einrichten, OAuth konfigurieren oder Ihre API manuell verwalten.

### Funktionsweise

Sie haben zwei Möglichkeiten, eine Workspace-Integration hinzuzufügen:

- **Im Chatfeld beschreiben**: Teilen Sie dem Agent einfach im Chatfeld unten mit, was Sie möchten. Beispiele: *„Erstelle einen Ausgaben-Tracker, der Belege in meiner Google-Tabelle protokolliert.“* oder *„Erstelle ein Dashboard, das meine ungelesenen Gmail-Nachrichten zusammenfasst.“*
- **Über den Bereich „Integrationen“ auswählen**: Öffnen Sie im Build-Modus in der rechten Seitenleiste den Bereich **Integrationen** und aktivieren Sie die Workspace-App, die Sie verbinden möchten.

Wenn Sie eine Workspace-App hinzufügen, wird in AI Studio automatisch Folgendes ausgeführt:

1. Verbindet die erforderliche Google API für Ihre App.
2. Generiert den serverseitigen Code zum Aufrufen der API.
3. Fügt einen sicheren „Über Google anmelden“-Ablauf hinzu, damit Endnutzer Ihrer App den Zugriff auf ihre eigenen Daten autorisieren können.

### Unterstützte Apps

Die folgenden Google Workspace-Apps sind verfügbar:

| App | Was Sie erstellen können |
| --- | --- |
| Google Kalender | Termine und Kalender lesen, erstellen und verwalten |
| Google Chat | Unterhaltungen und Gruppenbereiche lesen und mit ihnen interagieren |
| Google Docs | Dokumente erstellen, lesen, aktualisieren und formatieren |
| Google Drive | Dateien und Ordner organisieren, suchen und verwalten |
| Google Formulare | Umfragen erstellen, Fragen aktualisieren und Antworten abrufen |
| Gmail | E‑Mail-Inhalte lesen, senden und verwalten |
| Google Notizen | Notizen, Listen und Anhänge verwalten |
| Google Meet | Videoanrufe planen und verwalten |
| Kontakte | Kontakte synchronisieren und verwalten |
| Google Sheets | Tabellendaten lesen, schreiben und formatieren |
| Google Präsentationen | Präsentationen erstellen und bearbeiten |
| Google Tasks | Aufgaben erstellen, verwalten und organisieren |

### Authentifizierung und Berechtigungen

Als Ersteller müssen Sie keine OAuth-Clients konfigurieren, Anmeldedaten verwalten oder ein Google Cloud-Projekt einrichten. AI Studio übernimmt das alles für Sie.

Apps, in die Workspace APIs integriert sind, verwenden „Über Google anmelden“, um Endnutzer zu authentifizieren. Wenn ein Nutzer Ihre App öffnet, wird er aufgefordert, sich anzumelden und die spezifischen Berechtigungen zu erteilen, die Ihre App benötigt, z. B. schreibgeschützter Zugriff auf seinen Kalender oder die Möglichkeit, eine Tabelle zu bearbeiten. Ihre App greift nur auf die Daten der Person zu, die sie verwendet. Jeder Nutzer autorisiert den Zugriff auf sein eigenes Konto.

### Beispiele für Prompts

Hier sind einige Ideen für den Einstieg in Workspace-Integrationen:

- *„Erstelle eine App, die meinen Google-Kalender liest und für jede Besprechung Vorbereitungs-E‑Mails in Gmail entwirft.“*
- *„Erstelle ein Tool, das ein Google-Dokument nimmt und daraus eine Zusammenfassungspräsentation mit fünf Folien in Google Präsentationen generiert.“*
- *„Erstelle eine Ausgabenübersicht, in die ich einen Beleg hochlade. Gemini extrahiert die Details und fügt eine neue Zeile in mein Google-Tabellenblatt ein.“*

### OAuth einrichten

Ein wichtiger Anwendungsfall für die Verwaltung von Secrets ist die Einrichtung von OAuth, um eine Verbindung zu anderen Websites oder Apps herzustellen. Wenn Ihr Prompt Anweisungen zum Herstellen einer Verbindung zu einer Drittanbieter-App enthält, für die eine OAuth-Authentifizierung erforderlich ist, gibt der Agent Anweisungen zum Einrichten von OAuth für diese Anwendung. Diese Anleitung enthält die erforderlichen Callback-URLs zum Konfigurieren Ihrer OAuth-Anwendung.
Sie finden die Callback-URLs auch im Bereich „Einstellungen“ unter **Integrationen**.

## Mehrspielerfunktionen entwickeln

Die Full-Stack-Laufzeit ermöglicht Funktionen für die Zusammenarbeit in Echtzeit.

- **Echtzeitstatus**: Sie können den Agent bitten, Funktionen wie „ein Live-Chat“, „ein gemeinsames Whiteboard“ oder „ein Mehrspielerspiel“ zu erstellen.
- **Synchronisierte Sitzungen**: Der Server verwaltet den Status, sodass mehrere Nutzer in Echtzeit mit derselben Anwendungsinstanz interagieren können.

**Beispiel-Prompt**: > „Mache daraus ein Multiplayer-Spiel, in dem die Spieler die Cursor der anderen sehen können.“

### Tipps zum Testen von Apps im Mehrspielermodus

Sie haben zwei Möglichkeiten, den Mehrspielermodus zu testen, bevor Sie Ihre App bereitstellen.

1. Öffnen Sie Ihre App im Build-Modus von Google AI Studio auf mehreren Tabs. Wenn Sie im Build-Modus entwickeln, befindet sich Ihre App in einem Entwicklercontainer. Wenn Sie die App in mehreren Tabs öffnen, können Sie mehrere Spieler simulieren, die Ihre App verwenden.
2. Teilen Sie die App mit anderen über das Menü **Teilen** oben rechts.
   Verwenden Sie dann die **freigegebene URL** auf dem Tab **Integrationen** des Menüs **Teilen**, um die App mit den Spielern zu verwenden, mit denen Sie Ihre App geteilt haben.

## Best Practices

- **Gemini API-Aufrufe**: Ihr `GEMINI_API_KEY` wird automatisch als serverseitiges Secret konfiguriert. Führen Sie Gemini API-Aufrufe über Ihren serverseitigen Code mit diesem Schlüssel aus. Sie können sie im Bereich **Secrets** aufrufen.
- **Sicherheit von Secrets**: Verwenden Sie für vertrauliche Schlüssel immer den Secrets Manager.
  Sie dürfen niemals in Ihren Dateien hartcodiert werden.
- **Trennung von Belangen**: Die UI-Logik sollte im clientseitigen Framework (React/Angular) und die Geschäftslogik/Datenverarbeitung auf dem Server erfolgen.
- **Fehlerbehandlung**: Achten Sie darauf, dass Ihr serverseitiger Code Fehler aus externen API-Aufrufen robust behandelt, um Abstürze der App zu verhindern.

## Wie geht es weiter?

- [Apps in Google AI Studio entwickeln](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=de)
- [Über Google AI Studio bereitstellen](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=de)
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-19 (UTC)."],[],[]]
