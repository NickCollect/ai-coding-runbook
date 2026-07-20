---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=ja
fetched_at: 2026-07-20T04:49:10.827106+00:00
title: "\u30b3\u30f3\u30c6\u30ad\u30b9\u30c8\u306e\u30ad\u30e3\u30c3\u30b7\u30e5\u4fdd\u5b58 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# コンテキストのキャッシュ保存

一般的な AI ワークフローでは、同じ入力トークンをモデルに何度も渡すことがあります。Gemini API には、次の 2
つの異なるキャッシュ保存メカニズムが用意されています。

- 暗黙的なキャッシュ保存（Gemini 2.5 以降のモデルで自動的に有効になります。費用削減は保証されません）
- 明示的なキャッシュ保存（ほとんどのモデルで手動で有効にできます。費用削減が保証されます）

明示的なキャッシュ保存は、費用削減を保証したい場合に便利ですが、デベロッパーの作業が追加されます。

## 暗黙的なキャッシュ保存

暗黙的なキャッシュ保存は、Gemini 2.5 以降のすべてのモデルでデフォルトで有効になっています。リクエストがキャッシュにヒットした場合、費用削減が自動的に適用されます。これを有効にするために必要な操作はありません。コンテキスト
キャッシュ保存の最小入力トークン数は、モデルごとに次の表に示されています。

| モデル | トークン数の最小制限 |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro プレビュー版 | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

暗黙的なキャッシュ ヒットの可能性を高めるには:

- 大きくて一般的なコンテンツをプロンプトの先頭に配置する
- 短い時間で同様の接頭辞を持つリクエストを送信する

キャッシュ ヒットしたトークンの数は、レスポンス オブジェクトの `usage_metadata` フィールドで確認できます。

## 明示的なキャッシュ保存

Gemini API の明示的なキャッシュ保存機能を使用すると、一部のコンテンツをモデルに 1
回渡して入力トークンをキャッシュに保存し、後続のリクエストでキャッシュに保存されたトークンを参照できます。特定のボリュームでは、キャッシュに保存されたトークンを使用する方が、同じトークンセットを繰り返し渡すよりも低コストになります。

トークンセットをキャッシュに保存するときに、トークンが自動的に削除されるまでのキャッシュの存続期間を選択できます。このキャッシュ保存期間は有効期間（TTL）と呼ばれます。
設定しない場合、TTL はデフォルトで 1 時間になります。キャッシュ保存の費用は、入力トークンのサイズとトークンの保持期間によって異なります。

このセクションでは、スタートガイド
に記載されているように、Gemini SDK（または curl）をインストールし、API キーを構成していることを前提としています。

### キャッシュを使用してコンテンツを生成する

### Python

次の例は、キャッシュに保存されたシステム指示と動画ファイルを使用してコンテンツを生成する方法を示しています。

### 動画

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3.5-flash'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3.5-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

次の例は、キャッシュに保存されたシステム指示とテキスト ファイルを使用してコンテンツを生成する方法を示しています。

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3.5-flash";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Go

次の例は、キャッシュを使用してコンテンツを生成する方法を示しています。

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3.5-flash"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

次の例は、キャッシュを作成し、それを使用してコンテンツを生成する方法を示しています。

### 動画

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.5-flash",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.5-flash"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

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

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### キャッシュのリストを表示する

キャッシュに保存されたコンテンツを取得または表示することはできませんが、
キャッシュ メタデータ（`name`、`model`、`display_name`、`usage_metadata`、
`create_time`、`update_time`、`expire_time`）を取得できます。

### Python

アップロードされたすべてのキャッシュのメタデータを一覧表示するには、`CachedContent.list()` を使用します。

```
for cache in client.caches.list():
  print(cache)
```

1 つのキャッシュ オブジェクトのメタデータを取得するには、名前がわかっている場合は `get` を使用します。

```
client.caches.get(name=name)
```

### JavaScript

アップロードされたすべてのキャッシュのメタデータを一覧表示するには、`GoogleGenAI.caches.list()` を使用します。

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Go

