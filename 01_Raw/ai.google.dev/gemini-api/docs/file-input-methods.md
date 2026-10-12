---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-TW
fetched_at: 2026-10-12T06:55:34.314358+00:00
title: "\u6a94\u6848\u8f38\u5165\u65b9\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 檔案輸入方式

本指南說明向 Gemini API 提出要求時，如何加入圖片、音訊、影片和文件等媒體檔案。所有 Gemini API 端點都支援這些新方法，包括 Batch、Interactions 和 Live API。選擇合適的方法取決於檔案大小、資料儲存位置，以及檔案的使用頻率。

如要將檔案做為輸入內容，最簡單的方法是讀取本機檔案，然後將檔案納入提示。以下範例說明如何讀取本機 PDF 檔案。透過這種方法上傳的 PDF 檔案大小上限為 50 MB。如需檔案輸入類型和限制的完整清單，請參閱「[輸入法比較表](#method-comparison)」。

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

## 輸入法比較

下表比較各輸入方式的檔案限制和最佳用途。請注意，檔案大小上限可能因檔案類型和用於處理檔案的型號或權杖化工具而異。

| 方法 | 適用情境 | 檔案大小上限 | 保留設定 |
| --- | --- | --- | --- |
| **內嵌資料** | 快速測試、小型檔案、即時應用程式。 | 每個要求或酬載 100 MB   (PDF 為 **50 MB**) | 無 (隨每個要求傳送) |
| **透過 File API 上傳** | 大型檔案、多次使用的檔案。 | 每個檔案 2 GB， 每個專案最多 20 GB | 48 小時 |
| **檔案 API GCS URI 註冊** | Google Cloud Storage 中已有的檔案、多次使用的檔案。 | 每個檔案 2 GB，沒有總儲存空間限制 | 無 (每個要求都會擷取)。一次註冊最多可存取 30 天。 |
| **外部網址** | 公用資料或雲端 bucket (AWS、Azure、GCS) 中的資料，不必重新上傳。 | 每個檔案 15 MB | 無 (每個要求都會擷取) |

## 內嵌資料

如果是較小的檔案 (小於 100 MB，PDF 檔案則為小於 50 MB)，您可以直接在要求酬載中傳遞資料。這是最簡單的方法，適用於快速測試或處理即時暫時性資料的應用程式。您可以提供 base64 編碼字串形式的資料，也可以直接讀取本機檔案。

如需從本機檔案讀取的範例，請參閱本頁開頭的範例。

### 從網址擷取

您也可以從網址擷取檔案、轉換為位元組，然後納入輸入內容。

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

File API 適用於較大的檔案 (最多 2 GB)，或您打算在多項要求中使用的檔案。

### 標準檔案上傳

將本機檔案上傳至 Gemini API。以這種方式上傳的檔案會暫時儲存 (48 小時)，並經過處理，方便模型有效檢索。

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

### 註冊 Google Cloud Storage 檔案

如果資料已儲存在 Google Cloud Storage，就不需要下載並重新上傳。您可以直接透過 File API 註冊。

1. 授予每個值區的「服務代理」存取權

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
   - 建立具備適當權限的服務帳戶或代理程式。

   您必須先以具備儲存空間物件檢視者權限的服務身分進行驗證。這項作業的執行方式取決於檔案管理程式碼的執行環境。

   **Google Cloud 以外的服務**

   如果您的程式碼是從 Google Cloud 外部 (例如桌面) 執行，請按照下列步驟，從 Google Cloud 控制台下載帳戶憑證：

   1. 瀏覽至[服務帳戶控制台](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=zh-tw)
   2. 選取相關服務帳戶
   3. 選取「金鑰」分頁，然後依序選擇「新增金鑰」和「建立新的金鑰」
   4. 選擇「JSON」金鑰類型，並記下檔案下載至您電腦的位置。

   詳情請參閱 Google Cloud 官方說明文件，瞭解如何[管理服務帳戶金鑰](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=zh-tw)。

   然後使用下列指令進行驗證。這些指令會假設服務帳戶檔案位於目前目錄中，且名為 `service-account.json`。

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

   **在 Google Cloud 上**

   如果您直接在 Google Cloud 中執行，例如使用 [Cloud Run functions](https://cloud.google.com/functions?hl=zh-tw) 或 [Compute Engine 執行個體](https://cloud.google.com/products/compute?hl=zh-tw)，您會擁有隱含憑證，但需要重新驗證，才能授予適當的範圍。

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

這是互動式指令。對於 Compute Engine 等服務，您可以在設定層級將範圍附加至執行中的服務。如需範例，請參閱[使用者管理的服務文件](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=zh-tw#using)。

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. 註冊檔案 (Files API)
   使用 Files API 註冊檔案，並產生可直接在 Gemini API 中使用的 Files API 路徑。

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

## 外部 HTTP / 簽署網址

您可以直接在要求中傳遞可公開存取的 HTTPS 網址或預先簽署的網址。Gemini API 會在處理期間安全地擷取內容。
這項功能非常適合不想重新上傳的檔案。每個檔案的大小上限為 15 MB。如要上傳較大的檔案，請使用 [File API](#file-api)。

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

### 無障礙設定

確認您提供的網址不會導向需要登入或位於付費牆後的網頁。如果是私人資料庫，請務必建立具備正確存取權限和有效期限的經簽署的網址。

### 安全檢查

系統會對網址執行內容審核檢查，確認網址符合安全和政策標準。如果網址未通過這項檢查，您會收到 `url_retrieval_status` 的 `URL_RETRIEVAL_STATUS_UNSAFE`。

### 支援的內容類型

這份支援的檔案類型和限制清單僅為初步指引，並未涵蓋所有項目。支援的有效型別組合可能會變更，且會因使用的特定模型和權杖化工具版本而異。如果類型不受支援，就會發生錯誤。
此外，擷取這些檔案類型的內容時，僅支援可公開存取的網址。

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

- **選擇合適的方法：**針對小型暫時性檔案使用內嵌資料。
  如要處理較大或經常使用的檔案，請使用 File API。使用外部網址，
  匯入已在線上託管的資料。
- **指定 MIME 類型：**請務必為檔案資料提供正確的 MIME 類型，確保系統能正確處理。
- **處理錯誤：**在程式碼中實作錯誤處理機制，管理網路連線失敗、檔案存取問題或 API 錯誤等潛在問題。

## 限制

- 檔案大小限制會因方法 (請參閱[比較表](#method-comparison)) 和檔案類型而異。
- 內嵌資料會增加要求酬載大小。
- 檔案 API 上傳作業是暫時性的，會在 48 小時後失效。
- 每個檔案的外部網址擷取上限為 15 MB，且支援特定內容類型。

## 後續步驟

- 使用 [Google AI Studio](http://aistudio.google.com/?hl=zh-tw) 撰寫自己的多模態提示。
- 如要瞭解如何在提示中加入檔案，請參閱「[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw)」、「[Audio](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw)」和「[Document processing](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)」指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-07 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-07 (世界標準時間)。"],[],[]]
