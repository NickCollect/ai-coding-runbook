---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th
fetched_at: 2026-09-28T06:23:57.664950+00:00
title: "\u0e27\u0e34\u0e18\u0e35\u0e01\u0e32\u0e23\u0e1b\u0e49\u0e2d\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e1f\u0e25\u0e4c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# วิธีการป้อนข้อมูลไฟล์

คู่มือนี้จะอธิบายวิธีต่างๆ ในการรวมไฟล์สื่อ เช่น รูปภาพ เสียง วิดีโอ และเอกสาร เมื่อส่งคำขอไปยัง Gemini API
วิธีการใหม่นี้รองรับในปลายทาง Gemini API ทั้งหมด ซึ่งรวมถึง Batch, Interactions และ Live API
การเลือกวิธีการที่เหมาะสมขึ้นอยู่กับขนาดของไฟล์ ตำแหน่งที่จัดเก็บข้อมูล และความถี่ที่คุณวางแผนจะใช้ไฟล์

วิธีที่ง่ายที่สุดในการรวมไฟล์เป็นอินพุตคือการอ่านไฟล์ในเครื่องและ
รวมไว้ในพรอมต์ ตัวอย่างต่อไปนี้แสดงวิธีอ่านไฟล์ PDF ในเครื่อง
ไฟล์ PDF มีขนาดได้ไม่เกิน 50 MB สำหรับวิธีนี้ ดูรายการประเภทไฟล์อินพุตและขีดจำกัดทั้งหมดได้ใน
[ตารางเปรียบเทียบวิธีการป้อนข้อมูล](#method-comparison)

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("my_local_file.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    pdfBytes, err := os.ReadFile("my_local_file.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## การเปรียบเทียบวิธีการป้อนข้อมูล

ตารางต่อไปนี้เปรียบเทียบวิธีการป้อนข้อมูลแต่ละวิธีกับขีดจำกัดของไฟล์และกรณีการใช้งานที่ดีที่สุด
โปรดทราบว่าการจำกัดขนาดไฟล์อาจแตกต่างกันไปตามประเภทไฟล์และ
โมเดลหรือโทเค็นไนเซอร์ที่ใช้ประมวลผลไฟล์

| วิธีการ | เหมาะสำหรับ | ขนาดไฟล์สูงสุด | ความต่อเนื่อง |
| --- | --- | --- | --- |
| **ข้อมูลในบรรทัด** | การทดสอบอย่างรวดเร็ว ไฟล์ขนาดเล็ก และแอปพลิเคชันแบบเรียลไทม์ | 100 MB ต่อคำขอหรือเพย์โหลด   (**50 MB สำหรับ PDF**) | ไม่มี (ส่งพร้อมกับทุกคำขอ) |
| **การอัปโหลดไฟล์ผ่าน API** | ไฟล์ขนาดใหญ่ ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์   สูงสุด 20 GB ต่อโปรเจ็กต์ | 48 ชั่วโมง |
| **การลงทะเบียน URI ของ GCS สำหรับ File API** | ไฟล์ขนาดใหญ่ที่อยู่ใน Google Cloud Storage อยู่แล้ว ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์ ไม่มีขีดจำกัดพื้นที่เก็บข้อมูลโดยรวม | ไม่มี (ดึงข้อมูลต่อคำขอ) การลงทะเบียนครั้งเดียวจะให้สิทธิ์เข้าถึงได้นานสูงสุด 30 วัน |
| **URL ภายนอก** | ข้อมูลสาธารณะหรือข้อมูลในที่เก็บข้อมูลบนระบบคลาวด์ (AWS, Azure, GCS) โดยไม่ต้องอัปโหลดซ้ำ | 100 MB ต่อคำขอ/เพย์โหลด | ไม่มี (ดึงข้อมูลต่อคำขอ) |

## ข้อมูลแบบอินไลน์

สำหรับไฟล์ขนาดเล็ก (ไม่เกิน 100 MB หรือ 50 MB สำหรับ PDF) คุณสามารถส่งข้อมูล
ในเพย์โหลดคำขอได้โดยตรง นี่เป็นวิธีที่ง่ายที่สุดสำหรับการทดสอบอย่างรวดเร็วหรือแอปพลิเคชันที่จัดการข้อมูลแบบเรียลไทม์และข้อมูลชั่วคราว คุณระบุข้อมูลเป็นสตริงที่เข้ารหัส Base64 หรือโดยการอ่านไฟล์ในเครื่องโดยตรงก็ได้

ดูตัวอย่างการอ่านจากไฟล์ในเครื่องได้ที่ตัวอย่างที่ส่วนต้นของ
หน้านี้

### ดึงข้อมูลจาก URL

นอกจากนี้ คุณยังดึงข้อมูลไฟล์จาก URL แปลงเป็นไบต์ และรวมไว้ใน
อินพุตได้ด้วย

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String docUrl = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(docUrl)).build();
byte[] docData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
String base64Pdf = Base64.getEncoder().encodeToString(docData);

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    docURL := "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    resp, err := http.Get(docURL)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    docData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(docData)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.8-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

File API ออกแบบมาสำหรับไฟล์ขนาดใหญ่ (สูงสุด 2 GB) หรือไฟล์ที่คุณต้องการ
ใช้ในคำขอหลายรายการ

### การอัปโหลดไฟล์แบบมาตรฐาน

อัปโหลดไฟล์ในเครื่องไปยัง Gemini API ไฟล์ที่อัปโหลดด้วยวิธีนี้จะได้รับการจัดเก็บ
ชั่วคราว (48 ชั่วโมง) และประมวลผลเพื่อให้โมเดลเรียกข้อมูลได้อย่างมีประสิทธิภาพ

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File docFile =
    client.files.upload(
        new java.io.File("path/to/your/sample.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .uri(docFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(docFile.mimeType().orElse("application/pdf")))
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    docFile, err := client.Files.UploadFromPath(ctx, "path/to/your/sample.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(docFile.URI),
                    MimeType: interactions.DocumentContentMimeType(docFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### ลงทะเบียนไฟล์ Google Cloud Storage

หากข้อมูลอยู่ใน Google Cloud Storage อยู่แล้ว คุณไม่จำเป็นต้องดาวน์โหลดและอัปโหลดอีกครั้ง คุณลงทะเบียนได้โดยตรงด้วย File API

1. ให้สิทธิ์เข้าถึงแต่ละถังแก่ **Service Agent**

   1. เปิดใช้ Gemini API ในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google
   2. สร้าง Service Agent โดยทำดังนี้

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **ให้สิทธิ์ Agent บริการ Gemini API** ในการอ่านที่เก็บข้อมูล
      Bucket

      ผู้ใช้ต้องมอบหมาย`Storage Object Viewer`
      [บทบาท IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=th#storage.objectViewer)
      ให้กับตัวแทนบริการนี้ในที่เก็บข้อมูลที่ต้องการใช้

   โดยค่าเริ่มต้นแล้ว สิทธิ์เข้าถึงนี้จะไม่มีวันหมดอายุ แต่คุณสามารถเปลี่ยนแปลงได้ทุกเมื่อ คุณยังใช้คำสั่ง [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=th)
   เพื่อให้สิทธิ์ได้ด้วย
2. ตรวจสอบสิทธิ์บริการ

   **ข้อกำหนดเบื้องต้น**

   - เปิดใช้ API
   - สร้างบัญชีบริการหรือตัวแทนที่มีสิทธิ์ที่เหมาะสม

   ก่อนอื่นคุณต้องตรวจสอบสิทธิ์ในฐานะบริการที่มีสิทธิ์เข้าถึง Storage Object Viewer
   ซึ่งวิธีการนี้จะขึ้นอยู่กับสภาพแวดล้อมที่โค้ดการจัดการไฟล์จะทำงาน

   **ภายนอก Google Cloud**

   หากโค้ดของคุณทำงานจากภายนอก Google Cloud เช่น เดสก์ท็อป
   ให้ดาวน์โหลดข้อมูลเข้าสู่ระบบของบัญชีจากคอนโซล Google Cloud โดยทำตาม
   ขั้นตอนต่อไปนี้

   1. ไปที่[คอนโซลบัญชีบริการ](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=th)
   2. เลือกบัญชีบริการที่เกี่ยวข้อง
   3. เลือกแท็บ**คีย์** แล้วเลือก**เพิ่มคีย์ สร้างคีย์ใหม่**
   4. เลือกประเภทคีย์ **JSON** และจดบันทึกตำแหน่งที่ดาวน์โหลดไฟล์ในเครื่อง

   ดูรายละเอียดเพิ่มเติมได้ในเอกสารประกอบอย่างเป็นทางการของ Google Cloud เกี่ยวกับ
   [การจัดการคีย์บัญชีบริการ](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=th)

   จากนั้นใช้คำสั่งต่อไปนี้เพื่อตรวจสอบสิทธิ์ คำสั่งเหล่านี้ถือว่าไฟล์บัญชีบริการของคุณอยู่ในไดเรกทอรีปัจจุบันและมีชื่อว่า
   `service-account.json`

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **ใน Google Cloud**

   หากคุณเรียกใช้ใน Google Cloud โดยตรง เช่น ใช้[ฟังก์ชัน Cloud Run](https://cloud.google.com/functions?hl=th) หรือ[อินสแตนซ์ Compute Engine](https://cloud.google.com/products/compute?hl=th) คุณจะมีข้อมูลเข้าสู่ระบบโดยนัย แต่จะต้องตรวจสอบสิทธิ์อีกครั้งเพื่อให้ขอบเขตที่เหมาะสม

   ### Python

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่สามารถรับ
   [ข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=th)
   ได้โดยอัตโนมัติ เช่น Cloud Run หรือ Compute Engine

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่สามารถรับ
   [ข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=th)
   ได้โดยอัตโนมัติ เช่น Cloud Run หรือ Compute Engine

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;

List<String> gcsReadScopes =
    Arrays.asList(
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/cloud-platform");

String serviceAccountFile = "service-account.json";

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream(serviceAccountFile))
        .createScoped(gcsReadScopes);
```

### Go

```
package main

import (
    "log"

    "google.golang.org/genai"
)

func main() {
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    _ = cc.Credentials
}
```

### CLI

นี่คือคำสั่งแบบอินเทอร์แอกทีฟ สำหรับบริการอย่าง Compute Engine คุณสามารถแนบขอบเขตกับบริการที่กำลังทำงานที่ระดับการกำหนดค่าได้ ดูตัวอย่างได้ที่[เอกสารประกอบเกี่ยวกับบริการที่ผู้ใช้จัดการ](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=th#using)

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. การลงทะเบียนไฟล์ (Files API)
   ใช้ Files API เพื่อลงทะเบียนไฟล์และสร้างเส้นทาง Files API ที่ใช้ใน Gemini API ได้โดยตรง

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.8-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.8-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.RegisterFilesResponse;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream("service-account.json"))
        .createScoped(
            Arrays.asList(
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/cloud-platform"));

Client client = Client.builder().credentials(credentials).build();

RegisterFilesResponse registeredGcsFiles =
    client.files.registerFiles(
        credentials,
        Arrays.asList("gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"),
        null);

String prompt = "Summarize this file.";

for (File f : registeredGcsFiles.files().orElse(Collections.emptyList())) {
  System.out.println(f.name().orElse(""));

  Content textContent = TextContent.builder().text(prompt).build();
  Content docContent =
      DocumentContent.builder()
          .uri(f.uri().orElse(""))
          .mimeType(DocumentContentMimeType.of(f.mimeType().orElse("application/pdf")))
          .build();

  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(InteractionsInput.ofContent(Arrays.asList(textContent, docContent)))
          .build();

  Interaction interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
  System.out.println(interaction.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    client, err := genai.NewClient(ctx, cc)
    if err != nil {
        log.Fatal(err)
    }

    registeredGcsFiles, err := client.Files.RegisterFiles(
        ctx,
        []string{"gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"},
        cc.Credentials,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this file."

    for _, f := range registeredGcsFiles.Files {
        fmt.Println(f.Name)
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput([]interactions.Content{
                    interactions.NewContent(interactions.TextContent{
                        Text: prompt,
                    }),
                    interactions.NewContent(interactions.DocumentContent{
                        URI:      genai.Ptr(f.URI),
                        MimeType: interactions.DocumentContentMimeType(f.MIMEType).ToPointer(),
                    }),
                }),
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        if res.Interaction.OutputText != nil {
            fmt.Println(*res.Interaction.OutputText)
        }
    }
}
```

### CLI

```
access_token=$(gcloud auth application-default print-access-token)
project_id=$(gcloud config get-value project)
curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" \
    -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
```

## HTTP ภายนอก / URL ที่ลงนาม

คุณส่ง URL HTTPS ที่เข้าถึงได้แบบสาธารณะหรือ URL ที่ลงนามล่วงหน้าได้โดยตรงในคำขอ Gemini API จะดึงข้อมูลเนื้อหาอย่างปลอดภัยในระหว่างการประมวลผล
วิธีนี้เหมาะสำหรับไฟล์ขนาดไม่เกิน 100 MB ที่คุณไม่ต้องการอัปโหลดซ้ำ

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.8-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### การช่วยเหลือพิเศษ

ตรวจสอบว่า URL ที่คุณระบุไม่ได้นำไปยังหน้าที่ต้องมีการเข้าสู่ระบบหรือ
อยู่หลังเพย์วอลล์ สำหรับฐานข้อมูลส่วนตัว โปรดตรวจสอบว่าคุณสร้าง URL ที่ลงชื่อแล้ว
พร้อมสิทธิ์การเข้าถึงและวันหมดอายุที่ถูกต้อง

### การตรวจสอบความปลอดภัย

ระบบจะตรวจสอบการกลั่นกรองเนื้อหาใน URL เพื่อยืนยันว่า URL เป็นไปตาม
มาตรฐานด้านความปลอดภัยและนโยบาย หาก URL ไม่ผ่านการตรวจสอบนี้ คุณจะได้รับ
`url_retrieval_status`ของ `URL_RETRIEVAL_STATUS_UNSAFE`

### ประเภทเนื้อหาที่รองรับ

รายการประเภทไฟล์ที่รองรับและข้อจำกัดนี้มีไว้เพื่อเป็นคำแนะนำเบื้องต้นและไม่ได้ครอบคลุมข้อมูลทั้งหมด ชุดประเภทที่รองรับที่มีผลอาจมีการเปลี่ยนแปลงและอาจแตกต่างกันไปตามโมเดลและเวอร์ชันโทเค็นไนเซอร์ที่เฉพาะเจาะจงที่ใช้งานอยู่ ประเภทที่ไม่รองรับจะทำให้เกิดข้อผิดพลาด
นอกจากนี้ การดึงข้อมูลเนื้อหาสำหรับไฟล์ประเภทเหล่านี้จะรองรับเฉพาะ URL ที่เข้าถึงได้แบบสาธารณะเท่านั้น

#### ประเภทไฟล์ข้อความ

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### ประเภทไฟล์แอปพลิเคชัน

- `application/json`
- `application/pdf`

#### ไฟล์ประเภทรูปภาพ

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### ไฟล์ประเภทวิดีโอ

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## แนวทางปฏิบัติแนะนำ

- **เลือกวิธีที่เหมาะสม:** ใช้ข้อมูลแบบอินไลน์สำหรับไฟล์ขนาดเล็กที่ใช้ชั่วคราว
  ใช้ File API สำหรับไฟล์ที่มีขนาดใหญ่หรือใช้บ่อย ใช้ URL ภายนอก
  สำหรับข้อมูลที่โฮสต์ออนไลน์อยู่แล้ว
- **ระบุประเภท MIME:** ระบุประเภท MIME ที่ถูกต้องสำหรับข้อมูลไฟล์เสมอเพื่อให้ประมวลผลได้อย่างเหมาะสม
- **จัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดในโค้ดเพื่อจัดการ
  ปัญหาที่อาจเกิดขึ้น เช่น เครือข่ายล่ม ปัญหาการเข้าถึงไฟล์ หรือข้อผิดพลาดของ API

## ข้อจำกัด

- ขีดจำกัดขนาดไฟล์จะแตกต่างกันไปตามวิธีการ (ดู[ตารางเปรียบเทียบ](#method-comparison))
  และประเภทไฟล์
- ข้อมูลแบบอินไลน์จะเพิ่มขนาดเพย์โหลดของคำขอ
- การอัปโหลด File API เป็นแบบชั่วคราวและจะหมดอายุหลังจาก 48 ชั่วโมง
- การดึงข้อมูล URL ภายนอกจำกัดไว้ที่ 100 MB ต่อเพย์โหลด และรองรับเนื้อหาบางประเภท

## ขั้นตอนถัดไป

- ลองเขียนพรอมต์มัลติโมดัลของคุณเองโดยใช้ [Google AI Studio](http://aistudio.google.com/?hl=th)
- ดูข้อมูลเกี่ยวกับการรวมไฟล์ไว้ในพรอมต์ได้ในคำแนะนำเกี่ยวกับ[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=th), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=th) และ[การประมวลผลเอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
