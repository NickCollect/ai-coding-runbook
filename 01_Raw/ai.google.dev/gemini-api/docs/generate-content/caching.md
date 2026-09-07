---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=pl
fetched_at: 2026-09-07T05:36:07.026077+00:00
title: "Buforowanie kontekstu \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Buforowanie kontekstu

W typowym procesie AI możesz wielokrotnie przekazywać te same tokeny wejściowe do modelu. Gemini API oferuje 2 różne mechanizmy buforowania:

- niejawne buforowanie (automatycznie włączone w modelach Gemini 2.5 i nowszych, bez gwarancji oszczędności kosztów);
- jawne buforowanie (można je włączyć ręcznie w większości modeli, z gwarancją oszczędności kosztów).

Jawne buforowanie jest przydatne w przypadkach, gdy chcesz zagwarantować oszczędności kosztów, ale musisz wykonać dodatkowe prace programistyczne.

## Niejawne buforowanie

Niejawne buforowanie jest domyślnie włączone we wszystkich modelach Gemini 2.5 i nowszych. Automatycznie przekazujemy oszczędności kosztów, jeśli Twoje żądanie trafi do pamięci podręcznej. Aby to włączyć, nie musisz nic robić. Minimalna liczba tokenów wejściowych w przypadku buforowania kontekstu jest podana w tabeli poniżej dla każdego modelu:

| Model | Minimalny limit tokenów |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro (wersja testowa) | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Aby zwiększyć szansę na trafienie do niejawnej pamięci podręcznej:

- Spróbuj umieścić duże i popularne treści na początku prompta.
- Spróbuj wysyłać żądania z podobnym prefiksem w krótkim czasie.

Liczbę tokenów, które zostały trafione do pamięci podręcznej, możesz sprawdzić w polu `usage_metadata` obiektu odpowiedzi.

## Jawne buforowanie

Dzięki funkcji jawnego buforowania Gemini API możesz przekazać modelowi część treści, zapisać tokeny wejściowe w pamięci podręcznej, a następnie odwoływać się do nich w kolejnych żądaniach. W przypadku określonych ilości używanie tokenów z pamięci podręcznej jest tańsze niż wielokrotne przekazywanie tego samego korpusu tokenów.

Gdy zapisujesz w pamięci podręcznej zestaw tokenów, możesz wybrać, jak długo ma ona istnieć, zanim tokeny zostaną automatycznie usunięte. Ten czas buforowania nazywa się *czasem życia danych* (TTL). Jeśli nie jest ustawiony, domyślny czas TTL wynosi 1 godzinę. Koszt buforowania zależy od rozmiaru tokena wejściowego i czasu, przez jaki chcesz przechowywać tokeny.

W tej sekcji zakładamy, że masz zainstalowany pakiet SDK Gemini (lub zainstalowany curl)
i skonfigurowany klucz interfejsu API zgodnie z instrukcjami w
[przewodniku dla początkujących](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl).

### Generowanie treści za pomocą pamięci podręcznej

### Python

Poniższy przykład pokazuje, jak wygenerować treści za pomocą instrukcji systemowej i pliku wideo z pamięci podręcznej.

### Filmy

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

model='models/gemini-3.6-flash'

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

### Pliki PDF

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

model_name = "gemini-3.6-flash"
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

Poniższy przykład pokazuje, jak wygenerować treści za pomocą instrukcji systemowej i pliku tekstowego z pamięci podręcznej.

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

  const modelName = "gemini-3.6-flash";
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

### Go

Poniższy przykład pokazuje, jak wygenerować treści za pomocą pamięci podręcznej.

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

    modelName := "gemini-3.6-flash"
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

Poniższy przykład pokazuje, jak utworzyć pamięć podręczną, a następnie użyć jej do wygenerowania treści.

### Filmy

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.6-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
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

### Pliki PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.6-flash"
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

### Wyświetlanie pamięci podręcznych

