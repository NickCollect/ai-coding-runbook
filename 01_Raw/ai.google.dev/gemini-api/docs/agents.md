---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=de
fetched_at: 2026-09-07T05:39:37.687572+00:00
title: "Agenten\u00a0\u2013 \u00dcbersicht \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Agenten – Übersicht

Verwaltete KI-Agenten in der Gemini API bieten Ihnen eine konfigurierbare Agentenplattform. Mit einem einzigen API-Aufruf wird eine Linux-Sandbox bereitgestellt, in der der Agent autonom Schlussfolgerungen zieht, Code ausführt, Dateien verwaltet und im Web surft.

[rocket\_launch

Kurzanleitung

Ersten Agentenaufruf ausführen, Antworten streamen und benutzerdefinierten Agenten erstellen](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de)
[smart\_toy

Antigravity-Agent

Funktionen, Tools, multimodale Eingabe und Preise für den Standardagenten](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)
[experiment

Agenten in AI Studio

Visuelle Sandbox für das Prototyping von Agenten ohne Code](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=de)

## Verfügbare verwaltete KI-Agenten

- **[Antigravity-Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)**: Verwalteter Agent für allgemeine Zwecke, der auf Gemini 3.7 Flash basiert. Führt Code aus, verwaltet Dateien und durchsucht das Web in einer sicheren Linux-Sandbox, die von Google gehostet wird. Sie können
  das zugrunde liegende Modell (z. B. Gemini 3.7 Flash, Gemini 3.6 Flash oder Gemini 3.5 Flash)
  mit `agent_config` konfigurieren und es mit eigenen Anweisungen, Skills und Daten erweitern, um
  [einen benutzerdefinierten Agenten zu erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de)**: Autonomer Recherche-Agent, der mehrstufige Rechercheaufgaben für Anwendungsfälle wie Marktanalysen, Due-Diligence-Prüfungen und Literaturrecherchen plant, ausführt und zusammenfasst.

## Sicherheit und Best Practices

Jeder Agent wird in einer Sandbox-Umgebung ausgeführt, die auf Betriebssystemebene isoliert ist.
Die Sandbox hat standardmäßig uneingeschränkten ausgehenden Netzwerkzugriff. Sie können den Netzwerkzugriff mit einer Zulassungsliste einschränken oder deaktivieren.

### Netzwerkzugriff

Standardmäßig haben Umgebungen uneingeschränkten ausgehenden Netzwerkzugriff. Verwenden Sie eine `network`-Zulassungsliste, um den ausgehenden Traffic auf bestimmte Domains oder Platzhaltermuster zu beschränken. Weitere Informationen zur Konfiguration finden Sie unter
[Zulassungsliste für Netzwerke](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=de#network_allow_list) (AI
Studio) oder [Netzwerkregeln](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de#with_network_rules)
(API).

### Externe Tools und APIs

Sie können externe Tools und APIs verbinden, um den Agenten zu erweitern. Verwenden Sie nur Tools aus vertrauenswürdigen Quellen und beschränken Sie die Berechtigungen auf das Minimum. Anmeldedaten können sicher über Egress-Proxy-Header-Transformationen eingefügt werden und werden in der Sandbox nie offengelegt. Der Agent kann alle Anmeldedaten verwenden, auf die er Zugriff hat. Geben Sie daher nur Anmeldedaten an, deren vollen Umfang Sie gewähren möchten.

- Verwenden Sie Dienstkonten oder API-Schlüssel mit den geringsten Berechtigungen.
- Bevorzugen Sie kurzlebige Tokens gegenüber langlebigen Schlüsseln.
- Geben Sie nur Anmeldedaten an, deren vollen Umfang Sie gewähren möchten.
- Rotieren Sie Anmeldedaten regelmäßig.

Weitere Informationen zum Konfigurieren von Header-Transformationen finden Sie unter
[Anmeldedaten](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de#credentials).

### Menschliche Aufsicht

Überprüfen Sie die Ausgaben (generierter Code, Datentransformationen, Konfigurationsänderungen) immer, bevor Sie sie bereitstellen, insbesondere bei Aufgaben, bei denen Daten geändert werden oder mit externen Systemen interagiert wird.

## Preise

Für verwaltete KI-Agenten gilt ein [Pay as you go-Modell](https://ai.google.dev/gemini-api/docs/pricing?hl=de#pricing-for-agents)
das auf Gemini-Modell-Tokens und der Toolnutzung basiert. Eine einzelne Interaktion kann mehrere Reasoning-Schleifen auslösen, wobei in der Regel 100.000 bis 3 Millionen Tokens verbraucht werden. Die Compute-Kosten für die Umgebung werden während der Vorschau **nicht in Rechnung gestellt**. Die [geschätzten Kosten](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de#availability-and-pricing)
für die Aufschlüsselung nach Aufgabe finden Sie hier. Verwaltete KI-Agenten sind auch im kostenlosen Abo mit einem kostenlosen Ratenlimit und Nutzungskontingent verfügbar.

## Limits

| Limit | Beschreibung |
| --- | --- |
| **Lebensdauer der Umgebung** | Umgebungen werden nach 7 Tagen Inaktivität endgültig gelöscht. |
| **VM-Herunterfahren** | VMs werden nach kurzer Inaktivität heruntergefahren, um Ressourcen zu sparen. Bei der nächsten Anfrage wird der Status wiederhergestellt (mit einem Kaltstart). |
| **Vorinstallierte Software** | Ubuntu-basierte Umgebung mit Python 3.12 und Node.js 22. Weitere Informationen zum Basis-Image der Umgebung finden Sie unter [Vorinstallierte Software](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de#pre-installed-software). |
| **Maximale Anzahl von Agenten** | Sie können bis zu 1.000 verwaltete KI-Agenten haben. |

## Agenten-Frameworks

Sie können auch Agenten mit Gemini und den folgenden Frameworks und SDKs erstellen:

- [**\*\*LangChain / LangGraph\*\***](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=de): Erstellen Sie
  zustandsorientierte, komplexe Anwendungsabläufe und Multi-Agent-Systeme mit Graph
  strukturen.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=de): Verbinden Sie Gemini-Agenten mit
  Ihren privaten Daten für RAG-optimierte Workflows.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=de): Orchestrieren Sie kollaborative,
  Rollenspiel-basierte autonome KI-Agenten.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=de): Erstellen Sie
  KI-gestützte Benutzeroberflächen und Agenten in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): An
  Open-Source-Framework zum Erstellen und Orchestrieren interoperabler KI
  Agenten.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=de): Erstellen Sie
  autonome KI-Agenten mit denselben Tools, derselben Agentenschleife und derselben Kontext
  verwaltung, die Google Antigravity zugrunde liegen. Programmierbar in Python.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-08-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-08-19 (UTC)."],[],[]]
