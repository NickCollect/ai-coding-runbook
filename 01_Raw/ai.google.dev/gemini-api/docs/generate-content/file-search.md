---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=zh-TW
fetched_at: 2026-08-17T02:31:31.862124+00:00
title: "\u6a94\u6848\u641c\u5c0b \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 檔案搜尋

Gemini API 可透過檔案搜尋工具啟用檢索增強生成 (RAG)。檔案搜尋會匯入、分塊及建立資料索引，以便根據提供的提示詞快速檢索相關資訊。接著，模型會將擷取的資訊做為背景資訊，提供更準確且相關的回覆。檔案搜尋功能也支援多模態功能，可使用 `gemini-embedding-001` 支援的文字嵌入，以及 `gemini-embedding-2` 支援的圖片/多模態嵌入。

檔案儲存和查詢時的嵌入生成作業免費，您只需在首次為檔案建立索引時支付嵌入費用，以及正常的 Gemini 模型輸入 / 輸出權杖費用。這個新計費模式可讓您更輕鬆且經濟實惠地建構及擴充檔案搜尋工具。詳情請參閱[定價](#pricing)部分。

## 直接上傳至檔案搜尋儲存庫

這個範例說明如何直接將檔案上傳至[檔案搜尋儲存庫](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw#method:-media.uploadtofilesearchstore)：

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

詳情請參閱 [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw#method:-media.uploadtofilesearchstore) 的 API 參考資料。

## 匯入檔案

或者，你也可以上傳現有檔案，然後[匯入檔案搜尋儲存庫](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw#method:-filesearchstores.importfile)：

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

詳情請參閱 [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw#method:-filesearchstores.importfile) 的 API 參考資料。

## 分塊設定

將檔案匯入檔案搜尋儲存庫時，系統會自動將檔案分成多個區塊、嵌入、建立索引，然後上傳至檔案搜尋儲存庫。如要進一步控管分塊策略，可以指定 [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw#request-body_5) 設定，為每個分塊設定詞元數量上限，以及重疊詞元數量上限。

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

如要使用檔案搜尋儲存庫，請將其做為工具傳遞至 `generateContent` 方法，如「[上傳](#upload)」和「[匯入](#importing-files)」範例所示。

## 運作方式

檔案搜尋功能會使用語意搜尋技術，找出與使用者提示相關的資訊。與標準關鍵字搜尋不同，語意搜尋可解讀查詢的意義和上下文。

匯入檔案時，系統會將檔案轉換為稱為「嵌入」的數值表示法，擷取上傳內容的語意。這些嵌入內容會儲存在專用的檔案搜尋資料庫中。
您進行查詢時，系統也會將查詢內容轉換為嵌入。接著，系統會執行檔案搜尋，從檔案搜尋儲存庫找出最相似且相關的文件區塊。

嵌入內容沒有存留時間 (TTL)，會一直存在，直到手動刪除或模型淘汰為止。但檔案會在 48 小時後刪除。

以下說明使用 File Search `uploadToFileSearchStore` API 的程序：

1. **建立檔案搜尋儲存庫**：檔案搜尋儲存庫包含檔案中經過處理的資料。這是語意搜尋運作時使用的嵌入項目永久容器。
2. **上傳檔案並匯入檔案搜尋儲存庫**：同時上傳檔案並將結果匯入檔案搜尋儲存庫。這會建立暫時的 `File` 物件，也就是原始文件的參照。然後將資料分塊、轉換為檔案搜尋嵌入，並編入索引。`File`
   物件會在 48 小時後刪除，而匯入檔案搜尋儲存區的資料則會無限期保留，直到您選擇刪除為止。
3. **使用檔案搜尋查詢**：最後，您會在 `generateContent` 呼叫中使用 `FileSearch` 工具。在工具設定中，您會指定 `FileSearchRetrievalResource`，指向要搜尋的 `FileSearchStore`。這會指示模型對該特定「檔案搜尋」儲存庫執行語意搜尋，找出相關資訊做為回覆內容的依據。

![檔案搜尋的索引和查詢程序](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=zh-tw)

檔案搜尋的索引和查詢程序

在這張圖表中，從「文件」到「嵌入模型」的虛線 (使用 [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)) 代表 `uploadToFileSearchStore` API (略過「檔案儲存空間」)。否則，使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 分別建立及匯入檔案，會將索引程序從「文件」移至「檔案儲存空間」，然後移至「嵌入模型」。

## 檔案搜尋商店

檔案搜尋儲存庫是文件嵌入內容的容器。透過 File API 上傳的原始檔案會在 48 小時後刪除，但匯入檔案搜尋儲存庫的資料會無限期儲存，直到您手動刪除為止。你可以建立多個檔案搜尋商店，整理文件。您可以使用 `FileSearchStore` API 建立、列出、取得及刪除檔案，藉此管理檔案搜尋商店。檔案搜尋商店名稱的範圍為全球。

以下舉例說明如何管理檔案搜尋商店：

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

## 檔案搜尋文件

您可以使用 [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=zh-tw) API 管理檔案儲存庫中的個別文件，以便`list`檔案搜尋儲存庫中的每份文件、`get`文件相關資訊，以及`delete`依名稱搜尋文件。

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

## 檔案中繼資料

你可以為檔案新增自訂中繼資料，以便篩選檔案或提供額外背景資訊。中繼資料是一組鍵/值組合。

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

如果檔案搜尋商店中有多份文件，而您只想搜尋其中一部分，這項功能就非常實用。

### Python

```
response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${GEMINI_API_KEY}" \
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

如需實作 `metadata_filter` 清單篩選器語法的指引，請參閱 [google.aip.dev/160](https://google.aip.dev/160)。

## 多模態檔案搜尋

多模態檔案搜尋功能可讓您以原生方式嵌入及搜尋圖片，進而打造豐富的多模態 RAG 應用程式。

### 設定嵌入模型

建立 `FileSearchStore` 時，您必須覆寫預設的純文字嵌入模型，才能使用多模態模型。使用 `models/gemini-embedding-2` 處理文字和圖片。

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

### 上傳圖片

使用多模態嵌入模型建立儲存庫後，您可以直接使用「[直接上傳至檔案搜尋儲存庫](#upload)」或「[匯入檔案](#importing-files)」一節所述的相同上傳 API，上傳圖片檔案。

**圖片檔案規定：**

- 圖片檔案的解析度不得超過 4K x 4K 像素。
- 支援的格式包括 PNG、JPEG。

## 參考資料

使用檔案搜尋功能時，模型的回覆可能會包含引文，指出生成答案時參考了上傳文件的哪些部分。有助於事實查核和驗證。

您可以透過回應的 `grounding_metadata` 屬性存取引文資訊。

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

如要進一步瞭解基礎中繼資料的結構，請參閱[檔案搜尋食譜](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb)中的範例，或 [Google 搜尋基礎文件中的基礎部分](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw#attributing_sources_with_inline_citations)。

### 頁碼

使用檔案搜尋功能時，如果搜尋的文件包含頁面 (例如 PDF)，模型的回覆可能會包含找到資訊的頁碼。您可以透過 `retrieved_context` 的 `page_number` 屬性存取這項資訊。

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

### 媒體引用

模型在生成內容時如果參照圖片區塊，API 會在基礎中繼資料中傳回引文，其中包含 `media_id`。您可以使用這個 ID 下載模型參照的確切圖片區塊。這個 `media_id` 會在多個搜尋呼叫中持續存在，因此您可以使用 ID 穩定擷取或快取同一張圖片。

以下程式碼片段是 REST 回應範例：

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

下列程式碼片段示範如何擷取 `media_id` 並下載媒體：

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

## 基礎資料中的自訂中繼資料

如果您已在檔案中新增自訂中繼資料，可以在模型回覆的基礎中繼資料中存取。這項功能可將來源文件中的其他內容 (例如網址、頁碼或作者) 傳遞至應用程式邏輯，`retrieved_context` 中的每個 `grounding_chunk` 都包含這項自訂中繼資料。

### Python

```
response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

## 結構化輸出內容

從 Gemini 3 模型開始，您可以將檔案搜尋工具與[結構化輸出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)結合使用。

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## 支援的模型

下列機型支援檔案搜尋：

| 模型 | 檔案搜尋 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 支援的工具組合

Gemini 3 模型支援結合內建工具 (例如檔案搜尋) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

## 支援的檔案類型

檔案搜尋支援多種檔案格式，詳列於下列各節。

### 應用程式檔案類型

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

### 文字檔案類型

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

## 限制

- **Live API：**[Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) 不支援檔案搜尋。
- **工具不相容：**目前無法將檔案搜尋與其他工具合併使用，例如[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、[網址背景資訊](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)等。

### 頻率限制

為確保服務穩定性，File Search API 有下列限制：

- **檔案大小上限 / 單一文件限制**：100 MB
- **專案檔案搜尋儲存空間總大小** (依使用者層級而定)：
  - **免費**：1 GB
  - **第 1 級**：10 GB
  - **第 2 級**：100 GB
  - **第 3 級**：1 TB
- **建議**：將每個檔案搜尋商店的大小限制在 20 GB 以下，確保最佳的擷取延遲時間。

## 定價

- 系統會在建立索引時，根據現有的[嵌入定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-embedding-2)向您收取嵌入費用。
- 儲存空間免費。
- 查詢時嵌入功能不會產生費用。
- 系統會將擷取的檔案權杖視為一般[內容權杖](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)計費。

## 後續步驟

- 請參閱 [檔案搜尋商店](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-tw)和檔案搜尋[文件](https://ai.google.dev/api/file-search/documents?hl=zh-tw)的 API 參考資料。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
