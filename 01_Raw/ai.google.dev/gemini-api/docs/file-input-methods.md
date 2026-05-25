---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-TW
fetched_at: 2026-05-25T05:18:28.366469+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 檔案輸入方式

本指南說明向 Gemini API 提出要求時，可採用哪些方式加入圖片、音訊、影片和文件等媒體檔案。所有 Gemini API 端點都支援這些新方法，包括 Batch、Interactions 和 Live API。選擇合適的方法取決於檔案大小、資料目前的儲存位置，以及您預計使用檔案的頻率。

如要將檔案做為輸入內容，最簡單的方法是讀取本機檔案，然後將檔案納入提示詞。以下範例說明如何讀取本機 PDF 檔案。透過這個方法上傳的 PDF 檔案大小不得超過 50 MB。如需檔案輸入類型和限制的完整清單，請參閱「[輸入法比較表](#method-comparison)」。

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## 輸入法比較

下表比較各種輸入方式的檔案限制和最佳用途。請注意，檔案大小上限可能會因檔案類型和用於處理檔案的模型/分詞器而異。

| 方法 | 適用情境 | 檔案大小上限 | 持續性 |
| --- | --- | --- | --- |
| **內嵌資料** | 快速測試、小型檔案、即時應用程式。 | 每個要求/酬載 100 MB   (PDF 檔案為 **50 MB**) | 無 (隨每個要求傳送) |
| **檔案 API 上傳** | 大型檔案、多次使用的檔案。 | 每個檔案 2 GB， 每個專案最多 20 GB | 48 小時 |
| **File API GCS URI 註冊** | 已存放在 Google Cloud Storage 的大型檔案、多次使用的檔案。 | 每個檔案 2 GB，沒有總儲存空間限制 | 無 (系統會根據要求擷取)。一次註冊最多可存取 30 天。 |
| **外部網址** | 公用資料或雲端儲存空間 (AWS、Azure、GCS) 中的資料，不必重新上傳。 | 每個要求/酬載 100 MB | 無 (每次要求都會擷取) |

## 內嵌資料

如果是較小的檔案 (小於 100 MB，PDF 檔案則小於 50 MB)，您可以直接在要求酬載中傳遞資料。這是最簡單的方法，適用於快速測試或處理即時暫時性資料的應用程式。您可以提供 base64 編碼字串形式的資料，也可以直接讀取本機檔案。

如需從本機檔案讀取的範例，請參閱本頁開頭的範例。

### 從網址擷取

您也可以從網址擷取檔案、轉換為位元組，然後納入輸入內容。

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
  model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

File API 適用於較大的檔案 (最多 2 GB)，或您打算在多項要求中使用的檔案。

### 標準檔案上傳

將本機檔案上傳至 Gemini API。以這種方式上傳的檔案會暫時儲存 (48 小時)，並經過處理，方便模型有效率地擷取內容。

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### 註冊 Google Cloud Storage 檔案

如果資料已儲存在 Google Cloud Storage，就不需要下載並重新上傳。您可以直接透過 File API 註冊。

1. 授予**服務代理**每個 bucket 的存取權

   1. 在 Google Cloud 專案中啟用 Gemini API。
   2. 建立服務代理：

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **授予 Gemini API 服務代理讀取儲存空間 bucket 的權限**。

      使用者必須在打算使用的特定儲存空間 bucket 中，為這個服務代理指派 `Storage Object Viewer`
      [IAM 角色](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=zh-tw#storage.objectViewer)。

   這項存取權預設不會過期，但隨時可以變更。您也可以使用 [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=zh-tw) 指令授予權限。
2. 驗證服務

   **必要條件**

   - 啟用 API
   - 建立具備適當權限的服務帳戶/代理程式。

   您必須先以具備 Storage 物件檢視者權限的服務身分進行驗證。這取決於檔案管理程式碼的執行環境。

   **Google Cloud 以外**

   如果您的程式碼是在 Google Cloud 以外的位置 (例如桌面) 執行，請按照下列步驟，從 Google Cloud 控制台下載帳戶憑證：

   1. 瀏覽至[服務帳戶控制台](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=zh-tw)
   2. 選取相關服務帳戶
   3. 選取「金鑰」分頁，然後依序選擇「新增金鑰」和「建立新的金鑰」
   4. 選擇「JSON」金鑰類型，並記下檔案下載到電腦的位置。

   詳情請參閱 Google Cloud 官方說明文件，瞭解如何[管理服務帳戶金鑰](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=zh-tw)。

   然後使用下列指令進行驗證。這些指令假設您的服務帳戶檔案位於目前目錄中，且名為 `service-account.json`。

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

   **在 Google Cloud 中**

   如果您直接在 Google Cloud 中執行 (例如使用 [Cloud Run 函式](https://cloud.google.com/functions?hl=zh-tw)或 [Compute Engine 執行個體](https://cloud.google.com/products/compute?hl=zh-tw))，您會擁有隱含憑證，但需要重新驗證，才能授予適當的範圍。

   ### Python

   這段程式碼預期服務會在可自動取得[應用程式預設憑證](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-tw)的環境中執行，例如 Cloud Run 或 Compute Engine。

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   這段程式碼預期服務會在可自動取得[應用程式預設憑證](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-tw)的環境中執行，例如 Cloud Run 或 Compute Engine。

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

   這項指令是互動式指令，對於 Compute Engine 等服務，您可以在設定層級將範圍附加至執行中的服務。如需範例，請參閱[使用者自行管理的服務文件](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=zh-tw#using)。

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. 檔案註冊 (Files API)

   使用 Files API 註冊檔案，並產生可直接在 Gemini API 中使用的 Files API 路徑。

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
       model="gemini-3.5-flash",
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

## 外部 HTTP / 已簽章網址

您可以在生成要求中直接傳遞可公開存取的 HTTPS 網址或預先簽署的網址 (與 [S3 預先簽署的網址](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)和 Azure SAS 相容)。Gemini API 會在處理期間安全地擷取內容。如果檔案大小不超過 100 MB，且您不想重新上傳，這個方法就非常適合。

您可以使用「URLs」(網址) `file_uri` 欄位中的網址，以公開或已簽署的網址做為輸入內容。

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
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

### 無障礙設定

確認提供的網址不會導向需要登入或位於付費牆後的網頁。如果是私人資料庫，請務必建立具備正確存取權限和有效期限的經簽署網址。

### 安全檢查

系統會對網址執行內容審核檢查，確認網址符合安全和政策標準 (例如未停用及設有付費牆的內容)。如果提供的網址未通過這項檢查，您會收到`url_retrieval_status`的`URL_RETRIEVAL_STATUS_UNSAFE`。

### 支援的內容類型

這份支援的檔案類型和限制清單僅為初步指引，並未涵蓋所有項目。支援的有效型別組合可能會變更，且會因使用的特定模型和權杖化工具版本而異。如果類型不受支援，系統會顯示錯誤訊息。此外，目前僅支援可公開存取的網址，才能擷取這些檔案類型的內容。

#### 文字檔案類型

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### 應用程式檔案類型

- `application/json`
- `application/pdf`

#### 圖片檔案類型

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### 影片檔案類型

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 最佳做法

- **選擇合適的方法：**針對小型暫時性檔案使用內嵌資料。如要處理較大或經常使用的檔案，請使用 File API。使用外部網址，
  取得已在線上代管的資料。
- **指定 MIME 類型：**請務必為檔案資料提供正確的 MIME 類型，確保系統能正確處理。
- **處理錯誤：**在程式碼中實作錯誤處理機制，管理網路連線失敗、檔案存取問題或 API 錯誤等潛在問題。
- **管理 GCS 權限：**使用 GCS 註冊時，請只在特定值區中授予 Gemini API 服務代理必要的 `Storage Object Viewer` 角色。
- **經簽署的網址安全性：**請確保經簽署的網址的到期時間適當，且權限有限。

## 限制

- 檔案大小上限會因方法 (請參閱[比較表](#method-comparison)) 和檔案類型而異。
- 內嵌資料會增加要求酬載大小。
- File API 上傳的檔案為暫時性質，會在 48 小時後失效。
- 每個酬載的外部網址擷取上限為 100 MB，且支援特定內容類型。
- 如要註冊 Google Cloud Storage，必須正確設定 IAM 和 OAuth 權杖管理。

## 後續步驟

- 使用 [Google AI Studio](http://aistudio.google.com/?hl=zh-tw) 撰寫自己的多模態提示。
- 如要瞭解如何在提示中加入檔案，請參閱「[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw)」、「[Audio](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw)」和「[Document processing](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)」指南。
- 如要進一步瞭解如何設計提示 (例如微調取樣參數)，請參閱「[提示策略](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=zh-tw)」指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