Nie można pobrać ani wyświetlić treści z pamięci podręcznej, ale można pobrać
metadane pamięci podręcznej (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` i `expire_time`).

### Python

Aby wyświetlić metadane wszystkich przesłanych pamięci podręcznych, użyj `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Aby pobrać metadane jednego obiektu pamięci podręcznej, jeśli znasz jego nazwę, użyj `get`:

```
client.caches.get(name=name)
```

### JavaScript

Aby wyświetlić metadane wszystkich przesłanych pamięci podręcznych, użyj `GoogleGenAI.caches.list()`:

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

### Go

Poniższy przykład pokazuje, jak wyświetlić wszystkie pamięci podręczne.

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

Poniższy przykład pokazuje, jak wyświetlić pamięci podręczne z rozmiarem strony 2.

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

### Aktualizowanie pamięci podręcznej

Możesz ustawić nowy `ttl` lub `expire_time` dla pamięci podręcznej. Zmiana innych ustawień pamięci podręcznej nie jest obsługiwana.

### Python

Poniższy przykład pokazuje, jak zaktualizować `ttl` pamięci podręcznej za pomocą `client.caches.update()`.

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

Aby ustawić czas wygaśnięcia, możesz użyć obiektu `datetime`lub ciągu daty i godziny w formacie ISO (`dt.isoformat()`, np.
`2025-01-27T16:02:36.473528+00:00`). Czas musi zawierać strefę czasową
(`datetime.utcnow()` nie dołącza strefy czasowej,
`datetime.now(datetime.timezone.utc)` ją dołącza).

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

Poniższy przykład pokazuje, jak zaktualizować `ttl` pamięci podręcznej za pomocą `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

Poniższy przykład pokazuje, jak zaktualizować `TTL` pamięci podręcznej.

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

Poniższy przykład pokazuje, jak zaktualizować `ttl` pamięci podręcznej.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Usuwanie pamięci podręcznej

Usługa buforowania udostępnia operację usuwania, która umożliwia ręczne usuwanie treści z pamięci podręcznej. Poniższy przykład pokazuje, jak usunąć pamięć podręczną:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Go

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

### Jawne buforowanie za pomocą biblioteki OpenAI

Jeśli używasz biblioteki [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl), możesz włączyć
jawne buforowanie za pomocą właściwości `cached_content` w
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=pl#extra-body).

## Kiedy używać jawnego buforowania

Buforowanie kontekstu jest szczególnie przydatne w sytuacjach, gdy obszerny kontekst początkowy jest wielokrotnie przywoływany przez krótsze żądania. Rozważ użycie buforowania kontekstu w takich przypadkach:

- czatboty z rozbudowanymi [instrukcjami systemowymi](https://ai.google.dev/gemini-api/docs/system-instructions?hl=pl)
- powtarzająca się analiza długich plików wideo;
- powtarzające się zapytania dotyczące dużych zbiorów dokumentów;
- częsta analiza repozytorium kodu lub naprawianie błędów.

### Jak jawne buforowanie obniża koszty

Buforowanie kontekstu to płatna funkcja, która ma na celu obniżenie kosztów. Rozliczenia zależą od tych czynników:

1. **Liczba tokenów w pamięci podręcznej:** liczba tokenów wejściowych zapisanych w pamięci podręcznej, za które naliczana jest niższa opłata, gdy są one uwzględniane w kolejnych promptach.
2. **Czas przechowywania:** czas przechowywania tokenów w pamięci podręcznej (TTL), za który naliczana jest opłata na podstawie czasu TTL liczby tokenów w pamięci podręcznej. Nie ma minimalnego ani maksymalnego czasu TTL.
3. **Inne czynniki:** obowiązują inne opłaty, np. za tokeny wejściowe i wyjściowe, które nie są zapisane w pamięci podręcznej.

Aktualne informacje o cenach znajdziesz na stronie cennika Gemini API [pricing
page](https://ai.google.dev/pricing?hl=pl). Aby dowiedzieć się, jak liczyć tokeny, zapoznaj się z przewodnikiem po [tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

### Uwagi dodatkowe

Korzystając z buforowania kontekstu, pamiętaj o tych kwestiach:

- *Minimalna* liczba tokenów wejściowych w przypadku buforowania kontekstu różni się w zależności od modelu. *Maksymalna* liczba tokenów jest taka sama jak maksymalna liczba tokenów w danym modelu. (Więcej informacji o liczeniu tokenów,
  zobacz [przewodnik po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl)).
- Model nie rozróżnia tokenów z pamięci podręcznej i zwykłych tokenów wejściowych. Treści z pamięci podręcznej są prefiksem prompta.
- W przypadku buforowania kontekstu nie obowiązują żadne specjalne limity stawek ani limity wykorzystania. Obowiązują standardowe limity stawek dla `GenerateContent`, a limity tokenów obejmują tokeny z pamięci podręcznej.
- Liczba tokenów z pamięci podręcznej jest zwracana w `usage_metadata` z operacji tworzenia, pobierania i wyświetlania usługi pamięci podręcznej, a także w `GenerateContent` podczas korzystania z pamięci podręcznej.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
