---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=hi
fetched_at: 2026-10-05T06:41:49.044324+00:00
title: "\u092b\u093c\u093e\u0907\u0932 \u0916\u094b\u091c\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# फ़ाइल खोजना

Gemini API, फ़ाइल खोजने के टूल की मदद से, Retrieval Augmented Generation ("RAG") की सुविधा देता है. File Search, आपके डेटा को इंपोर्ट करता है, उसे छोटे-छोटे हिस्सों में बांटता है, और इंडेक्स करता है. इससे, दिए गए प्रॉम्प्ट के आधार पर काम की जानकारी को तेज़ी से वापस पाने में मदद मिलती है. इसके बाद, इस जानकारी का इस्तेमाल मॉडल के लिए कॉन्टेक्स्ट के तौर पर किया जाता है. इससे मॉडल को ज़्यादा सटीक और काम के जवाब देने में मदद मिलती है. फ़ाइल खोजने की सुविधा में, टेक्स्ट एम्बेडिंग के साथ-साथ मल्टीमॉडल क्षमताओं को भी इस्तेमाल किया जा सकता है. इसके लिए, `gemini-embedding-001` और इमेज/मल्टीमॉडल एम्बेडिंग की सुविधा देने वाले `gemini-embedding-2` का इस्तेमाल किया जाता है.

