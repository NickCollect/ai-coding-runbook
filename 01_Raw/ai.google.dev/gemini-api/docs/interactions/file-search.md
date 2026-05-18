---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=he
fetched_at: 2026-05-18T05:19:29.164116+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# חיפוש קבצים

‫Gemini API מאפשר יצירה משולבת-אחזור (RAG) באמצעות הכלי File Search (חיפוש קבצים). האפליקציה 'חיפוש קבצים' מייבאת את הנתונים, מחלקת אותם לחלקים ויוצרת אינדקס שלהם כדי לאפשר שליפה מהירה של מידע רלוונטי על סמך הנחיה שסופקה. המידע הזה משמש כהקשר למודל, וכך הוא יכול לספק תשובות מדויקות ורלוונטיות יותר. חיפוש קבצים יכול גם לספק יכולות מולטי-מודאליות עם הטמעות טקסט שנתמכות על ידי `gemini-embedding-001`, והטמעות תמונות/מולטי-מודאליות שנתמכות על ידי `gemini-embedding-2`.

אחסון קבצים ויצירת הטמעה בזמן השאילתה הם בחינם, ותשלמו רק על יצירת הטמעות כשמבצעים אינדוקס לקבצים בפעם הראשונה, ועל העלות הרגילה של טוקנים של קלט / פלט במודל Gemini. הפרדיגמה החדשה הזו של חיוב מאפשרת לבנות את הכלי לחיפוש קבצים ולהרחיב אותו בקלות וביעילות מבחינת עלויות. פרטים נוספים מופיעים בקטע [תמחור](#pricing).

## העלאה ישירה למאגר חיפוש קבצים

בדוגמה הזו אפשר לראות איך מעלים קובץ ישירות אל [מאגר הקבצים לחיפוש](https://ai.google.dev/api/file-search/file-search-stores?hl=he#method:-media.uploadtofilesearchstore):

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

מידע נוסף זמין בהפניית ה-API בנושא [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=he#method:-media.uploadtofilesearchstore).

## ייבוא קבצים

אפשר גם להעלות קובץ קיים ו[לייבא אותו למאגר של חיפוש הקבצים](https://ai.google.dev/api/file-search/file-search-stores?hl=he#method:-filesearchstores.importfile):

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

מידע נוסף זמין בהפניית ה-API בנושא [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=he#method:-filesearchstores.importfile).

## הגדרות חלוקה לחלקים

כשמייבאים קובץ למאגר חיפוש קבצים, הוא מפורק אוטומטית לחלקים, מוטמע, עובר אינדוקס ועולה למאגר חיפוש הקבצים. אם אתם צריכים שליטה רבה יותר באסטרטגיית החלוקה לחלקים, אתם יכולים לציין הגדרה של [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=he#request-body_5) כדי להגדיר מספר מקסימלי של טוקנים לכל חלק ומספר מקסימלי של טוקנים חופפים.

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

כדי להשתמש בחנות File Search, מעבירים אותה ככלי לשיטה `interactions.create`, כמו בדוגמאות של [העלאה](#upload) ו[ייבוא](#importing-files).

## איך זה עובד

בחיפוש קבצים נעשה שימוש בטכניקה שנקראת חיפוש סמנטי כדי למצוא מידע שרלוונטי להנחיה של המשתמש. בניגוד לחיפוש רגיל שמבוסס על מילות מפתח, חיפוש סמנטי מבין את המשמעות וההקשר של השאילתה.

כשמייבאים קובץ, הוא מומר לייצוגים מספריים שנקראים [הטמעות](https://ai.google.dev/gemini-api/docs/embeddings?hl=he), שמשקפים את המשמעות הסמנטית של התוכן שהועלה. ההטמעות האלה מאוחסנות במסד נתונים ייעודי של חיפוש קבצים.
כשמבצעים שאילתה, היא מומרת גם להטמעה. לאחר מכן, המערכת מבצעת חיפוש בקובץ כדי למצוא את חלקי המסמך הדומים והרלוונטיים ביותר ממאגר החיפוש בקובץ.

אין אורך חיים (TTL) להטמעות. הן נשמרות עד למחיקה ידנית או עד שהמודל יוצא משימוש. אבל הקבצים נמחקים אחרי 48 שעות.

פירוט התהליך לשימוש ב-File Search
`uploadToFileSearchStore` API:

1. **יצירת מאגר חיפוש קבצים**: מאגר חיפוש קבצים מכיל את הנתונים המעובדים מהקבצים שלכם. זהו מאגר קבוע של ההטמעות שעליהן יפעל החיפוש הסמנטי.
2. **העלאת קובץ וייבוא שלו למאגר של חיפוש קבצים**: אפשר להעלות קובץ ולייבא את התוצאות שלו למאגר של חיפוש קבצים בו-זמנית. הפעולה הזו יוצרת אובייקט `File` זמני, שהוא הפניה למסמך הגולמי. הנתונים האלה מחולקים לחלקים, מומרים להטמעות של חיפוש קבצים ומתווספים לאינדקס. אובייקט `File`
   יימחק אחרי 48 שעות, אבל הנתונים שיובאו למאגר של חיפוש קבצים
   יישמרו ללא הגבלת זמן עד שתבחרו למחוק אותם.
3. **שאילתה עם חיפוש קבצים**: לבסוף, אתם משתמשים בכלי `FileSearch` בשיחה ב-`generateContent`. בהגדרת הכלי, מציינים `FileSearchRetrievalResource`, שמפנה אל `FileSearchStore` שרוצים לחפש. ההוראה הזו אומרת למודל לבצע חיפוש סמנטי במאגר הספציפי הזה של חיפושי קבצים כדי למצוא מידע רלוונטי שישמש כבסיס לתשובה.

![תהליך ההוספה לאינדקס והשאילתה בחיפוש הקבצים](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=he)

תהליך ההוספה לאינדקס והשאילתות בחיפוש הקבצים

בתרשים הזה, הקו המקווקו מ*מסמכים* אל *מודל הטמעה* (באמצעות [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=he)) מייצג את `uploadToFileSearchStore` API (דילוג על *אחסון קבצים*).
אחרת, שימוש ב-[Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=he) כדי ליצור בנפרד ואז לייבא קבצים מעביר את תהליך יצירת האינדקס מ*מסמכים* ל*אחסון קבצים* ואז ל*מודל הטמעה*.

## מאגרי חיפוש קבצים

מאגר חיפוש קבצים הוא מאגר להטמעות של המסמכים שלכם. קובצי RAW שהועלו דרך File API נמחקים אחרי 48 שעות, אבל הנתונים שיובאו למאגר של חיפוש קבצים נשמרים ללא הגבלת זמן עד שמבצעים מחיקה ידנית. אתם יכולים ליצור כמה מאגרי חיפוש קבצים כדי לארגן את המסמכים שלכם. ‫`FileSearchStore` API מאפשר לכם ליצור, לרשום, לקבל ולמחוק כדי לנהל את חנויות החיפוש של הקבצים. שמות מאגרי חיפוש קבצים הם בהיקף גלובלי.

הנה כמה דוגמאות לניהול מאגרי חיפוש קבצים:

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

## מסמכים בחיפוש קבצים

אפשר לנהל מסמכים ספציפיים במאגרי הקבצים באמצעות [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=he) API כדי `list` כל מסמך במאגר קבצים, `get` מידע על מסמך ו`delete` מסמך לפי שם.

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

## המטא-נתונים של הקבצים

אתם יכולים להוסיף מטא-נתונים מותאמים אישית לקבצים כדי לסנן אותם או לספק הקשר נוסף. מטא-נתונים הם קבוצה של צמדי מפתח/ערך.

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

האפשרות הזו שימושית אם יש לכם כמה מסמכים במאגר של חיפוש קבצים ואתם רוצים לחפש רק בחלק מהם.

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

הנחיות להטמעה של תחביר סינון רשימות ל-`metadata_filter` זמינות בכתובת [google.aip.dev/160](https://google.aip.dev/160)

## חיפוש קבצים מרובה מצבים

חיפוש קבצים מולטימודאלי מאפשר לכם להטמיע ולחפש תמונות באופן מקורי,
וכך ליצור אפליקציות RAG מולטימודאליות ועשירות.

### הגדרת מודל ההטמעה

כשיוצרים `FileSearchStore`, צריך להחליף את מודל ההטמעה שמוגדר כברירת מחדל (טקסט בלבד) במודל multi-modal. משתמשים ב-`models/gemini-embedding-2` כדי לעבד טקסט ותמונות.

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

### העלאת תמונות

אחרי שיוצרים את המאגר באמצעות מודל הטמעה רב-אופני, אפשר להעלות קובצי תמונות ישירות באמצעות אותם ממשקי API להעלאה שמתוארים במאמרים [העלאה ישירה למאגר של חיפוש קבצים](#upload) או [ייבוא קבצים](#importing-files).

**הדרישות לגבי קובץ תמונה:**

- קבצי התמונות צריכים להיות ברזולוציה של 4K x 4K פיקסלים לכל היותר.
- הפורמטים הנתמכים הם PNG ו-JPEG.

## ציטוטים ביבליוגרפיים

כשמשתמשים בחיפוש קבצים, התשובה של המודל עשויה לכלול ציטוטים שמציינים אילו חלקים מהמסמכים שהועלו שימשו ליצירת התשובה. המידע הזה עוזר בבדיקת עובדות ובאימות.

אפשר לגשת לפרטי הציטוט דרך המאפיין `annotations` בתוך בלוקי התגובה של שלב `model_output` `content`.

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

מידע מפורט על מבנה הציטוטים זמין במאמר [הפניית API עבור Interactions](https://ai.google.dev/api/interactions-api?hl=he#Resource:FileCitation).

### מספרי דפים

כשמשתמשים בחיפוש קבצים עם מסמכים שיש בהם דפים (כמו קובצי PDF), התשובה של המודל עשויה לכלול את מספר הדף שבו נמצא המידע.
אפשר לגשת למידע הזה דרך מאפיין `page_number` של הערה `file_citation`.

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

### ציטוטים של מדיה

כשהמודל מתייחס לחלק של תמונה במהלך היצירה, ה-API מחזיר הערה מהסוג `file_citation` בהערות שכוללת `media_id`. אפשר להשתמש במזהה הזה כדי להוריד את נתח התמונה המדויק שהמודל התייחס אליו. הערך `media_id` נשמר בכמה קריאות חיפוש, כך שאפשר לאחזר את אותה תמונה או לשמור אותה במטמון באמצעות המזהה.

קטע הקוד הבא הוא דוגמה לשלב של תגובת REST:

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

בדוגמאות הקוד הבאות אפשר לראות איך מאחזרים את `media_id` ומורידים את המדיה:

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

## מטא-נתונים בהתאמה אישית

אם הוספתם מטא-נתונים מותאמים אישית לקבצים, תוכלו לגשת אליהם בהערות של תשובת המודל. האפשרות הזו שימושית להעברת הקשר נוסף (כמו כתובות URL, מספרי דפים או מחברים) ממסמכי המקור ללוגיקה של האפליקציה. כל הערת ציטוט מסוג `file_citation`
מכילה את המטא-נתונים המותאמים אישית האלה.

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

## פלט מובנה

החל ממודלים של Gemini 3, אפשר לשלב את הכלי לחיפוש קבצים עם [פלט מובנה](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=he).

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

## מודלים נתמכים

המודלים הבאים תומכים בחיפוש קבצים:

| מודל | חיפוש קבצים |
| --- | --- |
| ‫[Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=he) | ✔️ |
| ‫[Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=he) | ✔️ |
| [תצוגה מקדימה של Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) | ✔️ |
| ‫[Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=he) | ✔️ |
| ‫[Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=he) | ✔️ |

## שילובים נתמכים של כלים

מודלים של Gemini 3 תומכים בשילוב של כלים מובנים (כמו חיפוש קבצים) עם כלים מותאמים אישית (קריאה לפונקציה). מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

## סוגי קבצים נתמכים

חיפוש הקבצים תומך במגוון רחב של פורמטים של קבצים, שמפורטים בקטעים הבאים.

### סוגי קבצים של אפליקציות

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

### סוגים של קובצי טקסט

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

## מגבלות

- **Live API:** חיפוש קבצים לא נתמך ב-[Live API](https://ai.google.dev/gemini-api/docs/live?hl=he).
- **אי-תאימות לכלי אחר:** אי אפשר לשלב את חיפוש הקבצים עם כלים אחרים
  כמו [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=he),‏ [הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=he) וכו' בשלב הזה.

### מגבלות קצב

כדי לשמור על יציבות השירות, יש מגבלות על File Search API:

- **גודל קובץ מקסימלי / מגבלה לכל מסמך**: 100MB
- **הגודל הכולל של מאגרי חיפוש הקבצים בפרויקט** (על סמך רמת המשתמש):
  - **בחינם**: 1GB
  - **רמה 1**: 10GB
  - **רמה 2**: 100GB
  - **רמה 3**: 1TB
- **המלצה**: כדי להבטיח חביון אופטימלי של אחזור נתונים, מומלץ להגביל את הגודל של כל מאגר של חיפוש קבצים ל-20GB.

## תמחור

- החיוב על הטמעות מתבצע בזמן היצירה של האינדקס, על סמך [תמחור ההטמעות](https://ai.google.dev/gemini-api/docs/pricing?hl=he#gemini-embedding-2) הקיים.
- האחסון הוא בחינם.
- הטמעות בזמן השאילתה הן בחינם.
- האסימונים של המסמך שאוחזר מחויבים בתור [אסימוני הקשר](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=he) רגילים.

## המאמרים הבאים

- אפשר לעיין ב[הפניית API](https://ai.google.dev/api/file-search/file-search-stores?hl=he) בנושא מאגרי חיפוש קבצים ו[מסמכים](https://ai.google.dev/api/file-search/documents?hl=he) של חיפוש קבצים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-12 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-12 (שעון UTC)."],[],[]]
