---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar
fetched_at: 2026-05-18T05:13:07.388581+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# طُرق إدخال الملفات

يوضّح هذا الدليل الطرق المختلفة التي يمكنك من خلالها تضمين ملفات الوسائط، مثل الصور والصوت والفيديو والمستندات، عند إرسال طلبات إلى Gemini API.
تتوفّر الطرق الجديدة في جميع نقاط نهاية Gemini API، بما في ذلك
Batch وInteractions وLive API.
يعتمد اختيار الطريقة المناسبة على حجم ملفك ومكان تخزين بياناتك حاليًا ومدى تكرار استخدامك للملف.

أسهل طريقة لتضمين ملف كإدخال هي قراءة ملف محلي وتضمينه في طلب. يوضّح المثال التالي كيفية قراءة ملف PDF محلي. يقتصر حجم ملفات PDF على 50 ميغابايت في هذه الطريقة. للاطّلاع على قائمة كاملة بأنواع إدخال الملفات والحدود المفروضة عليها، راجِع جدول مقارنة طُرق الإدخال
.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## مقارنة طُرق الإدخال

يقارن الجدول التالي بين كل طريقة إدخال مع حدود الملفات وأفضل حالات الاستخدام. يُرجى العِلم أنّ الحدّ الأقصى لحجم الملف قد يختلف حسب نوع الملف والنموذج/أداة تقسيم الكلمات المستخدَمة لمعالجة الملف.

| الطريقة | الأفضل لـ | الحجم الأقصى للملف | الاستمرارية |
| --- | --- | --- | --- |
| **البيانات المضمّنة** | الاختبار السريع والملفات الصغيرة والتطبيقات في الوقت الفعلي | ‫100 ميغابايت لكل طلب/بيانات   (**50 ميغابايت لملفات PDF**) | لا شيء (يتم إرسالها مع كل طلب) |
| **تحميل الملفات باستخدام File API** | الملفات الكبيرة والملفات المستخدَمة عدة مرات | ‫2 غيغابايت لكل ملف،   ما يصل إلى 20 غيغابايت لكل مشروع | 48 ساعة |
| **تسجيل معرّف URI لـ Google Cloud Storage باستخدام File API** | الملفات الكبيرة المخزَّنة حاليًا في Google Cloud Storage والملفات المستخدَمة عدة مرات | ‫2 غيغابايت لكل ملف، بدون حدود إجمالية للتخزين | لا شيء (يتم استرجاعها لكل طلب). يمكن أن يمنح التسجيل لمرة واحدة إمكانية الوصول لمدة تصل إلى 30 يومًا. |
| **عناوين URL الخارجية** | البيانات العلنية أو البيانات في حِزم التخزين السحابي (AWS وAzure وGCS) بدون إعادة تحميلها | ‫100 ميغابايت لكل طلب/بيانات | لا شيء (يتم استرجاعها لكل طلب) |

## البيانات المضمّنة

بالنسبة إلى الملفات الأصغر حجمًا (أقل من 100 ميغابايت أو 50 ميغابايت لملفات PDF)، يمكنك تمرير البيانات مباشرةً في بيانات الطلب. هذه هي الطريقة الأسهل لإجراء اختبارات سريعة أو إنشاء تطبيقات تعالج البيانات المؤقتة في الوقت الفعلي. يمكنك تقديم البيانات كسلاسل base64 مشفّرة أو من خلال قراءة الملفات المحلية مباشرةً.

للاطّلاع على مثال لقراءة ملف محلي، راجِع المثال في بداية هذه الصفحة.

### استرجاع ملف من عنوان URL

يمكنك أيضًا استرجاع ملف من عنوان URL وتحويله إلى وحدات بايت وتضمينه في الإدخال.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: contents
    });
    console.log(response.text);
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

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## ‫Gemini File API

تم تصميم File API للملفات الأكبر حجمًا (ما يصل إلى 2 غيغابايت) أو الملفات التي تنوي استخدامها في طلبات متعددة.

### تحميل الملفات العادي

حمِّل ملفًا محليًا إلى Gemini API. يتم تخزين الملفات التي يتم تحميلها بهذه الطريقة مؤقتًا (48 ساعة) ومعالجتها لاسترجاعها بكفاءة من قِبل النموذج.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
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
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### تسجيل ملفات Google Cloud Storage

