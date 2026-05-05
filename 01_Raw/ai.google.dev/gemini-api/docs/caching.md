---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ar
fetched_at: 2026-05-05T19:49:34.629460+00:00
title: "\u0627\u0644\u062a\u062e\u0632\u064a\u0646 \u0627\u0644\u0645\u0624\u0642\u062a \u0644\u0644\u0633\u064a\u0627\u0642 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التخزين المؤقت للسياق

في سير عمل الذكاء الاصطناعي العادي، قد يتم تمرير الرموز المميزة نفسها بشكل متكرر إلى أحد النماذج. توفّر Gemini API آليتَين مختلفتَين للتخزين المؤقت:

- التخزين المؤقت الضمني (مفعّل تلقائيًا في Gemini 2.5 والإصدارات الأحدث، ولا نضمن تحقيق أي توفير في التكلفة)
- التخزين المؤقت الصريح (يمكن تفعيله يدويًا على معظم النماذج، وضمان توفير التكلفة)

تكون ميزة التخزين المؤقت الواضح مفيدة في الحالات التي تريد فيها ضمان توفير التكاليف، ولكن مع بعض العمل الإضافي من المطوّر.

## التخزين المؤقت الضمني

يتم تفعيل التخزين المؤقت الضمني تلقائيًا لجميع نماذج Gemini 2.5 والإصدارات الأحدث. ننقل إليك تلقائيًا أي توفير في التكاليف إذا وصل طلبك إلى ذاكرات التخزين المؤقت. ليس عليك اتّخاذ أي إجراء لتفعيل هذه الميزة. يتم إدراج الحد الأدنى لعدد الرموز المميزة للإدخال المطلوب لتفعيل التخزين المؤقت للسياق في الجدول التالي لكل نموذج:

| الطراز | الحدّ الأدنى لعدد الرموز المميّزة |
| --- | --- |
| معاينة Gemini 3 Flash | 1024 |
| معاينة Gemini 3 Pro | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

لزيادة فرصة تحقيق نتيجة ذاكرة التخزين المؤقت الضمنية، اتّبِع الخطوات التالية:

- جرِّب وضع المحتوى الكبير والشائع في بداية طلبك
- محاولة إرسال طلبات تتضمّن بادئة مشابهة في فترة زمنية قصيرة

يمكنك الاطّلاع على عدد الرموز المميزة التي تم العثور عليها في ذاكرة التخزين المؤقت ضمن الحقل `usage_metadata` في عنصر الاستجابة.

## التخزين المؤقت الصريح

باستخدام ميزة التخزين المؤقت الصريح في Gemini API، يمكنك تمرير بعض المحتوى إلى النموذج مرة واحدة، وتخزين الرموز المميزة للإدخال مؤقتًا، ثم الرجوع إلى الرموز المميزة المخزّنة مؤقتًا للطلبات اللاحقة. عند استخدام عدد كبير من الرموز المميزة، تكون تكلفة استخدام الرموز المميزة المخزّنة مؤقتًا أقل من تكلفة تمرير مجموعة الرموز المميزة نفسها بشكل متكرر.

عند تخزين مجموعة من الرموز المميزة مؤقتًا، يمكنك اختيار المدة التي تريد أن يستمر فيها التخزين المؤقت قبل حذف الرموز المميزة تلقائيًا. تُعرف مدة التخزين المؤقت هذه باسم *مدة البقاء* (TTL). إذا لم يتم ضبطها، تكون مدة البقاء التلقائية ساعة واحدة. تعتمد تكلفة التخزين المؤقت على حجم الرموز المميزة للإدخال ومدة الاحتفاظ بها.

يفترض هذا القسم أنّك ثبّت حزمة تطوير برامج (SDK) خاصة بـ Gemini (أو ثبّت curl)
وأنّك أعددت مفتاح واجهة برمجة تطبيقات، كما هو موضّح في
[دليل البدء السريع](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).

### إنشاء محتوى باستخدام ذاكرة تخزين مؤقت

### Python

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام تعليمات نظام مخزّنة مؤقتًا وملف فيديو.

### الفيديوهات

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

### ملفات PDF

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

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام تعليمات نظام مخزّنة مؤقتًا وملف نصي.

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

### Go

يوضّح المثال التالي كيفية إنشاء محتوى باستخدام ذاكرة تخزين مؤقت.

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

يوضّح المثال التالي كيفية إنشاء ذاكرة تخزين مؤقت ثم استخدامها لإنشاء محتوى.

### الفيديوهات

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

### ملفات PDF

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

### سرد ذاكرات التخزين المؤقت

لا يمكن استرداد المحتوى المخزّن مؤقتًا أو عرضه، ولكن يمكنك استرداد البيانات الوصفية للمحتوى المخزّن مؤقتًا (`name` و`model` و`display_name` و`usage_metadata` و`create_time` و`update_time` و`expire_time`).

### Python

