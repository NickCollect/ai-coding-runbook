---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=hi
fetched_at: 2026-08-17T02:24:02.450012+00:00
title: "Gemini Omni Flash \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0935\u0940\u0921\u093f\u092f\u094b \u091c\u0928\u0930\u0947\u091f \u0914\u0930 \u090f\u0921\u093f\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Omni Flash की मदद से वीडियो जनरेट और एडिट करना

Gemini Omni Flash (`gemini-omni-flash-preview`) एक हाई-परफ़ॉर्मेंस मल्टीमॉडल है. इसे वीडियो जनरेट करने, एडिट करने, और सिनेमैटिक कंट्रोल के लिए डिज़ाइन किया गया है. यह मॉडल, इन कामों को तेज़ी से करता है.
Gemini Omni को इन मुख्य क्षमताओं के आधार पर बनाया गया है. ये क्षमताएं, इसे वीडियो के पिछले मॉडल से अलग बनाती हैं:

- **नेटिव मल्टीमॉडल:** यह टेक्स्ट, इमेज, ऑडियो, और वीडियो को एक साथ प्रोसेस करता है. इससे आपको ज़्यादा कोहेसिव, एक जैसा, और कंट्रोल किया जा सकने वाला आउटपुट मिलता है.
- **बातचीत के ज़रिए एडिटिंग:** यह सुविधा, [Interactions
  API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) की मदद से उपलब्ध कराई जाती है. इसकी मदद से, नैचुरल लैंग्वेज में बातचीत करके, वीडियो को बार-बार बेहतर बनाया जा सकता है और उनमें बदलाव किया जा सकता है. बताएं कि आपको किस तरह के बदलाव करने हैं. मॉडल, वीडियो के उन हिस्सों को बनाए रखते हुए बदलाव करता है जिन्हें आपको रखना है.
- **दुनिया के बारे में जानकारी:** Gemini Omni, फ़िज़िक्स की समझ को इतिहास, विज्ञान, और सांस्कृतिक संदर्भ के बारे में Gemini की जानकारी के साथ जोड़ता है. इससे, फ़ोटोरेलिज़्म से लेकर कहानी कहने के मकसद तक के बीच के अंतर को कम किया जा सकता है.

## टेक्स्ट से वीडियो जनरेट करने की सुविधा

टेक्स्ट प्रॉम्प्ट की मदद से वीडियो जनरेट करें. मॉडल, आपके टेक्स्ट के ब्यौरे के आधार पर ऑडियो वाला वीडियो जनरेट करता है. बेहतर नतीजे पाने के लिए, सीन के ब्यौरे, कैमरा मूवमेंट, लाइटिंग, और मूड जैसी जानकारी के साथ प्रॉम्प्ट लिखें.

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### REST रिस्पॉन्स स्कीमा

सुविधा वाला फ़ील्ड `interaction.output_video` **सिर्फ़ एसडीके** के लिए उपलब्ध है.
REST API का सीधे तौर पर इस्तेमाल करने पर, `steps` कलेक्शन से वीडियो आउटपुट पाएं.

**REST JSON का रॉ स्ट्रक्चर:**

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

### आसपेक्ट रेशियो (चौड़ाई-ऊंचाई का अनुपात) कंट्रोल करना

पोर्ट्रेट वीडियो बनाने के लिए, `aspect_ratio` को `"9:16"` पर सेट करें. डिफ़ॉल्ट रूप से, लैंडस्केप (16:9) सेट होता है.

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

### REST

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

## इमेज से वीडियो जनरेट करने की सुविधा

टेक्स्ट प्रॉम्प्ट के साथ, रेफ़रंस इमेज दी जा सकती है. आपके प्रॉम्प्ट के आधार पर, मॉडल तय करेगा कि इमेज का इस्तेमाल कैसे करना है. यह सुविधा, प्रॉडक्ट की तस्वीरों, इलस्ट्रेशन या फ़ोटोग्राफ़ को असली जैसा दिखाने में मददगार है.

यहां दिए गए उदाहरण में, पानी से छलांग लगाती मछली के ड्रॉइंग की रेफ़रंस इमेज का इस्तेमाल करने का तरीका बताया गया है:

![पानी से बाहर छलांग लगाती हुई मछली का ड्रॉइंग](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=hi)

इस प्रॉम्प्ट के साथ:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

ड्रॉइंग का असली जैसा दिखने वाला वीडियो जनरेट करने के लिए.

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

### REST

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

### सब्जेक्ट रेफ़रंस

