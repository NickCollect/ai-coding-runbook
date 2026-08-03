---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=th
fetched_at: 2026-08-03T04:31:24.417682+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e27\u0e34\u0e14\u0e35\u0e42\u0e2d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจวิดีโอ

> ดูข้อมูลเกี่ยวกับการสร้างวิดีโอได้ที่คู่มือ [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)

โมเดล Gemini สามารถประมวลผลวิดีโอ ซึ่งช่วยให้นักพัฒนาแอปสามารถใช้กรณีการใช้งานที่ล้ำสมัยมากมายซึ่งในอดีตต้องใช้โมเดลเฉพาะโดเมน
ความสามารถด้านการมองเห็นของ Gemini บางอย่าง ได้แก่ ความสามารถในการอธิบาย แบ่งส่วน และดึงข้อมูลจากวิดีโอ ตอบคำถามเกี่ยวกับเนื้อหาวิดีโอ และอ้างอิงการประทับเวลาที่เฉพาะเจาะจงภายในวิดีโอ

คุณสามารถระบุวิดีโอเป็นอินพุตให้กับ Gemini ได้ด้วยวิธีต่อไปนี้

| วิธีการป้อนข้อมูล | ขนาดสูงสุด | กรณีการใช้งานที่แนะนำ |
| --- | --- | --- |
| [File API](#upload-video) | 20GB (แบบชำระเงิน) / 2GB (ฟรี) | ไฟล์ขนาดใหญ่ (100MB ขึ้นไป), วิดีโอแบบยาว (10 นาทีขึ้นไป), ไฟล์ที่ใช้ซ้ำได้ |
| [การลงทะเบียน Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th#registration) | 2GB (ต่อไฟล์ ไม่จำกัดพื้นที่เก็บข้อมูล) | ไฟล์ขนาดใหญ่ (100MB ขึ้นไป), วิดีโอแบบยาว (10 นาทีขึ้นไป), ไฟล์ที่คงอยู่และใช้ซ้ำได้ |
| [ข้อมูลแบบอินไลน์](#inline-video) | < 100MB | ไฟล์ขนาดเล็ก (<100MB), ระยะเวลาสั้น (<1 นาที), อินพุตแบบครั้งเดียว |
| [URL ของ YouTube](#youtube) | ไม่มี | วิดีโอ YouTube สาธารณะ |

> **หมายเหตุ:** เราขอแนะนำให้ใช้ [File API](#upload-video) สำหรับกรณีการใช้งานส่วนใหญ่ โดยเฉพาะอย่างยิ่งสำหรับไฟล์ที่มีขนาดใหญ่กว่า 100MB หรือเมื่อคุณต้องการใช้ไฟล์ซ้ำในคำขอหลายรายการ

[ดูข้อมูลเกี่ยวกับวิธีการป้อนข้อมูลไฟล์อื่นๆ เช่น การใช้ URL ภายนอกหรือไฟล์ที่จัดเก็บไว้ใน Google Cloud ได้ที่คู่มือวิธีการป้อนข้อมูลไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

### อัปโหลดไฟล์วิดีโอ

โค้ดต่อไปนี้จะดาวน์โหลดวิดีโอตัวอย่าง อัปโหลดโดยใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th),
รอให้ระบบประมวลผล และใช้ข้อมูลอ้างอิงไฟล์ที่อัปโหลดเพื่อ
สรุปวิดีโอ

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

ใช้ Files API เสมอเมื่อขนาดคำขอทั้งหมด (รวมถึงไฟล์ พรอมต์ข้อความ คำแนะนำของระบบ ฯลฯ) ใหญ่กว่า 20 MB ความยาววิดีโอมีความสำคัญ หรือหากคุณต้องการใช้วิดีโอเดียวกันในพรอมต์หลายรายการ
File API ยอมรับรูปแบบไฟล์วิดีโอโดยตรง

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับไฟล์สื่อได้ที่
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)

### ส่งข้อมูลวิดีโอแบบอินไลน์

คุณสามารถส่งวิดีโอขนาดเล็กโดยตรงในคำขอแทนการอัปโหลดไฟล์วิดีโอโดยใช้ File API วิธีนี้เหมาะสำหรับวิดีโอสั้นๆ ที่มีขนาดคำขอทั้งหมดไม่เกิน 20MB

ตัวอย่างการส่งข้อมูลวิดีโอแบบอินไลน์มีดังนี้

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### ส่ง URL ของ YouTube

คุณสามารถส่ง URL ของ YouTube ไปยัง Gemini API ได้โดยตรงเป็นส่วนหนึ่งของคำขอตามวิธีต่อไปนี้

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**ข้อจำกัด**

- สำหรับแพ็กเกจฟรี คุณจะอัปโหลดวิดีโอ YouTube ได้ไม่เกิน 8 ชั่วโมงต่อวัน
- สำหรับแพ็กเกจแบบชำระเงิน จะไม่มีการจำกัดตามความยาววิดีโอ
- สำหรับโมเดลก่อน Gemini 2.5 คุณจะอัปโหลดวิดีโอได้เพียง 1 รายการต่อคำขอ สำหรับโมเดล Gemini 2.5 และรุ่นที่ใหม่กว่า คุณจะอัปโหลดวิดีโอได้สูงสุด 10 รายการต่อคำขอ
- คุณอัปโหลดได้เฉพาะวิดีโอสาธารณะ (ไม่ใช่ส่วนตัวหรือวิดีโอที่ไม่เป็นสาธารณะ)

## อ้างอิงการประทับเวลาในเนื้อหา

คุณสามารถถามคำถามเกี่ยวกับจุดที่เฉพาะเจาะจงในวิดีโอได้โดยใช้การประทับเวลาในรูปแบบ `MM:SS`

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## ดึงข้อมูลเชิงลึกโดยละเอียดจากวิดีโอ

โมเดล Gemini มีความสามารถอันทรงพลังในการทำความเข้าใจเนื้อหาวิดีโอโดยการประมวลผลข้อมูลจากทั้งสตรีม**เสียงและภาพ** ซึ่งช่วยให้คุณดึงรายละเอียดต่างๆ มากมาย รวมถึงสร้างคำอธิบายเกี่ยวกับสิ่งที่เกิดขึ้นในวิดีโอและตอบคำถามเกี่ยวกับเนื้อหาของวิดีโอ

สำหรับคำอธิบายภาพ โมเดลจะสุ่มตัวอย่างวิดีโอที่อัตรา **1 เฟรมต่อวินาที** (FPS) อัตราการสุ่มตัวอย่างเริ่มต้นนี้เหมาะกับเนื้อหาส่วนใหญ่ แต่โปรดทราบว่าอาจพลาดรายละเอียดในวิดีโอที่มีการเคลื่อนไหวอย่างรวดเร็วหรือมีการเปลี่ยนแปลงฉากอย่างรวดเร็ว

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## รูปแบบวิดีโอที่รองรับ

Gemini รองรับ MIME ประเภทรูปแบบวิดีโอต่อไปนี้

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## รายละเอียดทางเทคนิคเกี่ยวกับวิดีโอ

- **โมเดลและบริบทที่รองรับ**: Gemini ทุกรุ่นสามารถประมวลผลข้อมูลวิดีโอได้
  - โมเดลที่มีหน้าต่างบริบท 1 ล้านโทเค็นสามารถประมวลผลวิดีโอที่มีความยาวสูงสุด 1 ชั่วโมงที่ความละเอียดสื่อเริ่มต้น หรือ 3 ชั่วโมงที่ความละเอียดสื่อต่ำ
- **การประมวลผล File API**: เมื่อใช้ File API ระบบจะจัดเก็บวิดีโอที่ 1
  เฟรมต่อวินาที (FPS) และประมวลผลเสียงที่ 1Kbps (ช่องเดียว)
  ระบบจะเพิ่มการประทับเวลาทุกวินาที
  - อัตราเหล่านี้อาจมีการเปลี่ยนแปลงในอนาคตเพื่อปรับปรุงการอนุมาน
- **การคำนวณโทเค็น**: ระบบจะแปลงวิดีโอแต่ละวินาทีเป็นโทเค็นดังนี้
  - เฟรมแต่ละเฟรม (สุ่มตัวอย่างที่ 1 FPS):
    - หากตั้งค่า `media_resolution` เป็นต่ำ ระบบจะแปลงเฟรมเป็นโทเค็นที่ 66 โทเค็นต่อเฟรม
    - ไม่เช่นนั้น ระบบจะแปลงเฟรมเป็นโทเค็นที่ 258 โทเค็นต่อเฟรม
  - เสียง: 32 โทเค็นต่อวินาที
  - รวมข้อมูลเมตาด้วย
  - รวม: ประมาณ 300 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อเริ่มต้น หรือ 100 โทเค็นต่อวินาทีของวิดีโอที่ความละเอียดสื่อต่ำ
- **ความละเอียดสื่อ**: Gemini 3 ขอแนะนำการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลการมองเห็นแบบมัลติโมดัล
  ด้วยพารามิเตอร์ `media_resolution` พารามิเตอร์ `media_resolution` จะกำหนด**จำนวนโทเค็นสูงสุดที่จัดสรรต่อรูปภาพอินพุตหรือเฟรมวิดีโอ**
  ความละเอียดที่สูงขึ้นจะช่วยเพิ่มความสามารถของโมเดลในการอ่านข้อความขนาดเล็กหรือระบุรายละเอียดเล็กๆ แต่จะเพิ่มการใช้โทเค็นและเวลาในการตอบสนอง

  ดูรายละเอียดเพิ่มเติมเกี่ยวกับการคำนวณโทเค็นได้ที่คู่มือ[โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)
- **รูปแบบการประทับเวลา**: เมื่ออ้างอิงถึงช่วงเวลาที่เฉพาะเจาะจงในวิดีโอภายในพรอมต์ ให้ใช้รูปแบบ `MM:SS` (เช่น `01:15` สำหรับ 1 นาที 15 วินาที)
- **แนวทางปฏิบัติแนะนำ**:

  - ใช้เพียงวิดีโอเดียวต่อคำขอพรอมต์เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด
  - หากรวมข้อความและวิดีโอเดียว ให้วางพรอมต์ข้อความ *หลัง* ส่วนวิดีโอในอาร์เรย์ `input`
  - โปรดทราบว่าลำดับการทำงานที่รวดเร็วอาจสูญเสียรายละเอียดเนื่องจากอัตราการสุ่มตัวอย่าง 1 FPS พิจารณาชะลอคลิปดังกล่าวหากจำเป็น

## ขั้นตอนถัดไป

คู่มือนี้แสดงวิธีอัปโหลดไฟล์วิดีโอและสร้างเอาต์พุตข้อความจากอินพุตวิดีโอ ดูข้อมูลเพิ่มเติมได้จากแหล่งข้อมูลต่อไปนี้

- [คำแนะนำของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำของระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตาม
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

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
