---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=it
fetched_at: 2026-05-11T04:59:34.187098+00:00
title: "Inferenza flessibile \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Inferenza flessibile

L'API Gemini Flex è un livello di inferenza che offre una riduzione dei costi del 50% rispetto alle tariffe standard, in cambio di latenza variabile e disponibilità
best-effort. È progettata per carichi di lavoro tolleranti alla latenza che richiedono
l'elaborazione sincrona, ma non necessitano delle prestazioni in tempo reale dell'API
standard.

## Come usare Flex

Per utilizzare il livello Flex, specifica `service_tier` come `flex` nel corpo della richiesta. Per impostazione predefinita, le richieste utilizzano il livello standard se questo campo
viene omesso.

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

### Go

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

## Come funziona l'inferenza flessibile

L'inferenza di Gemini Flex colma il divario tra l'API standard e il tempo di risposta di 24 ore
dell'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it). Utilizza la capacità di calcolo "riducibile" non di punta per fornire una soluzione conveniente per le attività in background e i flussi di lavoro sequenziali.

| Funzionalità | Flex | Priorità | Standard | Batch |
| --- | --- | --- | --- | --- |
| **Prezzi** | Sconto del 50% | 75-100% in più rispetto a Standard | Intero | Sconto del 50% |
| **Latenza** | Minuti (obiettivo 1-15 minuti) | Basso (secondi) | Da secondi a minuti | Fino a 24 ore |
| **Affidabilità** | Best effort (eliminabile) | Alto (non cedibile) | Alta / Medio alta | Alta (per il throughput) |
| **Interfaccia** | Sincrona | Sincrona | Sincrona | Asincrona |

### Vantaggi principali

- **Efficienza dei costi**: risparmi sostanziali per valutazioni non di produzione, agenti in background e arricchimento dei dati.
- **Semplice**: non è necessario gestire oggetti batch, ID job o polling; è sufficiente aggiungere un singolo parametro alle richieste esistenti.
- **Workflow sincroni**: ideali per le catene di API sequenziali in cui la richiesta successiva dipende dall'output di quella precedente, il che li rende più flessibili rispetto ai batch per i workflow agentici.

### Casi d'uso

- **Valutazioni offline**: esecuzione di test di regressione o classifiche "LLM-as-a-judge".
- **Agenti in background**: attività sequenziali come aggiornamenti del CRM, creazione di profili o moderazione dei contenuti in cui sono accettabili ritardi di minuti.
- **Ricerca con limiti di budget**: esperimenti accademici che richiedono un volume elevato di token con un budget limitato.

### Limiti di frequenza

Il traffico di inferenza flessibile viene conteggiato ai fini dei [limiti di frequenza](https://aistudio.google.com/rate-limit?hl=it) generali; non
offre limiti di frequenza estesi come l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it).

### Capacità riducibile

Il traffico flessibile viene trattato con priorità inferiore. Se si verifica un picco di traffico standard, le richieste flessibili potrebbero essere interrotte o rimosse per garantire la capacità per gli utenti ad alta priorità. Se stai cercando un'inferenza ad alta priorità, consulta
[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)

### Codici di errore

Quando la capacità flessibile non è disponibile o il sistema è sovraccarico, l'API
restituisce codici di errore standard:

- **503 - Servizio non disponibile**: il sistema è attualmente al massimo della capacità.
- **429 Too Many Requests**: limiti di frequenza o esaurimento delle risorse.

### Responsabilità del cliente

- **Nessun fallback lato server**: per evitare addebiti imprevisti, il sistema non esegue automaticamente l'upgrade di una richiesta Flex al livello Standard se la capacità Flex è piena.
- **Nuovi tentativi**: devi implementare la tua logica di nuovi tentativi lato client con
  backoff esponenziale.
- **Timeout**: poiché le richieste Flex potrebbero rimanere in una coda, ti consigliamo di aumentare i timeout lato client a 10 minuti o più per evitare la chiusura prematura della connessione.

## Regolare le finestre di timeout

Puoi configurare i timeout per richiesta per l'API REST e le librerie client e i timeout globali solo quando utilizzi le librerie client.

Assicurati sempre che il timeout lato client copra la finestra di attesa del server prevista (ad es. 600 secondi o più per le code di attesa flessibili). Gli SDK prevedono valori di timeout in
millisecondi.

### Timeout per richiesta

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

### Go

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

Quando effettui chiamate REST, puoi controllare i timeout utilizzando una combinazione di intestazioni HTTP e opzioni `curl`:

- **Intestazione `X-Server-Timeout` (timeout lato server)**: questa intestazione suggerisce una
  durata di timeout preferita (valore predefinito 600 secondi) per il server dell'API Gemini. Il server
  cercherà di rispettare questa impostazione, ma non è garantito. Il valore deve essere in secondi.
- **`--max-time` in `curl` (timeout lato client)**: l'opzione `curl --max-time
  <seconds>` imposta un limite rigido al tempo totale (in secondi) in cui `curl`
  attenderà il completamento dell'intera operazione. Si tratta di una protezione lato client.

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

### Timeout globali

Se vuoi che tutte le chiamate API effettuate tramite un'istanza `genai.Client` specifica
(solo librerie client) abbiano un timeout predefinito, puoi configurarlo durante
l'inizializzazione del client utilizzando `http_options` e `genai.types.HttpOptions`.

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

### Go

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

## Implementare i nuovi tentativi

Poiché Flex è eliminabile e non funziona con errori 503, ecco un esempio di
implementazione facoltativa della logica di ripetizione per continuare con le richieste non riuscite:

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

### Go

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

## Prezzi

L'inferenza flessibile ha un prezzo pari al 50% dell'[API standard](https://ai.google.dev/gemini-api/docs/pricing?hl=it)
e viene fatturata per token.

## Modelli supportati

I seguenti modelli supportano l'inferenza flessibile:

| Modello | Inferenza flessibile |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) | ✔️ |
| [Anteprima di Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Anteprima di Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Passaggi successivi

Scopri le altre opzioni di [inferenza e ottimizzazione](https://ai.google.dev/gemini-api/docs/optimization?hl=it) di Gemini:

- [Inferenza della priorità](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it) per la latenza molto bassa.
- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it) per l'elaborazione asincrona entro 24 ore.
- [Memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it) per ridurre i costi dei token di input.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-08 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-08 UTC."],[],[]]
