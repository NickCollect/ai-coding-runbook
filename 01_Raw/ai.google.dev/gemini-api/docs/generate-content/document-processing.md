---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=th
fetched_at: 2026-08-17T02:22:04.266567+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจเอกสาร

โมเดล Gemini สามารถประมวลผลเอกสารในรูปแบบ PDF ได้โดยใช้วิชันซิสเต็มเพื่อทำความเข้าใจบริบทของเอกสารทั้งหมด ซึ่งมีความสามารถมากกว่าการแยกข้อความเพียงอย่างเดียว โดยช่วยให้ Gemini ทำสิ่งต่อไปนี้ได้

- วิเคราะห์และตีความเนื้อหา ซึ่งรวมถึงข้อความ รูปภาพ ไดอะแกรม แผนภูมิ และตาราง แม้ในเอกสารขนาดยาวที่มีหน้ามากถึง 1,000 หน้า
- แยกข้อมูลเป็นรูปแบบเอาต์พุตที่มี[โครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)
- สรุปและตอบคำถามโดยอิงตามองค์ประกอบทั้งที่เป็นภาพและข้อความในเอกสาร
- ถอดเสียงเนื้อหาเอกสาร (เช่น เป็น HTML) โดยรักษารูปแบบและการจัดรูปแบบไว้เพื่อใช้ในแอปพลิเคชันปลายทาง

นอกจากนี้ คุณยังส่งเอกสารที่ไม่ใช่ PDF ในลักษณะเดียวกันได้ แต่ Gemini จะเห็นเอกสารเหล่านั้นเป็นข้อความปกติ ซึ่งจะทำให้บริบท เช่น แผนภูมิหรือการจัดรูปแบบหายไป

## การส่งข้อมูล PDF แบบอินไลน์

