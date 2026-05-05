---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=de
fetched_at: 2026-05-05T13:29:22.761707+00:00
title: "Apps in Google\u00a0AI Studio entwickeln \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

- [Startseite](https://ai.google.dev/gemini-api/docs/Startseite)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/Dokumentation)

Feedback geben

# Apps in Google AI Studio entwickeln

Auf dieser Seite wird beschrieben, wie Sie mit Google AI Studio schnell Apps erstellen (oder „vibe
coden“) und bereitstellen, mit denen die neuesten Funktionen von Gemini wie
[Nano Banana](https://ai.google.dev/gemini-api/docs/Nano Banana) und die [Live
API](https://ai.google.dev/gemini-api/docs/LiveAPI) getestet werden können. Google AI Studio unterstützt jetzt **Full-Stack
Laufzeiten**, mit denen Sie robuste Anwendungen mit serverseitiger Logik,
sicherer Secret-Verwaltung und Unterstützung für npm-Pakete erstellen können – alles über Prompts in natürlicher Sprache.

## Jetzt starten

Starten Sie den [Build-Modus](https://ai.google.dev/gemini-api/docs/Build-Modus) in Google AI Studio, um mit dem Vibe Coding zu beginnen. Sie haben mehrere Möglichkeiten, mit der Entwicklung zu beginnen:

- **Mit einem Prompt beginnen**: Geben Sie im Build-Modus im Eingabefeld eine
  Beschreibung dessen ein, was Sie erstellen möchten. Wählen Sie AI Chips aus, um Ihrem Prompt bestimmte Funktionen wie die Bildgenerierung oder Google Maps-Daten hinzuzufügen. Sie können auch die Schaltfläche für die Sprach-zu-Text-Funktion verwenden, um zu sagen, was Sie möchten.
- **Schaltfläche „Auf gut Glück“**: Wenn Sie eine kreative Idee brauchen, verwenden Sie die Schaltfläche „Auf gut Glück“. Gemini generiert dann einen Prompt mit einer Projektidee, mit der Sie beginnen können.
- **Projekt aus der Galerie remixen**: Öffnen Sie ein Projekt aus der [App
  Galerie](https://ai.google.dev/gemini-api/docs/App  Galerie) und wählen Sie **App kopieren** aus.

Nachdem Sie den Prompt ausgeführt haben, werden der erforderliche Code und die Dateien generiert. Rechts sehen Sie eine Live-Vorschau Ihrer App.

## Was wird erstellt?

Wenn Sie Ihren Prompt ausführen, erstellt AI Studio eine vollständige Anwendung. Standardmäßig wird eine Full-Stack-Umgebung erstellt, die Folgendes umfassen kann:

- **Clientseitig**: ein Web-Frontend (Standard ist React).
- **Serverseitig**: eine Node.js-Laufzeit, die sichere API-Aufrufe, Datenbankverbindungen und die Verwendung von npm-Paketen ermöglicht.

Sie können den generierten Code ansehen, indem Sie im rechten Vorschaufenster den Tab **Code** auswählen. Der **Antigravity Agent** verwaltet auf intelligente Weise mehrere Dateien in Ihrem Stack und sorgt dafür, dass Änderungen korrekt weitergegeben werden.

### Der Antigravity Agent

Der **Antigravity Agent** ist die wichtigste KI-Funktion in [Google
Antigravity](https://ai.google.dev/gemini-api/docs/GoogleAntigravity). Die Kernkomponenten des
Agent-Harness werden jetzt für den Build-Modus in Google AI Studio verwendet. Er geht über die einfache Code-Generierung hinaus, indem er den Kontext Ihres gesamten Projekts beibehält, mehrere Dateien verwaltet und komplexe Anweisungen versteht, um robuste Full-Stack-Anwendungen zu erstellen.

Zu den wichtigsten Funktionen gehören:

- **Kontextsensitivität**: Der Kontext vorheriger Prompts und Dateistatus wird beibehalten.
- **Verwaltung mehrerer Dateien**: Abhängigkeiten zwischen mehreren Dateien werden verarbeitet.
- **Überprüfte Ausführung**: Code-Updates werden überprüft, um Halluzinationen zu reduzieren.

## Full-Stack-Funktionen

Google AI Studio nutzt die Leistungsfähigkeit des modernen Web-Ökosystems, sodass Sie mehr als nur clientseitige Prototypen erstellen können.

- **Serverseitige Laufzeit und npm**: Nutzen Sie die umfangreiche Bibliothek von npm-Paketen. Der Agent identifiziert und installiert Pakete automatisch nach Bedarf für Ihre App (z.B. bestimmte Bibliotheken für die Datenvisualisierung oder API-Clients). Sie können auch bestimmte Pakete anfordern.
- **Secret-Verwaltung**: Speichern Sie API-Schlüssel und Secrets sicher im
  **Menü Einstellungen**. Sie sind in Ihrem serverseitigen Code zugänglich und somit vor der Offenlegung auf der Clientseite geschützt.
- **Multiplayer**: Erstellen Sie direkt in
  AI Studio kollaborative Echtzeit-Erlebnisse. Die serverseitige Laufzeit verwaltet den Status und die Verbindungen, die für die Interaktion der Nutzer erforderlich sind.
- **Firebase-Integration**: Firebase wird automatisch bereitgestellt und eingerichtet, einschließlich der Firestore-Datenbank (permanente Datenspeicherung) und der Firebase-Authentifizierung (Anmeldeabläufe, insbesondere „Über Google anmelden“).
  Der Agent übernimmt den gesamten Einrichtungsprozess und schreibt sogar den Code in Ihrer App für diese Dienste.

[Weitere Informationen zum Entwickeln von Full-Stack-Anwendungen](https://ai.google.dev/gemini-api/docs/Weitere Informationen zum Entwickeln von Full-Stack-Anwendungen)

## Noch mehr erstellen

Nachdem Google AI Studio den ersten Code für Ihre Anwendung generiert hat, können Sie ihn weiter verfeinern:

### In Google AI Studio entwickeln

- **Mit Gemini iterieren**: Verwenden Sie den Chatbereich im **Build-Modus**, um Gemini zu bitten,
  Änderungen vorzunehmen, neue Funktionen hinzuzufügen oder das Styling zu ändern.
- **Code direkt bearbeiten**: Öffnen Sie im Vorschaufenster den Tab **Code** , um
  Live-Änderungen vorzunehmen.

### Extern entwickeln

Für komplexere Arbeitsabläufe können Sie den Code exportieren und in Ihrer bevorzugten Umgebung arbeiten:

- **Herunterladen und lokal entwickeln**: Exportieren Sie den generierten Code als **ZIP
  Datei** und importieren Sie ihn in Ihren Code-Editor.
- **In GitHub übertragen**: Integrieren Sie den Code in Ihre bestehenden Entwicklungs- und
  Bereitstellungsprozesse, indem Sie ihn in ein **GitHub-Repository** übertragen.

## Wichtige Features

Google AI Studio bietet mehrere Funktionen, mit denen der Erstellungsprozess intuitiv und visuell gestaltet werden kann:

- **Full-Stack-Anwendungen erstellen und iterieren**: Erstellen Sie Full-Stack-Anwendungen mit nur
  einem Prompt und iterieren Sie im Chat- oder **Anmerkungsmodus**. Im Anmerkungsmodus können Sie jeden Teil der Benutzeroberfläche Ihrer App hervorheben und die gewünschte Änderung beschreiben.
- **App freigeben und bereitstellen**: Sie können Ihre Kreationen für andere freigeben, um zusammenzuarbeiten oder Ihre Arbeit zu präsentieren. Wenn Ihre App bereit ist, stellen Sie sie in Cloud Run bereit.
- **App-Galerie**: Die App-Galerie bietet eine visuelle Bibliothek mit Projektideen.
  Sie können sich ansehen, was mit Gemini möglich ist, eine Vorschau von Anwendungen aufrufen und sie remixen, um sie an Ihre Bedürfnisse anzupassen.

## App bereitstellen oder archivieren

Wenn Ihre Anwendung fertig ist, können Sie sie bereitstellen:

- **Google Cloud Run**: Stellen Sie Ihre Anwendung als skalierbaren Dienst bereit.
  Je nach Nutzung können Kosten für [Google Cloud Run](https://ai.google.dev/gemini-api/docs/Google Cloud Run) anfallen.
- **GitHub**: Exportieren Sie Ihr Projekt in ein GitHub-Repository.

## Beschränkungen

In diesem Abschnitt sind die aktuellen Beschränkungen des Build-Modus in Google AI Studio aufgeführt.

### Sicherheit von API-Schlüsseln

- **Clientseitig**: Verwenden Sie niemals echte API-Schlüssel direkt im clientseitigen Code.
- **Serverseitig**: Verwenden Sie die Funktion zur Secret-Verwaltung, um vertrauliche Schlüssel
  sicher in der serverseitigen Laufzeit zu verarbeiten.

### Bereitstellung außerhalb von Google AI Studio

- Sie können Ihre App zwar in Cloud Run für eine öffentliche URL bereitstellen, aber bei dieser Einrichtung wird Ihr API-Schlüssel für alle Gemini API-Aufrufe der Nutzer verwendet.
  - JavaScript-Apps werden clientseitig ausgeführt. Achten Sie daher darauf, dass API-Schlüssel nur minimalen Zugriff haben, um Datenlecks oder Missbrauch zu verhindern. So können beispielsweise andere File Search Stores aus demselben Projekt für Nutzer über diesen Mechanismus zugänglich sein.
- Sichere externe Bereitstellung: Wenn Sie eine App sicher außerhalb von AI Studio ausführen möchten (z.B. nach dem Herunterladen der ZIP-Datei), müssen Sie die Logik, die den API-Schlüssel verwendet, in eine serverseitige Komponente verschieben, um zu verhindern, dass der Schlüssel für Endnutzer offengelegt wird. Dies ist nicht erforderlich, wenn Sie die Bereitstellung über Cloud Run vornehmen.
- Warnung vor der Offenlegung von Schlüsseln: Es wird dringend davon abgeraten, den Platzhalter in einer clientseitigen Umgebung einfach durch einen echten API-Schlüssel zu ersetzen, da der Schlüssel dann für alle Nutzer sichtbar ist.

### Fehler beim Freigeben von Apps

Wenn Sie Ihre App freigeben und Ihr Endnutzer beim Verwenden der freigegebenen URL den Fehler **403 Access Restricted** erhält, kann das folgende Ursachen haben:

- **Browsererweiterungen**: Datenschutzerweiterungen wie Privacy Badger blockieren möglicherweise die App. Deaktivieren Sie die Erweiterung, um den Fehler zu vermeiden.
- **Build-Probleme**: Es gibt möglicherweise Probleme mit dem aktuellen Code. Bitten Sie den Agenten, „alle Build-Probleme mit dem aktuellen Code zu beheben“, und geben Sie die URL dann noch einmal frei.

## FAQ

### Was ist „In AI Studio entwickeln“?

„In AI Studio entwickeln“ ist eine Plattform, mit der Sie mit Gemini aus einem einfachen Prompt eine produktionsreife, KI-basierte Anwendung erstellen können. Beschreiben Sie mit einem Prompt, was Sie erstellen möchten, und Gemini generiert eine App für Sie. Sie können auch unsere Galerie durchsuchen, um zu sehen, was mit der Gemini API möglich ist, und Apps remixen, um sie an Ihre Bedürfnisse anzupassen.

### Warum ruft „In AI Studio entwickeln“ die Gemini API aus clientseitigem Code auf?

Normalerweise ist es Best Practice, die Gemini API serverseitig aufzurufen, um Ihren API-Schlüssel nicht offenzulegen. AI Studio hat jedoch einen Gemini API-Proxy für clientseitige Aufrufe, der den API-Schlüssel anhängt, ohne ihn im Code offenzulegen. Derzeit generieren wir Aufrufe clientseitig, um diesen Proxy zu nutzen, da er den Code vereinfacht und Sie Ihre App für andere freigeben können, ohne einen API-Schlüssel angeben zu müssen.

### Wird mein API-Schlüssel beim Freigeben von Apps offengelegt?

Verwenden Sie in Ihrer App keinen echten API-Schlüssel, sondern einen Platzhalterwert.
`process.env.GEMINI_API_KEY` ist auf einen Platzhalterwert festgelegt, den Sie verwenden können.
Wenn ein anderer Nutzer Ihre App verwendet, leitet AI Studio die Aufrufe an die Gemini
API weiter und ersetzt den Platzhalterwert durch *den API-Schlüssel des Nutzers* (nicht Ihren).
Verwenden Sie in Ihrer App keinen echten API-Schlüssel, da der Code für alle sichtbar ist, die Ihre App aufrufen können.

### Wer kann meine Apps sehen?

Standardmäßig ist Ihre App privat. Sie können Ihre App für andere Nutzer freigeben, damit sie sie verwenden können. Nutzer, für die Sie Ihre App freigeben, können den Code sehen und ihn für ihre eigenen Zwecke kopieren. Wenn Sie Ihre App mit Bearbeitungsberechtigung freigeben, können die anderen Nutzer den Code Ihrer App bearbeiten.

### Kann ich Apps außerhalb von AI Studio ausführen?

Sie können Ihre App aus AI Studio in [Cloud Run](https://ai.google.dev/gemini-api/docs/Cloud Run) bereitstellen. Dadurch erhält Ihre App eine öffentliche URL. Sie wird zusammen mit einem Proxyserver bereitgestellt, der Ihren API-Schlüssel privat hält. Die bereitgestellte App verwendet jedoch Ihren API-Schlüssel für alle Gemini API-Aufrufe der Nutzer. Sie können Ihre App auch als ZIP-Datei herunterladen. Wenn Sie den Platzhalterwert durch einen echten API-Schlüssel ersetzen, sollte die App weiterhin funktionieren. Sie *sollten* Ihre App jedoch nicht auf diese Weise bereitstellen, da der API-Schlüssel dann für alle Nutzer sichtbar ist. [Wenn eine App sicher außerhalb von AI Studio ausgeführt werden soll, muss ein Teil der Logik serverseitig verschoben werden, damit der API-Schlüssel nicht mehr offengelegt wird.](https://ai.google.dev/gemini-api/docs/Wenn eine App sicher außerhalb von AI Studio ausgeführt werden soll, muss ein Teil der Logik serverseitig verschoben werden, damit der API-Schlüssel nicht mehr offengelegt wird.)

### Kann ich Apps lokal mit meinen eigenen Tools entwickeln und sie dann hier freigeben?

Diese Funktion ist noch nicht verfügbar. Wir arbeiten daran, in Zukunft weitere Anwendungsfälle für Apps zu unterstützen. Wenn Sie etwas Bestimmtes im Sinn haben, geben Sie uns bitte Feedback.

### Wie kann ich eine Datenbank oder anderen Speicher mit meinen Apps verwenden?

AI Studio-Apps sind Standard-Apps, die in einem Cloud Run-Container ausgeführt werden. Sie können jede Speicherlösung verwenden, mit der Sie über ein Netzwerk eine Verbindung herstellen können, sofern keine Firewall den Zugriff von einem dynamischen IP-Bereich aus verhindert.

Wir arbeiten daran, in Zukunft direkte Unterstützung für Speicher hinzuzufügen, die Sie direkt in AI Studio konfigurieren können.

### Wie kann ich auf das Mikrofon, die Webcam und andere Navigator APIs zugreifen?

Damit Nutzer wissen, dass eine App ihre Webcam oder andere
Geräte verwendet, ist eine zusätzliche Bestätigung erforderlich, bevor die App auf diese
[Navigator APIs](https://ai.google.dev/gemini-api/docs/Navigator APIs) zugreifen kann.
App-Entwickler können diese Berechtigungsanfragen der Datei `metadata.json` ihrer App hinzufügen. Beispiel:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Die unterstützten Werte für `requestFramePermissions` sind eine Teilmenge der
standardmäßigen [richtlinienbasierten Funktionen](https://ai.google.dev/gemini-api/docs/richtlinienbasierten Funktionen).

### Wie kann ich GitHub mit meinen Apps verwenden?

Mit der GitHub-Integration von AI Studio können Sie ein Repository für Ihre Arbeit erstellen und Ihre letzten Änderungen übertragen. Das Abrufen von Remote-Änderungen wird derzeit nicht unterstützt.

### Kann ich anderen Nutzern Bearbeitungszugriff auf meine App gewähren?

Diese Funktion wird noch nicht unterstützt, ist aber bald verfügbar.

### Warum wurde meine App wegen eines Richtlinienverstoßes gemeldet?

Wir haben Systeme, die Apps automatisch überprüfen, um sicherzustellen, dass sie unseren Richtlinien entsprechen. Wenn wir feststellen, dass eine App gegen unsere Richtlinien verstößt, wird sie aus AI Studio entfernt. Beispiele für Richtlinienverstöße:

- Apps, die Malware, Phishing oder Identitätsdiebstahl enthalten
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu visuellen Darstellungen des sexuellen Missbrauchs von Kindern verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu Belästigung verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu Hassreden verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu Menschenhandel verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu sexuell expliziten Inhalten verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu Gewalt und Gewaltdarstellungen verstoßen
- Apps, die Inhalte anzeigen oder verbreiten, die gegen die Richtlinie zu schädlichen oder gefährlichen Inhalten verstoßen

Wenn Ihre App wegen eines Richtlinienverstoßes gemeldet wurde und Sie der Meinung sind, dass dies fälschlicherweise geschehen ist, können Sie Einspruch einlegen. Wiederholte Verstöße gegen unsere Richtlinien können dazu führen, dass Ihr Zugriff auf AI Studio beendet wird.

### Was sind meine Pflichten als App-Entwickler?

Als Eigentümer Ihrer Anwendung sind Sie für ihr Verhalten und alle Daten verantwortlich, die sie verarbeitet. Dazu zählen:

- **Einhaltung von Gesetzen und Rechten Dritter**:Ihre App muss allen anwendbaren Gesetzen und Vorschriften entsprechen und darf nicht gegen die Rechte anderer verstoßen, einschließlich geistiger Eigentumsrechte und des Rechts auf Privatsphäre.
- **Inhaltsüberwachung:** Für andere Dienste, die von Ihrer App verwendet werden, gelten möglicherweise zusätzliche Bedingungen. Gemäß den [Google Cloud-Nutzungsbedingungen](https://ai.google.dev/gemini-api/docs/Google Cloud-Nutzungsbedingungen), die für Firestore gelten, müssen Kunden, die Inhalte von Dritten hosten, beispielsweise Richtlinien veröffentlichen, in denen verbotene Inhalte definiert sind (z.B. illegale Inhalte), und die Inhalte auf das Vorhandensein solcher illegalen Inhalte überwachen.
- **Sichere Implementierung**:Sie müssen die erforderlichen Sicherheitsmaßnahmen und Moderationstools implementieren, um den Missbrauch Ihrer Anwendung zu verhindern.

Beachten Sie die [Nutzungsbeschränkungen](https://ai.google.dev/gemini-api/docs/Nutzungsbeschränkungen)
in den Nutzungsbedingungen.

### Welche Bedingungen gelten für Apps in der App-Galerie in AI Studio?

Für die Nutzung von Apps in der App-Galerie in AI Studio gelten die [Zusatzbedingungen für die Gemini API](https://ai.google.dev/gemini-api/docs/Zusatzbedingungen für die Gemini API), sofern nichts
anderes angegeben ist.

## Nächste Schritte

- [Full-Stack-Anwendungen entwickeln](https://ai.google.dev/gemini-api/docs/Full-Stack-Anwendungen entwickeln)
- Beispiele in der [App-Galerie](https://ai.google.dev/gemini-api/docs/App-Galerie) ansehen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 License) und Codebeispiele unter der [Apache 2.0 License](https://ai.google.dev/gemini-api/docs/Apache 2.0 License) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://ai.google.dev/gemini-api/docs/Websiterichtlinien von Google Developers). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?
