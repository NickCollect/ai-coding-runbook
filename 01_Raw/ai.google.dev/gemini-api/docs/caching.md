---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=it
fetched_at: 2026-05-05T20:00:37.007138+00:00
title: "Memorizzazione nella cache del contesto \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Memorizzazione nella cache del contesto

In un flusso di lavoro di AI tipico, potresti passare gli stessi token di input più e più volte a un modello. L'API Gemini offre due meccanismi di memorizzazione nella cache diversi:

- Memorizzazione nella cache implicita (abilitata automaticamente sui modelli Gemini 2.5 e versioni successive, senza garanzia di risparmio sui costi)
- Memorizzazione nella cache esplicita (può essere abilitata manualmente sulla maggior parte dei modelli, con garanzia di risparmio sui costi)

La memorizzazione nella cache esplicita è utile nei casi in cui vuoi garantire un risparmio sui costi, ma con un po' di lavoro di sviluppo in più.

## Memorizzazione nella cache implicita

La memorizzazione nella cache implicita è abilitata per impostazione predefinita per tutti i modelli Gemini 2.5 e versioni successive. Trasmettiamo automaticamente i risparmi sui costi se la tua richiesta raggiunge le cache. Non devi fare nulla per abilitare questa funzionalità. Il conteggio minimo dei token di input per la memorizzazione nella cache del contesto è elencato nella tabella seguente per ogni modello:

| Modello | Limite minimo di token |
| --- | --- |
| Gemini 3 Flash (anteprima) | 1024 |
| Gemini 3 Pro (anteprima) | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

Per aumentare la probabilità di un successo della cache implicita:

- Prova a inserire contenuti di grandi dimensioni e comuni all'inizio del prompt
- Prova a inviare richieste con prefisso simile in un breve periodo di tempo

Puoi vedere il numero di token che sono stati hit della cache nel campo `usage_metadata` dell'oggetto della risposta.

## Memorizzazione nella cache esplicita

Utilizzando la funzionalità di memorizzazione nella cache esplicita dell'API Gemini, puoi passare alcuni contenuti al modello una sola volta, memorizzare nella cache i token di input e poi fare riferimento ai token memorizzati nella cache per le richieste successive. Per determinati volumi, l'utilizzo di token memorizzati nella cache è meno costoso rispetto al passaggio ripetuto dello stesso corpus di token.

Quando memorizzi nella cache un insieme di token, puoi scegliere per quanto tempo vuoi che la cache esista prima che i token vengano eliminati automaticamente. Questa durata della memorizzazione nella cache è chiamata *durata (TTL)*. Se non viene impostata, la durata (TTL) è di 1 ora per impostazione predefinita. Il costo della memorizzazione nella cache dipende dalle dimensioni dei token di input e dalla durata di persistenza dei token.

