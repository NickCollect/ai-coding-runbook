---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=th
fetched_at: 2026-08-10T03:20:49.281261+00:00
title: "\u0e27\u0e34\u0e18\u0e35\u0e01\u0e32\u0e23\u0e1b\u0e49\u0e2d\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e1f\u0e25\u0e4c \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# วิธีการป้อนข้อมูลไฟล์

คำแนะนำนี้จะอธิบายวิธีต่างๆ ในการใส่ไฟล์สื่อ เช่น รูปภาพ เสียง วิดีโอ และเอกสาร เมื่อส่งคำขอไปยัง Gemini API
โดยวิธีใหม่นี้รองรับในปลายทาง Gemini API ทั้งหมด ซึ่งรวมถึง
Batch, Interactions และ Live API
การเลือกวิธีที่เหมาะสมขึ้นอยู่กับขนาดไฟล์ ตำแหน่งที่จัดเก็บข้อมูลในปัจจุบัน และความถี่ที่คุณวางแผนจะใช้ไฟล์

วิธีที่ง่ายที่สุดในการใส่ไฟล์เป็นอินพุตคือการอ่านไฟล์ในเครื่องแล้วใส่ลงในพรอมต์ ตัวอย่างต่อไปนี้แสดงวิธีอ่านไฟล์ PDF ในเครื่อง โดยวิธีนี้ PDF จะมีขนาดไม่เกิน 50 MB โปรดดูรายการประเภทอินพุตไฟล์และขีดจำกัดทั้งหมดใน
[ตารางเปรียบเทียบวิธีการป้อนข้อมูล](#method-comparison)

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
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
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
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

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## การเปรียบเทียบวิธีการป้อนข้อมูล

ตารางต่อไปนี้จะเปรียบเทียบวิธีการป้อนข้อมูลแต่ละวิธีกับขีดจำกัดของไฟล์และ Use Case ที่ดีที่สุด โปรดทราบว่าขีดจำกัดขนาดไฟล์อาจแตกต่างกันไปตามประเภทไฟล์และโมเดล/ตัวแยกคำที่ใช้ประมวลผลไฟล์

| วิธีการ | เหมาะสำหรับ | ขนาดไฟล์สูงสุด | ความต่อเนื่อง |
| --- | --- | --- | --- |
| **ข้อมูลแบบอินไลน์** | การทดสอบอย่างรวดเร็ว ไฟล์ขนาดเล็ก แอปพลิเคชันแบบเรียลไทม์ | 100 MB ต่อคำขอ/เพย์โหลด   (**50 MB สำหรับ PDF**) | ไม่มี (ส่งไปพร้อมกับทุกคำขอ) |
| **การอัปโหลด File API** | ไฟล์ขนาดใหญ่ ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์   สูงสุด 20 GB ต่อโปรเจ็กต์ | 48 ชั่วโมง |
| **การลงทะเบียน URI ของ File API GCS** | ไฟล์ขนาดใหญ่ที่อยู่ใน Google Cloud Storage อยู่แล้ว ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์ ไม่มีขีดจำกัดพื้นที่เก็บข้อมูลโดยรวม | ไม่มี (ดึงข้อมูลต่อคำขอ) การลงทะเบียนครั้งเดียวจะให้สิทธิ์เข้าถึงได้นานสูงสุด 30 วัน |
| **URL ภายนอก** | ข้อมูลสาธารณะหรือข้อมูลใน Bucket ของระบบคลาวด์ (AWS, Azure, GCS) โดยไม่ต้องอัปโหลดซ้ำ | 100 MB ต่อคำขอ/เพย์โหลด | ไม่มี (ดึงข้อมูลต่อคำขอ) |

## ข้อมูลแบบอินไลน์

สำหรับไฟล์ขนาดเล็กกว่า (ไม่เกิน 100 MB หรือ 50 MB สำหรับ PDF) คุณสามารถส่งข้อมูลในเพย์โหลดคำขอได้โดยตรง ซึ่งเป็นวิธีที่ง่ายที่สุดสำหรับการทดสอบอย่างรวดเร็วหรือแอปพลิเคชันที่จัดการข้อมูลชั่วคราวแบบเรียลไทม์ คุณสามารถระบุข้อมูลเป็นสตริงที่เข้ารหัส base64 หรืออ่านไฟล์ในเครื่องได้โดยตรง

ดูตัวอย่างการอ่านจากไฟล์ในเครื่องได้ที่ตัวอย่างที่จุดเริ่มต้นของหน้านี้

### ดึงข้อมูลจาก URL

นอกจากนี้ คุณยังดึงข้อมูลไฟล์จาก URL แปลงเป็นไบต์ แล้วใส่ลงในอินพุตได้ด้วย

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
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

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
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

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

File API ออกแบบมาสำหรับไฟล์ขนาดใหญ่ (สูงสุด 2 GB) หรือไฟล์ที่คุณต้องการใช้ในคำขอหลายรายการ

### การอัปโหลดไฟล์มาตรฐาน

อัปโหลดไฟล์ในเครื่องไปยัง Gemini API ไฟล์ที่อัปโหลดด้วยวิธีนี้จะจัดเก็บไว้ชั่วคราว (48 ชั่วโมง) และประมวลผลเพื่อให้โมเดลดึงข้อมูลได้อย่างมีประสิทธิภาพ

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[prompt, audio_file]
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
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
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
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### ลงทะเบียนไฟล์ Google Cloud Storage

หากข้อมูลอยู่ใน Google Cloud Storage อยู่แล้ว คุณไม่จำเป็นต้องดาวน์โหลดและอัปโหลดซ้ำ คุณสามารถลงทะเบียนข้อมูลกับ File API ได้โดยตรง

1. ให้สิทธิ์เข้าถึง **Service Agent** แก่แต่ละ Bucket

   1. เปิดใช้ Gemini API ในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google
   2. สร้าง Service Agent ด้วยคำสั่งต่อไปนี้

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **ให้สิทธิ์เข้าถึง Bucket พื้นที่เก็บข้อมูลแก่ Service Agent ของ Gemini API**

      ผู้ใช้ต้องกำหนดบทบาท `Storage Object Viewer`
      [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=th#storage.objectViewer)
      ให้กับตัวแทนบริการนี้ใน Bucket พื้นที่เก็บข้อมูลที่ต้องการใช้

   สิทธิ์เข้าถึงนี้จะไม่มีวันหมดอายุโดยค่าเริ่มต้น แต่คุณสามารถเปลี่ยนแปลงได้ทุกเมื่อ นอกจากนี้ คุณยังใช้
   [คำสั่ง Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=th)
   เพื่อให้สิทธิ์ได้ด้วย
2. ตรวจสอบสิทธิ์บริการ

   **ข้อกำหนดเบื้องต้น**

   - เปิดใช้ API
   - สร้างบัญชีบริการ/Agent ที่มีสิทธิ์ที่เหมาะสม

   ก่อนอื่น คุณต้องตรวจสอบสิทธิ์ในฐานะบริการที่มีสิทธิ์เข้าถึงพื้นที่เก็บข้อมูล ซึ่งวิธีการตรวจสอบสิทธิ์จะขึ้นอยู่กับสภาพแวดล้อมที่โค้ดการจัดการไฟล์จะทำงาน

   **ภายนอก Google Cloud**

   หากโค้ดทำงานจากภายนอก Google Cloud เช่น จากเดสก์ท็อป ให้ดาวน์โหลดข้อมูลเข้าสู่ระบบบัญชีจากคอนโซล Google Cloud โดยทำตามขั้นตอนต่อไปนี้

   1. ไปที่[คอนโซลบัญชีบริการ](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=th)
   2. เลือกบัญชีบริการที่เกี่ยวข้อง
   3. เลือกแท็บ**คีย์** แล้วเลือก**เพิ่มคีย์, สร้างคีย์ใหม่**
   4. เลือกประเภทคีย์ **JSON** และจดบันทึกตำแหน่งที่ดาวน์โหลดไฟล์ลงในเครื่อง

   ดูรายละเอียดเพิ่มเติมได้ในเอกสารประกอบอย่างเป็นทางการของ Google Cloud เกี่ยวกับการจัดการ[คีย์บัญชีบริการ](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=th)

   จากนั้นใช้คำสั่งต่อไปนี้เพื่อตรวจสอบสิทธิ์ คำสั่งเหล่านี้จะถือว่าไฟล์บัญชีบริการอยู่ในไดเรกทอรีปัจจุบันและมีชื่อว่า `service-account.json`

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

   ### Javascript

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

   หากคุณใช้งานใน Google Cloud โดยตรง เช่น โดยใช้ [ฟังก์ชัน Cloud Run](https://cloud.google.com/functions?hl=th) หรือ
   [อินสแตนซ์ Compute Engine](https://cloud.google.com/products/compute?hl=th) คุณจะ
   มีข้อมูลเข้าสู่ระบบโดยนัย แต่จะต้องตรวจสอบสิทธิ์อีกครั้งเพื่อให้สิทธิ์เข้าถึง
   ขอบเขตที่เหมาะสม

   ### Python

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่
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

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่
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

   ### CLI

   นี่เป็นคำสั่งแบบอินเทอร์แอกทีฟ สำหรับบริการอย่าง Compute Engine คุณสามารถแนบขอบเขตกับบริการที่ทำงานอยู่ที่ระดับการกำหนดค่าได้ ดูตัวอย่างได้ในเอกสารประกอบเกี่ยวกับบริการที่ผู้ใช้จัดการ

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. การลงทะเบียนไฟล์ (Files API)

   ใช้ Files API เพื่อลงทะเบียนไฟล์และสร้างเส้นทาง Files API ที่ใช้ใน Gemini API ได้โดยตรง

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.6-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
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

## URL HTTP ภายนอก / URL ที่ลงชื่อแล้ว

คุณสามารถส่ง URL HTTPS ที่เข้าถึงได้แบบสาธารณะหรือ URL ที่ลงชื่อไว้ล่วงหน้า (เข้ากันได้กับ
[URL ที่ลงชื่อไว้ล่วงหน้าของ S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
และ SAS ของ Azure) ในคำขอสร้างได้โดยตรง Gemini API จะดึงข้อมูลเนื้อหาอย่างปลอดภัยระหว่างการประมวลผล วิธีนี้เหมาะสำหรับไฟล์ที่มีขนาดไม่เกิน 100 MB ที่คุณไม่ต้องการอัปโหลดซ้ำ

คุณสามารถใช้ URL สาธารณะหรือ URL ที่ลงชื่อแล้วเป็นอินพุตได้โดยใช้ URL ในช่อง `file_uri`

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### Javascript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### การช่วยเหลือพิเศษ

ตรวจสอบว่า URL ที่คุณระบุไม่ได้นำไปยังหน้าที่ต้องเข้าสู่ระบบหรืออยู่หลังเพย์วอลล์ สำหรับฐานข้อมูลส่วนตัว โปรดสร้าง URL ที่ลงชื่อแล้วโดยมีสิทธิ์เข้าถึงและวันหมดอายุที่ถูกต้อง

### การตรวจสอบความปลอดภัย

ระบบจะทำการตรวจสอบการกลั่นกรองเนื้อหาใน URL เพื่อยืนยันว่า URL เป็นไปตามมาตรฐานด้านความปลอดภัยและนโยบาย (เช่น เนื้อหาที่ไม่ได้เลือกไม่รับและเนื้อหาที่อยู่หลังเพย์วอลล์) หาก URL ที่คุณระบุไม่ผ่านการตรวจสอบนี้ คุณจะได้รับ `url_retrieval_status` เป็น `URL_RETRIEVAL_STATUS_UNSAFE`

### ประเภทเนื้อหาที่รองรับ

รายการประเภทไฟล์และข้อจำกัดที่รองรับนี้มีไว้เพื่อเป็นแนวทางเบื้องต้นและไม่ครอบคลุมทั้งหมด ชุดประเภทที่รองรับจริงอาจมีการเปลี่ยนแปลงและแตกต่างกันไปตามโมเดลและเวอร์ชันตัวแยกคำที่ใช้ ประเภทที่ไม่รองรับจะทำให้เกิดข้อผิดพลาด
นอกจากนี้ การดึงข้อมูลเนื้อหาสำหรับไฟล์ประเภทเหล่านี้ในปัจจุบันรองรับเฉพาะ URL ที่เข้าถึงได้แบบสาธารณะ

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

#### ประเภทไฟล์รูปภาพ

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### ประเภทไฟล์วิดีโอ

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

- **เลือกวิธีที่เหมาะสม:** ใช้ข้อมูลแบบอินไลน์สำหรับไฟล์ขนาดเล็กและชั่วคราว
  ใช้ File API สำหรับไฟล์ขนาดใหญ่หรือไฟล์ที่ใช้บ่อย ใช้ URL ภายนอกสำหรับข้อมูลที่โฮสต์ออนไลน์อยู่แล้ว
- **ระบุประเภท MIME:** ระบุประเภท MIME ที่ถูกต้องสำหรับข้อมูลไฟล์เสมอเพื่อให้แน่ใจว่าระบบจะประมวลผลได้อย่างถูกต้อง
- **จัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดในโค้ดเพื่อจัดการปัญหาที่อาจเกิดขึ้น เช่น เครือข่ายล่ม ปัญหาการเข้าถึงไฟล์ หรือข้อผิดพลาดของ API
- **จัดการสิทธิ์ GCS:** เมื่อใช้การลงทะเบียน GCS ให้สิทธิ์เข้าถึงบทบาท `Storage Object Viewer` ที่จำเป็นเท่านั้นแก่ Service Agent ของ Gemini API ใน Bucket ที่เฉพาะเจาะจง
- **ความปลอดภัยของ URL ที่ลงชื่อแล้ว:** ตรวจสอบว่า URL ที่ลงชื่อแล้วมีเวลาหมดอายุที่เหมาะสมและสิทธิ์ที่จำกัด

## ข้อจำกัด

- ขีดจำกัดขนาดไฟล์จะแตกต่างกันไปตามวิธี (ดู [ตารางเปรียบเทียบ](#method-comparison))
  และประเภทไฟล์
- ข้อมูลแบบอินไลน์จะเพิ่มขนาดเพย์โหลดคำขอ
- การอัปโหลด File API เป็นการอัปโหลดชั่วคราวและจะหมดอายุหลังจากผ่านไป 48 ชั่วโมง
- การดึงข้อมูล URL ภายนอกจำกัดไว้ที่ 100 MB ต่อเพย์โหลดและรองรับเนื้อหาบางประเภท
- การลงทะเบียน Google Cloud Storage ต้องมีการตั้งค่า IAM ที่เหมาะสมและการจัดการโทเค็น OAuth

## ขั้นตอนถัดไป

- ลองเขียนพรอมต์มัลติโมดัลของคุณเองโดยใช้
  [Google AI Studio](http://aistudio.google.com/?hl=th)
- ดูข้อมูลเกี่ยวกับการใส่ไฟล์ในพรอมต์ได้ในคำแนะนำการประมวลผล
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=th),
  [เสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th) และ
  [เอกสาร](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)
- ดูคำแนะนำเพิ่มเติมเกี่ยวกับการออกแบบพรอมต์ เช่น การปรับพารามิเตอร์การสุ่มตัวอย่างได้ใน
  [คำแนะนำเกี่ยวกับกลยุทธ์พรอมต์](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
