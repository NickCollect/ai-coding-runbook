---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=de
fetched_at: 2026-07-27T04:50:21.685536+00:00
title: "Coding-Assistenten mit Gemini MCP und Skills einrichten \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Coding-Assistenten mit Gemini MCP und Skills einrichten

KI-Programmierassistenten sind leistungsstark, haben aber auch Einschränkungen: Die Trainingsdaten sind auf ein bestimmtes Datum begrenzt und enthalten keine neuen API-Funktionen und ‑Änderungen. Ohne Zugriff auf die Gemini-spezifische Dokumentation schlagen KI-Agenten möglicherweise generische Muster anstelle optimierter Ansätze vor.

Damit Ihr Programmierassistent immer auf dem neuesten Stand der sich entwickelnden Gemini API und ihrer empfohlenen Verwendung ist, empfehlen wir, den **Gemini Docs MCP** einzurichten und Ihre Umgebung mit **Gemini API-Skills** zu erweitern. Diese Tools können zwar unabhängig voneinander verwendet werden, sind aber so konzipiert, dass sie zusammenarbeiten, um eine vollständige Abdeckung zu bieten.

## Gemini Docs MCP verbinden

Gemini hostet einen öffentlichen MCP-Server (Model Context Protocol) unter `https://gemini-api-docs-mcp.dev`. Wenn Sie Ihren Programmieragenten mit diesem Server verbinden, haben alle Abfragen Zugriff auf die neuesten APIs, Codeupdates und Beispiele für optimale Konfigurationen.

Führen Sie den folgenden Befehl im Terminal oder im Stammverzeichnis des Projekts Ihres Agenten aus, um den Server zu installieren:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Dieser Server fügt eine Funktion `search_documentation` hinzu, mit der Ihr Agent Echtzeit-API-Definitionen und Integrationsmuster aus den offiziellen Gemini-Dokumentationsdateien abrufen kann.

## API-Entwicklungs-Skills hinzufügen

Die Skills enthalten **integrierte Regeln und Best Practices** (z. B. die Erzwingung der richtigen SDK- und aktuellen Modellversionen) direkt im Kontext Ihres Assistenten. Der Skill funktioniert mit dem Gemini Docs MCP-Dienst zusammen: Wenn Sie beide installiert haben, verwendet der Skill den MCP-Dienst für die Dokumentation. Auch ohne installierten MCP ruft er `llms.txt` von `ai.google.dev` als Fallback ab.

Verwenden Sie eines der folgenden unterstützten Tools, um diese Skills zu installieren. Installationsanleitungen für beide Tools finden Sie unter jedem Skill-Modul:

- **[skills.sh](https://skills.sh)**: Empfohlen. Der offene Standard für portable Agentenverhaltensweisen.
- **[Context7](https://context7.com)**

### gemini-api-dev

Der grundlegende Skill für die allgemeine Gemini-Entwicklung. Dieser Skill bietet Dokumentation und Best Practices für folgende Bereiche:

- Weiterleitung von Prompts an aktuelle Modelle (z.B. Gemini 3.1 Pro/Flash) und Vermeidung veralteter Modelle
- Multimodale Prompts, Funktionsaufrufe, strukturierte Ausgaben und gängige Integrationsmuster

#### Mit skills.sh installieren

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Mit Context7 installieren

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Skill zum Erstellen von konversationellen KI-Anwendungen in Echtzeit mit der Gemini Live API. Dieser Skill bietet Dokumentation und Best Practices für folgende Bereiche:

- WebSocket-Verbindungen für Streaming mit niedriger Latenz
- Streaming von Audio, Video und Text
- Erkennung von Sprachaktivität und Unterstützung für das Unterbrechen von Sprachausgaben

#### Mit skills.sh installieren

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Mit Context7 installieren

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Skill zum Erstellen von Apps mit der
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de). Die Interactions API ist die einfachste und beste Möglichkeit, mit Gemini-Modellen und ‑Agenten zu arbeiten. Dieser Skill umfasst folgende Bereiche:

- Textgenerierung, mehrstufiger Chat und Streaming
- Funktionsaufrufe, strukturierte Ausgabe und Bildgenerierung
- Hintergrundausführung und Deep Research-Agenten
- Serverseitige Verwaltung des Konversationsstatus
- SDK-Muster für Python und TypeScript

#### Mit skills.sh installieren

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Mit Context7 installieren

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Installation prüfen

Bestätigen Sie nach der Installation, dass Ihr Programmierassistent eine Verbindung zum Gemini Docs MCP-Server herstellen und Ihre installierten Skills verwenden kann.

### 1. Agentenverhalten prüfen

Am zuverlässigsten können Sie das überprüfen, indem Sie Ihrem Agenten eine technische Frage zur Gemini API stellen.

**Prompt** : „Wie verwende ich das Kontext-Caching mit der Gemini API?“

Eine erfolgreiche Einrichtung hat folgende Auswirkungen:

- **Genaue Codeausgabe**: Verweisen Sie auf bestimmte Gemini-Methoden wie `cacheContent` oder `cachedContents.create` von den neuesten Endpunkten.
- **MCP-Tool verwenden**: Zeigen Sie, dass es mit dem **Gemini Docs MCP-Server** verbunden ist oder das `search_documentation` Tool verwendet, um Daten abzurufen.
- **Geladene Skills aufrufen**: Zeigen Sie einen Hinweis an, dass der Skill „gemini-api-dev“ verwendet wird (wenn ein sekundärer Wrapper verwendet wird).

### 2. Manifeste und Tools prüfen

Wenn der Agent eine allgemeine oder generische Antwort gibt, verwenden Sie die spezifischen Discovery- oder Statusbefehle für Ihre Umgebung, um zu prüfen, ob der Docs MCP oder Skill in den Arbeitsspeicher geladen wurde.

| Umgebung | MCP-Überprüfung | Skill-Überprüfung |
| --- | --- | --- |
| **Claude Code** | Geben Sie im Terminal `/mcp` ein, um aktive Server und `search_documentation`-Tools aufzurufen. | Geben Sie im Terminal `/skills` ein, um alle aktiven Manifeste aufzulisten. |
| **Cursor** | Rufen Sie **Einstellungen > Funktionen > MCP** auf. Prüfen Sie, ob der Server „Verbunden“ ist. | Öffnen Sie **Einstellungen > Regeln**. Prüfen Sie, ob der Skill unter „Agent entscheidet“ angezeigt wird. |
| **Antigravity** | Prüfen Sie in der Seitenleiste **Anpassungen > Verbindungen** den MCP-Status. | Geben Sie `/skills list` ein oder prüfen Sie die Seitenleiste **Anpassungen > Regeln**. |
| **Gemini CLI** | Führen Sie `gemini mcp list` aus oder verwenden Sie `/mcp list`. | Führen Sie `gemini skills list` aus oder verwenden Sie den Schrägstrichbefehl `/skills` in der Sitzung. |
| **Copilot** | Geben Sie `@gemini /mcp` ein, um aktive Daten-Connectors aufzulisten. | Geben Sie `@gemini /skills` (oder `/skills`) ein, um aktive Erweiterungen aufzurufen. |

## Fehlerbehebung

Wenn Ihr Agent nur allgemeine Informationen liefert oder Gemini-spezifische Methoden nicht erkennt, prüfen Sie Folgendes:

### Agent hat den Skill nicht gefunden

Die meisten Agenten indexieren Skills nur beim Start.

**Lösung**:Starten Sie Ihre IDE (Cursor/VS Code) vollständig neu oder beenden Sie Ihren terminalbasierten Agenten (Claude Code) und öffnen Sie ihn noch einmal.

### Globaler vs. lokaler Konflikt

Wenn Sie die Installation mit dem Flag `--global` ausgeführt haben, ignoriert Ihr Agent dieses Flag möglicherweise zugunsten projektspezifischer Regeln.

**Lösung**:Installieren Sie den Skill direkt im Stammverzeichnis Ihres Projekts ohne das globale Flag:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Ressourcen

- [Gemini API-Skills auf GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de)
- [Jetzt starten](https://ai.google.dev/gemini-api/docs/get-started?hl=de)
- [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-08 (UTC)."],[],[]]
