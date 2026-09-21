---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=th
fetched_at: 2026-09-21T05:45:30.489395+00:00
title: "Batch API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Batch API

Gemini Batch API ออกแบบมาเพื่อประมวลผลคำขอจำนวนมาก
แบบไม่พร้อมกันโดยคิดค่าใช้จ่าย [50% ของราคามาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
เวลาดำเนินการที่ตั้งไว้คือ 24 ชั่วโมง แต่ในกรณีส่วนใหญ่จะเร็วกว่านั้นมาก

ใช้ Batch API สำหรับงานขนาดใหญ่ที่ไม่เร่งด่วน เช่น การประมวลผลข้อมูลล่วงหน้าหรือการประเมินผลที่ไม่ได้ต้องการการตอบกลับทันที

## การสร้างงานแบบกลุ่ม

คุณส่งคำขอใน Batch API ได้ 2 วิธี ดังนี้

- **[คำขอแบบอินไลน์](#inline-requests):** รายการออบเจ็กต์
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=th#GenerateContentRequest) ที่รวมอยู่ในคำขอสร้างแบบกลุ่มโดยตรง วิธีนี้เหมาะสำหรับกลุ่มขนาดเล็กที่ทำให้ขนาดคำขอทั้งหมดไม่เกิน 20 MB **เอาต์พุต** ที่ส่งคืนจากโมเดลคือรายการออบเจ็กต์ `inlineResponse`
- **[ไฟล์อินพุต](#input-file):** ไฟล์ [JSON Lines (JSONL)](https://jsonlines.org/)
  ที่แต่ละบรรทัดมีออบเจ็กต์
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=th#GenerateContentRequest) ที่สมบูรณ์
  เราขอแนะนำให้ใช้วิธีนี้สำหรับคำขอขนาดใหญ่ **เอาต์พุต** ที่ส่งคืนจากโมเดลคือไฟล์ JSONL ที่แต่ละบรรทัดเป็น `GenerateContentResponse` หรือออบเจ็กต์สถานะ

### คำขอแบบอินไลน์

สำหรับคำขอจำนวนเล็กน้อย คุณสามารถฝัง
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=th#GenerateContentRequest) ออบเจ็กต์
ไว้ใน [`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=th#request-body) ได้โดยตรง ตัวอย่างต่อไปนี้จะเรียกใช้เมธอด
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=th#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
ด้วยคำขอแบบอินไลน์

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

// A list of InlinedRequest objects
List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Tell me a one-sentence joke.")))
                        .build()))
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Why is the sky blue?")))
                        .build()))
            .build());

BatchJobSource src = BatchJobSource.builder().inlinedRequests(inlineRequests).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("inlined-requests-job-1").build();

BatchJob inlineBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### ไฟล์อินพุต

สำหรับคำขอจำนวนมาก ให้เตรียมไฟล์ JSON Lines (JSONL) แต่ละบรรทัดใน
ไฟล์นี้ต้องเป็นออบเจ็กต์ JSON ที่มีคีย์ที่ผู้ใช้กำหนดและออบเจ็กต์คำขอ
โดยคำขอต้องเป็นออบเจ็กต์
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=th#GenerateContentRequest) ที่ถูกต้อง ระบบจะใช้คีย์ที่ผู้ใช้กำหนดในคำตอบเพื่อระบุว่าเอาต์พุตใดเป็นผลลัพธ์ของคำขอใด ตัวอย่างเช่น คำขอที่มีคีย์กำหนดเป็น `request-1` จะมีคำตอบที่ใส่คำอธิบายประกอบด้วยชื่อคีย์เดียวกัน

ระบบจะอัปโหลดไฟล์นี้โดยใช้ [File API](https://ai.google.dev/gemini-api/docs/files?hl=th) ขนาดไฟล์สูงสุดที่อนุญาตสำหรับไฟล์อินพุตคือ 2 GB

ตัวอย่างไฟล์ JSONL มีดังนี้ คุณสามารถบันทึกไฟล์นี้ในชื่อ `my-batch-requests.json` ได้

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

เช่นเดียวกับคำขอแบบอินไลน์ คุณสามารถระบุพารามิเตอร์อื่นๆ เช่น คำแนะนำของระบบ เครื่องมือ หรือการกำหนดค่าอื่นๆ ใน JSON ของคำขอแต่ละรายการได้

คุณสามารถอัปโหลดไฟล์นี้โดยใช้ [File API](https://ai.google.dev/gemini-api/docs/files?hl=th) ตามที่
แสดงในตัวอย่างต่อไปนี้ หากใช้ข้อมูลอินพุตหลายรูปแบบ คุณสามารถอ้างอิงไฟล์อื่นๆ ที่อัปโหลดไว้ในไฟล์ JSONL ได้

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Create a sample JSONL file
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"Describe the process of photosynthesis.\"}]}]}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"What are the main ingredients in a Margherita pizza?\"}]}]}}");
Files.write(Paths.get("my-batch-requests.jsonl"), requests);

// Upload the file to the File API
UploadFileConfig uploadConfig =
    UploadFileConfig.builder()
        .displayName("my-batch-requests")
        .mimeType("jsonl")
        .build();
File uploadedFile = client.files.upload("my-batch-requests.jsonl", uploadConfig);

System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

ตัวอย่างต่อไปนี้จะเรียกใช้
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=th#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
เมธอดโดยใช้ไฟล์อินพุตที่อัปโหลดโดยใช้ File API

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;

Client client = new Client();

// Assumes `uploadedFileName` is the file name from the previous step
String uploadedFileName = "files/my-batch-requests-id";

BatchJobSource src = BatchJobSource.builder().fileName(uploadedFileName).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("file-upload-job-1").build();

BatchJob fileBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

เมื่อสร้างงานแบบกลุ่ม คุณจะได้รับชื่อของงาน ใช้ชื่อนี้
เพื่อ [ตรวจสอบ](#batch-job-status)สถานะของงาน รวมถึง
[ดึงข้อมูลผลลัพธ์](#retrieve-batch-results)เมื่องานเสร็จสมบูรณ์

ตัวอย่างเอาต์พุตที่มีชื่อของงานมีดังนี้

```
Created batch job from file: batches/123456789
```

### การรองรับการฝังแบบกลุ่ม

คุณสามารถใช้ Batch API เพื่อโต้ตอบกับ
[โมเดลการฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)เพื่อเพิ่มปริมาณงาน
หากต้องการสร้างงานแบบกลุ่มการฝังด้วย[คำขอแบบอินไลน์](#inline-requests)
หรือ[ไฟล์อินพุต](#input-file) ให้ใช้ API `batches.create_embeddings` และ
ระบุโมเดลการฝัง

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.Content;
import com.google.genai.types.CreateEmbeddingsBatchJobConfig;
import com.google.genai.types.EmbedContentBatch;
import com.google.genai.types.EmbeddingsBatchJobSource;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

String uploadedFileName = "files/my-embedding-requests-id";

// Creating an embeddings batch job with an input file request:
BatchJob fileJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().fileName(uploadedFileName).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Input embeddings batch").build());
System.out.println("Created batch job: " + fileJob.name().orElse(""));

// Creating an embeddings batch job with an inline request:
EmbedContentBatch inlinedRequests =
    EmbedContentBatch.builder()
        .contents(Arrays.asList(Content.fromParts(Part.fromText("What is the meaning of life?"))))
        .build();
BatchJob batchJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().inlinedRequests(inlinedRequests).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Inlined embeddings batch").build());
System.out.println("Created batch job: " + batchJob.name().orElse(""));
```

อ่านส่วนการฝังใน[คู่มือการใช้งาน Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)
เพื่อดูตัวอย่างเพิ่มเติม

### การกำหนดค่าคำขอ

คุณสามารถรวมการกำหนดค่าคำขอใดก็ได้ที่จะใช้ในคำขอมาตรฐานที่ไม่ใช่แบบกลุ่ม เช่น คุณระบุอุณหภูมิ คำแนะนำของระบบ หรือแม้แต่ส่งต่อรูปแบบอื่นๆ ได้ ตัวอย่างต่อไปนี้แสดงคำขอแบบอินไลน์ที่มีคำแนะนำของระบบสำหรับคำขอรายการหนึ่ง

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

List<InlinedRequest> inlineRequestsList =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cloud."))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cat."))))
            .config(
                GenerateContentConfig.builder()
                    .systemInstruction(
                        Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
                    .build())
            .build());
