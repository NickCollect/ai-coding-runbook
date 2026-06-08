---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=ko
fetched_at: 2026-06-08T05:33:15.019029+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 파일 입력 방법

이 가이드에서는 Gemini API에 요청할 때 이미지, 오디오, 동영상, 문서와 같은 미디어 파일을 포함하는 다양한 방법을 설명합니다.
새 메서드는 일괄, 상호작용, Live API를 비롯한 모든 Gemini API 엔드포인트에서 지원됩니다.
적절한 방법을 선택하는 것은 파일의 크기, 데이터가 저장된 위치, 파일 사용 빈도에 따라 달라집니다.

파일을 입력으로 포함하는 가장 간단한 방법은 로컬 파일을 읽고 프롬프트에 포함하는 것입니다. 다음 예에서는 로컬 PDF 파일을 읽는 방법을 보여줍니다. 이 메서드의 PDF는 50MB로 제한됩니다. 파일 입력 유형 및 제한의 전체 목록은 [입력 방법 비교 표](#method-comparison)를 참고하세요.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
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

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
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

## 입력 방법 비교

다음 표에서는 각 입력 방법과 파일 제한, 최적의 사용 사례를 비교합니다. 파일 크기 제한은 파일 형식과 파일을 처리하는 데 사용된 모델 또는 토크나이저에 따라 다를 수 있습니다.

| 메서드 | 권장 용도 | 최대 파일 크기 | 지속성 |
| --- | --- | --- | --- |
| **인라인 데이터** | 빠른 테스트, 작은 파일, 실시간 애플리케이션 | 요청 또는 페이로드당 100MB   (**PDF의 경우 50MB**) | 없음 (모든 요청과 함께 전송됨) |
| **파일 API 업로드** | 큰 파일, 여러 번 사용된 파일 | 파일당 2GB,   프로젝트당 최대 20GB | 48시간 |
| **파일 API GCS URI 등록** | 이미 Google Cloud Storage에 있는 대용량 파일, 여러 번 사용되는 파일 | 파일당 2GB, 전체 스토리지 제한 없음 | 없음 (요청별로 가져옴) 한 번 등록하면 최대 30일 동안 액세스할 수 있습니다. |
| **외부 URL** | 다시 업로드하지 않고 공개 데이터 또는 클라우드 버킷 (AWS, Azure, GCS)의 데이터 | 요청/페이로드당 100MB | 없음 (요청별로 가져옴) |

## 인라인 데이터

작은 파일 (100MB 미만 또는 PDF의 경우 50MB)의 경우 요청 페이로드에서 데이터를 직접 전달할 수 있습니다. 이는 빠른 테스트나 실시간 임시 데이터를 처리하는 애플리케이션에 가장 간단한 방법입니다. base64로 인코딩된 문자열로 데이터를 제공하거나 로컬 파일을 직접 읽어 데이터를 제공할 수 있습니다.

로컬 파일에서 읽어오는 예시는 이 페이지의 시작 부분에 있는 예시를 참고하세요.

### URL에서 가져오기

URL에서 파일을 가져와 바이트로 변환하고 입력에 포함할 수도 있습니다.

### Python

```
from google import genai
import httpx
import base64

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
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
"model": "gemini-3.5-flash",
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
    -H "Api-Revision: 2026-05-20" \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

File API는 더 큰 파일 (최대 2GB) 또는 여러 요청에서 사용하려는 파일을 위해 설계되었습니다.

### 표준 파일 업로드

로컬 파일을 Gemini API에 업로드합니다. 이 방식으로 업로드된 파일은 일시적으로 (48시간) 저장되며 모델에서 효율적으로 검색할 수 있도록 처리됩니다.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### 자바스크립트

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
    model: "gemini-3.5-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
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
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Google Cloud Storage 파일 등록

데이터가 이미 Google Cloud Storage에 있는 경우 다운로드하여 다시 업로드할 필요가 없습니다. File API에 직접 등록할 수 있습니다.

1. 각 버킷에 대한 **서비스 에이전트** 액세스 권한 부여

   1. Google Cloud 프로젝트에서 Gemini API를 사용 설정합니다.
   2. 서비스 에이전트를 만듭니다.

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. 스토리지 버킷을 읽을 수 있는 **Gemini API 서비스 에이전트 권한을 부여**합니다.

      사용자는 사용할 특정 스토리지 버킷에서 이 서비스 에이전트에게 `Storage Object Viewer`
      [IAM 역할](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=ko#storage.objectViewer)을 할당해야 합니다.

   이 액세스 권한은 기본적으로 만료되지 않지만 언제든지 변경할 수 있습니다. [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=ko) 명령어를 사용하여 권한을 부여할 수도 있습니다.
2. 서비스 인증

   **기본 요건**

   - API 사용 설정
   - 적절한 권한이 있는 서비스 계정 또는 에이전트를 만듭니다.

   먼저 스토리지 객체 뷰어 권한이 있는 서비스로 인증해야 합니다. 이 작업이 실행되는 방식은 파일 관리 코드가 실행되는 환경에 따라 다릅니다.

   **Google Cloud 외부**

   데스크톱과 같이 Google Cloud 외부에서 코드를 실행하는 경우 다음 단계에 따라 Google Cloud 콘솔에서 계정 사용자 인증 정보를 다운로드하세요.

   1. [서비스 계정 콘솔](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ko)로 이동합니다.
   2. 관련 서비스 계정 선택
   3. **키** 탭을 선택하고 **키 추가, 새 키 만들기**를 선택합니다.
   4. **JSON** 키 유형을 선택하고 머신에서 파일이 다운로드된 위치를 기록해 둡니다.

   자세한 내용은 [서비스 계정 키 관리](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=ko)에 관한 공식 Google Cloud 문서를 참고하세요.

   그런 다음 다음 명령어를 사용하여 인증합니다. 이 명령어는 서비스 계정 파일이 현재 디렉터리에 있으며 이름이 `service-account.json`이라고 가정합니다.

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

   **Google Cloud 환경**

   [Cloud Run 함수](https://cloud.google.com/functions?hl=ko) 또는 [Compute Engine 인스턴스](https://cloud.google.com/products/compute?hl=ko)를 사용하여 Google Cloud에서 직접 실행하는 경우 암시적 사용자 인증 정보가 있지만 적절한 범위를 부여하려면 다시 인증해야 합니다.

   ### Python

   이 코드는 Cloud Run 또는 Compute Engine과 같이 [애플리케이션 기본 사용자 인증 정보](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ko)를 자동으로 가져올 수 있는 환경에서 서비스가 실행된다고 가정합니다.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### 자바스크립트

   이 코드는 Cloud Run 또는 Compute Engine과 같이 [애플리케이션 기본 사용자 인증 정보](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ko)를 자동으로 가져올 수 있는 환경에서 서비스가 실행된다고 가정합니다.

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

   이는 대화형 명령어입니다. Compute Engine과 같은 서비스의 경우 구성 수준에서 실행 중인 서비스에 범위를 연결할 수 있습니다. 예는 [사용자 관리 서비스 문서](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=ko#using)를 참고하세요.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. 파일 등록 (Files API)

   Files API를 사용하여 파일을 등록하고 Gemini API에서 직접 사용할 수 있는 Files API 경로를 생성합니다.

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
       model="gemini-3.5-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### 자바스크립트

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
               model: "gemini-3.5-flash",
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

## 외부 HTTP / 서명된 URL

공개적으로 액세스 가능한 HTTPS URL 또는 사전 서명된 URL을 요청에 직접 전달할 수 있습니다. Gemini API는 처리 중에 콘텐츠를 안전하게 가져옵니다.
다시 업로드하지 않을 최대 100MB 크기의 파일에 적합합니다.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
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
      -H "Api-Revision: 2026-05-20" \
      -d '{
          "model": "gemini-3.5-flash",
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

### 접근성

제공한 URL이 로그인이 필요하거나 페이월이 적용된 페이지로 연결되지 않는지 확인합니다. 비공개 데이터베이스의 경우 올바른 액세스 권한과 만료가 있는 서명된 URL을 만들어야 합니다.

### 안전 확인

시스템은 URL이 안전 및 정책 표준을 충족하는지 확인하기 위해 URL에 대한 콘텐츠 검토를 수행합니다. URL이 이 검사를 통과하지 못하면 `URL_RETRIEVAL_STATUS_UNSAFE`의 `url_retrieval_status`가 표시됩니다.

### 지원되는 콘텐츠 유형

지원되는 파일 형식 및 제한사항 목록은 초기 안내로 제공되며 모든 내용을 포함하지는 않습니다. 지원되는 유형의 유효한 집합은 변경될 수 있으며 사용 중인 특정 모델 및 토큰화 도구 버전에 따라 다를 수 있습니다. 지원되지 않는 유형은 오류를 발생시킵니다.
또한 이러한 파일 형식의 콘텐츠 검색은 공개적으로 액세스할 수 있는 URL만 지원합니다.

#### 텍스트 파일 형식

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### 애플리케이션 파일 형식

- `application/json`
- `application/pdf`

#### 이미지 파일 형식

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## 권장사항

- **올바른 방법 선택:** 작고 일시적인 파일에는 인라인 데이터를 사용합니다.
  크기가 크거나 자주 사용하는 파일에는 File API를 사용하세요. 이미 온라인에 호스팅된 데이터에는 외부 URL을 사용합니다.
- **MIME 유형 지정:** 올바른 처리를 위해 항상 파일 데이터에 올바른 MIME 유형을 제공하세요.
- **오류 처리:** 코드에서 오류 처리를 구현하여 네트워크 오류, 파일 액세스 문제 또는 API 오류와 같은 잠재적인 문제를 관리합니다.

## 제한사항

- 파일 크기 제한은 방법 ([비교 표](#method-comparison) 참고)과 파일 유형에 따라 다릅니다.
- 인라인 데이터는 요청 페이로드 크기를 늘립니다.
- 파일 API 업로드는 임시이며 48시간 후에 만료됩니다.
- 외부 URL 가져오기는 페이로드당 100MB로 제한되며 특정 콘텐츠 유형을 지원합니다.

## 다음 단계

- [Google AI Studio](http://aistudio.google.com/?hl=ko)를 사용하여 나만의 멀티모달 프롬프트를 작성해 보세요.
- 프롬프트에 파일을 포함하는 방법에 관한 자세한 내용은 [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=ko), [오디오](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ko), [문서 처리](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ko) 가이드를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
