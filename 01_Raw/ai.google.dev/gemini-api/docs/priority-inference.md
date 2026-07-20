---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=de
fetched_at: 2026-07-20T04:39:12.568404+00:00
title: "Priorit\u00e4tsinferenz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Prioritätsinferenz

Beschreibung: Informationen zum Optimieren der Latenz mit der Prioritätsinferenzebene in der Interactions API

Die Gemini Priority API ist eine Premium-Inferenzebene, die für geschäftskritische Arbeitslasten entwickelt wurde, die eine geringere Latenz und höchste Zuverlässigkeit erfordern. Sie ist zu einem Premium-Preis erhältlich. Traffic mit Priorität wird gegenüber Traffic mit Standard-API- und Flex-Tarif priorisiert.

Die Prioritätsinferenz ist für alle Interactions API-Endpunkte verfügbar.

## Priority verwenden

Wenn Sie die Prioritätsstufe verwenden möchten, legen Sie das Feld `service_tier` in Ihrer Anfrage auf `priority` fest. Wenn das Feld ausgelassen wird, ist die Standardstufe „Standard“.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Funktionsweise der Prioritätsinferenz

Bei der Prioritätsinferenz werden Anfragen an Rechenwarteschlangen mit hoher Kritikalität weitergeleitet, was eine vorhersehbare, schnelle Leistung für nutzerorientierte Anwendungen ermöglicht. Der primäre Mechanismus ist ein reibungsloses serverseitiges Downgrade auf die Standardverarbeitung für Traffic, der dynamische Limits überschreitet. So wird die Anwendungsstabilität gewährleistet, anstatt dass die Anfrage fehlschlägt.

| Funktion | Priorität | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 75–100% mehr als bei Standard | Standardpreis | 50% Rabatt | 50% Rabatt |
| **Latenz** | Sekunden | Sekunden bis Minuten | Minuten (Ziel: 1–15 Minuten) | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Hoch (nicht löschbar) | Hoch / Mittel bis hoch | Best-Effort (reduzierbar) | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Niedrige Latenz**: Entwickelt für Reaktionszeiten im Sekundenbereich für interaktive, nutzerorientierte KI‑Tools.
- **Hohe Zuverlässigkeit**: Traffic wird mit der höchsten Priorität behandelt und darf nicht reduziert werden.
- **Sanfte Herabstufung**: Traffic-Spitzen, die dynamische Limits überschreiten, werden automatisch auf die Standardstufe für die Verarbeitung herabgestuft, anstatt zu einem Fehler zu führen. So werden Dienstausfälle verhindert.
- **Geringer Aufwand**: Es wird dieselbe synchrone `create`-Methode wie bei den Standard- und Flex-Tarifen verwendet.

### Anwendungsfälle

Die Prioritätsverarbeitung ist ideal für geschäftskritische Workflows, bei denen Leistung und Zuverlässigkeit von entscheidender Bedeutung sind.

- **Interaktive KI-Anwendungen**: Kundenservice-Chatbots und Copiloten, für die Nutzer eine Prämie zahlen und schnelle, konsistente Antworten erwarten.
- **Echtzeit-Entscheidungsmaschinen**: Systeme, die hochzuverlässige Ergebnisse mit geringer Latenz erfordern, z. B. die Live-Ticket-Triage oder die Betrugserkennung.
- **Premium-Kundenfunktionen**: Entwickler, die höhere Service Level Objectives (SLOs) für zahlende Kunden garantieren müssen.

### Ratenlimits

Für die Prioritätsnutzung gelten eigene Ratenbegrenzungen, obwohl die Nutzung auf die [Ratenbegrenzungen für den gesamten interaktiven Traffic](https://aistudio.google.com/rate-limit?hl=de) angerechnet wird. Die Standardratenlimits für die Prioritätsinferenz sind **0,3 × Standardratenlimit für Modell / Tier**.

### Logik für ordnungsgemäßes Downgrade

Wenn Prioritätslimits aufgrund von Überlastung überschritten werden, werden Überlaufanfragen **automatisch und ordnungsgemäß** auf die Standardverarbeitung herabgestuft, anstatt mit einem 503- oder 429-Fehler zu fehlschlagen. Herabgestufte Anfragen werden zum Standardtarif und nicht zum Priority-Premiumtarif abgerechnet.

### Verantwortung des Kunden

- **Antwortüberwachung**: Entwickler sollten den `x-gemini-service-tier`-Header in der API-Antwort überwachen, um festzustellen, ob Anfragen häufig auf `standard` herabgestuft werden.
- **Wiederholungen**: Clients müssen eine Wiederholungslogik/einen exponentiellen Backoff für Standardfehler wie `DEADLINE_EXCEEDED` implementieren.

## Preise

Die Prioritätsinferenz kostet 75–100% mehr als die [Standard-API](https://ai.google.dev/gemini-api/docs/pricing?hl=de) und wird pro Token abgerechnet.

## Unterstützte Modelle

Die folgenden Modelle unterstützen Priority Inference:

| Modell | Prioritätsinferenz |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

- [Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) zur Kostensenkung.
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de): Informationen zu Tokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-06 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-06 (UTC)."],[],[]]
