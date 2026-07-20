---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar
fetched_at: 2026-07-20T04:43:04.340018+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0641\u064a\u062f\u064a\u0648 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الفيديو

> لمعرفة المزيد حول إنشاء الفيديوهات، اطّلِع على دليل [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar).

يمكن لنماذج Gemini معالجة الفيديوهات، ما يتيح العديد من حالات الاستخدام المتقدّمة للمطوّرين
التي كانت تتطلّب في السابق نماذج خاصة بمجالات معيّنة.
تشمل بعض قدرات Gemini المرئية ما يلي: وصف الفيديوهات وتقسيمها واستخراج المعلومات منها، والإجابة عن أسئلة حول محتوى الفيديو، والإشارة إلى طوابع زمنية محدّدة ضمن الفيديو.

يمكنك تقديم فيديوهات كمدخلات إلى Gemini بالطرق التالية:

| طريقة الإرسال | الحد الأقصى للحجم | حالة الاستخدام المقترَحة |
| --- | --- | --- |
| [File API](#upload-video) | ‫20 غيغابايت (مدفوعة) / 2 غيغابايت (مجانية) | الملفات الكبيرة (100 ميغابايت أو أكثر) والفيديوهات الطويلة (10 دقائق أو أكثر) والملفات القابلة لإعادة الاستخدام |
| [تسجيل Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar#registration) | ‫2 غيغابايت (لكل ملف، بدون حدود لمساحة التخزين) | الملفات الكبيرة (100 ميغابايت أو أكثر) والفيديوهات الطويلة (10 دقائق أو أكثر) والملفات الدائمة والقابلة لإعادة الاستخدام |
| [البيانات المضمّنة](#inline-video) | ‫< 100 ميغابايت | الملفات الصغيرة (أقل من 100 ميغابايت) والمدّة القصيرة (أقل من دقيقة واحدة) والمدخلات لمرة واحدة |
| [عناوين URL على YouTube](#youtube) | لا ينطبق | الفيديوهات العلنية على YouTube |

> **ملاحظة:** ننصح باستخدام [File API](#upload-video) في معظم حالات الاستخدام، خاصةً للملفات التي يزيد حجمها عن 100 ميغابايت أو عندما تريد إعادة استخدام الملف في عدة طلبات.

للتعرّف على طرق إدخال الملفات الأخرى، مثل استخدام عناوين URL أو ملفات خارجية
مخزّنة في Google Cloud، راجِع دليل
[طرق إدخال الملفات](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ar).

### تحميل ملف فيديو

ينزّل الرمز التالي فيديو نموذجيًا ويحمّله باستخدام [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar)،
وينتظر إلى أن تتم معالجته، ثم يستخدم مرجع الملف الذي تم تحميله
لتلخيص الفيديو.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.5-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

استخدِم دائمًا Files API عندما يكون الحجم الإجمالي للطلب (بما في ذلك الملف، والنص
المطلوب، وتعليمات النظام، وما إلى ذلك) أكبر من 20 ميغابايت، أو عندما تكون مدة الفيديو
كبيرة، أو إذا كنت تنوي استخدام الفيديو نفسه في طلبات متعددة.
تقبل File API تنسيقات ملفات الفيديو مباشرةً.

لمزيد من المعلومات حول العمل باستخدام ملفات الوسائط، يُرجى الاطّلاع على [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

### تمرير بيانات الفيديو مضمّنة

بدلاً من تحميل ملف فيديو باستخدام File API، يمكنك تمرير فيديوهات أصغر حجمًا مباشرةً في الطلب إلى `generateContent`. هذه الطريقة مناسبة للفيديوهات القصيرة التي يقلّ إجمالي حجم طلبها عن 20 ميغابايت.

في ما يلي مثال على تقديم بيانات الفيديو المضمّن:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### تمرير عناوين URL لفيديوهات YouTube

يمكنك تمرير عناوين URL على YouTube مباشرةً إلى Gemini API كجزء من طلبك على النحو التالي:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**القيود:**

- في المستوى المجاني، لا يمكنك تحميل أكثر من 8 ساعات من فيديوهات على YouTube يوميًا.
- بالنسبة إلى المستوى المدفوع، لا يوجد حد أقصى استنادًا إلى مدة الفيديو.
- بالنسبة إلى النماذج الأقدم من Gemini 2.5، يمكنك تحميل فيديو واحد فقط لكل طلب. بالنسبة إلى Gemini 2.5 والإصدارات الأحدث، يمكنك تحميل 10 فيديوهات بحدّ أقصى لكل طلب.
- يمكنك تحميل فيديوهات علنية فقط (وليس فيديوهات خاصة أو غير مُدرَجة).

## استخدام التخزين المؤقّت للسياق في الفيديوهات الطويلة

بالنسبة إلى الفيديوهات التي تزيد مدتها عن 10 دقائق أو عندما تخطّط لإجراء طلبات متعددة على ملف الفيديو نفسه، استخدِم [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل التكاليف وتحسين وقت الاستجابة. تتيح لك ميزة التخزين المؤقت للسياق معالجة الفيديو مرة واحدة وإعادة استخدام الرموز المميزة لطلبات البحث اللاحقة، ما يجعلها مثالية لجلسات المحادثة أو التحليل المتكرر للمحتوى الطويل.

## الرجوع إلى الطوابع الزمنية في المحتوى

يمكنك طرح أسئلة حول نقاط زمنية محدّدة في الفيديو باستخدام طوابع زمنية بالتنسيق `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## استخراج إحصاءات تفصيلية من الفيديو

توفّر نماذج Gemini إمكانات قوية لفهم محتوى الفيديو من خلال معالجة المعلومات من كل من **محتوى الصوت والمرئي**. يتيح لك ذلك استخراج مجموعة كبيرة من التفاصيل، بما في ذلك إنشاء أوصاف لما يحدث في فيديو والإجابة عن الأسئلة حول محتواه.

بالنسبة إلى الأوصاف المرئية، يأخذ النموذج عيّنات من الفيديو بمعدّل **لقطة واحدة
في الثانية** (FPS). يعمل معدّل أخذ العيّنات التلقائي هذا بشكل جيد مع معظم المحتوى، ولكن يجب الانتباه إلى أنّه قد لا يرصد التفاصيل في الفيديوهات التي تتضمّن حركة سريعة أو تغييرات سريعة في المشاهد.
بالنسبة إلى المحتوى الذي يتضمّن الكثير من الحركة، ننصحك [بضبط عدد اللقطات في الثانية المخصّص](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## تخصيص معالجة الفيديو

يمكنك تخصيص معالجة الفيديو في Gemini API من خلال ضبط فواصل زمنية لتقطيع الفيديو أو تقديم عيّنات مخصّصة لمعدّل اللقطات في الثانية.

### ضبط الفواصل الزمنية لقص الفيديو

يمكنك قص الفيديو من خلال تحديد `videoMetadata` مع إزاحة البدء والانتهاء.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.5-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### ضبط عدد اللقطات في الثانية بشكل مخصّص

يمكنك ضبط أخذ عيّنات مخصّص لعدد اللقطات في الثانية من خلال تمرير الوسيطة `fps` إلى `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

يتم تلقائيًا أخذ عيّنة من الفيديو بمعدل لقطة واحدة في الثانية (FPS). ننصحك بضبط عدد اللقطات في الثانية على قيمة منخفضة (< 1) للفيديوهات الطويلة. ويكون ذلك مفيدًا بشكل خاص للفيديوهات الثابتة في معظمها (مثل المحاضرات). استخدِم عددًا أكبر من اللقطات في الثانية للفيديوهات التي تتطلّب تحليلًا زمنيًا دقيقًا، مثل فهم المشاهد السريعة أو تتبُّع الحركة السريعة.

## تنسيقات الفيديو المتوافقة

يتوافق Gemini مع أنواع MIME التالية لتنسيقات الفيديو:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## التفاصيل الفنية حول الفيديوهات

- **النماذج والسياق المتوافقان**: يمكن لجميع نماذج Gemini معالجة بيانات الفيديو.
  - يمكن للنماذج التي تتضمّن قدرة استيعاب تبلغ مليون رمز مميّز معالجة فيديوهات تصل مدتها إلى ساعة واحدة بدقة الوسائط التلقائية أو 3 ساعات بدقة الوسائط المنخفضة.
- **معالجة File API**: عند استخدام File API، يتم تخزين الفيديوهات بمعدّل لقطة واحدة في الثانية (FPS) وتتم معالجة الصوت بمعدّل 1 كيلوبت في الثانية (قناة واحدة).
  تتم إضافة الطوابع الزمنية كل ثانية.
  - هذه المعدّلات عرضة للتغيير في المستقبل لتحسين الاستدلال.
  - يمكنك تجاوز معدّل أخذ العيّنات البالغ إطارًا واحدًا في الثانية من خلال [ضبط عدد اللقطات في الثانية المخصّص](#custom-frame-rate).
- **احتساب الرموز المميزة**: يتم تقسيم كل ثانية من الفيديو إلى رموز مميزة على النحو التالي:
  - اللقطات الفردية (يتم أخذ عينات بمعدّل لقطة واحدة في الثانية):
    - إذا تم ضبط قيمة [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=ar#MediaResolution) على منخفضة، يتم تقسيم اللقطات إلى 66 رمزًا مميزًا لكل لقطة.
    - بخلاف ذلك، يتم تقسيم اللقطات إلى رموز مميزة بمعدل 258 رمزًا مميزًا لكل لقطة.
  - الصوت: 32 رمزًا مميزًا في الثانية
  - يتم تضمين البيانات الوصفية أيضًا.
  - الإجمالي: حوالي 300 رمز مميز لكل ثانية من الفيديو بدقة الوسائط التلقائية، أو 100 رمز مميز لكل ثانية من الفيديو بدقة الوسائط المنخفضة
- **دقة الوسائط**: يتيح Gemini 3 التحكّم بدقة في معالجة الصور المتعدّدة الوسائط باستخدام المَعلمة `media_resolution`. تحدّد المَعلمة
  `media_resolution`
  **الحد الأقصى لعدد الرموز المميزة المخصّصة لكل صورة إدخال أو إطار فيديو.**
  تؤدي الدقة الأعلى إلى تحسين قدرة النموذج على قراءة النصوص الدقيقة أو تحديد التفاصيل الصغيرة، ولكنها تزيد من استخدام الرموز المميزة ووقت الاستجابة.

  للحصول على مزيد من التفاصيل حول المَعلمة وكيفية تأثيرها في عمليات حساب الرموز المميزة، يمكنك الاطّلاع على دليل [دقة الوسائط](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ar).
- **تنسيق الطابع الزمني**: عند الإشارة إلى لحظات معيّنة في فيديو ضمن طلبك، استخدِم التنسيق `MM:SS` (مثلاً، `01:15` للدقيقة الواحدة و15 ثانية).
- **أفضل الممارسات**:

  - استخدِم فيديو واحدًا فقط لكل طلب للحصول على أفضل النتائج.
  - في حال الجمع بين نص وفيديو واحد، ضَع طلب النص *بعد* جزء الفيديو في مصفوفة `contents`.
  - يُرجى العِلم أنّ تسلسلات اللقطات السريعة قد تفقد بعض التفاصيل بسبب معدّل أخذ العيّنات البالغ لقطة واحدة في الثانية. ننصحك بإبطاء سرعة هذه المقاطع إذا لزم الأمر.

## الخطوات التالية

يوضّح هذا الدليل كيفية تحميل ملفات الفيديو وإنشاء نواتج نصية من مدخلات الفيديو. لمزيد من المعلومات، يُرجى الاطّلاع على المراجع التالية:

- [تعليمات النظام](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#system-instructions):
  تتيح لك تعليمات النظام توجيه سلوك النموذج استنادًا إلى احتياجاتك وحالات الاستخدام المحدّدة.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar): مزيد من المعلومات حول تحميل الملفات وإدارتها لاستخدامها مع Gemini
- [استراتيجيات إنشاء الطلبات](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide): تتيح واجهة Gemini API إمكانية إنشاء الطلبات باستخدام بيانات نصية وصور وملفات صوت وفيديوهات، ويُعرف ذلك أيضًا باسم إنشاء الطلبات المتعددة الوسائط.
- [إرشادات الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar): في بعض الأحيان، تقدّم نماذج الذكاء الاصطناعي التوليدي نتائج غير متوقعة، مثل نتائج غير دقيقة أو متحيزة أو مسيئة. تُعد المعالجة اللاحقة والتقييم من قِبل فريق ضروريَين للحدّ من مخاطر الضرر الناجم عن هذه النتائج.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
