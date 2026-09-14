---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=hi
fetched_at: 2026-09-14T05:50:10.423802+00:00
title: "\u0915\u0949\u0928\u094d\u091f\u0947\u0915\u094d\u0938\u094d\u091f \u0915\u0948\u0936 \u092e\u0947\u092e\u094b\u0930\u0940 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# कॉन्टेक्स्ट कैश मेमोरी

एआई के सामान्य वर्कफ़्लो में, एक ही इनपुट टोकन को बार-बार किसी मॉडल को पास किया जा सकता है. Gemini API, कैश मेमोरी की सुविधा के लिए दो अलग-अलग तरीके उपलब्ध कराता है:

- इंप्लिसिट कैश मेमोरी (Gemini 2.5 और नए मॉडल पर अपने-आप चालू हो जाती है. इससे लागत कम होने की कोई गारंटी नहीं है)
- एक्सप्लिसिट कैश मेमोरी (इसे ज़्यादातर मॉडल पर मैन्युअल तरीके से चालू किया जा सकता है. इससे लागत कम करने की गारंटी मिलती है)

एक्सप्लिसिट कैशिंग उन मामलों में फ़ायदेमंद होती है जहां आपको लागत में बचत की गारंटी चाहिए. हालांकि, इसमें डेवलपर को कुछ अतिरिक्त काम करना पड़ता है.

## इंप्लिसिट कैशिंग

Gemini 2.5 और इसके बाद के सभी मॉडल के लिए, इंप्लिसिट कैश मेमोरी की सुविधा डिफ़ॉल्ट रूप से चालू होती है. अगर आपका अनुरोध कैश मेमोरी से मिलता है, तो हम लागत में हुई बचत को अपने-आप लागू कर देते हैं. इसे चालू करने के लिए, आपको कुछ भी करने की ज़रूरत नहीं है. कॉन्टेक्स्ट कैश मेमोरी के लिए, हर मॉडल के हिसाब से कम से कम इनपुट टोकन की संख्या यहां दी गई है:

| मॉडल | कम से कम टोकन सीमा |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro की झलक | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

इंप्लिसिट कैश हिट की संभावना बढ़ाने के लिए:

- अपने प्रॉम्प्ट की शुरुआत में, बड़े और सामान्य कॉन्टेंट को शामिल करें
- कम समय में, एक जैसे प्रीफ़िक्स वाले अनुरोध भेजने की कोशिश करना

आपको रिस्पॉन्स ऑब्जेक्ट के `usage_metadata` फ़ील्ड में, उन टोकन की संख्या दिखेगी जो कैश मेमोरी में मौजूद थे.

## एक्सप्लिसिट कैशिंग

Gemini API की एक्सप्लिसिट कैशिंग सुविधा का इस्तेमाल करके, मॉडल को एक बार कुछ कॉन्टेंट दिया जा सकता है. साथ ही, इनपुट टोकन को कैश मेमोरी में सेव किया जा सकता है. इसके बाद, अगले अनुरोधों के लिए कैश मेमोरी में सेव किए गए टोकन का इस्तेमाल किया जा सकता है. कुछ वॉल्यूम पर, कैश किए गए टोकन का इस्तेमाल करना, टोकन के एक ही कॉर्पस को बार-बार पास करने की तुलना में कम खर्चीला होता है.

टोकन के सेट को कैश मेमोरी में सेव करते समय, यह चुना जा सकता है कि टोकन के अपने-आप मिटने से पहले, कैश मेमोरी कितने समय तक सेव रहे. कैश मेमोरी में सेव रहने की इस अवधि को *टाइम टू लिव* (टीटीएल) कहा जाता है. अगर इसे सेट नहीं किया जाता है, तो टीटीएल डिफ़ॉल्ट रूप से एक घंटे पर सेट होता है. कैशिंग की लागत, इनपुट टोकन के साइज़ और टोकन को सेव रखने की अवधि पर निर्भर करती है.

इस सेक्शन में यह माना गया है कि आपने Gemini SDK इंस्टॉल कर लिया है या आपके पास curl इंस्टॉल है. साथ ही, आपने [शुरू करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi) में दिखाए गए तरीके से एपीआई पासकोड कॉन्फ़िगर कर लिया है.

### कैश मेमोरी का इस्तेमाल करके कॉन्टेंट जनरेट करना

