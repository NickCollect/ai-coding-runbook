---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-CN
fetched_at: 2026-05-25T05:29:44.445809+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 文件搜索

Gemini API 通过文件搜索工具启用检索增强生成 (RAG)。文件搜索会导入您的数据、将其分块并编制索引，以便根据提供的提示快速检索相关信息。然后，检索到的信息会用作模型的上下文，使其能够提供更准确、更相关的答案。文件搜索还能够提供多模态功能，支持 `gemini-embedding-001` 提供的文本嵌入，以及 `gemini-embedding-2` 提供的图片/多模态嵌入。

查询时的文件存储和嵌入生成是免费的，您只需在首次为文件编制索引时支付创建嵌入的费用，以及正常的 Gemini 模型输入 / 输出令牌费用。这种新的结算模式使得文件搜索工具的构建和扩缩变得更简单、更经济实惠。如需了解详情，请参阅
[价格](#pricing)部分。

## 直接上传到文件搜索存储区

此示例展示了如何将文件直接上传到
[文件搜索存储区](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn#method:-media.uploadtofilesearchstore)：

### Python

```
# This will only work for SDK newer than 2.0.0
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "file_citation":
                            print(f"  - {annotation.file_name}: {annotation.source}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
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

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'file_citation') {
                console.log(`  - ${annotation.file_name}: ${annotation.source}`);
              }
            }
          }
        }
      }
    }
  }
}

run();
```

如需了解详情，请参阅 [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn#method:-media.uploadtofilesearchstore) 的 API 参考文档。

## 导入文件

或者，您也可以上传现有文件并将其[导入到文件搜索存储区](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn#method:-filesearchstores.importfile)：

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'display_name': 'display_file_name'})

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { displayName: 'file-name' }
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

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
        }
      }
    }
  }
}

run();
```

如需了解详情，请参阅 [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn#method:-filesearchstores.importfile) 的 API 参考文档。

## 分块配置

将文件导入文件搜索存储区时，系统会自动将文件分解为多个块，然后进行嵌入、编制索引并上传到文件搜索存储区。如果您
需要更好地控制分块策略，可以指定
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn#request-body_5) 设置
，以设置每个块的令牌数量上限和重叠
令牌数量上限。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file='sample.txt',
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
// This will only work for SDK newer than 2.0.0
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

如需使用文件搜索存储区，请将其作为工具传递给 `interactions.create`
方法，如 [上传](#upload) 和 [导入](#importing-files) 示例所示。

## 运作方式

文件搜索使用一种称为语义搜索的技术来查找与用户提示相关的信息。与基于关键字的标准搜索不同，语义搜索可以理解查询的含义和上下文。

导入文件时，系统会将其转换为称为
[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)的数值表示形式，这些嵌入会捕获
上传内容的语义含义。这些嵌入存储在专用的文件搜索数据库中。
当您进行查询时，系统也会将其转换为嵌入。然后，系统会执行文件搜索，以从文件搜索存储区中找到最相似、最相关的文档块。

嵌入没有存留时间 (TTL)，它们会一直保留，直到手动删除或模型被废弃。不过，文件会在 48 小时后被删除。

下面详细介绍了使用文件搜索 `uploadToFileSearchStore` API 的流程：

1. **创建文件搜索存储区**：文件搜索存储区包含文件中经过处理的
   数据。它是语义搜索将对其进行操作的嵌入的持久容器。
2. **上传文件并导入到文件搜索存储区**：同时上传
   文件并将结果导入到文件搜索存储区。这会创建一个临时 `File` 对象，该对象是对原始文档的引用。然后，系统会对该数据进行分块、转换为文件搜索嵌入并编制索引。`File` 对象会在 48 小时后被删除，而导入到文件搜索存储区的数据将无限期存储，直到您选择将其删除为止。
3. **使用文件搜索进行查询**：最后，您可以在
   `FileSearch`工具`generateContent`调用中使用。在工具配置中，您可以指定 `FileSearchRetrievalResource`，该资源指向您要搜索的 `FileSearchStore`。这会告知模型对该特定文件搜索存储区执行语义搜索，以查找相关信息来支持其回答。

![文件搜索的索引编制和查询流程](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=zh-cn)

文件搜索的索引和查询流程

在此图中，从*文档*到*嵌入模型*
（使用[`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)）
的虚线表示`uploadToFileSearchStore` API（绕过*文件存储*）。否则，使用 [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-cn) 分别创建
文件，然后导入文件会将索引流程从 *文档* 移至
*文件存储*，然后再移至 *嵌入模型*。

