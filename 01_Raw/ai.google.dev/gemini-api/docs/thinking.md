---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=it
fetched_at: 2026-05-25T05:24:20.425705+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Ragionamento di Gemini

I modelli delle serie [Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=it) utilizzano un "processo di ragionamento" interno che migliora notevolmente le loro capacità di ragionamento e pianificazione in più passaggi, rendendoli altamente efficaci per attività complesse come la programmazione, la matematica avanzata e l'analisi dei dati.

Questa guida mostra come utilizzare le funzionalità di ragionamento di Gemini utilizzando l'API Gemini.

## Generare contenuti con il ragionamento

L'avvio di una richiesta con un modello di ragionamento è simile a qualsiasi altra richiesta di generazione di contenuti. La differenza fondamentale consiste nello specificare uno dei
[modelli con supporto per il ragionamento](#supported-models) nel campo `model`, come
illustrato nel seguente [esempio di generazione di testo](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Riepiloghi del ragionamento

I riepiloghi del ragionamento sono versioni riassuntive dei ragionamenti non elaborati del modello e offrono informazioni sul processo di ragionamento interno del modello. Tieni presente che i livelli e i budget di ragionamento si applicano ai ragionamenti non elaborati del modello e non ai riepiloghi del ragionamento.

Puoi attivare i riepiloghi del ragionamento impostando `includeThoughts` su `true` nella configurazione della richiesta. Puoi quindi accedere al riepilogo scorrendo i `parts` del parametro `response` e controllando il valore booleano `thought`.

Ecco un esempio che mostra come attivare e recuperare i riepiloghi del ragionamento senza streaming, che restituisce un singolo riepilogo del ragionamento finale con la risposta:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  model := "gemini-3.5-flash"
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

Ecco un esempio di utilizzo del ragionamento con lo streaming, che restituisce riepiloghi incrementali durante la generazione:

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  model := "gemini-3.5-flash"

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

## Controllare il ragionamento

Per impostazione predefinita, i modelli Gemini eseguono un ragionamento dinamico, regolando automaticamente la quantità di ragionamento in base alla complessità della richiesta dell'utente.
Tuttavia, se hai vincoli di latenza specifici o richiedi che il modello esegua un ragionamento più approfondito del solito, puoi utilizzare facoltativamente i parametri per controllare il comportamento del ragionamento.

### Livelli di ragionamento (Gemini 3)

Il parametro `thinkingLevel`, consigliato per i modelli Gemini 3 e versioni successive, consente di controllare il comportamento del ragionamento.

La tabella seguente descrive in dettaglio le impostazioni di `thinkingLevel` per ogni tipo di modello:

| Livello di ragionamento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Gemini 3.5 Flash | Descrizione |
| --- | --- | --- | --- | --- | --- |
| **`minimal`** | Non supportato | Supportato (valore predefinito) | Supportato | Supportato | Corrisponde all'impostazione "nessun ragionamento" per la maggior parte delle query. Il modello potrebbe ragionare in modo molto minimo per attività di programmazione complesse. Riduce al minimo la latenza per le applicazioni di chat o con throughput elevato. Tieni presente che `minimal` non garantisce che il ragionamento sia disattivato. |
| **`low`** | Supportato | Supportato | Supportato | Supportato | Riduce al minimo la latenza e i costi. Ideale per istruzioni semplici, chat o applicazioni con velocità effettiva elevata. |
| **`medium`** | Supportato | Supportato | Supportato | Supportato (valore predefinito) | Ragionamento bilanciato per la maggior parte delle attività. |
| **`high`** | Supportato (valore predefinito, dinamico) | Supportato (dinamico) | Supportato (valore predefinito, dinamico) | Supportato (dinamico) | Massimizza la profondità del ragionamento. Il modello potrebbe impiegare molto più tempo per raggiungere un primo token di output (non di ragionamento), ma l'output sarà più accurato. |

Il seguente esempio mostra come impostare il livello di ragionamento.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  model := "gemini-3.5-flash"
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Non puoi disattivare il ragionamento per Gemini 3.1 Pro. Anche Gemini 3 Flash e Flash-Lite non supportano la disattivazione completa del ragionamento, ma l'impostazione `minimal` indica che il modello probabilmente non ragionerà (anche se potenzialmente può farlo).
Se non specifichi un livello di ragionamento, Gemini utilizzerà il livello di ragionamento predefinito dei modelli Gemini 3 (ad es. `"high"` per Gemini 3.1 Pro e `"medium"` per Gemini 3.5 Flash).

I modelli della serie Gemini 2.5 non supportano `thinkingLevel`; utilizza invece `thinkingBudget`.

### Budget di ragionamento

Il parametro `thinkingBudget`, introdotto con la serie Gemini 2.5, indica al modello il numero specifico di token di ragionamento da utilizzare per il ragionamento.

Di seguito sono riportati i dettagli di configurazione di `thinkingBudget` per ogni tipo di modello.
Puoi disattivare il ragionamento impostando `thinkingBudget` su 0.
Se imposti `thinkingBudget` su -1, viene attivato il **ragionamento dinamico**, il che significa che il modello regolerà il budget in base alla complessità della richiesta.

| Modello | Impostazione predefinita (il budget di ragionamento non è impostato) | Intervallo | Disattiva il ragionamento | Attiva il ragionamento dinamico |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Ragionamento dinamico | Da `128` a `32768` | N/A: non è possibile disattivare il ragionamento | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash** | Ragionamento dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash (anteprima)** | Ragionamento dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash Lite** | Il modello non ragiona | Da `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite (anteprima)** | Il modello non ragiona | Da `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 (anteprima)** | Ragionamento dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |
| **2.5 Flash Live Native Audio (anteprima) (09-2025)** | Ragionamento dinamico | Da `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (valore predefinito) |

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

## Firme del ragionamento

L'API Gemini è senza stato, quindi il modello tratta ogni richiesta API in modo indipendente e non ha accesso al contesto di ragionamento dei turni precedenti nelle interazioni in più turni.

Per consentire il mantenimento del contesto di ragionamento nelle interazioni in più turni, Gemini restituisce le firme del ragionamento, che sono rappresentazioni criptate del processo di ragionamento interno del modello.

- **I modelli Gemini 2.5** restituiscono le firme del ragionamento quando il ragionamento è attivato e
  la richiesta include [la chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#thinking),
  in particolare [le dichiarazioni di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-2).
- I **modelli Gemini 3** possono restituire le firme del ragionamento per tutti i tipi di [parti](https://ai.google.dev/api/caching?hl=it#Part).
  Ti consigliamo di restituire sempre tutte le firme così come le hai ricevute, ma è *obbligatorio* per le firme di chiamata di funzione. Per saperne di più, consulta la pagina
  [Firme del ragionamento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it).

Altre limitazioni di utilizzo da considerare con la chiamata di funzione includono:

- Le firme vengono restituite dal modello all'interno di altre parti della risposta, ad esempio le parti di chiamata di funzione o di testo.
  [Restituisci l'intera risposta](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-4)
  con tutte le parti al modello nei turni successivi.
- Non concatenare le parti con le firme.
- Non unire una parte con una firma con un'altra parte senza firma.

## Prezzi

Quando il ragionamento è attivato, il prezzo della risposta è la somma dei token di output e dei token di ragionamento. Puoi ottenere il numero totale di token di ragionamento generati dal campo `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
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
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

I modelli di ragionamento generano ragionamenti completi per migliorare la qualità della risposta finale
e poi restituiscono i [riepiloghi](#summaries) per fornire informazioni sul
processo di ragionamento. Pertanto, il prezzo si basa sui token di ragionamento completi che il modello deve generare per creare un riepilogo, anche se dall'API viene restituito solo il riepilogo.

Per saperne di più sui token, consulta la [guida](https://ai.google.dev/gemini-api/docs/tokens?hl=it)
al conteggio dei token.

## Best practice

Questa sezione include alcune indicazioni per l'utilizzo efficiente dei modelli di ragionamento.
Come sempre, seguendo le nostre [indicazioni e best practice per i prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it) otterrai i risultati migliori.

### Debug e guida

- **Esamina il ragionamento**: quando non ricevi la risposta prevista dai
  modelli di ragionamento, può essere utile analizzare attentamente i riepiloghi del ragionamento di Gemini.
  Puoi vedere come ha suddiviso l'attività e come è arrivato alla sua conclusione e utilizzare queste informazioni per correggere i risultati corretti.
- **Fornisci indicazioni nel ragionamento**: se prevedi un output particolarmente lungo, potresti voler fornire indicazioni nel prompt per limitare la
  [quantità di ragionamento](#set-budget) utilizzata dal modello. In questo modo, puoi riservare più token di output per la risposta.

### Complessità dell'attività

- **Attività semplici (il ragionamento potrebbe essere disattivato):** per le richieste semplici in cui non è richiesto un ragionamento complesso, come il recupero o la classificazione dei fatti, il ragionamento non è necessario. Di seguito trovi alcuni esempi.
  - "Dove è stata fondata DeepMind?"
  - "Questa email chiede una riunione o fornisce solo informazioni?"
- **Attività di media difficoltà (ragionamento predefinito/parziale):** molte richieste comuni traggono vantaggio da un certo grado di elaborazione passo passo o da una comprensione più approfondita. Gemini può utilizzare in modo flessibile la funzionalità di ragionamento per attività come:
  - Analogizzare la fotosintesi e la crescita.
  - Confrontare e contrapporre auto elettriche e auto ibride.
- **Attività difficili (capacità di ragionamento massima):** per le sfide veramente complesse, come la risoluzione di problemi di matematica complessi o attività di programmazione, ti consigliamo di impostare un budget di ragionamento elevato. Questi tipi di attività richiedono che il modello utilizzi tutte le sue capacità di ragionamento e pianificazione, spesso coinvolgendo molti passaggi interni prima di fornire una risposta. Di seguito trovi alcuni esempi.
  - Risolvi il problema 1 in AIME 2025: trova la somma di tutte le basi intere b > 9 per
    le quali 17b è un divisore di 97b.
  - Scrivi codice Python per un'applicazione web che visualizzi i dati del mercato azionario in tempo reale, inclusa l'autenticazione utente. Rendilo il più efficiente possibile.

## Modelli, strumenti e funzionalità supportati

Le funzionalità di ragionamento sono supportate su tutti i modelli delle serie 3 e 2.5.
Puoi trovare tutte le funzionalità del modello nella
[pagina di panoramica del modello](https://ai.google.dev/gemini-api/docs/models?hl=it).

I modelli di ragionamento funzionano con tutti gli strumenti e le funzionalità di Gemini. In questo modo, i modelli possono interagire con sistemi esterni, eseguire codice o accedere a informazioni in tempo reale, incorporando i risultati nel loro ragionamento e nella risposta finale.

Puoi provare esempi di utilizzo degli strumenti con i modelli di ragionamento nel
[ricettario di ragionamento](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb?hl=it).

## Passaggi successivi

- La copertura del ragionamento è disponibile nella nostra guida alla compatibilità con [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it#thinking).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