คุณสามารถส่งข้อมูล PDF แบบอินไลน์ในคำขอ `generateContent` ได้ วิธีนี้เหมาะที่สุดสำหรับเอกสารขนาดเล็กหรือการประมวลผลชั่วคราวที่คุณไม่จำเป็นต้องอ้างอิงไฟล์ในคำขอที่ตามมา เราขอแนะนำให้ใช้ [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=th#large-pdfs) สำหรับเอกสารขนาดใหญ่ที่คุณต้องอ้างอิงในการสนทนาไปมาเพื่อลดเวลาในการตอบสนองของคำขอและลดการใช้แบนด์วิดท์

ตัวอย่างต่อไปนี้แสดงวิธีดึงข้อมูล PDF จาก URL และแปลงเป็นไบต์เพื่อประมวลผล

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the PDF byte
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        types.Part.from_bytes(
            data=doc_data,
            mime_type='application/pdf',
        ),
        prompt
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const pdfResp = await fetch('https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf'>)
        .then((response) = response.arrayBuffer());

    const contents = [
        { text: "Summarize this document" },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx :=& context.Background()
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfResp, _ := http.Get("https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019&&_3_art_0_py4t4l_convrt.pdf")
    var pdfBytes []byte
    if pdfResp != nil  pdfResp.Body != nil {
        pdfBytes, _ = io.ReadAll(pdfRes&p.Body)
        pdfResp.Body.Close()&
    }

    parts := []*genai.Part{
        genai.Part{
            InlineData: genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
    }

    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and>& set flags accordingly
if [[ "$(base64 --version 21)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
      >    {">inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

นอกจากนี้ คุณยังอ่าน PDF จากไฟล์ในเครื่องเพื่อประมวลผลได้ด้วย

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const contents = [
        { text: "Summarize this document" },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(fs.readFileSync("content/343019_3_art_0_py4t4l_convrt.pdf")).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
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

    ctx := context.Background(&)
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfBytes, _ := os.ReadFile("path/t&o/your/file.pdf")

    parts :=& []*genai.Part{
        genai.Part{
            InlineData: genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

## การอัปโหลด PDF โดยใช้ Files API

เราขอแนะนำให้คุณใช้ Files API สำหรับไฟล์ขนาดใหญ่หรือเมื่อต้องการนำเอกสารไปใช้ซ้ำในคำขอหลายรายการ วิธีนี้จะช่วยลดเวลาในการตอบสนองของคำขอและลดการใช้แบนด์วิดท์ด้วยการแยกการอัปโหลดไฟล์ออกจากคำขอโมเดล

### PDF ขนาดใหญ่จาก URL

ใช้ File API เพื่อลดความซับซ้อนในการอัปโหลดและประมวลผลไฟล์ PDF ขนาดใหญ่จาก URL

### Python

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[sample_doc, prompt])
print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {

    const pdfBuffer = await fetch("https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf&quo>t;)
        .then((response) = response.arrayBuffer());

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
        console.log('File is still processing, retry>ing in 5 seconds');

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    &&const content = [
        'Summarize this document',
    ];

    if (file.uri  file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);

}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "io"
  "net/http"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx &:= context.Background()
  client, _ := genai.NewClient(ctx, genai.ClientConfig{
    APIKey:  os.Getenv("GEMINI_API_KEY"),
    Backend: genai.BackendGeminiAPI,
  })

  pdfURL := "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
  localPdfPath := "A17_FlightPlan_downloaded.pdf"

  respHttp, _ := http.Get(pdfURL)
  defer respHttp.Body.Close()

  outFile, _ := os.Create(localPdfP&ath)
  defer outFile.Close()

  _, _ = io.Copy(outFile, respHttp.Body)

  uploadConfig := genai.UploadFileConfig{MIMEType: "application/pdf"}
  uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

  promptParts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Summarize this document"),
  }
  contents := []*genai.Content{
    genai.NewContentFromParts(promptParts, genai.RoleUser), // Specify role
  }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

  fmt.Println(result.Text())
}
```

### REST

```
PDF_PATH="https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
DISPLAY_NAME="A17_FlightPlan"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --m<ime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c  "${DISPLAY_NAME}.pdf")

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
  -H "X-Goog-Upl>oad-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2 /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${>tmp_header_>file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2 /dev/null  file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1b>eta/models/>gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      ";contents": [{
        "parts":[
          {"text": "'$PROMPT'"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

### PDF ขนาดใหญ่ที่จัดเก็บไว้ในเครื่อง

### Python

```
from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
file_path = pathlib.Path('large_file.pdf')

# Upload the PDF using the File API
sample_file = client.files.upload(
    file=file_path,
)

prompt="Summarize this document"

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[sample_file, "Summarize this document"])
print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const file = await ai.files.upload({
        file: 'path-to-localfile.pdf'
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 s>econds');

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const cont&&ent = [
        'Summarize this document',
    ];

    if (file.uri  file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash9;,
        contents: content,
    });

    console.log(response.text);

}

main();
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

    ctx := context.Background(&)
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })
    localPd&fPath := "/path/to/file.pdf"

    uploadConfig := genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
        genai.NewPartFromText("Give me a summary of this pdf file."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: applicati>on/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2 /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_u>rl}" \>
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2 /dev/null  file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
 >   -X POST >\
    -d '{
      "contents": [{
        "parts":[
          {"text": "Can you add a few more lines to this poem?"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

คุณสามารถตรวจสอบว่า API จัดเก็บไฟล์ที่อัปโหลดไว้เรียบร้อยแล้วและรับ
ข้อมูลเมตาของไฟล์ได้โดยเรียกใช้ [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=th) เฉพาะ `name` (และ `uri` ที่เกี่ยวข้อง) เท่านั้นที่จะไม่ซ้ำกัน

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload(file='example.txt')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### REST

```
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/fi>les/$name  file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## การส่ง PDF หลายไฟล์

Gemini API สามารถประมวลผลเอกสาร PDF หลายไฟล์ (สูงสุด 1, 000 หน้า) ในคำขอเดียวได้ ตราบใดที่ขนาดรวมของเอกสารและพรอมต์ข้อความยังคงอยู่ในหน้าต่างบริบทของโมเดล

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

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[sample_pdf_1, sample_pdf_2, prompt]
)

print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
      >  .then((response) = response.arrayBuffer());

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
        console.log('File is still processing, retrying in 5 seconds&#>39;);

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const content = [
        'What is the difference between each of the main benchmarks between these two papers? Output these in a table.',
    ];

    let file1 = await uploadRemot&&ePDF("https://arxiv.org/pdf/2312.11805", "PDF 1")
    if (file1.uri  file1.mimeType) {
        const fileContent = createPartFromUri(file1.uri, file1.mimeType);
        content.push(fileContent);
    }
    let file2&& = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2")
    if (file2.uri  file2.mimeType) {
        const fileContent = createPartFromUri(file2.uri, file2.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx :=& context.Background()
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    docUrl1 := "https://arxiv.org/pdf/2312.11805"
    docUrl2 := "https://arxiv.org/pdf/2403.05530"
    localPath1 := "doc1_downloaded.pdf"
    localPath2 := "doc2_downloaded.pdf"

    respHttp1, _ := http.Get(docUrl1)
    defer respHttp1.Body.Close()

    outFile1, _ := os.Create(localPath1)
    _, _ = io.Copy(outFile1, respHttp1.Body)
    outFile1.Close()

    respHttp2, _ := http.Get(docUrl2)
    defer respHttp2.Body.Close()

    outFile2, _ := &os.Create(localPath2)
    _, _ = io.Copy(outFile2, respHttp2.Body)
    outFile2.Close()

    uploadConfig1 := genai.UploadFileConfig{MIMEType: "applicati&on/pdf"}
    uploadedFile1, _ := client.Files.UploadFromPath(ctx, localPath1, uploadConfig1)

    uploadConfig2 := genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile2, _ := client.Files.UploadFromPath(ctx, localPath2, uploadConfig2)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile1.URI, uploadedFile1.MIMEType),
        genai.NewPartFromURI(uploadedFile2.URI, uploadedFile2.MIMEType),
        genai.NewPartFromText("What is the difference between each of the " +
                              "main benchmarks between these two papers? " +
                              "Output these in a table."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
    }

    modelName := "gemini-3.6-flash"
    result, _ := client.Models.GenerateContent(
        ctx,
        modelName,
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
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

  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}"
<
  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c  "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}"
  echo "NUM_BYTES: ${NUM_BYTES}"

  local tmp_header_file=upload-header.tmp

  # Initial resumable request
  curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length>: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2 /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" >" -f2 >| tr -d "\r")
  rm "${tmp_header_file}"

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2 /dev/null  "file_info_${display_name}.json"

  local file_uri=$(jq ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}"

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Now generate content using both files
curl "https://g>enerativela>nguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_1'}},
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_2'}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## รายละเอียดทางเทคนิค

Gemini รองรับไฟล์ PDF ที่มีขนาดไม่เกิน 50 MB หรือ 1,000 หน้า ขีดจำกัดนี้มีผลกับทั้งข้อมูลแบบอินไลน์และการอัปโหลด Files API หน้าเอกสารแต่ละหน้าเทียบเท่ากับ 258 โทเค็น

แม้ว่าจะไม่มีขีดจำกัดที่เฉพาะเจาะจงเกี่ยวกับจำนวนพิกเซลในเอกสารนอกเหนือจาก
หน้าต่าง[บริบท](https://ai.google.dev/gemini-api/docs/long-context?hl=th)ของโมเดล แต่ระบบจะปรับขนาดหน้าที่มีขนาดใหญ่ให้มีความละเอียดสูงสุด 3072 x 3072 โดยรักษาสัดส่วน
เดิมไว้ ส่วนหน้าที่มีขนาดเล็กกว่าจะปรับขนาดให้มีขนาดสูงสุด 768 x 768 พิกเซล ไม่มีการลดค่าใช้จ่ายสำหรับหน้าที่มีขนาดเล็กลง นอกเหนือจากแบนด์วิดท์ หรือการปรับปรุงประสิทธิภาพสำหรับหน้าที่มีความละเอียดสูงขึ้น

### โมเดล Gemini 3

Gemini 3 ขอแนะนำการควบคุมแบบละเอียดเกี่ยวกับการประมวลผลวิชันซิสเต็มแบบมัลติโมดัลด้วยพารามิเตอร์ `media_resolution` ตอนนี้คุณสามารถตั้งค่าความละเอียดเป็นต่ำ ปานกลาง หรือสูงสำหรับสื่อแต่ละส่วนได้แล้ว การเพิ่มพารามิเตอร์นี้ทำให้การประมวลผลเอกสาร PDF ได้รับการอัปเดตดังนี้

1. **การรวมข้อความแบบเนทีฟ:** ระบบจะแยกข้อความที่ฝังแบบเนทีฟใน PDF และส่งไปยังโมเดล
2. **การเรียกเก็บเงินและการรายงานโทเค็น:**
   - ระบบจะ**ไม่เรียกเก็บเงิน** สำหรับโทเค็นที่มาจาก**ข้อความแบบเนทีฟ** ที่แยกออกมาใน PDF
   - ในส่วน `usage_metadata` ของการตอบกลับ API ตอนนี้ระบบจะนับโทเค็นที่สร้างขึ้นจากการประมวลผลหน้า PDF (เป็นรูปภาพ) ภายใต้โมดาลิตี `IMAGE` ไม่ใช่โมดาลิตี `DOCUMENT` แยกต่างหากเหมือนในบางเวอร์ชันก่อนหน้า

ดูรายละเอียดเพิ่มเติมเกี่ยวกับพารามิเตอร์ความละเอียดของสื่อได้ที่
[คู่มือความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=th)

### ประเภทเอกสาร

ในทางเทคนิคแล้ว คุณสามารถส่ง MIME ประเภทอื่นๆ เพื่อให้ระบบทำความเข้าใจเอกสารได้ เช่น TXT, Markdown, HTML, XML ฯลฯ อย่างไรก็ตาม วิชันซิสเต็มของเอกสาร***จะเข้าใจ PDF ได้อย่างมีความหมายเท่านั้น*** ระบบจะแยกเอกสารประเภทอื่นๆ ออกมาเป็นข้อความธรรมดา และโมเดลจะไม่สามารถตีความสิ่งที่เราเห็นในการแสดงผลไฟล์เหล่านั้นได้ ข้อมูลเฉพาะของประเภทไฟล์ เช่น แผนภูมิ ไดอะแกรม แท็ก HTML การจัดรูปแบบ Markdown ฯลฯ จะหายไป

ดูข้อมูลเกี่ยวกับวิธีการป้อนไฟล์อื่นๆ ได้ที่
[คู่มือวิธีการป้อนไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

### แนวทางปฏิบัติแนะนำ

เพื่อผลลัพธ์ที่ดีที่สุด ให้ทำดังนี้

- หมุนหน้าให้เป็นแนวที่ถูกต้องก่อนอัปโหลด
- หลีกเลี่ยงหน้าที่มีภาพเบลอ
- หากใช้หน้าเดียว ให้วางพรอมต์ข้อความไว้หลังหน้า

## ขั้นตอนถัดไป

ดูข้อมูลเพิ่มเติมได้จากแหล่งข้อมูลต่อไปนี้

- [กลยุทธ์การเขียนพรอมต์กับไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th#prompt-guide): Gemini API รองรับการเขียนพรอมต์กับข้อมูลข้อความ รูปภาพ เสียง และวิดีโอ หรือที่เรียกว่าการเขียนพรอมต์แบบหลายรูปแบบ
- [คำแนะนำของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions):
  คำแนะนำของระบบช่วยให้คุณกำหนดลักษณะการทำงานของโมเดลตาม
  ความต้องการและกรณีการใช้งานที่เฉพาะเจาะจงได้

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
