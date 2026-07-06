---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=hi
fetched_at: 2026-07-06T05:19:55.276213+00:00
title: "\u0936\u0941\u0930\u0942 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# शुरू करना

इस गाइड में, [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) का इस्तेमाल करके, Gemini API को शुरू करने के बारे में बताया गया है. इसमें एक मिनट से भी कम समय में, पहला एपीआई कॉल किया जा सकेगा. साथ ही, टेक्स्ट जनरेट करने, मल्टीमॉडल को समझने, इमेज जनरेट करने, स्ट्रक्चर्ड आउटपुट, टूल, फ़ंक्शन कॉल करने, एजेंट, और बैकग्राउंड में प्रोसेस करने के बारे में जानकारी मिलेगी.

Interactions API, [Python](https://github.com/googleapis/python-genai) और [JavaScript](https://github.com/googleapis/js-genai) SDK के साथ-साथ REST के ज़रिए उपलब्ध है.

## 1. एपीआई पासकोड पाना

Gemini API का इस्तेमाल करने के लिए, आपके पास एक एपीआई पासकोड होना चाहिए. इससे आपके अनुरोधों की पुष्टि की जा सकेगी, सुरक्षा से जुड़ी सीमाओं को लागू किया जा सकेगा, और आपके खाते के इस्तेमाल को ट्रैक किया जा सकेगा.

- Google AI Studio, नए उपयोगकर्ताओं के लिए प्रोजेक्ट और एपीआई पासकोड अपने-आप बना देता है.
  इसे [एपीआई पासकोड पेज](https://aistudio.google.com/api-keys?hl=hi) से कॉपी किया जा सकता है.
- अगर आपको नई कुंजी चाहिए, तो AI Studio में **एपीआई पासकोड बनाएं** पर क्लिक करें. इसके बाद, नई कुंजी-प्रोजेक्ट का जोड़ा जोड़ने के लिए, डायलॉग बॉक्स में दिए गए निर्देशों का पालन करें.

[Gemini API पासकोड बनाना](https://aistudio.google.com/apikey?hl=hi)

अपनी कुंजी को एनवायरमेंट वैरिएबल के तौर पर सेट करें:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### पैसे चुकाकर इस्तेमाल किए जाने वाले टियर पर अपग्रेड करना

पैसे चुकाकर इस्तेमाल किए जाने वाले टियर पर अपग्रेड करने से, अनुरोध करने की सीमा बढ़ जाती है. इसके लिए, Cloud Billing सेट अप करना ज़रूरी है.

- AI Studio के [एपीआई पासकोड](https://aistudio.google.com/api-keys?hl=hi) या [प्रोजेक्ट](https://aistudio.google.com/projects?hl=hi) पेजों पर, **बिलिंग सेट अप करें** पर क्लिक करें.
- बिलिंग खाता बनाने या लिंक करने के लिए, Cloud Billing डायलॉग बॉक्स में दिए गए निर्देशों का पालन करें. साथ ही, पेमेंट का तरीका जोड़ें और कम से कम 10 डॉलर (या मुद्रा के हिसाब से इसके बराबर) के पेड क्रेडिट के लिए पहले से पेमेंट करें.
- [Google AI Studio](https://aistudio.google.com/usage?hl=hi) में, **डैशबोर्ड** > **इस्तेमाल** में जाकर, एपीआई के इस्तेमाल की जानकारी देखें.

ज़्यादा जानकारी के लिए, [बिलिंग पेज](https://ai.google.dev/gemini-api/docs/billing?hl=hi) देखें.

## 2. एसडीके टूल इंस्टॉल करना और पहली कॉल करना

एसडीके इंस्टॉल करें और एक एपीआई कॉल से टेक्स्ट जनरेट करें.

### Python

एसडीके टूल इंस्टॉल करें:

```
pip install -U google-genai
```

क्लाइंट शुरू करें और अनुरोध करें:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

एसडीके टूल इंस्टॉल करें:

```
npm install @google/genai
```

क्लाइंट शुरू करें और अनुरोध करें:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**जवाब:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

REST का इस्तेमाल करने पर, एपीआई पूरा `Interaction` रिसॉर्स दिखाता है. इसमें मेटाडेटा, इस्तेमाल के आंकड़े, और बातचीत के हर चरण का इतिहास शामिल होता है.

एसडीके, पूरा जवाब दिखाते हैं. साथ ही, ये सीधे तौर पर फ़ाइनल आउटपुट को ऐक्सेस करने के लिए, `interaction.output_text` और `interaction.output_image` जैसी सुविधाएं भी देते हैं. [इंटरैक्शन की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) में, रिस्पॉन्स के स्ट्रक्चर के बारे में ज़्यादा जानें. इसके अलावा, सिस्टम के निर्देशों और जनरेशन कॉन्फ़िगरेशन के बारे में जानकारी पाने के लिए, [टेक्स्ट जनरेट करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi) पढ़ें.

## 3. जवाब को स्ट्रीम करना

बेहतर इंटरैक्शन के लिए, जवाब जनरेट होते ही उसे स्ट्रीम करें. हर `step.delta` इवेंट, टेक्स्ट का एक हिस्सा डिलीवर करता है. इसे तुरंत दिखाया जा सकता है.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

स्ट्रीमिंग के दौरान, सर्वर, सर्वर-सेंट इवेंट (एसएसई) की स्ट्रीम के साथ जवाब देता है. हर इवेंट में एक टाइप और JSON डेटा शामिल होता है.

**जवाब:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

स्ट्रीमिंग इवेंट और डेल्टा टाइप को मैनेज करने के बारे में ज़्यादा जानने के लिए, [स्ट्रीमिंग इंटरैक्शन गाइड](https://ai.google.dev/gemini-api/docs/streaming?hl=hi) देखें.

## 4. सिलसिलेवार बातचीत

Interactions API, बातचीत को कई चरणों में पूरा करने की सुविधा देता है. इसके लिए, ये दो तरीके इस्तेमाल किए जाते हैं:

- **स्टेटफ़ुल (सुझाया गया)**: `previous_interaction_id` का इस्तेमाल करके, सर्वर पर बातचीत जारी रखें. यह ज़्यादातर चैट और एजेंटिक वर्कफ़्लो के लिए सबसे सही है. इनमें आपको सर्वर से इतिहास को मैनेज करने और कैश मेमोरी को ऑप्टिमाइज़ करने की ज़रूरत होती है.
- **स्टेटलेस**: क्लाइंट पर बातचीत के इतिहास को मैनेज करें. इसके लिए, हर अनुरोध में पिछले सभी टर्न (इसमें इंटरमीडिएट मॉडल थॉट और टूल के चरण शामिल हैं) पास करें.

### स्टेटफ़ुल (सुझाया गया)

`previous_interaction_id` पास करके, इंटरैक्शन को एक-दूसरे से जोड़ें. सर्वर, आपकी पूरी बातचीत के इतिहास को मैनेज करता है.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### स्टेटलेस

क्लाइंट-साइड पर `store=false` सेट अप करें और बातचीत के इतिहास को मैनेज करें. आपको मॉडल से जनरेट किए गए सभी चरणों (`thought` और `function_call` चरणों सहित) को उसी तरह से सेव करके फिर से भेजना होगा जिस तरह से वे आपको मिले थे.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.5-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**जवाब:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

दूसरे इंटरैक्शन में, जवाब के तौर पर पूरा ऑब्जेक्ट मिलता है. इसमें सिर्फ़ नए चरण शामिल होते हैं. हालांकि, यह पिछले टर्न के कॉन्टेक्स्ट पर आधारित होता है. [सिलसिलेवार बातचीत से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#multi-turn-conversations) में, स्टेट बनाए रखने के बारे में ज़्यादा जानें. इसके अलावा, क्लाइंट-साइड पर इतिहास को मैनेज करने के लिए, [स्टेटलेस मोड](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#stateless-conversations) के बारे में जानें.

## 5. अलग-अलग सोर्स से जानकारी समझने की क्षमता

Gemini मॉडल, इमेज, ऑडियो, वीडियो, और दस्तावेज़ों को आसानी से समझ सकते हैं. एक ही अनुरोध में टेक्स्ट के साथ-साथ मीडिया भी पास करें.

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**जवाब:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

[इमेज समझने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi) में जाकर, इमेज, वीडियो, और ऑडियो फ़ाइलें पास करने का तरीका जानें.

[hearing

ऑडियो को समझना

ऑडियो फ़ाइलों को टेक्स्ट में बदलें, उनकी खास जानकारी पाएं या उनसे जुड़े सवालों के जवाब पाएं.](https://ai.google.dev/gemini-api/docs/audio?hl=hi)
[videocam

वीडियो को समझना

वीडियो कॉन्टेंट का विश्लेषण करना, इवेंट का पता लगाना, और कार्रवाइयों के बारे में बताना.](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi)
[description

दस्तावेज़ों को प्रोसेस करना

PDF और अन्य दस्तावेज़ फ़ॉर्मैट से जानकारी निकालें.](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi)

## 6. मल्टीमॉडल जनरेशन

Gemini, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) इमेज मॉडल का इस्तेमाल करके, इमेज जनरेट कर सकता है.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**जवाब:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

जब मॉडल कोई इमेज जनरेट करता है, तो वह `steps` ऐरे में मौजूद किसी चरण में, base64-encoded इमेज डेटा दिखाता है. साथ ही, `output_image` प्रॉपर्टी के ज़रिए भी यह डेटा दिखाता है. आसपेक्ट रेशियो, इमेज में बदलाव करने, और रेफ़रंस के बारे में जानने के लिए, [इमेज जनरेट करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) देखें.

[record\_voice\_over

लिखे गए शब्दों को बोली में बदलने की सुविधा

Gemini 3.1 Flash TTS की मदद से, अलग-अलग आवाज़ों में बोलकर जानकारी जनरेट करें.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi)
[music\_note

संगीत जनरेट करने की सुविधा

Lyria 3 की मदद से, क्लिप और पूरी अवधि के गाने बनाएँ.](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi)

## 7. स्ट्रक्चर्ड आउटपुट का इस्तेमाल करना

मॉडल को इस तरह कॉन्फ़िगर करें कि वह आपके तय किए गए स्कीमा से मेल खाने वाला JSON जवाब दे. स्ट्रक्चर्ड आउटपुट, [Pydantic](https://docs.pydantic.dev/latest/) (Python) और [Zod](https://zod.dev/) (JavaScript) के साथ काम करता है.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**जवाब:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

आउटपुट टेक्स्ट ब्लॉक में, मान्य JSON स्ट्रिंग मौजूद है. यह स्ट्रिंग, अनुरोध किए गए स्कीमा के मुताबिक है. ज़्यादा जटिल स्ट्रक्चर और रिकर्सिव स्कीमा तय करने का तरीका जानने के लिए, [स्ट्रक्चर्ड आउटपुट गाइड](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) देखें.

## 8. टूल इस्तेमाल करना

Google Search की मदद से, मॉडल के जवाब में रीयल-टाइम की जानकारी शामिल करना. यह एपीआई, अपने-आप खोज करता है, नतीजों को प्रोसेस करता है, और उद्धरण दिखाता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**जवाब:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

खोज के चरणों के बारे में, इंटरैक्शन के इतिहास में पूरी जानकारी दी गई है. साथ ही, फ़ाइनल आउटपुट में वेब सोर्स की ओर इशारा करने वाले इनलाइन उद्धरण शामिल हैं.

[Google Search के जवाब में शामिल उद्धरणों को निकालने के तरीके के बारे में जानने के लिए, Google Search के जवाब में शामिल उद्धरणों के बारे में जानकारी देने वाली गाइड](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) पढ़ें. इसके अलावा, [एक से ज़्यादा टूल को एक साथ इस्तेमाल करने के तरीके के बारे में जानकारी देने वाली गाइड](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पढ़ें.

[code

कोड एक्ज़ीक्यूट करना

सुरक्षित सैंडबॉक्स वाले Borg एनवायरमेंट में Python कोड चलाएं.](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi)
[link

यूआरएल का कॉन्टेक्स्ट

वेबपेज के कॉन्टेंट में जवाबों को आधार देने के लिए, सार्वजनिक वेब यूआरएल सीधे तौर पर पास करें.](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)
[search

फ़ाइल खोजना

अपलोड किए गए दस्तावेज़ों और मीडिया फ़ाइलों को इंडेक्स करना और उनमें खोजना.](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)
[map

Google Maps

जवाबों में, असल दुनिया के जियोस्पेशल और जगह की जानकारी का डेटा शामिल करें.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)
[computer

कंप्यूटर का इस्तेमाल

ब्राउज़र ऑटोमेशन और स्क्रीन इंटरैक्शन.](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi)

## 9. अपने फ़ंक्शन कॉल करना

फ़ंक्शन कॉलिंग की सुविधा की मदद से, मॉडल को अपने कोड से कनेक्ट किया जा सकता है. आपको फ़ंक्शन का नाम और पैरामीटर तय करने होते हैं. मॉडल यह तय करता है कि इसे कब कॉल करना है और स्ट्रक्चर्ड आर्ग्युमेंट दिखाता है. इसके बाद, आपको इसे स्थानीय तौर पर लागू करना होता है और नतीजे वापस भेजने होते हैं.

### स्टेटफ़ुल (सुझाया गया)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### स्टेटलेस

स्टेटलेस मोड में फ़ंक्शन कॉलिंग का इस्तेमाल भी किया जा सकता है. इसके लिए, क्लाइंट साइड पर बातचीत के इतिहास को मैनेज करें और `store=false` सेट करें. स्टेटलेस मोड में, आपको हर अनुरोध के `input` फ़ील्ड में बातचीत का पूरा इतिहास पास करना होगा. इस इतिहास में यह जानकारी शामिल होनी चाहिए:

1. शुरुआती `user_input` चरण.
2. पहले राउंड में मॉडल से जनरेट किए गए सभी चरणों को, ठीक उसी तरह दिखाया गया है जिस तरह से वे मिले थे. इनमें `thought` और `function_call` चरण भी शामिल हैं.
3. `function_result` चरण में, आपके लागू किए गए फ़ंक्शन का आउटपुट शामिल होता है.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**जवाब:**

पहले टर्न के दौरान, मॉडल `requires_action` स्टेटस और `function_call` चरण के साथ जवाब देता है:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

फ़ंक्शन को स्थानीय तौर पर चलाने और नतीजे सबमिट करने (दूसरा टर्न) के बाद, पूरा किया गया फ़ाइनल इंटरैक्शन यह दिखता है:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

पैरलल फ़ंक्शन कॉलिंग या फ़ंक्शन चुनने के मोड जैसी ऐडवांस सुविधाओं के बारे में जानने के लिए, [फ़ंक्शन कॉलिंग गाइड](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) देखें.

## 10. मैनेज किए जा रहे एजेंट को चलाना

मैनेज किए गए एजेंट, रिमोट सैंडबॉक्स में चलते हैं. इनके पास कोड एक्ज़ीक्यूशन और फ़ाइल मैनेजमेंट जैसे टूल का ऐक्सेस होता है. `model` के बजाय `agent` पास करें और `environment="remote"` सेट करें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

आपके पास अपने निर्देशों, कौशल, और डेटा सोर्स के साथ [कस्टम एजेंट](https://ai.google.dev/gemini-api/docs/custom-agents?hl=hi) को तय करने और सेव करने का विकल्प भी होता है.

[rocket\_launch

क्विकस्टार्ट

पहला एजेंट कॉल करें, जवाब स्ट्रीम करें, और कस्टम एजेंट बनाएं.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi)
[smart\_toy

Antigravity एजेंट

डिफ़ॉल्ट एजेंट के लिए केपबिलिटी, टूल, मल्टीमॉडल इनपुट, और कीमत.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi)
[experiment

AI Studio में एजेंट

बिना कोड लिखे एजेंट के प्रोटोटाइप बनाने के लिए विज़ुअल प्लेग्राउंड.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=hi)

## 11. बैकग्राउंड में टास्क चलाने की अनुमति

लंबे समय तक चलने वाले टास्क को एसिंक्रोनस तरीके से चलाने के लिए, `background=True` को सेट करें. `interactions.get()` के साथ नतीजों के लिए पोल. ज़्यादा जानकारी के लिए, [बैकग्राउंड में टास्क पूरा करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi) देखें.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**जवाब:**

शुरुआती रिस्पॉन्स, `in_progress` स्टेटस के साथ तुरंत दिखता है:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.5-flash"
}
```

बैकग्राउंड टास्क पूरी तरह से लागू होने के बाद, इंटरैक्शन की स्थिति की जांच करने पर यह दिखता है:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.5-flash",
}
```

[बैकग्राउंड में प्रोसेस करने से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi) में, मॉडल और एजेंट को एसिंक्रोनस तरीके से चलाने के बारे में पढ़ें.

## आगे क्या करना है

- [बैकग्राउंड में प्रोसेस करना](https://ai.google.dev/gemini-api/docs/background-execution?hl=hi): लंबे समय तक चलने वाले टास्क को एसिंक्रोनस तरीके से चलाएं और उनकी स्थिति मैनेज करें.
- [टेक्स्ट जनरेट करना](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi): सिस्टम के निर्देश, जनरेशन कॉन्फ़िगरेशन, और टेक्स्ट के अडवांस पैटर्न.
- [इमेज जनरेट करना](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi): आसपेक्ट रेशियो, इमेज में बदलाव करना, और स्टाइल के रेफ़रंस.
- [इमेज को समझना](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi): इमेज को कैटगरी में बांटना, ऑब्जेक्ट का पता लगाना, और इमेज के बारे में सवाल-जवाब.
- [सोचना](https://ai.google.dev/gemini-api/docs/thinking?hl=hi): मुश्किल टास्क के लिए, सोच-समझकर एक-एक करके जवाब देना.
- [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi): पैरलल, कंपोज़िशनल, और कंस्ट्रेंट फ़ंक्शन मोड.
- [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi): जवाब में भरोसेमंद सोर्स से जानकारी लेना, जवाब में उद्धरण जोड़ना, और खोज सुझाव.
- [मैनेज किए गए एजेंट](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi): ये पहले से बनाए गए एजेंट होते हैं. इनमें कोड एक्ज़ीक्यूट करने और फ़ाइल मैनेज करने की सुविधा होती है.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi): यह सुविधा, कई चरणों में अपने-आप रिसर्च करती है. साथ ही, रिसर्च के लिए प्लान बनाती है और जानकारी को व्यवस्थित करती है.
- [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi): JSON स्कीमा, enum, और रिकर्सिव टाइप की परिभाषाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-01 (UTC) को अपडेट किया गया."],[],[]]
