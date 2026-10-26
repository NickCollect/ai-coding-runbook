---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=fa
fetched_at: 2026-10-26T05:59:29.014021+00:00
title: "\u0630\u062e\u06cc\u0631\u0647 \u06a9\u0631\u062f\u0646 \u0628\u0627\u0641\u062a \u062f\u0631 \u062d\u0627\u0641\u0638\u0647 \u0646\u0647\u0627\u0646 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# ذخیره کردن بافت در حافظه نهان

در یک گردش کار معمول هوش مصنوعی، ممکن است بارها و بارها همان کدهای ورودی را به یک مدل ارسال کنید. ‫Gemini API دو سازوکار ذخیره‌سازی موقت متفاوت ارائه می‌دهد:

- ذخیره ضمنی در حافظه نهان (به‌طور خودکار در Gemini 2.5 و مدل‌های جدیدتر فعال می‌شود، تضمینی برای صرفه‌جویی در هزینه وجود ندارد)
- ذخیره صریح در حافظه نهان (می‌تواند به‌صورت دستی در مدل‌های Gemini 3 و 2.5 فعال شود، تضمین صرفه‌جویی در هزینه؛ برای Gemini 4 Argon و نسخه‌های بعدی پشتیبانی نمی‌شود)

ذخیره‌سازی صریح در مواردی مفید است که می‌خواهید صرفه‌جویی در هزینه را تضمین کنید،
اما با کمی کار توسعه‌دهنده اضافی.

## ذخیره در حافظه نهان ضمنی

ذخیره‌سازی ضمنی در حافظه نهان به‌طور پیش‌فرض برای همه مدل‌های Gemini 2.5 و جدیدتر فعال است. اگر درخواستتان به حافظه‌های پنهان برسد،
ما به‌طور خودکار صرفه‌جویی در هزینه را منتقل می‌کنیم. برای روشن کردن آن نیازی به پیکربندی چیزی ندارید. جدول زیر حداقل تعداد داده‌واحد ورودی را برای هر مدل فهرست می‌کند:

| مدل | حداقل حد توکن |
| --- | --- |
| Gemini 4 Argon | ۴٬۰۹۶ |
| Gemini 3.8 Flash | ۴٬۰۹۶ |
| Gemini 3.6 Flash | ۴٬۰۹۶ |
| Gemini 3.1 Pro Preview | ۴٬۰۹۶ |
| ‫Gemini 2.5 Flash | ۲۰۴۸ |
| ‫Gemini 2.5 Pro | ۲۰۴۸ |

برای افزایش احتمال اصابت حافظه نهان ضمنی:

- سعی کنید محتوای بزرگ و رایج را در ابتدای پیام‌واره‌تان قرار دهید
- سعی کنید درخواست‌های دارای پیشوند مشابه را در مدت زمان کوتاهی ارسال کنید

می‌توانید تعداد کدهای استفاده‌شده‌ای را که در فیلد `usage_metadata` شیء پاسخ، بازدیدهای حافظه نهان بوده‌اند ببینید.

## ذخیره صریح در حافظه نهان

بااستفاده از ویژگی ذخیره‌سازی صریح در حافظه نهان Gemini API، می‌توانید یک‌بار محتوایی را به مدل ارسال کنید،
نمانه‌های ورودی را در حافظه نهان ذخیره کنید، و سپس برای درخواست‌های بعدی به نمانه‌های ذخیره‌شده در حافظه نهان ارجاع دهید. در حجم‌های خاص، استفاده از نشانه‌های ذخیره‌شده در حافظه نهان هزینه کمتری دارد
تا اینکه همان مجموعه نشانه‌ها را به‌طور مکرر ارسال کنید.

وقتی مجموعه‌ای از نشان‌ها را ذخیره می‌کنید، می‌توانید انتخاب کنید که حافظه پنهان چه مدت وجود داشته باشد تا نشان‌ها به‌طور خودکار حذف شوند. به این مدت‌زمان ذخیره در حافظه نهان،
*زمان بقا* (TTL) می‌گویند. اگر تنظیم نشده باشد، TTL به‌طور پیش‌فرض روی ۱ ساعت تنظیم می‌شود. هزینه ذخیره‌سازی موقت به اندازه توکن ورودی و مدت زمانی که می‌خواهید توکن‌ها باقی بمانند بستگی دارد.

