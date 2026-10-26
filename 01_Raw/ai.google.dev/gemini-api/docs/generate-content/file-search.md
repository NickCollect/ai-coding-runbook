---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=fa
fetched_at: 2026-10-26T05:47:36.915728+00:00
title: "\u062c\u0633\u062a\u062c\u0648\u06cc \u0641\u0627\u06cc\u0644 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# جستجوی فایل

«میانای برنامه‌سازی کاربردی Gemini» ازطریق ابزار «جستجوی فایل»، «تولید با کمک بازیابی» ("RAG") را فعال می‌کند. «جستجوی فایل» داده‌های شما را وارد، دسته‌بندی، و نمایه‌گذاری می‌کند تا براساس پیام‌واره ارائه‌شده، بازیابی سریع اطلاعات مرتبط را امکان‌پذیر کند. این اطلاعات بازیابی‌شده سپس به‌عنوان زمینه برای مدل استفاده می‌شود و به آن امکان می‌دهد پاسخ‌های دقیق‌تر و مرتبط‌تری ارائه دهد. جستجوی فایل همچنین می‌تواند قابلیت‌های چندحالته را با جاسازی‌های نوشتاری پشتیبانی‌شده توسط `gemini-embedding-001` و جاسازی تصویری/چندحالته پشتیبانی‌شده توسط `gemini-embedding-2` ارائه دهد.