```

เช่นเดียวกัน คุณสามารถระบุเครื่องมือที่จะใช้สำหรับคำขอได้ ตัวอย่างต่อไปนี้
แสดงคำขอที่เปิดใช้เครื่องมือ [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;
import java.util.List;

List<InlinedRequest> inlinedRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 1998?"))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 2025?"))))
            .config(
                GenerateContentConfig.builder()
                    .tools(Tool.builder().googleSearch(GoogleSearch.builder().build()).build())
                    .build())
            .build());
```

นอกจากนี้ คุณยังระบุ[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)ได้ด้วย
ตัวอย่างต่อไปนี้แสดงวิธีระบุสำหรับคำขอแบบกลุ่ม

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

### Java

```
import java.util.HashMap;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.List;
import java.util.Map;
import java.util.Set;

Client client = new Client();

Map<String, Schema> properties = new HashMap<>();
properties.put("recipeName", Schema.builder().type(Type.Known.STRING).build());
properties.put(
    "ingredients",
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(Schema.builder().type(Type.Known.STRING).build())
        .build());

Schema recipeSchema =
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
properties)
                .required("recipeName")
                .build())
        .build();

GenerateContentConfig jsonConfig =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(recipeSchema)
        .build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular gluten free cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3.8-flash",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("structured-output-job-1").build());

// Wait for the job to finish
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJobInline = client.batches.get(jobName, null);
while (!completedStates.contains(batchJobInline.state().get().knownEnum())) {
  System.out.println(
      "Job not finished. Current state: " + batchJobInline.state().get() + ". Waiting 30 seconds...");
  Thread.sleep(30000);
  batchJobInline = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJobInline.state().get());

// Print the response
List<InlinedResponse> responses = batchJobInline.dest().get().inlinedResponses().orElse(Collections.emptyList());
for (int i = 0; i < responses.size(); i++) {
  System.out.println("\n--- Response " + (i + 1) + " ---");
  InlinedResponse inlineResponse = responses.get(i);
  if (inlineResponse.response().isPresent()) {
    System.out.println(inlineResponse.response().get().text());
  }
}
```