این بخش فرض می‌کند که شما یک Gemini SDK را نصب کرده‌اید (یا curl نصب شده است)
و یک کلید API را پیکربندی کرده‌اید، همان‌طور که در
[راهنمای شروع به کار](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa) نشان داده شده است.

### تولید محتوا بااستفاده از حافظه نهان

### Python

مثال زیر نحوه تولید محتوا بااستفاده از دستورالعمل سیستم ذخیره‌شده در حافظه نهان و فایل ویدیویی را نشان می‌دهد.

### ویدیوها

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

### فایل‌های پی‌دی‌اف

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

مثال زیر نحوه تولید محتوا بااستفاده از دستورالعمل سیستم ذخیره‌شده در حافظه نهان و فایل نوشتاری را نشان می‌دهد.

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

### رفتن

مثال زیر نحوه تولید محتوا بااستفاده از حافظه نهان را نشان می‌دهد.

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

### استراحت

مثال زیر نحوه ایجاد حافظه پنهان و سپس استفاده از آن برای تولید محتوا را نشان می‌دهد.

### ویدیوها

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

### فایل‌های پی‌دی‌اف

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

### فهرست کردن حافظه‌های نهان

بازیابی یا مشاهده محتوای ذخیره‌شده در حافظه نهان امکان‌پذیر نیست، اما می‌توانید
فراداده حافظه نهان (`name`، `model`، `display_name`، `usage_metadata`،
`create_time`، `update_time`، و `expire_time`) را بازیابی کنید.

### Python

برای فهرست کردن فراداده‌های همه حافظه‌های پنهان بارگذاری‌شده، از `CachedContent.list()` استفاده کنید:

```
for cache in client.caches.list():
  print(cache)
```

برای واکشی فراداده یک شیء حافظه پنهان، اگر نام آن را می‌دانید، از `get` استفاده کنید:

```
client.caches.get(name=name)
```

### JavaScript

برای فهرست کردن فراداده‌های همه حافظه‌های پنهان بارگذاری‌شده، از `GoogleGenAI.caches.list()` استفاده کنید:

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

### رفتن

مثال زیر همه حافظه‌های پنهان را فهرست می‌کند.

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

مثال زیر حافظه‌های پنهان را بااستفاده از اندازه صفحه ۲ فهرست می‌کند.

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

### استراحت

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### به‌روزرسانی حافظه نهان

می‌توانید `ttl` یا `expire_time` جدیدی برای حافظه نهان تنظیم کنید. تغییر دادن چیز دیگری
درباره حافظه پنهان پشتیبانی نمی‌شود.

### Python

مثال زیر نحوه به‌روزرسانی `ttl` حافظه نهان را بااستفاده از
`client.caches.update()` نشان می‌دهد.

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

برای تنظیم زمان انقضا، یا شیء `datetime`
یا رشته تاریخ و زمان با قالب ISO (`dt.isoformat()`، مانند
`2025-01-27T16:02:36.473528+00:00`) را می‌پذیرد. زمان شما باید شامل منطقه زمانی باشد
(`datetime.utcnow()` منطقه زمانی را پیوست نمی‌کند،
`datetime.now(datetime.timezone.utc)` منطقه زمانی را پیوست می‌کند).

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

مثال زیر نحوه به‌روزرسانی `ttl` حافظه نهان را بااستفاده از
`GoogleGenAI.caches.update()` نشان می‌دهد.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### رفتن

مثال زیر نحوه به‌روزرسانی `TTL` حافظه نهان را نشان می‌دهد.

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

### استراحت

مثال زیر نحوه به‌روزرسانی `ttl` حافظه نهان را نشان می‌دهد.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### حذف حافظه نهان

سرویس ذخیره‌سازی موقت عملیات حذفی را برای برداشتن دستی محتوا از حافظه پنهان ارائه می‌دهد. مثال زیر نحوه حذف حافظه نهان را نشان می‌دهد:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### رفتن

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### استراحت

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### ذخیره صریح در حافظه نهان بااستفاده از کتابخانه OpenAI

