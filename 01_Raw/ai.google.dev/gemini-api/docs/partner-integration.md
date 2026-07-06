---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=de
fetched_at: 2026-07-06T05:12:06.853854+00:00
title: "Partner- und Bibliotheksintegrationen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Partner- und Bibliotheksintegrationen

In diesem Leitfaden werden Architekturstrategien für die Entwicklung von Bibliotheken, Plattformen und Gateways auf Grundlage der Gemini API beschrieben. Außerdem werden die technischen Kompromisse zwischen der Verwendung der offiziellen GenAI SDKs, der Direct API (REST/gRPC) und der OpenAI-Kompatibilitätsebene erläutert.

Dieser Leitfaden richtet sich an Entwickler, die Tools für andere Entwickler erstellen, z. B. Open-Source-Frameworks, Enterprise-Gateways oder SaaS-Aggregatoren, und die die Abhängigkeitshygiene, die Bundle-Größe oder die Feature-Parität optimieren müssen.

## Was ist eine Partnerintegration?

Ein Partner ist jeder, der eine Integration zwischen der Gemini API und Endnutzerentwicklern erstellt. Wir unterteilen Partner in vier Archetypen. Wenn Sie wissen, zu welchem Archetyp Sie am besten passen, können Sie den richtigen Integrationspfad auswählen.

#### Ökosystem-Framework

- **Wer Sie sind**:Maintainer eines Open-Source-Frameworks (z.B. LangChain, LlamaIndex, Spring AI) oder sprachspezifischer Clients.
- **Ihr Ziel**:Breite Kompatibilität. Ihre Bibliothek soll in jeder Umgebung funktionieren, die der Nutzer auswählt, ohne Konflikte zu verursachen.

#### Laufzeit- und Edge-Plattform

- **Wer Sie sind**:SaaS-Plattformen, KI-Gateways oder Cloud-Infrastrukturanbieter (z.B. Vercel, Cloudflare, Zapier), bei denen die Codeausführung in eingeschränkten Umgebungen erfolgt.
- **Ihr Ziel**:Leistung. Sie benötigen eine geringe Latenz, eine minimale Bundle-Größe und schnelle Kaltstarts.

#### Dienstleister

- **Wer Sie sind**:Plattformen, Proxys oder interne „Model Gardens“, die den Zugriff auf viele verschiedene LLM-Anbieter (z.B. OpenAI, Anthropic, Google) über eine einzige Schnittstelle normalisieren.
- **Ihr Ziel**:Portabilität und Einheitlichkeit.

#### Enterprise-Gateway

- **Wer Sie sind**:Interne Platform Engineering-Teams in großen Unternehmen, die „Golden Paths“ für Hunderte von internen Entwicklern erstellen.
- **Ihr Ziel**:Standardisierung, Governance und einheitliche Authentifizierung.

## Vergleich auf einen Blick

