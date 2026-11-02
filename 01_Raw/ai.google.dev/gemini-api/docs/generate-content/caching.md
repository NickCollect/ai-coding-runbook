---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=bn
fetched_at: 2026-11-02T07:16:13.677605+00:00
title: "\u0995\u09a8\u09cd\u099f\u09c7\u0995\u09cd\u09b8\u099f \u0995\u09cd\u09af\u09be\u09b6\u09bf\u0982 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# কন্টেক্সট ক্যাশিং

সাধারণ AI ওয়ার্কফ্লোতে, আপনি একই ইনপুট টোকেন বারবার কোনও মডেলে
পাস করতে পারেন। Gemini API দুটি ভিন্ন ক্যাশিং মেকানিজম অফার করে:

- ইমপ্লিসিট ক্যাশিং (Gemini 2.5 এবং আরও নতুন মডেলে অটোমেটিক চালু করা হয়, খরচ বাঁচানোর কোনও গ্যারেন্টি নেই)
- এক্সপ্লিসিট ক্যাশিং (Gemini 3 এবং 2.5 মডেলে ম্যানুয়ালি চালু করা যেতে পারে, খরচ বাঁচানোর গ্যারান্টি; Gemini 4 Argon এবং তার পরবর্তী ভার্সনে কাজ করে না)

এক্সপ্লিসিট ক্যাশিং সেইসব ক্ষেত্রে উপযোগী যেখানে আপনি খরচ বাঁচানোর গ্যারান্টি চান,
তবে এর জন্য ডেভেলপারকে কিছু অতিরিক্ত কাজ করতে হয়।

## ইমপ্লিসিট ক্যাশিং

সব Gemini 2.5 এবং নতুন মডেলের জন্য ডিফল্ট হিসেবে ইমপ্লিসিট ক্যাশিং চালু করা থাকে। আপনার অনুরোধ ক্যাশে হিট করলে, আমরা অটোমেটিক
খরচ বাঁচাই। এটি চালু করার জন্য আপনাকে কিছু কনফিগার করতে হবে না। নিম্নলিখিত সারণীতে প্রতিটি মডেলের জন্য ন্যূনতম ইনপুট টোকেন কাউন্ট তালিকাভুক্ত করা হয়েছে:

| মডেল | টোকেনের ন্যূনতম সীমা |
| --- | --- |
| Gemini 4 Argon | ৪,০৯৬ |
| Gemini 3.8 Flash | ৪,০৯৬ |
| Gemini 3.6 Flash | ৪,০৯৬ |
| Gemini 3.1 Pro প্রিভিউ | ৪,০৯৬ |
| Gemini 2.5 Flash | ২,০৪৮ |
| Gemini 2.5 Pro | ২,০৪৮ |

ইমপ্লিসিট ক্যাশে হিট হওয়ার সম্ভাবনা বাড়াতে:

- আপনার প্রম্পটের শুরুতে বড় এবং সাধারণ কন্টেন্ট রাখার চেষ্টা করুন
- অল্প সময়ের মধ্যে একই প্রিফিক্স সহ অনুরোধ পাঠানোর চেষ্টা করুন

আপনি রেসপন্স অবজেক্টের `usage_metadata` ফিল্ডে ক্যাশে হিট হওয়া টোকেনের সংখ্যা দেখতে পাবেন।

## এক্সপ্লিসিট ক্যাশিং

Gemini API-এর এক্সপ্লিসিট ক্যাশিং ফিচার ব্যবহার করে, আপনি কোনও কন্টেন্ট
মডেলে একবার পাস করতে, ইনপুট টোকেন ক্যাশে করতে এবং তারপরে পরবর্তী অনুরোধের জন্য
ক্যাশে করা টোকেন রেফার করতে পারবেন। নির্দিষ্ট ভলিউমে, একই কর্পাস টোকেন বারবার পাস করার চেয়ে
ক্যাশে করা টোকেন ব্যবহার করার খরচ কম।

আপনি যখন টোকেনের সেট ক্যাশে করেন, তখন টোকেনগুলি অটোমেটিক মুছে ফেলার আগে আপনি কতক্ষণ ক্যাশে রাখতে চান তা বেছে নিতে পারেন। এই ক্যাশিংয়ের সময়সীমাকে
*টাইম টু লাইভ* (TTL) বলা হয়। সেট করা না থাকলে, TTL ডিফল্ট হিসেবে ১ ঘণ্টা সেট করা হয়। ক্যাশিংয়ের
খরচ ইনপুট টোকেনের সাইজ এবং আপনি কতক্ষণ টোকেন
রাখতে চান তার উপর নির্ভর করে।

