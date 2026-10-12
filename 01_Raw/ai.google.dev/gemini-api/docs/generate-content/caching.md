---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=sq
fetched_at: 2026-10-12T06:58:41.677614+00:00
title: "Ruajtja e kontekstit n\u00eb memorien specifike \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash është tani në dispozicion. [Provojeni](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=sq) .

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Ruajtja e kontekstit në memorien specifike

Në një fluks tipik pune të IA-së, mund t'i kalosh të njëjtët kode hyrëse vazhdimisht te një model. Gemini API ofron dy mekanizma të ndryshëm të ruajtjes në memorien specifike:

- Ruajtja e fshehtë e të dhënave në mënyrë të nënkuptuar (aktivizuar automatikisht në Gemini 2.5 dhe modelet më të reja, pa garanci për kursimin e kostos)
- Ruajtja e qartë në memorien specifike (mund të aktivizohet manualisht në shumicën e modeleve, garanci për kursim kostosh)

Ruajtja e qartë në memorien specifike është e dobishme në rastet kur dëshiron të garantosh kursime kostosh,
por me pak punë shtesë nga zhvilluesi.

## Ruajtja e nënkuptuar në memorien specifike

Ruajtja e fshehtë e të dhënave është e aktivizuar si parazgjedhje për të gjitha modelet Gemini 2.5 dhe më të reja. Ne i kalojmë automatikisht
kursimet e kostos nëse kërkesa jote arrin te memoriet specifike. Nuk ka asgjë që duhet të bësh për ta aktivizuar këtë. Numri minimal i kodeve hyrëse
për ruajtjen në memorien specifike të kontekstit është listuar në tabelën e mëposhtme për secilin model:

| Modeli | Kufiri minimal i tokenëve |
| --- | --- |
| Gemini 3.8 Flash | 4,096 |
| Gemini 3.6 Flash | 4,096 |
| Gemini 3.1 Pro Preview | 4,096 |
| Gemini 2.5 Flash | 2,048 |
| Gemini 2.5 Pro | 2,048 |

Për të rritur mundësinë e një përputhjeje të nënkuptuar të memories specifike:

- Provo të vendosësh përmbajtje të mëdha dhe të zakonshme në fillim të kërkesës sate
- Provo të dërgosh kërkesa me prefiks të ngjashëm në një kohë të shkurtër

Mund të shohësh numrin e kodeve që ishin goditje të memories specifike në fushën `usage_metadata` të objektit të përgjigjes.

## Ruajtja specifike

Duke përdorur veçorinë e ruajtjes specifike në memorien specifike të Gemini API, mund t'i kalosh disa përmbajtje te modeli një herë, të ruash në memorien specifike kodet hyrëse dhe më pas t'i referohesh kodeve të ruajtura në memorien specifike për kërkesat vijuese. Në vëllime të caktuara, përdorimi i kodeve të ruajtura në memorien specifike është me kosto më të ulët se kalimi i të njëjtit korpus kodësh në mënyrë të përsëritur.

Kur ruan në memorien specifike një grup token-ësh, mund të zgjedhësh se për sa kohë dëshiron që të ekzistojë memoria specifike para se token-at të fshihen automatikisht. Kjo kohëzgjatje e ruajtjes në memorien specifike quhet *kohëzgjatja e jetës* (TTL). Nëse nuk caktohet, TTL-ja është si parazgjedhje 1 orë. Kostoja për ruajtjen në memorien specifike varet nga madhësia e kodit hyrës dhe për sa kohë dëshiron që të ruhen kodet.

Ky seksion supozon se ke instaluar një Gemini SDK (ose ke të instaluar curl) dhe se ke konfiguruar një çelës API, siç tregohet në
[Udhëzuesin e fillimit](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq).

### Gjenero përmbajtje duke përdorur një memorie specifike

### Python

Shembulli i mëposhtëm tregon se si të gjenerosh përmbajtje duke përdorur një udhëzim të sistemit në memorien specifike dhe një skedar video.

### Videot

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

model='models/gemini-3.8-flash'

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

### Skedarë PDF

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

model_name = "gemini-3.8-flash"
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

Shembulli i mëposhtëm tregon se si të gjenerosh përmbajtje duke përdorur një udhëzim të sistemit të ruajtur në memorien specifike
dhe një skedar teksti.

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

  const modelName = "gemini-3.8-flash";
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

Shembulli i mëposhtëm tregon se si të gjenerosh përmbajtje duke përdorur një memorie specifike.

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

    modelName := "gemini-3.8-flash"
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

### QETËSI

Shembulli i mëposhtëm tregon se si të krijosh një memorie specifike dhe më pas ta përdorësh atë për të gjeneruar përmbajtje.

### Videot

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.8-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
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

### Skedarë PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.8-flash"
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

### Listo memoriet specifike

