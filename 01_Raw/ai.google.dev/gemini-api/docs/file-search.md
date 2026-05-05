---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=ko
fetched_at: 2026-05-05T20:01:57.994598+00:00
title: "\ud30c\uc77c \uac80\uc0c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 파일 검색

Gemini API를 사용하면 파일 검색 도구를 통해 검색 증강 생성 ('RAG')을 사용할 수 있습니다. 파일 검색은 제공된 프롬프트를 기반으로 관련 정보를 빠르게 검색할 수 있도록 데이터를 가져오고, 청크로 나누고, 색인을 생성합니다. 이렇게 검색된 정보는 모델의 컨텍스트로 사용되어 더 정확하고 관련성 있는 답변을 제공할 수 있습니다. 파일 검색은 `gemini-embedding-001`에서 지원하는 텍스트 임베딩과 `gemini-embedding-2`에서 지원하는 이미지/멀티모달 임베딩을 통해 멀티모달 기능을 제공할 수도 있습니다.

쿼리 시 파일 저장 및 임베딩 생성은 무료이며, 파일을 처음 색인화할 때 임베딩 생성 비용과 일반 Gemini 모델 입력 / 출력 토큰 비용만 지불하면 됩니다. 이 새로운 청구 패러다임 덕분에 파일 검색 도구를 더 쉽고 비용 효율적으로 빌드하고 확장할 수 있습니다. 자세한 내용은 [가격 책정](#pricing) 섹션을 참고하세요.

## 파일 검색 스토어에 직접 업로드

다음은 [파일 검색 스토어](https://ai.google.dev/api/file-search/file-search-stores?hl=ko#method:-media.uploadtofilesearchstore)에 파일을 직접 업로드하는 방법을 보여주는 예시입니다.

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

### 자바스크립트

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

자세한 내용은 [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ko#method:-media.uploadtofilesearchstore) API 참조를 확인하세요.

## 파일 가져오기

또는 기존 파일을 업로드하고 [파일 검색 저장소로 가져올](https://ai.google.dev/api/file-search/file-search-stores?hl=ko#method:-filesearchstores.importfile) 수 있습니다.

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

### 자바스크립트

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

자세한 내용은 [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ko#method:-filesearchstores.importfile) API 참조를 확인하세요.

## 청크 구성

파일을 파일 검색 스토어로 가져오면 파일이 자동으로 청크로 분할되고, 삽입되고, 색인이 생성되고, 파일 검색 스토어로 업로드됩니다. 청크 전략을 더 세부적으로 관리해야 하는 경우 [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ko#request-body_5) 설정을 지정하여 청크당 최대 토큰 수와 중복되는 최대 토큰 수를 설정할 수 있습니다.

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

### 자바스크립트

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

파일 검색 저장소를 사용하려면 [업로드](#upload) 및 [가져오기](#importing-files) 예시에 표시된 대로 `generateContent` 메서드에 도구로 전달합니다.

## 작동 방식

파일 검색은 시맨틱 검색이라는 기법을 사용하여 사용자 프롬프트와 관련된 정보를 찾습니다. 표준 키워드 기반 검색과 달리 시맨틱 검색은 질문의 의미와 컨텍스트를 이해합니다.

파일을 가져오면 업로드된 콘텐츠의 시맨틱 의미를 포착하는 [임베딩](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko)이라는 숫자 표현으로 변환됩니다. 이러한 임베딩은 특수 파일 검색 데이터베이스에 저장됩니다.
쿼리를 입력하면 쿼리도 임베딩으로 변환됩니다. 그런 다음 시스템은 파일 검색을 실행하여 파일 검색 저장소에서 가장 유사하고 관련성 높은 문서 청크를 찾습니다.

삽입에는 TTL (수명)이 없습니다. 수동으로 삭제하거나 모델이 지원 중단될 때까지 유지됩니다. 파일은 48시간 후에 삭제됩니다.

파일 검색 `uploadToFileSearchStore` API를 사용하는 과정은 다음과 같습니다.

1. **파일 검색 스토어 만들기**: 파일 검색 스토어에는 파일에서 처리된 데이터가 포함됩니다. 시맨틱 검색이 작동하는 임베딩의 영구 컨테이너입니다.
2. **파일을 업로드하고 파일 검색 스토어로 가져오기**: 파일을 동시에 업로드하고 결과를 파일 검색 스토어로 가져옵니다. 이렇게 하면 원시 문서를 참조하는 임시 `File` 객체가 생성됩니다. 그런 다음 데이터가 청크로 분할되고, 파일 검색 임베딩으로 변환되고, 색인이 생성됩니다. `File`
   객체는 48시간 후에 삭제되지만 파일 검색 스토어로 가져온 데이터는 삭제할 때까지 무기한 저장됩니다.
3. **파일 검색으로 쿼리**: 마지막으로 `generateContent` 호출에서 `FileSearch` 도구를 사용합니다. 도구 구성에서 검색할 `FileSearchStore`를 가리키는 `FileSearchRetrievalResource`를 지정합니다. 이렇게 하면 모델이 해당 특정 파일 검색 스토어에서 시맨틱 검색을 실행하여 대답의 근거가 될 관련 정보를 찾습니다.

![파일 검색의 색인 생성 및 쿼리 프로세스](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ko)

파일 검색의 색인 생성 및 쿼리 프로세스

이 다이어그램에서 *문서*에서 *임베딩 모델*([`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko) 사용)로 연결되는 점선은 `uploadToFileSearchStore` API (*파일 저장소* 우회)를 나타냅니다.
그렇지 않으면 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 사용하여 파일을 별도로 만든 후 가져오면 색인 생성 프로세스가 *Documents*에서 *File storage*로 이동한 후 *Embedding model*로 이동합니다.

## 파일 검색 스토어

파일 검색 저장소는 문서 임베딩의 컨테이너입니다. 파일 API를 통해 업로드된 원시 파일은 48시간 후에 삭제되지만 파일 검색 스토어로 가져온 데이터는 수동으로 삭제할 때까지 무기한 저장됩니다. 문서를 정리하기 위해 여러 파일 검색 저장소를 만들 수 있습니다. `FileSearchStore` API를 사용하면 파일 검색 저장소를 생성, 나열, 가져오기, 삭제하여 관리할 수 있습니다. 파일 검색 스토어 이름은 전역 범위입니다.

파일 검색 저장소를 관리하는 방법의 몇 가지 예는 다음과 같습니다.

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

### 자바스크립트

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

## 파일 검색 문서

[파일 검색 문서](https://ai.google.dev/api/file-search/documents?hl=ko) API를 사용하여 파일 스토어의 개별 문서를 관리하여 파일 검색 스토어의 각 문서를 `list`하고, 문서에 관한 정보를 `get`하고, 이름으로 문서를 `delete`할 수 있습니다.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
```

### 자바스크립트

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

## 파일 메타데이터

파일을 필터링하거나 추가 컨텍스트를 제공하기 위해 파일에 맞춤 메타데이터를 추가할 수 있습니다. 메타데이터는 키-값 쌍의 집합입니다.

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

### 자바스크립트

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

이는 파일 검색 저장소에 여러 문서가 있고 그중 일부만 검색하려는 경우에 유용합니다.

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

### 자바스크립트

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

`metadata_filter`의 목록 필터 문법 구현에 관한 안내는 [google.aip.dev/160](https://google.aip.dev/160)에서 확인할 수 있습니다.

## 멀티모달 파일 검색

멀티모달 파일 검색을 사용하면 이미지를 기본적으로 삽입하고 검색하여 풍부한 멀티모달 RAG 애플리케이션을 사용할 수 있습니다.

### 임베딩 모델 구성

`FileSearchStore`을 만들 때 멀티모달 모델을 사용하려면 기본 텍스트 전용 임베딩 모델을 재정의해야 합니다. `models/gemini-embedding-2`를 사용하여 텍스트와 이미지를 모두 처리합니다.

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### 자바스크립트

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

### 이미지 업로드

멀티모달 임베딩 모델로 스토어를 만든 후 [파일 검색 스토어에 직접 업로드](#upload) 또는 [파일 가져오기](#importing-files)에 설명된 것과 동일한 업로드 API를 사용하여 이미지 파일을 직접 업로드할 수 있습니다.

**이미지 파일 요구사항:**

- 이미지 파일의 해상도는 4K x 4K 픽셀 이하여야 합니다.
- 요청당 최대 6개의 이미지
- 지원되는 형식은 PNG, JPEG입니다.

## 인용

파일 검색을 사용하면 모델의 대답에 업로드된 문서 중 대답을 생성하는 데 사용된 부분을 지정하는 인용이 포함될 수 있습니다. 이는 사실 확인 및 검증에 도움이 됩니다.

응답의 `grounding_metadata` 속성을 통해 인용 정보에 액세스할 수 있습니다.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### 자바스크립트

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

그라운딩 메타데이터의 구조에 관한 자세한 내용은 [파일 검색 쿡북](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) 또는 [Google 검색으로 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko#attributing_sources_with_inline_citations) 문서의 그라운딩 섹션에 있는 예를 참고하세요.

### 페이지 번호

페이지가 있는 문서 (예: PDF)로 파일 검색을 사용하면 정보가 발견된 페이지 번호가 모델의 대답에 포함될 수 있습니다.
이 정보는 `retrieved_context`의 `page_number` 속성을 통해 액세스할 수 있습니다.

### Python

```
# Iterate through citations and check for page numbers
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.page_number:
       print(f"Cited Page: {chunk.retrieved_context.page_number}")
```

### 자바스크립트

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.pageNumber) {
    console.log(`Cited Page: ${chunk.retrievedContext.pageNumber}`);
  }
}
```

### 미디어 인용

모델이 생성 중에 이미지 청크를 참조하면 API는 `media_id`가 포함된 그라운딩 메타데이터에 인용을 반환합니다. 이 ID를 사용하여 모델이 참조한 정확한 이미지 청크를 다운로드할 수 있습니다.

다음 스니펫은 REST 응답의 예입니다.

```
"groundingMetadata": {
  "groundingChunks": [
    {
      "retrievedContext": {
        "title": "product_image",
        "fileSearchStore": "fileSearchStores/my-store-123",
        "media_id": "fileSearchStores/my-store-123/blobs/BlobId-456"
      }
    }
  ]
}
```

다음 코드 스니펫은 `media_id`를 가져오고 미디어를 다운로드하는 방법을 보여줍니다.

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

### 자바스크립트

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
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/blobs/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 그라운딩 데이터의 맞춤 메타데이터

파일에 맞춤 메타데이터를 추가한 경우 모델 응답의 그라운딩 메타데이터에서 액세스할 수 있습니다. 이는 소스 문서에서 애플리케이션 로직으로 URL, 페이지 번호, 작성자와 같은 추가 컨텍스트를 전달하는 데 유용합니다. `retrieved_context`의 각 `grounding_chunk`에는 이 맞춤 메타데이터가 포함됩니다.

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

### 자바스크립트

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

## 구조화된 출력

Gemini 3 모델부터 파일 검색 도구를 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)과 결합할 수 있습니다.

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

### 자바스크립트

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

## 지원되는 모델

다음 모델은 파일 검색을 지원합니다.

| 모델 | 파일 검색 |
| --- | --- |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite 프리뷰](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 지원되는 도구 조합

Gemini 3 모델은 기본 제공 도구 (예: 파일 검색)와 맞춤 도구 (함수 호출)의 조합을 지원합니다. [도구 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko) 페이지에서 자세히 알아보세요.

## 지원되는 파일 형식

파일 검색은 다음 섹션에 나열된 다양한 파일 형식을 지원합니다.

### 애플리케이션 파일 형식

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

### 텍스트 파일 형식

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

## 제한사항

- **Live API:** [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)에서는 파일 검색이 지원되지 않습니다.
- **도구 비호환성:** 현재 파일 검색은 [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko) 등의 다른 도구와 결합할 수 없습니다.

### 비율 제한

File Search API에는 서비스 안정성을 위해 다음과 같은 한도가 적용됩니다.

- **최대 파일 크기 / 문서당 한도**: 100MB
- **프로젝트 파일 검색 저장소의 총 크기** (사용자 등급 기준):
  - **무료**: 1GB
  - **Tier 1**: 10 GB
  - **Tier 2**: 100 GB
  - **Tier 3**: 1 TB
- **권장사항**: 최적의 검색 지연 시간을 보장하려면 각 파일 검색 스토어의 크기를 20GB 미만으로 제한하세요.

## 가격 책정

- 기존 [임베딩 가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-embedding-2)에 따라 색인 생성 시 임베딩 비용이 청구됩니다.
- 저장 공간은 무료입니다.
- 쿼리 시간 임베딩은 무료입니다.
- 검색된 문서 토큰은 일반 [컨텍스트 토큰](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)으로 청구됩니다.

## 다음 단계

- [파일 검색 스토어](https://ai.google.dev/api/file-search/file-search-stores?hl=ko) 및 파일 검색 [문서](https://ai.google.dev/api/file-search/documents?hl=ko)의 API 참조를 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-05(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-05(UTC)"],[],[]]
