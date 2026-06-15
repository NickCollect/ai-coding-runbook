---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=ja
fetched_at: 2026-06-15T06:27:01.662578+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# ファイル検索

Gemini API では、ファイル検索ツールを使用して検索拡張生成（RAG）が可能です。ファイル検索は、提供されたプロンプトに基づいて関連情報を迅速に取得できるように、データをインポート、チャンク化、インデックス化します。取得した情報はモデルのコンテキストとして使用され、より正確で関連性の高い回答を提供できるようになります。ファイル検索では、`gemini-embedding-001` でサポートされているテキスト エンベディングと、`gemini-embedding-2` でサポートされている画像/マルチモーダル エンベディングを使用して、マルチモーダル機能を提供することもできます。

クエリ時のファイルの保存とエンベディングの生成は無料です。エンベディングの作成に対して料金が発生するのは、ファイルを初めてインデックス登録するときと、通常の Gemini モデルの入力 / 出力トークンの費用のみです。この新しい課金パラダイムにより、ファイル検索ツールの構築とスケーリングが簡単かつ費用対効果の高いものになります。詳細については、
[料金](#pricing)セクションをご覧ください。

## ファイル検索ストアに直接アップロードする

この例では、ファイルを[ファイル検索ストア](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-media.uploadtofilesearchstore)に直接アップロードする方法を示します。

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

詳細については、[`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-media.uploadtofilesearchstore) の API リファレンスをご覧ください。

## ファイルのインポート

または、既存のファイルをアップロードして、[ファイル検索ストアにインポート](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-filesearchstores.importfile)することもできます。

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { name: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

詳細については、[`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-filesearchstores.importfile) の API リファレンスをご覧ください。

## チャンク化の構成

ファイルをファイル検索ストアにインポートすると、自動的にチャンクに分割され、埋め込み、インデックス化されて、ファイル検索ストアにアップロードされます。チャンク化戦略をより細かく制御する必要がある場合は、
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#request-body_5) 設定
を指定して、チャンクあたりのトークンの最大数と重複する
トークンの最大数を設定できます。

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

[[ファイル検索ストアを使用するには、アップロードとインポートの例に示すように、ツールとして `generateContent`
メソッドに渡します。](#upload)](#importing-files)

## 仕組み

ファイル検索では、セマンティック検索という手法を使用して、ユーザー プロンプトに関連する情報を検索します。標準のキーワード ベースの検索とは異なり、セマンティック検索はクエリの意味とコンテキストを理解します。

ファイルをインポートすると、アップロードされたコンテンツのセマンティックな意味を捉える
[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)と呼ばれる数値表現に変換されます。これらのエンベディングは、専用のファイル検索データベースに保存されます。
クエリを行うと、エンベディングに変換されます。次に、システムはファイル検索を実行して、ファイル検索ストアから最も類似した関連性の高いドキュメント チャンクを見つけます。

エンベディングには有効期間（TTL）はありません。手動で削除されるか、モデルが非推奨になるまで保持されます。ただし、ファイルは 48 時間後に削除されます。

ファイル検索 `uploadToFileSearchStore` API を使用するプロセスの内訳は次のとおりです。

1. **ファイル検索ストアを作成する**: ファイル検索ストアには、ファイルから処理された
   データが含まれます。これは、セマンティック検索が実行されるエンベディングの永続的なコンテナです。
2. **ファイルをアップロードしてファイル検索ストアにインポートする**: ファイルをアップロードし、結果をファイル検索ストアに同時にインポートします。これにより、元のドキュメントへの参照である一時的な `File` オブジェクトが作成されます。そのデータはチャンク化され、ファイル検索エンベディングに変換されてインデックス化されます。`File` オブジェクトは 48 時間後に削除されますが、ファイル検索ストアにインポートされたデータは、削除するまで無期限に保存されます。
3. **ファイル検索でクエリを実行する**: 最後に、`FileSearch` ツールを
   `generateContent` 呼び出しで使用します。ツール構成で、検索する `FileSearchStore` を指す `FileSearchRetrievalResource` を指定します。これにより、モデルは特定のファイル検索ストアでセマンティック検索を実行して、レスポンスのグラウンディングに関連する情報を検索します。

![ファイル検索のインデックス登録とクエリのプロセス](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ja)

ファイル検索のインデックス登録とクエリのプロセス

この図では、[*ドキュメント*]から [*エンベディング モデル*]
（[`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)を使用）への点線は、`uploadToFileSearchStore` API（[*ファイル ストレージ*]をバイパス）を表しています。
*それ以外の場合は、[[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja)] を使用してファイルを個別に作成
してからインポートすると、インデックス登録プロセスが [*ドキュメント*] から
[*ファイル ストレージ*]、[エンベディング モデル]* に移動します。

## ファイル検索ストア

ファイル検索ストアは、ドキュメント エンベディングのコンテナです。File API を使用してアップロードされた元のファイルは 48 時間後に削除されますが、ファイル検索ストアにインポートされたデータは、手動で削除するまで無期限に保存されます。複数のファイル検索ストアを作成して、ドキュメントを整理できます。`FileSearchStore` API を使用すると、ファイル検索ストアの作成、一覧表示、取得、削除を行って管理できます。ファイル検索ストア名はグローバル スコープです。

ファイル検索ストアを管理する方法の例を次に示します。

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'my-file_search-store-123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'my-file_search-store-123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: 'fileSearchStores/my-file_search-store-123'
});

await ai.fileSearchStores.delete({
  name: 'fileSearchStores/my-file_search-store-123',
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## ファイル検索ドキュメント

[ファイル検索ドキュメント](https://ai.google.dev/api/file-search/documents?hl=ja) API を使用すると、ファイルストア内の個々のドキュメントを管理できます。ファイル検索ストア内の各ドキュメントを `list` し、ドキュメントに関する情報を `get` し、名前でドキュメントを `delete` できます。

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc',
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"
```

## ファイルのメタデータ

ファイルにカスタム メタデータを追加して、フィルタリングや追加のコンテキストの提供に役立てることができます。メタデータは Key-Value ペアのセットです。

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    custom_metadata=[
        {"key": "author", "string_value": "Robert Graves"},
        {"key": "year", "numeric_value": 1934}
    ]
)
```

### JavaScript

```
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

これは、ファイル検索ストアに複数のドキュメントがあり、そのサブセットのみを検索する場合に便利です。

### Python

```
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Tell me about the book 'I, Claudius'",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name],
                    metadata_filter="author=Robert Graves",
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Tell me about the book 'I, Claudius'",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name],
          metadataFilter: 'author="Robert Graves"',
        }
      }
    ]
  }
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=${GEMINI_API_KEY}" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "contents": [{
                "parts":[{"text": "Tell me about the book I, Claudius"}]
            }],
            "tools": [{
                "file_search": {
                    "file_search_store_names":["'$STORE_NAME'"],
                    "metadata_filter": "author = \"Robert Graves\""
                }
            }]
        }' 2> /dev/null > response.json

cat response.json
```

`metadata_filter` のリストフィルタ構文の実装に関するガイダンスについては、[google.aip.dev/160](https://google.aip.dev/160) をご覧ください。

## マルチモーダル ファイル検索

マルチモーダル ファイル検索を使用すると、画像をネイティブに埋め込んで検索できるため、リッチなマルチモーダル RAG アプリケーションが可能になります。

### エンベディング モデルを構成する

`FileSearchStore` を作成する場合は、デフォルトのテキストのみのエンベディング モデルをオーバーライドして、マルチモーダル モデルを使用する必要があります。`models/gemini-embedding-2` を使用して、テキストと画像の両方を処理します。

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### 画像のアップロード

マルチモーダル エンベディング モデルを使用してストアを作成したら、
ファイル検索ストアに直接アップロードする[または](#upload)[ファイルのインポート](#importing-files)で説明されているのと同じアップロード API を使用して、画像ファイルを直接アップロードできます。

**画像ファイルの要件:**

- 画像ファイルの解像度は 4K x 4K ピクセル以下にする必要があります。
- サポートされている形式は PNG、JPEG です。

## 引用

ファイル検索を使用すると、モデルのレスポンスに、アップロードしたドキュメントのどの部分が回答の生成に使用されたかを指定する引用が含まれることがあります。これは、ファクト チェックと検証に役立ちます。

引用情報には、レスポンスの `grounding_metadata` 属性からアクセスできます。

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

グラウンディング メタデータの構造の詳細については、
[ファイル検索
クックブックの例](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb)
または [Google
検索によるグラウンディング ドキュメントのグラウンディング セクション](https://ai.google.dev/gemini-api/docs/google-search?hl=ja#attributing_sources_with_inline_citations)
をご覧ください。

### ページ番号

ページがあるドキュメント（PDF など）でファイル検索を使用すると、モデルのレスポンスに情報が見つかったページ番号が含まれることがあります。
この情報には、`retrieved_context` の `page_number` 属性からアクセスできます。

### Python

```
# Iterate through citations and check for page numbers
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.page_number:
       print(f"Cited Page: {chunk.retrieved_context.page_number}")
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.pageNumber) {
    console.log(`Cited Page: ${chunk.retrievedContext.pageNumber}`);
  }
}
```

### メディアの引用

生成中にモデルが画像チャンクを参照すると、API は `media_id` を含むグラウンディング メタデータで引用を返します。この ID を使用すると、モデルが参照した正確な画像チャンクをダウンロードできます。この `media_id` は複数の検索呼び出しで永続的に保持されるため、同じ画像を確実に取得したり、ID を使用してキャッシュに保存したりできます。

次のスニペットは、REST レスポンスの例です。

```
"groundingMetadata": {
  "groundingChunks": [
    {
      "retrievedContext": {
        "title": "product_image",
        "fileSearchStore": "fileSearchStores/my-store-123",
        "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
      }
    }
  ]
}
```

次のコード スニペットは、`media_id` を取得してメディアをダウンロードする方法を示しています。

### Python

```
# Iterate through citations and download media if present
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.media_id:
       print(f"Cited Media ID: {chunk.retrieved_context.media_id}")
       # Download the blob using the SDK
       blob_content = client.file_search_stores.download_media(
           media_id=chunk.retrieved_context.media_id
       )
       # Save blob_content to file...
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.mediaId) {
    console.log(`Cited Media ID: ${chunk.retrievedContext.mediaId}`);
    const blobContent = await ai.fileSearchStores.downloadMedia(chunk.retrievedContext.mediaId);
    // Save blobContent to file...
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## グラウンディング データ内のカスタム メタデータ

ファイルにカスタム メタデータを追加した場合は、モデルのレスポンスのグラウンディング メタデータでアクセスできます。これは、ソース ドキュメントからアプリケーション ロジックに追加のコンテキスト（URL、ページ番号、作成者など）を渡す場合に便利です。`retrieved_context` の各 `grounding_chunk` には、このカスタム メタデータが含まれています。

### Python

```
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Tell me about [insert question]",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
    if chunk.retrieved_context:
        print(f"Text: {chunk.retrieved_context.text}")
        if chunk.retrieved_context.custom_metadata:
            for metadata in chunk.retrieved_context.custom_metadata:
                print(f"Metadata Key: {metadata.key}")
                print(f"Value: {metadata.string_value or metadata.numeric_value}")
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Tell me about [insert question]",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name]
        }
      }
    ]
  }
});

