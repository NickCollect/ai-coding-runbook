---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=th
fetched_at: 2026-08-10T03:11:09.674716+00:00
title: "\u0e01\u0e32\u0e23\u0e41\u0e04\u0e0a\u0e1a\u0e23\u0e34\u0e1a\u0e17 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การแคชบริบท

ในเวิร์กโฟลว์ AI ทั่วไป คุณอาจส่งโทเค็นอินพุตเดียวกันซ้ำๆ ไปยังโมเดล Gemini API มีกลไกการแคช 2 แบบดังนี้

- การแคชแบบไม่เจาะจง (เปิดใช้โดยอัตโนมัติในโมเดล Gemini 2.5 และใหม่กว่า ไม่รับประกันการประหยัดค่าใช้จ่าย)
- การแคชแบบเจาะจง (เปิดใช้ด้วยตนเองในโมเดลส่วนใหญ่ได้ รับประกันการประหยัดค่าใช้จ่าย)

การแคชแบบเจาะจงมีประโยชน์ในกรณีที่คุณต้องการรับประกันการประหยัดค่าใช้จ่าย แต่ต้องมีงานเพิ่มเติมสำหรับนักพัฒนาแอป

## การแคชแบบไม่เจาะจง

การแคชแบบไม่เจาะจงจะเปิดใช้โดยค่าเริ่มต้นสำหรับโมเดล Gemini 2.5 และใหม่กว่าทั้งหมด เราจะส่งต่อการประหยัดค่าใช้จ่ายโดยอัตโนมัติหากคำขอของคุณตรงกับแคช คุณไม่จำเป็นต้องดำเนินการใดๆ เพื่อเปิดใช้ฟีเจอร์นี้ จำนวนโทเค็นอินพุตขั้นต่ำสำหรับการแคชบริบทแสดงอยู่ในตารางต่อไปนี้สำหรับแต่ละโมเดล

| รุ่น | ขีดจำกัดโทเค็นขั้นต่ำ |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro Preview | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

วิธีเพิ่มโอกาสที่จะพบแคชแบบไม่เจาะจง

- ลองวางเนื้อหาขนาดใหญ่และเนื้อหาทั่วไปไว้ที่จุดเริ่มต้นของพรอมต์
- ลองส่งคำขอที่มีคำนำหน้าที่คล้ายกันภายในระยะเวลาสั้นๆ

คุณสามารถดูจำนวนโทเค็นที่แคชทำงานได้ในช่อง `usage_metadata` ของออบเจ็กต์การตอบกลับ

## การแคชแบบเจาะจง

การใช้ฟีเจอร์การแคชแบบเจาะจงของ Gemini API ช่วยให้คุณส่งเนื้อหาบางส่วนไปยังโมเดลได้ครั้งเดียว แคชโทเค็นอินพุต แล้วอ้างอิงโทเค็นที่แคชไว้สำหรับคำขอที่ตามมา เมื่อมีปริมาณการใช้งานถึงระดับหนึ่ง การใช้โทเค็นที่แคชไว้จะมีค่าใช้จ่ายต่ำกว่าการส่งโทเค็นชุดเดียวกันซ้ำๆ

เมื่อแคชชุดโทเค็น คุณสามารถเลือกระยะเวลาที่ต้องการให้แคชอยู่ก่อนที่ระบบจะลบโทเค็นโดยอัตโนมัติ ระยะเวลาการแคชนี้เรียกว่า *Time to Live* (TTL) หากไม่ได้ตั้งค่า TTL จะมีค่าเริ่มต้นเป็น 1 ชั่วโมง ค่าใช้จ่ายในการแคชขึ้นอยู่กับขนาดโทเค็นอินพุตและระยะเวลาที่คุณต้องการให้โทเค็นอยู่

ส่วนนี้จะถือว่าคุณได้ติดตั้ง Gemini SDK (หรือติดตั้ง curl)
และกำหนดค่าคีย์ API แล้วตามที่แสดงใน
[คู่มือเริ่มต้นใช้งาน](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)

### สร้างเนื้อหาโดยใช้แคช

### Python

ตัวอย่างต่อไปนี้แสดงวิธีสร้างเนื้อหาโดยใช้คำแนะนำระบบและไฟล์วิดีโอที่แคชไว้

### วิดีโอ

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

ตัวอย่างต่อไปนี้แสดงวิธีสร้างเนื้อหาโดยใช้คำแนะนำระบบและไฟล์ข้อความที่แคชไว้

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

ตัวอย่างต่อไปนี้แสดงวิธีสร้างเนื้อหาโดยใช้แคช

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

ตัวอย่างต่อไปนี้แสดงวิธีสร้างแคชแล้วใช้แคชเพื่อสร้างเนื้อหา

### วิดีโอ

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

### PDF

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

### แสดงรายการแคช

