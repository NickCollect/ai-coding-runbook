---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=tr
fetched_at: 2026-08-03T04:31:09.531045+00:00
title: "Ba\u011flam\u0131 \u00f6nbelle\u011fe alma \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Bağlamı önbelleğe alma

Tipik bir yapay zeka iş akışında, aynı giriş jetonlarını bir modele tekrar tekrar iletebilirsiniz. Gemini API iki farklı önbelleğe alma mekanizması sunar:

- Örtülü önbelleğe alma (Gemini 2.5 ve daha yeni modellerde otomatik olarak etkinleştirilir, maliyet tasarrufu garantisi yoktur)
- Açık önbelleğe alma (Çoğu modelde manuel olarak etkinleştirilebilir, maliyet tasarrufu garantisi)

Açık önbelleğe alma, maliyet tasarrufu sağlamak istediğiniz ancak geliştiricinin biraz daha fazla çalışması gereken durumlarda faydalıdır.

## Örtülü önbelleğe alma

Örtülü önbelleğe alma, tüm Gemini 2.5 ve daha yeni modeller için varsayılan olarak etkindir. İsteğiniz önbelleklere isabet ederse maliyet tasarruflarını otomatik olarak aktarırız. Bu özelliği etkinleştirmek için herhangi bir işlem yapmanız gerekmez. Bağlam önbelleğe alma için minimum giriş jetonu sayısı, her model için aşağıdaki tabloda listelenmiştir:

| Model | Minimum jeton sınırı |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro Önizlemesi | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Örtülü önbellek isabeti olasılığını artırmak için:

- Büyük ve yaygın içerikleri isteminizin başına eklemeyi deneyin.
- Kısa süre içinde benzer öneklere sahip istekler göndermeye çalışmak

Yanıt nesnesinin `usage_metadata` alanında, önbellek isabeti olan jetonların sayısını görebilirsiniz.

## Açık önbelleğe alma

Gemini API'nin açık önbelleğe alma özelliğini kullanarak bazı içerikleri modele bir kez iletebilir, giriş jetonlarını önbelleğe alabilir ve ardından sonraki istekler için önbelleğe alınmış jetonlara başvurabilirsiniz. Belirli hacimlerde, önbelleğe alınmış jetonları kullanmak, aynı jeton gövdesini tekrar tekrar iletmekten daha düşük maliyetlidir.

Bir dizi jetonu önbelleğe aldığınızda, jetonlar otomatik olarak silinmeden önce önbelleğin ne kadar süreyle var olmasını istediğinizi seçebilirsiniz. Bu önbelleğe alma süresine *geçerlilik süresi* (TTL) adı verilir. Ayarlanmazsa TTL varsayılan olarak 1 saat olur. Önbelleğe alma maliyeti, giriş jetonu boyutuna ve jetonların ne kadar süreyle kalıcı olmasını istediğinize bağlıdır.

Bu bölümde, bir Gemini SDK'sını yüklediğiniz (veya curl'ü yüklediğiniz) ve [Başlangıç kılavuzunda](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr) gösterildiği gibi bir API anahtarı yapılandırdığınız varsayılır.

### Önbelleği kullanarak içerik oluşturma

### Python

Aşağıdaki örnekte, önbelleğe alınmış bir sistem talimatı ve video dosyası kullanarak nasıl içerik oluşturulacağı gösterilmektedir.

### Videolar

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

### PDF'ler

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

Aşağıdaki örnekte, önbelleğe alınmış bir sistem talimatı ve bir metin dosyası kullanarak nasıl içerik oluşturulacağı gösterilmektedir.

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

Aşağıdaki örnekte, önbellek kullanarak nasıl içerik oluşturulacağı gösterilmektedir.

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

Aşağıdaki örnekte, nasıl önbellek oluşturulacağı ve ardından içerik oluşturmak için nasıl kullanılacağı gösterilmektedir.

### Videolar

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

### PDF'ler

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

### Önbellekleri listeleme

