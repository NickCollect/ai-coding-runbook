---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=ar
fetched_at: 2026-07-06T05:09:44.688583+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0627\u0644\u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a \u0648\u062a\u0639\u062f\u064a\u0644\u0647\u0627 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء الفيديوهات وتعديلها باستخدام Gemini Omni Flash

‫Gemini Omni Flash‏ (`gemini-omni-flash-preview`) هو نموذج متعدّد الوسائط عالي الأداء مصمّم لإنشاء الفيديوهات وتعديلها والتحكّم فيها بشكل سينمائي وبسرعة عالية.
يستند Gemini Omni إلى الإمكانات الأساسية التالية التي تميّزه عن نماذج الفيديوهات السابقة:

- **تعدُّد الوسائط الأصلي:** يعالج النموذج النصوص والصور والمقاطع الصوتية والفيديوهات في آنٍ واحد، ما يمنحك نتائج أكثر تماسكًا واتساقًا وقابلة للتحكّم.
- **التعديل الحواري:** تتيح لك واجهة برمجة التطبيقات [Interactions
  API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) تحسين فيديوهاتك وتعديلها بشكل متكرّر من خلال محادثة بلغة طبيعية. يمكنك وصف التغييرات المطلوبة، وسيُطبّق النموذج التعديل مع الاحتفاظ بأجزاء الفيديو التي تريدها.
- **المعرفة بالعالم:** يجمع Gemini Omni بين فهم الفيزياء ومعرفة Gemini بالتاريخ والعلوم والسياق الثقافي، ما يربط بين الواقعية الفائقة وسرد القصص الهادف.

## إنشاء فيديو من نص

