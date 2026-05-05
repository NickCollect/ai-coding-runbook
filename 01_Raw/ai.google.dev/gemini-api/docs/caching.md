---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=vi
fetched_at: 2026-05-05T13:21:28.438444+00:00
title: "L\u01b0u ng\u1eef c\u1ea3nh v\u00e0o b\u1ed9 nh\u1edb \u0111\u1ec7m \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/Tính năng Nghiên cứu chuyên sâu của Gemini) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

- [Trang chủ](https://ai.google.dev/gemini-api/docs/Trang chủ)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/Tài liệu)

Gửi ý kiến phản hồi

# Lưu ngữ cảnh vào bộ nhớ đệm

Trong quy trình làm việc điển hình của AI, bạn có thể truyền đi truyền lại cùng một mã thông báo đầu vào cho một mô hình. Gemini API cung cấp 2 cơ chế lưu vào bộ nhớ đệm:

- Lưu vào bộ nhớ đệm ngầm (tự động bật trên Gemini 2.5 và các mô hình mới hơn, không đảm bảo tiết kiệm chi phí)
- Lưu vào bộ nhớ đệm rõ ràng (có thể bật theo cách thủ công trên hầu hết các mô hình, đảm bảo tiết kiệm chi phí)

Việc lưu vào bộ nhớ đệm rõ ràng sẽ hữu ích trong trường hợp bạn muốn đảm bảo tiết kiệm chi phí, nhưng cần thêm một số công việc của nhà phát triển.

## Lưu vào bộ nhớ đệm ngầm

Tính năng lưu vào bộ nhớ đệm ngầm định được bật theo mặc định cho tất cả các mô hình Gemini 2.5 trở lên. Chúng tôi tự động chuyển các khoản tiết kiệm chi phí nếu yêu cầu của bạn truy cập vào bộ nhớ đệm. Bạn không cần làm gì để bật tính năng này. Số lượng mã thông báo đầu vào tối thiểu để lưu vào bộ nhớ đệm ngữ cảnh được liệt kê trong bảng sau cho từng mô hình:

| Mô hình | Giới hạn mã thông báo tối thiểu |
| --- | --- |
| Bản xem trước Gemini 3 Flash | 1024 |
| Bản dùng thử Gemini 3 Pro | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

Để tăng cơ hội đạt được kết quả tìm kiếm trong bộ nhớ cache ngầm ẩn:

- Hãy thử đặt nội dung lớn và phổ biến ở đầu câu lệnh
- Hãy thử gửi các yêu cầu có tiền tố tương tự trong một khoảng thời gian ngắn

Bạn có thể xem số lượng mã thông báo là lượt truy cập vào bộ nhớ đệm trong trường `usage_metadata` của đối tượng phản hồi.

## Lưu vào bộ nhớ đệm một cách rõ ràng

Khi sử dụng tính năng lưu vào bộ nhớ đệm rõ ràng của Gemini API, bạn có thể truyền một số nội dung đến mô hình một lần, lưu mã thông báo đầu vào vào bộ nhớ đệm, sau đó tham chiếu đến mã thông báo đã lưu vào bộ nhớ đệm cho các yêu cầu tiếp theo. Ở một số lượng nhất định, việc sử dụng mã thông báo được lưu vào bộ nhớ đệm sẽ có chi phí thấp hơn so với việc truyền cùng một tập hợp mã thông báo nhiều lần.

Khi lưu trữ một nhóm mã thông báo vào bộ nhớ đệm, bạn có thể chọn khoảng thời gian bạn muốn bộ nhớ đệm tồn tại trước khi mã thông báo bị xoá tự động. Khoảng thời gian lưu vào bộ nhớ đệm này được gọi là *thời gian tồn tại* (TTL). Nếu bạn không đặt, TTL sẽ mặc định là 1 giờ. Chi phí lưu vào bộ nhớ đệm phụ thuộc vào kích thước mã thông báo đầu vào và thời gian bạn muốn mã thông báo duy trì.

Phần này giả định rằng bạn đã cài đặt Gemini SDK (hoặc đã cài đặt curl) và bạn đã định cấu hình khoá API, như trong phần [bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/bắt đầu nhanh).

### Tạo nội dung bằng bộ nhớ đệm

### Python

Ví dụ sau đây cho biết cách tạo nội dung bằng chỉ dẫn hệ thống và tệp video được lưu vào bộ nhớ đệm.

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

Ví dụ sau đây minh hoạ cách tạo nội dung bằng cách sử dụng một chỉ dẫn hệ thống được lưu vào bộ nhớ đệm và một tệp văn bản.

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

Ví dụ sau đây cho thấy cách tạo nội dung bằng bộ nhớ đệm.

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

Ví dụ sau đây cho biết cách tạo bộ nhớ đệm rồi dùng bộ nhớ đệm đó để tạo nội dung.

### Video

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

### PDF

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

### Liệt kê bộ nhớ đệm

Bạn không thể truy xuất hoặc xem nội dung trong bộ nhớ đệm, nhưng có thể truy xuất siêu dữ liệu bộ nhớ đệm (`name`, `model`, `display_name`, `usage_metadata`, `create_time`, `update_time` và `expire_time`).

### Python

Để liệt kê siêu dữ liệu cho tất cả bộ nhớ đệm đã tải lên, hãy sử dụng `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Để tìm nạp siêu dữ liệu cho một đối tượng trong bộ nhớ đệm, nếu bạn biết tên của đối tượng đó, hãy sử dụng `get`:

```
client.caches.get(name=name)
```

### JavaScript

Để liệt kê siêu dữ liệu cho tất cả bộ nhớ đệm đã tải lên, hãy sử dụng `GoogleGenAI.caches.list()`:

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

Ví dụ sau đây liệt kê tất cả các bộ nhớ đệm.

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

Ví dụ sau đây liệt kê các bộ nhớ đệm bằng kích thước trang là 2.

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

### Cập nhật bộ nhớ đệm

Bạn có thể đặt `ttl` hoặc `expire_time` mới cho bộ nhớ đệm. Không hỗ trợ việc thay đổi bất kỳ thông tin nào khác về bộ nhớ đệm.

### Python

Ví dụ sau đây cho thấy cách cập nhật `ttl` của một bộ nhớ đệm bằng `client.caches.update()`.

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

Để đặt thời gian hết hạn, bạn có thể chấp nhận đối tượng `datetime` hoặc chuỗi ngày giờ theo định dạng ISO (`dt.isoformat()`, chẳng hạn như `2025-01-27T16:02:36.473528+00:00`). Thời gian của bạn phải bao gồm múi giờ (`datetime.utcnow()` không đính kèm múi giờ, `datetime.now(datetime.timezone.utc)` có đính kèm múi giờ).

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

Ví dụ sau đây cho thấy cách cập nhật `ttl` của một bộ nhớ đệm bằng `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

Ví dụ sau đây cho thấy cách cập nhật `TTL` của một bộ nhớ đệm.

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

Ví dụ sau đây cho thấy cách cập nhật `ttl` của một bộ nhớ đệm.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Xoá bộ nhớ đệm

Dịch vụ lưu vào bộ nhớ đệm cung cấp một thao tác xoá để xoá nội dung khỏi bộ nhớ đệm theo cách thủ công. Ví dụ sau đây cho thấy cách xoá bộ nhớ đệm:

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

### Lưu vào bộ nhớ đệm một cách rõ ràng bằng thư viện OpenAI

Nếu đang sử dụng [thư viện OpenAI](https://ai.google.dev/gemini-api/docs/thư viện OpenAI), bạn có thể bật tính năng lưu vào bộ nhớ đệm rõ ràng bằng cách sử dụng thuộc tính `cached_content` trên [`extra_body`](https://ai.google.dev/gemini-api/docs/`extra_body`).

## Trường hợp sử dụng tính năng lưu vào bộ nhớ đệm rõ ràng

Tính năng lưu vào bộ nhớ đệm theo bối cảnh đặc biệt phù hợp với những trường hợp mà một bối cảnh ban đầu đáng kể được các yêu cầu ngắn hơn tham chiếu nhiều lần. Hãy cân nhắc sử dụng tính năng lưu vào bộ nhớ đệm theo bối cảnh cho các trường hợp sử dụng như:

- Chatbot có [hướng dẫn chi tiết về hệ thống](https://ai.google.dev/gemini-api/docs/hướng dẫn chi tiết về hệ thống)
- Phân tích lặp đi lặp lại các tệp video dài
- Truy vấn định kỳ đối với các tập tài liệu lớn
- Thường xuyên phân tích kho lưu trữ mã hoặc sửa lỗi

### Cách bộ nhớ đệm rõ ràng giúp giảm chi phí

Lưu vào bộ nhớ đệm theo ngữ cảnh là một tính năng có tính phí được thiết kế để giảm chi phí. Việc tính phí dựa trên các yếu tố sau:

1. **Số lượng mã thông báo trong bộ nhớ đệm:** Số lượng mã thông báo đầu vào được lưu vào bộ nhớ đệm, được tính phí với mức giá thấp hơn khi có trong các câu lệnh tiếp theo.
2. **Thời gian lưu trữ:** Khoảng thời gian lưu trữ mã thông báo được lưu vào bộ nhớ đệm (TTL), được tính phí dựa trên thời lượng TTL của số lượng mã thông báo được lưu vào bộ nhớ đệm. Không có giới hạn tối thiểu hoặc tối đa về TTL.
3. **Các yếu tố khác:** Các khoản phí khác được áp dụng, chẳng hạn như đối với mã thông báo đầu vào và đầu ra không được lưu vào bộ nhớ đệm.

Để biết thông tin chi tiết mới nhất về giá, hãy tham khảo [trang định giá](https://ai.google.dev/gemini-api/docs/trang định giá) của Gemini API. Để tìm hiểu cách đếm mã thông báo, hãy xem [Hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/Hướng dẫn về mã thông báo).

### Các yếu tố cần cân nhắc khác

Khi sử dụng tính năng lưu vào bộ nhớ đệm theo bối cảnh, hãy lưu ý những điểm sau:

- Số lượng mã thông báo đầu vào *tối thiểu* để lưu vào bộ nhớ đệm theo bối cảnh sẽ khác nhau tuỳ theo mô hình. *Tối đa* cũng giống như giá trị tối đa của mô hình đã cho. (Để biết thêm thông tin về cách đếm mã thông báo, hãy xem [Hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/Hướng dẫn về mã thông báo)).
- Mô hình này không phân biệt giữa các mã thông báo được lưu vào bộ nhớ đệm và các mã thông báo đầu vào thông thường. Nội dung trong bộ nhớ đệm là tiền tố của câu lệnh.
- Không có giới hạn đặc biệt về tốc độ hoặc mức sử dụng đối với tính năng lưu vào bộ nhớ đệm theo ngữ cảnh; các giới hạn tiêu chuẩn về tốc độ đối với `GenerateContent` sẽ được áp dụng và giới hạn mã thông báo bao gồm cả mã thông báo được lưu vào bộ nhớ đệm.
- Số lượng mã thông báo được lưu vào bộ nhớ đệm sẽ được trả về trong `usage_metadata` từ các thao tác tạo, nhận và liệt kê của dịch vụ bộ nhớ đệm, cũng như trong `GenerateContent` khi sử dụng bộ nhớ đệm.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://ai.google.dev/gemini-api/docs/Giấy phép ghi nhận tác giả 4.0 của Creative Commons) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://ai.google.dev/gemini-api/docs/Giấy phép Apache 2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://ai.google.dev/gemini-api/docs/Chính sách trang web của Google Developers). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?
