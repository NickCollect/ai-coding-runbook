---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=de
fetched_at: 2026-06-15T06:21:40.601300+00:00
title: "KI-Agenten in AI\u00a0Studio Playground \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# KI-Agenten in AI Studio Playground

Google AI Studio Playground bietet eine visuelle Oberfläche, mit der Sie Prototypen erstellen und lernen können, wie Sie verwaltete Agents entwickeln, ohne API-Aufrufe erstellen und schreiben zu müssen.

Rufen Sie dazu in der Navigationsleiste von Google AI Studio den Tab **Playground** auf und stellen Sie den Schalter auf **Agents**.

## Vordefinierte Vorlagen

Auf dem Tab **Agents** (KI-Agenten) finden Sie eine Reihe von Vorlagen, mit denen der Antigravity-Basis-KI-Agent durch Festlegen von Tool- und Umgebungskonfigurationen vorkonfiguriert wird. Alle Vorlagen sind Open Source und werden im Repository [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/) veröffentlicht. Wenn Sie sich diese Vorlagen ansehen, können Sie lernen, wie Sie Ihren eigenen verwalteten Agent erstellen und strukturieren.

Wenn Sie beispielsweise die Vorlage „KI‑Radio“ auswählen, werden alle zulässigen Tools aktiviert und eine spezielle `AGENTS.md`-Datei sowie Skills für die Produktion von Radiosendungen verknüpft. Sie können diese Einstellungen in der Playground-Benutzeroberfläche im Bereich **Environment** (Umgebung) aufrufen, indem Sie auf die Schaltfläche **Sources** (Quellen) klicken.

## Toolkonfiguration

In den Agent-Einstellungen im Playground können Sie den Zugriff auf die folgenden integrierten Tools aktivieren oder deaktivieren:

- **Google Suche**:Auf das öffentliche Web zugreifen, um Echtzeitinformationen zu erhalten.
- **URL-Kontext**:Textinhalte bestimmter Webseiten-URLs abrufen und parsen.
- **Codeausführung**:Bash- und Python-Befehle direkt in der isolierten Sandbox-Umgebung ausführen.
- **Dateisystemtools**:Dateien im Arbeitsbereich lesen, schreiben, auflisten und löschen.

## Umgebung konfigurieren

Verwaltete Agents werden in einer sicheren, kurzlebigen Linux-Sandbox (der Umgebung) ausgeführt, die den Arbeitsbereich und die Tools bereitstellt, die sie für ihre Arbeit benötigen. Weitere Informationen finden Sie im Leitfaden zur [verwalteten Agent-Umgebung](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de).

### Agent-Verhalten steuern

Das Verhalten, die Persona und die Funktionen des Agenten werden hauptsächlich durch die Dateien in seiner Umgebung bestimmt. Der Agent erkennt und lädt Konfigurationen automatisch aus einem speziellen `.agents`-Ordner:

- **`AGENTS.md`**: Vorgegeben im Kontext des Agenten, um Systemanweisungen und Persona zu definieren.
- **`SKILL.md`**: Diese Dateien befinden sich in den jeweiligen Skill-Ordnern (z.B. `.agents/skills/my-skill/SKILL.md`), um bestimmte Funktionen und Workflows zu definieren.

### Umgebung bereitstellen

Sie können die vom Agent verwendete Umgebung konfigurieren, indem Sie Dateien in die Umgebung einbinden, bevor Sie eine Sitzung starten. Sie können entweder eine neue Umgebung erstellen, indem Sie Quellen einbinden, oder eine vorherige Umgebung wiederherstellen:

- **So erstellen Sie eine neue Umgebung**: Klicken Sie im Bereich „Umgebungseinstellungen“ auf **Quellen hinzufügen** und wählen Sie einen der folgenden Quelltypen aus:

| Quelltyp | Beschreibung | Bereitstellungspfad |
| --- | --- | --- |
| **Inline-Dateien** | Konfigurationsdateien, Mock-Datasets oder Utility-Scripts (bis zu 100 KB) können direkt in die Playground-Benutzeroberfläche geschrieben oder eingefügt werden. | Benutzerdefinierter Zielpfad (z.B. `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Einen öffentlichen oder privaten Cloud Storage-Bucket einbinden  Für private Buckets ist ein standardmäßiges OAuth 2.0-Inhabertoken erforderlich. Weitere Informationen finden Sie unter [Private Quellen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de#private-sources). | Ordnet einen GCS-Bucket-Pfad (z.B. `gs://your-bucket-name/data/`) einem Workspace-Verzeichnis (z.B. `/workspace/data/`) zu. |
| **GitHub-Repositories** | Öffentliche oder private Codebases klonen  Für private Repositories ist die Standardauthentifizierung mit Ihrem persönlichen GitHub-Zugriffstoken (Personal Access Token, PAT) erforderlich. Weitere Informationen finden Sie unter [Private Quellen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de#private-sources). | Direkt in `/workspace/` geklont (in der Regel unter `/workspace/<repo-name>`). |

- **Wenn Sie eine frühere Umgebung wiederherstellen möchten**, können Sie [eine vorhandene Umgebungs-ID wiederverwenden](#reusing-an-existing-environment-id), um ihren genauen Status zu klonen und zu forken.

### Vorhandene Umgebungs-ID wiederverwenden

Wenn Sie bereits eine Sandbox-Umgebung eingerichtet haben, müssen Sie nicht von vorn beginnen. So verwenden Sie eine vorhandene Umgebung:

1. Rufen Sie in AI Studio den Bereich „Umgebungen“ auf und stellen Sie **Typ** auf **Vorhanden** um.
2. Geben Sie die **Umgebungs-ID** ein, z. B. `env_abc123`.

Weitere Informationen finden Sie unter [Umgebung konfigurieren](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de#configure-an-environment). Sie können die Umgebungs-ID der aktuellen Sitzung auch auf dem Tab „Umgebung“ in der Benutzeroberfläche abrufen.

Sobald Sie Ihre erste Nachricht an den Agent senden, ist die Umgebungskonfiguration für diese Sitzung festgelegt. Sie können keine neuen Quellen einbinden oder die Zulassungsliste für das Netzwerk ändern, während die Interaktion aktiv ausgeführt wird.

## Umgebung herunterladen

Nachdem eine Umgebung erstellt wurde, können Sie den Umgebungs-Snapshot jederzeit über die Schaltfläche **Herunterladen** in den Umgebungseinstellungen des AI Studio Playgrounds herunterladen, um Umgebungsdateien als Tarball abzurufen.

## Sicherheit und Kostenverwaltung

### Tokenverbrauch verwalten

Im Gegensatz zu einer Standard-Chatanfrage, die eine einzelne Ausgabe erzeugt, führt der Antigravity-Agent einen autonomen Workflow aus. Es plant, führt Code aus, beobachtet Ergebnisse und wiederholt den Vorgang. Das bedeutet, dass ein einzelner Prompt zu einem unbegrenzten Tokenverbrauch führen kann.

Um die Kosten zu verwalten, **geben Sie in Ihren Prompts klare Beendigungskriterien an und begrenzen Sie die Aufgaben für den Agenten**. Ein gutes Beispiel ist der Prompt: *Überprüfe die Pull-Anfrage und stoppe, sobald du die Markdown-Zusammenfassung erstellt hast.
Versuchen Sie nicht, die Korrektur selbst zu schreiben.*

### Zusätzliche Kosten

Standardmäßig haben alle Agent-Vorlagen im Playground Zugriff auf den Gemini API-Dienst und können API-Aufrufe aus der Umgebung ausführen, um Anfragen zu bearbeiten. Dabei können zusätzliche Kosten anfallen, die nicht im Tokenverbrauch berücksichtigt werden.

Wenn Sie andere externe Dienste hinzufügen, können für den Agenten zusätzliche Kosten anfallen, da er diese Dienste in Ihrem Namen aufruft.

### Zulassungsliste für Netzwerke

Standardmäßig werden in AI Studio alle ausgehenden Netzwerkanfragen aus der Sandbox-Umgebung Ihres Agents streng kontrolliert und eingeschränkt, um die Sicherheit zu gewährleisten. Damit Ihr Agent externe APIs, Webservices oder Paketmanager erreichen kann, müssen Sie diese explizit deklarieren:

1. Rufen Sie in AI Studio das Feld „Umgebungen“ auf.
2. Klicken Sie neben **Netzwerk** auf die Schaltfläche **Regeln**.
3. Klicken Sie im Bereich **Netzwerkkonfiguration** auf **Zur Zulassungsliste hinzufügen** und geben Sie die entsprechenden Details ein:
   - **Domainbeschränkung**:Nur auf die bestimmten Domains oder Platzhaltermuster, die der Liste hinzugefügt wurden, kann über die virtuelle Maschine des Agents zugegriffen werden. Sie können beispielsweise genaue Domains wie `api.github.com` oder allgemeine Muster wie `*.googleapis.com` eingeben.
   - **HTTP-Header und Token-Injection hinzufügen**:Mit der Option **HTTP-Header hinzufügen** können Sie erforderliche Anmeldedaten (z. B. ein API-Token) für eine bestimmte Domain sicher einfügen. Diese Anmeldedaten werden sicher über einen Egress-Proxy weitergeleitet und niemals direkt als Rohtext in der Agent-Sandbox offengelegt.

Seien Sie immer vorsichtig, wenn Sie Domains auf die Zulassungsliste setzen. Wenn Sie dem Agent Zugriff auf authentifizierte Dienste gewähren, kann er in Ihrem Namen handeln. Wenn Sie das nicht sorgfältig überwachen, kann das zu unbeabsichtigten Aktionen führen.

### Best Practices für Anmeldedaten

Wenn für Ihren Workflow eine Authentifizierung des Agenten bei externen Diensten erforderlich ist, sind Sie für die Bereitstellung und den Umfang dieser Anmeldedaten verantwortlich. Befolgen Sie diese Richtlinien, um das Risiko zu verringern:

- **Anmeldedaten mit geringsten Berechtigungen verwenden**:Erstellen Sie Dienstkonten oder API-Schlüssel mit nur den Berechtigungen, die Ihr Agent benötigt. Vermeiden Sie die Übergabe von Anmeldedaten mit umfassendem oder administrativem Zugriff.
- **Kurzlebige Tokens bevorzugen**:Verwenden Sie nach Möglichkeit zeitlich begrenzte Anmeldedaten oder Tokens, die ablaufen, anstatt langlebiger API-Schlüssel.
- **Vollzugriff annehmen**:Der Agent kann alle Anmeldedaten verwenden, auf die er Zugriff hat, um die von Ihnen erteilte Aufgabe auszuführen. Geben Sie nur Anmeldedaten an, deren vollständigen Zugriffsbereich Sie gewähren möchten.
- **Anmeldedaten regelmäßig rotieren**:Behandeln Sie Anmeldedaten, die für den Agenten freigegeben wurden, genauso wie alle anderen programmatischen Anmeldedaten. Rotieren Sie sie regelmäßig.

### Verbindung zu externen Tools und APIs herstellen

Sie können externe Tools und APIs (z. B. Model Context Protocol-/MCP-Server) verbinden, um die Funktionen des Agenten zu erweitern. Dabei gilt:

- Verbinden Sie nur Tools von Quellen, denen Sie vertrauen. Ein böswilliges oder schlecht geschriebenes Tool kann Daten offenlegen oder unbeabsichtigte Aktionen ausführen.
- Konfigurieren Sie Tools mit den für Ihren Anwendungsfall erforderlichen Mindestberechtigungen. Wenn ein Tool den schreibgeschützten Modus unterstützt, sollten Sie diesen bevorzugen, es sei denn, Schreibvorgänge sind unbedingt erforderlich.
- Bevor Sie ein Tool mit einer Produktionsdatenquelle verbinden, sollten Sie es mit Beispiel- oder synthetischen Daten testen, um zu prüfen, ob der Agent es wie erwartet verwendet.

### Menschliche Aufsicht

KI-Agenten können mehrstufige Workflows mit einem hohen Maß an Autonomie planen, begründen und ausführen. Das ist zwar leistungsstark, bedeutet aber auch, dass Sie für eine angemessene Aufsicht sorgen müssen, insbesondere bei Aufgaben, die Daten ändern oder mit externen Systemen interagieren.

Prüfen Sie immer kritische Ausgaben wie generierten Code, Datentransformationen oder Konfigurationsänderungen, bevor Sie sie bereitstellen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-20 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-20 (UTC)."],[],[]]