اگر از [کتابخانه OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fa) استفاده می‌کنید، می‌توانید
ذخیره صریح در حافظه نهان را بااستفاده از ویژگی `cached_content` در
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=fa#extra-body) فعال کنید.

## چه زمانی از ذخیره‌سازی صریح در حافظه نهان استفاده کنیم

ذخیره کردن بافت در حافظه نهان به‌ویژه برای سناریوهایی مناسب است که در آن‌ها یک بافت اولیه قابل‌توجه به‌طور مکرر توسط درخواست‌های کوتاه‌تر ارجاع داده می‌شود. برای موارد استفاده‌ای مثل موارد زیر،
استفاده از حافظه نهان بافت را درنظر بگیرید:

- روبات‌های گپ با [دستورالعمل‌های سیستم](https://ai.google.dev/gemini-api/docs/system-instructions?hl=fa) گسترده
- تجزیه‌وتحلیل تکراری فایل‌های ویدیویی طولانی
- پرسمان‌های تکرارشونده درمقابل مجموعه‌های بزرگ اسناد
- تجزیه‌وتحلیل مکرر مخزن کد یا رفع اشکال

### چگونه ذخیره‌سازی صریح در حافظه نهان هزینه‌ها را کاهش می‌دهد

ذخیره‌سازی بافت در حافظه نهان ویژگی پولی‌ای است که برای کاهش هزینه طراحی شده است. صدور صورت‌حساب براساس
عوامل زیر است:

1. **تعداد داده‌واحد ذخیره‌شده در حافظه نهان:** تعداد داده‌واحدهای ورودی ذخیره‌شده در حافظه نهان که درصورت گنجانده شدن در پیام‌واره‌های بعدی، با نرخ کاهش‌یافته صورت‌حساب می‌شود.
2. **مدت ذخیره‌سازی:** مدت زمانی که کدهای ذخیره‌شده در حافظه نهان ذخیره می‌شوند (TTL)،
   که براساس مدت TTL تعداد کدهای ذخیره‌شده در حافظه نهان صورت‌حساب می‌شود. هیچ حد کمینه یا بیشینه‌ای برای TTL وجود ندارد.
3. **عوامل دیگر:** هزینه‌های دیگری اعمال می‌شود، مثلاً برای کدهای ورودی غیرذخیره‌شده در حافظه نهان و کدهای خروجی.

برای جزئیات به‌روز قیمت‌گذاری، به [صفحه قیمت‌گذاری](https://ai.google.dev/pricing?hl=fa) Gemini API مراجعه کنید. برای آشنایی با نحوه شمارش نشانه‌ها، به [راهنمای
نشانه](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) مراجعه کنید.

### سایر ملاحظات

هنگام استفاده از ذخیره‌سازی بافت در حافظه نهان، ملاحظات زیر را درنظر داشته باشید:

- *حداقل* تعداد داده‌واحد ورودی برای ذخیره‌سازی موقت بافت بسته به مدل متفاوت است. *حداکثر*
  همان حداکثر برای مدل داده‌شده است. (برای اطلاعات بیشتر درباره شمارش نشانه‌ها،
  [راهنمای نشانه](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) را ببینید).
- مدل هیچ تفاوتی بین نشان‌های ذخیره‌شده در حافظه نهان و نشان‌های ورودی معمولی قائل نمی‌شود. محتوای ذخیره‌شده در حافظه نهان پیشوندی برای پیام‌واره است.
- هیچ حد نرخ یا حد استفاده خاصی برای ذخیره‌سازی موقت بافت وجود ندارد؛ حد نرخ استاندارد برای `GenerateContent` اعمال می‌شود و حد نشان شامل نشان‌های ذخیره‌شده موقت می‌شود.
- تعداد نشان‌های ذخیره‌شده در حافظه نهان در `usage_metadata` از
  عملیات ایجاد، دریافت، و فهرست کردن سرویس حافظه نهان، و همچنین در
  `GenerateContent` هنگام استفاده از حافظه نهان برگردانده می‌شود.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-23 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-23 به‌وقت ساعت هماهنگ جهانی."],[],[]]
