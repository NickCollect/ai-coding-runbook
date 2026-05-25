---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=ar
fetched_at: 2026-05-25T05:20:57.959731+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البحث عن الملفات

تتيح Gemini API ميزة "التوليد المعزّز بالاسترجاع" ("RAG") من خلال أداة "البحث في الملفات". تستورد ميزة "البحث عن الملفات" بياناتك وتقسّمها إلى أجزاء وتفهرسها لتتيح استرجاع المعلومات ذات الصلة بسرعة استنادًا إلى طلب مقدَّم. يتم بعد ذلك استخدام هذه المعلومات المسترجَعة كسياق للنموذج، ما يتيح له تقديم إجابات أكثر دقة وملاءمةً. تتوفّر أيضًا إمكانات البحث المتعدّد الوسائط في ميزة &quot;البحث عن الملفات&quot;، وذلك من خلال تضمين النصوص المتوافق مع `gemini-embedding-001`، وتضمين الصور والوسائط المتعددة المتوافق مع `gemini-embedding-2`.

تكون عملية تخزين الملفات وإنشاء عمليات التضمين عند وقت طلب البحث مجانية، ولن تدفع إلا مقابل إنشاء عمليات التضمين عند فهرسة ملفاتك للمرة الأولى وتكلفة الرموز المميزة العادية الخاصة بمدخلات ومخرجات نموذج Gemini. يساهم نموذج الفوترة الجديد هذا في تسهيل عملية إنشاء &quot;أداة البحث عن الملفات&quot; وتوسيع نطاقها، كما يجعلها أكثر فعالية من حيث التكلفة. راجِع قسم [الأسعار](#pricing) لمعرفة التفاصيل.

## التحميل مباشرةً إلى "متجر البحث عن الملفات"

يوضّح هذا المثال كيفية تحميل ملف مباشرةً إلى [مستودع البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore):

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

راجِع مرجع واجهة برمجة التطبيقات [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore) للحصول على مزيد من المعلومات.

## استيراد الملفات

بدلاً من ذلك، يمكنك تحميل ملف حالي و[استيراده إلى مساحة تخزين البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) باتّباع الخطوات التالية:

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

راجِع مرجع واجهة برمجة التطبيقات [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) للحصول على مزيد من المعلومات.

## إعدادات تقسيم المحتوى

عند استيراد ملف إلى مستودع &quot;البحث عن الملفات&quot;، يتم تقسيمه تلقائيًا إلى أجزاء، وتضمينه، وفهرسته، وتحميله إلى مستودع &quot;البحث عن الملفات&quot;. إذا كنت بحاجة إلى المزيد من التحكّم في استراتيجية التقسيم، يمكنك تحديد إعداد [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#request-body_5) لضبط الحد الأقصى لعدد الرموز المميزة لكل جزء والحد الأقصى لعدد الرموز المميزة المتداخلة.

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

لاستخدام متجر "بحث الملفات"، مرِّره كأداة إلى طريقة `generateContent`، كما هو موضّح في المثالَين [تحميل](#upload) و[استيراد](#importing-files).

## آلية العمل

تستخدم ميزة &quot;البحث عن الملفات&quot; أسلوبًا يُعرف باسم البحث الدلالي للعثور على معلومات ذات صلة بطلب المستخدم. على عكس البحث العادي المستند إلى الكلمات الرئيسية، يفهم البحث الدلالي المعنى والسياق الخاصين بطلب البحث.

عند استيراد ملف، يتم تحويله إلى تمثيلات رقمية تُعرف باسم
[التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)، وهي تلتقط المعنى الدلالي للمحتوى الذي تم تحميله. يتم تخزين هذه التضمينات في قاعدة بيانات متخصصة في "البحث عن الملفات".
عند إجراء طلب بحث، يتم تحويله أيضًا إلى تضمين. بعد ذلك، يجري النظام عملية &quot;بحث في الملفات&quot; للعثور على أجزاء المستندات الأكثر تشابهًا وملاءمةً من مستودع &quot;بحث في الملفات&quot;.

لا تتوفّر مدة بقاء (TTL) للتضمينات، بل تبقى متاحة إلى أن يتم حذفها يدويًا أو عند إيقاف النموذج نهائيًا. أما الملفات، فيتم حذفها بعد 48 ساعة.

في ما يلي تفصيل لعملية استخدام واجهة برمجة التطبيقات File Search
`uploadToFileSearchStore`:

1. **إنشاء مستودع "بحث في الملفات"**: يحتوي مستودع "بحث في الملفات" على البيانات المعالَجة من ملفاتك. وهي الحاوية الدائمة لعمليات التضمين التي سيتم إجراء البحث الدلالي عليها.
2. **تحميل ملف واستيراده إلى مستودع &quot;البحث عن الملفات&quot;**: يمكنك تحميل ملف واستيراد النتائج إلى مستودع &quot;البحث عن الملفات&quot; في الوقت نفسه. يؤدي ذلك إلى إنشاء كائن `File` مؤقت، وهو مرجع إلى مستندك الأولي. بعد ذلك، يتم تقسيم هذه البيانات إلى أجزاء وتحويلها إلى تضمينات &quot;بحث الملفات&quot; وفهرستها. يتم حذف عنصر `File` بعد 48 ساعة، بينما يتم تخزين البيانات التي تم استيرادها إلى مساحة تخزين &quot;البحث عن الملفات&quot; إلى أجل غير مسمى إلى أن تختار حذفها.
3. **طلب البحث باستخدام "البحث عن الملفات"**: أخيرًا، يمكنك استخدام أداة `FileSearch` في مكالمة `generateContent`. في إعدادات الأداة، يمكنك تحديد
   `FileSearchRetrievalResource`، الذي يشير إلى `FileSearchStore` الذي تريد البحث فيه. يطلب ذلك من النموذج إجراء بحث دلالي في مخزن &quot;بحث الملفات&quot; المحدّد للعثور على معلومات ذات صلة يستند إليها في رده.

![عملية الفهرسة وطلب البحث في &quot;بحث الملفات&quot;](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ar)

عملية الفهرسة والبحث في &quot;بحث الملفات&quot;

في هذا الرسم التخطيطي، يمثّل الخط المتقطّع من *المستندات* إلى *نموذج التضمين*
(باستخدام [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar))
واجهة برمجة التطبيقات `uploadToFileSearchStore` (مع تجاوز *تخزين الملفات*).
في ما عدا ذلك، يؤدي استخدام [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) لإنشاء الملفات بشكل منفصل ثم استيرادها إلى نقل عملية الفهرسة من *المستندات* إلى *مساحة تخزين الملفات* ثم إلى *نموذج التضمين*.

## متاجر "بحث الملفات"

مخزن "البحث عن الملفات" هو حاوية لتضمينات المستندات. في حين يتم حذف الملفات الأولية التي تم تحميلها من خلال File API بعد 48 ساعة، يتم تخزين البيانات التي تم استيرادها إلى مستودع "بحث الملفات" إلى أجل غير مسمى إلى أن تحذفها يدويًا. يمكنك إنشاء عدة مستودعات بحث في الملفات لتنظيم مستنداتك. تتيح لك واجهة برمجة التطبيقات
`FileSearchStore` إنشاء قوائم بملفاتك وحذفها والبحث عنها وإدارتها. تكون أسماء متاجر "بحث الملفات" محدّدة النطاق على مستوى العالم.

في ما يلي بعض الأمثلة على كيفية إدارة متاجر "بحث الملفات":

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

## مستندات "البحث في الملفات"

يمكنك إدارة المستندات الفردية في مخازن الملفات باستخدام واجهة برمجة التطبيقات
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=ar) من أجل `list` كل مستند
في مخزن بحث الملفات، و`get` معلومات حول مستند، و`delete` مستند
حسب الاسم.

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

## البيانات الوصفية للملف

يمكنك إضافة بيانات وصفية مخصّصة إلى ملفاتك للمساعدة في فلترتها أو تقديم سياق إضافي. بيانات التعريف هي مجموعة من أزواج المفاتيح والقيم.

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

يكون ذلك مفيدًا عندما يكون لديك مستندات متعددة في متجر "بحث الملفات" وتريد البحث في مجموعة فرعية منها فقط.

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

يمكن العثور على إرشادات حول تنفيذ بنية فلتر القائمة الخاصة بـ `metadata_filter` على الرابط [google.aip.dev/160](https://google.aip.dev/160).

## البحث المتعدد الوسائط في الملفات

تتيح لك ميزة "البحث في الملفات" المتعدّد الوسائط تضمين الصور والبحث فيها بشكلٍ أصلي، ما يتيح إنشاء تطبيقات غنية ومتعدّدة الوسائط تستخدم "التوليد المعزّز بالاسترجاع".

### ضبط نموذج التضمين

عند إنشاء `FileSearchStore`، عليك تجاهل نموذج التضمين التلقائي النصي فقط واستخدام نموذج متعدد الوسائط. استخدِم `models/gemini-embedding-2` لمعالجة كل من النص والصور.

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

### تحميل صور

بعد إنشاء المتجر باستخدام نموذج التضمين المتعدّد الوسائط، يمكنك تحميل ملفات الصور مباشرةً باستخدام واجهات برمجة التطبيقات نفسها الخاصة بالتحميل والموضّحة في [التحميل مباشرةً إلى متجر "بحث الملفات"](#upload) أو [استيراد الملفات](#importing-files).

**متطلبات ملف الصورة:**

- يجب ألا تزيد دقة ملفات الصور عن 4K x 4K بكسل.
- التنسيقات المتوافقة هي PNG وJPEG.

## الاقتباسات

عند استخدام &quot;البحث عن الملفات&quot;، قد يتضمّن ردّ النموذج اقتباسات تحدّد الأجزاء من المستندات التي حمّلتها والتي تم استخدامها لإنشاء الإجابة. ويساعد ذلك في التحقّق من صحة المعلومات.

يمكنك الوصول إلى معلومات الاقتباس من خلال السمة `grounding_metadata` في الرد.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

للحصول على معلومات مفصّلة حول بنية البيانات الوصفية الخاصة بالاستناد إلى مصادر، يمكنك الاطّلاع على الأمثلة في [كتاب الطبخ الخاص بميزة &quot;البحث عن الملفات&quot;](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) أو [قسم &quot;الاستناد إلى مصادر&quot; في مستندات &quot;الاستناد إلى مصادر مع بحث Google&quot;](https://ai.google.dev/gemini-api/docs/google-search?hl=ar#attributing_sources_with_inline_citations).

### أرقام الصفحات

عند استخدام ميزة "البحث في الملفات" مع المستندات التي تتضمّن صفحات (مثل ملفات PDF)، قد يتضمّن ردّ النموذج رقم الصفحة التي تم العثور على المعلومات فيها.
يمكنك الوصول إلى هذه المعلومات من خلال السمة `page_number` الخاصة بـ `retrieved_context`.

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

### اقتباسات من الوسائط

عندما يشير النموذج إلى جزء من صورة أثناء عملية الإنشاء، تعرض واجهة برمجة التطبيقات اقتباسًا في البيانات الوصفية لتحديد المصدر يتضمّن `media_id`. يمكنك استخدام هذا المعرّف لتنزيل جزء الصورة الذي أشار إليه النموذج بالضبط. يكون هذا `media_id` ثابتًا في طلبات البحث المتعددة، ما يتيح لك استرداد الصورة نفسها أو تخزينها مؤقتًا بشكل موثوق باستخدام المعرّف.

المقتطف التالي هو مثال على استجابة REST:

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

توضّح مقتطفات الرموز البرمجية التالية كيفية استرداد `media_id` وتنزيل الوسائط:

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

## البيانات الوصفية المخصّصة في بيانات التأسيس

إذا أضفت بيانات وصفية مخصّصة إلى ملفاتك، يمكنك الوصول إليها في البيانات الوصفية الخاصة بالمستندات الأساسية التي استند إليها ردّ النموذج. ويكون ذلك مفيدًا لتمرير سياق إضافي (مثل عناوين URL أو أرقام الصفحات أو المؤلّفين) من المستندات المصدر إلى منطق التطبيق. يحتوي كل `grounding_chunk` في
`retrieved_context` على هذه البيانات الوصفية المخصّصة.

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

## الناتج المنظَّم

بدءًا من نماذج Gemini 3، يمكنك دمج أداة البحث عن الملفات مع
[النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar).

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

## النماذج المتوافقة

تتيح الطُرز التالية استخدام ميزة "البحث عن الملفات":

| الطراز | البحث عن الملفات |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [‫Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "البحث عن الملفات") والأدوات المخصّصة (استدعاء الدالة). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## أنواع الملفات المعتمدة

يتيح &quot;بحث الملفات&quot; مجموعة كبيرة من تنسيقات الملفات، كما هو موضّح في الأقسام التالية.

### أنواع ملفات التطبيقات

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

### أنواع الملفات النصية

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

## القيود

- **واجهة برمجة التطبيقات المباشرة:** لا تتوفّر ميزة &quot;البحث عن الملفات&quot; في
  [واجهة برمجة التطبيقات المباشرة](https://ai.google.dev/gemini-api/docs/live?hl=ar).
- **عدم التوافق مع أدوات أخرى:** لا يمكن استخدام &quot;البحث عن ملف&quot; مع أدوات أخرى، مثل [تحديد المصدر من خلال &quot;بحث Search&quot;](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) وغيرها في الوقت الحالي.

### حدود معدّل الاستخدام

تفرض واجهة برمجة التطبيقات "بحث الملفات" الحدود التالية لضمان استقرار الخدمة:

- **الحدّ الأقصى لحجم الملف / الحدّ الأقصى لكل مستند**: 100 ميغابايت
- **إجمالي حجم مساحات تخزين "البحث عن الملفات" في المشروع** (استنادًا إلى فئة المستخدم):
  - **مجانًا**: 1 غيغابايت
  - **المستوى 1**: 10 غيغابايت
  - **المستوى 2**: ‏100 غيغابايت
  - **المستوى 3**: 1 تيرابايت
- **اقتراح**: يجب ألا يتجاوز حجم كل مستودع بيانات في "بحث الملفات" 20 غيغابايت لضمان أفضل أوقات استرجاع.

## الأسعار

- يتم تحصيل رسوم منك مقابل التضمينات في وقت الفهرسة استنادًا إلى [أسعار التضمينات](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-embedding-2) الحالية.
- تتوفر مساحة التخزين بدون أي رسوم.
- إنّ تضمينات وقت طلب البحث مجانية.
- يتم تحصيل رسوم من الرموز المميزة للمستندات التي تم استرجاعها باعتبارها
  [رموزًا مميزة للسياق](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) عادية.

## الخطوات التالية

- انتقِل إلى مرجع واجهة برمجة التطبيقات [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=ar) و[Documents](https://ai.google.dev/api/file-search/documents?hl=ar) في File Search.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
