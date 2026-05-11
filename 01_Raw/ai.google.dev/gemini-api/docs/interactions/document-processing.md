---
source_url: https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th
fetched_at: 2026-05-11T04:58:38.835823+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจเอกสาร

โมเดล Gemini สามารถประมวลผลเอกสารในรูปแบบ PDF โดยใช้
Vision ดั้งเดิมเพื่อทำความเข้าใจบริบทของเอกสารทั้งฉบับ ซึ่งจะช่วยให้ Gemini ทำสิ่งต่อไปนี้ได้
นอกเหนือจากการดึงข้อความ

- วิเคราะห์และตีความเนื้อหา รวมถึงข้อความ รูปภาพ แผนภาพ
  แผนภูมิ และตาราง แม้ในเอกสารขนาดยาวที่มีมากถึง 1,000 หน้า
- ดึงข้อมูลลงในรูปแบบ[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=th)
- สรุปและตอบคำถามโดยอิงตามทั้งองค์ประกอบภาพและข้อความ
  ในเอกสาร
- ถอดเสียงเนื้อหาเอกสาร (เช่น เป็น HTML) โดยคงเลย์เอาต์และการจัดรูปแบบไว้เพื่อใช้ในแอปพลิเคชันดาวน์สตรีม

นอกจากนี้ คุณยังส่งเอกสารที่ไม่ใช่ PDF ในลักษณะเดียวกันได้ แต่ Gemini จะเห็นเอกสารเหล่านั้นเป็นข้อความปกติ ซึ่งจะไม่มีบริบท เช่น แผนภูมิหรือการจัดรูปแบบ

## การส่งข้อมูล PDF แบบอินไลน์

คุณส่งข้อมูล PDF แบบอินไลน์ในคำขอได้ วิธีนี้เหมาะที่สุดสำหรับเอกสารขนาดเล็กหรือการประมวลผลชั่วคราวซึ่งคุณไม่จำเป็นต้องอ้างอิงไฟล์ในคำขอที่ตามมา เราขอแนะนำให้ใช้
[Files API](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th#large-pdfs)
สำหรับเอกสารขนาดใหญ่ที่คุณต้องอ้างอิงในการโต้ตอบแบบหลายรอบเพื่อ
ปรับปรุงเวลาในการตอบสนองของคำขอและลดการใช้แบนด์วิดท์

ตัวอย่างต่อไปนี้แสดงวิธีส่งข้อมูล PDF ในบรรทัด

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/document.pdf', 'rb') as f:
    pdf_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "document",
            "data": base64.b64encode(pdf_bytes).decode('utf-8'),
            "mime_type": "application/pdf"
        },
        {"type": "text", "text": "Summarize this document"}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    const pdfData = fs.readFileSync("path/to/document.pdf", {
        encoding: "base64"
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                data: pdfData,
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

### REST

```
PDF_PATH="path/to/document.pdf"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {
        "type": "document",
        "data": "'$(base64 $B64FLAGS $PDF_PATH)'",
        "mime_type": "application/pdf"
      },
      {"type": "text", "text": "Summarize this document"}
    ]
  }'
```

นอกจากนี้ คุณยังอัปโหลดไฟล์ PDF ในเครื่องเพื่อประมวลผลได้ด้วย โดยทำดังนี้

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="file.pdf")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const uploadedFile = await ai.files.upload({
        file: "file.pdf",
        config: { mime_type: "application/pdf" }
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                uri: uploadedFile.uri,
                mime_type: uploadedFile.mime_type
            }
        ]
    });
    console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

## การอัปโหลด PDF โดยใช้ Files API

เราขอแนะนำให้คุณใช้ Files API สำหรับไฟล์ขนาดใหญ่หรือเมื่อต้องการนำเอกสารกลับมาใช้ซ้ำในคำขอหลายรายการ ซึ่งจะช่วยปรับปรุงเวลาในการตอบสนองของคำขอและลดการใช้แบนด์วิดท์ด้วยการแยกการอัปโหลดไฟล์ออกจากคำขอโมเดล

### PDF ขนาดใหญ่จาก URL

ใช้ File API เพื่อลดความซับซ้อนในการอัปโหลดและประมวลผลไฟล์ PDF ขนาดใหญ่จาก URL โดยทำดังนี้

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://arxiv.org/pdf/2312.11805"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": sample_doc.uri, "mime_type": sample_doc.mime_type},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

    const pdfBuffer = await fetch("https://arxiv.org/pdf/2312.11805")
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3-flash-preview',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.steps.at(-1).content[0].text);

}

