---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi
fetched_at: 2026-05-05T19:51:48.543101+00:00
title: "Hi\u1ec3u video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hiểu video

> Để tìm hiểu về tính năng tạo video, hãy xem hướng dẫn về [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi).

Các mô hình Gemini có thể xử lý video, cho phép nhiều trường hợp sử dụng tiên tiến dành cho nhà phát triển mà trước đây cần đến các mô hình dành riêng cho miền.
Một số tính năng về thị giác của Gemini bao gồm khả năng: mô tả, phân đoạn và trích xuất thông tin từ video, trả lời câu hỏi về nội dung video và tham chiếu đến các dấu thời gian cụ thể trong video.

Bạn có thể cung cấp video làm dữ liệu đầu vào cho Gemini theo những cách sau:

| Phương thức nhập | Kích thước tối đa | Trường hợp sử dụng được đề xuất |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (có tính phí) / 2 GB (miễn phí) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp có thể dùng lại. |
| [Đăng ký Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi#registration) | 2 GB (mỗi tệp, không có giới hạn về bộ nhớ) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp liên tục, có thể dùng lại. |
| [Dữ liệu nội tuyến](#inline-video) | < 100 MB | Tệp nhỏ (dưới 100 MB), thời lượng ngắn (dưới 1 phút), dữ liệu đầu vào một lần. |
| [URL trên YouTube](#youtube) | Không áp dụng | Video công khai trên YouTube. |

> **Lưu ý:** Bạn nên sử dụng [File API](#upload-video) cho hầu hết các trường hợp sử dụng, đặc biệt là đối với các tệp có kích thước lớn hơn 100 MB hoặc khi bạn muốn sử dụng lại tệp trên nhiều yêu cầu.

Để tìm hiểu về các phương thức nhập tệp khác, chẳng hạn như sử dụng URL bên ngoài hoặc tệp
được lưu trữ trong Google Cloud, hãy xem hướng dẫn về
[Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

### Tải tệp video lên

Đoạn mã sau đây tải một video mẫu xuống, tải video đó lên bằng [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi),
đợi video được xử lý, sau đó sử dụng tham chiếu tệp đã tải lên để
tóm tắt video.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3-flash-preview",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Luôn sử dụng Files API khi tổng kích thước yêu cầu (bao gồm tệp, câu lệnh bằng văn bản, hướng dẫn hệ thống, v.v.) lớn hơn 20 MB, thời lượng video đáng kể hoặc nếu bạn dự định sử dụng cùng một video trong nhiều câu lệnh.
File API chấp nhận trực tiếp các định dạng tệp video.

Để tìm hiểu thêm về cách làm việc với các tệp đa phương tiện, hãy xem
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

### Truyền dữ liệu video nội tuyến

Thay vì tải tệp video lên bằng File API, bạn có thể truyền trực tiếp các video nhỏ hơn trong yêu cầu đến `generateContent`. Phương thức này phù hợp với các video ngắn hơn có tổng kích thước yêu cầu dưới 20 MB.

Sau đây là ví dụ về cách cung cấp dữ liệu video nội tuyến:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### Truyền URL trên YouTube

Bạn có thể truyền trực tiếp URL trên YouTube đến Gemini API như một phần của yêu cầu như sau:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Giới hạn:**

- Đối với gói miễn phí, bạn không thể tải lên quá 8 giờ video trên YouTube mỗi ngày.
- Đối với gói có tính phí, không có giới hạn dựa trên thời lượng video.
- Đối với các mô hình trước Gemini 2.5, bạn chỉ có thể tải lên 1 video cho mỗi yêu cầu. Đối với các mô hình Gemini 2.5 trở lên, bạn có thể tải lên tối đa 10 video cho mỗi yêu cầu.
- Bạn chỉ có thể tải lên video công khai (không phải video riêng tư hoặc không công khai).

## Sử dụng tính năng lưu vào bộ nhớ đệm theo bối cảnh cho video dài

Đối với những video dài hơn 10 phút hoặc khi bạn dự định thực hiện nhiều yêu cầu
đối với cùng một tệp video, hãy sử dụng [tính năng lưu vào bộ nhớ đệm theo bối cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) để
giảm chi phí và cải thiện độ trễ. Tính năng lưu vào bộ nhớ đệm theo bối cảnh cho phép bạn xử lý video một lần và sử dụng lại các mã thông báo cho các truy vấn tiếp theo, giúp tính năng này trở nên lý tưởng cho các phiên trò chuyện hoặc phân tích lặp lại nội dung dài.

## Tham chiếu đến dấu thời gian trong nội dung

Bạn có thể đặt câu hỏi về các điểm cụ thể trong video bằng cách sử dụng dấu thời gian ở dạng `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Trích xuất thông tin chi tiết từ video

Các mô hình Gemini cung cấp các tính năng mạnh mẽ để hiểu nội dung video bằng cách xử lý thông tin từ cả luồng **âm thanh và hình ảnh**. Điều này cho phép bạn trích xuất một tập hợp thông tin chi tiết phong phú, bao gồm cả việc tạo nội dung mô tả về những gì đang diễn ra trong video và trả lời câu hỏi về nội dung của video đó.

Đối với nội dung mô tả bằng hình ảnh, mô hình này lấy mẫu video với tốc độ **1 khung hình/giây** (FPS). Tốc độ lấy mẫu mặc định này hoạt động hiệu quả đối với hầu hết nội dung, nhưng lưu ý rằng tốc độ này có thể bỏ lỡ thông tin chi tiết trong các video có chuyển động nhanh hoặc thay đổi cảnh nhanh.
Đối với nội dung có chuyển động nhanh như vậy, hãy cân nhắc [đặt tốc độ khung hình tuỳ chỉnh](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Tuỳ chỉnh quá trình xử lý video

Bạn có thể tuỳ chỉnh quá trình xử lý video trong Gemini API bằng cách đặt khoảng thời gian cắt hoặc cung cấp tính năng lấy mẫu tốc độ khung hình tuỳ chỉnh.

### Đặt khoảng thời gian cắt

Bạn có thể cắt video bằng cách chỉ định `videoMetadata` với độ lệch bắt đầu và kết thúc.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3-flash-preview',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3-flash-preview';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Đặt tốc độ khung hình tuỳ chỉnh

Bạn có thể đặt tính năng lấy mẫu tốc độ khung hình tuỳ chỉnh bằng cách truyền đối số `fps` đến `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3-flash-preview',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

Theo mặc định, 1 khung hình/giây (FPS) được lấy mẫu từ video. Bạn có thể muốn đặt FPS thấp (dưới 1) cho video dài. Điều này đặc biệt hữu ích đối với các video tĩnh (ví dụ: bài giảng). Sử dụng FPS cao hơn cho các video yêu cầu phân tích chi tiết theo thời gian, chẳng hạn như hiểu hành động nhanh hoặc theo dõi chuyển động tốc độ cao.

## Định dạng video được hỗ trợ

Gemini hỗ trợ các loại MIME định dạng video sau:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Thông tin chi tiết kỹ thuật về video

- **Mô hình và bối cảnh được hỗ trợ**: Tất cả các mô hình Gemini đều có thể xử lý dữ liệu video.
  - Các mô hình có cửa sổ ngữ cảnh 1M có thể xử lý video dài tối đa 1 giờ ở độ phân giải phương tiện mặc định hoặc dài tối đa 3 giờ ở độ phân giải phương tiện thấp.
- **Xử lý File API**: Khi sử dụng File API, video được lưu trữ ở tốc độ 1
  khung hình/giây (FPS) và âm thanh được xử lý ở tốc độ 1 Kbps (một kênh).
  Dấu thời gian được thêm vào mỗi giây.
  - Các tốc độ này có thể thay đổi trong tương lai để cải thiện khả năng suy luận.
  - Bạn có thể ghi đè tốc độ lấy mẫu 1 FPS bằng cách [đặt tốc độ khung hình tuỳ chỉnh](#custom-frame-rate).
- **Tính toán mã thông báo**: Mỗi giây video được mã hoá thành mã thông báo như sau:
  - Khung hình riêng lẻ (được lấy mẫu ở tốc độ 1 FPS):
    - Nếu [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=vi#MediaResolution) được đặt
      thành thấp, thì các khung hình sẽ được mã hoá thành mã thông báo ở tốc độ 66 mã thông báo/khung hình.
    - Nếu không, các khung hình sẽ được mã hoá thành mã thông báo ở tốc độ 258 mã thông báo/khung hình.
  - Âm thanh: 32 mã thông báo/giây.
  - Siêu dữ liệu cũng được đưa vào.
  - Tổng cộng: Khoảng 300 mã thông báo/giây video ở độ phân giải phương tiện mặc định hoặc 100 mã thông báo/giây video ở độ phân giải phương tiện thấp.
- **Độ phân giải phương tiện**: Gemini 3 giới thiệu tính năng kiểm soát chi tiết quá trình xử lý thị giác đa phương thức
  bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi hình ảnh hoặc khung hình video đầu vào.**
  Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

  Để biết thêm thông tin chi tiết về tham số và cách tham số này có thể tác động đến việc tính toán mã thông báo, hãy xem hướng dẫn về [độ phân giải phương tiện](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi).
- **Định dạng dấu thời gian**: Khi tham chiếu đến các khoảnh khắc cụ thể trong video trong lời nhắc, hãy sử dụng định dạng `MM:SS` (ví dụ: `01:15` cho 1 phút 15 giây).
- **Các phương pháp hay nhất**:

  - Chỉ sử dụng một video cho mỗi yêu cầu lời nhắc để có kết quả tối ưu.
  - Nếu kết hợp văn bản và một video, hãy đặt lời nhắc bằng văn bản *sau* phần video trong mảng `contents`.
  - Xin lưu ý rằng các chuỗi hành động nhanh có thể mất thông tin chi tiết do tốc độ lấy mẫu 1 FPS. Hãy cân nhắc làm chậm các đoạn video như vậy nếu cần.

## Bước tiếp theo

Hướng dẫn này trình bày cách tải tệp video lên và tạo văn bản đầu ra từ dữ liệu đầu vào video. Để tìm hiểu thêm, hãy xem các tài nguyên sau:

- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions):
  Hướng dẫn hệ thống cho phép bạn điều chỉnh hành vi của mô hình dựa trên
  nhu cầu và trường hợp sử dụng cụ thể.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý
  tệp để sử dụng với Gemini.
- [Chiến lược đưa ra lời nhắc bằng tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide): Gemini API hỗ trợ đưa ra lời nhắc bằng dữ liệu văn bản, hình ảnh, âm thanh và video,
  còn được gọi là đưa ra lời nhắc đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh
  tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Việc xử lý hậu kỳ và đánh giá của con người là điều cần thiết để
  hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