ตัวอย่างต่อไปนี้แสดงเอาต์พุตของงานนี้

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## การตรวจสอบสถานะของงาน

ใช้ชื่อการดำเนินการที่ได้รับเมื่อสร้างงานแบบกลุ่มเพื่อสำรวจสถานะของงาน
ฟิลด์สถานะของงานแบบกลุ่มจะระบุสถานะปัจจุบันของงาน งานแบบกลุ่มอาจมีสถานะอย่างใดอย่างหนึ่งต่อไปนี้

- `JOB_STATE_PENDING`: ระบบสร้างงานแล้วและกำลังรอให้บริการประมวลผล
- `JOB_STATE_RUNNING`: งานกำลังดำเนินการ
- `JOB_STATE_SUCCEEDED`: งานเสร็จสมบูรณ์แล้ว ตอนนี้คุณสามารถดึงข้อมูลผลลัพธ์ได้แล้ว
- `JOB_STATE_FAILED`: งานล้มเหลว ดูข้อมูลเพิ่มเติมได้ในรายละเอียดข้อผิดพลาด
- `JOB_STATE_CANCELLED`: ผู้ใช้ยกเลิกงาน
- `JOB_STATE_EXPIRED`: งานหมดอายุเนื่องจากทำงานหรือรอนานกว่า 48 ชั่วโมง งานจะไม่มีผลลัพธ์ให้ดึงข้อมูล
  คุณลองส่งงานอีกครั้งหรือแบ่งคำขอออกเป็นกลุ่มย่อยๆ ได้

คุณสามารถสำรวจสถานะของงานเป็นระยะๆ เพื่อตรวจสอบว่างานเสร็จสมบูรณ์แล้วหรือไม่

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.JobState;
import java.util.Set;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

System.out.println("Polling status for job: " + jobName);
BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(30000); // Wait for 30 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### การสำรวจและเว็บฮุค

