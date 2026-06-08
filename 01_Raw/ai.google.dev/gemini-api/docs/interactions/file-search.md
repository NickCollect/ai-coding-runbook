---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ar
fetched_at: 2026-06-08T05:27:06.624551+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البحث عن الملفات

تتيح Gemini API ميزة "التوليد المعزّز بالاسترجاع" من خلال أداة "البحث في الملفات". تستورد ميزة "البحث عن الملفات" بياناتك وتقسّمها وتفهرسها لتتيح استرجاع المعلومات ذات الصلة بسرعة استنادًا إلى طلب مقدَّم. يتم بعد ذلك استخدام هذه المعلومات المسترجَعة كسياق للنموذج، ما يتيح له تقديم إجابات أكثر دقة وملاءمةً. تتوفّر أيضًا إمكانات متعدّدة الوسائط في ميزة &quot;البحث عن الملفات&quot;، وذلك من خلال تضمين النصوص باستخدام `gemini-embedding-001`، وتضمين الصور والوسائط المتعدّدة باستخدام `gemini-embedding-2`.

تكون عملية تخزين الملفات وإنشاء عمليات التضمين عند وقت طلب البحث مجانية، ولن تدفع إلا مقابل إنشاء عمليات التضمين عند فهرسة ملفاتك لأول مرة وتكلفة الرموز المميزة العادية الخاصة بمدخلات ومخرجات نموذج Gemini. يساهم نموذج الفوترة الجديد هذا في تسهيل عملية إنشاء &quot;أداة البحث عن الملفات&quot; وتوسيع نطاقها، كما يقلّل من تكلفتها. راجِع قسم [الأسعار](#pricing) لمعرفة التفاصيل.

## التحميل مباشرةً إلى متجر "بحث الملفات"

يوضّح المثال التالي كيفية تحميل ملف مباشرةً إلى
[مخزن البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

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
    model="gemini-3.5-flash",
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
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
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
    model: "gemini-3.5-flash",
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

راجِع مرجع واجهة برمجة التطبيقات [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore) للحصول على مزيد من المعلومات.

## استيراد الملفات

بدلاً من ذلك، يمكنك تحميل ملف حالي و[استيراده إلى متجر البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) باتّباع الخطوات التالية:

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

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
    model="gemini-3.5-flash",
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
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
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
    model: "gemini-3.5-flash",
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

راجِع مرجع واجهة برمجة التطبيقات [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) للحصول على مزيد من المعلومات.

## إعدادات التقسيم

عند استيراد ملف إلى مستودع &quot;البحث عن الملفات&quot;، يتم تقسيمه تلقائيًا إلى أجزاء، وتضمينه، وفهرسته، وتحميله إلى مستودع &quot;البحث عن الملفات&quot;. إذا كنت بحاجة إلى المزيد من التحكّم في استراتيجية التقسيم، يمكنك تحديد إعداد [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#request-body_5) لضبط الحد الأقصى لعدد الرموز المميزة لكل جزء والحد الأقصى لعدد الرموز المميزة المتداخلة.

### Python

```
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

لاستخدام متجر "بحث الملفات"، مرِّره كأداة إلى طريقة `interactions.create`، كما هو موضّح في المثالَين [تحميل](#upload) و[استيراد](#importing-files).

## آلية العمل

تستخدم ميزة &quot;البحث في الملفات&quot; أسلوبًا يُعرف باسم البحث الدلالي للعثور على معلومات ذات صلة بطلب المستخدم. وعلى عكس البحث العادي المستند إلى الكلمات الرئيسية، يفهم البحث الدلالي معنى طلب البحث وسياقه.

عند استيراد ملف، يتم تحويله إلى تمثيلات رقمية تُعرف باسم
[التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)، وهي تلتقط المعنى الدلالي للمحتوى الذي تم تحميله. يتم تخزين هذه التضمينات في قاعدة بيانات متخصصة في "البحث عن الملفات".
عند إجراء طلب بحث، يتم تحويله أيضًا إلى تضمين. بعد ذلك، يجري النظام عملية &quot;البحث في الملفات&quot; للعثور على أجزاء المستندات الأكثر تشابهًا وملاءمةً من مستودع &quot;البحث في الملفات&quot;.

لا تتوفّر مدة بقاء (TTL) للتضمينات، بل تبقى متاحة إلى أن يتم حذفها يدويًا أو عند إيقاف النموذج نهائيًا، بينما يتم حذف الملفات بعد 48 ساعة.

في ما يلي تفصيل لعملية استخدام واجهة برمجة التطبيقات File Search
`uploadToFileSearchStore`:

1. **إنشاء مستودع بحث في الملفات**: يحتوي مستودع بحث في الملفات على البيانات المعالَجة من ملفاتك. وهي الحاوية الدائمة لعمليات التضمين التي سيتم إجراء البحث الدلالي عليها.
2. **تحميل ملف واستيراده إلى مستودع "البحث عن الملفات"**: يمكنك تحميل ملف واستيراد النتائج إلى مستودع "البحث عن الملفات" في الوقت نفسه، ما يؤدي إلى إنشاء عنصر `File` مؤقت، وهو مرجع إلى المستند الأولي. بعد ذلك، يتم تقسيم البيانات إلى أجزاء وتحويلها إلى تضمينات "البحث عن الملفات" وفهرستها. يتم حذف العنصر `File` بعد 48 ساعة، بينما يتم تخزين البيانات التي تم استيرادها إلى مستودع "البحث عن الملفات" إلى أجل غير مسمى إلى أن تختار حذفها.
3. **طلب البحث باستخدام أداة "البحث في الملفات"**: أخيرًا، يمكنك استخدام أداة `FileSearch` في طلب `generateContent`. في إعدادات الأداة، يمكنك تحديد `FileSearchRetrievalResource`، الذي يشير إلى `FileSearchStore` الذي تريد البحث فيه. يطلب ذلك من النموذج إجراء بحث دلالي في مخزن "البحث في الملفات" المحدّد للعثور على معلومات ذات صلة لتضمينها في الرد.

![عملية الفهرسة وطلب البحث في &quot;بحث الملفات&quot;](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ar)

عملية الفهرسة والبحث في &quot;بحث الملفات&quot;

في هذا المخطط، يمثّل الخط المتقطّع من *المستندات* إلى *نموذج التضمين* (باستخدام [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)) واجهة برمجة التطبيقات `uploadToFileSearchStore` (مع تجاوز *مساحة تخزين الملفات*).
في ما عدا ذلك، يؤدي استخدام [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ar) لإنشاء الملفات بشكل منفصل ثم استيرادها إلى نقل عملية الفهرسة من *المستندات* إلى *مساحة تخزين الملفات* ثم إلى *نموذج التضمين*.

## متاجر "بحث الملفات"

مستودع "البحث عن الملفات" هو حاوية لتضمينات المستندات. في حين يتم حذف الملفات الأولية التي تم تحميلها من خلال File API بعد 48 ساعة، يتم تخزين البيانات التي تم استيرادها إلى مستودع &quot;بحث الملفات&quot; إلى أجل غير مسمى إلى أن تحذفها يدويًا. يمكنك إنشاء عدة مستودعات بحث في الملفات لتنظيم مستنداتك. تتيح لك واجهة برمجة التطبيقات
`FileSearchStore` إنشاء قوائم بملفاتك وحذفها والبحث عنها وإدارتها. يتم تحديد نطاق أسماء متاجر "بحث الملفات" على مستوى العالم.

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

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc', config={'force': True})
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

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}&force=true"
```

## البيانات الوصفية للملف

يمكنك إضافة بيانات وصفية مخصّصة إلى ملفاتك للمساعدة في فلترتها أو تقديم سياق إضافي، والبيانات الوصفية هي مجموعة من أزواج المفتاح والقيمة.

### Python

```
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

يكون هذا الإجراء مفيدًا عندما يكون لديك مستندات متعددة في مستودع &quot;بحث الملفات&quot; وتريد البحث في مجموعة فرعية منها فقط.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d '{
            "model": "gemini-3.5-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

يمكن العثور على إرشادات حول تنفيذ بنية فلتر القائمة الخاصة بـ `metadata_filter` على الرابط [google.aip.dev/160](https://google.aip.dev/160).

## البحث المتعدّد الوسائط في الملفات

تتيح لك ميزة "البحث في الملفات" المتعدّد الوسائط تضمين الصور والبحث فيها بشكلٍ مدمج، ما يتيح إنشاء تطبيقات غنية ومتعدّدة الوسائط تستخدم "التوليد المعزّز بالاسترجاع".

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

بعد إنشاء المتجر باستخدام نموذج التضمين المتعدّد الوسائط، يمكنك تحميل ملفات الصور مباشرةً باستخدام واجهات برمجة التطبيقات نفسها الموضّحة في [التحميل مباشرةً إلى متجر "بحث الملفات"](#upload) أو [استيراد الملفات](#importing-files).

**متطلبات ملف الصورة:**

- يجب ألا تزيد دقة ملفات الصور عن 4K x 4K بكسل.
- التنسيقات المتوافقة هي PNG وJPEG.

## الاقتباسات

عند استخدام &quot;البحث في الملفات&quot;، قد يتضمّن ردّ النموذج اقتباسات تحدّد الأجزاء من المستندات التي حمّلتها والتي تم استخدامها لإنشاء الإجابة، ما يساعد في التحقّق من صحة المعلومات.

يمكنك الوصول إلى معلومات الاقتباس من خلال السمة `annotations` داخل كتل `content` الخاصة بالخطوة `model_output` في الردّ.

### Python

```
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
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

للحصول على معلومات تفصيلية حول بنية الاقتباسات، يُرجى الاطّلاع على
[مرجع واجهة برمجة التطبيقات للتفاعلات](https://ai.google.dev/api/interactions-api?hl=ar#Resource:FileCitation).

### أرقام الصفحات

عند استخدام ميزة "البحث في الملفات" مع المستندات التي تتضمّن صفحات (مثل ملفات PDF)، قد يتضمّن ردّ النموذج رقم الصفحة التي تم العثور على المعلومات فيها.
يمكنك الوصول إلى هذه المعلومات من خلال السمة `page_number` الخاصة بالتعليق التوضيحي `file_citation`.

### Python

```
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

### اقتباسات من الوسائط

عندما يشير النموذج إلى جزء من صورة أثناء عملية الإنشاء، تعرض واجهة برمجة التطبيقات تعليقًا توضيحيًا من النوع `file_citation` في التعليقات التوضيحية يتضمّن `media_id`. يمكنك استخدام هذا المعرّف لتنزيل جزء الصورة الذي أشار إليه النموذج. يكون `media_id` هذا ثابتًا في طلبات البحث المتعددة، ما يتيح لك استرداد الصورة نفسها أو تخزينها مؤقتًا بشكل موثوق باستخدام المعرّف.

المقتطف التالي هو مثال على خطوة استجابة REST:

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

توضّح مقتطفات الرموز البرمجية التالية كيفية استرداد `media_id` وتنزيل الوسائط:

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
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

## البيانات الوصفية المخصّصة

إذا أضفت بيانات وصفية مخصّصة إلى ملفاتك، يمكنك الوصول إليها في التعليقات التوضيحية الخاصة برد النموذج. ويكون ذلك مفيدًا في تمرير سياق إضافي (مثل عناوين URL أو أرقام الصفحات أو المؤلّفين) من المستندات المصدر إلى منطق التطبيق. يحتوي كل تعليق توضيحي للاقتباس من النوع `file_citation`
على هذه البيانات الوصفية المخصّصة.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
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

## ناتج منظَّم

بدءًا من طُرز Gemini 3، يمكنك دمج أداة البحث عن الملفات مع
[النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ar).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
result = Money.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
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
    model: "gemini-3.5-flash",
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

  const result = moneySchema.parse(JSON.parse(interaction.output_text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
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

## النماذج المتوافقة

تتيح الطُرز التالية استخدام ميزة "البحث عن الملفات":

| الطراز | البحث عن الملفات |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "البحث عن الملفات") والأدوات المخصّصة (استدعاء الدالة). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## أنواع الملفات المعتمدة

يتيح &quot;بحث الملفات&quot; مجموعة كبيرة من تنسيقات الملفات، والمدرَجة في الأقسام التالية.

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

- **واجهة برمجة التطبيقات المباشرة:** لا تتوفّر ميزة &quot;البحث عن الملفات&quot; في [واجهة برمجة التطبيقات المباشرة](https://ai.google.dev/gemini-api/docs/live?hl=ar).
- **عدم توافق الأداة:** لا يمكن حاليًا استخدام &quot;البحث عن ملف&quot; مع أدوات أخرى، مثل [تحديد المصدر من خلال &quot;بحث Search&quot;](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar) وغير ذلك.

### حدود معدّل الاستخدام

تفرض واجهة برمجة التطبيقات "البحث عن الملفات" الحدود التالية لضمان استقرار الخدمة:

- **الحدّ الأقصى لحجم الملف / الحدّ الأقصى لكل مستند**: 100 ميغابايت
- **إجمالي حجم مساحات تخزين "البحث عن الملفات" في المشروع** (استنادًا إلى فئة المستخدم):
  - **الخطة المجانية**: 1 غيغابايت
  - **المستوى 1**: 10 غيغابايت
  - **المستوى 2**: ‏100 غيغابايت
  - **المستوى 3**: 1 تيرابايت
- **اقتراح**: يجب ألا يتجاوز حجم كل مستودع بيانات في "بحث الملفات" 20 غيغابايت لضمان أفضل أوقات استرجاع.

## الأسعار

- يتم تحصيل رسوم منك مقابل التضمينات في وقت الفهرسة استنادًا إلى [أسعار التضمينات](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-embedding-2) الحالية.
- تتوفر مساحة التخزين بدون أي رسوم.
- إنّ تضمينات وقت طلب البحث مجانية.
- يتم تحصيل رسوم من الرموز المميزة للمستندات التي تم استرجاعها باعتبارها
  [رموزًا مميزة للسياق](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ar) عادية.

## الخطوات التالية

- انتقِل إلى مرجع واجهة برمجة التطبيقات [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=ar) و[Documents](https://ai.google.dev/api/file-search/documents?hl=ar) في File Search.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
