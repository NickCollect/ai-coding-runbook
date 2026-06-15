---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=th
fetched_at: 2026-06-15T06:22:20.296915+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจวิดีโอ

> ดูข้อมูลเกี่ยวกับการสร้างวิดีโอได้ที่คู่มือ [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)

โมเดล Gemini สามารถประมวลผลวิดีโอ ซึ่งช่วยให้เกิดกรณีการใช้งานที่ล้ำสมัยสำหรับนักพัฒนาซอฟต์แวร์มากมาย ซึ่งในอดีตจะต้องใช้โมเดลเฉพาะโดเมน
ความสามารถด้านวิชันซิสเต็มบางอย่างของ Gemini ได้แก่ ความสามารถในการอธิบาย แบ่งส่วน และดึงข้อมูลจากวิดีโอ ตอบคำถามเกี่ยวกับเนื้อหาวิดีโอ และอ้างอิงการประทับเวลาที่เฉพาะเจาะจงภายในวิดีโอ

คุณสามารถระบุวิดีโอเป็นอินพุตให้กับ Gemini ได้ด้วยวิธีต่อไปนี้

| วิธีการป้อนข้อมูล | ขนาดสูงสุด | กรณีการใช้งานที่แนะนำ |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (แบบชำระเงิน) / 2 GB (ฟรี) | ไฟล์ขนาดใหญ่ (มากกว่า 100 MB) วิดีโอแบบยาว (มากกว่า 10 นาที) ไฟล์ที่ใช้ซ้ำได้ |
| [การลงทะเบียน Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th#registration) | 2 GB (ต่อไฟล์ ไม่จำกัดพื้นที่เก็บข้อมูล) | ไฟล์ขนาดใหญ่ (มากกว่า 100 MB) วิดีโอแบบยาว (มากกว่า 10 นาที) ไฟล์ที่คงอยู่และใช้ซ้ำได้ |
| [ข้อมูลแบบอินไลน์](#inline-video) | น้อยกว่า 100 MB | ไฟล์ขนาดเล็ก (น้อยกว่า 100 MB) ระยะเวลาสั้น (น้อยกว่า 1 นาที) อินพุตแบบครั้งเดียว |
| [URL ของ YouTube](#youtube) | ไม่มี | วิดีโอ YouTube สาธารณะ |

> **หมายเหตุ:** เราขอแนะนำให้ใช้ [File API](#upload-video) สำหรับกรณีการใช้งานส่วนใหญ่ โดยเฉพาะอย่างยิ่งสำหรับไฟล์ที่มีขนาดใหญ่กว่า 100 MB หรือเมื่อคุณต้องการใช้ไฟล์ซ้ำในคำขอหลายรายการ

[ดูข้อมูลเกี่ยวกับวิธีการป้อนข้อมูลไฟล์อื่นๆ เช่น การใช้ URL ภายนอกหรือไฟล์ที่จัดเก็บไว้ใน Google Cloud ได้ที่คู่มือวิธีการป้อนข้อมูลไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

### อัปโหลดไฟล์วิดีโอ

โค้ดต่อไปนี้จะดาวน์โหลดวิดีโอตัวอย่าง อัปโหลดโดยใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th),
รอให้ระบบประมวลผล และใช้ข้อมูลอ้างอิงไฟล์ที่อัปโหลดเพื่อ
สรุปวิดีโอ

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.5-flash",
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
    "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

ใช้ Files API เสมอเมื่อขนาดคำขอทั้งหมด (รวมถึงไฟล์ พรอมต์ข้อความ คำแนะนำของระบบ ฯลฯ) ใหญ่กว่า 20 MB วิดีโอมีความยาวมาก หรือหากคุณต้องการใช้วิดีโอเดียวกันในพรอมต์หลายรายการ
File API ยอมรับรูปแบบไฟล์วิดีโอโดยตรง

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับไฟล์สื่อได้ที่
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

### ส่งข้อมูลวิดีโอแบบอินไลน์

คุณสามารถส่งวิดีโอขนาดเล็กโดยตรงในคำขอไปยัง `generateContent` แทนการอัปโหลดไฟล์วิดีโอโดยใช้ File API วิธีนี้เหมาะสำหรับวิดีโอสั้นๆ ที่มีขนาดคำขอทั้งหมดไม่เกิน 20 MB

ตัวอย่างการส่งข้อมูลวิดีโอแบบอินไลน์มีดังนี้

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### ส่ง URL ของ YouTube

คุณสามารถส่ง URL ของ YouTube ไปยัง Gemini API ได้โดยตรงเป็นส่วนหนึ่งของคำขอตามวิธีต่อไปนี้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

**ข้อจำกัด**

- สำหรับแพ็กเกจฟรี คุณจะอัปโหลดวิดีโอ YouTube ได้ไม่เกิน 8 ชั่วโมงต่อวัน
- สำหรับแพ็กเกจแบบชำระเงิน จะไม่มีการจำกัดตามความยาววิดีโอ
- สำหรับโมเดลก่อน Gemini 2.5 คุณจะอัปโหลดวิดีโอได้เพียง 1 รายการต่อคำขอ สำหรับโมเดล Gemini 2.5 และรุ่นที่ใหม่กว่า คุณจะอัปโหลดวิดีโอได้สูงสุด 10 รายการต่อคำขอ
- คุณอัปโหลดได้เฉพาะวิดีโอสาธารณะ (ไม่ใช่ส่วนตัวหรือวิดีโอที่ไม่เป็นสาธารณะ)

## ใช้การแคชบริบทสำหรับวิดีโอแบบยาว

สำหรับวิดีโอที่มีความยาวมากกว่า 10 นาที หรือเมื่อคุณวางแผนที่จะส่งคำขอหลายรายการ
ไปยังไฟล์วิดีโอเดียวกัน ให้ใช้ [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th) เพื่อ
ลดค่าใช้จ่ายและปรับปรุงเวลาในการตอบสนอง การแคชบริบทช่วยให้คุณประมวลผลวิดีโอได้เพียงครั้งเดียวและใช้โทเค็นซ้ำสำหรับการค้นหาในภายหลัง ซึ่งเหมาะอย่างยิ่งสำหรับเซสชันการแชทหรือการวิเคราะห์เนื้อหาแบบยาวซ้ำๆ

## อ้างอิงการประทับเวลาในเนื้อหา

คุณสามารถถามคำถามเกี่ยวกับจุดที่เฉพาะเจาะจงในวิดีโอได้โดยใช้การประทับเวลาในรูปแบบ `MM:SS`

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

## ดึงข้อมูลเชิงลึกโดยละเอียดจากวิดีโอ

โมเดล Gemini มีความสามารถอันทรงพลังในการทำความเข้าใจเนื้อหาวิดีโอโดยการประมวลผลข้อมูลจากทั้งสตรีม**เสียงและภาพ** ซึ่งช่วยให้คุณดึงรายละเอียดต่างๆ มากมาย รวมถึงการสร้างคำอธิบายเกี่ยวกับสิ่งที่เกิดขึ้นในวิดีโอและการตอบคำถามเกี่ยวกับเนื้อหา

สำหรับคำอธิบายภาพ โมเดลจะสุ่มตัวอย่างวิดีโอที่อัตรา **1 เฟรมต่อวินาที** (FPS) อัตราการสุ่มตัวอย่างเริ่มต้นนี้เหมาะกับเนื้อหาส่วนใหญ่ แต่โปรดทราบว่าอาจพลาดรายละเอียดในวิดีโอที่มีการเคลื่อนไหวอย่างรวดเร็วหรือการเปลี่ยนแปลงฉากอย่างรวดเร็ว
สำหรับเนื้อหาที่มีการเคลื่อนไหวสูงเช่นนี้ ให้ลอง[ตั้งค่าอัตราเฟรมที่กำหนดเอง](#custom-frame-rate)

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

## ปรับแต่งการประมวลผลวิดีโอ

คุณสามารถปรับแต่งการประมวลผลวิดีโอใน Gemini API ได้โดยการตั้งค่าช่วงการตัดหรือระบุการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเอง

 

### ตั้งค่าช่วงการตัด

คุณสามารถตัดวิดีโอได้โดยระบุ `videoMetadata` พร้อมออฟเซ็ตเริ่มต้นและสิ้นสุด

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
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
const model = 'gemini-3.5-flash';

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

### ตั้งค่าอัตราเฟรมที่กำหนดเอง

คุณสามารถตั้งค่าการสุ่มตัวอย่างอัตราเฟรมที่กำหนดเองได้โดยส่งอาร์กิวเมนต์ `fps` ไปยัง `videoMetadata`

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
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

โดยค่าเริ่มต้น ระบบจะสุ่มตัวอย่าง 1 เฟรมต่อวินาที (FPS) จากวิดีโอ คุณอาจต้องการตั้งค่า FPS ต่ำ (< 1) สำหรับวิดีโอแบบยาว ซึ่งมีประโยชน์อย่างยิ่งสำหรับวิดีโอที่ส่วนใหญ่เป็นภาพนิ่ง (เช่น การบรรยาย) ใช้ FPS ที่สูงขึ้นสำหรับวิดีโอที่ต้องมีการวิเคราะห์ตามเวลาแบบละเอียด เช่น การทำความเข้าใจการกระทำที่รวดเร็วหรือการติดตามการเคลื่อนไหวความเร็วสูง

## รูปแบบวิดีโอที่รองรับ

Gemini รองรับ MIME ประเภทรูปแบบวิดีโอต่อไปนี้

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## รายละเอียดด้านเทคนิคเกี่ยวกับวิดีโอ

- **โมเดลและบริบทที่รองรับ**: Gemini ทุกรุ่นสามารถประมวลผลข้อมูลวิดีโอได้
  - โมเดลที่มีหน้าต่างบริบท 1 ล้านโทเค็นสามารถประมวลผลวิดีโอที่มีความยาวสูงสุด 1 ชั่วโมงที่ความละเอียดสื่อเริ่มต้น หรือ 3 ชั่วโมงที่ความละเอียดสื่อต่ำ
- **การประมวลผล File API**: เมื่อใช้ File API ระบบจะจัดเก็บวิดีโอที่ 1
  เฟรมต่อวินาที (FPS) และประมวลผลเสียงที่ 1 Kbps (ช่องเดียว)
  ระบบจะเพิ่มการประทับเวลาทุกวินาที
  - อัตราเหล่านี้อาจมีการเปลี่ยนแปลงในอนาคตเพื่อปรับปรุงการอนุมาน
  - คุณสามารถลบล้างอัตราการสุ่มตัวอย่าง 1 FPS ได้โดยการ[ตั้งค่าอัตราเฟรมที่กำหนดเอง](#custom-frame-rate)
- **การคำนวณโทเค็น**: ระบบจะแปลงวิดีโอแต่ละวินาทีเป็นโทเค็นดังนี้
  - เฟรมแต่ละเฟรม (สุ่มตัวอย่างที่ 1 FPS):
    - หากตั้งค่า [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=th#MediaResolution) เป็นต่ำ ระบบจะแปลงเฟรมเป็นโทเค็นที่ 66 โทเค็นต่อเฟรม
    - ไม่เช่นนั้น ระบบจะแปลงเฟรมเป็นโทเค็นที่ 258 โทเค็นต่อเฟรม
  - เสียง: 32 โทเค็นต่อวินาที
  - รวมข้อมูลเมตาด้วย
  - รวม: ประมาณ 300 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อเริ่มต้น หรือ 100 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อต่ำ
- **ความละเอียดสื่อ**: Gemini 3 นำเสนอการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลวิชันซิสเต็มแบบมัลติโมดัล
  ด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**
  ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง

  ดูรายละเอียดเพิ่มเติมเกี่ยวกับพารามิเตอร์และวิธีที่พารามิเตอร์นี้อาจส่งผลต่อการคำนวณโทเค็น
  ได้ที่คู่มือ[ความละเอียดสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th)
- **รูปแบบการประทับเวลา**: เมื่ออ้างอิงถึงช่วงเวลาที่เฉพาะเจาะจงในวิดีโอภายในพรอมต์ ให้ใช้รูปแบบ `MM:SS` (เช่น `01:15` สำหรับ 1 นาที 15 วินาที)
- **แนวทางปฏิบัติแนะนำ**:

  - ใช้เพียงวิดีโอเดียวต่อคำขอพรอมต์เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด
  - หากรวมข้อความและวิดีโอเดียว ให้วางพรอมต์ข้อความ *หลัง* ส่วนวิดีโอในอาร์เรย์ `contents`
  - โปรดทราบว่าลำดับการกระทำที่รวดเร็วอาจสูญเสียรายละเอียดเนื่องจากอัตราการสุ่มตัวอย่าง 1 FPS ให้ลองชะลอคลิปดังกล่าวหากจำเป็น

## ขั้นตอนถัดไป

คู่มือนี้แสดงวิธีอัปโหลดไฟล์วิดีโอและสร้างเอาต์พุตข้อความจากอินพุตวิดีโอ ดูข้อมูลเพิ่มเติมได้จากแหล่งข้อมูลต่อไปนี้

- [คำแนะนำของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำของระบบช่วยให้คุณควบคุมลักษณะการทำงานของโมเดลตาม
  ความต้องการและกรณีการใช้งานที่เฉพาะเจาะจง
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): ดูข้อมูลเพิ่มเติมเกี่ยวกับการอัปโหลดและจัดการ
  ไฟล์เพื่อใช้กับ Gemini
- [กลยุทธ์การเขียนพรอมต์ไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini API รองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ หรือที่เรียกว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำด้านความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=th): บางครั้งโมเดล Generative
  AI จะสร้างเอาต์พุตที่ไม่คาดคิด เช่น เอาต์พุตที่ไม่ถูกต้อง
  มีอคติ หรือไม่เหมาะสม การประมวลผลภายหลังและการประเมินโดยเจ้าหน้าที่เป็นสิ่งสำคัญในการ
  จำกัดความเสี่ยงที่จะเกิดอันตรายจากเอาต์พุตดังกล่าว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