फ़ाइल स्टोरेज और क्वेरी के समय एम्बेडिंग जनरेट करने की सुविधा बिना किसी शुल्क के उपलब्ध है. आपको सिर्फ़ तब पेमेंट करना होगा, जब पहली बार अपनी फ़ाइलों को इंडेक्स किया जाता है और Gemini के सामान्य मॉडल के इनपुट / आउटपुट टोकन की सामान्य लागत लगती है. बिलिंग के इस नए मॉडल की मदद से, फ़ाइल खोजने वाले टूल को बनाना और उसे स्केल करना आसान और किफ़ायती हो जाता है. ज़्यादा जानकारी के लिए, [कीमत](#pricing) सेक्शन देखें.

## फ़ाइल खोज स्टोर में सीधे तौर पर अपलोड करना

इस उदाहरण में, [फ़ाइल खोज स्टोर](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-media.uploadtofilesearchstore) में फ़ाइल को सीधे अपलोड करने का तरीका बताया गया है:

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

ज़्यादा जानकारी के लिए, [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-media.uploadtofilesearchstore) के लिए एपीआई रेफ़रंस देखें.

## फ़ाइलें इंपोर्ट करना

इसके अलावा, किसी मौजूदा फ़ाइल को अपलोड करके, [उसे फ़ाइल खोजने की सुविधा वाले स्टोर में इंपोर्ट किया जा सकता है](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-filesearchstores.importfile):

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

ज़्यादा जानकारी के लिए, [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-filesearchstores.importfile) के लिए एपीआई रेफ़रंस देखें.

## कॉन्फ़िगरेशन को हिस्सों में बांटना

किसी फ़ाइल को File Search स्टोर में इंपोर्ट करने पर, वह अपने-आप छोटे-छोटे हिस्सों में बंट जाती है. इसके बाद, उसे एंबेड किया जाता है, इंडेक्स किया जाता है, और File Search स्टोर में अपलोड किया जाता है. अगर आपको चंकिंग की रणनीति पर ज़्यादा कंट्रोल चाहिए, तो [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#request-body_5) सेटिंग का इस्तेमाल करें. इससे, हर चंक के लिए ज़्यादा से ज़्यादा टोकन और ओवरलैप होने वाले टोकन की ज़्यादा से ज़्यादा संख्या सेट की जा सकती है.

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

फ़ाइल खोजने की सुविधा वाले स्टोर का इस्तेमाल करने के लिए, इसे `generateContent`
तरीके में टूल के तौर पर पास करें. इसके लिए, [अपलोड करें](#upload) और [इंपोर्ट करें](#importing-files) के उदाहरण देखें.

## यह कैसे काम करता है

फ़ाइल सर्च, सिमैंटिक सर्च नाम की तकनीक का इस्तेमाल करता है. इससे वह उपयोगकर्ता के प्रॉम्प्ट से जुड़ी जानकारी ढूंढ पाता है. कीवर्ड पर आधारित स्टैंडर्ड सर्च के उलट, सिमैंटिक सर्च आपकी क्वेरी के मतलब और कॉन्टेक्स्ट को समझती है.

किसी फ़ाइल को इंपोर्ट करने पर, उसे संख्या के हिसाब से दिखाया जाता है. इसे [एम्बेडिंग](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) कहा जाता है. इससे अपलोड किए गए कॉन्टेंट का सिमैंटिक मतलब पता चलता है. इन एम्बेडिंग को, फ़ाइल खोज के खास डेटाबेस में सेव किया जाता है.
क्वेरी करने पर, उसे भी एम्बेडिंग में बदल दिया जाता है. इसके बाद, सिस्टम फ़ाइल खोज की सुविधा का इस्तेमाल करके, फ़ाइल खोज के स्टोर से मिलते-जुलते और काम के दस्तावेज़ के हिस्सों को ढूंढता है.

एम्बेडिंग के लिए कोई टाइम टू लिव (टीटीएल) नहीं होता;
ये तब तक बने रहते हैं, जब तक इन्हें मैन्युअल तरीके से मिटाया नहीं जाता या मॉडल को बंद नहीं कर दिया जाता. हालांकि, फ़ाइलें 48 घंटे बाद मिट जाती हैं.

फ़ाइल खोजने की सुविधा वाले `uploadToFileSearchStore` एपीआई का इस्तेमाल करने की प्रोसेस के बारे में यहां बताया गया है:

1. **फ़ाइल खोज का स्टोर बनाएं**: फ़ाइल खोज के स्टोर में, आपकी फ़ाइलों से प्रोसेस किया गया डेटा होता है. यह एम्बेडिंग के लिए परसिस्टेंट कंटेनर है. इस पर सिमैंटिक सर्च काम करेगी.
2. **फ़ाइल अपलोड करें और उसे फ़ाइल खोज वाले स्टोर में इंपोर्ट करें**: एक साथ फ़ाइल अपलोड करें और नतीजों को फ़ाइल खोज वाले स्टोर में इंपोर्ट करें. इससे एक
   अस्थायी `File` ऑब्जेक्ट बनता है, जो आपके ओरिजनल दस्तावेज़ का रेफ़रंस होता है. इसके बाद, उस डेटा को छोटे-छोटे हिस्सों में बांटा जाता है. साथ ही, उसे फ़ाइल खोजने की सुविधा के लिए एम्बेड किए गए डेटा में बदला जाता है और इंडेक्स किया जाता है. `File`
   ऑब्जेक्ट 48 घंटे बाद मिट जाता है. वहीं, फ़ाइल खोज में इंपोर्ट किया गया डेटा तब तक सेव रहेगा, जब तक आप उसे मिटाने का विकल्प नहीं चुनते.
3. **फ़ाइल खोजने के लिए क्वेरी**: आखिर में, `generateContent` कॉल में `FileSearch` टूल का इस्तेमाल किया जाता है. टूल कॉन्फ़िगरेशन में, आपको एक `FileSearchRetrievalResource` तय करना होता है. यह `FileSearchStore` की ओर इशारा करता है, जिसे आपको खोजना है. इससे मॉडल को उस फ़ाइल सर्च स्टोर पर सिमैंटिक सर्च करने का निर्देश मिलता है, ताकि वह अपने जवाब के लिए काम की जानकारी ढूंढ सके.

![फ़ाइल खोजने की सुविधा के लिए इंडेक्स करने और क्वेरी करने की प्रोसेस](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=hi)

फ़ाइल खोजने की सुविधा के लिए, इंडेक्स करने और क्वेरी करने की प्रोसेस

इस डायग्राम में, *Documents* से *Embedding model* तक की डॉटेड लाइन ([`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) का इस्तेमाल करके) `uploadToFileSearchStore` API को दिखाती है. इसमें *File storage* को बायपास किया जाता है.
इसके अलावा, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल करके, फ़ाइलों को अलग से बनाने और फिर इंपोर्ट करने से, इंडेक्सिंग की प्रोसेस *दस्तावेज़* से *फ़ाइल स्टोरेज* और फिर *एम्बेडिंग मॉडल* पर चली जाती है.

## फ़ाइल खोजने की सुविधा देने वाले ऐप्लिकेशन

फ़ाइल खोजने की सुविधा वाला स्टोर, आपके दस्तावेज़ों के एम्बेड किए गए वर्शन के लिए कंटेनर होता है. File API के ज़रिए अपलोड की गई रॉ फ़ाइलें, 48 घंटे बाद मिट जाती हैं. हालांकि, फ़ाइल सर्च स्टोर में इंपोर्ट किया गया डेटा तब तक सेव रहता है, जब तक उसे मैन्युअल तरीके से नहीं मिटाया जाता. अपने दस्तावेज़ों को व्यवस्थित करने के लिए, एक से ज़्यादा फ़ाइल खोज स्टोर बनाए जा सकते हैं. `FileSearchStore` एपीआई की मदद से, फ़ाइल खोज स्टोर को मैनेज करने के लिए, फ़ाइल खोज स्टोर बनाए जा सकते हैं, उनकी सूची बनाई जा सकती है, उन्हें पाया जा सकता है, और उन्हें मिटाया जा सकता है. फ़ाइल खोज में स्टोर के नाम, दुनिया भर में उपलब्ध होते हैं.

यहां फ़ाइल खोज की सुविधा वाले स्टोर मैनेज करने के कुछ उदाहरण दिए गए हैं:

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

## फ़ाइल खोज से जुड़े दस्तावेज़

[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=hi) API की मदद से, फ़ाइल स्टोर में मौजूद अलग-अलग दस्तावेज़ों को मैनेज किया जा सकता है. इससे फ़ाइल सर्च स्टोर में मौजूद `list` हर दस्तावेज़, `get` किसी दस्तावेज़ के बारे में जानकारी, और नाम के हिसाब से `delete` कोई दस्तावेज़ ढूंढा जा सकता है.

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

## फ़ाइल का मेटाडेटा

फ़ाइलों को फ़िल्टर करने या उनके बारे में ज़्यादा जानकारी देने के लिए, उनमें कस्टम मेटाडेटा जोड़ा जा सकता है. मेटाडेटा, की-वैल्यू पेयर का एक सेट होता है.

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

यह तब काम आता है, जब आपके पास फ़ाइल खोजने की सुविधा वाले स्टोर में कई दस्तावेज़ हों और आपको उनमें से सिर्फ़ कुछ दस्तावेज़ों को खोजना हो.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${GEMINI_API_KEY}" \
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

`metadata_filter` के लिए, सूची फ़िल्टर सिंटैक्स लागू करने के बारे में दिशा-निर्देश यहां दिए गए हैं: [google.aip.dev/160](https://google.aip.dev/160)

## मल्टीमॉडल फ़ाइल खोजने की सुविधा

मल्टीमॉडल फ़ाइल सर्च की सुविधा की मदद से, इमेज को नेटिव तौर पर एम्बेड किया जा सकता है और उनमें खोज की जा सकती है. इससे मल्टीमॉडल RAG ऐप्लिकेशन को बेहतर बनाया जा सकता है.

### एम्बेडिंग मॉडल को कॉन्फ़िगर करना

`FileSearchStore` बनाते समय, आपको टेक्स्ट-ओनली एम्बेडिंग मॉडल के डिफ़ॉल्ट मॉडल को बदलकर, मल्टीमॉडल मॉडल का इस्तेमाल करना होगा. टेक्स्ट और इमेज, दोनों को प्रोसेस करने के लिए `models/gemini-embedding-2` का इस्तेमाल करें.

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

### इमेज अपलोड करें

मल्टीमॉडल एम्बेडिंग मॉडल का इस्तेमाल करके स्टोर बनाने के बाद, इमेज फ़ाइलें सीधे तौर पर अपलोड की जा सकती हैं. इसके लिए, [फ़ाइल खोज के लिए बनाए गए स्टोर में सीधे तौर पर अपलोड करना](#upload) या [फ़ाइलें इंपोर्ट करना](#importing-files) में बताए गए अपलोड एपीआई का इस्तेमाल करें.

**इमेज फ़ाइल के लिए ज़रूरी शर्तें:**

- इमेज फ़ाइलों का रिज़ॉल्यूशन 4K x 4K पिक्सल से ज़्यादा नहीं होना चाहिए.
- इन फ़ॉर्मैट का इस्तेमाल किया जा सकता है: PNG, JPEG.

## उद्धरण

फ़ाइल खोज की सुविधा का इस्तेमाल करने पर, मॉडल के जवाब में उद्धरण शामिल हो सकते हैं. इनमें यह जानकारी होती है कि जवाब जनरेट करने के लिए, अपलोड किए गए दस्तावेज़ों के किन हिस्सों का इस्तेमाल किया गया था. इससे तथ्यों की जांच करने और पुष्टि करने में मदद मिलती है.

जवाब के `grounding_metadata` एट्रिब्यूट के ज़रिए, उद्धरण की जानकारी ऐक्सेस की जा सकती है.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

ग्राउंडिंग मेटाडेटा के स्ट्रक्चर के बारे में ज़्यादा जानकारी के लिए, [फ़ाइल खोजने से जुड़ी कुकबुक](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) में दिए गए उदाहरण देखें. इसके अलावा, ['Google Search की मदद से ग्राउंडिंग' दस्तावेज़ के ग्राउंडिंग सेक्शन](https://ai.google.dev/gemini-api/docs/google-search?hl=hi#attributing_sources_with_inline_citations) में भी उदाहरण देखे जा सकते हैं.

### पेज नंबर

पेज वाले दस्तावेज़ों (जैसे कि PDF) में फ़ाइल खोजने की सुविधा का इस्तेमाल करने पर, मॉडल के जवाब में उस पेज का नंबर शामिल हो सकता है जहां जानकारी मिली थी.
इस जानकारी को `retrieved_context` के `page_number` एट्रिब्यूट के ज़रिए ऐक्सेस किया जा सकता है.

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

### मीडिया साइटेशन

जब मॉडल, जनरेट करने के दौरान किसी इमेज चंक का रेफ़रंस देता है, तो एपीआई, ग्राउंडिंग मेटाडेटा में एक उद्धरण दिखाता है. इसमें `media_id` शामिल होता है. इस आईडी का इस्तेमाल करके, इमेज का वह हिस्सा डाउनलोड किया जा सकता है जिसे मॉडल ने रेफ़र किया है. यह `media_id` कई खोज कॉल में बना रहता है. इससे आपको एक ही इमेज को भरोसेमंद तरीके से वापस पाने या आईडी का इस्तेमाल करके उसे कैश मेमोरी में सेव करने में मदद मिलती है.

यहां REST रिस्पॉन्स का एक उदाहरण दिया गया है:

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

यहां दिए गए कोड स्निपेट में, `media_id` को वापस पाने और मीडिया को डाउनलोड करने का तरीका बताया गया है:

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

## ग्राउंडिंग डेटा में कस्टम मेटाडेटा

अगर आपने अपनी फ़ाइलों में कस्टम मेटाडेटा जोड़ा है, तो मॉडल के जवाब के ग्राउंडिंग मेटाडेटा में इसे ऐक्सेस किया जा सकता है. यह आपके सोर्स दस्तावेज़ों से, ऐप्लिकेशन लॉजिक में अतिरिक्त कॉन्टेक्स्ट (जैसे कि यूआरएल, पेज नंबर या लेखक) पास करने के लिए काम का होता है. `retrieved_context` में मौजूद हर `grounding_chunk` में यह कस्टम मेटाडेटा शामिल होता है.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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

## स्ट्रक्चर्ड आउटपुट

Gemini 3 मॉडल से शुरू करके, फ़ाइल खोजने वाले टूल को [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) के साथ इस्तेमाल किया जा सकता है.

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## इन मॉडल के साथ काम करता है

फ़ाइल खोजने की सुविधा के साथ ये मॉडल काम करते हैं:

| मॉडल | फ़ाइल खोजने की सुविधा |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## इस्तेमाल किए जा सकने वाले टूल कॉम्बिनेशन

Gemini 3 मॉडल, बिल्ट-इन टूल (जैसे, फ़ाइल खोजने की सुविधा) को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ इस्तेमाल करने की सुविधा देते हैं. [टूल के कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर ज़्यादा जानें.

## इस्तेमाल किए जा सकने वाले फ़ाइल टाइप

फ़ाइल खोजने की सुविधा, अलग-अलग तरह की फ़ाइलों के साथ काम करती है. इनकी जानकारी यहां दी गई है.

### ऐप्लिकेशन फ़ाइल के टाइप

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

### टेक्स्ट फ़ाइल के टाइप

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

## सीमाएं

- **Live API:** फ़ाइल खोजने की सुविधा, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) में मौजूद नहीं है.
- **टूल के साथ काम न करना:** फ़ाइल खोजने की सुविधा को फ़िलहाल, [Google Search से मिली जानकारी के आधार पर जवाब देने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), [यूआरएल के कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) वगैरह जैसे अन्य टूल के साथ इस्तेमाल नहीं किया जा सकता.

### अनुरोधों की संख्या की सीमाएं

सेवा को बेहतर तरीके से उपलब्ध कराने के लिए, File Search API पर ये सीमाएं लागू होती हैं:

- **फ़ाइल का ज़्यादा से ज़्यादा साइज़ / हर दस्तावेज़ के लिए तय सीमा**: 100 एमबी
- **प्रोजेक्ट फ़ाइल खोज के लिए इस्तेमाल किए जाने वाले स्टोरेज का कुल साइज़** (उपयोगकर्ता के टियर के आधार पर):
  - **मुफ़्त**: 1 जीबी
  - **टियर 1**: 10 जीबी
  - **दूसरा टियर**: 100 जीबी
  - **तीसरा टियर**: 1 टीबी
- **सुझाव**: हर फ़ाइल खोज स्टोर का साइज़ 20 जीबी से कम रखें, ताकि डेटा को तेज़ी से वापस पाया जा सके.

## कीमत

- इंडेक्सिंग के समय, आपसे एम्बेडिंग के लिए शुल्क लिया जाता है. यह शुल्क, [एम्बेडिंग की मौजूदा कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#gemini-embedding-2) के हिसाब से लिया जाता है.
- स्टोरेज की सुविधा बिना किसी शुल्क के उपलब्ध है.
- क्वेरी टाइम एम्बेडिंग की सुविधा बिना किसी शुल्क के उपलब्ध है.
- फ़ेच किए गए दस्तावेज़ टोकन के लिए, सामान्य [कॉन्टेक्स्ट टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) के तौर पर शुल्क लिया जाता है.

## आगे क्या करना है

- [फ़ाइल खोजने की सुविधा देने वाले स्टोर](https://ai.google.dev/api/file-search/file-search-stores?hl=hi) और फ़ाइल खोजने की सुविधा देने वाले [दस्तावेज़ों](https://ai.google.dev/api/file-search/documents?hl=hi) के लिए, एपीआई रेफ़रंस पर जाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-01 (UTC) को अपडेट किया गया."],[],[]]
