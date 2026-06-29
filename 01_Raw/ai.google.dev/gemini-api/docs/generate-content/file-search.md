---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=tr
fetched_at: 2026-06-29T05:34:26.273426+00:00
title: "Dosya Arama \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Dosya Arama

Gemini API, FileSearch aracı aracılığıyla Veriyle Artırılmış Üretim ("RAG") özelliğini etkinleştirir. Dosya Arama, verilerinizi içe aktarır, parçalara ayırır ve dizine ekler. Böylece, sağlanan bir isteme göre ilgili bilgilerin hızlıca alınmasını sağlar. Daha sonra bu bilgiler model için bağlam olarak kullanılır. Böylece model, daha doğru ve alakalı yanıtlar verebilir. Dosya arama özelliği, `gemini-embedding-001` tarafından desteklenen metin yerleştirmeleri ve `gemini-embedding-2` tarafından desteklenen resim/çok formatlı yerleştirmelerle çok formatlı özellikler de sunabilir.

Sorgu sırasında dosya depolama ve yerleştirme oluşturma ücretsizdir. Yalnızca dosyalarınızı ilk kez indekslediğinizde yerleştirme oluşturma ve normal Gemini modeli giriş / çıkış jetonları için ödeme yaparsınız. Bu yeni faturalandırma paradigması, Dosya Arama Aracı'nın hem daha kolay hem de daha uygun maliyetli bir şekilde oluşturulup ölçeklendirilmesini sağlar. Ayrıntılar için [fiyatlandırma](#pricing) bölümüne bakın.

## Doğrudan Dosya Arama mağazasına yükleme