रेफ़रंस इमेज के तौर पर दिए गए खास सब्जेक्ट को शामिल करके, वीडियो जनरेट किया जा सकता है.
उदाहरण के लिए, यहां दिए गए कोड में, बिल्ली और ऊन की दो इमेज दी गई हैं. इससे, बिल्ली के ऊन से खेलने का वीडियो जनरेट किया जा सकता है.

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

### REST

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

### टास्क पैरामीटर

वीडियो-कॉन्फ़िगरेशन में, `task` पैरामीटर का इस्तेमाल करके, वीडियो जनरेट करने के मकसद के बारे में साफ़ तौर पर बताया जा सकता है. उदाहरण के लिए, अगर आपको मॉडल से किसी इमेज से वीडियो जनरेट कराना है,
तो पैरामीटर को `image_to_video` पर सेट किया जा सकता है.`video-config` अगर यह सेट नहीं किया जाता है, तो मॉडल प्रॉम्प्ट से यह अनुमान लगाएगा कि आपको क्या चाहिए.

ये वैल्यू इस्तेमाल की जा सकती हैं:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

यहां दिए गए उदाहरण में, पहले दिखाई गई इमेज से वीडियो बनाने के उदाहरण के लिए, इसे सेट करने का तरीका बताया गया है.

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

### REST

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

## स्टेटफ़ुल वीडियो एडिटिंग

फ़ॉलो-अप प्रॉम्प्ट का इस्तेमाल करके, वीडियो जनरेट करें और उसे बार-बार एडिट करें. हर बार, पिछले नतीजे के आधार पर वीडियो में बदलाव किया जाता है. मॉडल, वीडियो के कॉन्टेक्स्ट को याद रखता है. साथ ही, आपके बदलावों को लागू करते समय, उन एलिमेंट को बनाए रखता है जिनके बारे में आपने नहीं बताया है. `previous_interaction_id` का इस्तेमाल करके, बातचीत के इतिहास और जनरेट किए गए वीडियो की स्थिति को ट्रैक किया जा सकता है. इसके लिए, पिछले वीडियो को दोबारा अपलोड करने की ज़रूरत नहीं होती.

यहां दिए गए उदाहरण में, पहले वीडियो जनरेट करने और फिर उसे एडिट करने का तरीका बताया गया है:

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

शुरुआती वीडियो का उदाहरण:

एडिट किए गए वीडियो का उदाहरण:

बातचीत में हर बार, एक नया वीडियो जनरेट होता है. मॉडल, पिछली बातचीत के कॉन्टेक्स्ट को समझता है. इससे, लाइटिंग को अडजस्ट करने और बैकग्राउंड बदलने जैसे बदलाव किए जा सकते हैं. इसके लिए, पूरे सीन के बारे में दोबारा बताने की ज़रूरत नहीं होती.

### अपने वीडियो एडिट करना

अपने वीडियो अपलोड करने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल करें. इसके बाद, उन्हें एडिट करने के लिए
Gemini Omni Flash की मदद लें.

यहां दिए गए उदाहरण में, इस ओरिजनल वीडियो को एडिट करने का तरीका बताया गया है:

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

### REST

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

एडिट किए गए वीडियो का उदाहरण:

 

## यूआरआई की मदद से वीडियो वापस पाना

जनरेट किए गए ऐसे वीडियो वापस पाने के लिए जो 4 एमबी से बड़े हैं,
`response_format` में `delivery="uri"` पैरामीटर का इस्तेमाल करें.
इससे, Google पर होस्ट किया गया यूआरआई मिलता है. इसे डाउनलोड करने से पहले, वीडियो के `ACTIVE` होने तक पोल किया जा सकता है.

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

### REST

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

**REST JSON का रॉ स्ट्रक्चर (यूआरआई):**

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

## सबसे सही तरीके

- **बड़े वीडियो के लिए यूआरआई डिलीवरी का इस्तेमाल करना:** 4 एमबी से बड़े वीडियो (>720p
  उपलब्ध होने पर) के लिए, पेलोड
  साइज़ की सीमाओं से बचने के लिए, `delivery="uri"` में `response_format` का इस्तेमाल करें.
