---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=it
fetched_at: 2026-05-05T13:26:42.380548+00:00
title: "Guida rapida all'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

- [Home page](https://ai.google.dev/gemini-api/docs/Home page)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documenti](https://ai.google.dev/gemini-api/docs/Documenti)

Invia feedback

# Guida rapida all'API Gemini

Questa guida rapida mostra come installare le nostre [librerie](https://ai.google.dev/gemini-api/docs/librerie)
ed effettuare la prima richiesta all'API Gemini.

## Prima di iniziare

Per utilizzare l'API Gemini è necessaria una chiave API, che puoi creare senza costi per iniziare.

[Crea una chiave API Gemini](https://ai.google.dev/gemini-api/docs/Crea una chiave API Gemini)

## Installa l'SDK Google GenAI

### Python

Utilizzando [Python 3.9 o versioni successive](https://ai.google.dev/gemini-api/docs/Python 3.9 o versioni successive), installa il
[`google-genai` pacchetto](https://ai.google.dev/gemini-api/docs/`google-genai` pacchetto)
utilizzando il seguente
[comando pip](https://ai.google.dev/gemini-api/docs/comando pip):

```
pip install -q -U google-genai
```

### JavaScript

Utilizzando [Node.js v18+](https://ai.google.dev/gemini-api/docs/Node.js v18+),
installa l'
[SDK Google Gen AI per TypeScript e JavaScript](https://ai.google.dev/gemini-api/docs/SDK Google Gen AI per TypeScript e JavaScript)
utilizzando il seguente
[comando npm](https://ai.google.dev/gemini-api/docs/comando npm):

```
npm install @google/genai
```

### Vai

Installa
[google.golang.org/genai](https://ai.google.dev/gemini-api/docs/google.golang.org/genai) nella
directory del modulo utilizzando il [comando go get](https://ai.google.dev/gemini-api/docs/comando go get):

```
go get google.golang.org/genai
```

### Java

Se utilizzi Maven, puoi installare
[google-genai](https://ai.google.dev/gemini-api/docs/google-genai) aggiungendo quanto segue alle dipendenze:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

Installa
[googleapis/go-genai](https://ai.google.dev/gemini-api/docs/googleapis/go-genai) nella
directory del modulo utilizzando il [comando dotnet add](https://ai.google.dev/gemini-api/docs/comando dotnet add)

```
dotnet add package Google.GenAI
```

### Apps Script

1. Per creare un nuovo progetto Apps Script, vai a
   [script.new](https://ai.google.dev/gemini-api/docs/script.new).
2. Fai clic su **Progetto senza titolo**.
3. Rinomina il progetto Apps Script **AI Studio** e fai clic su **Rinomina**.
4. Imposta la [chiave API](https://ai.google.dev/gemini-api/docs/chiave API)
   1. A sinistra, fai clic su **Impostazioni progetto** ![L&#39;icona delle impostazioni progetto](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
   2. In **Proprietà script** fai clic su **Aggiungi proprietà script**.
   3. In **Proprietà**, inserisci il nome della chiave: `GEMINI_API_KEY`.
   4. In **Valore**, inserisci il valore della chiave API.
   5. Fai clic su **Salva proprietà script**.
5. Sostituisci i contenuti del file `Code.gs` con il seguente codice:

## Effettua la prima richiesta

Ecco un esempio che utilizza il
[`generateContent`](https://ai.google.dev/gemini-api/docs/`generateContent`) metodo
per inviare una richiesta all'API Gemini utilizzando il modello Gemini 2.5 Flash.

Se [imposti la chiave API](https://ai.google.dev/gemini-api/docs/imposti la chiave API) come
variabile di ambiente `GEMINI_API_KEY`, il client la rileverà automaticamente quando utilizzi le [librerie dell'API Gemini](https://ai.google.dev/gemini-api/docs/librerie dell'API Gemini).
In caso contrario, dovrai [passare la chiave API](https://ai.google.dev/gemini-api/docs/passare la chiave API) come
argomento durante l'inizializzazione del client.

Tieni presente che tutti gli esempi di codice nella documentazione dell'API Gemini presuppongono che tu abbia impostato la variabile di ambiente `GEMINI_API_KEY`.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
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
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Passaggi successivi

Ora che hai effettuato la prima richiesta API, potresti voler esplorare le seguenti guide che mostrano Gemini in azione:

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/Generazione di testo)
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/Generazione di immagini)
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/Comprensione delle immagini)
- [Ragionamento](https://ai.google.dev/gemini-api/docs/Ragionamento)
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/Chiamata di funzione)
- [Contesto lungo](https://ai.google.dev/gemini-api/docs/Contesto lungo)
- [Incorporamenti](https://ai.google.dev/gemini-api/docs/Incorporamenti)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/licenza Creative Commons Attribution 4.0), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://ai.google.dev/gemini-api/docs/licenza Apache 2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://ai.google.dev/gemini-api/docs/norme del sito di Google Developers). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?
