---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=de
fetched_at: 2026-07-06T05:07:07.676840+00:00
title: "Kontext-Caching \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Kontext-Caching

In einem typischen KI-Workflow werden dieselben Eingabetokens möglicherweise immer wieder an ein Modell übergeben. Die Gemini API bietet zwei verschiedene Caching-Mechanismen:

- Implizites Caching (automatisch für Gemini 2.5 und neuere Modelle aktiviert, keine Garantie für Kosteneinsparungen)
- Explizites Caching (kann bei den meisten Modellen manuell aktiviert werden, Kosteneinsparungsgarantie)

Explizites Caching ist nützlich, wenn Sie Kosten sparen möchten, aber dafür etwas mehr Entwicklerarbeit in Kauf nehmen.

## Implizites Caching

Implizites Caching ist für alle Gemini 2.5-Modelle und neuere Modelle standardmäßig aktiviert. Wir geben Kosteneinsparungen automatisch weiter, wenn Ihre Anfrage auf Caches trifft. Sie müssen nichts weiter tun, um diese Funktion zu aktivieren. Die Mindestanzahl an Eingabetokens für das Zwischenspeichern von Kontext ist in der folgenden Tabelle für jedes Modell aufgeführt:

| Modell | Mindest-Tokenlimit |
| --- | --- |
| Gemini 3.5 Flash | 4.096 |
| Gemini 3.1 Pro (Vorabversion) | 4.096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

So erhöhen Sie die Wahrscheinlichkeit eines impliziten Cache-Treffers:

- Große und gängige Inhalte am Anfang des Prompts platzieren
- Versuchen Sie, Anfragen mit ähnlichem Präfix innerhalb kurzer Zeit zu senden.

Die Anzahl der Tokens, die Cache-Treffer waren, finden Sie im Feld `usage_metadata` des Antwortobjekts.

## Explizites Caching

Mit der Funktion zum expliziten Caching der Gemini API können Sie einige Inhalte einmal an das Modell übergeben, die Eingabe-Tokens im Cache speichern und dann bei nachfolgenden Anfragen auf die im Cache gespeicherten Tokens verweisen. Bei bestimmten Mengen ist die Verwendung von im Cache gespeicherten Tokens kostengünstiger als die wiederholte Übergabe desselben Token-Korpus.

Wenn Sie eine Gruppe von Tokens im Cache speichern, können Sie festlegen, wie lange der Cache bestehen soll, bevor die Tokens automatisch gelöscht werden. Diese Caching-Dauer wird als *Gültigkeitsdauer* (time to live, TTL) bezeichnet. Wenn nichts anderes festgelegt ist, beträgt die TTL standardmäßig 1 Stunde. Die Kosten für das Caching hängen von der Größe der Eingabetokens und der Dauer ab, für die die Tokens beibehalten werden sollen.

In diesem Abschnitt wird davon ausgegangen, dass Sie ein Gemini SDK installiert haben (oder curl installiert ist) und dass Sie einen API-Schlüssel konfiguriert haben, wie im [Leitfaden für den Einstieg](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de) beschrieben.

### Inhalte mit einem Cache generieren

### Python

Im folgenden Beispiel wird gezeigt, wie Sie Inhalte mit einer im Cache gespeicherten Systemanweisung und Videodatei generieren.

### Videos

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

model='models/gemini-3.5-flash'

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

### PDF-Dateien

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

model_name = "gemini-3.5-flash"
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

Im folgenden Beispiel wird gezeigt, wie Sie Inhalte mit einer im Cache gespeicherten Systemanweisung und einer Textdatei generieren.

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

  const modelName = "gemini-3.5-flash";
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

### Ok

Im folgenden Beispiel wird gezeigt, wie Inhalte mithilfe eines Cache generiert werden.

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

    modelName := "gemini-3.5-flash"
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

Im folgenden Beispiel wird gezeigt, wie ein Cache erstellt und dann zum Generieren von Inhalten verwendet wird.

### Videos

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.5-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
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

### PDF-Dateien

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.5-flash"
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

### Caches auflisten

