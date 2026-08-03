---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar
fetched_at: 2026-08-03T04:41:21.498945+00:00
title: "\u0637\u064f\u0631\u0642 \u0625\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0644\u0641\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# طُرق إدخال الملفات

يوضّح هذا الدليل الطرق المختلفة التي يمكنك من خلالها تضمين ملفات وسائط، مثل الصور والصوت والفيديو والمستندات، عند إرسال طلبات إلى Gemini API.
تتوفّر الطرق الجديدة في جميع نقاط نهاية Gemini API، بما في ذلك Batch وInteractions وLive API.
يعتمد اختيار الطريقة المناسبة على حجم ملفك ومكان تخزين بياناتك ومعدّل تكرار استخدامك للملف.

أبسط طريقة لتضمين ملف كمدخل هي قراءة ملف محلي وتضمينه في طلب. يوضّح المثال التالي كيفية قراءة ملف PDF محلي. يقتصر حجم ملفات PDF على 50 ميغابايت عند استخدام هذه الطريقة. راجِع [جدول مقارنة طرق الإدخال](#method-comparison) للحصول على قائمة كاملة بأنواع الملفات التي يمكن إدخالها والحدود القصوى المسموح بها.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## مقارنة طرق الإدخال

يقارن الجدول التالي بين كل طريقة إدخال من حيث حدود الملفات وحالات الاستخدام الأفضل. يُرجى العِلم أنّ الحدّ الأقصى المسموح به لحجم الملف قد يختلف حسب نوع الملف والنموذج أو أداة تقسيم النص المستخدَمة لمعالجة الملف.

| الطريقة | يناسب هذا الخيار: | الحجم الأقصى للملف | الاستمرارية |
| --- | --- | --- | --- |
| **البيانات المضمّنة** | اختبار سريع، وملفات صغيرة، وتطبيقات في الوقت الفعلي | ‫100 ميغابايت لكل طلب أو حمولة   (**50 ميغابايت لملفات PDF**) | بلا قيمة (يتم إرسالها مع كل طلب) |
| **تحميل الملفات من خلال واجهة برمجة التطبيقات** | الملفات الكبيرة والملفات المستخدَمة عدة مرات | ‫2 غيغابايت لكل ملف،   ما يصل إلى 20 غيغابايت لكل مشروع | ‫48 ساعة |
| **تسجيل معرّف الموارد المنتظم (URI) في File API على "خدمة التخزين السحابي من Google"** | الملفات الكبيرة المخزَّنة في Google Cloud Storage، والملفات المستخدَمة عدة مرات | ‫2 غيغابايت لكل ملف، بدون حدود إجمالية لمساحة التخزين | لا شيء (يتم استرجاعها لكل طلب). يمكن أن تتيح عملية التسجيل لمرة واحدة الوصول إلى التطبيق لمدة تصل إلى 30 يومًا. |
| **عناوين URL الخارجية** | البيانات العامة أو البيانات في حِزم السحابة الإلكترونية (AWS وAzure وGCS) بدون إعادة تحميلها | ‫100 ميغابايت لكل طلب/حمولة | لا شيء (يتم استرجاعها لكل طلب) |

## البيانات المضمّنة

بالنسبة إلى الملفات الأصغر حجمًا (أقل من 100 ميغابايت، أو 50 ميغابايت لملفات PDF)، يمكنك تمرير البيانات مباشرةً في حمولة الطلب. هذه هي الطريقة الأبسط لإجراء اختبارات سريعة أو للتطبيقات التي تعالج البيانات المؤقتة في الوقت الفعلي. يمكنك تقديم البيانات كسلاسل مشفّرة باستخدام base64 أو من خلال قراءة الملفات المحلية مباشرةً.

للاطّلاع على مثال على القراءة من ملف محلي، راجِع المثال في بداية هذه الصفحة.

### الجلب من عنوان URL

يمكنك أيضًا جلب ملف من عنوان URL وتحويله إلى وحدات بايت وتضمينه في الإدخال.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.6-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

تم تصميم File API للملفات الأكبر حجمًا (حتى 2 غيغابايت) أو الملفات التي تنوي استخدامها في طلبات متعددة.

### تحميل الملفات العادي

حمِّل ملفًا محليًا إلى Gemini API. يتم تخزين الملفات التي يتم تحميلها بهذه الطريقة بشكل مؤقت (لمدة 48 ساعة) ومعالجتها ليتمكّن النموذج من استرجاعها بكفاءة.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### تسجيل ملفات Google Cloud Storage

إذا كانت بياناتك متوفّرة في Google Cloud Storage، لن تحتاج إلى تنزيلها وإعادة تحميلها. يمكنك تسجيلها مباشرةً باستخدام File API.

1. منح **وكيل الخدمة** إذن الوصول إلى كل حزمة

   1. فعِّل Gemini API في مشروعك على Google Cloud.
   2. إنشاء وكيل الخدمة:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **امنح وكيل خدمة Gemini API الأذونات** اللازمة لقراءة حِزم التخزين.

      على المستخدم منح `Storage Object Viewer`
      [دور IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=ar#storage.objectViewer)
      لوكيل الخدمة هذا في حِزم التخزين المحدّدة التي ينوي استخدامها.

   لا تنتهي صلاحية هذا الإذن بالوصول تلقائيًا، ولكن يمكن تغييره في أي وقت. يمكنك أيضًا استخدام أوامر [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=ar) لمنح الأذونات.
2. مصادقة خدمتك

   **المتطلبات الأساسية**

   - تفعيل واجهة برمجة التطبيقات
   - أنشئ حساب خدمة أو وكيلًا لديه الأذونات المناسبة.

   عليك أولاً إجراء المصادقة بصفتك الخدمة التي لديها أذونات عارض عنصر التخزين. وتختلف طريقة فعل ذلك حسب البيئة التي سيتم فيها تشغيل رمز إدارة الملفات.

   **خارج Google Cloud**

   إذا كان الرمز البرمجي يعمل من خارج Google Cloud، مثلاً من سطح المكتب،
   نزِّل بيانات اعتماد الحساب من &quot;وحدة تحكّم Google Cloud&quot; باتّباع الخطوات التالية:

   1. انتقِل إلى [وحدة تحكّم حساب الخدمة](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ar)
   2. اختَر حساب الخدمة ذي الصلة
   3. اختَر علامة التبويب **المفاتيح**، ثم انقر على **إضافة مفتاح، إنشاء مفتاح جديد**.
   4. اختَر نوع المفتاح **JSON**، ودَوِّن المكان الذي تم تنزيل الملف فيه على جهازك.

   لمزيد من التفاصيل، يُرجى الاطّلاع على مستندات Google Cloud الرسمية حول [إدارة مفاتيح حسابات الخدمة](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=ar).

   بعد ذلك، استخدِم الأوامر التالية للمصادقة. تفترض هذه الأوامر أنّ ملف حساب الخدمة موجود في الدليل الحالي، ويحمل الاسم `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **على Google Cloud**

   إذا كنت تستخدم Google Cloud مباشرةً، مثلاً من خلال استخدام [وظائف Cloud Run](https://cloud.google.com/functions?hl=ar) أو [مثيل Compute Engine](https://cloud.google.com/products/compute?hl=ar)، ستتوفّر لك بيانات اعتماد ضمنية، ولكن عليك إعادة المصادقة لمنح النطاقات المناسبة.

   ### Python

   يفترض هذا الرمز البرمجي أنّ الخدمة تعمل في بيئة يمكن فيها الحصول على [بيانات الاعتماد التلقائية للتطبيق](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ar) تلقائيًا، مثل Cloud Run أو Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   يفترض هذا الرمز البرمجي أنّ الخدمة تعمل في بيئة يمكن فيها الحصول على [بيانات الاعتماد التلقائية للتطبيق](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ar) تلقائيًا، مثل Cloud Run أو Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   هذا أمر تفاعلي. بالنسبة إلى خدمات مثل Compute Engine، يمكنك ربط النطاقات بالخدمة قيد التشغيل على مستوى الإعدادات. راجِع [مستندات الخدمة التي يديرها المستخدم](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=ar#using) للحصول على مثال.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. تسجيل الملفات (Files API)

   استخدِم Files API لتسجيل الملفات وإنشاء مسار Files API يمكن استخدامه مباشرةً في Gemini API.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.6-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.6-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## عناوين URL الخارجية التي تستخدم HTTP أو عناوين URL الموقَّعة

يمكنك تمرير عناوين URL تستخدم HTTPS ومتاحة للجميع أو عناوين URL موقّعة مسبقًا مباشرةً في طلبك. ستجلب واجهة Gemini API المحتوى بشكل آمن أثناء المعالجة.
هذه الطريقة مثالية للملفات التي يصل حجمها إلى 100 ميغابايت والتي لا تريد إعادة تحميلها.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.6-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### تسهيل الاستخدام

تأكَّد من أنّ عناوين URL التي تقدّمها لا تؤدي إلى صفحات تتطلّب تسجيل الدخول أو
تستخدم حاجز الدفع. بالنسبة إلى قواعد البيانات الخاصة، تأكَّد من إنشاء عنوان URL موقَّع
مع أذونات الوصول وتاريخ انتهاء الصلاحية الصحيحَين.

### عمليات التحقّق من الأمان

يُجري النظام عملية التحقّق من الإشراف على المحتوى في عنوان URL للتأكّد من استيفائه لمعايير الأمان والسياسات. إذا لم يجتَز عنوان URL عملية التحقّق هذه، سيظهر لك
`url_retrieval_status` من `URL_RETRIEVAL_STATUS_UNSAFE`.

### أنواع المحتوى المتوافقة

هذه القائمة بأنواع الملفات المتوافقة والقيود هي إرشادات أولية وليست شاملة. يخضع نطاق أنواع البيانات المتوافقة للتغيير، ويمكن أن يختلف حسب الطراز المحدد وإصدار أداة تقسيم النص المستخدَمة. وستؤدي الأنواع غير المتوافقة إلى حدوث خطأ.
بالإضافة إلى ذلك، لا يمكن استرداد المحتوى لأنواع الملفات هذه إلا من خلال عناوين URL متاحة للجميع.

#### أنواع الملفات النصية

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### أنواع ملفات التطبيقات

- `application/json`
- `application/pdf`

#### أنواع ملفات الصور

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### أنواع ملفات الفيديو

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## أفضل الممارسات

- **اختيار الطريقة المناسبة:** استخدِم البيانات المضمّنة للملفات الصغيرة والمؤقتة.
  استخدِم File API للملفات الأكبر حجمًا أو الملفات المستخدَمة بشكل متكرّر. استخدِم عناوين URL خارجية
  للبيانات المستضافة على الإنترنت.
- **تحديد أنواع MIME:** احرص دائمًا على تقديم نوع MIME الصحيح لبيانات الملف لضمان معالجتها بشكل سليم.
- **معالجة الأخطاء:** نفِّذ إجراءات معالجة الأخطاء في الرمز البرمجي لإدارة المشاكل المحتملة، مثل الأعطال في الشبكة أو مشاكل الوصول إلى الملفات أو أخطاء واجهة برمجة التطبيقات.

## القيود

- تختلف حدود حجم الملف حسب الطريقة (راجِع [جدول المقارنة](#method-comparison)) ونوع الملف.
- تزيد البيانات المضمّنة من حجم حمولة الطلب.
- عمليات التحميل باستخدام File API مؤقتة وتنتهي صلاحيتها بعد 48 ساعة.
- يقتصر جلب عناوين URL الخارجية على 100 ميغابايت لكل حمولة، ويتوافق مع أنواع محتوى معيّنة.

## الخطوات التالية

- يمكنك تجربة كتابة طلبات متعددة الوسائط باستخدام
  [Google AI Studio](http://aistudio.google.com/?hl=ar).
- للحصول على معلومات حول تضمين الملفات في طلباتك، يُرجى الاطّلاع على أدلة
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=ar) و
  [الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar) و
  [معالجة المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
