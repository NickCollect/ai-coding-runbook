---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=zh-CN
fetched_at: 2026-09-28T06:14:19.888120+00:00
title: "\u6587\u4ef6\u8f93\u5165\u65b9\u6cd5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 文件输入方法

本指南介绍了在向 Gemini API 发出请求时，您可以通过哪些不同的方式来添加媒体文件，例如图片、音频、视频和文档。
所有 Gemini API 端点（包括
Batch、Interactions and Live API
）都支持这些新方法。选择正确的方法取决于文件的大小、数据的当前存储位置以及您计划使用文件的频率。

将文件作为输入的最简单方法是读取本地文件并将其添加到提示中。以下示例展示了如何读取本地 PDF 文件。对于此方法，PDF 的大小上限为 50MB。如需查看文件
输入类型和限制的完整列表，请参阅
[输入方法比较表](#method-comparison)。

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

## 输入方法比较

下表比较了每种输入方法的文件限制和最佳使用场景。请注意，文件大小限制可能会因文件类型以及用于处理文件的模型/分词器而异。

| 方法 | 适用场景 | 文件大小的最大值 | 持久性 |
| --- | --- | --- | --- |
| **内嵌数据** | 快速测试、小文件、实时应用。 | 每个请求/载荷 100 MB   (**PDF 为 50 MB**) | 无（随每个请求发送） |
| **File API 上传** | 大文件、多次使用的文件。 | 每个文件 2 GB，  每个项目最多 20 GB | 48 小时 |
| **File API GCS URI 注册** | 已在 Google Cloud Storage 中的大文件、多次使用的文件。 | 每个文件 2 GB，无总体存储空间限制 | 无（按请求提取）。一次性注册最多可提供 30 天的访问权限。 |
| **外部网址** | 无需重新上传即可访问云端存储分区（AWS、Azure、GCS）中的公开数据或数据。 | 每个请求/载荷 100 MB | 无（按请求提取） |

## 内嵌数据

对于较小的文件（小于 100MB，或 PDF 小于 50MB），您可以直接在请求载荷中传递数据。对于处理实时瞬态数据的快速测试或应用，这是最简单的方法。您可以将数据作为 base64 编码的字符串提供，也可以直接读取本地文件。

如需查看从本地文件读取数据的示例，请参阅本页开头的示例。

### 从网址提取

您还可以从网址提取文件，将其转换为字节，并将其添加到输入中。

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

File API 专为较大的文件（最大 2GB）或您打算在多个请求中使用的文件而设计。

### 标准文件上传

将本地文件上传到 Gemini API。以这种方式上传的文件会暂时存储（48 小时），并经过处理，以便模型高效检索。

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

### 注册 Google Cloud Storage 文件

如果您的数据已在 Google Cloud Storage 中，则无需下载并重新上传。您可以直接使用 File API 注册。

1. 向每个存储分区授予**服务代理** 访问权限

   1. 在 Google Cloud 云项目中启用 Gemini API。
   2. 创建服务代理：

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **授予 Gemini API 服务代理权限** 以读取您的存储分区。

      用户需要在他们打算使用的特定存储分区上向此服务代理分配 `Storage Object Viewer`
      [IAM 角色](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=zh-cn#storage.objectViewer)
      。

   默认情况下，此访问权限不会过期，但可以随时更改。您还可以使用
   [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=zh-cn)
   命令来授予权限。
2. 对您的服务进行身份验证

   **前提条件**

   - 启用 API
   - 创建具有适当权限的服务账号/代理。

   您首先需要以具有存储对象查看器权限的服务的身份进行身份验证。具体如何操作取决于文件管理代码将在哪个环境中运行。

   **在 Google Cloud 之外**

   如果您的代码在 Google Cloud 之外（例如桌面设备）运行，请按照以下步骤从 Google Cloud 控制台下载账号凭据：

   1. 浏览到[服务账号控制台](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=zh-cn)
   2. 选择相关服务账号
   3. 选择**密钥** 标签页，然后依次选择**添加密钥、创建新密钥**
   4. 选择 **JSON** 密钥类型，并记下文件下载到您计算机上的哪个位置。

   如需了解详情，请参阅有关 [服务账号密钥
   管理的 Google Cloud 官方文档](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=zh-cn)。

   然后，使用以下命令进行身份验证。这些命令假定您的服务账号文件位于当前目录中，名为 `service-account.json`。

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

   **在 Google Cloud 上**

   如果您直接在 Google Cloud 中运行（例如使用 [Cloud
   Run 函数](https://cloud.google.com/functions?hl=zh-cn)或
   [Compute Engine 实例](https://cloud.google.com/products/compute?hl=zh-cn)），您将
   拥有隐式凭据，但需要重新进行身份验证以授予
   适当的权限范围。

   ### Python

   此代码假定服务在可以自动获取
   [应用默认凭证](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-cn)
   的环境（例如 Cloud Run 或 Compute Engine）中运行。

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   此代码假定服务在可以自动获取
   [应用默认凭证](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-cn)
   的环境（例如 Cloud Run 或 Compute Engine）中运行。

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

   这是一个互动式命令。对于 Compute Engine 等服务，您可以在配置级别将权限范围附加到正在运行的服务。如需查看示例，请参阅[用户管理的服务
   文档](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=zh-cn#using)
   。

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. 文件注册 (Files API)

   使用 Files API 注册文件，并生成可直接在 Gemini API 中使用的 Files API 路径。

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

## 外部 HTTP / 签名网址

您可以直接在生成请求中传递可公开访问的 HTTPS 网址或预签名网址（与
[S3 预签名
网址](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
和 Azure SAS 兼容）。Gemini API 将在处理期间安全地提取内容。这非常适合您不想重新上传的最大 100MB 的文件。

您可以使用 `file_uri` 字段中的网址将公开网址或签名网址用作输入。

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

### JavaScript

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

### 无障碍

验证您提供的网址不会指向需要登录或付费的网页。对于私有数据库，请确保您创建的签名网址具有正确的访问权限和有效期。

### 安全检查

系统会对网址执行内容审核检查，以确认其符合安全和政策标准（例如，未选择停用且付费内容）。如果您提供的网址未通过此检查，您将获得 `url_retrieval_status` 的 `URL_RETRIEVAL_STATUS_UNSAFE`。

### 支持的内容类型

此支持的文件类型和限制列表旨在提供初步指导，并不全面。支持的有效类型集可能会发生变化，并且可能会因所使用的特定模型和分词器版本而异。不支持的类型会导致错误。
此外，目前仅支持使用可公开访问的网址检索这些文件类型的内容。

#### 文本文件类型

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### 应用文件类型

- `application/json`
- `application/pdf`

#### 图片文件类型

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### 视频文件类型

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 最佳实践

- **选择正确的方法** ：对于较小的瞬态文件，请使用内嵌数据。
  对于较大或经常使用的文件，请使用 File API。对于已在线托管的数据，请使用外部网址。
- **指定 MIME 类型** ：请务必为文件数据提供正确的 MIME 类型，以确保正确处理。
- **处理错误** ：在代码中实现错误处理，以管理潜在问题，例如网络故障、文件访问问题或 API 错误。
- **管理 GCS 权限** ：使用 GCS 注册时，仅向 Gemini API 服务代理授予特定存储分区上必要的 `Storage Object Viewer` 角色。
- **签名网址安全性** ：确保签名网址具有适当的有效期和有限的权限。

## 限制

- 文件大小限制因方法（请参阅[比较表](#method-comparison)）
  和文件类型而异。
- 内嵌数据会增加请求载荷大小。
- File API 上传是临时的，会在 48 小时后过期。
- 外部网址提取限制为每个载荷 100MB，并且支持特定的内容类型。
- Google Cloud Storage 注册需要正确的 IAM 设置和 OAuth 令牌管理。

## 后续步骤

- 尝试使用
  [Google AI Studio](http://aistudio.google.com/?hl=zh-cn)编写自己的多模态提示。
- 如需了解如何在提示中添加文件，请参阅
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn)、
  [音频](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)和
  [文档处理](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)指南。
- 如需获得有关提示设计的更多指导（例如调整抽样参数），请参阅
  [提示策略](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