Bu örnekte, bir dosyanın doğrudan [dosya arama deposuna](https://ai.google.dev/api/file-search/file-search-stores?hl=tr#method:-media.uploadtofilesearchstore) nasıl yükleneceği gösterilmektedir:

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

Daha fazla bilgi için [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=tr#method:-media.uploadtofilesearchstore) API referansına bakın.

## Dosyaları içe aktarma

Alternatif olarak, mevcut bir dosyayı yükleyip [dosya arama mağazanıza aktarabilirsiniz](https://ai.google.dev/api/file-search/file-search-stores?hl=tr#method:-filesearchstores.importfile):

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

Daha fazla bilgi için [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=tr#method:-filesearchstores.importfile) API referansına bakın.

## Parçalara ayırma yapılandırması

Bir dosyayı Dosya Arama mağazasına aktardığınızda dosya otomatik olarak parçalara ayrılır, yerleştirilir, dizine eklenir ve Dosya Arama mağazanıza yüklenir. Parçalama stratejisi üzerinde daha fazla kontrol sahibi olmak istiyorsanız bir [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=tr#request-body_5) ayarı belirterek parça başına maksimum jeton sayısı ve maksimum sayıda çakışan jeton ayarlayabilirsiniz.

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

Dosya Arama mağazanızı kullanmak için `generateContent` yöntemine araç olarak iletin. Bu işlem, [Yükleme](#upload) ve [İçe Aktarma](#importing-files) örneklerinde gösterilmiştir.

## İşleyiş şekli

Dosya Arama, kullanıcı istemiyle alakalı bilgileri bulmak için semantik arama adı verilen bir teknik kullanır. Standart anahtar kelime tabanlı aramanın aksine, semantik arama sorgunuzun anlamını ve bağlamını anlar.

İçe aktardığınız dosyalar, yüklenen içeriğin semantik anlamını yakalayan [yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) adı verilen sayısal gösterimlere dönüştürülür. Bu yerleştirmeler, özel bir Dosya Arama veritabanında saklanır.
Sorgularınız da yerleştirmeye dönüştürülür. Ardından sistem, Dosya Arama deposunda en benzer ve alakalı belge parçalarını bulmak için Dosya Arama işlemi gerçekleştirir.

Yerleştirmeler için geçerlilik süresi (TTL) yoktur. Bu öğeler, manuel olarak silinene veya model kullanımdan kaldırılana kadar kalır. Ancak dosyalar 48 saat sonra silinir.

Dosya Arama API'sini kullanma sürecinin dökümünü aşağıda bulabilirsiniz:
`uploadToFileSearchStore`

1. **Dosya Arama mağazası oluşturma**: Dosya Arama mağazası, dosyalarınızdaki işlenmiş verileri içerir. Bu, semantik aramanın üzerinde çalışacağı yerleştirmeler için kalıcı kapsayıcıdır.
2. **Dosya yükleme ve Dosya Arama mağazasına aktarma**: Aynı anda dosya yükleyin ve sonuçları Dosya Arama mağazanıza aktarın. Bu işlem, ham belgenize referans veren geçici bir `File` nesne oluşturur. Bu veriler daha sonra parçalara ayrılır, Dosya Arama yerleştirmelerine dönüştürülür ve dizine eklenir. `File`
   Nesne 48 saat sonra silinir. Dosya Arama deposuna aktarılan veriler ise siz silmeyi seçene kadar süresiz olarak saklanır.
3. **Dosya Arama ile sorgu**: Son olarak, `generateContent` görüşmesinde `FileSearch` aracını kullanırsınız. Araç yapılandırmasında, aramak istediğiniz `FileSearchStore` öğesini işaret eden bir `FileSearchRetrievalResource` belirtirsiniz. Bu, modele yanıtını temellendirmek için alakalı bilgileri bulmak üzere söz konusu File Search deposunda anlamsal arama yapmasını söyler.

![Dosya Arama&#39;nın dizine ekleme ve sorgulama süreci](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=tr)

Dosya Arama'nın dizine ekleme ve sorgulama süreci

Bu şemada, *Belgeler*'den *Yerleştirme modeli*'ne ([`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) kullanılarak) giden noktalı çizgi, `uploadToFileSearchStore` API'yi (*Dosya depolama*'yı atlayarak) temsil eder.
Aksi takdirde, dosyaları ayrı ayrı oluşturmak ve ardından içe aktarmak için [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr)'yi kullanmak, dizine ekleme sürecini *Dokümanlar*'dan *Dosya depolama*'ya ve ardından *Yerleştirme modeli*'ne taşır.

## Dosya Arama'yı saklar

File Search mağazası, doküman yerleştirmelerinizin bulunduğu bir kapsayıcıdır. Dosya API'si aracılığıyla yüklenen ham dosyalar 48 saat sonra silinirken, Dosya Arama mağazasına aktarılan veriler, siz manuel olarak silene kadar süresiz olarak saklanır. Dokümanlarınızı düzenlemek için birden fazla Dosya Arama deposu oluşturabilirsiniz. `FileSearchStore` API, dosya arama depolarınızı yönetmek için oluşturma, listeleme, alma ve silme işlemlerini yapmanıza olanak tanır. Dosya Arama mağazası adları küresel kapsamlıdır.

Dosya Arama mağazalarınızı nasıl yönetebileceğinize dair bazı örnekleri aşağıda bulabilirsiniz:

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

## Dosya Arama belgeleri

Dosya depolarınızdaki tek tek dokümanları `list`, `get` ve `delete` için [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=tr) API ile yönetebilirsiniz.

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

## Dosya meta verileri

Dosyalarınızı filtrelemenize yardımcı olması veya ek bağlam bilgisi sağlaması için dosyalarınıza özel meta veriler ekleyebilirsiniz. Meta veriler, anahtar/değer çiftlerinden oluşan bir settir.

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

Bu özellik, Dosya Arama deposunda birden fazla dokümanınız olduğunda ve yalnızca bir alt kümede arama yapmak istediğinizde kullanışlıdır.

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

`metadata_filter` için liste filtresi söz dizimini uygulama ile ilgili yönergeleri [google.aip.dev/160](https://google.aip.dev/160) adresinde bulabilirsiniz.

## Çok formatlı dosya arama

Çok formatlı dosya arama özelliği, resimleri yerel olarak yerleştirmenize ve aramanıza olanak tanıyarak zengin ve çok formatlı RAG uygulamaları oluşturmanızı sağlar.

### Yerleştirme modelini yapılandırma

`FileSearchStore` oluşturduğunuzda, çok formatlı bir model kullanmak için varsayılan yalnızca metin içeren yerleştirme modelini geçersiz kılmanız gerekir. Hem metinleri hem de resimleri işlemek için `models/gemini-embedding-2` simgesini kullanın.

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

### Resim yükle

Çok formatlı yerleştirme modeliyle mağazayı oluşturduktan sonra, [Doğrudan Dosya Arama mağazasına yükleme](#upload) veya [Dosyaları içe aktarma](#importing-files) başlıklı makalelerde açıklanan yükleme API'lerini kullanarak doğrudan resim dosyaları yükleyebilirsiniz.

**Resim dosyası koşulları:**

- Resim dosyalarının çözünürlüğü en fazla 4K x 4K piksel olmalıdır.
- Desteklenen biçimler PNG ve JPEG'dir.

## Alıntılar

Dosya Arama'yı kullandığınızda modelin yanıtında, yüklenen dokümanlarınızın hangi bölümlerinin yanıtı oluşturmak için kullanıldığını belirten alıntılar yer alabilir. Bu, doğruluk kontrolü ve doğrulama işlemlerine yardımcı olur.

Alıntı bilgilerine yanıtın `grounding_metadata` özelliği üzerinden erişebilirsiniz.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

Temellendirme meta verilerinin yapısı hakkında ayrıntılı bilgi için [Dosya Arama çözüm kitabındaki](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) örnekleri veya [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr#attributing_sources_with_inline_citations) dokümanlarındaki temellendirme bölümünü inceleyin.

### Sayfa numaraları

Sayfaları olan belgelerle (ör. PDF'ler) Dosya Arama'yı kullandığınızda modelin yanıtında, bilgilerin bulunduğu sayfa numarası yer alabilir.
Bu bilgilere `page_number` özelliğini kullanarak erişebilirsiniz.
`retrieved_context`

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

### Medya alıntıları

Model, oluşturma sırasında bir resim parçasını referans aldığında API, temellendirme meta verilerinde `media_id` içeren bir alıntı döndürür. Modelin referans verdiği tam görüntü parçasını indirmek için bu<0x0x0A>kimliği kullanabilirsiniz. Bu `media_id`, birden fazla arama çağrısında kalıcıdır. Bu sayede, aynı resmi güvenilir bir şekilde alabilir veya kimliği kullanarak önbelleğe alabilirsiniz.

Aşağıdaki snippet, örnek bir REST yanıtıdır:

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

Aşağıdaki kod snippet'lerinde `media_id` değerinin nasıl alınacağı ve medyanın nasıl indirileceği gösterilmektedir:

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

## Temellendirme verilerindeki özel meta veriler

Dosyalarınıza özel meta veriler eklediyseniz bunlara modelin yanıtının temel meta verilerinden erişebilirsiniz. Bu, kaynak dokümanlarınızdaki ek bağlamı (ör. URL'ler, sayfa numaraları veya yazarlar) uygulama mantığınıza aktarmak için kullanışlıdır. `retrieved_context` içindeki her `grounding_chunk` bu özel meta verileri içerir.

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

## Yapılandırılmış çıkış

Gemini 3 modellerinden itibaren, dosya arama aracını [yapılandırılmış çıktılarla](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) birlikte kullanabilirsiniz.

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

## Desteklenen modeller

Aşağıdaki modellerde Dosya Arama özelliği desteklenir:

| Model | Dosya Arama |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Desteklenen araç kombinasyonları

Gemini 3 modelleri, yerleşik araçların (ör. Dosya Arama) özel araçlarla (işlev çağrısı) birlikte kullanılmasını destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

## Desteklenen dosya türleri

Dosya Arama, aşağıdaki bölümlerde listelenen çok çeşitli dosya biçimlerini destekler.

### Uygulama dosyası türleri

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

### Metin dosyası türleri

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

## Sınırlamalar

- **Live API:** Dosya Arama, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr)'de desteklenmez.
- **Araç uyumsuzluğu:** Dosya Arama, şu anda [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) ve [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) gibi diğer araçlarla birlikte kullanılamaz.

### Hız sınırları

File Search API, hizmet kararlılığını sağlamak için aşağıdaki sınırlara sahiptir:

- **Maksimum dosya boyutu / belge başına sınır**: 100 MB
- **Proje Dosya Arama'nın depoladığı toplam boyut** (kullanıcı katmanına göre):
  - **Ücretsiz**: 1 GB
  - **1. katman**: 10 GB
  - **2. katman**: 100 GB
  - **3. Katman**: 1 TB
- **Öneri**: Optimal alma gecikmeleri sağlamak için her bir Dosya Arama deposunun boyutunu 20 GB'ın altında tutun.

## Fiyatlandırma

- Mevcut [yerleştirme fiyatlandırmasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-embedding-2) göre, dizine ekleme sırasında yerleştirmeler için ücretlendirilirsiniz.
- Depolama alanı ücretsizdir.
- Sorgu zamanı yerleştirmeleri ücretsizdir.
- Alınan doküman jetonları normal [bağlam jetonları](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) olarak ücretlendirilir.

## Sırada ne var?

- [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=tr) ve File Search [Documents](https://ai.google.dev/api/file-search/documents?hl=tr) için API referansını ziyaret edin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-23 UTC."],[],[]]
