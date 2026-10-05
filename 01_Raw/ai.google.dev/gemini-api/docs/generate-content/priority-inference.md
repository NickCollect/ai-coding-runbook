---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=de
fetched_at: 2026-10-05T06:36:17.398096+00:00
title: "Priorit\u00e4tsinferenz \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Prioritätsinferenz

Beschreibung: Latenz mit der Priority-Inferenzstufe optimieren

Die Gemini Priority API ist eine Premium-Inferenzstufe, die für geschäftskritische Arbeitslasten entwickelt wurde, die eine geringere Latenz und höchste Zuverlässigkeit zu einem Premiumpreis erfordern. Der Traffic der Priority-Stufe hat Vorrang vor dem Traffic der Standard-API und der Flex-Stufe.

Die Priority-Inferenz ist für [Nutzer der Stufen 2 und 3](https://ai.google.dev/gemini-api/docs/billing?hl=de#about-billing) an den Endpunkten der GenerateContent API
und der Interactions API verfügbar.

## Priority verwenden

Wenn Sie die Priority-Stufe verwenden möchten, legen Sie das Feld `service_tier` im Anfragetext auf `priority` fest. Wenn das Feld ausgelassen wird, ist die Standardstufe die Standardeinstellung.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Funktionsweise der Priority-Inferenz

Bei der Priority-Inferenz werden Anfragen an Rechenwarteschlangen mit hoher Priorität weitergeleitet, was eine vorhersehbare, schnelle Leistung für nutzerorientierte Anwendungen ermöglicht. Der Hauptmechanismus ist ein reibungsloser serverseitiger Wechsel zur Standardverarbeitung für Traffic, der dynamische Limits überschreitet. So wird die Anwendungsstabilität gewährleistet, anstatt dass die Anfrage fehlschlägt.

| Funktion | Priorität | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 75–100% mehr als Standard | Standardpreis | 50% Rabatt | 50% Rabatt |
| **Latenz** | Sekunden | Sekunden bis Minuten | Minuten (Ziel: 1–15 Minuten) | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Hoch (nicht abwerfbar) | Hoch / mittel bis hoch | Best-Effort-Ansatz (abwerfbar) | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Geringe Latenz**: Entwickelt für Reaktionszeiten im Sekundenbereich für interaktive,
  nutzerorientierte KI-Tools.
- **Hohe Zuverlässigkeit**: Traffic wird mit höchster Priorität behandelt und ist
  nicht abwerfbar.
- **Graceful Degradation**: Trafficspitzen, die dynamische Limits überschreiten, werden
  automatisch auf die Standardstufe für die Verarbeitung herabgestuft, anstatt dass sie fehlschlagen.
  So werden Dienstausfälle verhindert.
- **Geringe Reibung**: Verwendet dieselbe synchrone `generateContent` Methode wie die
  Standard- und Flex-Stufen.

### Anwendungsfälle

Die Priority-Verarbeitung ist ideal für geschäftskritische Arbeitsabläufe, bei denen Leistung und Zuverlässigkeit von größter Bedeutung sind.

- **Interaktive KI-Anwendungen**: Kundenservice-Chatbots und -Copiloten, bei denen
  Nutzer einen Aufpreis zahlen und schnelle, konsistente Antworten erwarten.
- **Echtzeit-Entscheidungsmaschinen**: Systeme, die hochzuverlässige Ergebnisse mit geringer Latenz
  erfordern, z. B. Live-Ticket-Triage oder Betrugserkennung.
- **Premium-Kundenfunktionen**: Entwickler, die höhere Service
  Level Objectives (SLOs) für zahlende Kunden garantieren müssen.

### Ratenlimits

Für die Priority-Nutzung gelten eigene Ratenlimits, auch wenn die Nutzung auf die [allgemeinen Ratenlimits für interaktiven Traffic angerechnet wird](https://aistudio.google.com/rate-limit?hl=de). Die Standardratenlimits für die Priority-Inferenz sind **0,3-mal das Standardratenlimit für Modell / Stufe**.

### Logik für Graceful Degradation

Wenn die Priority-Limits aufgrund von Überlastung überschritten werden, werden Anfragen, die das Limit überschreiten, **automatisch und reibungslos** auf die Standardverarbeitung herabgestuft, anstatt dass sie mit einem 503- oder 429-Fehler fehlschlagen. Herabgestufte Anfragen werden zum Standardpreis und nicht zum Premiumpreis für Priority abgerechnet.

### Verantwortung des Clients

- **Monitoring der Antwort**: Entwickler sollten den `x-gemini-service-tier`
  Header in der API-Antwort beobachten, um festzustellen, ob Anfragen häufig auf
  `standard` herabgestuft werden.
- **Wiederholungen**: Clients müssen eine Wiederholungslogik/einen exponentiellen Backoff für
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
| [Gemini 3 Pro Image (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

Weitere Informationen zu den anderen [Inferenz- und Optimierungs](https://ai.google.dev/gemini-api/docs/optimization?hl=de)optionen von Gemini:

- [Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) für eine Kostenreduzierung von 50 %
- [Batch-API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) für die asynchrone Verarbeitung innerhalb von 24 Stunden
- [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) für geringere Kosten für Eingabetokens

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
