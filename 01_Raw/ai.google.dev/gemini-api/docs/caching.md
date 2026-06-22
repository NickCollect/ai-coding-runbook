---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ko
fetched_at: 2026-06-22T06:27:45.255147+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 컨텍스트 캐싱

일반적인 AI 워크플로에서는 동일한 입력 토큰을 모델에 반복적으로 전달할 수 있습니다. Gemini API는 다음과 같은 두 가지 캐싱 메커니즘을 제공합니다.

- 암시적 캐싱 (Gemini 2.5 이상 모델에서 자동으로 사용 설정되며 비용 절감 보장 없음)
- 명시적 캐싱 (대부분의 모델에서 수동으로 사용 설정할 수 있으며 비용 절감 보장)

명시적 캐싱은 비용 절감을 보장하되 개발자 작업을 추가하려는 경우에 유용합니다.

## 암시적 캐싱

암시적 캐싱은 모든 Gemini 2.5 이상 모델에서 기본적으로 사용 설정됩니다. 요청이 캐시에 적중하면 비용 절감 효과가 자동으로 전달됩니다. 이를 사용 설정하기 위해 수행해야 할 작업은 없습니다. 컨텍스트 캐싱의 최소 입력 토큰 수는 각 모델의 다음 표에 나와 있습니다.

| 모델 | 최소 토큰 한도 |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro 프리뷰 | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

암시적 캐시 적중 가능성을 높이려면 다음 안내를 따르세요.

- 프롬프트 시작 부분에 크고 공통적인 콘텐츠를 배치해 보세요.
- 짧은 시간 내에 유사한 프리픽스를 가진 요청을 전송해 보세요.

응답 객체의 `usage_metadata` 필드에서 캐시 적중된 토큰 수를 확인할 수 있습니다.

## 명시적 캐싱

Gemini API 명시적 캐싱 기능을 사용하면 콘텐츠를 모델에 한 번 전달하고 입력 토큰을 캐시한 후 후속 요청에서 캐시된 토큰을 참조할 수 있습니다. 특정 볼륨에서 캐시된 토큰을 사용하는 것이 동일한 토큰 코퍼스를 반복적으로 전달하는 것보다 비용이 저렴합니다.

토큰 세트를 캐시할 때 토큰이 자동으로 삭제되기 전에 캐시가 유지될 기간을 선택할 수 있습니다. 이 캐싱 기간을 *TTL (수명)* 이라고 합니다. 설정하지 않으면 TTL 기본값은 1시간입니다. 캐싱 비용은 입력 토큰 크기와 토큰을 유지하려는 기간에 따라 다릅니다.

이 섹션에서는 빠른 시작에 표시된 대로 Gemini SDK를 설치했거나 curl이 설치되어 있고
API 키를 구성했다고 가정합니다.

### 캐시를 사용하여 콘텐츠 생성

### Python

다음 예시에서는 캐시된 시스템 안내 및 동영상 파일을 사용하여 콘텐츠를 생성하는 방법을 보여줍니다.

### 동영상

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

다음 예시에서는 캐시된 시스템 안내 및 텍스트 파일을 사용하여 콘텐츠를 생성하는 방법을 보여줍니다.

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

다음 예시에서는 캐시를 사용하여 콘텐츠를 생성하는 방법을 보여줍니다.

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

다음 예시에서는 캐시를 만든 후 이를 사용하여 콘텐츠를 생성하는 방법을 보여줍니다.

### 동영상

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

### 캐시 나열