- **ऑप्टिमाइज़ की गई परफ़ॉर्मेंस:** तेज़ और सिंक्रोनस यूनरी जनरेशन के लिए, `background=false`, `store=false`, और `stream=false` सेट करें. ध्यान दें कि `store=false` सेट करने का मतलब है कि जनरेट किए गए वीडियो को, `previous_interaction_id` का इस्तेमाल करके, बाद में एडिट नहीं किया जा सकेगा.
- **प्रॉम्प्ट की सटीक जानकारी:** ज़्यादा जानकारी के लिए, [प्रॉम्प्ट के लिए गाइडेंस](#prompt-guide) सेक्शन देखें.

## सीमाएं

- यूरोपियन इकनॉमिक एरिया, स्विट्ज़रलैंड, और यूनाइटेड किंगडम में, नाबालिगों की इमेज अपलोड और एडिट नहीं की जा सकतीं.
- कुछ पहचाने जा सकने वाले लोगों की इमेज अपलोड और एडिट नहीं की जा सकतीं.
- फ़िलहाल, यूरोपियन इकनॉमिक एरिया (ईईए), स्विट्ज़रलैंड, और यूनाइटेड किंगडम में रहने वाले लोग, अपलोड किए गए वीडियो को एडिट नहीं कर सकते. हालांकि, मॉडल से जनरेट किए गए वीडियो को एडिट किया जा सकता है.
- एपीआई के मौजूदा वर्शन में, ऑडियो रेफ़रंस अपलोड नहीं किए जा सकते.
- एपीआई स्कीमा में, तीन सेकंड तक की अवधि वाले वीडियो रेफ़रंस स्वीकार किए जाते हैं. हालांकि, फ़िलहाल मॉडल इन्हें सही तरीके से प्रोसेस नहीं करता.
- एक से ज़्यादा वीडियो के लिए रेफ़रंस या तर्क देने की सुविधा उपलब्ध नहीं है. एक से ज़्यादा वीडियो के लिए प्रॉम्प्ट देने की कोशिश करने पर, मॉडल की परफ़ॉर्मेंस खराब हो सकती है या अनचाहे आउटपुट मिल सकते हैं.
- वीडियो एक्सटेंशन और वीडियो इंटरपोलेशन (पहले और आखिरी फ़्रेम के बीच वीडियो जनरेट करना) की सुविधा उपलब्ध नहीं है.
- आवाज़ में बदलाव करने की सुविधा उपलब्ध नहीं है.
- प्रोविज़न किए गए थ्रूपुट की सुविधा उपलब्ध नहीं है.
- सिस्टम के निर्देश, तापमान, `top_p`, स्टॉप सीक्वेंस, और नेगेटिव प्रॉम्प्ट की सुविधा उपलब्ध नहीं है.हालांकि, नेगेटिव प्रॉम्प्ट को सामान्य प्रॉम्प्ट में शामिल किया जा सकता है. जैसे, "X न करें".
- YouTube वीडियो को मीडिया सोर्स के तौर पर इस्तेमाल करने की सुविधा उपलब्ध नहीं है.

## तकनीकी जानकारी

- जनरेट किए गए सभी वीडियो में SynthID वॉटरमार्क शामिल होता है. यह वॉटरमार्क, दर्शकों को नहीं दिखता. हालांकि, ओरिजन की पुष्टि करने के लिए, इसे प्रोग्राम के ज़रिए डिटेक्ट किया जा सकता है.
- वीडियो जनरेट होने में लगने वाला समय, अवधि, रिज़ॉल्यूशन, और एपीआई के मौजूदा लोड के आधार पर अलग-अलग होता है. ज़्यादा अवधि और ज़्यादा रिज़ॉल्यूशन वाले वीडियो जनरेट होने में ज़्यादा समय लगता है.
- इनपुट प्रॉम्प्ट और जनरेट किए गए वीडियो, दोनों पर कॉन्टेंट की सुरक्षा के फ़िल्टर लागू होते हैं. ये फ़िल्टर, आपके देश/इलाके के हिसाब से लागू होते हैं. इस्तेमाल की नीतियों का उल्लंघन करने वाले प्रॉम्प्ट ब्लॉक कर दिए जाएंगे.
- अंग्रेज़ी (ईएन) पूरी तरह से काम करती है. हालांकि, अन्य भाषाओं की जांच नहीं की गई है. इसलिए, वे काम कर सकती हैं, लेकिन नतीजे अलग-अलग हो सकते हैं.

## Gemini Omni Flash के लिए प्रॉम्प्ट गाइड

इस सेक्शन में, Gemini Omni Flash के लिए असरदार तरीके से प्रॉम्प्ट लिखने के बारे में सलाह और उदाहरण दिए गए हैं.

### एक सीन

डिफ़ॉल्ट रूप से, Omni Flash कुछ अलग-अलग शॉट वाला वीडियो बनाने की कोशिश करेगा.
यह प्रॉम्प्ट के आधार पर, दिलचस्प कहानी बनाने की कोशिश करेगा.

अगर आपको आउटपुट वीडियो में एक ही सीन चाहिए, तो इसके लिए प्रॉम्प्ट में यह जानकारी शामिल करें:

- एक ही सीन में
- एक ही शॉट में
- सीन में कोई कट नहीं

उदाहरण के लिए:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### अनचाहे एलिमेंट हटाना

अगर जनरेट किए गए वीडियो में ऐसी चीज़ें शामिल हैं जो आपको नहीं चाहिए, तो उन्हें हटाने के लिए, सामान्य नेगेटिव प्रॉम्प्ट शामिल करें:

- कोई डायलॉग नहीं
- कोई सजावट नहीं
- कोई अतिरिक्त साउंड इफ़ेक्ट नहीं

### एडिटिंग के लिए प्रॉम्प्ट

वीडियो एडिटिंग के लिए, सामान्य प्रॉम्प्ट सबसे सही तरीके से काम करते हैं. ज़्यादा जानकारी वाले प्रॉम्प्ट से, अनचाहे बदलाव हो सकते हैं.

यहां एडिटिंग के लिए सामान्य प्रॉम्प्ट के कुछ और उदाहरण दिए गए हैं:

- इस वीडियो को ऐनिमे में बदलो
- इस व्यक्ति को फ़ैशन वाला हैट पहनाओ
- लाइटिंग को ज़्यादा ड्रामैटिक बनाओ
- साइन पर मौजूद टेक्स्ट को बदलकर "Omni Flash" लिखो

वीडियो के किसी खास पहलू को एडिट करते समय, विज़ुअल कंसिस्टेंसी बनाए रखने के लिए, `"Keep everything else the same"` शामिल करें.

यहां कुछ उदाहरण दिए गए हैं, जिनसे पता चलता है कि इस तकनीक को कैसे लागू किया जाता है:

- **ऐसा करने से बचें:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **आसान बनाएं:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **ऐसा करने से बचें:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **आसान बनाएं:** `Make the phone invisible. Keep everything else the
    same.`

### ऑडियो के लिए प्रॉम्प्ट

डिफ़ॉल्ट रूप से, मॉडल किसी वीडियो के लिए सही ऑडियो ट्रैक जनरेट करने की कोशिश करेगा. यह हमेशा आपकी ज़रूरत के हिसाब से नहीं हो सकता. प्रॉम्प्ट का इस्तेमाल करके, यह बताया जा सकता है कि आपको किस तरह का ऑडियो चाहिए. अगर आपको अपने वीडियो में संगीत चाहिए, तो यह खास तौर पर ज़रूरी है:

- शांत बैकग्राउंड संगीत शामिल करें
- वीडियो में हाई एनर्जी वाला टेक्नो बीट है
- ऑडियो, बैकग्राउंड में बजने वाला कम क्वालिटी वाला रेडियो ब्रॉडकास्ट है, जिसमें एक गाना बज रहा है

### इवेंट का समय तय करना

वीडियो में किसी खास समय पर होने वाली चीज़ों के लिए प्रॉम्प्ट दिया जा सकता है. इसके लिए, सटीक सिंटैक्स की ज़रूरत नहीं होती. साथ ही, नैचुरल लैंग्वेज का इस्तेमाल किया जा सकता है. यह सुविधा, सीन कट, रिदम या रैपिड फ़ायर सीक्वेंस बनाने में खास तौर पर काम आती है.
उदाहरण के लिए, यह देखें:

- तीन सेकंड बाद, एक महिला सीन में आती है.
- पांचवें सेकंड पर, बैकग्राउंड ऑडियो में कोरस शुरू होता है.
- हर दो सेकंड में, नया फ़्रेम दिखाएं.
- रैपिड फ़ायर सीक्वेंस में, हर आधे सेकंड (24fps पर 12 फ़्रेम) में सीन को नई जगह पर बदलें.

टाइमकोड सिंटैक्स का भी इस्तेमाल किया जा सकता है:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### मेटा प्रॉम्प्टिंग

Gemini Omni Flash से, वीडियो जनरेट करने की सामान्य क्वालिटी या सिद्धांतों पर ध्यान देने के लिए कहा जा सकता है:

- बहुत ज़्यादा जानकारी वाला, लेकिन पूरी तरह से असली दिखने वाला सीन बनाने के लिए, माइक्रो-डिटेल, एक्सप्रेशन, और टाइमिंग का ध्यान रखें.
- किरदारों और एनवायरमेंट के ब्यौरे में ज़्यादा से ज़्यादा जानकारी दें.
  किरदारों पर कॉस्ट्यूम डिज़ाइन के सिद्धांत लागू करें. सीन में मौजूद लोगों, आइटम, और ऑब्जेक्ट के बारे में साफ़ तौर पर जानकारी दें.
- सीन को असली और नैचुरल दिखाने के लिए, बैकग्राउंड एलिमेंट में सही जानकारी शामिल करें.
- रैपिड फ़ायर वीडियो बनाएं, जिसमें हर एक सेकंड में एक अलग और दुर्लभ `[thing]` दिखे. इसमें अपबीट संगीत शामिल करें. साथ ही, चीज़ को लेबल करने के लिए टेक्स्ट शामिल करें.

### वीडियो में टेक्स्ट

वीडियो में टेक्स्ट शामिल करने के लिए प्रॉम्प्ट दिया जा सकता है. Gemini Omni, टेक्स्ट को सही और पढ़ने लायक तरीके से रेंडर करेगा. अगर आपके वीडियो में नैचुरल तरीके से टेक्स्ट दिखेगा, तो यह तय करने में मदद मिल सकती है कि उसे क्या कहना चाहिए. भले ही, यह टेक्स्ट बैकग्राउंड एलिमेंट में हो.

- स्क्रीन पर एक बार में एक शब्द: "did, you, know, that, Omni, can, do, awesome, text?" हर शब्द, एक सेकंड के लिए अलग-अलग ऐनिमेटेड स्टाइल में दिखता है. कोई डायलॉग नहीं.
- सड़क पर एक साइन है, जिस पर लिखा है: "This is an AI generation by Omni". एक स्टोरफ़्रंट है, जिस पर लिखा है: "All you need AI". एक कार है, जिसकी नंबर प्लेट पर लिखा है: "OMN111"

### इमेज के रोल सेट करने के लिए, प्रॉम्प्ट में टैग का इस्तेमाल करना

अपलोड किए गए मीडिया को जनरेशन के खास रोल से बाइंड करने के लिए, टैग का इस्तेमाल किया जा सकता है. इससे, यह तय किया जा सकता है कि हर इमेज, शुरुआती फ़्रेम है या रेफ़रंस.

#### 1. सामान्य टैग (सुझाया गया)

ऐसे सामान्य मामलों में जहां प्रॉम्प्ट से इमेज के रोल साफ़ तौर पर पता चलते हैं, वहां इमेज को सीधे रोल से बाइंड किया जा सकता है:

- **`<FIRST_FRAME>`**: वीडियो के शुरुआती फ़्रेम के तौर पर इमेज का इस्तेमाल करें. उदाहरण के लिए: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: रेफ़रंस के तौर पर इमेज का इस्तेमाल करें. उदाहरण के लिए: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (पहली इमेज से स्टाइल
  रेफ़रंस और दूसरी इमेज से सब्जेक्ट रेफ़रंस को जोड़ता है).
  इमेज रेफ़रंस की शुरुआत 0 से होती है.

यहां छह रेफ़रंस इमेज वाला उदाहरण दिया गया है:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. साफ़ तौर पर एलान

एक से ज़्यादा इमेज और एक से ज़्यादा रोल वाले ज़्यादा मुश्किल मामलों के लिए, नैचुरल लैंग्वेज वाले निर्देश सफ़िक्स के साथ, साफ़ तौर पर प्रीफ़िक्स टैग का इस्तेमाल किया जा सकता है.

- **सोर्स और रेफ़रंस इमेज का एलान करना**:
  - `[# Sources <FIRST_FRAME>@Image1]` पहली इमेज को शुरुआती फ़्रेम के तौर पर इस्तेमाल करेगा.
  - `[# References <IMAGE_REF_0>@Image1]` पहली इमेज को रेफ़रंस के तौर पर इस्तेमाल करेगा.
  - `[# References <IMAGE_REF_1>@Image2]` दूसरी इमेज को रेफ़रंस के तौर पर इस्तेमाल करेगा.
  - `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` दोनों इमेज को रेफ़रंस के तौर पर इस्तेमाल करेगा.
  - `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` पहली इमेज को शुरुआती फ़्रेम के तौर पर और दूसरी इमेज को रेफ़रंस के तौर पर इस्तेमाल करेगा.
- **निर्देश**: अपने प्रॉम्प्ट के आखिर में निर्देश जोड़ें:
  - शुरुआती फ़्रेम के लिए: `"Use this image as the starting frame."`
  - रेफ़रंस इमेज के लिए: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

प्रॉम्प्ट का बड़ा उदाहरण:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## आगे क्या करना है

- [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=hi) में एक्सपेरिमेंट करके, Gemini Omni Flash का इस्तेमाल शुरू करें.
- प्रॉम्प्ट डिज़ाइन के बारे में जानकारी देने वाले हमारे [लेख](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=hi) की मदद से, और भी बेहतर प्रॉम्प्ट लिखने का तरीका जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
