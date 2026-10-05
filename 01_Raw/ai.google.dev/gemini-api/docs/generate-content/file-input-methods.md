---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=ja
fetched_at: 2026-10-05T06:30:24.617272+00:00
title: "\u30d5\u30a1\u30a4\u30eb\u5165\u529b\u30e1\u30bd\u30c3\u30c9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# ファイル入力メソッド

このガイドでは、Gemini API にリクエストを行う際に、画像、音声、動画、ドキュメントなどのメディア ファイルを含めるさまざまな方法について説明します。新しいメソッドは、Batch API、Interactions API、Live API など、すべての Gemini API エンドポイントでサポートされています。適切な方法を選択するかどうかは、ファイルのサイズ、データの現在の保存場所、ファイルの利用頻度によって異なります。

ファイルを入力として含める最も簡単な方法は、ローカル ファイルを読み取ってプロンプトに含めることです。次の例は、ローカルの PDF ファイルを読み取る方法を示しています。この方法では、PDF は 50 MB に制限されます。ファイル入力の種類と上限の完全なリストについては、[入力方法の比較表](#method-comparison)をご覧ください。

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## 入力方法の比較

次の表は、各入力方法とファイルの上限、最適なユースケースを比較したものです。ファイルサイズの上限は、ファイルの種類と、ファイルの処理に使用されるモデル/トークナイザーによって異なる場合があります。

| メソッド | 最適な用途 | 最大ファイルサイズ | 永続性 |
| --- | --- | --- | --- |
| **インライン データ** | 迅速なテスト、小容量ファイル、リアルタイム アプリケーション。 | リクエスト/ペイロードあたり 100 MB  （**PDF の場合は 50 MB**） | なし（すべてのリクエストで送信） |
| **ファイル API アップロード** | サイズの大きなファイル、複数回使用されるファイル。 | ファイルあたり 2 GB、  プロジェクトあたり最大 20 GB | 48 時間 |
| **File API GCS URI の登録** | Google Cloud Storage にすでに保存されている大きなファイル、複数回使用されるファイル。 | 1 ファイルあたり 2 GB、保存容量の合計に制限なし | なし（リクエストごとに取得）。1 回の登録で最大 30 日間アクセスできます。 |
| **外部 URL** | パブリック データまたはクラウド バケット（AWS、Azure、GCS）内のデータを再アップロードせずに使用できます。 | リクエスト/ペイロードあたり 100 MB | なし（リクエストごとに取得） |

## インライン データ

小さいファイル（100 MB 未満、PDF の場合は 50 MB 未満）の場合は、リクエスト ペイロードでデータを直接渡すことができます。これは、リアルタイムの一時データを処理するクイック テストやアプリケーションに最適な最も簡単な方法です。データは、Base64 エンコード文字列として提供するか、ローカル ファイルを直接読み取って提供できます。

ローカル ファイルから読み取る例については、このページの冒頭の例をご覧ください。

### URL から取得する

URL からファイルを取得し、バイトに変換して入力に含めることもできます。

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
  model="gemini-3.8-flash",
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
    const pdfResp = await fetch(docUrl)
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
        model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

File API は、大きなファイル（最大 2 GB）や複数のリクエストで使用するファイルを対象に設計されています。

### 標準のファイル アップロード

ローカル ファイルを Gemini API にアップロードします。この方法でアップロードされたファイルは一時的に（48 時間）保存され、モデルによる効率的な取得のために処理されます。

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

### Google Cloud Storage ファイルを登録する

データがすでに Google Cloud Storage にある場合は、ダウンロードして再アップロードする必要はありません。File API に直接登録できます。

1. 付与**サービスエージェント**各バケットへのアクセス

   1. Google Cloud プロジェクトで Gemini API を有効にしてください。
   2. サービスエージェントを作成します。

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Gemini API サービスエージェントにストレージバケットを読み取る権限を付与します。**

      ユーザーは、使用する特定のストレージバケットに対して、このサービスエージェントに `Storage Object Viewer`
      [IAM ロール](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=ja#storage.objectViewer) を割り当てる必要があります。

   このアクセス権はデフォルトでは期限切れになりませんが、いつでも変更できます。また、[Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=ja)権限を付与するためのコマンド。
2. サービスを認証する

   **前提条件**

   - API を有効にする
   - 適切な権限を持つサービスアカウント／エージェントを作成します。

   まず、ストレージオブジェクト閲覧権限を持つサービスとして認証を行う必要があります。これがどのように起こるかは、ファイル管理コードが実行される環境によって異なります。

   **Google Cloud 以外**

   コードがデスクトップなど、Google Cloud の外部で実行されている場合は、以下の手順で Google Cloud Console からアカウント認証情報をダウンロードしてください。

   1. [サービスアカウントコンソール](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ja)へ移動します
   2. 該当するサービスアカウントを選択してください。
   3. 選択してください**キー**タブを選択して**キーの追加、新しいキーの作成**
   4. キータイプとして**JSON**を選択し、ファイルがマシン上のどこにダウンロードされたかをメモしてください。

   詳細については、[サービスアカウントキー管理](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=ja)に関する公式の Google Cloud ドキュメントを参照してください。

   次に、以下のコマンドを使用して認証を行います。これらのコマンドは、サービスアカウントファイルが現在のディレクトリにあり、名前が `service-account.json` であることを前提としています。

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

   **Google Cloud**

   例えば、[Cloud Run 関数](https://cloud.google.com/functions?hl=ja)や[Compute Engine インスタンス](https://cloud.google.com/products/compute?hl=ja)を使用して Google Cloud で直接実行している場合は、暗黙の認証情報が付与されますが、適切なスコープを付与するために再認証する必要があります。

   ### Python

   このコードは、Cloud Run や Compute Engine など、[アプリケーションのデフォルト認証情報](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ja) を自動的に取得できる環境でサービスが実行されていることを前提としています。

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   このコードは、Cloud Run や Compute Engine など、[アプリケーションのデフォルト認証情報](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ja) を自動的に取得できる環境でサービスが実行されていることを前提としています。

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

   これは対話型のコマンドです。Compute Engine のようなサービスの場合、構成レベルで実行中のサービスにスコープを割り当てることができます。例については、[ユーザー管理サービスドキュメント](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=ja#using)を参照してください。

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. ファイル登録（ファイル API）

   ファイル API を使用してファイルを登録し、Gemini API で直接使用できるファイル API パスを生成します。

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
       model="gemini-3.8-flash",
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

## 外部 HTTP / 署名付き URL

公開アクセス可能な HTTPS URL または事前署名された URL ([S3 署名付き URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) （Azure SAS を含む）を生成リクエストに直接含めてください。Gemini API は、処理中にコンテンツを安全に取得します。これは、再アップロードしたくない 100MB までのファイルに最適です。

`file_uri` フィールドの URL を使用することで、公開 URL または署名付き URL を入力として使用できます。

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
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

### ユーザー補助

提供された URL が、ログインが必要なページや有料コンテンツに繋がっていないことを確認してください。プライベートデータベースの場合は、適切なアクセス権限と有効期限を設定した署名付き URL を作成してください。

### 安全チェック

システムは URL に対してコンテンツモデレーションチェックを実行し、安全性およびポリシー基準（オプトアウトされていないコンテンツや有料コンテンツなど）を満たしていることを確認します。提供された URL がこのチェックに失敗した場合は、`url_retrieval_status` または `URL_RETRIEVAL_STATUS_UNSAFE` が返されます。

### サポートされているコンテンツの種類

このサポート対象ファイル形式と制限事項のリストは、あくまでも初期的なガイダンスであり、網羅的なものではありません。実際にサポートされる型セットは変更される可能性があり、使用する特定のモデルやトークナイザーのバージョンによって異なる場合があります。サポートされていない型を使用するとエラーが発生します。
さらに、これらのファイルタイプのコンテンツ取得は、現時点では公開アクセス可能な URL のみをサポートしています。

#### テキストファイルの種類

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### アプリケーションファイルの種類

- `application/json`
- `application/pdf`

#### 画像ファイル形式

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### 動画ファイル形式

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## ベスト プラクティス

- **適切な方法を選択してください:** 小さくて一時的なファイルにはインラインデータを使用します。
  サイズの大きいファイルや頻繁に使用するファイルには、ファイル API を使用してください。既にオンラインでホストされているデータには、外部 URL を使用してください。
- **MIME タイプの指定:** 適切な処理を保証するために、ファイルデータには常に正しい MIME タイプを指定してください。
- **エラー処理:** ネットワーク障害、ファイルアクセス問題、API エラーなどの潜在的な問題に対処するために、コードにエラー処理を実装します。
- **GCS 権限の管理:** GCS 登録を使用する場合は、特定のバケットに対して必要な`Storage Object Viewer`ロールのみを Gemini API サービスエージェントに付与します。
- **署名付き URL のセキュリティ:**署名付き URL には適切な有効期限と制限された権限があることを確認してください。

## 制限事項

- ファイルサイズの制限は方法によって異なります（参照）[比較表](#method-comparison)）とファイルの種類。
- インラインデータはリクエストのペイロードサイズを増加させます。
- ファイル API によるアップロードは一時的なものであり、48 時間後に期限切れとなります。
- 外部 URL の取得は、ペイロードあたり 100MB に制限されており、特定のコンテンツタイプのみがサポートされています。
- Google Cloud Storage への登録には、適切な IAM 設定と OAuth トークン管理が必要です。

## 次のステップ

- [Google AI Studio](http://aistudio.google.com/?hl=ja)を使って、独自のマルチモーダルプロンプトを作成してみてください。
- プロンプトにファイルを含める方法については、[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=ja)、[音声](https://ai.google.dev/gemini-api/docs/audio?hl=ja)、[ドキュメント処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)の各ガイドをご覧ください。
- サンプリング パラメータのチューニングなど、プロンプト設計に関するその他のガイダンスについては、[プロンプト戦略](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)ガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-01 UTC。"],[],[]]