**Globale Best Practice:** Alle Partner müssen den [`x-goog-api-client`
Header](#client-id) senden, unabhängig vom gewählten Pfad.

| Wenn Sie... | Empfohlener Pfad | Vorteil | Wichtigster Kompromiss | Best Practice |
| --- | --- | --- | --- | --- |
| **Enterprise-Gateway, Ökosystem-Framework** | **[Google GenAI SDK](#genai-sdk)** | **Parität und Geschwindigkeit der Gemini Enterprise Agent Platform.** Integrierte Verarbeitung von Typen, Authentifizierung und komplexen Funktionen (z.B. Datei-Uploads). Nahtlose Migration zu Google Cloud. | **Gewicht der Abhängigkeiten.** Transitive Abhängigkeiten können komplex sein und außerhalb Ihrer Kontrolle liegen. Beschränkt auf unterstützte Sprachen (Python/Node/Go/Java). | **Versionen sperren.** Fixieren Sie SDK-Versionen in Ihren internen Basis-Images, um die Stabilität teamübergreifend zu gewährleisten. |
| **Ökosystem-Framework, Edge-Plattformen und Aggregatoren** | **[Direct API](#rest)**  *(REST / gRPC)* | **Keine Abhängigkeiten.** Sie steuern den HTTP-Client und die genaue Bundle-Größe. Vollständiger Zugriff auf alle API- und Modellfunktionen. | **Hoher Entwicklungsaufwand.** JSON-Strukturen können tief verschachtelt sein und erfordern eine strenge manuelle Validierung und Typüberprüfung. | **OpenAPI-Spezifikationen verwenden.** Automatisieren Sie die Typerstellung mit unseren offiziellen Spezifikationen, anstatt sie manuell zu schreiben. |
| **Aggregator, der OpenAI SDKs verwendet, die nur textbasierte Workflows erfordern**  *(Optimierung für Legacy-Portabilität)* | **[OpenAI-Kompatibilität](#openai)** | **Sofortige Portabilität.** Vorhandenen OpenAI-kompatiblen Code oder Bibliotheken wiederverwenden. | **Funktionsbeschränkungen.** Modellspezifische Funktionen (native Videoanzeige, Caching) sind möglicherweise nicht verfügbar. | **Migrationsplan.** Verwenden Sie dies für die schnelle Validierung, planen Sie aber ein Upgrade auf die Direct API für die vollständige API-Funktionalität. |

## Google GenAI SDK-Integration

Für Frameworks ist die Implementierung des [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=de)
oft der einfachste Weg, da in den unterstützten
Sprachen die wenigsten Codezeilen erforderlich sind.

Für interne Plattformteams ist das wichtigste Ergebnis oft ein „Golden Path“, mit dem Produktentwickler schnell arbeiten und gleichzeitig die Sicherheitsrichtlinien einhalten können.

**Vorteile** :

- **Einheitliche Schnittstelle für die Migration zur Gemini Enterprise Agent Platform**:Interne Entwickler erstellen oft Prototypen mit API-Schlüsseln (Gemini API) und stellen sie zur Einhaltung der Produktionsanforderungen auf der Gemini Enterprise Agent Platform (IAM) bereit. Das SDK abstrahiert diese Authentifizierungsunterschiede.
  Ähnlich wie bei Frameworks können Sie einen Codepfad implementieren und zwei Nutzergruppen unterstützen.
- **Clientseitige Hilfsfunktionen**:Das SDK enthält idiomatische Dienstprogramme, die den Boilerplate-Code für komplexe Aufgaben reduzieren.
  - *Beispiele*:Direkte Unterstützung von `PIL`-Bildobjekten in Prompts, automatische Funktionsaufrufe und umfassende Typen.
- **Zugriff auf Funktionen ab dem ersten Tag**:Neue API-Funktionen sind zum Zeitpunkt der Einführung über die SDKs verfügbar.
- **Verbesserte Unterstützung für die Codegenerierung**:Bei der lokalen SDK-Installation werden Typdefinitionen und Docstrings für Coding-Assistenten (z.B. Cursor, Copilot) verfügbar gemacht.
  Dieser Kontext verbessert die Genauigkeit der Codegenerierung im Vergleich zur Generierung von Roh-REST-Anfragen.

**Der Kompromiss** :

- **Gewicht und Komplexität der Abhängigkeiten**:Die SDKs haben eigene Abhängigkeiten, die die Bundle-Größe erhöhen und potenziell das Risiko in der Lieferkette erhöhen können.
- **Versionsverwaltung**:Neue API-Funktionen sind oft an Mindestversionen des SDK gebunden.
  Möglicherweise müssen Sie Updates für Nutzer bereitstellen, um auf neue Funktionen oder Modelle zuzugreifen. In einigen Fällen sind dazu Änderungen an transitiven Abhängigkeiten erforderlich, die sich auf Ihre Nutzer auswirken.
- **Protokollbeschränkungen**:Die SDKs unterstützen nur HTTPS für die Haupt-API und WebSockets (WSS) für die Live API. gRPC wird mit den SDK-Clients der höheren Ebene nicht unterstützt.
- **Sprachunterstützung**:Die SDKs unterstützen die *aktuellen* Sprachversionen. Wenn Sie EOL-Versionen (z.B. Python 3.9) unterstützen müssen, müssen Sie einen Fork verwalten.

**Best Practice** :

- **Versionen sperren**:Fixieren Sie die SDK-Version in Ihren internen Basis-Images, um die Stabilität teamübergreifend zu gewährleisten.

## Direkte API-Integration

Wenn Sie eine Bibliothek an Tausende von Entwicklern verteilen, in einer eingeschränkten Umgebung ausführen oder einen Aggregator erstellen, der die neuesten Funktionen von Gemini erfordert, müssen Sie die API möglicherweise direkt mit REST oder gRPC einbinden.

**Vorteile** :

- **Vollständiger Zugriff auf alle Funktionen**:Im Gegensatz zur OpenAI-Kompatibilitätsebene können Sie bei der direkten Verwendung der API Gemini-spezifische Funktionen nutzen, z. B. das Hochladen in die File API, das Erstellen von Content-Caching und die Verwendung der bidirektionalen Live API.
- **Minimale Abhängigkeiten**:In einer Umgebung, in der Abhängigkeiten aufgrund der Größe oder der Auditkosten kritisch sind. Wenn Sie die API direkt über eine Standardbibliothek wie `fetch` oder einen Wrapper wie `httpx` verwenden, bleibt Ihre Bibliothek schlank.
- **Sprachunabhängig**:Dies ist der einzige Weg für Sprachen, die nicht von den SDKs abgedeckt werden, z. B. Rust, PHP und Ruby, da es keine Sprachbeschränkungen gibt.
- **Leistung**:Die Direct API hat keinen Initialisierungsaufwand, wodurch Kaltstarts in serverlosen Funktionen minimiert werden.

**Der Kompromiss** :

- **Manuelle Implementierung der Gemini Enterprise Agent Platform**:Im Gegensatz zum SDK werden bei der direkten Verwendung der API die Authentifizierungsunterschiede zwischen AI Studio (API-Schlüssel) und der Gemini Enterprise Agent Platform (IAM) nicht automatisch verarbeitet. Sie müssen separate Authentifizierungs-Handler implementieren, wenn Sie beide Umgebungen unterstützen möchten.
- **Keine nativen Typen oder Hilfsfunktionen**:Sie erhalten keine Codevervollständigungen oder Kompilierzeitprüfungen für Anfrageobjekte, es sei denn, Sie implementieren sie selbst. Es gibt keine Client-Hilfsfunktionen (z.B. Konverter von Funktionen zu Schemas), daher müssen Sie diese Logik manuell schreiben.

**Best Practice**

Wir stellen eine maschinenlesbare Spezifikation zur Verfügung, mit der Sie Typdefinitionen für Ihre Bibliothek generieren können, sodass Sie sie nicht manuell schreiben müssen. Laden Sie die Spezifikation während des Build-Prozesses herunter, generieren Sie die Typen und liefern Sie den kompilierten Code aus.

- **Endpunkt**:`https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## OpenAI SDK-Integration

Wenn Sie eine Plattform verwenden, bei der ein einheitliches Schema (OpenAI Chat Completions) wichtiger ist als modellspezifische Funktionen, ist dies die schnellste Route.

**Vorteile** :

- **Geringer Aufwand**:Oft können Sie die Gemini-Unterstützung hinzufügen, indem Sie `baseURL` und `apiKey` ändern. Dies ist eine schnelle Möglichkeit, „Bring Your Own Key“-Implementierungen einzubinden und die Gemini-Unterstützung hinzuzufügen, ohne neuen Code schreiben zu müssen.
- **Einschränkungen**:Dieser Pfad wird nur empfohlen, wenn Sie auf das OpenAI SDK beschränkt sind und keine erweiterten Gemini-Funktionen wie die File API benötigen oder die Unterstützung für Tools wie Fundierung mit der Google Suche manuell hinzufügen müssen.

**Der Kompromiss** :

- **Funktionsbeschränkungen**:Die Kompatibilitätsebene schränkt die Kernfunktionen von Gemini ein. Die verfügbaren serverseitigen Tools unterscheiden sich je nach Plattform und erfordern möglicherweise eine manuelle Verarbeitung, um mit den Gemini API-Tools zu funktionieren.
- **Aufwand für die Übersetzung**:Da das OpenAI-Schema nicht 1:1 der Gemini-Architektur entspricht, führt die Verwendung der Kompatibilitätsebene zu einigen Komplexitäten, die zusätzlichen Implementierungsaufwand erfordern, z. B. die Zuordnung eines Nutzer-„Such“-Tools zum richtigen Plattformtool.
  Wenn Sie eine erhebliche Anzahl von Sonderfällen benötigen, ist es möglicherweise sinnvoller, für jede Plattform ein eigenes SDK oder eine eigene API zu verwenden.

**Best Practice**

Binden Sie die Gemini API nach Möglichkeit direkt ein. Für maximale Kompatibilität sollten Sie jedoch eine Bibliothek verwenden, die verschiedene Anbieter kennt und die Tool- und Nachrichtenzuordnung für Sie übernehmen kann.

## Best Practice für alle Partner: Client-Identifikation

Wenn Sie als Plattform oder Bibliothek Aufrufe an die Gemini API senden, müssen Sie Ihren Client mit dem Header `x-goog-api-client` identifizieren.

So kann Google Ihre spezifischen Traffic-Segmente identifizieren. Wenn Ihre Bibliothek ein bestimmtes Fehlermuster erzeugt, können wir Sie kontaktieren, um bei der Fehlerbehebung zu helfen.

Verwenden Sie das Format `company-product/version` (z.B. `acme-framework/1.2.0`).

### Implementierungsbeispiele

### GenAI SDK

Wenn Sie den API-Client angeben, fügt das SDK Ihren benutzerdefinierten Header automatisch an die internen Header an.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Nächste Schritte

- Besuchen Sie die [Bibliotheksübersicht](https://ai.google.dev/gemini-api/docs/libraries?hl=de), um mehr über
  die GenAI SDKs zu erfahren
- Durchsuchen Sie die [API-Referenz](https://ai.google.dev/api?hl=de)
- Leitfaden zur [OpenAI-Kompatibilität](https://ai.google.dev/gemini-api/docs/openai?hl=de) lesen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-22 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-22 (UTC)."],[],[]]