এই বিভাগে ধরে নেওয়া হয়েছে যে আপনি Gemini SDK ইনস্টল করেছেন (অথবা curl ইনস্টল করেছেন)
এবং আপনি API কী কনফিগার করেছেন, যেমনটি
[শুরু করার নির্দেশিকা](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)-তে দেখানো হয়েছে।

### ক্যাশে ব্যবহার করে কন্টেন্ট জেনারেট করা

### Python

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে ক্যাশে করা সিস্টেম নির্দেশাবলী এবং ভিডিও ফাইল ব্যবহার করে কন্টেন্ট জেনারেট করতে হয়।

### ভিডিও

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

### জাভাস্ক্রিপ্ট

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে ক্যাশে করা সিস্টেম নির্দেশাবলী এবং টেক্সট ফাইল ব্যবহার করে কন্টেন্ট জেনারেট করতে হয়।

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

### খুলুন

ক্যাশে ব্যবহার করে কীভাবে কন্টেন্ট জেনারেট করতে হয় তা নিম্নলিখিত উদাহরণ থেকে দেখুন।

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

### বিশ্রাম

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে ক্যাশে তৈরি করতে হয় এবং তারপর কন্টেন্ট জেনারেট করতে
সেটি ব্যবহার করতে হয়।

### ভিডিও

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

### PDF

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

### ক্যাশের তালিকা তৈরি করা হচ্ছে

