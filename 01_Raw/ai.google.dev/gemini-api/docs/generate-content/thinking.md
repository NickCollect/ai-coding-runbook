---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it
fetched_at: 2026-08-24T02:24:04.056309+00:00
title: "Pensiero di Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Pensiero di Gemini

I modelli delle serie [Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=it) utilizzano un
"processo di pensiero" interno che migliora notevolmente le loro capacità di ragionamento e pianificazione in più passaggi,
rendendoli altamente efficaci per attività complesse come la
programmazione, la matematica avanzata e l'analisi dei dati.

Questa guida mostra come utilizzare le funzionalità di pensiero di Gemini utilizzando l'API Gemini.

## Generare contenuti con il pensiero

L'avvio di una richiesta con un modello di ragionamento è simile a qualsiasi altra richiesta di generazione di contenuti. La differenza fondamentale consiste nello specificare uno dei
[modelli con supporto per il pensiero](#supported-models) nel campo `model`, come
mostrato nel seguente [esempio di generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Vai

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Riepiloghi del pensiero

I riepiloghi del pensiero sono versioni riassunte dei pensieri non elaborati del modello e offrono informazioni sul processo di ragionamento interno del modello. Tieni presente che i livelli e i budget di pensiero si applicano ai pensieri non elaborati del modello e non ai riepiloghi del pensiero.

Puoi attivare i riepiloghi del pensiero impostando `includeThoughts` su `true` nella configurazione della richiesta. Puoi quindi accedere al riepilogo scorrendo i `parts` del parametro `response` e controllando il valore booleano `thought`.

Ecco un esempio che mostra come attivare e recuperare i riepiloghi del pensiero senza streaming, che restituisce un unico riepilogo del pensiero finale con la risposta:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Vai

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Ecco un esempio di utilizzo del pensiero con lo streaming, che restituisce riepiloghi incrementali durante la generazione:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.6-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Controllare il pensiero

Per impostazione predefinita, i modelli Gemini utilizzano il pensiero dinamico, regolando automaticamente la quantità di ragionamento in base alla complessità della richiesta dell'utente.
Tuttavia, se hai vincoli di latenza specifici o richiedi che il modello utilizzi un ragionamento più approfondito del solito, puoi facoltativamente utilizzare i parametri per controllare il comportamento del pensiero.

### Livelli di pensiero (Gemini 3)

Il parametro `thinkingLevel`, consigliato per i modelli Gemini 3 e versioni successive, consente di controllare il comportamento del ragionamento.

La tabella seguente descrive in dettaglio le impostazioni di `thinkingLevel` per ogni tipo di modello:

| Livello di pensiero | Gemini 3.6 e 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 e 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Descrizione |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Supportato | Non supportato | Supportato (valore predefinito) | Supportato (valore predefinito) | Supportato | Corrisponde all'impostazione "nessun pensiero" per la maggior parte delle query. Tieni presente che `minimal` non garantisce che il pensiero sia disattivato, il modello potrebbe ragionare in modo molto minimo per attività complesse. |
| **`low`** | Supportato | Supportato | Supportato | Non supportato | Supportato | Riduce al minimo la latenza e i costi. |
| **`medium`** | Supportato (valore predefinito) | Supportato | Supportato | Non supportato | Supportato | Pensiero bilanciato per la maggior parte delle attività. |
| **`high`** | Supportato (dinamico) | Supportato (valore predefinito, dinamico) | Supportato (dinamico) | Supportato (dinamico) | Supportato (valore predefinito, dinamico) | Massimizza la profondità del ragionamento. Il modello potrebbe impiegare molto più tempo per raggiungere un primo token di output (non di pensiero), ma l'output sarà più accurato. |

Il seguente esempio mostra come impostare il livello di pensiero.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Vai

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Non puoi disattivare il pensiero per Gemini 3.1 Pro. Anche Gemini 3 Flash e Flash-Lite
non supportano la disattivazione completa del pensiero.
Se non specifichi un livello di pensiero, Gemini utilizzerà il livello di pensiero predefinito dei modelli Gemini 3 (ad es. `"high"` per Gemini 3.1 Pro e `"medium"` per Gemini 3.5 Flash).

I modelli della serie Gemini 2.5 non supportano `thinkingLevel`; utilizza invece `thinkingBudget`.

### Budget di pensiero

Il parametro `thinkingBudget`, introdotto con la serie Gemini 2.5, indica al modello il numero specifico di token di pensiero da utilizzare per il ragionamento.

Di seguito sono riportati i dettagli di configurazione di `thinkingBudget` per ogni tipo di modello.
Puoi disattivare il pensiero impostando `thinkingBudget` su 0.
Se imposti `thinkingBudget` su -1, viene attivato il **pensiero dinamico**, il che significa che il modello regolerà il budget in base alla complessità della richiesta.

| Modello | Impostazione predefinita (il budget di pensiero non è impostato) | Intervallo | Disattiva il pensiero | Attiva il pensiero dinamico |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Pensiero dinamico | Da `128` a `32768` | N/A: non è possibile disattivare il pensiero | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash** | Pensiero dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash Preview** | Pensiero dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash Lite** | Il modello non pensa | Da `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Il modello non pensa | Da `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Pensiero dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Pensiero dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Vai

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

A seconda del prompt, il modello potrebbe superare o non raggiungere il budget di token.

## Firme del pensiero

L'API Gemini è senza stato, quindi il modello tratta ogni richiesta API in modo indipendente e non ha accesso al contesto di pensiero dei turni precedenti nelle interazioni in più turni.

Per consentire il mantenimento del contesto di pensiero nelle interazioni multi-turno, Gemini restituisce le firme del pensiero, che sono rappresentazioni criptate del processo di pensiero interno del modello.

- **I modelli Gemini 2.5** restituiscono le firme del pensiero quando il pensiero è attivato e
  la richiesta include la [chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#thinking),
  in particolare le [dichiarazione di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-2).
- **I modelli Gemini 3** possono restituire le firme del pensiero per tutti i tipi di [parti](https://ai.google.dev/api/caching?hl=it#Part).
  Ti consigliamo di restituire sempre tutte le firme così come le hai ricevute, ma è *obbligatorio* per le firme di chiamata di funzione. Per saperne di più, consulta la pagina
  [Firme del pensiero](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it).

Altre limitazioni di utilizzo da considerare con la chiamata di funzione includono:

- Le firme vengono restituite dal modello all'interno di altre parti della risposta, ad esempio le parti di chiamata di funzione o di testo.
  [Restituisci l'intera risposta](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-4)
  con tutte le parti al modello nei turni successivi.
- Non concatenare le parti con le firme.
- Non unire una parte con una firma con un'altra parte senza firma.

## Prezzi

Quando il pensiero è attivato, il prezzo della risposta è la somma dei token di output e dei token di pensiero. Puoi ottenere il numero totale di token di pensiero generati dal campo `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Vai

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

I modelli di pensiero generano pensieri completi per migliorare la qualità della risposta
finale, quindi restituiscono [i riepiloghi](#summaries) per fornire informazioni sul
processo di pensiero. Pertanto, il prezzo si basa sui token di pensiero completi che il modello deve generare per creare un riepilogo, anche se dall'API viene restituito solo il riepilogo.

Per saperne di più sui token, consulta la [guida](https://ai.google.dev/gemini-api/docs/tokens?hl=it)
al conteggio dei token.

## Best practice

Questa sezione include alcune indicazioni per l'utilizzo efficiente dei modelli di pensiero.
Come sempre, seguendo le nostre [indicazioni e best practice per i prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it) otterrai i risultati migliori.

### Debug e orientamento

- **Esamina il ragionamento**: quando non ricevi la risposta prevista dai
  modelli di pensiero, può essere utile analizzare attentamente i riepiloghi del pensiero di Gemini.
  Puoi vedere come ha suddiviso l'attività e come è arrivato alla sua conclusione e utilizzare queste informazioni per correggere i risultati corretti.
- **Fornisci indicazioni nel ragionamento**: se prevedi un output particolarmente lungo, potresti voler fornire indicazioni nel prompt per limitare la
  [quantità di pensiero](#set-budget) utilizzata dal modello. In questo modo, puoi riservare più token di output per la risposta.

### Complessità dell'attività

- **Attività semplici (il pensiero potrebbe essere disattivato):** per le richieste semplici in cui non è richiesto un ragionamento complesso, come il recupero o la classificazione dei fatti, il pensiero non è necessario. Esempi:
  - "Dove è stata fondata DeepMind?"
  - "Questa email chiede un incontro o fornisce solo informazioni?"
- **Attività di livello medio (pensiero predefinito/parziale):** molte richieste comuni traggono vantaggio da un certo grado di elaborazione passo passo o da una comprensione più approfondita. Gemini può utilizzare in modo flessibile la funzionalità di pensiero per attività come:
  - Analogizzare la fotosintesi e la crescita.
  - Confrontare e contrapporre auto elettriche e auto ibride.
- **Attività difficili (capacità di pensiero massima):** per le sfide veramente complesse, come la risoluzione di problemi di matematica complessi o attività di programmazione, ti consigliamo di impostare un budget di pensiero elevato. Questi tipi di attività richiedono che il modello utilizzi tutte le sue capacità di ragionamento e pianificazione, spesso con molti passaggi interni prima di fornire una risposta. Esempi:
  - Risolvi il problema 1 in AIME 2025: trova la somma di tutte le basi intere b > 9 per
    le quali 17b è un divisore di 97b.
  - Scrivi codice Python per un'applicazione web che visualizzi i dati del mercato azionario in tempo reale, inclusa l'autenticazione utente. Rendilo il più efficiente possibile.

## Modelli, strumenti e funzionalità supportati

Le funzionalità di pensiero sono supportate su tutti i modelli delle serie 3 e 2.5.
Puoi trovare tutte le funzionalità del modello nella
[pagina di panoramica del modello](https://ai.google.dev/gemini-api/docs/models?hl=it).

I modelli di pensiero funzionano con tutti gli strumenti e le funzionalità di Gemini. In questo modo, i modelli possono interagire con sistemi esterni, eseguire codice o accedere a informazioni in tempo reale, incorporando i risultati nel loro ragionamento e nella risposta finale.

Puoi provare esempi di utilizzo degli strumenti con i modelli di pensiero nel [ricettario di pensiero][Colab].

## Passaggi successivi

- La copertura del pensiero è disponibile nella nostra guida alla compatibilità con [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
