---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=it
fetched_at: 2026-08-31T06:36:04.700943+00:00
title: "Inferenza della priorit\u00e0 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Inferenza della priorità

Descrizione: scopri come ottimizzare la latenza con il livello di inferenza Priority

L'API Gemini Priority è un livello di inferenza premium progettato per workload mission critical che richiedono una latenza inferiore e la massima affidabilità a un prezzo premium. Il traffico del livello Priority ha la priorità rispetto al traffico dell'API standard e del livello Flex.

L'inferenza Priority è disponibile per gli utenti [di livello 2 e 3](https://ai.google.dev/gemini-api/docs/billing?hl=it#about-billing) negli endpoint dell'API GenerateContent
e dell'API Interactions.

## Come utilizzare Priority

Per utilizzare il livello Priority, imposta il campo `service_tier` nel corpo della richiesta su `priority`. Se il campo viene omesso, il livello predefinito è standard.

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

### Vai

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

## Come funziona l'inferenza Priority

L'inferenza Priority indirizza le richieste alle code di calcolo ad alta criticità, offrendo prestazioni veloci e prevedibili per le applicazioni rivolte agli utenti. Il suo meccanismo principale è un downgrade controllato lato server all'elaborazione standard per il traffico che supera i limiti dinamici, garantendo la stabilità dell'applicazione anziché la mancata riuscita della richiesta.

| Funzionalità | Priorità | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Prezzi** | 75-100% in più rispetto a Standard | Intero | Sconto del 50% | Sconto del 50% |
| **Latenza** | Secondi | Da secondi a minuti | Minuti (target 1-15 min) | Fino a 24 ore |
| **Affidabilità** | Elevata (non eliminabile) | Elevata / medio-alta | Best effort (eliminabile) | Elevata (per il throughput) |
| **Interfaccia** | Sincrona | Sincrona | Sincrona | Asincrona |

### Vantaggi principali

- **Bassa latenza**: progettata per tempi di risposta in secondi per gli strumenti di AI interattivi
  rivolti agli utenti.
- **Elevata affidabilità**: il traffico viene trattato con la massima criticità ed è
  strettamente non eliminabile.
- **Riduzione controllata**: i picchi di traffico che superano i limiti dinamici vengono
  automaticamente sottoposti a downgrade al livello Standard per l'elaborazione anziché non riuscire,
  evitando interruzioni del servizio.
- **Basso attrito**: utilizza lo stesso metodo sincrono `generateContent` dei livelli
  Standard e Flex.

### Casi d'uso

L'elaborazione Priority è ideale per i flussi di lavoro mission critical in cui le prestazioni e l'affidabilità sono fondamentali.

- **Applicazioni di AI interattive**: chatbot e copiloti dell'assistenza clienti in cui
  gli utenti pagano un premio e si aspettano risposte rapide e coerenti.
- **Motori decisionali in tempo reale**: sistemi che richiedono risultati a bassa latenza e altamente affidabili
  , come il triage dei ticket live o il rilevamento delle frodi.
- **Funzionalità premium per i clienti**: sviluppatori che devono garantire obiettivi di livello
  di servizio (SLO) più elevati per i clienti paganti.

### Limiti di frequenza

Il consumo di Priority ha i propri limiti di frequenza, anche se il consumo viene
conteggiato ai fini dei [limiti di frequenza del traffico interattivo complessivo](https://aistudio.google.com/rate-limit?hl=it). I limiti di frequenza predefiniti per l'inferenza Priority sono **0,3 volte il limite di frequenza standard per modello / livello**

### Logica di downgrade controllato

Se i limiti di Priority vengono superati a causa della congestione, le richieste di overflow vengono sottoposte a downgrade **automatico e controllato** all'elaborazione Standard anziché non riuscire con un errore 503 o 429. Le richieste sottoposte a downgrade vengono fatturate alla tariffa standard, non alla tariffa premium Priority.

### Responsabilità del cliente

- **Monitoraggio delle risposte**: gli sviluppatori devono monitorare l'`x-gemini-service-tier`
  intestazione nella risposta dell'API per rilevare se le richieste vengono sottoposte a downgrade frequente a
  `standard`.
- **Nuovi tentativi**: i client devono implementare la logica di nuovi tentativi/backoff esponenziale per gli
  errori standard, ad esempio `DEADLINE_EXCEEDED`.

## Prezzi

L'inferenza Priority ha un prezzo superiore del 75-100% rispetto all'[API standard](https://ai.google.dev/gemini-api/docs/pricing?hl=it) e viene fatturata per token.

## Modelli supportati

I seguenti modelli supportano l'inferenza Priority:

| Modello | Inferenza Priority |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3.1 Pro (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 3 Pro Image (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Passaggi successivi

Scopri le altre opzioni di [inferenza e ottimizzazione](https://ai.google.dev/gemini-api/docs/optimization?hl=it) di Gemini:

- [Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it) per una riduzione dei costi del 50%.
- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it) per l'elaborazione asincrona entro 24 ore.
- [Memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it) per ridurre i costi dei token di input.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