Questa sezione presuppone che tu abbia installato un SDK Gemini (o curl)
e che tu abbia configurato una chiave API, come mostrato nella
[guida rapida](https://ai.google.dev/gemini-api/docs/quickstart?hl=it).

### Generare contenuti utilizzando una cache

### Python

L'esempio seguente mostra come generare contenuti utilizzando un'istruzione di sistema e un file video memorizzati nella cache.

### Video

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3-flash-preview'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3-flash-preview"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

L'esempio seguente mostra come generare contenuti utilizzando un'istruzione di sistema e un file di testo memorizzati nella cache.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3-flash-preview";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Vai

L'esempio seguente mostra come generare contenuti utilizzando una cache.

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3-flash-preview"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

L'esempio seguente mostra come creare una cache e poi utilizzarla per generare contenuti.

### Video

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3-flash-preview",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3-flash-preview"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### Elencare le cache

Non è possibile recuperare o visualizzare i contenuti memorizzati nella cache, ma puoi recuperare
i metadati della cache (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` e `expire_time`).

### Python

Per elencare i metadati di tutte le cache caricate, utilizza `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Per recuperare i metadati di un oggetto cache, se ne conosci il nome, utilizza `get`:

```
client.caches.get(name=name)
```

### JavaScript

Per elencare i metadati di tutte le cache caricate, utilizza `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Vai

L'esempio seguente elenca tutte le cache.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

L'esempio seguente elenca le cache utilizzando una dimensione della pagina di 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### Aggiornare una cache

Puoi impostare una nuova `ttl` o `expire_time` per una cache. La modifica di qualsiasi altro elemento della cache non è supportata.

### Python

L'esempio seguente mostra come aggiornare la `ttl` di una cache utilizzando `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

Per impostare la data di scadenza, accetta un oggetto `datetime`o una stringa datetime in formato ISO (`dt.isoformat()`, ad esempio
`2025-01-27T16:02:36.473528+00:00`). L'ora deve includere un fuso orario
(`datetime.utcnow()` non associa un fuso orario,
`datetime.now(datetime.timezone.utc)` associa un fuso orario).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

L'esempio seguente mostra come aggiornare la `ttl` di una cache utilizzando `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Vai

L'esempio seguente mostra come aggiornare la `TTL` di una cache.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

L'esempio seguente mostra come aggiornare la `ttl` di una cache.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Eliminare una cache

Il servizio di memorizzazione nella cache fornisce un'operazione di eliminazione per rimuovere manualmente i contenuti dalla cache. L'esempio seguente mostra come eliminare una cache:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Vai

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### Memorizzazione nella cache esplicita utilizzando la libreria OpenAI

Se utilizzi una [libreria OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it), puoi abilitare la
memorizzazione nella cache esplicita utilizzando la proprietà `cached_content` su
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=it#extra-body).

## Quando utilizzare la memorizzazione nella cache esplicita

La memorizzazione nella cache del contesto è particolarmente adatta agli scenari in cui un contesto iniziale sostanziale viene referenziato ripetutamente da richieste più brevi. Valuta la possibilità di utilizzare la memorizzazione nella cache del contesto per casi d'uso come:

- Chatbot con istruzioni di sistema estese [system instructions](https://ai.google.dev/gemini-api/docs/system-instructions?hl=it)
- Analisi ripetitiva di file video lunghi
- Query ricorrenti su grandi set di documenti
- Analisi frequente del repository di codice o correzione di bug

### In che modo la memorizzazione nella cache esplicita riduce i costi

La memorizzazione nella cache del contesto è una funzionalità a pagamento progettata per ridurre i costi. La fatturazione si basa sui seguenti fattori:

1. **Conteggio dei token della cache:** il numero di token di input memorizzati nella cache, fatturati a una tariffa ridotta se inclusi nei prompt successivi.
2. **Durata di archiviazione:** il periodo di tempo in cui i token memorizzati nella cache vengono archiviati (durata (TTL)), fatturati in base alla durata (TTL) del conteggio dei token memorizzati nella cache. Non esistono limiti minimi o massimi per la durata (TTL).
3. **Altri fattori:** si applicano altri addebiti, ad esempio per i token di input e di output non memorizzati nella cache.

Per i dettagli sui prezzi aggiornati, consulta la pagina dei [prezzi
dell'API Gemini](https://ai.google.dev/pricing?hl=it). Per scoprire come contare i token, consulta la [Token
guide](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

### Considerazioni aggiuntive

Tieni presente le seguenti considerazioni quando utilizzi la memorizzazione nella cache del contesto:

- Il conteggio dei token di input *minimo* per la memorizzazione nella cache del contesto varia in base al modello. Il valore *massimo* è lo stesso del valore massimo per il modello specificato. Per ulteriori informazioni sul conteggio dei token,
  consulta la [guida ai token](https://ai.google.dev/gemini-api/docs/tokens?hl=it)).
- Il modello non fa distinzione tra i token memorizzati nella cache e i token di input normali. I contenuti memorizzati nella cache sono un prefisso del prompt.
- Non esistono limiti di tariffa o di utilizzo speciali per la memorizzazione nella cache del contesto; si applicano i limiti di frequenza standard per `GenerateContent` e i limiti di token includono i token memorizzati nella cache.
- Il numero di token memorizzati nella cache viene restituito in `usage_metadata` dalle operazioni di creazione, recupero ed elenco del servizio di memorizzazione nella cache e anche in `GenerateContent` quando si utilizza la cache.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