main();
```

### REST

```
PDF_PATH="https://arxiv.org/pdf/2312.11805"
DISPLAY_NAME="Gemini_paper"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
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

file_uri=$(jq -r ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Create payload JSON file for safety
cat << EOF > payload.json
{
  "model": "gemini-3-flash-preview",
  "input": [
    {"type": "text", "text": "${PROMPT}"},
    {"type": "document", "uri": "${file_uri}", "mime_type": "application/pdf"}
  ]
}
EOF

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm "${DISPLAY_NAME}.pdf"
rm payload.json
```

### PDF ขนาดใหญ่ที่จัดเก็บไว้ในเครื่อง

### Python

```
from google import genai
import pathlib

client = genai.Client()

# Upload the PDF using the File API
file_path = pathlib.Path('large_file.pdf')
sample_file = client.files.upload(
    file=file_path,
)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": sample_file.uri, "mime_type": sample_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const file = await ai.files.upload({
        file: 'path-to-localfile.pdf',
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3-flash-preview',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.steps.at(-1).content[0].text);

}

main();
```

### REST

```
PDF_PATH="path/to/large_file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "document", "uri": '$file_uri', "mime_type": "application/pdf"},
        {"type": "text", "text": "Can you add a few more lines to this poem?"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json
```

คุณสามารถยืนยันว่า API จัดเก็บไฟล์ที่อัปโหลดเรียบร้อยแล้วและรับข้อมูลเมตาของไฟล์ได้โดยการเรียกใช้ [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=th) มีเพียง `name`
(และ `uri`) เท่านั้นที่ไม่ซ้ำกัน

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.pdf')
fpath.write_text('hello')

file = client.files.upload(file='example.pdf')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### REST

```
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl "https://generativelanguage.googleapis.com/v1beta/$name?key=$GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## ส่ง PDF หลายไฟล์

Gemini API สามารถประมวลผลเอกสาร PDF หลายรายการ (สูงสุด 1, 000 หน้า)
ในคำขอเดียวได้ ตราบใดที่ขนาดรวมของเอกสารและพรอมต์ข้อความ
ยังคงอยู่ภายในหน้าต่างบริบทของโมเดล

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

# Retrieve and upload both PDFs using the File API
doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": sample_pdf_1.uri, "mime_type": sample_pdf_1.mime_type},
        {"type": "document", "uri": sample_pdf_2.uri, "mime_type": sample_pdf_2.mime_type},
        {"type": "text", "text": prompt}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1");
    const file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2");

    const interaction = await ai.interactions.create({
        model: 'gemini-3-flash-preview',
        input: [
            { type: "document", uri: file1.uri, mime_type: file1.mime_type },
            { type: "document", uri: file2.uri, mime_type: file2.mime_type },
            { type: "text", text: "What is the difference between each of the main benchmarks between these two papers? Output these in a table." }
        ],
    });

    console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

### REST

```
DOC_URL_1="https://arxiv.org/pdf/2312.11805"
DOC_URL_2="https://arxiv.org/pdf/2403.05530"
DISPLAY_NAME_1="Gemini_paper"
DISPLAY_NAME_2="Gemini_1.5_paper"
PROMPT="What is the difference between each of the main benchmarks between these two papers? Output these in a table."

# Function to download and upload a PDF
upload_pdf() {
  local doc_url="$1"
  local display_name="$2"

  echo "Downloading ${display_name} from ${doc_url}..." >&2
  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}" 2> /dev/null

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}" >&2
  echo "NUM_BYTES: ${NUM_BYTES}" >&2

  local tmp_header_file="upload-header-${display_name}.tmp"

  # Initial resumable request
  # Using GEMINI_API_KEY instead of GOOGLE_API_KEY
  curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  echo "Upload URL for ${display_name}: ${upload_url}" >&2

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

  local file_uri=$(jq -r ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}" >&2

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Create payload JSON file for safety
cat << EOF > payload_multi.json
{
  "model": "gemini-3-flash-preview",
  "input": [
    {"type": "document", "uri": "${file_uri_1}", "mime_type": "application/pdf"},
    {"type": "document", "uri": "${file_uri_2}", "mime_type": "application/pdf"},
    {"type": "text", "text": "${PROMPT}"}
  ]
}
EOF

# Now create an interaction using both files
# Using GEMINI_API_KEY instead of GOOGLE_API_KEY
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload_multi.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm payload_multi.json
rm "file_info_${DISPLAY_NAME_1}.json"
rm "file_info_${DISPLAY_NAME_2}.json"
```

## รายละเอียดทางเทคนิค

Gemini รองรับไฟล์ PDF ที่มีขนาดไม่เกิน 50 MB หรือ 1,000 หน้า ขีดจํากัดนี้มีผล
ทั้งกับข้อมูลแบบอินไลน์และการอัปโหลดผ่าน Files API หน้าเอกสารแต่ละหน้าจะเท่ากับโทเค็น 258 รายการ

แม้จะไม่มีขีดจำกัดที่เฉพาะเจาะจงสำหรับจำนวนพิกเซลในเอกสารนอกเหนือจาก[หน้าต่างบริบท](https://ai.google.dev/gemini-api/docs/long-context?hl=th)ของโมเดล แต่ระบบจะปรับขนาดหน้าเว็บที่ใหญ่ขึ้นให้มีความละเอียดสูงสุด 3072 x 3072 โดยยังคงอัตราส่วนเดิมไว้ ส่วนหน้าเว็บที่เล็กลงจะได้รับการปรับขนาดเป็น 768 x 768 พิกเซล ไม่มีการลดต้นทุนสำหรับหน้าเว็บที่มีขนาดเล็กลงนอกเหนือจากแบนด์วิดท์ หรือการปรับปรุงประสิทธิภาพสำหรับหน้าเว็บที่มีความละเอียดสูงขึ้น

### โมเดล Gemini 3

Gemini 3 มีการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลวิสัยทัศน์แบบมัลติโมดอลด้วยพารามิเตอร์ `media_resolution`
ตอนนี้คุณสามารถตั้งค่าความละเอียดเป็นต่ำ ปานกลาง หรือสูงสำหรับสื่อแต่ละส่วนได้แล้ว การเพิ่มฟีเจอร์นี้จะอัปเดตการประมวลผลเอกสาร PDF ดังนี้

1. **การรวมข้อความดั้งเดิม:** ระบบจะดึงข้อความที่ฝังอยู่ใน PDF
   และส่งให้โมเดล
2. **การเรียกเก็บเงินและการรายงานโทเค็น:**
   - ระบบ**ไม่เรียกเก็บเงิน**สำหรับโทเค็นที่มาจาก**ข้อความดั้งเดิม**ที่ดึงออกมาใน PDF
   - ในส่วน `usage_metadata` ของการตอบกลับของ API ตอนนี้ระบบจะนับโทเค็นที่สร้างขึ้น
     จากการประมวลผลหน้า PDF (เป็นรูปภาพ) ภายใต้รูปแบบ `IMAGE`
     ไม่ใช่รูปแบบ `DOCUMENT` แยกต่างหากเหมือนในบางเวอร์ชันก่อนหน้า

### ประเภทเอกสาร

ในทางเทคนิค คุณสามารถส่ง MIME ประเภทอื่นๆ สำหรับการทำความเข้าใจเอกสารได้ เช่น TXT, Markdown, HTML, XML ฯลฯ อย่างไรก็ตาม Document Vision ***จะเข้าใจเฉพาะ PDF เท่านั้น*** ส่วนไฟล์ประเภทอื่นๆ จะได้รับการแยกเป็นข้อความธรรมดา และโมเดล
จะไม่สามารถตีความสิ่งที่เห็นในการแสดงผลไฟล์เหล่านั้นได้ รายละเอียดของประเภทไฟล์ เช่น แผนภูมิ ไดอะแกรม แท็ก HTML การจัดรูปแบบ Markdown ฯลฯ จะหายไป

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ ได้ที่คู่มือ[วิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=th)

### แนวทางปฏิบัติแนะนำ

เพื่อผลลัพธ์ที่ดีที่สุด ให้ทำดังนี้

- หมุนหน้าให้เป็นการวางแนวที่ถูกต้องก่อนอัปโหลด
- หลีกเลี่ยงหน้าเว็บที่เบลอ
- หากใช้หน้าเดียว ให้วางพรอมต์ข้อความไว้หลังหน้า

## ขั้นตอนถัดไป

ดูข้อมูลเพิ่มเติมได้ที่แหล่งข้อมูลต่อไปนี้

- [กลยุทธ์การเขียนพรอมต์ด้วยไฟล์](https://ai.google.dev/gemini-api/docs/interactions/files?hl=th#prompt-guide): Gemini API รองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ ซึ่งเรียกอีกอย่างว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th#system-instructions):
  คำสั่งของระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตามความต้องการและกรณีการใช้งานเฉพาะของคุณได้

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-09 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-09 UTC"],[],[]]