Es ist nicht möglich, im Cache gespeicherte Inhalte abzurufen oder anzusehen, aber Sie können Cache-Metadaten (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time` und `expire_time`) abrufen.

### Python

Verwenden Sie `CachedContent.list()`, um Metadaten für alle hochgeladenen Caches aufzulisten:

```
for cache in client.caches.list():
  print(cache)
```

Wenn Sie die Metadaten für ein Cacheobjekt abrufen möchten und den Namen des Objekts kennen, verwenden Sie `get`:

```
client.caches.get(name=name)
```

### JavaScript

Verwenden Sie `GoogleGenAI.caches.list()`, um Metadaten für alle hochgeladenen Caches aufzulisten:

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

### Ok

Im folgenden Beispiel werden alle Caches aufgelistet.

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

Im folgenden Beispiel werden Caches mit einer Seitengröße von 2 aufgelistet.

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

### Cache aktualisieren

Sie können für einen Cache eine neue `ttl` oder `expire_time` festlegen. Das Ändern anderer Aspekte des Caches wird nicht unterstützt.

### Python

Im folgenden Beispiel wird gezeigt, wie Sie die `ttl` eines Cache mit `client.caches.update()` aktualisieren.

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

Zum Festlegen der Ablaufzeit kann entweder ein `datetime`-Objekt oder ein ISO-formatierter Datetime-String (`dt.isoformat()`, z. B. `2025-01-27T16:02:36.473528+00:00`) verwendet werden. Ihre Zeit muss eine Zeitzone enthalten (`datetime.utcnow()` fügt keine Zeitzone an, `datetime.now(datetime.timezone.utc)` schon).

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

Im folgenden Beispiel wird gezeigt, wie Sie die `ttl` eines Cache mit `GoogleGenAI.caches.update()` aktualisieren.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Ok

Das folgende Beispiel zeigt, wie Sie die `TTL` eines Cache aktualisieren.

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

Das folgende Beispiel zeigt, wie Sie die `ttl` eines Cache aktualisieren.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Cache löschen

Der Caching-Dienst bietet einen Löschvorgang zum manuellen Entfernen von Inhalten aus dem Cache. Das folgende Beispiel zeigt, wie ein Cache gelöscht wird:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Ok

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

### Explizites Caching mit der OpenAI-Bibliothek

Wenn Sie eine [OpenAI-Bibliothek](https://ai.google.dev/gemini-api/docs/openai?hl=de) verwenden, können Sie das explizite Caching mit der Eigenschaft `cached_content` für [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=de#extra-body) aktivieren.

## Wann sollte explizites Caching verwendet werden?

Kontext-Caching eignet sich besonders für Szenarien, bei denen in kürzeren Anfragen wiederholt auf eine hohe anfängliche Kontextmenge verwiesen wird. Ziehen Sie die Verwendung von Kontext-Caching für Anwendungsfälle wie diese in Betracht:

- Chatbots mit ausführlichen [Systemanweisungen](https://ai.google.dev/gemini-api/docs/system-instructions?hl=de)
- Wiederholte Analyse langer Videodateien
- Wiederkehrende Abfragen großer Dokumentgruppen
- Häufige Analyse des Code-Repositorys oder Fehlerbehebung

### So werden Kosten durch explizites Caching gesenkt

Das Kontext-Caching ist eine kostenpflichtige Funktion, die darauf ausgelegt ist, die Kosten zu senken. Die Abrechnung basiert auf den folgenden Faktoren:

1. **Anzahl der Cache-Tokens:** Die Anzahl der im Cache gespeicherten Eingabetokens, für die ein ermäßigter Tarif für die Nutzung in nachfolgenden Prompts gilt.
2. **Speicherdauer**:Die Zeit, über die hinweg im Cache gespeicherte Tokens erhalten werden (TTL). Die Abrechnung erfolgt auf Grundlage der TTL-Dauer der Anzahl der im Cache gespeicherten Tokens. Es gibt keine Mindest- oder Höchstwerte für die TTL.
3. **Andere Faktoren:** Es fallen weitere Gebühren an, z. B. für nicht im Cache gespeicherte Eingabe- und Ausgabetokens.

Aktuelle Preisinformationen finden Sie auf der [Preisseite für die Gemini API](https://ai.google.dev/pricing?hl=de). Informationen zum Zählen von Tokens finden Sie im [Token-Leitfaden](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

### Weitere Überlegungen

Beachten Sie bei der Verwendung von Kontext-Caching Folgendes:

- Die *Mindestanzahl* der Eingabetokens für das Kontext-Caching variiert je nach Modell. Der *Höchstwert* entspricht dem Höchstwert für das angegebene Modell. Weitere Informationen zum Zählen von Tokens finden Sie im [Token-Leitfaden](https://ai.google.dev/gemini-api/docs/tokens?hl=de).
- Das Modell unterscheidet nicht zwischen zwischengespeicherten und regulären Eingabetokens. Im Cache gespeicherte Inhalte werden dem Prompt vorangestellt.
- Für das Zwischenspeichern von Kontexten gelten keine besonderen Raten- oder Nutzungslimits. Es gelten die Standardratenlimits für `GenerateContent` und die Tokenlimits umfassen zwischengespeicherte Tokens.
- Die Anzahl der im Cache gespeicherten Tokens wird in `usage_metadata` der Cache-Dienstvorgänge „create“, „get“ und „list“ sowie in `GenerateContent` bei Verwendung des Cache zurückgegeben.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-24 (UTC)."],[],[]]