Nuk është e mundur të marrësh ose të shikosh përmbajtjet e ruajtura në memorien specifike, por mund të marrësh metadata të memories specifike (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time` dhe `expire_time`).

### Python

Për të listuar metadatat për të gjitha memoriet e ngarkuara të përkohshme, përdor `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Për të marrë metadatat për një objekt të memories specifike, nëse e di emrin e tij, përdor `get`:

```
client.caches.get(name=name)
```

### JavaScript

Për të listuar metadatat për të gjitha memoriet e ngarkuara të përkohshme, përdor `GoogleGenAI.caches.list()`:

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

Shembulli i mëposhtëm liston të gjitha memoriet specifike.

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

Shembulli i mëposhtëm liston memoriet specifike duke përdorur një madhësi faqeje prej 2.

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

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### Përditëso një memorie specifike

Mund të caktosh një `ttl` ose `expire_time` të ri për një memorie specifike. Ndryshimi i çdo gjëje tjetër
në lidhje me memorien specifike nuk mbështetet.

### Python

Shembulli i mëposhtëm tregon se si të përditësosh `ttl` të një memorie specifike duke përdorur `client.caches.update()`.

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

Për të caktuar kohën e skadimit, ajo pranon ose një objekt `datetime` ose një varg datë-ore të formatuar në ISO (`dt.isoformat()`, si p.sh. `2025-01-27T16:02:36.473528+00:00`). Ora jote duhet të përfshijë një brez orar (`datetime.utcnow()` nuk bashkëngjit një brez orar, `datetime.now(datetime.timezone.utc)` bashkëngjit një brez orar).

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

Shembulli i mëposhtëm tregon se si të përditësosh `ttl` të një memorie specifike duke përdorur `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

Shembulli i mëposhtëm tregon se si të përditësosh `TTL` të një memorie specifike.

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

### QETËSI

Shembulli i mëposhtëm tregon se si të përditësosh `ttl` të një memorie specifike.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Fshi një memorie specifike

Shërbimi i ruajtjes në memorien specifike ofron një operacion fshirjeje për heqjen manuale të përmbajtjeve nga memoria specifike. Shembulli i mëposhtëm tregon se si të fshish një memorie specifike:

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

### QETËSI

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### Ruajtja e qartë në memorien specifike duke përdorur bibliotekën e OpenAI

Nëse po përdor një [bibliotekë të OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=sq), mund të aktivizosh
ruajtjen në memorien specifike duke përdorur karakteristikën `cached_content` në
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=sq#extra-body).

## Kur të përdorësh ruajtjen e qartë në memorien specifike

Ruajtja në memorien specifike e kontekstit është veçanërisht e përshtatshme për skenarët ku një kontekst fillestar i konsiderueshëm referohet në mënyrë të përsëritur nga kërkesa më të shkurtra. Ki parasysh të përdorësh
ruajtjen në memorien specifike për raste përdorimi si:

- Robotët e bisedës me [udhëzime të gjera të sistemit](https://ai.google.dev/gemini-api/docs/system-instructions?hl=sq)
- Analiza e përsëritur e skedarëve të gjatë të videove
- Kërkesa të përsëritura ndaj grupeve të mëdha të dokumenteve
- Analiza e shpeshtë e depos së kodeve ose rregullimi i defekteve

### Si e zvogëlon kostot ruajtja e përmbajtjeve të qarta në memorien specifike

Ruajtja në memorien specifike e kontekstit është një veçori me pagesë e projektuar për të zvogëluar koston. Faturimi bazohet në faktorët e mëposhtëm:

1. **Numri i tokenëve të memories specifike:** Numri i tokenëve të hyrjes të ruajtur në memorien specifike, të faturuar me një tarifë të
   reduktuar kur përfshihen në kërkesat e mëvonshme.
2. **Kohëzgjatja e ruajtjes:** Koha për të cilën ruhen kodet e ruajtura në memorien specifike (TTL),
   fakturohet bazuar në kohëzgjatjen TTL të numrit të kodeve të ruajtura në memorien specifike. Nuk ka kufij minimalë
   ose maksimalë për TTL-në.
3. **Faktorë të tjerë:** Zbatohen tarifa të tjera, si p.sh. për tokenat e hyrjes dhe daljes që nuk janë në memorien specifike.

Për detaje të përditësuara të çmimeve, referoju [faqes së çmimeve
të Gemini API](https://ai.google.dev/pricing?hl=sq). Për të mësuar se si të numërosh kodet, shiko [Udhëzuesin e kodeve](https://ai.google.dev/gemini-api/docs/tokens?hl=sq).

### Të tjera për t'u marrë parasysh

Ki parasysh konsideratat e mëposhtme kur përdor ruajtjen në memorien specifike të kontekstit:

- Numri *minimal* i kodeve hyrëse për ruajtjen e kontekstit në memorien specifike ndryshon sipas modelit. *Maksimumi*
  është i njëjtë me maksimumin për modelin e dhënë. (Për më shumë rreth numërimit të kodeve, shiko [Udhëzuesin e kodeve](https://ai.google.dev/gemini-api/docs/tokens?hl=sq)).
- Modeli nuk bën asnjë dallim midis kodeve të ruajtura në memorien specifike dhe kodeve të rregullta të hyrjes. Përmbajtja e ruajtur në memorien specifike është një prefiks për kërkesën.
- Nuk ka kufij të veçantë të normës ose përdorimit për ruajtjen në memorien specifike të kontekstit; zbatohen kufijtë standardë të normës për `GenerateContent` dhe kufijtë e kodeve përfshijnë kodet e ruajtura në memorien specifike.
- Numri i kodeve të ruajtura në memorien specifike kthehet në `usage_metadata` nga veprimet e krijimit, marrjes dhe listimit të shërbimit të memories specifike, si dhe në `GenerateContent` kur përdoret memoria specifike.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-09 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-09 UTC."],[],[]]