### Python

यहां दिए गए उदाहरण में, कैश मेमोरी में सेव किए गए सिस्टम के निर्देश और वीडियो फ़ाइल का इस्तेमाल करके, कॉन्टेंट जनरेट करने का तरीका बताया गया है.

### वीडियो

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

यहां दिए गए उदाहरण में, कैश मेमोरी में सेव किए गए सिस्टम के निर्देश और टेक्स्ट फ़ाइल का इस्तेमाल करके कॉन्टेंट जनरेट करने का तरीका बताया गया है.

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

### ऐप पर जाएं

यहां दिए गए उदाहरण में, कैश मेमोरी का इस्तेमाल करके कॉन्टेंट जनरेट करने का तरीका बताया गया है.

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

यहां दिए गए उदाहरण में, कैश मेमोरी बनाने और फिर उसका इस्तेमाल करके कॉन्टेंट जनरेट करने का तरीका बताया गया है.

### वीडियो

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

### कैश मेमोरी की सूची बनाना

कैश किए गए कॉन्टेंट को वापस नहीं लाया जा सकता और न ही देखा जा सकता है. हालांकि, कैश मेटाडेटा (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time`, और `expire_time`) को वापस लाया जा सकता है.

### Python

अपलोड की गई सभी कैश मेमोरी के लिए मेटाडेटा की सूची बनाने के लिए, `CachedContent.list()` का इस्तेमाल करें:

```
for cache in client.caches.list():
  print(cache)
```

अगर आपको किसी कैश मेमोरी ऑब्जेक्ट का नाम पता है, तो उसका मेटाडेटा पाने के लिए `get` का इस्तेमाल करें:

```
client.caches.get(name=name)
```

### JavaScript

अपलोड की गई सभी कैश मेमोरी के लिए मेटाडेटा की सूची बनाने के लिए, `GoogleGenAI.caches.list()` का इस्तेमाल करें:

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

### ऐप पर जाएं

यहां दिए गए उदाहरण में, सभी कैश मेमोरी की सूची दी गई है.

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

यहां दिए गए उदाहरण में, 2 पेज साइज़ का इस्तेमाल करके कैश मेमोरी की सूची दी गई है.

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

### कैश मेमोरी अपडेट करना

किसी कैश मेमोरी के लिए, नया `ttl` या `expire_time` सेट किया जा सकता है. कैश मेमोरी के बारे में कोई और बदलाव नहीं किया जा सकता.

### Python

यहां दिए गए उदाहरण में, `client.caches.update()` का इस्तेमाल करके, कैश मेमोरी के `ttl` को अपडेट करने का तरीका बताया गया है.

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

मैसेज की समयसीमा खत्म होने का समय सेट करने के लिए, यह `datetime` ऑब्जेक्ट या आईएसओ फ़ॉर्मैट वाली तारीख और समय की स्ट्रिंग (`dt.isoformat()`, जैसे कि `2025-01-27T16:02:36.473528+00:00`) स्वीकार करता है. आपके समय में टाइम ज़ोन शामिल होना चाहिए (`datetime.utcnow()` में टाइम ज़ोन शामिल नहीं होता है, `datetime.now(datetime.timezone.utc)` में टाइम ज़ोन शामिल होता है).

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

यहां दिए गए उदाहरण में, `GoogleGenAI.caches.update()` का इस्तेमाल करके, कैश मेमोरी के `ttl` को अपडेट करने का तरीका बताया गया है.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### ऐप पर जाएं

यहां दिए गए उदाहरण में, कैश मेमोरी के `TTL` को अपडेट करने का तरीका बताया गया है.

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

यहां दिए गए उदाहरण में, कैश मेमोरी के `ttl` को अपडेट करने का तरीका बताया गया है.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### कैश मेमोरी मिटाना

कैशिंग सेवा, कैश मेमोरी से कॉन्टेंट को मैन्युअल तरीके से हटाने के लिए, मिटाने की सुविधा देती है. यहां दिए गए उदाहरण में, कैश मेमोरी मिटाने का तरीका बताया गया है:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### ऐप पर जाएं

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

### OpenAI लाइब्रेरी का इस्तेमाल करके, कैश मेमोरी को साफ़ तौर पर मैनेज करना

अगर [OpenAI लाइब्रेरी](https://ai.google.dev/gemini-api/docs/openai?hl=hi) का इस्तेमाल किया जा रहा है, तो [`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=hi#extra-body) पर `cached_content` प्रॉपर्टी का इस्तेमाल करके, एक्सप्लिसिट कैश मेमोरी चालू की जा सकती है.

## एक्सप्लिसिट कैशिंग का इस्तेमाल कब करें

कॉन्टेक्स्ट कैश मेमोरी की सुविधा, खास तौर पर उन स्थितियों के लिए सही है जहां शुरुआती कॉन्टेक्स्ट के बड़े हिस्से को छोटे अनुरोधों में बार-बार रेफ़र किया जाता है. इन जैसे इस्तेमाल के उदाहरणों के लिए, कॉन्टेक्स्ट कैश मेमोरी का इस्तेमाल करें:

- [सिस्टम के निर्देशों](https://ai.google.dev/gemini-api/docs/system-instructions?hl=hi) के साथ चैटबॉट
- लंबी वीडियो फ़ाइलों का बार-बार विश्लेषण करना
- दस्तावेज़ों के बड़े सेट के ख़िलाफ़ बार-बार की जाने वाली क्वेरी
- कोड रिपॉज़िटरी का बार-बार विश्लेषण करना या गड़बड़ी ठीक करना

### एक्सप्लिसिट कैशिंग से लागत कैसे कम होती है

कॉन्टेक्स्ट कैश मेमोरी, पैसे चुकाकर इस्तेमाल की जाने वाली सुविधा है. इसे लागत कम करने के लिए डिज़ाइन किया गया है. बिलिंग इन बातों पर निर्भर करती है:

1. **कैश किए गए टोकन की संख्या:** कैश किए गए इनपुट टोकन की संख्या. इन्हें बाद के प्रॉम्प्ट में शामिल करने पर, कम दर पर बिल किया जाता है.
2. **स्टोरेज की अवधि:** कैश मेमोरी में सेव किए गए टोकन को सेव रखने की अवधि (टीटीएल).
   कैश मेमोरी में सेव किए गए टोकन की संख्या के टीटीएल के आधार पर बिल भेजा जाता है. टीटीएल के लिए, कम से कम या ज़्यादा से ज़्यादा की कोई सीमा नहीं होती.
3. **अन्य कारक:** अन्य शुल्क लागू होते हैं. जैसे, कैश मेमोरी में सेव न किए गए इनपुट टोकन और आउटपुट टोकन के लिए.

कीमत के बारे में अप-टू-डेट जानकारी के लिए, Gemini API के [कीमत वाले पेज](https://ai.google.dev/pricing?hl=hi) पर जाएं. टोकन की गिनती करने का तरीका जानने के लिए, [टोकन गाइड](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) देखें.

### ज़रूरी बातें

कॉन्टेक्स्ट कैश मेमोरी का इस्तेमाल करते समय, इन बातों का ध्यान रखें:

- कॉन्टेक्स्ट कैश मेमोरी के लिए, *कम से कम* इनपुट टोकन की संख्या मॉडल के हिसाब से अलग-अलग होती है. *ज़्यादा से ज़्यादा*
  की वैल्यू, दिए गए मॉडल के लिए ज़्यादा से ज़्यादा वैल्यू के बराबर होती है. (टोकन की गिनती के बारे में ज़्यादा जानने के लिए, [टोकन गाइड](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) देखें).
- यह मॉडल, कैश किए गए टोकन और सामान्य इनपुट टोकन के बीच कोई अंतर नहीं करता. कैश किया गया कॉन्टेंट, प्रॉम्प्ट का प्रीफ़िक्स होता है.
- कॉन्टेक्स्ट को कैश मेमोरी में सेव करने पर, इस्तेमाल की कोई सीमा या खास शुल्क नहीं लगता. `GenerateContent` के लिए, दर की स्टैंडर्ड सीमाएं लागू होती हैं. साथ ही, टोकन की सीमाओं में कैश मेमोरी में सेव किए गए टोकन शामिल होते हैं.
- कैश किए गए टोकन की संख्या, कैश सेवा के create, get, और list ऑपरेशनों के `usage_metadata` में दिखाई जाती है. साथ ही, कैश का इस्तेमाल करते समय `GenerateContent` में भी यह संख्या दिखती है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया."],[],[]]