const groundingMetadata = response.candidates[0].groundingMetadata;
groundingMetadata.groundingChunks.forEach((chunk) => {
  if (chunk.retrievedContext) {
    console.log(`Text: ${chunk.retrievedContext.text}`);
    if (chunk.retrievedContext.customMetadata) {
      chunk.retrievedContext.customMetadata.forEach((metadata) => {
        console.log(`Metadata Key: ${metadata.key}`);
        console.log(`Value: ${metadata.stringValue || metadata.numericValue}`);
      });
    }
  }
});
```

### REST

```
{
  "candidates": [
    {
      "content": { ... },
      "grounding_metadata": {
        "grounding_chunks": [
          {
            "retrieved_context": {
              "text": "...",
              "title": "...",
              "uri": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          }
        ],
        "grounding_supports": [ ... ]
      }
    }
  ]
}
```

## 構造化出力

Gemini 3 モデル以降では、ファイル検索ツールと
[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を組み合わせることができます。

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the minimum hourly wage in Tokyo right now?",
    config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ],
                response_format={"text": {"mime_type": "application/json", "schema": Money.model_json_schema()}}
      )
)
result = Money.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneySchema = z.object({
  amount: z.string().describe("The numerical part of the amount."),
  currency: z.string().describe("The currency of amount."),
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What is the minimum hourly wage in Tokyo right now?",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [file_search_store.name],
          },
        },
      ],
      responseFormat: { text: { mimeType: "application/json", schema: z.toJSONSchema(moneySchema) } },
    },
  });

  const result = moneySchema.parse(JSON.parse(response.text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "What is the minimum hourly wage in Tokyo right now?"}]
    }],
    "tools": [
      {
        "fileSearch": {
          "fileSearchStoreNames": ["$FILE_SEARCH_STORE_NAME"]
        }
      }
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "string", "description": "The numerical part of the amount."},
                "currency": {"type": "string", "description": "The currency of amount."}
  }
}
},
            "required": ["amount", "currency"]
        }
    }
  }'
```

## サポートされているモデル

次のモデルはファイル検索をサポートしています。

| モデル | ファイル検索 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## サポートされているツールの組み合わせ

Gemini 3 モデルでは、組み込みツール（ファイル検索など）とカスタムツール（関数呼び出し）を組み合わせることができます。詳細については、
[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

## サポートされているファイル形式

ファイル検索では、次のセクションに示すように、幅広いファイル形式がサポートされています。

### アプリケーション ファイル形式

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### テキスト ファイル形式

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## 制限事項

- **Live API:** ファイル検索は
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja)ではサポートされていません。
- **ツールの非互換性:** 現時点では、ファイル検索を他のツール
  （[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)、
  [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)など）と組み合わせることはできません。

### レート上限

サービスを安定させるため、ファイル検索 API には次の制限があります。

- **最大ファイルサイズ / ドキュメントあたりの上限**: 100 MB
- **プロジェクトのファイル検索ストアの合計サイズ** （ユーザー階層に基づく）:
  - **無料**: 1 GB
  - **階層 1**: 10 GB
  - **階層 2**: 100 GB
  - **階層 3**: 1 TB
- **推奨事項**: 取得レイテンシを最適化するため、各ファイル検索ストアのサイズを 20 GB 未満に制限します。

## 料金

- エンベディングの料金は、既存の
  [エンベディングの料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#gemini-embedding-2)に基づいて、インデックス登録時に請求されます。
- ストレージは無料です。
- クエリ時のエンベディングは無料です。
- 取得したドキュメント トークンは、通常の
  [コンテキスト トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)として課金されます。

## 次のステップ

- [ファイル検索ストア](https://ai.google.dev/api/file-search/file-search-stores?hl=ja)とファイル検索[ドキュメント](https://ai.google.dev/api/file-search/documents?hl=ja)の API リファレンスをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-05 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-05 UTC。"],[],[]]
