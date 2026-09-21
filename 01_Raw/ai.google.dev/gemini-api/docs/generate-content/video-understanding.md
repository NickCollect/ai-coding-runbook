---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=vi
fetched_at: 2026-09-21T05:47:27.686029+00:00
title: "Hi\u1ec3u video \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Hiểu video

> Để tìm hiểu về tính năng tạo video, hãy xem hướng dẫn về [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=vi).

Các mô hình Gemini có thể xử lý video, cho phép nhiều trường hợp sử dụng của nhà phát triển tiên phong mà trước đây cần đến các mô hình dành riêng cho miền.
Một số khả năng thị giác của Gemini bao gồm: mô tả, phân đoạn và trích xuất thông tin từ video, trả lời câu hỏi về nội dung video và tham khảo các dấu thời gian cụ thể trong video.

Bạn có thể cung cấp video làm dữ liệu đầu vào cho Gemini theo những cách sau:

| Phương thức nhập | Kích thước tối đa | Trường hợp sử dụng được đề xuất |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (có tính phí) / 2 GB (miễn phí) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp có thể dùng lại. |
| [Đăng ký Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi#registration) | 2 GB (mỗi tệp, không giới hạn bộ nhớ) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp có thể dùng lại và lưu trữ lâu dài. |
| [Dữ liệu nội tuyến](#inline-video) | < 100MB | Tệp nhỏ (<100 MB), thời lượng ngắn (<1 phút), dữ liệu đầu vào một lần. |
| [URL trên YouTube](#youtube) | Không áp dụng | Video công khai trên YouTube. |

> **Lưu ý:** Bạn nên dùng [File API](#upload-video) cho hầu hết các trường hợp sử dụng, đặc biệt là đối với những tệp có kích thước lớn hơn 100 MB hoặc khi bạn muốn dùng lại tệp trong nhiều yêu cầu.

Để tìm hiểu về các phương thức nhập tệp khác, chẳng hạn như sử dụng URL bên ngoài hoặc tệp được lưu trữ trong Google Cloud, hãy xem hướng dẫn [Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

### Tải tệp video lên

Đoạn mã sau đây tải một video mẫu xuống, tải video đó lên bằng [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi), đợi video được xử lý, sau đó dùng thông tin tham chiếu về tệp đã tải lên để tóm tắt video.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.8-flash",
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
    "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Để tối ưu hoá hiệu quả và hiệu suất của mã thông báo, hãy cân nhắc sử dụng [Xử lý video bằng tác nhân](#agentic-video-understanding).

Luôn sử dụng Files API khi tổng kích thước yêu cầu (bao gồm cả tệp, lời nhắc bằng văn bản, hướng dẫn hệ thống, v.v.) lớn hơn 20 MB, thời lượng video đáng kể hoặc nếu bạn dự định sử dụng cùng một video trong nhiều lời nhắc.
File API chấp nhận trực tiếp các định dạng tệp video.

Để tìm hiểu thêm về cách làm việc với các tệp nội dung nghe nhìn, hãy xem [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

### Truyền dữ liệu video nội tuyến

Thay vì tải tệp video lên bằng File API, bạn có thể truyền trực tiếp các video nhỏ hơn trong yêu cầu đến `generateContent`. Phương thức này phù hợp với những video ngắn có tổng kích thước yêu cầu dưới 20 MB.

Dưới đây là ví dụ về cách cung cấp dữ liệu video nội tuyến:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

### URL của YouTube

Bạn có thể truyền trực tiếp URL của YouTube đến Gemini API trong yêu cầu của mình như sau:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

**Các điểm hạn chế:**

- Đối với gói miễn phí, bạn không thể tải quá 8 giờ video trên YouTube lên mỗi ngày.
- Đối với gói có tính phí, không có giới hạn dựa trên thời lượng video.
- Đối với các mô hình trước Gemini 2.5, bạn chỉ có thể tải 1 video lên mỗi yêu cầu. Đối với Gemini 2.5 và các mô hình sau này, bạn có thể tải tối đa 10 video lên cho mỗi yêu cầu.
- Bạn chỉ có thể tải video công khai lên (không thể tải video riêng tư hoặc không công khai lên).

## Tính năng hiểu video dựa trên tác nhân

Theo mặc định, đầu vào video sử dụng quy trình xử lý tĩnh (trích xuất khung hình ở tốc độ 1 khung hình/giây).
Các mô hình Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash và 3.5 Flash Lite cũng hỗ trợ **khả năng hiểu video dựa trên tác nhân**, trong đó mô hình này sẽ khám phá dòng thời gian của video một cách linh hoạt, chọn lọc kiểm tra bản chép lời và điều chỉnh tốc độ khung hình cũng như độ phân giải một cách thích ứng ngay lập tức dựa trên câu lệnh.

| **Chế độ** | **Nội dung mô tả** | **Các mẫu được hỗ trợ** |
| --- | --- | --- |
| **Tĩnh** (mặc định) | Trích xuất các khung hình ở tốc độ cố định (1 khung hình/giây) và đặt chúng vào ngữ cảnh trong một lượt. Phù hợp với các đoạn video ngắn. | Tất cả các mô hình Gemini |
| **Tác nhân** | Mô hình này điều hướng dòng thời gian của video một cách linh hoạt, chỉ tải nội dung cần thiết dựa trên câu lệnh. Hiệu quả hơn tới 88% về mã thông báo và chất lượng cao hơn khoảng 7% đối với nội dung dạng dài. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### Chọn một chế độ xử lý

Theo nguyên tắc chung, hãy bắt đầu với chế độ **có tác nhân**, đặc biệt là khi tối ưu hoá để có chất lượng phản hồi hoặc hiệu quả sử dụng mã thông báo.

- **Dựa trên tác nhân:** Video dài hoặc cụm từ tìm kiếm nhắm đến những khoảnh khắc cụ thể. Mô hình này điều hướng dòng thời gian một cách linh hoạt để nhắm đến thông tin phù hợp theo ngữ cảnh mà không cần điền vào cửa sổ ngữ cảnh.
- **Tĩnh:** Các truy vấn nhạy cảm với độ trễ trên các đoạn video ngắn (dưới 5 phút) hoặc các trường hợp cần độ chính xác ở cấp khung hình trên toàn bộ đoạn video.

> **Lưu ý:** Đối với video dài hoặc câu lệnh phức tạp mà quá trình xử lý dựa trên tác nhân mất nhiều thời gian hơn, hãy sử dụng tính năng phát trực tuyến (`client.models.generate_content_stream`). Tính năng này duy trì kết nối, hiển thị các bước suy luận trung gian và tránh hết thời gian chờ kết nối hoặc xác thực.

### Đặt chế độ xử lý

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Lưu ý:** Để xác minh rằng quá trình xử lý dựa trên tác nhân đã được sử dụng, hãy kiểm tra `response.candidates[0].content.parts`. Sự xuất hiện của các phần `tool_call` và `tool_response` với loại công cụ `MEDIA_PROCESSING` cho biết rằng mô hình đã điều hướng video một cách linh hoạt.

> **Lưu ý:** Không giống như các công cụ phía máy chủ khác (chẳng hạn như Google Tìm kiếm hoặc ngữ cảnh URL), video dựa trên tác nhân không yêu cầu bạn đặt `include_server_side_tool_invocations=True` trong `ToolConfig` để các lệnh gọi công cụ và kết quả được trả về hoặc truyền trực tuyến. Các phần `tool_call` và `tool_response` để điều hướng video sẽ tự động được trả về khi `media_processing="AGENTIC"` được đặt trên bất kỳ phần đầu vào nào.

### Cấu trúc phản hồi

Khi được bật, tính năng xử lý dựa trên tác nhân sẽ bao gồm các phần bổ sung cho thấy dấu vết điều hướng nội bộ:

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`): được phát ra mỗi khi mô hình yêu cầu một đoạn video hoặc bản chép lời âm thanh.
- `tool_response` **parts** (`tool_type: "MEDIA_PROCESSING"`): kết quả của mỗi thao tác tải.

Bạn không cần xử lý hoặc trả lời những phần này theo cách thủ công: hãy truyền toàn bộ câu trả lời trở lại dưới dạng nhật ký cuộc trò chuyện và những phần này sẽ được xử lý tự động.

Nếu `include_thoughts=True` được đặt trong `ThinkingConfig`, các bước suy luận sẽ xuất hiện dưới dạng các phần `thought: true` xen kẽ với các cặp lệnh gọi/phản hồi của công cụ. Khi tắt tính năng suy nghĩ, văn bản suy nghĩ sẽ bị bỏ qua nhưng các phần công cụ vẫn xuất hiện.

Ví dụ sau đây cho thấy tải trọng phản hồi có các phần phản hồi và lệnh gọi công cụ xen kẽ:

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Kết hợp các chế độ xử lý trên nhiều video

Bạn có thể đặt các chế độ xử lý khác nhau cho từng Phần video trong cùng một yêu cầu:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Sử dụng tính năng lưu vào bộ nhớ đệm theo bối cảnh cho video dài

Đối với những video dài hơn 10 phút hoặc khi bạn dự định đưa ra nhiều yêu cầu đối với cùng một tệp video, hãy sử dụng [tính năng lưu vào bộ nhớ đệm theo bối cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) để giảm chi phí và cải thiện độ trễ. Tính năng lưu vào bộ nhớ đệm theo ngữ cảnh cho phép bạn xử lý video một lần và sử dụng lại các mã thông báo cho các truy vấn tiếp theo, nhờ đó, tính năng này rất phù hợp cho các phiên trò chuyện hoặc phân tích lặp lại nội dung dạng dài.

## Tham khảo dấu thời gian trong nội dung

Bạn có thể đặt câu hỏi về những thời điểm cụ thể trong video bằng cách sử dụng dấu thời gian có dạng `MM:SS`.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Trích xuất thông tin chi tiết từ video

Các mô hình Gemini có khả năng mạnh mẽ trong việc hiểu nội dung video bằng cách xử lý thông tin từ cả luồng **âm thanh và hình ảnh**. Nhờ đó, bạn có thể trích xuất một bộ thông tin chi tiết phong phú, bao gồm cả việc tạo nội dung mô tả về những gì đang diễn ra trong video và trả lời các câu hỏi về nội dung của video.

Đối với nội dung mô tả bằng hình ảnh, mô hình lấy mẫu video ở tốc độ **1 khung hình/giây** (FPS). Tỷ lệ lấy mẫu mặc định này phù hợp với hầu hết nội dung, nhưng lưu ý rằng tỷ lệ này có thể bỏ lỡ các chi tiết trong video có chuyển động nhanh hoặc cảnh thay đổi nhanh.
Đối với nội dung có chuyển động nhanh như vậy, hãy cân nhắc [đặt tốc độ khung hình tuỳ chỉnh](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Tuỳ chỉnh quy trình xử lý video

Bạn có thể tuỳ chỉnh quy trình xử lý video trong Gemini API bằng cách đặt khoảng thời gian cắt hoặc cung cấp chế độ lấy mẫu tốc độ khung hình tuỳ chỉnh. Các lựa chọn tuỳ chỉnh này chỉ được hỗ trợ khi xử lý video ở chế độ `"static"`.

### Đặt khoảng thời gian cắt

Bạn có thể cắt video bằng cách chỉ định `videoMetadata` với độ lệch bắt đầu và kết thúc.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
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
const model = 'gemini-3.8-flash';

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

Bạn có thể thiết lập chế độ lấy mẫu tốc độ khung hình tuỳ chỉnh bằng cách truyền một đối số `fps` đến `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
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

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

Theo mặc định, 1 khung hình/giây (FPS) sẽ được lấy mẫu từ video. Bạn nên đặt FPS thấp (< 1) cho video dài. Điều này đặc biệt hữu ích đối với những video tĩnh (ví dụ: bài giảng). Sử dụng tỷ lệ khung hình trên giây (FPS) cao hơn cho những video cần phân tích chi tiết về thời gian, chẳng hạn như hiểu được hành động nhanh hoặc theo dõi chuyển động tốc độ cao.

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

## Thông tin kỹ thuật về video

- **Mô hình và ngữ cảnh được hỗ trợ**: Tất cả các mô hình Gemini đều có thể xử lý dữ liệu video.
  - Theo mặc định, các mô hình có cửa sổ ngữ cảnh 1 triệu token có thể xử lý video dài tối đa 3 giờ (ở độ phân giải thấp) hoặc tối đa 1 giờ (ở độ phân giải cao).
- **Chế độ xử lý**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite và các mô hình sau này hỗ trợ 2 chế độ xử lý video:
  - **Tĩnh**: Khung hình được trích xuất ở tốc độ 1 FPS và được đặt vào ngữ cảnh (mặc định cho tất cả các mô hình). Âm thanh được xử lý ở tốc độ 1 Kb/giây (một kênh).
    Dấu thời gian được thêm vào mỗi giây. Phù hợp nhất với các đoạn video ngắn hoặc khi mọi khung hình đều quan trọng (chẳng hạn như kiểm tra từng khung hình). Xin lưu ý rằng các chuỗi hành động nhanh có thể mất chi tiết do tốc độ lấy mẫu 1 FPS.
  - **Agentic**: Mô hình này điều hướng video một cách linh hoạt, tải bản chép lời và/hoặc khung hình và/hoặc âm thanh theo yêu cầu. Điều này giúp giảm số lượng mã thông báo lên đến 88% cho nội dung dài, mặc dù điều hướng có thể làm tăng nhẹ Thời gian hiển thị mã thông báo đầu tiên (TTFT) trên các đoạn video ngắn (<5 phút) do quá trình suy luận nội bộ và các chuyến đi khứ hồi của công cụ trước khi bắt đầu tạo.
    Các phản hồi bao gồm các phần gọi công cụ và phản hồi `MEDIA_PROCESSING` để duy trì bối cảnh suy luận qua các lượt. Phù hợp nhất với video dài để tối ưu hoá chi phí mã thông báo và chất lượng phản hồi. Được hỗ trợ trên Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash và 3.5 Flash Lite. Hãy xem phần [Tính năng hiểu video dựa trên tác nhân](#agentic-video-understanding) để biết thông tin chi tiết.
- **Tính mã thông báo (chế độ tĩnh)**: Mỗi giây của video được mã hoá như sau:
  - Khung hình riêng lẻ (lấy mẫu ở tốc độ 1 khung hình/giây):
    - Nếu `media_resolution` được đặt thành thấp, các khung hình sẽ được mã hoá thành 66 mã thông báo trên mỗi khung hình.
    - Nếu không, các khung hình sẽ được mã hoá thành 258 mã thông báo cho mỗi khung hình.
  - Âm thanh: 32 mã thông báo mỗi giây.
  - Siêu dữ liệu cũng được đưa vào.
  - Tổng cộng: Khoảng 100 mã thông báo cho mỗi giây video ở độ phân giải mặc định (thấp) của nội dung nghe nhìn hoặc khoảng 300 mã thông báo cho mỗi giây video ở độ phân giải cao của nội dung nghe nhìn.
- **Tính toán mã thông báo (chế độ có tác nhân)**: Mức sử dụng mã thông báo sẽ thay đổi tuỳ theo độ phức tạp của nội dung và chiến lược điều hướng của mô hình. Các mã thông báo suy luận điều hướng được tạo trong quá trình khám phá video được tính là **mã thông báo tư duy** (`thoughts_token_count`), trong khi các khung hình, âm thanh và bản chép lời được tải theo yêu cầu được tính là mã thông báo lời nhắc công cụ (`tool_use_prompt_token_count`). Xử lý bằng tác nhân thường sử dụng ít hơn đến 88% tổng số mã thông báo so với xử lý tĩnh đối với nội dung dài vì mô hình chỉ tải bản chép lời và/hoặc khung hình và/hoặc âm thanh cần thiết để trả lời lời nhắc (xem [hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=vi#video-token-usage)).
- **Độ phân giải của nội dung nghe nhìn**: Gemini 3 cho phép kiểm soát chi tiết quá trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.** Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ. Các tham số `media_resolution` và `media_processing` là độc lập: bạn có thể đặt cả hai tham số này trên cùng một phần của video.

Để biết thêm thông tin về cách tính mã thông báo, hãy xem hướng dẫn về [mã thông báo](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=vi).

- **Định dạng dấu thời gian**: Khi đề cập đến những khoảnh khắc cụ thể trong video trong câu lệnh, hãy sử dụng định dạng `MM:SS` (ví dụ: `01:15` cho 1 phút 15 giây).
- **Vị trí của câu lệnh**: Nếu kết hợp văn bản và một video, hãy đặt câu lệnh văn bản *sau* phần video trong mảng `contents`.
- **Thời gian chờ cho các yêu cầu dài**: Đối với những video cần thời gian xử lý kéo dài hoặc có suy luận đa bước phức tạp, hãy sử dụng tính năng truyền trực tuyến (`client.models.generate_content_stream`). Các yêu cầu đồng bộ, không truyền trực tuyến gặp phải tình trạng thử lại phụ trợ trong điều kiện có nhu cầu cao có thể vượt quá thời gian hiệu lực của kết nối hoặc mã thông báo xác thực, điều này có thể xuất hiện dưới dạng lỗi `401 Unauthorized` hoặc lỗi hết thời gian chờ không mong muốn. Tính năng truyền trực tuyến duy trì kết nối và hiển thị suy luận trung gian cũng như tiến trình gọi công cụ.

## Bước tiếp theo

- [Độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=vi): Kiểm soát độ phân giải của khung hình video để cân bằng chất lượng và mức sử dụng mã thông báo.
- [Mã thông báo](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=vi): Tìm hiểu cách nội dung video được mã hoá ở cả chế độ xử lý tĩnh và chế độ xử lý dựa trên tác nhân.
- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=vi#system-instructions): Hướng dẫn hệ thống giúp bạn điều hướng hành vi của mô hình dựa trên nhu cầu và trường hợp sử dụng cụ thể của bạn.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý tệp để sử dụng với Gemini.
- [Chiến lược đặt câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide): Gemini API hỗ trợ đặt câu lệnh bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là đặt câu lệnh đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Hậu xử lý và đánh giá của con người là những yếu tố cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-18 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-18 UTC."],[],[]]