**เบื่อการสำรวจแล้วใช่ไหม** ตอนนี้ Gemini รองรับ
[เว็บฮุค](https://ai.google.dev/gemini-api/docs/webhooks?hl=th)สำหรับการประมวลผลการเติมข้อความแบบไม่พร้อมกันแล้ว
แทนที่จะเรียกใช้ `GET / operations` อย่างต่อเนื่อง ให้สมัครใช้บริการ `batch.succeeded` โดยตรงเพื่ออนุญาตให้ Gemini API ส่งการแจ้งเตือนแบบเรียลไทม์ไปยังเซิร์ฟเวอร์ของคุณเมื่อการดำเนินการแบบไม่พร้อมกันหรือการดำเนินการที่ใช้เวลานานเสร็จสมบูรณ์

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookInput;
import com.google.genai.gaos.models.webhooks.WebhookSubscribedEvent;
import java.util.List;

Client client = new Client();

WebhookInput input =
    WebhookInput.builder()
        .name("MyBatchWebhook")
        .subscribedEvents(
            Arrays.asList(
                WebhookSubscribedEvent.BATCH_SUCCEEDED,
                WebhookSubscribedEvent.BATCH_FAILED))
        .uri("https://my-api.com/gemini-callback")
        .build();

Webhook webhook = client.webhooks.create(input).webhook().get();
System.out.println("Created webhook: " + webhook.name().orElse(""));
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## การดึงข้อมูลผลลัพธ์

เมื่อสถานะของงานระบุว่างานแบบกลุ่มเสร็จสมบูรณ์แล้ว ผลลัพธ์จะอยู่ในฟิลด์ `response`
โดยค่าเริ่มต้น ระบบจะจัดเก็บผลลัพธ์ของงานแบบกลุ่มและให้ดาวน์โหลดได้เป็นเวลา 6 สัปดาห์ก่อนที่จะลบออกอย่างถาวร

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobDestination;
import com.google.genai.types.InlinedEmbedContentResponse;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";
BatchJob batchJob = client.batches.get(jobName, null);

if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  BatchJobDestination dest = batchJob.dest().orElse(null);

  // If batch job was created with a file destination
  if (dest != null && dest.fileName().isPresent()) {
    String resultFileName = dest.fileName().get();
    System.out.println("Results are in file: " + resultFileName);

    System.out.println("Downloading result file content...");
    client.files.download(resultFileName, "batch_results.jsonl", null);
    String fileContent = Files.readString(Paths.get("batch_results.jsonl"));
    System.out.println(fileContent);
  }
  // If batch job was created with inline requests
  else if (dest != null && dest.inlinedResponses().isPresent()) {
    System.out.println("Results are inline:");
    List<InlinedResponse> responses = dest.inlinedResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get().text());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  }
  // If batch job was an embedding batch with inline responses
  else if (dest != null && dest.inlinedEmbedContentResponses().isPresent()) {
    System.out.println("Embedding results found inline:");
    List<InlinedEmbedContentResponse> responses = dest.inlinedEmbedContentResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedEmbedContentResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  } else {
    System.out.println("No results found (neither file nor inline).");
  }
} else {
  System.out.println("Job did not succeed. Final state: " + batchJob.state().get());
  batchJob.error().ifPresent(err -> System.out.println("Error: " + err));
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## การแสดงรายการงานแบบกลุ่ม

คุณสามารถแสดงรายการงานแบบกลุ่มล่าสุดได้

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.Pager;
import com.google.genai.types.BatchJob;
import com.google.genai.types.ListBatchJobsConfig;

Client client = new Client();

Pager<BatchJob> batchJobs = client.batches.list(null);

// Optional query config:
// Pager<BatchJob> batchJobs = client.batches.list(ListBatchJobsConfig.builder().pageSize(5).build());

for (BatchJob batchJob : batchJobs) {
  System.out.println(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## การยกเลิกงานแบบกลุ่ม

คุณสามารถยกเลิกงานแบบกลุ่มที่กำลังดำเนินการอยู่ได้โดยใช้ชื่อของงาน เมื่อยกเลิกงาน ระบบจะหยุดประมวลผลคำขอใหม่

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToCancelName = "batches/your-batch-id";
client.batches.cancel(batchJobToCancelName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## การลบงานแบบกลุ่ม

คุณสามารถลบงานแบบกลุ่มที่มีอยู่ได้โดยใช้ชื่อของงาน เมื่อลบงาน ระบบจะหยุดประมวลผลคำขอใหม่และนำงานออกจากรายการงานแบบกลุ่ม

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToDeleteName = "batches/your-batch-id";
client.batches.delete(batchJobToDeleteName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## การสร้างรูปภาพแบบกลุ่ม

หากคุณใช้ [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=th) และต้องการสร้างรูปภาพจำนวนมาก
คุณสามารถใช้ Batch API เพื่อรับ
[ขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)ที่สูงขึ้นโดยแลกกับการดำเนินการที่ใช้เวลาสูงสุด
24 ชั่วโมง

คุณสามารถใช้[คำขอแบบอินไลน์](#inline-requests-images)สำหรับคำขอแบบกลุ่มขนาดเล็ก (ไม่เกิน 20 MB) หรือ
ไฟล์อินพุต [JSONL](#input-file-images) สำหรับคำขอแบบกลุ่มขนาดใหญ่ (แนะนำสำหรับการสร้างรูปภาพ)

### คำขอแบบอินไลน์สำหรับรูปภาพ

### Python

```
import time
import base64
import json
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create batch job with inline requests
inline_requests = [
    {
        'contents': [{'parts': [{'text': 'A big letter A surrounded by animals starting with the A letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    },
    {
        'contents': [{'parts': [{'text': 'A big letter B surrounded by animals starting with the B letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=inline_requests,
    config={
        'display_name': "inlined-image-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")

# 2. Monitor job status
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 3. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    print("Results are inline:")
    for i, inline_response in enumerate(batch_job.dest.inlined_responses):
        print(f"Response {i+1}:")
        if inline_response.response:
            for part in inline_response.response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.inline_data:
                    print(f"Image mime type: {part.inline_data.mime_type}")
                    image = part.as_image()
                    image.save(f"image_{i+1}.png")
        elif inline_response.error:
            print(f"Error: {inline_response.error}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create batch job with inline requests
    const inlinedRequests = [
        {
            contents: [{parts: [{text: 'A big letter A surrounded by animals starting with the A letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        },
        {
            contents: [{parts: [{text: 'A big letter B surrounded by animals starting with the B letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        }
    ]

    const inlineBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: inlinedRequests,
        config: {
            displayName: 'inlined-image-requests-job-1',
        }
    });

    console.log(inlineBatchJob);

    // 2. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: inlineBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${inlineBatchJob.name}:`, error);
        return;
    }

    // 3. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    for (const part of inlineResponse.response.candidates[0].content.parts) {
                        if (part.text) {
                            console.log(part.text);
                        } else if (part.inlineData) {
                            console.log(`Image mime type: ${part.inlineData.mimeType}`);
                        }
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No inline results found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create batch job with inline requests
GenerateContentConfig imageConfig =
    GenerateContentConfig.builder().responseModalities("TEXT", "IMAGE").build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter A surrounded by animals starting with the A letter"))))
            .config(imageConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter B surrounded by animals starting with the B letter"))))
            .config(imageConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("inlined-image-requests-job-1").build());

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));

// 2. Monitor job status
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 3. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  System.out.println("Results are inline:");
  List<InlinedResponse> responses = batchJob.dest().get().inlinedResponses().orElse(Collections.emptyList());
  for (int i = 0; i < responses.size(); i++) {
    System.out.println("Response " + (i + 1) + ":");
    InlinedResponse inlineResponse = responses.get(i);
    if (inlineResponse.response().isPresent()) {
      for (Part part : inlineResponse.response().get().parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          System.out.println("Image mime type: " + part.inlineData().get().mimeType().orElse(""));
          Files.write(
              Paths.get("image_" + (i + 1) + ".png"),
              part.inlineData().get().data().get());
        }
      }
    } else if (inlineResponse.error().isPresent()) {
      System.out.println("Error: " + inlineResponse.error().get());
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-image-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-1" }
                    },
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-2" }
                    }
                ]
            }
        }
    }
}'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 2. Poll job status until completion by repeating the following command
# Replace $BATCH_NAME with the name returned above.
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 3. If state is JOB_STATE_SUCCEEDED, retrieve results from batch_status.json
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    echo "Job succeeded. Results:"
    jq -r '.dest.inlinedResponses' batch_status.json
