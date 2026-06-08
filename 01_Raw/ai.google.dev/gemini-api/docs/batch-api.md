---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=ar
fetched_at: 2026-06-08T05:36:04.718503+00:00
title: "Batch API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Batch API

تم تصميم Gemini Batch API لمعالجة كميات كبيرة من الطلبات
بشكل غير متزامن بنسبة [% 50 من التكلفة العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).
يبلغ وقت الاستجابة المستهدَف 24 ساعة، ولكن في معظم الحالات، يكون أسرع بكثير.

استخدِم Batch API للمهام غير العاجلة على نطاق واسع، مثل المعالجة المسبقة للبيانات أو إجراء التقييمات التي لا تتطلّب استجابة فورية.

## إنشاء مهمة مجمّعة

تتوفّر طريقتان لإرسال طلباتك في Batch API:

- **[الطلبات المضمّنة](#inline-requests):** قائمة بعناصر
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=ar#GenerateContentRequest) مضمّنة مباشرةً في طلب إنشاء المجموعة. هذا مناسب للمجموعات الأصغر التي تحافظ على إجمالي حجم الطلب أقل من 20 ميغابايت. **الناتج** الذي يعرضه النموذج هو قائمة بعناصر `inlineResponse`.
- **[ملف الإدخال](#input-file):** ملف [JSON Lines (JSONL)](https://jsonlines.org/)
  يحتوي كل سطر فيه على عنصر
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=ar#GenerateContentRequest) كامل.
  ننصح باستخدام هذه الطريقة للطلبات الأكبر. **الناتج** الذي يعرضه النموذج هو ملف JSONL يكون كل سطر فيه إما `GenerateContentResponse` أو عنصر حالة.

### الطلبات المضمّنة

بالنسبة إلى عدد صغير من الطلبات، يمكنك تضمين عناصر
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=ar#GenerateContentRequest) مباشرةً في [`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=ar#request-body). يستدعي المثال التالي طريقة
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=ar#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
باستخدام طلبات مضمّنة:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### ملف الإدخال

بالنسبة إلى مجموعات الطلبات الأكبر، يمكنك إعداد ملف JSON Lines (JSONL). يجب أن يكون كل سطر في
هذا الملف عنصر JSON يحتوي على مفتاح يحدّده المستخدم وعنصر طلب، حيث يكون الطلب عنصر
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=ar#GenerateContentRequest) صالحًا. يتم استخدام المفتاح الذي يحدّده المستخدم في الردّ للإشارة إلى الناتج الذي يمثّل نتيجة الطلب. على سبيل المثال، سيتم وضع علامة على الردّ على الطلب الذي تم تحديد المفتاح له على أنّه `request-1` باستخدام اسم المفتاح نفسه.

يتم تحميل هذا الملف باستخدام [File API](https://ai.google.dev/gemini-api/docs/files?hl=ar). الحد الأقصى المسموح به لحجم ملف الإدخال هو 2 غيغابايت.

في ما يلي مثال على ملف JSONL. يمكنك حفظه في ملف باسم `my-batch-requests.json`:

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

على غرار الطلبات المضمّنة، يمكنك تحديد مَعلمات أخرى، مثل تعليمات النظام أو الأدوات أو الإعدادات الأخرى في كل طلب JSON.

يمكنك تحميل هذا الملف باستخدام [File API](https://ai.google.dev/gemini-api/docs/files?hl=ar) كما
هو موضّح في المثال التالي. إذا كنت تعمل على إدخال متعدد الوسائط، يمكنك الإشارة إلى ملفات أخرى تم تحميلها ضمن ملف JSONL.

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

يستدعي المثال التالي طريقة
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=ar#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
باستخدام ملف الإدخال الذي تم تحميله باستخدام File API:

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

عند إنشاء مهمة مجمّعة، سيتم عرض اسم المهمة. استخدِم هذا الاسم
لـ [تتبُّع](#batch-job-status) حالة المهمة واسترداد النتائج
[بعد اكتمالها](#retrieve-batch-results).

في ما يلي مثال على الناتج الذي يحتوي على اسم المهمة:

```
Created batch job from file: batches/123456789
```

### دعم التضمين المجمّع

يمكنك استخدام Batch API للتفاعل مع الـ
[Embeddings model](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar) من أجل زيادة معدّل النقل.
لإنشاء مهمة مجمّعة للتضمينات باستخدام [طلبات مضمّنة](#inline-requests)
أو [ملفات إدخال](#input-file)، استخدِم واجهة برمجة التطبيقات `batches.create_embeddings` وحدِّد نموذج التضمينات.

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

يمكنك الاطّلاع على قسم Embeddings في [Batch API cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)
لمزيد من الأمثلة.

### تهيئة الطلب

يمكنك تضمين أيّ إعدادات للطلب تستخدمها في طلب عادي غير مجمّع. على سبيل المثال، يمكنك تحديد درجة العشوائية أو تعليمات النظام أو حتى تمرير وسائط أخرى. يوضّح المثال التالي طلبًا مضمّنًا يحتوي على تعليمات النظام لأحد الطلبات:

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

يمكنك أيضًا تحديد الأدوات التي تريد استخدامها لطلب معيّن. يوضّح المثال التالي
طلبًا يفعِّل أداة [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar):

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

يمكنك أيضًا تحديد [ناتج منظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar).
يوضّح المثال التالي كيفية تحديد ذلك لطلباتك المجمّعة.

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

في ما يلي مثال على ناتج هذه المهمة:

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## تتبُّع حالة المهمة

استخدِم اسم العملية الذي تم الحصول عليه عند إنشاء المهمة المجمّعة لإجراء استطلاع حول حالتها.
سيشير حقل الحالة في المهمة المجمّعة إلى حالتها الحالية. يمكن أن تكون المهمة المجمّعة في إحدى الحالات التالية:

- `JOB_STATE_PENDING`: تم إنشاء المهمة وتنتظر أن تعالجها الخدمة.
- `JOB_STATE_RUNNING`: المهمة قيد التقدّم.
- `JOB_STATE_SUCCEEDED`: اكتملت المهمة بنجاح. يمكنك الآن استرداد النتائج.
- `JOB_STATE_FAILED`: تعذّر إكمال المهمة. يمكنك الاطّلاع على تفاصيل الخطأ لمزيد من المعلومات.
- `JOB_STATE_CANCELLED`: ألغاها المستخدم.
- `JOB_STATE_EXPIRED`: انتهت صلاحية المهمة لأنّها كانت قيد التشغيل أو في انتظار المراجعة لأكثر من 48 ساعة. لن تتضمّن المهمة أي نتائج لاستردادها.
  يمكنك محاولة إرسال المهمة مرة أخرى أو تقسيم الطلبات إلى مجموعات أصغر.

يمكنك إجراء استطلاع حول حالة المهمة بشكل دوري لمعرفة ما إذا اكتملت.

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### الاستطلاعات والويب هوك

**هل سئمت من إجراء الاستطلاعات؟** تتيح Gemini الآن استخدام
[Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=ar) لمعالجة عمليات الإكمال بشكل غير متزامن.
بدلاً من استدعاء `GET / operations` باستمرار، يمكنك الاشتراك في `batch.succeeded` مباشرةً للسماح لواجهة Gemini API بإرسال إشعارات في الوقت الفعلي إلى الخادم عند اكتمال العمليات غير المتزامنة أو الطويلة الأمد.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## استرداد النتائج

بعد أن تشير حالة المهمة إلى أنّ مهمتك المجمّعة قد اكتملت بنجاح، ستتوفّر النتائج في حقل `response`.

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## إدراج المهام المجمّعة

يمكنك إدراج مهامك المجمّعة الأخيرة.

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## إلغاء مهمة مجمّعة

يمكنك إلغاء مهمة مجمّعة قيد التقدّم باستخدام اسمها. عند إلغاء مهمة، تتوقّف معالجة الطلبات الجديدة.

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## حذف مهمة مجمّعة

يمكنك حذف مهمة مجمّعة حالية باستخدام اسمها. عند حذف مهمة، تتوقّف معالجة الطلبات الجديدة وتتم إزالتها من قائمة المهام المجمّعة.

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## إنشاء صور مجمّعة

إذا كنت تستخدم [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) وتحتاج إلى إنشاء الكثير
من الصور، يمكنك استخدام Batch API للحصول على حدود أعلى
[لمعدّل النقل](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar) مقابل وقت استجابة يصل
إلى 24 ساعة.

يمكنك استخدام [الطلبات المضمّنة](#inline-requests-images) للمجموعات الصغيرة من الطلبات (أقل من 20 ميغابايت) أو
[ملف إدخال JSONL](#input-file-images) للمجموعات الكبيرة (ننصح به لإنشاء الصور):

### الطلبات المضمّنة للصور

### Python

```
import time
import base64
import json
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create batch job with inline requests
inline_requests = [
    {
        'contents': [{'parts': [{'text': 'A big letter A surrounded by animals starting with the A letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    },
    {
        'contents': [{'parts': [{'text': 'A big letter B surrounded by animals starting with the B letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=inline_requests,
    config={
        'display_name': "inlined-image-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")

# 2. Monitor job status
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 3. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    print("Results are inline:")
    for i, inline_response in enumerate(batch_job.dest.inlined_responses):
        print(f"Response {i+1}:")
        if inline_response.response:
            for part in inline_response.response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.inline_data:
                    print(f"Image mime type: {part.inline_data.mime_type}")
                    image = part.as_image()
                    image.save(f"image_{i+1}.png")
        elif inline_response.error:
            print(f"Error: {inline_response.error}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create batch job with inline requests
    const inlinedRequests = [
        {
            contents: [{parts: [{text: 'A big letter A surrounded by animals starting with the A letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        },
        {
            contents: [{parts: [{text: 'A big letter B surrounded by animals starting with the B letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        }
    ]

    const inlineBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: inlinedRequests,
        config: {
            displayName: 'inlined-image-requests-job-1',
        }
    });

    console.log(inlineBatchJob);

    // 2. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: inlineBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${inlineBatchJob.name}:`, error);
        return;
    }

    // 3. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    for (const part of inlineResponse.response.candidates[0].content.parts) {
                        if (part.text) {
                            console.log(part.text);
                        } else if (part.inlineData) {
                            console.log(`Image mime type: ${part.inlineData.mimeType}`);
                        }
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No inline results found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### REST

```
# 1. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-image-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-1" }
                    },
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-2" }
                    }
                ]
            }
        }
    }
}'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 2. Poll job status until completion by repeating the following command
# Replace $BATCH_NAME with the name returned above.
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 3. If state is JOB_STATE_SUCCEEDED, retrieve results from batch_status.json
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    echo "Job succeeded. Results:"
    jq -r '.dest.inlinedResponses' batch_status.json
fi
```

### ملف الإدخال للصور

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## التفاصيل الفنية

- **النماذج المتوافقة:** تتيح Batch API استخدام مجموعة من نماذج Gemini.
  يمكنك الاطّلاع على [صفحة النماذج](https://ai.google.dev/gemini-api/docs/models?hl=ar) لمعرفة ما إذا كان كل نموذج يتيح استخدام Batch API. تتطابق الوسائط المتوافقة مع Batch API مع الوسائط المتوافقة مع واجهة برمجة التطبيقات التفاعلية (أو غير المجمّعة).
- **الأسعار:** يتم احتساب تكلفة استخدام Batch API بنسبة% 50 من التكلفة العادية لواجهة برمجة التطبيقات التفاعلية للنموذج المكافئ. يمكنك الاطّلاع على [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)
  لمعرفة التفاصيل. يمكنك الاطّلاع على [صفحة حدود معدّل النقل](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar#batch-mode)
  لمعرفة تفاصيل حدود معدّل النقل لهذه الميزة.
- **هدف مستوى الخدمة (SLO):** تم تصميم المهام المجمّعة بحيث تكتمل خلال 24 ساعة. قد تكتمل العديد من المهام بشكل أسرع بكثير حسب حجمها وحِمل النظام الحالي.
- **التخزين المؤقت:** [يتيح استخدام التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar) للطلبات المجمّعة. يمكنك إعادة استخدام المحتوى المخزّن مؤقتًا من خلال تحديد اسم مورد `cached_content` في إعدادات الطلبات الفردية ضمن المجموعة.
  إذا أدّى طلب في المجموعة إلى نتيجة ذاكرة التخزين المؤقت، ستدفع
  [المعدّلات العادية للتخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## أفضل الممارسات

- **استخدِم ملفات الإدخال للطلبات الكبيرة:** بالنسبة إلى عدد كبير من الطلبات،
  استخدِم دائمًا طريقة إدخال الملفات
  لتحسين إمكانية الإدارة وتجنُّب بلوغ حدود حجم الطلب لاستدعاء
  [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=ar#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
  نفسه. يُرجى العِلم أنّ الحد الأقصى لحجم الملف لكل ملف إدخال هو 2 غيغابايت.
- **التعامل مع الأخطاء:** بعد اكتمال المهمة، اطّلِع على `batchStats` لمعرفة `failedRequestCount`. في حال استخدام ناتج الملف، يمكنك تحليل كل سطر لمعرفة ما إذا كان `GenerateContentResponse` أو عنصر حالة يشير إلى خطأ في هذا الطلب المحدّد. يمكنك الاطّلاع على دليل [تحديد المشاكل
  وحلّها](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ar#error-codes) للحصول على مجموعة كاملة من
  رموز الخطأ.
- **إرسال المهام مرة واحدة:** لا يمكن تكرار عملية إنشاء مهمة مجمّعة.
  إذا أرسلت طلب الإنشاء نفسه مرّتين، سيتم إنشاء مهمتَين مجمّعتَين منفصلتَين.
- **تقسيم المجموعات الكبيرة جدًا:** على الرغم من أنّ وقت الاستجابة المستهدَف هو 24 ساعة، يمكن أن يختلف وقت المعالجة الفعلي استنادًا إلى حِمل النظام وحجم المهمة.
  بالنسبة إلى المهام الكبيرة، ننصحك بتقسيمها إلى مجموعات أصغر إذا كنت بحاجة إلى نتائج وسيطة في وقت أقرب.

## الخطوات التالية

- يمكنك الاطّلاع على دفتر ملاحظات [Batch API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=ar)
  لمزيد من الأمثلة.
- تتيح طبقة التوافق مع OpenAI استخدام Batch API. يمكنك قراءة الأمثلة في صفحة التوافق مع
  [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar#batch).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