## 文件搜索存储区

文件搜索存储区是文档嵌入的容器。虽然通过 File API 上传的原始文件会在 48 小时后被删除，但导入到文件搜索存储区的数据会无限期存储，直到您手动将其删除为止。您可以创建多个文件搜索存储区来整理文档。借助 `FileSearchStore` API，您可以创建、列出、获取和删除文件搜索存储区，以便对其进行管理。文件搜索存储区名称的作用域是全局的。

以下是一些管理文件搜索存储区的示例：

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

## 文件搜索文档

您可以使用
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=zh-cn) API 管理文件存储区中的各个文档，以便 `list` 文件搜索存储区中的每个文档、`get` 有关文档的信息，以及按名称 `delete` 文档。

### Python

```
# This will only work for SDK newer than 2.0.0
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc', config={'force': True})
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}&force=true"
```

## 文件元数据

您可以为文件添加自定义元数据，以帮助过滤文件或提供其他上下文。元数据是一组键值对。

### Python

```
# This will only work for SDK newer than 2.0.0
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'custom_metadata': [
            {"key": "author", "string_value": "Robert Graves"},
            {"key": "year", "numeric_value": 1934}
        ]
    }
)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
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

当文件搜索存储区中有多个文档，并且您只想搜索其中的一部分时，此功能非常有用。

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about the book 'I, Claudius'",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name],
        "metadata_filter": 'author="Robert Graves"',
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: "Tell me about the book 'I, Claudius'",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name],
    metadata_filter: 'author="Robert Graves"',
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
      }
    }
  }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d '{
            "model": "gemini-3-flash-preview",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

如需了解有关为 `metadata_filter` 实现列表过滤语法的指南，请访问
[google.aip.dev/160](https://google.aip.dev/160)

## 多模态文件搜索

借助多模态文件搜索，您可以原生嵌入图片并搜索图片，从而实现丰富的多模态 RAG 应用。

### 配置嵌入模型

创建 `FileSearchStore` 时，您必须替换默认的纯文本嵌入模型，以使用多模态模型。使用 `models/gemini-embedding-2` 处理文本和图片。

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

### 上传图片

使用多模态嵌入模型创建存储区后，您可以使用与
[直接上传到文件搜索存储区](#upload)或[导入文件](#importing-files)中所述相同的上传 API 直接上传
图片文件。

**图片文件要求**：

- 图片文件的分辨率不得超过 4K x 4K 像素。
- 支持的格式为 PNG、JPEG。

## 引用

使用文件搜索时，模型的回答可能包含引用，用于指定生成答案时使用了上传文档的哪些部分。这有助于进行事实核查和验证。

您可以通过响应的 `model_output` 步骤的 `content` 块内的 `annotations` 属性访问引用信息。

### Python

```
# This will only work for SDK newer than 2.0.0
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text' && contentBlock.annotations) {
        console.log(JSON.stringify(contentBlock.annotations, null, 2));
      }
    }
  }
}
```

如需详细了解引用的结构，请参阅
[Interactions 的 API 参考文档](https://ai.google.dev/api/interactions-api?hl=zh-cn#Resource:FileCitation)。

### 页码

将文件搜索与包含页面的文档（例如 PDF）搭配使用时，模型的回答可能包含找到信息的页码。
您可以通过 `file_citation` 注解的 `page_number` 属性访问此信息。

### Python

```
# Iterate through citations and check for page numbers
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.page_number:
                        print(f"Cited Page: {annotation.page_number}")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.pageNumber) {
            console.log(`Cited Page: ${annotation.pageNumber}`);
          }
        }
      }
    }
  }
}
```

### 媒体引用

当模型在生成过程中引用图片块时，API 会在包含 `media_id` 的注解中返回类型为 `file_citation` 的注解。您可以使用此 ID 下载模型引用的确切图片块。此 `media_id` 在多次搜索调用中保持不变，因此您可以可靠地检索同一图片或使用该 ID 缓存图片。

以下代码段是一个 REST 响应步骤示例：

```
{
  "type": "model_output",
  "content": [
    {
      "type": "text",
      "text": "...",
      "annotations": [
        {
          "type": "file_citation",
          "file_name": "product_image",
          "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
        }
      ]
    }
  ]
}
```

以下代码段展示了如何检索 `media_id` 并下载媒体：

### Python

```
# Iterate through citations and download media if present
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        # Download the blob using the SDK
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
                        # Save blob_content to file...
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.mediaId) {
            console.log(`Cited Media ID: ${annotation.mediaId}`);
            const blobContent = await ai.fileSearchStores.downloadMedia(annotation.mediaId);
            // Save blobContent to file...
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 自定义元数据

如果您已为文件添加自定义元数据，则可以在模型响应的注解中访问该元数据。这对于将其他上下文（例如网址、页码或作者）从源文档传递到应用逻辑非常有用。类型为 `file_citation` 的每个引用注解都包含此自定义元数据。

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                for annotation in content_block.annotations:
                    print(annotation)
```

### JavaScript

```
  // This will only work for SDK newer than 2.0.0
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.annotations) {
          contentBlock.annotations.forEach((annotation) => {
            console.log(annotation);
          });
        }
      }
    }
  }
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "file_name": "...",
              "source": "...",
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
          ]
        }
      ]
    }
  ]
}
```

## 结构化输出

从 Gemini 3 模型开始，您可以将文件搜索工具与
[结构化输出](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=zh-cn)结合使用。

### Python

```
# This will only work for SDK newer than 2.0.0
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the minimum hourly wage in Tokyo right now?",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Money.model_json_schema()
    },
)
result = Money.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { z } from "zod";