fi
```

### ไฟล์อินพุตสำหรับรูปภาพ

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.File;
import com.google.genai.types.JobState;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create and upload file
String fileName = "my-batch-image-requests.jsonl";
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter A surrounded by animals starting with the A letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter B surrounded by animals starting with the B letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}");
Files.write(Paths.get(fileName), requests);

File uploadedFile =
    client.files.upload(
        fileName,
        UploadFileConfig.builder()
            .displayName("my-batch-image-requests")
            .mimeType("jsonl")
            .build());
System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));

// 2. Create batch job
BatchJob fileBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().fileName(uploadedFile.name().get()).build(),
        CreateBatchJobConfig.builder().displayName("file-image-upload-job-1").build());
System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));

// 3. Monitor job status
String jobName = fileBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 4. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  String resultFileName = batchJob.dest().get().fileName().get();
  System.out.println("Results are in file: " + resultFileName);
  System.out.println("Downloading result file content...");
  client.files.download(resultFileName, "batch_image_results.jsonl", null);
  for (String line : Files.readAllLines(Paths.get("batch_image_results.jsonl"))) {
    if (!line.isEmpty()) {
      System.out.println(line);
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## รายละเอียดทางเทคนิค

- **โมเดลที่รองรับ:** Batch API รองรับโมเดล Gemini หลายรุ่น
  โปรดดูที่[หน้าโมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)เพื่อดูการรองรับ
  Batch API ของแต่ละโมเดล รูปแบบที่รองรับสำหรับ Batch API จะเหมือนกับรูปแบบที่รองรับใน API แบบโต้ตอบ (หรือที่ไม่ใช่แบบกลุ่ม)
- **ราคา:** การใช้งาน Batch API คิดราคา 50% ของราคา API แบบโต้ตอบมาตรฐานสำหรับโมเดลที่เทียบเท่า ดูรายละเอียดได้ใน[หน้าราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
  โปรดดูรายละเอียดเกี่ยวกับขีดจำกัดอัตราสำหรับฟีเจอร์นี้ได้ในหน้า[ขีดจำกัดอัตรา](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th#batch-mode)
- **เป้าหมายระดับการให้บริการ (SLO):** งานแบบกลุ่มออกแบบมาให้เสร็จสมบูรณ์ภายในเวลาดำเนินการ 24 ชั่วโมง งานจำนวนมากอาจเสร็จสมบูรณ์เร็วกว่านั้นมาก ทั้งนี้ขึ้นอยู่กับขนาดของงานและภาระงานปัจจุบันของระบบ
- **การแคช:** [ระบบรองรับการแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)สำหรับคำขอแบบกลุ่ม ใช้เนื้อหาที่แคชไว้ซ้ำโดยระบุชื่อทรัพยากร `cached_content` ในการกำหนดค่าคำขอแต่ละรายการภายในกลุ่ม
  หากคำขอในกลุ่มทำให้เกิดการพบแคช คุณจะต้องชำระเงินตามอัตราการแคชบริบทมาตรฐาน

## แนวทางปฏิบัติแนะนำ

- **ใช้ไฟล์อินพุตสำหรับคำขอขนาดใหญ่:** สำหรับคำขอจำนวนมาก
  ให้ใช้วิธีการป้อนไฟล์
  เสมอเพื่อให้จัดการได้ง่ายขึ้นและหลีกเลี่ยงการถึงขีดจำกัดขนาดคำขอสำหรับ
  การเรียก [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=th#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
  เอง โปรดทราบว่าไฟล์อินพุตแต่ละไฟล์มีขีดจำกัดขนาด 2 GB
- **การจัดการข้อผิดพลาด:** ตรวจสอบ `batchStats` เพื่อดู `failedRequestCount` หลังจากงานเสร็จสมบูรณ์ หากใช้เอาต์พุตไฟล์ ให้แยกวิเคราะห์แต่ละบรรทัดเพื่อตรวจสอบว่าเป็น `GenerateContentResponse` หรือออบเจ็กต์สถานะที่ระบุข้อผิดพลาดสำหรับคำขอนั้นๆ ดูชุดรหัสข้อผิดพลาดทั้งหมดได้ใน[คู่มือ
  การแก้ปัญหา](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=th#error-codes)
- **ส่งงานเพียงครั้งเดียว:** การสร้างงานแบบกลุ่มไม่ใช่การดำเนินการที่ทำซ้ำได้
  หากคุณส่งคำขอสร้างเดียวกัน 2 ครั้ง ระบบจะสร้างงานแบบกลุ่ม 2 งานแยกกัน
- **แบ่งกลุ่มขนาดใหญ่มาก:** แม้ว่าเวลาดำเนินการที่ตั้งไว้คือ 24 ชั่วโมง แต่เวลาประมวลผลจริงอาจแตกต่างกันไปตามภาระงานของระบบและขนาดของงาน
  สำหรับงานขนาดใหญ่ ให้พิจารณาแบ่งงานออกเป็นกลุ่มย่อยๆ หากต้องการผลลัพธ์ระดับกลางเร็วขึ้น

## ขั้นตอนถัดไป

- ดูตัวอย่างเพิ่มเติมได้ในโน้ตบุ๊ก [Batch API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=th)
- เลเยอร์ความเข้ากันได้กับ OpenAI รองรับ Batch API อ่านตัวอย่างในหน้า
  [ความเข้ากันได้กับ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th#batch)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-18 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-18 UTC"],[],[]]
