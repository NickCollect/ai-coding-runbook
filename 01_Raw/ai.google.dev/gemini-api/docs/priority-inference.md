---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=de
fetched_at: 2026-09-07T05:46:27.410764+00:00
title: "Priorit\u00e4tsinferenz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Prioritätsinferenz

Beschreibung: Informationen zur Optimierung der Latenz mit der Priority-Inferenzstufe in der Interactions API

Die Gemini Priority API ist eine Premium-Inferenzstufe, die für geschäftskritische Arbeitslasten entwickelt wurde, die eine geringere Latenz und höchste Zuverlässigkeit erfordern. Sie ist zu einem Premiumpreis verfügbar. Der Traffic der Priority-Stufe hat eine höhere Priorität als der Traffic der Standard-API und der Flex-Stufe.

Die Priority-Inferenz ist für alle Endpunkte der Interactions API verfügbar.

## Priority verwenden

Wenn Sie die Priority-Stufe verwenden möchten, legen Sie das Feld `service_tier` in Ihrer Anfrage auf `priority` fest. Wenn das Feld ausgelassen wird, ist die Standardstufe die Standardeinstellung.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
        model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Funktionsweise der Priority-Inferenz

Bei der Priority-Inferenz werden Anfragen an Rechenwarteschlangen mit hoher Kritikalität weitergeleitet, was eine vorhersehbare, schnelle Leistung für nutzerorientierte Anwendungen ermöglicht. Der primäre Mechanismus ist ein reibungsloser serverseitiger Downgrade auf die Standardverarbeitung für Traffic, der dynamische Limits überschreitet. So wird die Anwendungsstabilität gewährleistet, anstatt die Anfrage abzulehnen.

| Funktion | Priorität | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 75–100% mehr als Standard | Standardpreis | 50% Rabatt | 50% Rabatt |
| **Latenz** | Sekunden | Sekunden bis Minuten | Minuten (Ziel: 1–15 Minuten) | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Hoch (nicht absetzbar) | Hoch / Mittel bis hoch | Best-Effort-Ansatz (absetzbar) | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Geringe Latenz**: Entwickelt für Reaktionszeiten im Sekundenbereich für interaktive,
  nutzerorientierte KI-Tools.
- **Hohe Zuverlässigkeit**: Der Traffic wird mit höchster Kritikalität behandelt und ist
  nicht absetzbar.
- **Graceful Degradation**: Trafficspitzen, die dynamische Limits überschreiten, werden
  automatisch auf die Standardstufe für die Verarbeitung herabgestuft, anstatt abzulehnen.
  So werden Dienstausfälle verhindert.
- **Geringe Reibung**: Verwendet dieselbe synchrone `create` Methode wie die
  Standard- und Flex-Stufen.

### Anwendungsfälle

Die Priority-Verarbeitung ist ideal für geschäftskritische Arbeitsabläufe, bei denen Leistung und Zuverlässigkeit von größter Bedeutung sind.

- **Interaktive KI-Anwendungen**: Kundenservice-Chatbots und Copiloten, bei denen
  Nutzer einen Aufpreis zahlen und schnelle, konsistente Antworten erwarten.
- **Entscheidungsmaschinen in Echtzeit**: Systeme, die hochzuverlässige Ergebnisse mit geringer Latenz
  erfordern, z. B. Live-Ticket-Triage oder Betrugserkennung.
- **Premium-Kundenfunktionen**: Entwickler, die höhere Service
  Level Objectives (SLOs) für zahlende Kunden garantieren müssen.

### Ratenlimits

Für die Priority-Nutzung gelten eigene Ratenlimits, auch wenn die Nutzung auf die [allgemeinen Ratenlimits für interaktiven Traffic angerechnet wird](https://aistudio.google.com/rate-limit?hl=de). Die Standardratenlimits für die Priority-Inferenz sind **0,3-mal das Standardratenlimit für Modell / Stufe**.

### Graceful-Downgrade-Logik

Wenn die Priority-Limits aufgrund von Überlastung überschritten werden, werden Anfragen, die das Limit überschreiten, **automatisch und reibungslos** auf die Standardverarbeitung herabgestuft, anstatt mit einem 503- oder 429-Fehler abzulehnen. Herabgestufte Anfragen werden zum Standardpreis und nicht zum Premiumpreis für Priority abgerechnet.

### Verantwortung des Clients

- **Monitoring der Antwort**: Entwickler sollten den `x-gemini-service-tier`
  Header in der API-Antwort beobachten, um festzustellen, ob Anfragen häufig auf
  `standard` herabgestuft werden.
- **Wiederholungen**: Clients müssen eine Logik für Wiederholungen/exponentielle Backoffs für
  Standardfehler wie `DEADLINE_EXCEEDED` implementieren.

## Preise

Die Priority-Inferenz kostet 75–100% mehr als die [Standard-API](https://ai.google.dev/gemini-api/docs/pricing?hl=de) und wird pro Token abgerechnet.

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Priority-Inferenz:

| Modell | Priority-Inferenz |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

- [Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) zur Kostensenkung.
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de): Informationen zu Tokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
