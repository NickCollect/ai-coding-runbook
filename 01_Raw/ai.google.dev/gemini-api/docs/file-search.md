---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=zh-CN
fetched_at: 2026-05-05T13:22:13.312617+00:00
title: "\u6587\u4ef6\u641c\u7d22 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

- [首页](https://ai.google.dev/gemini-api/docs/首页)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文档](https://ai.google.dev/gemini-api/docs/文档)

发送反馈

# 文件搜索

Gemini API 通过文件搜索工具实现检索增强生成（简称“RAG”）。文件搜索功能会导入、分块和索引您的数据，以便根据您提供的提示快速检索相关信息。然后，这些信息会用作模型的上下文，使模型能够提供更准确、更相关的答案。

为了让开发者能够以简单实惠的方式使用文件搜索功能，我们决定在查询时免费提供文件存储和嵌入生成服务。您只需在首次为文件编制索引时支付创建嵌入内容的费用（按适用的嵌入模型费用）以及正常的 Gemini 模型输入 / 输出 token 费用。这种新的结算模式使得文件搜索工具的构建和扩展更加简单且更具成本效益。

## 直接上传到文件搜索存储区

此示例展示了如何将文件直接上传到[文件搜索存储区](https://ai.google.dev/gemini-api/docs/文件搜索存储区)：

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(config={'display_name': 'your-fileSearchStore-name'})

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
    model="gemini-3-flash-preview",
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
    config: { displayName: 'your-fileSearchStore-name' }
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
    model: "gemini-3-flash-preview",
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

如需了解详情，请参阅 [`uploadToFileSearchStore`](https://ai.google.dev/gemini-api/docs/`uploadToFileSearchStore`) 的 API 参考文档。

## 导入文件

或者，您也可以上传现有文件，然后[将其导入文件搜索存储区](https://ai.google.dev/gemini-api/docs/将其导入文件搜索存储区)：

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

file_search_store = client.file_search_stores.create(config={'display_name': 'your-fileSearchStore-name'})

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    config: { displayName: 'your-fileSearchStore-name' }
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
    model: "gemini-3-flash-preview",
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

如需了解详情，请参阅 [`importFile`](https://ai.google.dev/gemini-api/docs/`importFile`) 的 API 参考文档。

## 分块配置

将文件导入到文件搜索存储区后，系统会自动将其分解为块、嵌入、编入索引，然后上传到您的文件搜索存储区。如果您需要更精细地控制分块策略，可以指定 [`chunking_config`](https://ai.google.dev/gemini-api/docs/`chunking_config`) 设置，以设置每个块的 token 数量上限和重叠 token 数量上限。

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

如需使用您的文件搜索商店，请将其作为工具传递给 `generateContent` 方法，如[上传](https://ai.google.dev/gemini-api/docs/上传)和[导入](https://ai.google.dev/gemini-api/docs/导入)示例所示。

## 运作方式

文件搜索功能使用一种称为语义搜索的技术来查找与用户提示相关的信息。与基于标准关键字的搜索不同，语义搜索能够理解查询的含义和上下文。

导入文件后，系统会将其转换为称为[嵌入](https://ai.google.dev/gemini-api/docs/嵌入)的数值表示形式，用于捕捉文本的语义。这些嵌入会存储在专门的文件搜索数据库中。
当您提出查询时，系统也会将其转换为嵌入。然后，系统会执行文件搜索，以从文件搜索存储区中找到最相似且最相关的文档块。

嵌入内容和文件没有存留时间 (TTL)；它们会一直保留，直到手动删除或模型被弃用为止。

下面详细介绍了使用文件搜索 `uploadToFileSearchStore` API 的流程：

1. **创建文件搜索存储区**：文件搜索存储区包含来自文件的处理后数据。它是语义搜索将使用的嵌入的持久容器。
2. **上传文件并导入到文件搜索存储区**：同时上传文件并将结果导入到文件搜索存储区。这会创建一个临时 `File` 对象，该对象是对原始文档的引用。然后，该数据会被分块、转换为文件搜索嵌入内容并编入索引。`File`对象会在 48 小时后被删除，而导入到文件搜索存储区的数据会无限期存储，直到您选择删除为止。
3. **使用文件搜索进行查询**：最后，您可以在 `generateContent` 调用中使用 `FileSearch` 工具。在工具配置中，您需要指定一个 `FileSearchRetrievalResource`，该 `FileSearchRetrievalResource` 指向您要搜索的 `FileSearchStore`。这会指示模型对该特定文件搜索存储区执行语义搜索，以查找相关信息来为回答提供依据。

![文件搜索的索引编制和查询流程](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=zh-cn)

文件搜索的索引和查询过程

在此图中，从*文档*到*嵌入模型*（使用 [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/`gemini-embedding-001`)）的虚线表示 `uploadToFileSearchStore` API（绕过*文件存储*）。否则，使用 [Files API](https://ai.google.dev/gemini-api/docs/Files API) 单独创建文件，然后导入文件，会将索引编制流程从*文档*移至*文件存储空间*，然后再移至*嵌入模型*。

## 文件搜索存储区

文件搜索存储区是文档嵌入的容器。虽然通过 File API 上传的原始文件会在 48 小时后被删除，但导入到文件搜索存储区的数据会无限期存储，直到您手动将其删除。您可以创建多个文件搜索存储区来整理文档。借助 `FileSearchStore` API，您可以创建、列出、获取和删除文件搜索存储区，从而管理这些存储区。文件搜索存储区名称具有全局范围。

以下是一些有关如何管理文件搜索商店的示例：

### Python

```
file_search_store = client.file_search_stores.create(config={'display_name': 'my-file_search-store-123'})

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: { displayName: 'my-file_search-store-123' }
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
    -H "Content-Type: application/json"
    -d '{ "displayName": "My Store" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## 文件搜索文档

您可以使用 [File Search Documents](https://ai.google.dev/gemini-api/docs/File Search Documents) API 管理文件存储区中的各个文档，以`list` 文件搜索存储区中的每个文档、`get` 文档的相关信息，以及按名称`delete` 文档。

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

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"
```

## 文件元数据

您可以为文件添加自定义元数据，以便过滤文件或提供更多背景信息。元数据是一组键值对。

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

如果您在文件搜索存储区中有多个文档，并且只想搜索其中的一部分，此参数会非常有用。

### Python

```
response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${GEMINI_API_KEY}" \
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

有关为 `metadata_filter` 实现列表过滤条件语法的指南，请参阅 [google.aip.dev/160](https://ai.google.dev/gemini-api/docs/google.aip.dev/160)

## 引用

使用文件搜索功能时，模型生成的回答可能包含引用，指明回答中使用了哪些上传的文档内容。这有助于进行事实核查和验证。

您可以通过响应的 `grounding_metadata` 属性访问引用信息。

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

如需详细了解接地元数据的结构，请参阅[文件搜索实用指南](https://ai.google.dev/gemini-api/docs/文件搜索实用指南)中的示例，或[“依托 Google 搜索进行接地”文档的接地部分](https://ai.google.dev/gemini-api/docs/“依托 Google 搜索进行接地”文档的接地部分)。

## 接地数据中的自定义元数据

如果您已向文件添加自定义元数据，则可以在模型回答的接地元数据中访问该元数据。这有助于将其他上下文（例如网址、页码或作者）从源文档传递到应用逻辑。`retrieved_context` 中的每个 `grounding_chunk` 都包含此自定义元数据。

### Python

```
response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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

## 结构化输出

从 Gemini 3 模型开始，您可以将文件搜索工具与[结构化输出](https://ai.google.dev/gemini-api/docs/结构化输出)相结合。

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the minimum hourly wage in Tokyo right now?",
    config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ],
                response_mime_type="application/json",
                response_schema=Money.model_json_schema()
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
    model: "gemini-3-flash-preview",
    contents: "What is the minimum hourly wage in Tokyo right now?",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [file_search_store.name],
          },
        },
      ],
      responseMimeType: "application/json",
      responseJsonSchema: z.toJSONSchema(moneySchema),
    },
  });

  const result = moneySchema.parse(JSON.parse(response.text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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
        "responseMimeType": "application/json",
        "responseJsonSchema": {
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
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Pro 预览版) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Flash-Lite 预览版) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3 Flash 预览版) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Pro) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash-Lite) | ✔️ |

## 支持的工具组合

Gemini 3 模型支持将内置工具（例如文件搜索）与自定义工具（函数调用）相结合。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/工具组合)页面。

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