const moneyJsonSchema = {
  type: "object",
  properties: {
    amount: { type: "string", description: "The numerical part of the amount." },
    currency: { type: "string", description: "The currency of amount." }
  },
  required: ["amount", "currency"]
};

const moneySchema = z.fromJSONSchema(moneyJsonSchema);

async function run() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the minimum hourly wage in Tokyo right now?",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name],
    }],
    response_format: {
      type: 'text',
      mime_type: 'application/json',
      schema: moneyJsonSchema
    },
  });

  const result = moneySchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(result);
}

run();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the minimum hourly wage in Tokyo right now?",
    "tools": [{
      "type": "file_search",
      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]
    }],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "amount": {"type": "string", "description": "The numerical part of the amount."},
          "currency": {"type": "string", "description": "The currency of amount."}
        },
        "required": ["amount", "currency"]
      }
    }
  }'
```

## 支持的模型

以下模型支持文件搜索：

| 模型 | 文件搜索 |
| --- | --- |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 支持的工具组合

Gemini 3 模型支持将内置工具（例如文件搜索）与自定义工具（函数调用）结合使用。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

## 支持的文件类型

文件搜索支持多种文件格式，详见以下各部分。

### 应用文件类型

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

### 文本文件类型

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

- [**Live API**： Live API 不支持文件搜索。](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)
- **工具不兼容**： 目前，文件搜索无法与其他工具
  （例如[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-cn)、
  [网址上下文](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)等）结合使用。

### 速率限制

文件搜索 API 具有以下限制，以确保服务的稳定性：

- **文件大小上限 / 每个文档的限制**：100 MB
- **项目文件搜索存储区的总大小** （基于用户层级）：
  - **免费**：1 GB
  - **第 1 层级**：10 GB
  - **第 2 层级**：100 GB
  - **第 3 层级**：1 TB
- **建议**：将每个文件搜索存储区的大小限制在 20 GB 以下，以确保最佳检索延迟时间。

## 价格

- 系统会在编制索引时根据现有的
  [嵌入价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-embedding-2)向您收取嵌入费用。
- 存储空间免费。
- 查询时的嵌入免费。
- 检索到的文档令牌按常规
  [上下文令牌](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-cn)收费。

## 后续步骤

- 访问 [文件搜索存储区](https://ai.google.dev/api/file-search/file-search-stores?hl=zh-cn) 和文件搜索 [文档](https://ai.google.dev/api/file-search/documents?hl=zh-cn) 的 API 参考文档。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-12。"],[],[]]