คุณไม่สามารถดึงหรือดูเนื้อหาที่แคชไว้ได้ แต่สามารถดึง
ข้อมูลเมตาของแคช (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` และ `expire_time`)

### Python

หากต้องการแสดงข้อมูลเมตาสำหรับแคชที่อัปโหลดทั้งหมด ให้ใช้ `CachedContent.list()`

```
for cache in client.caches.list():
  print(cache)
```

หากต้องการดึงข้อมูลเมตาสำหรับออบเจ็กต์แคชรายการเดียว ให้ใช้ `get` หากทราบชื่อ

```
client.caches.get(name=name)
```

### JavaScript

หากต้องการแสดงข้อมูลเมตาสำหรับแคชที่อัปโหลดทั้งหมด ให้ใช้ `GoogleGenAI.caches.list()`

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

ตัวอย่างต่อไปนี้แสดงรายการแคชทั้งหมด

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

ตัวอย่างต่อไปนี้แสดงรายการแคชโดยใช้ขนาดหน้า 2

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

### อัปเดตแคช

คุณสามารถตั้งค่า `ttl` หรือ `expire_time` ใหม่สำหรับแคช ระบบไม่รองรับการเปลี่ยนแปลงอื่นๆ เกี่ยวกับแคช

### Python

ตัวอย่างต่อไปนี้แสดงวิธีอัปเดต `ttl` ของแคชโดยใช้ `client.caches.update()`

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

หากต้องการตั้งเวลาหมดอายุ ระบบจะยอมรับออบเจ็กต์ `datetime` หรือสตริง datetime ที่จัดรูปแบบ ISO (`dt.isoformat()`, เช่น
`2025-01-27T16:02:36.473528+00:00`) เวลาของคุณต้องมีเขตเวลา
(`datetime.utcnow()` จะไม่แนบเขตเวลา แต่
`datetime.now(datetime.timezone.utc)` จะแนบเขตเวลา)

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

ตัวอย่างต่อไปนี้แสดงวิธีอัปเดต `ttl` ของแคชโดยใช้ `GoogleGenAI.caches.update()`

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

ตัวอย่างต่อไปนี้แสดงวิธีอัปเดต `TTL` ของแคช

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

ตัวอย่างต่อไปนี้แสดงวิธีอัปเดต `ttl` ของแคช

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### ลบแคช

บริการแคชมีการดำเนินการลบเพื่อนำเนื้อหาออกจากแคชด้วยตนเอง ตัวอย่างต่อไปนี้แสดงวิธีลบแคช

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

### การแคชแบบเจาะจงโดยใช้ไลบรารี OpenAI

หากคุณใช้[ไลบรารี OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th) คุณสามารถเปิดใช้
การแคชแบบเจาะจงได้โดยใช้พร็อพเพอร์ตี้ `cached_content` ใน
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=th#extra-body)

## กรณีที่ควรใช้การแคชแบบเจาะจง

การแคชบริบทเหมาะอย่างยิ่งสำหรับสถานการณ์ที่คำขอสั้นๆ อ้างอิงบริบทเริ่มต้นขนาดใหญ่ซ้ำๆ ลองใช้การแคชบริบทสำหรับกรณีการใช้งานต่อไปนี้

- แชทบ็อตที่มี[คำแนะนำระบบ](https://ai.google.dev/gemini-api/docs/system-instructions?hl=th)ที่ครอบคลุม
- การวิเคราะห์ไฟล์วิดีโอขนาดยาวซ้ำๆ
- การค้นหาชุดเอกสารขนาดใหญ่ที่เกิดขึ้นซ้ำๆ
- การวิเคราะห์ที่เก็บโค้ดหรือการแก้ไขข้อบกพร่องบ่อยๆ

### วิธีที่การแคชแบบเจาะจงช่วยลดค่าใช้จ่าย

การแคชบริบทเป็นฟีเจอร์แบบชำระเงินที่ออกแบบมาเพื่อลดค่าใช้จ่าย การเรียกเก็บเงินจะพิจารณาจากปัจจัยต่อไปนี้

1. **จำนวนโทเค็นแคช:** จำนวนโทเค็นอินพุตที่แคชไว้ ซึ่งจะเรียกเก็บเงินในอัตราที่ลดลงเมื่อรวมอยู่ในพรอมต์ที่ตามมา
2. **ระยะเวลาการจัดเก็บ:** ระยะเวลาที่จัดเก็บโทเค็นที่แคชไว้ (TTL) ซึ่งจะเรียกเก็บเงินตามระยะเวลา TTL ของจำนวนโทเค็นที่แคชไว้ ไม่มีขีดจำกัดขั้นต่ำหรือสูงสุดสำหรับ TTL
3. **ปัจจัยอื่นๆ:** ระบบจะเรียกเก็บค่าใช้จ่ายอื่นๆ เช่น โทเค็นอินพุตและโทเค็นเอาต์พุตที่ไม่ได้แคชไว้

โปรดดูรายละเอียดราคาล่าสุดในหน้าการกำหนดราคา Gemini API [pricing
page](https://ai.google.dev/pricing?hl=th) ดูวิธีนับโทเค็นได้ที่[คู่มือ
โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

### ข้อควรพิจารณาเพิ่มเติม

โปรดคำนึงถึงข้อควรพิจารณาต่อไปนี้เมื่อใช้การแคชบริบท

- จำนวนโทเค็นอินพุต *ขั้นต่ำ* สำหรับการแคชบริบทจะแตกต่างกันไปตามโมเดล *สูงสุด* จะเท่ากับค่าสูงสุดสำหรับโมเดลที่กำหนด (ดูข้อมูลเพิ่มเติมเกี่ยวกับการนับโทเค็นได้ที่
  ดู[คู่มือโทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th))
- โมเดลจะไม่แยกความแตกต่างระหว่างโทเค็นที่แคชไว้กับโทเค็นอินพุตปกติ เนื้อหาที่แคชไว้จะเป็นคำนำหน้าของพรอมต์
- ไม่มีอัตราพิเศษหรือขีดจำกัดการใช้งานสำหรับการแคชบริบท โดยจะใช้ขีดจำกัดอัตรามาตรฐานสำหรับ `GenerateContent` และขีดจำกัดโทเค็นจะรวมโทเค็นที่แคชไว้
- ระบบจะแสดงจำนวนโทเค็นที่แคชไว้ใน `usage_metadata` จากการดำเนินการสร้าง รับ และแสดงรายการของบริการแคช รวมถึงใน `GenerateContent` เมื่อใช้แคช

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