- **Live API**：[Live API](https://ai.google.dev/gemini-api/docs/Live API) 不支持文件搜索。
- **工具不兼容**：目前，文件搜索无法与其他工具（例如[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/依托 Google 搜索进行接地)、[网址上下文](https://ai.google.dev/gemini-api/docs/网址上下文)等）结合使用。

### 速率限制

为了确保服务稳定性，文件搜索 API 具有以下限制：

- **文件大小上限 / 每个文档的限制**：100 MB
- **项目文件搜索存储空间总大小**（取决于用户层级）：
  - **免费**：1 GB
  - **第 1 级**：10 GB
  - **第 2 级**：100 GB
  - **3 级**：1 TB
- **建议**：将每个文件搜索存储区的大小限制在 20 GB 以下，以确保最佳检索延迟时间。

## 价格

- 开发者需根据现有的[嵌入模型价格](https://ai.google.dev/gemini-api/docs/嵌入模型价格)（每 100 万个令牌 0.15 美元）在编入索引时支付嵌入模型费用。
- 存储空间免费。
- 查询时嵌入是免费的。
- 检索到的文档令牌按常规[上下文令牌](https://ai.google.dev/gemini-api/docs/上下文令牌)收费。

## 后续步骤

- 访问 [File Search Stores](https://ai.google.dev/gemini-api/docs/File Search Stores) 和 File Search [Documents](https://ai.google.dev/gemini-api/docs/Documents) 的 API 参考文档。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://ai.google.dev/gemini-api/docs/知识共享署名 4.0 许可)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://ai.google.dev/gemini-api/docs/Apache 2.0 许可)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://ai.google.dev/gemini-api/docs/Google 开发者网站政策)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？