لعرض البيانات الوصفية لجميع الذاكرات المؤقتة التي تم تحميلها، استخدِم `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

لاسترداد البيانات الوصفية لعنصر واحد من ذاكرة التخزين المؤقت، إذا كنت تعرف اسمه، استخدِم `get`:

```
client.caches.get(name=name)
```

### JavaScript

لعرض البيانات الوصفية لجميع الذاكرات المؤقتة التي تم تحميلها، استخدِم `GoogleGenAI.caches.list()`:

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

يعرض المثال التالي جميع الذاكرات المؤقتة.

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

يعرض المثال التالي قوائم ذاكرة التخزين المؤقت باستخدام حجم صفحة يبلغ 2.

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

### تعديل ذاكرة تخزين مؤقت

يمكنك ضبط قيمة جديدة `ttl` أو `expire_time` لذاكرة تخزين مؤقت. لا يمكن تغيير أي شيء آخر في ذاكرة التخزين المؤقت.

### Python

يوضّح المثال التالي كيفية تعديل `ttl` لذاكرة تخزين مؤقت باستخدام `client.caches.update()`.

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

لتحديد وقت انتهاء الصلاحية، سيتم قبول إما عنصر `datetime` أو سلسلة بتنسيق ISO للتاريخ والوقت (`dt.isoformat()`، مثل `2025-01-27T16:02:36.473528+00:00`). يجب أن يتضمّن الوقت منطقة زمنية (لا يرفق `datetime.utcnow()` منطقة زمنية، بينما يرفق `datetime.now(datetime.timezone.utc)` منطقة زمنية).

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

يوضّح المثال التالي كيفية تعديل `ttl` لذاكرة تخزين مؤقت باستخدام `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

يوضّح المثال التالي كيفية تعديل `TTL` ذاكرة تخزين مؤقت.

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

يوضّح المثال التالي كيفية تعديل `ttl` ذاكرة تخزين مؤقت.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### حذف ذاكرة تخزين مؤقت

توفّر خدمة التخزين المؤقت عملية حذف لإزالة المحتوى يدويًا من ذاكرة التخزين المؤقت. يوضّح المثال التالي كيفية حذف ذاكرة تخزين مؤقت:

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

### التخزين المؤقت الصريح باستخدام مكتبة OpenAI

إذا كنت تستخدم [مكتبة OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)، يمكنك تفعيل التخزين المؤقت الصريح باستخدام السمة `cached_content` في [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=ar#extra-body).

## حالات استخدام التخزين المؤقّت الواضح

تكون ميزة التخزين المؤقت للسياق مناسبة بشكل خاص للحالات التي تتم فيها الإشارة بشكل متكرر إلى سياق أولي كبير من خلال طلبات أقصر. يمكنك استخدام التخزين المؤقت للسياق في حالات الاستخدام التالية:

- روبوتات الدردشة التي تتضمّن [تعليمات نظام](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ar) شاملة
- التحليل المتكرّر لملفات الفيديو الطويلة
- الاستعلامات المتكرّرة عن مجموعات كبيرة من المستندات
- تحليل مستودع الرموز البرمجية أو إصلاح الأخطاء بشكل متكرّر

### كيفية تقليل التكاليف باستخدام التخزين المؤقت الصريح

تخزين السياق مؤقتًا هو ميزة مدفوعة مصمَّمة لخفض التكلفة. تستند الفوترة إلى العوامل التالية:

1. **عدد الرموز المميزة المخزّنة مؤقتًا:** عدد الرموز المميزة للإدخال المخزّنة مؤقتًا، والتي يتم تحصيل رسومها بمعدّل مخفَّض عند تضمينها في الطلبات اللاحقة.
2. **مدة التخزين:** هي المدة التي يتم فيها تخزين الرموز المميّزة المخزَّنة مؤقتًا (مدة البقاء)،
   ويتم تحصيل الرسوم استنادًا إلى مدة البقاء لعدد الرموز المميّزة المخزَّنة مؤقتًا. ليس هناك حد أدنى أو أقصى لقيمة TTL.
3. **عوامل أخرى:** تنطبق رسوم أخرى، مثل رسوم الرموز المميزة للإدخال غير المخزّنة مؤقتًا
   والرموز المميزة للإخراج.

للاطّلاع على تفاصيل الأسعار الحديثة، يُرجى الرجوع إلى [صفحة الأسعار](https://ai.google.dev/pricing?hl=ar) الخاصة بواجهة Gemini API. للتعرّف على كيفية احتساب الرموز المميزة، اطّلِع على [دليل الرموز المميزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

### اعتبارات أخرى

يجب مراعاة ما يلي عند استخدام التخزين المؤقت للسياق:

- يختلف *الحد الأدنى* لعدد الرموز المميزة للإدخال في التخزين المؤقت للسياق حسب النموذج. *الحدّ الأقصى*
  هو الحدّ الأقصى للنموذج المحدّد. (لمزيد من المعلومات حول احتساب الرموز المميزة، اطّلِع على [دليل الرموز المميزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar)).
- لا يميّز النموذج بين الرموز المميزة المخزّنة مؤقتًا والرموز المميزة العادية للإدخال. المحتوى المخزّن مؤقتًا هو بادئة للطلب.
- لا توجد حدود خاصة على معدّل الاستخدام أو عدد مرات الاستخدام في ما يتعلق بالتخزين المؤقت للسياق، بل تنطبق حدود المعدّل العادية الخاصة بـ `GenerateContent`، وتشمل حدود الرموز المميزة الرموز المميزة المخزّنة مؤقتًا.
- يتم عرض عدد الرموز المميزة المخزّنة مؤقتًا في `usage_metadata` من عمليات الإنشاء والحصول على البيانات وعرض القائمة في خدمة التخزين المؤقت، وكذلك في `GenerateContent` عند استخدام التخزين المؤقت.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