次の例では、すべてのキャッシュを一覧表示します。

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

次の例では、ページサイズ 2 でキャッシュを一覧表示します。

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### キャッシュを更新する

キャッシュの新しい `ttl` または `expire_time` を設定できます。キャッシュのその他の変更はサポートされていません。

### Python

次の例は、`client.caches.update()` を使用してキャッシュの `ttl` を更新する方法を示しています。

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

有効期限を設定するには、`datetime` オブジェクト
または ISO 形式の日付と時刻の文字列（`dt.isoformat()`、
`2025-01-27T16:02:36.473528+00:00` など）を指定します。時刻にはタイムゾーンを含める必要があります
（`datetime.utcnow()` にはタイムゾーンが追加されませんが、
`datetime.now(datetime.timezone.utc)` にはタイムゾーンが追加されます）。

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

次の例は、`GoogleGenAI.caches.update()` を使用してキャッシュの `ttl` を更新する方法を示しています。

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

次の例は、キャッシュの `TTL` を更新する方法を示しています。

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

次の例は、キャッシュの `ttl` を更新する方法を示しています。

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### キャッシュを削除する

キャッシュ保存サービスには、キャッシュからコンテンツを手動で削除するための削除オペレーションが用意されています。次の例は、キャッシュを削除する方法を示しています。

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Go

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### OpenAI ライブラリを使用した明示的なキャッシュ保存

[OpenAI ライブラリ](https://ai.google.dev/gemini-api/docs/openai?hl=ja)を使用している場合は、
`cached_content` プロパティを使用して
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=ja#extra-body)を有効にできます。

## 明示的なキャッシュ保存を使用する状況

コンテキスト キャッシュ保存は、初期コンテキストの実体部分が、短いリクエストで繰り返し参照されるシナリオに特に適しています。次のようなユースケースでは、コンテキスト キャッシュ保存の使用を検討してください。

- 広範な[システム指示](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ja)を伴う chatbot
- 長時間の動画ファイルの繰り返し分析
- 大規模なドキュメント セットに対する繰り返しのクエリ
- 頻繁なコード リポジトリの分析やバグ修正

### 明示的なキャッシュ保存によるコスト削減の方法

コンテキスト キャッシュ保存は、コスト削減を目的とした有料の機能です。課金は次の要素に基づいて行われます。

1. **キャッシュ トークン数:** キャッシュに保存された入力トークンの数。後続のプロンプトに含まれる場合は、割引料金で請求されます。
2. **保存期間:** キャッシュに保存されたトークンの保存時間（TTL）。キャッシュに保存されたトークン数の TTL 期間に基づいて課金されます。TTL に最小値や最大値はありません。
3. **その他の項目:** 入力トークンや出力トークンがキャッシュされていない場合などは、別の料金が適用されます。

最新の料金の詳細については、Gemini API [料金
ページ](https://ai.google.dev/pricing?hl=ja)をご覧ください。トークンをカウントする方法については、[トークン
ガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)をご覧ください。

### その他の考慮事項

コンテキスト キャッシュ保存を使用する場合は、次の点に注意してください。

- コンテキスト キャッシュ保存の最小入力トークン数は、モデルによって異なります。 最大値は、指定されたモデルの最大値と同じです。 （トークンのカウントについて詳しくは、[トークンガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)をご覧ください
  ）。
- モデルは、キャッシュに保存されたトークンと通常の入力トークンを区別しません。キャッシュに保存されたコンテンツは、プロンプトの接頭辞です。
- コンテキスト キャッシュ保存には特別な料金や使用制限はありません。`GenerateContent` の標準のレート制限が適用され、トークン制限にはキャッシュに保存されたトークンが含まれます。
- キャッシュに保存されたトークンの数は、キャッシュ サービスの作成、取得、一覧表示オペレーションの `usage_metadata` と、キャッシュを使用する際の `GenerateContent` で返されます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-24 UTC。"],[],[]]