يمكنكم إنشاء فيديو من طلب نصي. ينشئ النموذج فيديو يتضمّن محتوًى صوتيًا استنادًا إلى الوصف النصي الذي تقدّمونه. للحصول على أفضل النتائج، اكتبوا طلبات تتضمّن تفاصيل مثل وصف المشهد وحركة الكاميرا والإضاءة والمزاج.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({  
  model: 'gemini-omni-flash-preview',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### مخطط استجابة REST

حقل `interaction.output_video` المريح **خاص بحزمة تطوير البرامج (SDK) فقط**.
يمكنكم الحصول على الناتج من الفيديو من مصفوفة `steps` عند استخدام REST API مباشرةً.

**بنية JSON غير المُعالَجة في REST:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

### التحكّم في نسبة العرض إلى الارتفاع

اضبطوا `aspect_ratio` على `"9:16"` لإنشاء فيديوهات باتجاه عمودي. الوضع الأفقي (16:9) هو الإعداد التلقائي.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

## إنشاء فيديو من صورة

يمكنكم تقديم صورة مرجعية مع الطلب النصي. سيقرّر النموذج كيفية استخدام الصورة استنادًا إلى الطلب. يفيد ذلك في إضفاء الحيوية على لقطات المنتجات أو الرسومات التوضيحية أو الصور الفوتوغرافية.

يوضّح المثال التالي كيفية استخدام الصورة المرجعية لرسمة سمكة تقفز خارج الماء:

![رسم لسمكة تقفز خارج الماء](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=ar)

مع الطلب التالي:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

لإنشاء فيديو واقعي للرسمة.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### معرِّف الموضوع

يمكنكم إنشاء فيديو يتضمّن مواضيع محدّدة يتم تقديمها كصور مرجعية.
على سبيل المثال، يوضّح الرمز التالي كيفية تقديم صورتَين لقطة وخيط لإنشاء فيديو للقطة وهي تلعب بالخيط.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### مَعلمة المهام

استخدِموا المَعلمة `task` في `video-config` للإشارة بوضوح إلى السلوك المقصود، على سبيل المثال، إذا كنتم تريدون أن ينشئ النموذج فيديو من صورة، يمكنكم ضبط المَعلمة على `image_to_video`. إذا لم يتم ضبط هذه المَعلمة، سيستنتج النموذج ما تريدونه من الطلب.

في ما يلي القيم المسموح بها:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

يوضّح المثال التالي كيفية ضبط هذه المَعلمة لمثال إنشاء فيديو من صورة الذي تم عرضه سابقًا.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-flash-preview",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## تعديل الفيديوهات مع الاحتفاظ بالحالة

يمكنكم إنشاء فيديو وتعديله بشكل متكرّر باستخدام طلبات المتابعة. يستند كل دور إلى النتيجة السابقة. يتذكّر النموذج سياق الفيديو، ويُطبّق التغييرات مع الاحتفاظ بالعناصر التي لم تذكروها. استخدِموا `previous_interaction_id` لتتبُّع سجلّ المحادثات وحالة الفيديو الذي تم إنشاؤه بدون إعادة تحميل الفيديو السابق.

يوضّح المثال التالي كيفية إنشاء فيديو أولاً ثم تعديله:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-flash-preview", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-flash-preview",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

مثال على فيديو أولي:

مثال على فيديو معدَّل:

ينتج عن كل دور في المحادثة فيديو جديد. يفهم النموذج السياق من الأدوار السابقة، ما يتيح لكم إجراء تغييرات تدريجية، مثل تعديل الإضاءة واستبدال الخلفيات، بدون إعادة وصف المشهد بأكمله.

### تعديل فيديوهاتكم

يمكنكم تحميل فيديوهاتكم باستخدام [واجهة برمجة التطبيقات Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) لتعديلها
باستخدام Gemini Omni Flash.

يوضّح المثال التالي كيفية تعديل الفيديو الأصلي التالي:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### راحة

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-flash-preview",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

مثال على فيديو معدَّل:

 

## استرداد الفيديوهات باستخدام معرّف موارد موحّد (URI)

استخدِموا المَعلمة `delivery="uri"` في
`response_format` لاسترداد الفيديوهات التي تم إنشاؤها والتي يزيد حجمها عن 4 ميغابايت.
يؤدي ذلك إلى عرض معرّف موارد موحّد (URI) مستضاف على Google يمكنكم طلبه بشكل متكرّر إلى أن تصبح حالة الفيديو `ACTIVE` قبل تنزيله.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### راحة

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**بنية JSON غير المُعالَجة في REST (معرّف موارد موحّد):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

## أفضل الممارسات

- **استخدام طريقة التسليم من خلال معرّف موارد موحّد للفيديوهات الكبيرة:** بالنسبة إلى الفيديوهات التي يزيد حجمها عن 4 ميغابايت (>720p
  إذا كانت متوفّرة)، استخدِموا `delivery="uri"` في `response_format` لتجنُّب الحدود القصوى
  لحجم الحمولة.
- **الأداء المحسّن:** اضبطوا `background=false` و`store=false` و`stream=false` لإنشاء أسرع ومتزامن أحادي. يُرجى العِلم أنّ ضبط `store=false` يعني أنّه لن يكون من الممكن تعديل الفيديو الذي تم إنشاؤه في الأدوار اللاحقة باستخدام `previous_interaction_id`.
- **دقة الطلب:** يُرجى الاطّلاع على قسم [إرشادات الطلبات](#prompt-guide) للحصول على
  التفاصيل.

## القيود

- لا يمكن تحميل الصور التي تتضمّن قاصرين وتعديلها في المنطقة الاقتصادية الأوروبية وسويسرا والمملكة المتحدة.
- لا يمكن تحميل الصور التي تتضمّن أشخاصًا معيّنين يمكن التعرّف عليهم وتعديلها.
- لا يمكن حاليًا للمستخدمين في المنطقة الاقتصادية الأوروبية وسويسرا والمملكة المتحدة تعديل الفيديوهات التي تم تحميلها (يمكن تعديل الفيديوهات التي ينشئها النموذج).
- لا يمكن تحميل المراجع الصوتية في الإصدار الحالي من واجهة برمجة التطبيقات.
- يقبل مخطط واجهة برمجة التطبيقات المراجع الصوتية التي تصل مدتها إلى 3 ثوانٍ، ولكن لا يعالجها النموذج بشكل صحيح في الوقت الحالي.
- لا يمكن الإشارة إلى فيديوهات متعدّدة أو الاستنتاج منها. قد تؤدي محاولة توجيه طلبات متعدّدة الفيديوهات إلى تدهور أداء النموذج أو ظهور نتائج غير متوقّعة.
- لا يمكن توسيع الفيديوهات أو إجراء استيفاء لها (إنشاء فيديو بين الإطار الأول والأخير).
- لا يمكن تعديل الصوت.
- لا يمكن استخدام معدّل النقل الذي تم توفيره.
- لا يمكن استخدام تعليمات النظام ودرجة الحرارة و`top_p` وتسلسلات الإيقاف والطلبات السلبية (يمكنكم وضع الطلبات السلبية في الطلب العادي، مثلاً "لا تفعل X").
- لا يمكن استخدام فيديوهات YouTube كمصدر للوسائط.

## التفاصيل الفنية

- تتضمّن جميع الفيديوهات التي يتم إنشاؤها علامات مائية من SynthID، وهي غير مرئية للمشاهدين ولكن يمكن رصدها آليًا للتحقّق من المصدر.
- تختلف أوقات إنشاء الفيديوهات استنادًا إلى المدة ودرجة الدقة والحِمل الحالي على واجهة برمجة التطبيقات. يستغرق إنشاء الفيديوهات الأطول والأعلى دقةً وقتًا أطول.
- يتم تطبيق فلاتر أمان المحتوى على كلٍّ من الطلبات المُدخَلة والفيديو الذي تم إنشاؤه (ويعتمد ذلك على منطقتكم). سيتم حظر الطلبات التي تنتهك سياسات الاستخدام.
- اللغة الإنجليزية (EN) متوافقة بالكامل، ولكن لم يتم تقييم اللغات الأخرى، لذا قد تعمل ولكن يمكن أن تختلف النتائج.

## دليل كتابة الطلبات المُوجَّهة إلى Gemini Omni Flash

يحتوي هذا القسم على نصائح وأمثلة حول كيفية توجيه الطلبات إلى Gemini Omni Flash بفعالية.

### مشهد واحد

سيحاول Omni Flash تلقائيًا إنشاء فيديو يتضمّن بضع لقطات مختلفة.
سيحاول النموذج إنشاء سرد مثير للاهتمام استنادًا إلى الطلب.

إذا كنتم بحاجة إلى أن يحتوي الفيديو الناتج على مشهد واحد، يجب أن تطلبوا ذلك:

- في مشهد واحد متواصل
- في لقطة واحدة متواصلة
- بدون قطع المشهد

على سبيل المثال:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### إزالة العناصر غير المرغوب فيها

إذا كان الفيديو الذي تم إنشاؤه يحتوي على عناصر لا تريدونها، أدرِجوا طلبات سلبية بسيطة لتجنُّبها:

- بدون حوار
- بدون زينة
- بدون تأثيرات صوتية إضافية

### طلبات التعديل

تعمل الطلبات البسيطة بشكل أفضل لتعديل الفيديوهات. قد تؤدي الطلبات الوصفية المفرطة إلى تغييرات غير مقصودة.

في ما يلي المزيد من الأمثلة على طلبات التعديل البسيطة:

- اجعلوا هذا الفيديو رسومًا متحركة
- ضعوا قبعة عصرية على رأس هذا الشخص
- غيِّروا الإضاءة لتكون أكثر إثارة
- غيِّروا النص على اللافتة ليصبح "Omni Flash"

عند تعديل جانب معيّن من الفيديو، أدرِجوا `"Keep everything else the same"` للحفاظ على الاتساق المرئي.

في ما يلي بعض الأمثلة لتوضيح كيفية تطبيق هذه التقنية:

- **تجنُّب:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **التبسيط:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **تجنُّب:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **التبسيط:** `Make the phone invisible. Keep everything else the
    same.`

### توجيه الطلبات بشأن المحتوى الصوتي

سيحاول النموذج تلقائيًا إنشاء مقطع صوتي مناسب لفيديو. وقد لا يكون هذا ما تريدونه دائمًا. يمكنكم استخدام الطلب لوصف نوع المحتوى الصوتي المطلوب. يُعدّ ذلك مهمًا بشكل خاص إذا كنتم تريدون إضافة موسيقى إلى الفيديو:

- أدرِجوا موسيقى هادئة في الخلفية
- يتضمّن الفيديو إيقاعًا سريعًا لموسيقى التكنو
- المحتوى الصوتي هو بث إذاعي منخفض الجودة في الخلفية يعرض أغنية

### تحديد توقيت الأحداث

يمكنكم توجيه طلبات لحدوث أشياء في أوقات معيّنة في الفيديو، ولا حاجة إلى استخدام بنية دقيقة ويمكنكم استخدام لغة طبيعية. يفيد ذلك بشكل خاص في إنشاء عمليات قطع المشاهد أو الإيقاع أو التسلسلات السريعة.
في ما يلي أمثلة:

- بعد 3 ثوانٍ، تدخل امرأة إلى المشهد.
- في الثانية 5، يبدأ الكورس في المحتوى الصوتي في الخلفية.
- كل ثانيتَين، يتم الانتقال إلى إطار جديد.
- في تسلسل سريع، يتم تغيير المشهد إلى موقع جديد كل نصف ثانية (12 إطارًا بمعدّل 24 إطارًا في الثانية).

يمكنكم أيضًا استخدام بنية الرمز الزمني:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### توجيه الطلبات الوصفية

يمكنكم أن تطلبوا من Gemini Omni Flash الانتباه إلى الصفات العامة أو المبادئ العامة لإنشاء الفيديوهات:

- ضعوا في الاعتبار التفاصيل الدقيقة والتعبير والتوقيت لإنشاء مشهد غني جدًا ومفصّل ولكنه طبيعي تمامًا.
- كونوا دقيقين للغاية في أوصاف الشخصيات والبيئات.
  طبِّقوا مبادئ تصميم الأزياء على الشخصيات. كونوا دقيقين للغاية بشأن الأشخاص والعناصر والأشياء في المشهد.
- أدرِجوا الكثير من التفاصيل المناسبة في عناصر الخلفية لجعل المشهد يبدو واقعيًا وطبيعيًا.
- أنشئوا فيديو سريعًا يعرض `[thing]` مختلفًا ونادرًا كل ثانية، وموسيقى مبهجة
  ، وأدرِجوا نصًا لتسمية الشيء.

### النص في الفيديوهات

يمكنكم توجيه طلبات لتضمين نص في الفيديو، وسيعرضه Gemini Omni بطريقة صحيحة وقابلة للقراءة. إذا كان الفيديو يتضمّن نصًا يظهر بشكل طبيعي، حتى في عناصر الخلفية، يمكن أن يساعد ذلك في تحديد ما يجب أن يقوله.

- كلمة واحدة على الشاشة في كل مرة: "did, you, know, that, Omni, can, do, awesome, text?" تظهر كل كلمة لمدة ثانية واحدة بنمط متحرك مختلف. بدون حوار.
- هناك لافتة شارع مكتوب عليها: "This is an AI generation by Omni"، وهناك واجهة متجر مكتوب عليها: "All you need AI"، وهناك سيارة تحمل لوحة الأرقام: "OMN111"

### استخدام العلامات في الطلبات لضبط أدوار الصور

يمكنكم استخدام العلامات لربط الوسائط التي تم تحميلها بأدوار إنشاء محدّدة. يتيح لكم ذلك تحديد ما إذا كانت كل صورة هي إطار أولي أو مرجع.

#### 1. العلامات البسيطة (يُنصح بها)

في الحالات البسيطة التي تكون فيها أدوار الصور واضحة من الطلب، يمكنكم ربط الصور بالأدوار مباشرةً:

- **`<FIRST_FRAME>`**: استخدِموا الصورة كإطار بداية للفيديو، لـ
  مثلاً: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: استخدِموا الصورة كمرجع، مثلاً: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (يجمع بين مرجع النمط من الصورة الأولى ومرجع الموضوع من الصورة الثانية).
  تبدأ المراجع من الصور من 0.

في ما يلي مثال يتضمّن 6 صور مرجعية:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. الإعلانات الصريحة

في الحالات الأكثر تعقيدًا التي تتضمّن صورًا وأدوارًا متعدّدة، يمكنكم استخدام علامات البادئة الصريحة المقترنة باللاحقات التعليمية باللغة الطبيعية.

- **تحديد المصادر والصور المرجعية**:
  - `[# Sources <FIRST_FRAME>@Image1]` سيستخدم الصورة الأولى كإطار بداية.
  - `[# References <IMAGE_REF_0>@Image1]` سيستخدم الصورة الأولى كمرجع.
  - `[# References <IMAGE_REF_1>@Image2]` سيستخدم الصورة الثانية كمرجع.
  - `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` سيستخدم كلتا الصورتَين كمرجعَين.
  - `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` سيستخدم الصورة الأولى كإطار بداية والصورة الثانية كمرجع.
- **التعليمات الإرشادية**: أدرِجوا التعليمات الإرشادية في نهاية الطلب:
  - بالنسبة إلى إطار البداية: `"Use this image as the starting frame."`
  - بالنسبة إلى الصور المرجعية: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

مثال على طلب موسّع:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## الخطوات التالية

- ابدأوا رحلتكم مع Gemini Omni Flash من خلال التجربة في [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=ar).
- تعلَّموا كيفية كتابة طلبات أفضل باستخدام [مقدّمة في تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
