---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=de
fetched_at: 2026-05-05T20:04:28.716066+00:00
title: "Flex-Inferenz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Flex-Inferenz

Die Gemini Flex API ist eine Inferenzstufe, die im Vergleich zu Standardpreisen eine Kostenreduzierung von 50% bietet, im Gegenzug für variable Latenz und Best-Effort-Verfügbarkeit. Sie wurde für latenzunempfindliche Arbeitslasten entwickelt, die eine synchrone Verarbeitung erfordern, aber nicht die Echtzeitleistung der Standard-API benötigen.

## Flex verwenden

Wenn Sie die Flex-Stufe verwenden möchten, geben Sie im Anfragetext `service_tier` als `flex` an. Standardmäßig verwenden Anfragen die Standardstufe, wenn dieses Feld nicht angegeben wird.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## So funktioniert die Flex-Inferenz

Die Gemini Flex-Inferenz schließt die Lücke zwischen der Standard-API und der 24-Stunden
Bearbeitungszeit der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de). Sie nutzt Rechenkapazität außerhalb der Spitzenzeiten, die bei Bedarf reduziert werden kann, um eine kostengünstige Lösung für Hintergrundaufgaben und sequenzielle Workflows zu bieten.

| Funktion | Flex | Priorität | Standard | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 50% Rabatt | 75–100% mehr als Standard | Standardpreis | 50% Rabatt |
| **Latenz** | Minuten (Ziel: 1–15 Minuten) | Niedrig (Sekunden) | Sekunden bis Minuten | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Best-Effort-Ansatz (reduzierbar) | Hoch (nicht reduzierbar) | Hoch / mittel bis hoch | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Kosteneffizienz**: Erhebliche Einsparungen bei nicht produktionsbezogenen Evaluierungen, Hintergrund-Agents und Datenanreicherung.
- **Geringer Aufwand**: Sie müssen keine Batch-Objekte, Job-IDs oder Abrufe verwalten. Fügen Sie einfach einen einzelnen Parameter zu Ihren bestehenden Anfragen hinzu.
- **Synchrone Arbeitsabläufe**: Ideal für sequenzielle API-Ketten, bei denen die nächste Anfrage von der Ausgabe der vorherigen abhängt. Dadurch ist sie flexibler als Batch für Agent-basierte Arbeitsabläufe.

### Anwendungsfälle

- **Offline-Evaluierungen**: Ausführen von Regressionstests oder Bestenlisten mit „LLM-as-a-judge“.
- **Hintergrund-Agents**: Sequenzielle Aufgaben wie CRM-Updates, Profilerstellung oder Inhaltsmoderation, bei denen Verzögerungen von einigen Minuten akzeptabel sind.
- **Forschung mit beschränktem Budget**: Akademische Experimente, die ein hohes Tokenvolumen bei einem begrenzten Budget erfordern.

### Ratenlimits

Der Flex-Inferenz-Traffic wird auf Ihre allgemeinen [Ratenlimits](https://aistudio.google.com/rate-limit?hl=de) angerechnet. Im Gegensatz zur [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) bietet sie keine erweiterten Ratenlimits.

### Reduzierbare Kapazität

Flex-Traffic wird mit niedrigerer Priorität behandelt. Bei einem Anstieg des Standard-Traffics können Flex-Anfragen vorzeitig beendet oder entfernt werden, um Kapazität für Nutzer mit hoher Priorität zu gewährleisten. Wenn Sie eine Inferenz mit hoher Priorität benötigen, sehen Sie sich die
[Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) an.

### Fehlercodes

Wenn die Flex-Kapazität nicht verfügbar ist oder das System überlastet ist, gibt die API Standardfehlercodes zurück:

- **503 Dienst nicht verfügbar**: Das System ist derzeit voll ausgelastet.
- **429 Zu viele Anfragen**: Ratenlimits oder Ressourcenerschöpfung.

### Verantwortung des Clients

- **Kein serverseitiges Fallback**: Um unerwartete Kosten zu vermeiden, wird eine Flex-Anfrage nicht
  automatisch auf die Standardstufe aktualisiert, wenn die Flex-Kapazität
  voll ist.
- **Wiederholungen**: Sie müssen Ihre eigene clientseitige Wiederholungslogik mit
  exponentiellem Backoff implementieren.
- **Zeitlimits**: Da Flex-Anfragen in einer Warteschlange stehen können, empfehlen wir,
  die clientseitigen Zeitlimits auf mindestens 10 Minuten zu erhöhen, um ein vorzeitiges
  Schließen der Verbindung zu vermeiden.

## Zeitlimitfenster anpassen

Sie können Zeitlimits pro Anfrage für die REST API und Clientbibliotheken sowie globale Zeitlimits nur bei Verwendung der Clientbibliotheken konfigurieren.

Achten Sie immer darauf, dass das clientseitige Zeitlimit das vorgesehene serverseitige Zeitlimit abdeckt (z.B. 600 Sekunden oder mehr für Flex-Warteschlangen). Die SDKs erwarten Zeitlimitwerte in Millisekunden.

### Zeitlimits pro Anfrage

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3-flash-preview",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3-flash-preview",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

Bei REST-Aufrufen können Sie Zeitlimits mit einer Kombination aus HTTP-Headern und `curl`-Optionen steuern:

- **`X-Server-Timeout` -Header (serverseitiges Zeitlimit)** : Dieser Header schlägt dem Gemini API-Server eine bevorzugte Zeitlimitdauer vor (Standard: 600 Sekunden). Der Server versucht, dies zu berücksichtigen, aber es gibt keine Garantie. Der Wert sollte in Sekunden angegeben werden.
- **`--max-time` in `curl` (clientseitiges Zeitlimit)**: Mit der Option `curl --max-time
  <seconds>` wird ein hartes Limit für die Gesamtzeit (in Sekunden) festgelegt, die `curl`
  wartet, bis der gesamte Vorgang abgeschlossen ist. Dies ist eine clientseitige Sicherheitsmaßnahme.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### Globale Zeitlimits

Wenn für alle API-Aufrufe, die über eine bestimmte `genai.Client`-Instanz erfolgen (nur Clientbibliotheken), ein Standardzeitlimit gelten soll, können Sie dies beim Initialisieren des Clients mit `http_options` und `genai.types.HttpOptions` konfigurieren.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3-flash-preview")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## Wiederholungen implementieren

Da Flex reduziert werden kann und mit 503-Fehlern fehlschlägt, finden Sie hier ein Beispiel für die optionale Implementierung einer Wiederholungslogik, um mit fehlgeschlagenen Anfragen fortzufahren:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3-flash-preview",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3-flash-preview",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3-flash-preview",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3-flash-preview"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## Preise

Die Flex-Inferenz kostet 50% der [Standard-API](https://ai.google.dev/gemini-api/docs/pricing?hl=de)
und wird pro Token abgerechnet.

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Flex-Inferenz:

| Modell | Flex-Inferenz |
| --- | --- |
| [Gemini 3.1 Flash-Lite (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 3 Pro Image (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

Weitere Informationen zu den anderen [Inferenz- und Optimierungs](https://ai.google.dev/gemini-api/docs/optimization?hl=de)optionen von Gemini:

- [Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) für extrem niedrige Latenz.
- [Batch-API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) für die asynchrone Verarbeitung innerhalb von 24 Stunden.
- [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) für geringere Kosten für Eingabetokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