Önbelleğe alınmış içerikleri almak veya görüntülemek mümkün değildir ancak önbellek meta verilerini (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time` ve `expire_time`) alabilirsiniz.

### Python

Yüklenen tüm önbelleklerin meta verilerini listelemek için `CachedContent.list()` kullanın:

```
for cache in client.caches.list():
  print(cache)
```

Adını biliyorsanız bir önbellek nesnesinin meta verilerini getirmek için `get` kullanın:

```
client.caches.get(name=name)
```

### JavaScript

Yüklenen tüm önbelleklerin meta verilerini listelemek için `GoogleGenAI.caches.list()` kullanın:

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

Aşağıdaki örnekte tüm önbellekler listelenmektedir.

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

Aşağıdaki örnekte, sayfa boyutu 2 olan önbellekler listelenmektedir.

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

### Önbelleği güncelleme

Önbellek için yeni bir `ttl` veya `expire_time` ayarlayabilirsiniz. Önbellekle ilgili başka bir şeyin değiştirilmesi desteklenmez.

### Python

Aşağıdaki örnekte, `client.caches.update()` kullanılarak bir önbelleğin `ttl` değerinin nasıl güncelleneceği gösterilmektedir.

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

Süre sonunu ayarlamak için `datetime` nesnesi veya ISO biçimli bir tarih/saat dizesi (`dt.isoformat()`, örneğin `2025-01-27T16:02:36.473528+00:00`) kabul edilir. Zamanınız bir saat dilimi içermelidir (`datetime.utcnow()` saat dilimi eklemez, `datetime.now(datetime.timezone.utc)` saat dilimi ekler).

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

Aşağıdaki örnekte, `GoogleGenAI.caches.update()` kullanılarak bir önbelleğin `ttl` değerinin nasıl güncelleneceği gösterilmektedir.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

Aşağıdaki örnekte, bir önbelleğin `TTL` değerinin nasıl güncelleneceği gösterilmektedir.

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

Aşağıdaki örnekte, bir önbelleğin `ttl` değerinin nasıl güncelleneceği gösterilmektedir.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Önbelleği silme

Önbelleğe alma hizmeti, içeriği önbellekten manuel olarak kaldırmak için silme işlemi sağlar. Aşağıdaki örnekte önbelleğin nasıl silineceği gösterilmektedir:

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

### OpenAI kitaplığını kullanarak açık önbelleğe alma

[OpenAI kitaplığı](https://ai.google.dev/gemini-api/docs/openai?hl=tr) kullanıyorsanız [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=tr#extra-body) üzerinde `cached_content` özelliğini kullanarak açık önbelleğe almayı etkinleştirebilirsiniz.

## Açık önbelleğe alma ne zaman kullanılır?

Bağlamı önbelleğe alma, özellikle önemli bir ilk bağlamın daha kısa istekler tarafından tekrar tekrar referans alındığı senaryolar için uygundur. Aşağıdaki gibi kullanım alanlarında bağlamı önbelleğe alma özelliğini kullanabilirsiniz:

- Kapsamlı [sistem talimatlarına](https://ai.google.dev/gemini-api/docs/system-instructions?hl=tr) sahip chatbot'lar
- Uzun video dosyalarının tekrar tekrar analiz edilmesi
- Büyük doküman kümelerine karşı yinelenen sorgular
- Sık kod deposu analizi veya hata düzeltme

### Açıkça önbelleğe alma, maliyetleri nasıl azaltır?

Bağlam önbelleğe alma, maliyeti düşürmek için tasarlanmış ücretli bir özelliktir. Faturalandırma aşağıdaki faktörlere göre yapılır:

1. **Önbelleğe alınan jeton sayısı:** Giriş jetonlarının sayısı önbelleğe alınır ve sonraki istemlere dahil edildiğinde daha düşük bir ücretle faturalandırılır.
2. **Depolama süresi:** Önbelleğe alınan jetonların depolandığı süre (TTL). Önbelleğe alınan jeton sayısının TTL süresine göre faturalandırılır. TTL için minimum veya maksimum sınır yoktur.
3. **Diğer faktörler:** Giriş ve çıkış jetonları gibi önbelleğe alınmamış jetonlar için diğer ücretler geçerlidir.

En güncel fiyatlandırma bilgileri için Gemini API [fiyatlandırma sayfasını](https://ai.google.dev/pricing?hl=tr) inceleyin. Jetonları nasıl sayacağınızı öğrenmek için [Jeton kılavuzuna](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) bakın.

### Göz önünde bulundurulacak diğer noktalar

Bağlam önbelleğe almayı kullanırken aşağıdaki hususları göz önünde bulundurun:

- Bağlam önbelleğe alma için *minimum* giriş jetonu sayısı modele göre değişir. *Maksimum*, belirli model için maksimum değerle aynıdır. (Jeton sayma hakkında daha fazla bilgi için [Jeton kılavuzu](https://ai.google.dev/gemini-api/docs/tokens?hl=tr)'na bakın).
- Model, önbelleğe alınmış jetonlar ile normal giriş jetonları arasında herhangi bir ayrım yapmaz. Önbelleğe alınmış içerik, istemin önekidir.
- Bağlam önbelleğe alma konusunda özel bir oran veya kullanım sınırı yoktur. `GenerateContent` için standart oran sınırları geçerlidir ve jeton sınırlarına önbelleğe alınmış jetonlar da dahildir.
- Önbelleğe alınan jeton sayısı, önbellek hizmetinin oluşturma, alma ve listeleme işlemlerinden `usage_metadata` içinde, önbellek kullanılırken de `GenerateContent` içinde döndürülür.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
