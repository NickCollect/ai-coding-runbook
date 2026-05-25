---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=id
fetched_at: 2026-05-25T05:20:47.775534+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Context caching

Dalam alur kerja AI yang umum, Anda mungkin meneruskan token input yang sama berulang kali ke model. Gemini API menawarkan dua mekanisme caching yang berbeda:

- Caching implisit (diaktifkan secara otomatis di Gemini 2.5 dan model yang lebih baru, tanpa jaminan penghematan biaya)
- Caching eksplisit (dapat diaktifkan secara manual di sebagian besar model, dengan jaminan penghematan biaya)

Caching eksplisit berguna jika Anda ingin menjamin penghematan biaya, tetapi dengan beberapa pekerjaan developer tambahan.

## Caching implisit

Caching implisit diaktifkan secara default untuk semua model Gemini 2.5 dan yang lebih baru. Kami otomatis meneruskan penghematan biaya jika permintaan Anda cocok dengan cache. Anda tidak perlu melakukan apa pun untuk mengaktifkan fitur ini. Jumlah token input minimum untuk context caching tercantum dalam tabel berikut untuk setiap model:

| Model | Batas token minimum |
| --- | --- |
| Gemini 3.5 Flash | 1024 |
| Gemini 3 Pro Preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

Untuk meningkatkan peluang kecocokan cache implisit:

- Coba tempatkan konten besar dan umum di awal perintah Anda
- Coba kirim permintaan dengan awalan yang serupa dalam waktu singkat

Anda dapat melihat jumlah token yang cocok dengan cache di kolom `usage_metadata` objek respons.

## Caching eksplisit

Dengan menggunakan fitur caching eksplisit Gemini API, Anda dapat meneruskan beberapa konten ke model sekali, menyimpan token input ke cache, lalu merujuk ke token yang di-cache untuk permintaan berikutnya. Pada volume tertentu, penggunaan token yang di-cache lebih murah daripada meneruskan korpus token yang sama berulang kali.

Saat menyimpan kumpulan token ke cache, Anda dapat memilih berapa lama cache akan ada sebelum token dihapus secara otomatis. Durasi caching ini disebut *time to live* (TTL). Jika tidak disetel, TTL akan ditetapkan secara default ke 1 jam. Biaya untuk caching bergantung pada ukuran token input dan berapa lama Anda ingin token tetap ada.

Bagian ini mengasumsikan bahwa Anda telah menginstal Gemini SDK (atau telah menginstal curl)
dan bahwa Anda telah mengonfigurasi kunci API, seperti yang ditunjukkan dalam
[panduan memulai](https://ai.google.dev/gemini-api/docs/quickstart?hl=id).

### Membuat konten menggunakan cache

### Python

Contoh berikut menunjukkan cara membuat konten menggunakan petunjuk sistem dan file video yang di-cache.

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

Contoh berikut menunjukkan cara membuat konten menggunakan petunjuk sistem dan file teks yang di-cache.

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

### Go

Contoh berikut menunjukkan cara membuat konten menggunakan cache.

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

Contoh berikut menunjukkan cara membuat cache, lalu menggunakannya untuk membuat konten.

### Video

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

### PDF

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

### Mencantumkan cache

Anda tidak dapat mengambil atau melihat konten yang di-cache, tetapi Anda dapat mengambil
metadata cache (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time`, dan `expire_time`).

### Python

Untuk mencantumkan metadata untuk semua cache yang diupload, gunakan `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Untuk mengambil metadata untuk satu objek cache, jika Anda mengetahui namanya, gunakan `get`:

```
client.caches.get(name=name)
```

### JavaScript

Untuk mencantumkan metadata untuk semua cache yang diupload, gunakan `GoogleGenAI.caches.list()`:

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

Contoh berikut mencantumkan semua cache.

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

Contoh berikut mencantumkan cache menggunakan ukuran halaman 2.

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

### Memperbarui cache

Anda dapat menetapkan `ttl` atau `expire_time` baru untuk cache. Perubahan pada hal lain terkait cache tidak didukung.

### Python

Contoh berikut menunjukkan cara memperbarui `ttl` cache menggunakan `client.caches.update()`.

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

Untuk menetapkan waktu habis masa berlaku, Anda dapat menerima objek `datetime`
atau string datetime berformat ISO (`dt.isoformat()`, seperti
`2025-01-27T16:02:36.473528+00:00`). Waktu Anda harus menyertakan zona waktu
(`datetime.utcnow()` tidak melampirkan zona waktu,
`datetime.now(datetime.timezone.utc)` melampirkan zona waktu).

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

Contoh berikut menunjukkan cara memperbarui `ttl` cache menggunakan `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

Contoh berikut menunjukkan cara memperbarui `TTL` cache.

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

Contoh berikut menunjukkan cara memperbarui `ttl` cache.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Menghapus cache

Layanan caching menyediakan operasi penghapusan untuk menghapus konten dari cache secara manual. Contoh berikut menunjukkan cara menghapus cache:

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

### Caching eksplisit menggunakan library OpenAI

Jika menggunakan [library OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id), Anda dapat mengaktifkan
caching eksplisit menggunakan properti `cached_content` di
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=id#extra-body).

## Kapan harus menggunakan caching eksplisit

Context caching sangat cocok untuk skenario saat konteks awal yang substansial dirujuk berulang kali oleh permintaan yang lebih singkat. Pertimbangkan untuk menggunakan context caching untuk kasus penggunaan seperti:

- Chatbot dengan petunjuk [sistem](https://ai.google.dev/gemini-api/docs/system-instructions?hl=id) yang ekstensif
- Analisis berulang pada file video yang panjang
- Kueri berulang terhadap kumpulan dokumen besar
- Analisis repositori kode atau perbaikan bug yang sering dilakukan

### Cara caching eksplisit mengurangi biaya

Context caching adalah fitur berbayar yang dirancang untuk mengurangi biaya. Penagihan didasarkan pada faktor-faktor berikut:

1. **Jumlah token cache:** Jumlah token input yang di-cache, ditagih dengan tarif yang lebih rendah jika disertakan dalam perintah berikutnya.
2. **Durasi penyimpanan:** Jumlah waktu token yang di-cache disimpan (TTL), ditagih berdasarkan durasi TTL jumlah token yang di-cache. Tidak ada batas minimum atau maksimum pada TTL.
3. **Faktor lainnya:** Biaya lain berlaku, seperti untuk token input dan token output yang tidak di-cache.

Untuk mengetahui detail harga terbaru, lihat halaman harga Gemini API [pricing
page](https://ai.google.dev/pricing?hl=id). Untuk mempelajari cara menghitung token, lihat [Panduan
token](https://ai.google.dev/gemini-api/docs/tokens?hl=id).

### Pertimbangan tambahan

Perhatikan pertimbangan berikut saat menggunakan context caching:

- Jumlah token input *minimum* untuk context caching bervariasi menurut model. Jumlah *maksimum* sama dengan jumlah maksimum untuk model tertentu. (Untuk mengetahui informasi selengkapnya tentang cara menghitung token,
  lihat [Panduan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id)).
- Model tidak membedakan antara token yang di-cache dan token input reguler. Konten yang di-cache adalah awalan untuk perintah.
- Tidak ada batasan tarif atau penggunaan khusus untuk context caching; batasan tarif standar untuk `GenerateContent` berlaku, dan batas token mencakup token yang di-cache.
- Jumlah token yang di-cache ditampilkan di `usage_metadata` dari operasi pembuatan, pengambilan, dan pencantuman layanan cache, serta di `GenerateContent` saat menggunakan cache.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