ذخیره‌سازی فایل و تولید جاسازی در زمان پُرسمان رایگان است و فقط برای ایجاد جاسازی‌ها هنگام نمایه‌سازی اولیه فایل‌ها و هزینه معمولی توکن‌های ورودی / خروجی مدل Gemini پرداخت خواهید کرد. این الگوی جدید صورت‌حساب باعث می‌شود که ساختن و مقیاس‌بندی با «ابزار جستجوی فایل» هم آسان‌تر و هم مقرون‌به‌صرفه‌تر شود. برای جزئیات، بخش
[قیمت‌گذاری](#pricing) را ببینید.

## مستقیماً در فروشگاه «جستجوی فایل» بارگذاری کنید

این مثال نشان می‌دهد که چگونه می‌توان فایلی را مستقیماً در [فضای ذخیره‌سازی جستجوی فایل](https://ai.google.dev/api/file-search/file-search-stores?hl=fa#method:-media.uploadtofilesearchstore) بارگذاری کرد:

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

برای اطلاعات بیشتر، مرجع میانای برنامه‌سازی کاربردی برای [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=fa#method:-media.uploadtofilesearchstore) را بررسی کنید.

## درحال وارد کردن فایل‌ها

یا می‌توانید فایل موجودی را بارگذاری کنید و [آن را به فروشگاه جستجوی فایل خود وارد کنید](https://ai.google.dev/api/file-search/file-search-stores?hl=fa#method:-filesearchstores.importfile):

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

برای اطلاعات بیشتر، مرجع میانای برنامه‌سازی کاربردی برای [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=fa#method:-filesearchstores.importfile) را بررسی کنید.

## پیکربندی تکه‌تکه کردن

وقتی فایلی را به فروشگاه «جستجوی فایل» وارد می‌کنید، به‌طور خودکار به
تکه‌هایی تقسیم می‌شود، جاسازی می‌شود، نمایه‌گذاری می‌شود، و در فروشگاه «جستجوی فایل» شما بارگذاری می‌شود. اگر
به کنترل بیشتری بر استراتژی تکه‌تکه کردن نیاز دارید، می‌توانید تنظیم
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=fa#request-body_5) را
برای تعیین حداکثر تعداد داده‌واحد در هر تکه و حداکثر تعداد داده‌واحدهای هم‌پوشان
مشخص کنید.

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

برای استفاده از فضای ذخیره‌سازی «جستجوی فایل»، آن را به‌عنوان ابزار به روش `generateContent` ارسال کنید، همان‌طور که در مثال‌های [بارگذاری](#upload) و [وارد کردن](#importing-files) نشان داده شده است.

## روش کار

«جستجوی فایل» از تکنیکی به‌نام جستجوی معنایی برای پیدا کردن اطلاعات مرتبط با پیام‌واره کاربر استفاده می‌کند. برخلاف جستجوی استاندارد براساس کلیدواژه، جستجوی معنایی
معنی و بافت پُرسمان شما را درک می‌کند.

وقتی فایلی را وارد می‌کنید، به نمایش‌های عددی به نام
[جاسازی‌ها](https://ai.google.dev/gemini-api/docs/embeddings?hl=fa) تبدیل می‌شود که معنای معنایی
محتوای بارگذاری‌شده را ثبت می‌کند. این جاسازی‌ها در پایگاه داده تخصصی «جستجوی فایل» ذخیره می‌شوند.
وقتی پُرسمانی ایجاد می‌کنید، آن پُرسمان نیز به جاسازی تبدیل می‌شود. سپس سیستم
«جستجوی فایل» را اجرا می‌کند تا مشابه‌ترین و مرتبط‌ترین بخش‌های سند را
از فروشگاه «جستجوی فایل» پیدا کند.

هیچ «زمان بقایی» (TTL) برای جاسازی‌ها وجود ندارد؛
آن‌ها تا زمانی که به‌صورت دستی حذف شوند یا مدل منسوخ شود، باقی می‌مانند. اما فایل‌ها
پس‌از ۴۸ ساعت حذف می‌شوند.

در اینجا تفکیک فرایند استفاده از «میانای برنامه‌سازی کاربردی جستجوی فایل»
`uploadToFileSearchStore` آمده است:

1. **ایجاد فروشگاه «جستجوی فایل»:** فروشگاه «جستجوی فایل» حاوی داده‌های پردازش‌شده
   از فایل‌های شما است. این محتوی پایدار برای جاسازی‌هایی است که جستجوی معنایی روی آن‌ها عمل خواهد کرد.
2. **بارگذاری فایل و وارد کردن در فروشگاه «جستجوی فایل»**: به‌طور هم‌زمان فایلی را بارگذاری کنید و نتایج را در فروشگاه «جستجوی فایل» وارد کنید. این کار یک
   شیء `File` موقت ایجاد می‌کند که مرجعی برای سند خام شما است. سپس آن داده‌ها
   تکه‌تکه می‌شود، به جاسازی‌های «جستجوی فایل» تبدیل می‌شود، و نمایه می‌شود. شیء `File`
   پس‌از ۴۸ ساعت حذف می‌شود، درحالی‌که داده‌های واردشده به مخزن «جستجوی فایل»
   تا زمانی که خودتان آن‌ها را حذف نکنید به‌طور نامحدود ذخیره خواهند شد.
3. **پرس‌وجو با «جستجوی فایل»**: درنهایت، از ابزار `FileSearch` در تماس `generateContent` استفاده می‌کنید. در پیکربندی ابزار، `FileSearchRetrievalResource` را مشخص می‌کنید که به `FileSearchStore` موردنظر برای جستجو اشاره می‌کند. این دستور به مدل می‌گوید که در آن فروشگاه «جستجوی فایل» خاص، جستجوی معنایی انجام دهد تا اطلاعات مربوطه را برای پاسخ خود پیدا کند.

![فرایند فهرست‌بندی و پُرسمان «جستجوی فایل»](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=fa)

فرایند نمایه‌سازی و پرسمان «جستجوی فایل»

در این نمودار، خط‌چین از *اسناد* به *مدل جاسازی*
(بااستفاده از [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=fa))
نشان‌دهنده میانای برنامه‌سازی کاربردی `uploadToFileSearchStore` است (با دور زدن *فضای ذخیره‌سازی فایل*).
درغیراین‌صورت، استفاده از [Files API](https://ai.google.dev/gemini-api/docs/files?hl=fa) برای ایجاد جداگانه
و سپس وارد کردن فایل‌ها، فرایند نمایه‌سازی را از *اسناد* به
*فضای ذخیره‌سازی فایل* و سپس به *مدل جاسازی* منتقل می‌کند.

## فروشگاه‌های «جستجوی فایل»

فروشگاه «جستجوی فایل» محفظه‌ای برای جاسازی‌های سند شما است. درحالی‌که فایل‌های خام
بارگذاری‌شده ازطریق File API پس‌از ۴۸ ساعت حذف می‌شوند، داده‌های واردشده به
فروشگاه «جستجوی فایل» به‌طور نامحدود ذخیره می‌شوند تا زمانی‌که آن‌ها را به‌صورت دستی حذف کنید. می‌توانید
چند فروشگاه «جستجوی فایل» برای سازمان‌دهی اسنادتان ایجاد کنید. میانای برنامه‌سازی کاربردی
`FileSearchStore` به شما امکان می‌دهد برای مدیریت فروشگاه‌های جستجوی فایل، ایجاد، فهرست کردن، دریافت، و حذف کنید. نام‌های فروشگاه «جستجوی فایل» دارای دامنه جهانی هستند.

در اینجا چند نمونه از نحوه مدیریت فروشگاه‌های «جستجوی فایل» آورده شده است:

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

### استراحت

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## اسناد جستجوی فایل

بااستفاده از
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=fa) API می‌توانید سندهای جداگانه را در فروشگاه‌های فایل مدیریت کنید تا هر سند را در فروشگاه جستجوی فایل `list` کنید،
اطلاعات مربوط به سند را `get` کنید، و سند را براساس نام `delete` کنید.

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

## فراداده‌های فایل

می‌توانید فراداده سفارشی به فایل‌هایتان اضافه کنید تا به فیلتر کردن آن‌ها کمک کنید یا
بافت بیشتری ارائه دهید. فراداده مجموعه‌ای از جفت‌های کلید-مقدار است.

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

این ویژگی زمانی مفید است که چندین سند در فروشگاه «جستجوی فایل» داشته باشید و بخواهید
فقط زیرمجموعه‌ای از آن‌ها را جستجو کنید.

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

### استراحت

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

راهنمای پیاده‌سازی نحو فیلتر فهرست برای `metadata_filter` را می‌توانید در
[google.aip.dev/160](https://google.aip.dev/160) پیدا کنید

## جستجوی چندحالته فایل

«جستجوی فایل چندحالتی» به شما امکان می‌دهد تصاویر را به‌طور بومی جاسازی و جستجو کنید،
و برنامه‌های RAG چندحالتی غنی را فعال کنید.

### پیکربندی مدل جاسازی

وقتی `FileSearchStore` ایجاد می‌کنید، باید مدل جاسازی فقط نوشتاری پیش‌فرض را ملغی کنید تا از مدل چندحالته استفاده کنید. از `models/gemini-embedding-2` برای پردازش نوشتار و تصویر استفاده کنید.

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

### بارگذاری کردن تصویرها

پس‌از ایجاد فروشگاه با مدل جاسازی چندحالتی، می‌توانید فایل‌های تصویری را مستقیماً بااستفاده از همان میاناهای برنامه‌سازی کاربردی بارگذاری که در [بارگذاری مستقیم در فروشگاه «جستجوی فایل»](#upload) یا [وارد کردن فایل‌ها](#importing-files) شرح داده شده است بارگذاری کنید.

**الزامات فایل تصویر:**

- وضوح فایل‌های تصویر باید حداکثر ۴K x ۴K پیکسل باشد.
- قالب‌های پشتیبانی‌شده عبارت‌اند از PNG،‏ JPEG.

## نقل‌قول‌ها

وقتی از «جستجوی فایل» استفاده می‌کنید، پاسخ مدل ممکن است شامل استنادهایی باشد که مشخص می‌کند از کدام بخش‌های اسناد بارگذاری‌شده شما برای تولید پاسخ استفاده شده است. این کار به درستی‌سنجی و تأیید کمک می‌کند.

می‌توانید ازطریق ویژگی `grounding_metadata` در پاسخ به اطلاعات ارجاع دسترسی پیدا کنید.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

برای اطلاعات دقیق درباره ساختار فراداده پایه‌سازی،
نمونه‌های موجود در [کتاب راهنمای
جستجوی فایل](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb)
یا [بخش پایه‌سازی در اسناد
«پایه‌سازی با جستجوی Google»](https://ai.google.dev/gemini-api/docs/google-search?hl=fa#attributing_sources_with_inline_citations)
را ببینید.

### شماره صفحه

وقتی از «جستجوی فایل» با اسنادی که صفحه دارند (مثل PDF) استفاده می‌کنید، پاسخ مدل ممکن است شامل شماره صفحه‌ای باشد که اطلاعات در آن پیدا شده است.
می‌توانید ازطریق مشخصه `page_number` در
`retrieved_context` به این اطلاعات دسترسی پیدا کنید.

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

### نقل‌قول‌های رسانه‌ای

وقتی مدل درطول تولید به یک قطعه تصویر ارجاع می‌دهد، API یک
استناد در فراداده‌های زمینه‌سازی برمی‌گرداند که شامل `media_id` است. می‌توانید از این
شناسه برای بارگیری کردن تکه تصویر دقیقی که مدل به آن ارجاع داده است استفاده کنید. این `media_id` در چندین فراخوانی جستجو ماندگار است، که به شما امکان می‌دهد
تصویر یکسان را به‌طور قابل‌اعتمادی بازیابی کنید یا آن را بااستفاده از شناسه در حافظه نهان ذخیره کنید.

قطعه زیر نمونه‌ای از پاسخ REST است:

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

تکه‌کدهای زیر نحوه بازیابی `media_id` و
بارگیری رسانه را نشان می‌دهند:

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

### استراحت

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## فراداده سفارشی در داده‌های زمینه‌ای

اگر فراداده سفارشی به فایل‌هایتان اضافه کرده باشید، می‌توانید در فراداده زمینه‌سازی پاسخ مدل به آن دسترسی پیدا کنید. این کار برای انتقال بافت اضافی (مانند نشانی‌های وب، شماره صفحات، یا نویسندگان) از اسناد منبع به منطق برنامه شما مفید است. هر `grounding_chunk` در
`retrieved_context` حاوی این فراداده سفارشی است.

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

### استراحت

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

## برونداد ساختاریافته

با شروع از مدل‌های Gemini 3، می‌توانید ابزار جستجوی فایل را با
[بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa) ترکیب کنید.

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
                response_mime_type="application/json",
                response_json_schema=Money.model_json_schema()
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
          "mimeType": "APPLICATION_JSON",
          "schema": {
            "type": "object",
            "properties": {
              "amount": {"type": "string", "description": "The numerical part of the amount."},
              "currency": {"type": "string", "description": "The currency of amount."}
            },
            "required": ["amount", "currency"]
          }
        }
      }
    }
  }'
```

## مدل‌های پشتیبانی‌شده

مدل‌های زیر از «جستجوی فایل» پشتیبانی می‌کنند:

| مدل | جستجوی فایل |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fa) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fa) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fa) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fa) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fa) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fa) | ✔️ |

## ترکیب‌های ابزار پشتیبانی‌شده

مدل‌های Gemini 4 و Gemini 3 از ترکیب ابزارهای داخلی (مانند «جستجوی فایل») با ابزارهای سفارشی (فراخوانی تابع) پشتیبانی می‌کنند. در صفحه
[ترکیب‌های ابزار](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) بیشتر بدانید.

## انواع فایل‌های پشتیبانی‌شده

«جستجوی فایل» از طیف وسیعی از قالب‌های فایل پشتیبانی می‌کند که در بخش‌های زیر فهرست شده‌اند.

### انواع فایل برنامه

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

### انواع فایل نوشتاری

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

## محدودیت‌ها

- **Live API:** «جستجوی فایل» در
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=fa) پشتیبانی نمی‌شود.
- **عدم سازگاری ابزار:** «جستجوی فایل» درحال‌حاضر نمی‌تواند با ابزارهای دیگر
  مثل [زمینه‌سازی با «جستجوی Google»](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)،
  [زمینه نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)، و غیره ترکیب شود.

### محدودیت‌های نرخ

«میانای برنامه‌سازی کاربردی جستجوی فایل» برای اعمال پایداری سرویس محدودیت‌های زیر را دارد:

- **حداکثر اندازه فایل / حد مجاز برای هر سند**: ۱۰۰ مگابایت
- **اندازه کل فروشگاه‌های «جستجوی فایل» پروژه** (براساس سطح کاربر):
  - **رایگان**: ۱ گیگابایت
  - **سطح ۱**: ۱۰ گیگابایت
  - **سطح ۲**: ۱۰۰ گیگابایت
  - **سطح ۳**: ۱ ترابایت
- **توصیه**: برای اطمینان از تأخیرهای بهینه بازیابی، اندازه هر فروشگاه «جستجوی فایل» را به کمتر از ۲۰ گیگابایت محدود کنید.

## قیمت‌گذاری

- هزینه جاسازی‌ها در زمان نمایه‌گذاری براساس
  [قیمت‌گذاری جاسازی](https://ai.google.dev/gemini-api/docs/pricing?hl=fa#gemini-embedding-2) موجود از شما کسر می‌شود.
- فضای ذخیره‌سازی رایگان است.
- جاسازی‌های زمان پُرسمان رایگان است.
- هزینه داده‌واحدهای بازیابی‌شده سند مانند
  [داده‌واحدهای بافتی](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) معمولی محاسبه می‌شود.

## قدم بعدی چیست

- به مرجع میانای برنامه‌سازی کاربردی برای [فروشگاه‌های جستجوی فایل](https://ai.google.dev/api/file-search/file-search-stores?hl=fa) و [اسناد](https://ai.google.dev/api/file-search/documents?hl=fa) جستجوی فایل مراجعه کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-19 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-19 به‌وقت ساعت هماهنگ جهانی."],[],[]]
