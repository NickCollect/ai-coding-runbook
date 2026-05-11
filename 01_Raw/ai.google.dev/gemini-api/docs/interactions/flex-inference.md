---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=de
fetched_at: 2026-05-11T04:59:44.346467+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Flex-Inferenz

Die Gemini Flex API ist eine Inferenzstufe, die im Vergleich zu Standardraten eine Kostenreduzierung von 50% bietet. Im Gegenzug werden variable Latenz und Best-Effort-Verfügbarkeit geboten. Sie ist für latenztolerante Arbeitslasten konzipiert, die eine synchrone Verarbeitung erfordern, aber nicht die Echtzeitleistung der Standard-API benötigen.

## Flex verwenden

Wenn Sie das Flex-Modell verwenden möchten, geben Sie in Ihrer Anfrage `service_tier` als `flex` an. Standardmäßig wird für Anfragen die Standardstufe verwendet, wenn dieses Feld ausgelassen wird.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.steps[-1].content[0].text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.steps.at(-1).content[0].text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3-flash-preview",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## So funktioniert die Flex-Inferenz

Die Gemini Flex-Inferenz schließt die Lücke zwischen der Standard-API und der Bearbeitungszeit von 24 Stunden der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de). Dabei wird Rechenleistung außerhalb der Spitzenzeiten genutzt, die bei Bedarf reduziert werden kann. So wird eine kostengünstige Lösung für Hintergrundaufgaben und sequenzielle Workflows geboten.

| Funktion | Flex | Priorität | Standard | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 50% Rabatt | 75–100% mehr als bei Standard | Standardpreis | 50% Rabatt |
| **Latenz** | Minuten (Ziel: 1–15 Minuten) | Niedrig (Sekunden) | Sekunden bis Minuten | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Best-Effort-Ansatz (reduzierbar) | Hoch (nicht weitergebbar) | Hoch / Mittel bis hoch | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Kosteneffizienz**: Erhebliche Einsparungen bei Evaluierungen, Hintergrund-Agents und Datenanreicherung, die nicht für die Produktion bestimmt sind.
- **Geringer Aufwand**: Fügen Sie Ihren bestehenden Anfragen einfach einen einzelnen Parameter hinzu.
- **Synchrone Workflows**: Ideal für sequenzielle API-Ketten, bei denen die nächste Anfrage von der Ausgabe der vorherigen abhängt. Dadurch sind sie flexibler als Batch-Workflows für agentenbasierte Workflows.

### Anwendungsfälle

- **Offline-Bewertungen**: Regressions- oder Leaderboard-Tests mit „LLM-as-a-Judge“ durchführen.
- **Hintergrund-Agents**: Sequenzielle Aufgaben wie CRM-Aktualisierungen, Profilerstellung oder Inhaltsmoderation, bei denen eine Verzögerung von einigen Minuten akzeptabel ist.
- **Forschung mit beschränktem Budget**: Akademische Experimente, für die ein hohes Tokenvolumen bei beschränktem Budget erforderlich ist.

### Ratenlimits

Flex-Inferenz-Traffic wird auf Ihre allgemeinen [Ratenbegrenzungen](https://aistudio.google.com/rate-limit?hl=de) angerechnet. Es gelten keine erweiterten Ratenbegrenzungen wie bei der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de).

### Abschaltbare Kapazität

Flex-Traffic wird mit niedrigerer Priorität behandelt. Bei einem Anstieg des Standard-Traffics können Flex-Anfragen unterbrochen oder beendet werden, um Kapazität für Nutzer mit hoher Priorität zu schaffen. Wenn Sie eine Prioritätsinferenz durchführen möchten, lesen Sie den Abschnitt [Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=de).

### Fehlercodes

Wenn Flex-Kapazität nicht verfügbar ist oder das System überlastet ist, gibt die API Standardfehlercodes zurück:

- **503 Service Unavailable**: Das System ist derzeit ausgelastet.
- **429 Too Many Requests** (429 Zu viele Anfragen): Ratenbegrenzungen oder Ressourcenerschöpfung.

### Verantwortung des Kunden

- **Kein serverseitiges Fallback**: Um unerwartete Gebühren zu vermeiden, wird eine Flex-Anfrage nicht automatisch auf die Standard-Stufe aktualisiert, wenn die Flex-Kapazität ausgeschöpft ist.
- **Wiederholungsversuche**: Sie müssen Ihre eigene clientseitige Wiederholungslogik mit exponentiellem Backoff implementieren.
- **Zeitüberschreitungen**: Da Flex-Anfragen in einer Warteschlange stehen können, empfehlen wir, clientseitige Zeitüberschreitungen auf mindestens 10 Minuten zu erhöhen, um einen vorzeitigen Verbindungsabbruch zu vermeiden.

## Zeitüberschreitungszeiträume anpassen

Sie können Zeitüberschreitungen pro Anfrage für die REST API und Clientbibliotheken konfigurieren.
Achten Sie immer darauf, dass das clientseitige Zeitlimit das vorgesehene Server-Patience-Fenster abdeckt (z.B. 600 Sekunden und mehr für Flex-Warteschlangen). Die SDKs erwarten Zeitlimitwerte in Millisekunden.

### Zeitlimits für Anfragen

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3-flash-preview",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## Wiederholungsversuche implementieren

Da Flex abwerfbar ist und mit 503-Fehlern fehlschlägt, finden Sie hier ein Beispiel für die optionale Implementierung einer Wiederholungslogik, um mit fehlgeschlagenen Anfragen fortzufahren:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3-flash-preview",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3-flash-preview",
                    input="Analyze this batch statement."
                )

# Usage
interaction = call_with_retry()
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3-flash-preview",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3-flash-preview",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

## Preise

Die Flex-Inferenz kostet 50% der [Standard-API](https://ai.google.dev/gemini-api/docs/pricing?hl=de) und wird pro Token abgerechnet.

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Flex-Inferenz:

| Modell | Flex-Inferenz |
| --- | --- |
| [Gemini 3.1 Flash Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3.1 Flash Lite (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

- [Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=de) für extrem niedrige Latenz.
- [Tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=de): Informationen zu Tokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-09 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-09 (UTC)."],[],[]]