ক্যাশে করা কন্টেন্ট ফিরিয়ে আনা বা দেখা সম্ভব নয়, তবে আপনি ক্যাশে মেটাডেটা (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` এবং `expire_time`) ফিরিয়ে আনতে পারবেন।

### Python

আপলোড করা সব ক্যাশের মেটাডেটা তালিকাভুক্ত করতে, `CachedContent.list()` ব্যবহার করুন:

```
for cache in client.caches.list():
  print(cache)
```

একটি ক্যাশে অবজেক্টের মেটাডেটা ফেচ করতে, আপনি যদি এটির নাম জানেন, তাহলে `get` ব্যবহার করুন:

```
client.caches.get(name=name)
```

### জাভাস্ক্রিপ্ট

আপলোড করা সব ক্যাশের মেটাডেটা তালিকাভুক্ত করতে, `GoogleGenAI.caches.list()` ব্যবহার করুন:

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

### খুলুন

নিম্নলিখিত উদাহরণে সব ক্যাশের তালিকা দেখানো হয়েছে।

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

নিম্নলিখিত উদাহরণে ২ পৃষ্ঠার সাইজ ব্যবহার করে ক্যাশে তালিকাভুক্ত করা হয়েছে।

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

### বিশ্রাম

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### ক্যাশে আপডেট করা

আপনি ক্যাশের জন্য নতুন `ttl` বা `expire_time` সেট করতে পারবেন। ক্যাশে সম্পর্কে অন্য কিছু পরিবর্তন করার
সুবিধা কাজ করে না।

### Python

`client.caches.update()` ব্যবহার করে কীভাবে ক্যাশের `ttl` আপডেট করতে হয় তা নিম্নলিখিত উদাহরণে দেখানো হয়েছে।

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

মেয়াদ উত্তীর্ণের সময় সেট করতে, এটি হয় `datetime` অবজেক্ট
অথবা ISO-ফর্ম্যাট করা তারিখ ও সময়ের স্ট্রিং (`dt.isoformat()`, যেমন
`2025-01-27T16:02:36.473528+00:00`) গ্রহণ করবে। আপনার সময়ে অবশ্যই টাইম জোন অন্তর্ভুক্ত থাকতে হবে
(`datetime.utcnow()`-এ টাইম জোন অ্যাটাচ করা থাকে না,
`datetime.now(datetime.timezone.utc)`-এ টাইম জোন অ্যাটাচ করা থাকে)।

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

### জাভাস্ক্রিপ্ট

`GoogleGenAI.caches.update()` ব্যবহার করে কীভাবে ক্যাশের `ttl` আপডেট করতে হয় তা নিম্নলিখিত উদাহরণে দেখানো হয়েছে।

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### খুলুন

ক্যাশের `TTL` কীভাবে আপডেট করতে হয় তা নিম্নলিখিত উদাহরণ থেকে দেখুন।

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

### বিশ্রাম

নিচের উদাহরণে দেখানো হয়েছে যে কীভাবে ক্যাশের `ttl` আপডেট করতে হয়।

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### ক্যাশে মুছে ফেলা

ক্যাশিং পরিষেবা ক্যাশ থেকে ম্যানুয়ালি কন্টেন্ট সরানোর জন্য
একটি মুছে ফেলার অপারেশন প্রদান করে। নিচের উদাহরণে দেখানো হয়েছে কীভাবে ক্যাশে মুছতে হয়:

### Python

```
client.caches.delete(cache.name)
```

### জাভাস্ক্রিপ্ট

```
await ai.caches.delete({ name: cache.name });
```

### খুলুন

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### বিশ্রাম

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### OpenAI লাইব্রেরি ব্যবহার করে এক্সপ্লিসিট ক্যাশিং

আপনি [OpenAI লাইব্রেরি](https://ai.google.dev/gemini-api/docs/openai?hl=bn) ব্যবহার করলে, [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=bn#extra-body)-এ `cached_content` প্রপার্টি ব্যবহার করে
এক্সপ্লিসিট ক্যাশিং চালু করতে পারবেন।

## এক্সপ্লিসিট ক্যাশিং কখন ব্যবহার করতে হয়

কন্টেক্সট ক্যাশে করার সুবিধাটি বিশেষ করে এমন পরিস্থিতিতে উপযুক্ত যেখানে একটি উল্লেখযোগ্য
প্রাথমিক কন্টেক্সট ছোট অনুরোধের মাধ্যমে বারবার রেফার করা হয়। এই ধরনের ব্যবহারের ক্ষেত্রে
কনটেক্সট ক্যাশিং ব্যবহার করার কথা বিবেচনা করুন:

- বিস্তারিত [সিস্টেম নির্দেশাবলী](https://ai.google.dev/gemini-api/docs/system-instructions?hl=bn) সহ চ্যাটবট
- দীর্ঘ ভিডিও ফাইলের পুনরাবৃত্তিমূলক বিশ্লেষণ
- ডকুমেন্টের বড় সেট থেকে বারবার কোয়েরি করা
- ঘন ঘন কোড রিপোজিটরি বিশ্লেষণ বা ত্রুটি সমাধান করা

### কীভাবে এক্সপ্লিসিট ক্যাশিং খরচ কমায়

কনটেক্সট ক্যাশিং হল একটি পেড ফিচার যা খরচ কমানোর জন্য ডিজাইন করা হয়েছে। বিলিং নিম্নলিখিত
বিষয়ের উপর নির্ভর করে:

1. **ক্যাশে টোকেন কাউন্ট:** ক্যাশে করা ইনপুট টোকেনের সংখ্যা, পরবর্তী প্রম্পটে অন্তর্ভুক্ত করা হলে
   কম রেটে বিল করা হয়।
2. **স্টোরেজের সময়সীমা:** ক্যাশে করা টোকেন যত সময়ের জন্য স্টোর করা হয় (TTL),
   ক্যাশে করা টোকেন কাউন্টের TTL সময়সীমার ভিত্তিতে বিল করা হয়। TTL-এর কোনও ন্যূনতম
   বা সর্বাধিক সীমা নেই।
3. **অন্যান্য ফ্যাক্টর:** অন্যান্য চার্জ প্রযোজ্য, যেমন নন-ক্যাশড ইনপুট টোকেন
   এবং আউটপুট টোকেনের জন্য।

আপ-টু-ডেট দামের বিবরণ জানতে, Gemini API [দামের
পৃষ্ঠা](https://ai.google.dev/pricing?hl=bn) দেখুন। টোকেন কীভাবে গণনা করতে হয় তা জানতে, [টোকেন
গাইড](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) দেখুন।

### বিবেচনা করার মতো আরও বিষয়

কনটেক্সট ক্যাশিং ব্যবহার করার সময় নিম্নলিখিত বিষয়গুলি মনে রাখবেন:

- কনটেক্সট ক্যাশিংয়ের জন্য *ন্যূনতম* ইনপুট টোকেন কাউন্ট মডেল অনুযায়ী আলাদা হয়। *সর্বাধিক*
  মান প্রদত্ত মডেলের সর্বাধিক মানের সমান। (টোকেন গণনা সম্পর্কে আরও জানতে,
  [টোকেন সংক্রান্ত নির্দেশিকা](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) দেখুন)।
- মডেলটি ক্যাশে করা টোকেন এবং সাধারণ ইনপুট টোকেনের মধ্যে কোনও পার্থক্য করে না। ক্যাশে করা কন্টেন্ট হল প্রম্পটের প্রিফিক্স।
- কনটেক্সট ক্যাশিংয়ের ক্ষেত্রে কোনও বিশেষ রেট বা ব্যবহারের সীমা নেই; `GenerateContent`-এর জন্য স্ট্যান্ডার্ড
  রেট সীমা প্রযোজ্য হয় এবং টোকেন সীমার মধ্যে ক্যাশে করা
  টোকেন অন্তর্ভুক্ত থাকে।
- ক্যাশে করা টোকেনের সংখ্যা `usage_metadata`-এ ক্যাশে পরিষেবার তৈরি, পাওয়া এবং তালিকা অপারেশন থেকে এবং ক্যাশে ব্যবহার করার সময় `GenerateContent`-এও ফেরত দেওয়া হয়।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-23 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-23 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