캐시된 콘텐츠를 가져오거나 볼 수는 없지만
캐시 메타데이터 (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time`, `expire_time`)는 가져올 수 있습니다.

### Python

업로드된 모든 캐시의 메타데이터를 나열하려면 `CachedContent.list()`를 사용하세요.

```
for cache in client.caches.list():
  print(cache)
```

이름을 알고 있는 경우 하나의 캐시 객체의 메타데이터를 가져오려면 `get`을 사용하세요.

```
client.caches.get(name=name)
```

### JavaScript

업로드된 모든 캐시의 메타데이터를 나열하려면 `GoogleGenAI.caches.list()`를 사용하세요.

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

다음 예시에서는 모든 캐시를 나열합니다.

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

다음 예시에서는 페이지 크기가 2인 캐시를 나열합니다.

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

### 캐시 업데이트

캐시에 새 `ttl` 또는 `expire_time`을 설정할 수 있습니다. 캐시에 대한 다른 변경사항은 지원되지 않습니다.

### Python

다음 예시에서는 `client.caches.update()`를 사용하여 캐시의 `ttl`을 업데이트하는 방법을 보여줍니다.

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

만료 시간을 설정하려면 `datetime` 객체
또는 ISO 형식의 datetime 문자열 (`dt.isoformat()`,
`2025-01-27T16:02:36.473528+00:00`과 같은)을 허용합니다. 시간에는 시간대가 포함되어야 합니다
(`datetime.utcnow()`는 시간대를 연결하지 않지만
`datetime.now(datetime.timezone.utc)`는 시간대를 연결함).

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

다음 예시에서는 `GoogleGenAI.caches.update()`를 사용하여 캐시의 `ttl`을 업데이트하는 방법을 보여줍니다.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

다음 예시에서는 캐시의 `TTL`을 업데이트하는 방법을 보여줍니다.

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

다음 예시에서는 캐시의 `ttl`을 업데이트하는 방법을 보여줍니다.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### 캐시 삭제

캐싱 서비스는 캐시에서 콘텐츠를 수동으로 삭제하는 삭제 작업을 제공합니다. 다음 예시에서는 캐시를 삭제하는 방법을 보여줍니다.

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

### OpenAI 라이브러리를 사용한 명시적 캐싱

[OpenAI 라이브러리를 사용하는 경우  속성을 사용하여 명시적 캐싱을 사용 설정할 수 있습니다.](https://ai.google.dev/gemini-api/docs/openai?hl=ko#extra-body)`cached_content``extra_body`

## 명시적 캐싱을 사용하는 경우

컨텍스트 캐싱은 짧은 요청에서 상당한 양의 초기 컨텍스트를 반복적으로 참조하는 시나리오에 특히 적합합니다. 다음과 같은 사용 사례에 컨텍스트 캐싱을 사용하는 것이 좋습니다.

- 다양한 [시스템 안내](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ko)를 제공하는 챗봇
- 긴 동영상 파일 반복 분석
- 대규모 문서 세트에 대해 반복 쿼리
- 빈번한 코드 저장소 분석 또는 버그 수정

### 명시적 캐싱으로 비용을 절감하는 방법

컨텍스트 캐싱은 비용을 절감하기 위해 설계된 유료 기능입니다. 다음 요소를 기준으로 결제가 청구됩니다.

1. **캐시 토큰 수:** 캐시된 입력 토큰 수로, 후속 프롬프트에 포함될 경우 할인된 요율로 청구됩니다.
2. **스토리지 기간:** 캐시된 토큰이 저장되는 시간 (TTL)으로, 캐시된 토큰 수의 TTL 기간을 기준으로 청구됩니다. TTL에는 최소 또는 최대 경계가 없습니다.
3. **기타 요인:** 캐시되지 않은 입력 토큰 및 출력 토큰과 같은 기타 요인에 다른 요금이 청구됩니다.

최신 가격 책정 세부정보는 Gemini API [pricing
page](https://ai.google.dev/pricing?hl=ko)를 참조하세요. 토큰 수를 집계하는 방법을 알아보려면 [토큰
가이드](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)를 참고하세요.

### 추가 고려사항

컨텍스트 캐싱을 사용할 때는 다음 고려사항에 유의하세요.

- 컨텍스트 캐싱의 *최소* 입력 토큰 수는 모델에 따라 다릅니다. *최대* 는 지정된 모델의 최대값과 동일합니다. (토큰 집계에 대한 자세한 내용은
  [토큰 가이드](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)를 참고하세요.)
- 모델은 캐시된 토큰과 일반 입력 토큰을 구분하지 않습니다. 캐시된 콘텐츠는 프롬프트의 프리픽스입니다.
- 컨텍스트 캐싱에는 특별한 요율 또는 사용량 제한이 없습니다. `GenerateContent`의 표준 요율 제한이 적용되며 토큰 한도에는 캐시된 토큰이 포함됩니다.
- 캐시된 토큰 수는 캐시 서비스의 생성, 가져오기, 나열 작업의 `usage_metadata`와 캐시를 사용할 때 `GenerateContent`에서 반환됩니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-19(UTC)"],[],[]]