إذا كانت بياناتك مخزَّنة حاليًا في Google Cloud Storage، لن تحتاج إلى تنزيلها وإعادة تحميلها. يمكنك تسجيلها مباشرةً باستخدام File API.

1. منح إذن الوصول إلى **وكيل الخدمة** لكل حزمة

   1. فعِّل Gemini API في مشروعك على Google Cloud.
   2. أنشئ وكيل الخدمة:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **امنح وكيل خدمة Gemini API أذونات** قراءة حِزم التخزين.

      على المستخدم منح دور `Storage Object Viewer`
      [إدارة الهوية والوصول (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=ar#storage.objectViewer)
      لوكيل الخدمة هذا على حِزم التخزين المحدّدة التي ينوي استخدامها.

   لا تنتهي صلاحية إذن الوصول هذا تلقائيًا، ولكن يمكن تغييره في أي وقت. يمكنك
   أيضًا استخدام
   [أوامر Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=ar)
   لمنح الأذونات.
2. مصادقة خدمتك

   **المتطلبات الأساسية**

   - تفعيل واجهة برمجة التطبيقات
   - إنشاء حساب خدمة/وكيل بأذونات مناسبة

   عليك أولاً المصادقة بصفتك الخدمة التي لديها أذونات عارض عناصر التخزين. يعتمد ذلك على البيئة التي سيتم فيها تشغيل رمز إدارة الملفات.

   **خارج Google Cloud**

   إذا كان الرمز قيد التشغيل من خارج Google Cloud، مثل جهاز الكمبيوتر، نزِّل بيانات اعتماد الحساب من Google Cloud Console باتّباع الخطوات التالية:

   1. انتقِل إلى [وحدة تحكّم حساب الخدمة](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ar)
   2. اختَر حساب الخدمة ذي الصلة
   3. اختَر علامة التبويب **المفاتيح** واختَر **إضافة مفتاح، إنشاء مفتاح جديد**
   4. اختَر نوع المفتاح **JSON**، ولاحِظ مكان تنزيل الملف على جهازك.

   لمزيد من التفاصيل، راجِع مستندات Google Cloud الرسمية حول [إدارة
   مفاتيح حسابات الخدمة](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=ar).

   بعد ذلك، استخدِم الأوامر التالية للمصادقة. تفترض هذه الأوامر أنّ ملف حساب الخدمة موجود في الدليل الحالي باسم `service-account.json`.

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

   ### Javascript

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

   إذا كنت تستخدم Google Cloud مباشرةً، مثلاً من خلال استخدام [وظائف Cloud Run](https://cloud.google.com/functions?hl=ar) أو
   [مثيل Compute Engine](https://cloud.google.com/products/compute?hl=ar)، ستتوفّر لك
   بيانات اعتماد ضمنية ولكن عليك إعادة المصادقة لمنح
   النطاقات المناسبة.

   ### Python

   يتوقّع هذا الرمز تشغيل الخدمة في بيئة يمكن فيها الحصول تلقائيًا على
   [بيانات الاعتماد التلقائية للتطبيق](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ar)
   ، مثل Cloud Run أو Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   يتوقّع هذا الرمز تشغيل الخدمة في بيئة يمكن فيها الحصول تلقائيًا على
   [بيانات الاعتماد التلقائية للتطبيق](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ar)
   ، مثل Cloud Run أو Compute Engine.

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

   هذا أمر تفاعلي. بالنسبة إلى خدمات مثل Compute Engine، يمكنك إرفاق النطاقات بالخدمة قيد التشغيل على مستوى الإعداد. [راجِع مستندات الخدمة التي يديرها المستخدم للحصول على مثال.](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=ar#using)

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. تسجيل الملفات (Files API)

   استخدِم Files API لتسجيل الملفات وإنشاء مسار Files API يمكن استخدامه مباشرةً في Gemini API.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3-flash-preview",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
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

## عناوين URL الخارجية لبروتوكول HTTP / عناوين URL الموقَّعة

يمكنك تمرير عناوين URL لبروتوكول HTTPS التي يمكن الوصول إليها علنًا أو عناوين URL الموقَّعة مسبقًا (المتوافقة مع
[عناوين URL الموقَّعة مسبقًا في S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
وعناوين URL لبروتوكول SAS في Azure) مباشرةً في طلب الإنشاء. سيسترجع Gemini API المحتوى بأمان أثناء المعالجة. هذا مثالي للملفات التي يصل حجمها إلى 100 ميغابايت والتي لا تريد إعادة تحميلها.

يمكنك استخدام عناوين URL العلنية أو الموقَّعة كإدخال من خلال استخدام عناوين URL في الحقل `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### Javascript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### تسهيل الاستخدام

تأكَّد من أنّ عناوين URL التي تقدّمها لا تؤدي إلى صفحات تتطلّب تسجيل الدخول أو تستخدم نظام حظر الاشتراك غير المدفوع (جدار الدفع). بالنسبة إلى قواعد البيانات الخاصة، تأكَّد من إنشاء عنوان URL موقَّع بأذونات الوصول الصحيحة وتاريخ انتهاء الصلاحية.

### عمليات فحص الأمان

يُجري النظام فحصًا للإشراف على المحتوى على عنوان URL للتأكّد من استيفائه لمعايير الأمان والسياسات (مثل المحتوى غير المستبعَد والمحتوى المحظور بنظام حظر الاشتراك غير المدفوع). إذا لم يستوفِ عنوان URL الذي قدّمته هذا الفحص، سيظهر لك `url_retrieval_status` بقيمة `URL_RETRIEVAL_STATUS_UNSAFE`.

### أنواع المحتوى المتوافقة

تهدف قائمة أنواع الملفات المتوافقة والقيود إلى تقديم إرشادات أولية وليست شاملة. قد تتغيّر المجموعة الفعّالة من الأنواع المتوافقة ويمكن أن تختلف حسب النموذج المحدّد وإصدار أداة تقسيم الكلمات المستخدَمة. ستؤدي الأنواع غير المتوافقة إلى ظهور خطأ.
بالإضافة إلى ذلك، لا يتيح استرجاع المحتوى لأنواع الملفات هذه حاليًا سوى عناوين URL التي يمكن الوصول إليها علنًا.

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
  استخدِم File API للملفات الأكبر حجمًا أو الملفات المستخدَمة بشكل متكرر. استخدِم عناوين URL الخارجية للبيانات المستضافة حاليًا على الإنترنت.
- **تحديد أنواع MIME:** قدِّم دائمًا نوع MIME الصحيح لبيانات الملف لضمان معالجتها بشكل سليم.
- **معالجة الأخطاء:** نفِّذ عملية معالجة الأخطاء في الرمز لإدارة المشاكل المحتمَلة، مثل الأعطال في الشبكة أو مشاكل الوصول إلى الملفات أو أخطاء واجهة برمجة التطبيقات.
- **إدارة أذونات Google Cloud Storage:** عند استخدام تسجيل Google Cloud Storage، امنح وكيل خدمة Gemini API دور `Storage Object Viewer` اللازم فقط على الحِزم المحدّدة.
- **أمان عناوين URL الموقَّعة:** تأكَّد من أنّ عناوين URL الموقَّعة لها وقت انتهاء صلاحية مناسب وأذونات محدودة.

## القيود

- تختلف الحدود القصوى لحجم الملف حسب الطريقة (راجِع [جدول المقارنة](#method-comparison))
  ونوع الملف.
- تزيد البيانات المضمّنة من حجم بيانات الطلب.
- تكون عمليات تحميل الملفات باستخدام File API مؤقتة وتنتهي صلاحيتها بعد 48 ساعة.
- يقتصر استرجاع عناوين URL الخارجية على 100 ميغابايت لكل بيانات ويدعم أنواع محتوى محدّدة.
- يتطلّب تسجيل Google Cloud Storage إعداد IAM بشكل سليم وإدارة رموز OAuth المميزة.

## الخطوات التالية

- جرِّب كتابة طلبات متعددة الوسائط خاصة بك باستخدام
  [Google AI Studio](http://aistudio.google.com/?hl=ar).
- للحصول على معلومات حول تضمين الملفات في طلباتك، راجِع أدلة معالجة
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=ar)، و
  [الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar)، و
  [المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar).
- لمزيد من الإرشادات حول تصميم الطلبات، مثل ضبط مَعلمات أخذ العيّنات، راجِع الـ
  [دليل استراتيجيات الطلبات](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
