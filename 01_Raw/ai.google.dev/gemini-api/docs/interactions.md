---
source_url: https://ai.google.dev/gemini-api/docs/interactions?hl=ar
fetched_at: 2026-05-05T20:49:45.543184+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API

‫Interactions API ([إصدار تجريبي](https://ai.google.dev/gemini-api/docs/api-versions?hl=ar)) هي واجهة موحّدة للتفاعل مع نماذج Gemini وبرامج Gemini الآلية. وهي بديل محسّن لواجهة برمجة التطبيقات [`generateContent`](https://ai.google.dev/api/generate-content?hl=ar#method:-models.generatecontent)، وتسهّل إدارة الحالة وتنظيم الأدوات والمهام الطويلة الأمد. للحصول على عرض شامل لمخطط واجهة برمجة التطبيقات، يُرجى الاطّلاع على [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). أثناء الإصدار التجريبي، قد تحدث [تغييرات غير متوافقة](#breaking-changes) في الميزات والمخططات.
للبدء بسرعة، جرِّب [دفتر ملاحظات التشغيل السريع لواجهة Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).

الاستخدام العام
استدعاء الدوال البرمجية
وكيل Deep Research

يوضّح المثال التالي كيفية استدعاء Interactions API باستخدام طلب نصي.

### Python

```
from google import genai

client = genai.Client()

interaction =  client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction =  await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a short joke about programming.',
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a short joke about programming."
}'
```

## التفاعلات الأساسية

تتوفّر Interactions API من خلال [حِزم تطوير البرامج (SDK) الحالية](#sdk). أبسط طريقة للتفاعل مع النموذج هي تقديم طلب نصي. يمكن أن يكون `input` سلسلة أو قائمة تتضمّن عناصر محتوى أو قائمة أدوار مع عناصر محتوى.

### Python

```
from google import genai

client = genai.Client()

interaction =  client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction =  await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a short joke about programming.',
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a short joke about programming."
}'
```

## المحادثة

يمكنك إنشاء محادثات متعدّدة الجولات بطريقتَين:

- حفظ الحالة من خلال الرجوع إلى تفاعل سابق
- بدون الاحتفاظ بأي بيانات من خلال تقديم سجلّ المحادثات بالكامل

### محادثة ذات حالة

لمواصلة محادثة، مرِّر `id` من التفاعل السابق إلى المَعلمة `previous_interaction_id`. يتذكّر واجهة برمجة التطبيقات سجلّ المحادثات،
لذلك ما عليك سوى إرسال الإدخال الجديد. للحصول على تفاصيل حول الحقول التي يتم توريثها والحقول التي يجب إعادة تحديدها، اطّلِع على [إدارة الحالة من جهة الخادم](#server-side-state).

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hi, my name is Phil."
)
print(f"Model: {interaction1.outputs[-1].text}")

# 2. Second turn (passing previous_interaction_id)
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is my name?",
    previous_interaction_id=interaction1.id
)
print(f"Model: {interaction2.outputs[-1].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. First turn
const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Hi, my name is Phil.'
});
console.log(`Model: ${interaction1.outputs[interaction1.outputs.length - 1].text}`);

// 2. Second turn (passing previous_interaction_id)
const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is my name?',
    previous_interaction_id: interaction1.id
});
console.log(`Model: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
```

### REST

```
# 1. First turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Hi, my name is Phil."
}'

# 2. Second turn (Replace INTERACTION_ID with the ID from the previous interaction)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "input": "What is my name?",
#     "previous_interaction_id": "INTERACTION_ID"
# }'
```

#### استرداد التفاعلات السابقة التي تتضمّن معلومات الحالة

استخدام التفاعل `id` لاسترداد أدوار المحادثة السابقة

### Python

```
previous_interaction = client.interactions.get("<YOUR_INTERACTION_ID>")

print(previous_interaction)
```

### JavaScript

```
const previous_interaction = await client.interactions.get("<YOUR_INTERACTION_ID>");
console.log(previous_interaction);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/<YOUR_INTERACTION_ID>" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

#### تضمين الإدخال الأصلي

بشكلٍ تلقائي، تعرض الدالة `interactions.get()` نواتج النموذج فقط. لتضمين الإدخال الأصلي الذي تمّت تسويته في الردّ، اضبط `include_input` على `true`.

### Python

```
interaction = client.interactions.get(
    "<YOUR_INTERACTION_ID>",
    include_input=True
)

print(f"Input: {interaction.input}")
print(f"Output: {interaction.outputs}")
```

### JavaScript

```
const interaction = await client.interactions.get(
    "<YOUR_INTERACTION_ID>",
    { include_input: true }
);

console.log(`Input: ${JSON.stringify(interaction.input)}`);
console.log(`Output: ${JSON.stringify(interaction.outputs)}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/<YOUR_INTERACTION_ID>?include_input=true" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

### محادثة بدون حالة

يمكنك إدارة سجلّ المحادثات يدويًا من جهة العميل.

### Python

```
from google import genai

client = genai.Client()

conversation_history = [
    {
        "role": "user",
        "content": "What are the three largest cities in Spain?"
    }
]

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input=conversation_history
)

print(f"Model: {interaction1.outputs[-1].text}")

conversation_history.append({"role": "model", "content": interaction1.outputs})
conversation_history.append({
    "role": "user",
    "content": "What is the most famous landmark in the second one?"
})

interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input=conversation_history
)

print(f"Model: {interaction2.outputs[-1].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const conversationHistory = [
    {
        role: 'user',
        content: "What are the three largest cities in Spain?"
    }
];

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: conversationHistory
});

console.log(`Model: ${interaction1.outputs[interaction1.outputs.length - 1].text}`);

conversationHistory.push({ role: 'model', content: interaction1.outputs });
conversationHistory.push({
    role: 'user',
    content: "What is the most famous landmark in the second one?"
});

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: conversationHistory
});

console.log(`Model: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
```

### REST

```
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
 -H "Content-Type: application/json" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {
            "role": "user",
            "content": "What are the three largest cities in Spain?"
        },
        {
            "role": "model",
            "content": "The three largest cities in Spain are Madrid, Barcelona, and Valencia."
        },
        {
            "role": "user",
            "content": "What is the most famous landmark in the second one?"
        }
    ]
}'
```

## الإمكانات المتعددة الوسائط

يمكنك استخدام Interactions API لحالات الاستخدام المتعدّدة الوسائط، مثل فهم الصور أو إنشاء الفيديوهات.

### فهم المحتوى المتعدد الوسائط

يمكنك تقديم مدخلات متعددة الوسائط كبيانات مضمّنة مرمّزة بـ base64، أو باستخدام Files API للملفات الأكبر حجمًا، أو عن طريق تمرير رابط متاح للجميع في الحقل uri. توضّح عيّنات الرموز البرمجية التالية طريقة استخدام عنوان URL العام.

#### فهم الصور

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Describe the image."},
        {
            "type": "image",
            "uri": "YOUR_URL",
            "mime_type": "image/png"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        {type: 'text', text: 'Describe the image.'},
        {
            type: 'image',
            uri: 'YOUR_URL',
            mime_type: 'image/png'
        }
    ]
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
    {
        "type": "text",
        "text": "Describe the image."
    },
    {
        "type": "image",
        "uri": "YOUR_URL",
        "mime_type": "image/png"
    }
    ]
}'
```

#### فهم الصوت

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What does this audio say?"},
        {
            "type": "audio",
            "uri": "YOUR_URL",
            "mime_type": "audio/wav"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What does this audio say?' },
        {
            type: 'audio',
            uri: 'YOUR_URL',
            mime_type: 'audio/wav'
        }
    ]
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What does this audio say?"},
        {
            "type": "audio",
            "uri": "YOUR_URL",
            "mime_type": "audio/wav"
        }
    ]
}'
```

#### فهم الفيديوهات

### Python

```
from google import genai
client = genai.Client()

print("Analyzing video...")
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is happening in this video? Provide a timestamped summary."},
        {
            "type": "video",
            "uri": "YOUR_URL",
            "mime_type": "video/mp4"
        }
    ]
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

console.log('Analyzing video...');
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What is happening in this video? Provide a timestamped summary.' },
        {
            type: 'video',
            uri: 'YOUR_URL',
            mime_type: 'video/mp4'
        }
    ]
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What is happening in this video?"},
        {
            "type": "video",
            "uri": "YOUR_URL",
            "mime_type": "video/mp4"
        }
    ]
}'
```

#### فهم المستندات (ملف PDF)

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "YOUR_URL",
            "mime_type": "application/pdf"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'YOUR_URL',
            mime_type: 'application/pdf'
        }
    ],
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "YOUR_URL",
            "mime_type": "application/pdf"
        }
    ]
}'
```

### إنشاء محتوى متعدد الوسائط

يمكنك استخدام Interactions API لإنشاء مخرجات متعددة الوسائط.

#### إنشاء الصور

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an image of a futuristic city.",
    response_modalities=["image"]
)

for output in interaction.outputs:
    if output.type == "image":
        print(f"Generated image with mime_type: {output.mime_type}")
        # Save the image
        with open("generated_city.png", "wb") as f:
            f.write(base64.b64decode(output.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-pro-image-preview',
    input: 'Generate an image of a futuristic city.',
    response_modalities: ['image']
});

for (const output of interaction.outputs) {
    if (output.type === 'image') {
        console.log(`Generated image with mime_type: ${output.mime_type}`);
        // Save the image
        fs.writeFileSync('generated_city.png', Buffer.from(output.data, 'base64'));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate an image of a futuristic city.",
    "response_modalities": ["image"]
}'
```

##### ضبط إعدادات إخراج الصور

يمكنك تخصيص الصور التي تم إنشاؤها باستخدام `image_config` ضمن `generation_config`
للتحكّم في نسبة العرض إلى الارتفاع ودرجة الدقة.

| المَعلمة | الخيارات | الوصف |
| --- | --- | --- |
| `aspect_ratio` | ‫`1:1`، `2:3`، `3:2`، `3:4`، `4:3`، `4:5`، `5:4`، `9:16`، `16:9`، `21:9` | تتحكّم هذه السمة في نسبة عرض الصورة الناتجة إلى ارتفاعها. |
| `image_size` | ‫`1k`، `2k`، `4k` | تضبط هذه السمة درجة دقة الصورة الناتجة. |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an image of a futuristic city.",
    generation_config={
        "image_config": {
            "aspect_ratio": "9:16",
            "image_size": "2k"
        }
    }
)

for output in interaction.outputs:
    if output.type == "image":
        print(f"Generated image with mime_type: {output.mime_type}")
        # Save the image
        with open("generated_city.png", "wb") as f:
            f.write(base64.b64decode(output.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-pro-image-preview',
    input: 'Generate an image of a futuristic city.',
    generation_config: {
        image_config: {
            aspect_ratio: '9:16',
            image_size: '2k'
        }
    }
});

for (const output of interaction.outputs) {
    if (output.type === 'image') {
        console.log(`Generated image with mime_type: ${output.mime_type}`);
        // Save the image
        fs.writeFileSync('generated_city.png', Buffer.from(output.data, 'base64'));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate an image of a futuristic city.",
    "generation_config": {
        "image_config": {
            "aspect_ratio": "9:16",
            "image_size": "2k"
        }
    }
}'
```

#### إنشاء الكلام

إنشاء كلام يبدو طبيعيًا من نص باستخدام نموذج "تحويل النص إلى كلام"
اضبط إعدادات الصوت واللغة والمكبّر باستخدام المَعلمة `speech_config`.

### Python

```
import base64
from google import genai
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say the following: WOOHOO This is so much fun!. [laughs]",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {
                "language": "en-us",
                "voice": "kore"
            }
        ]
    }
)

for output in interaction.outputs:
    if output.type == "audio":
        print(f"Generated audio with mime_type: {output.mime_type}")
        # Save the audio as wave file to the current directory.
        wave_file("generated_audio.wav", base64.b64decode(output.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
import wav from 'wav';

async function saveWaveFile(
    filename,
    pcmData,
    channels = 1,
    rate = 24000,
    sampleWidth = 2,
) {
    return new Promise((resolve, reject) => {
        const writer = new wav.FileWriter(filename, {
                channels,
                sampleRate: rate,
                bitDepth: sampleWidth * 8,
        });

        writer.on('finish', resolve);
        writer.on('error', reject);

        writer.write(pcmData);
        writer.end();
    });
}

async function main() {
    const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
    const client = new GoogleGenAI({apiKey: GEMINI_API_KEY});

    const interaction = await client.interactions.create({
        model: 'gemini-3.1-flash-tts-preview',
        input: 'Say the following: WOOHOO This is so much fun!.',
        response_modalities: ['audio'],
        generation_config: {
            speech_config: [
                {
                    language: "en-us",
                    voice: "kore"
                }
            ]
        }
    });

    for (const output of interaction.outputs) {
        if (output.type === 'audio') {
            console.log(`Generated audio with mime_type: ${output.mime_type}`);
            const audioBuffer = Buffer.from(output.data, 'base64');
            // Save the audio as wave file to the current directory
            await saveWaveFile("generated_audio.wav", audioBuffer);
        }
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say the following: WOOHOO This is so much fun!.",
    "response_modalities": ["audio"],
    "generation_config": {
        "speech_config": [
            {
                "language": "en-us",
                "voice": "kore"
            }
        ]
    }
}' | jq -r '.outputs[] | select(.type == "audio") | .data' | base64 -d > generated_audio.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i generated_audio.pcm generated_audio.wav
```

لا تتيح ميزة "تحويل النص إلى كلام" البث.

##### إنشاء محتوى صوتي لعدة متحدثين

إنشاء محتوى صوتي يتضمّن عدة متحدثين من خلال تحديد أسماء المتحدثين في الطلب
ومطابقتها في `speech_config`

يجب أن يتضمّن الطلب أسماء المتحدثين:

```
TTS the following conversation between Alice and Bob:
Alice: Hi Bob, how are you doing today?
Bob: I'm doing great, thanks for asking! How about you?
Alice: Fantastic! I just learned about the Gemini API.
```

بعد ذلك، اضبط `speech_config` باستخدام مكبّرات صوت متوافقة:

```
"generation_config": {
    "speech_config": [
        {"voice": "Zephyr", "speaker": "Alice", "language": "en-US"},
        {"voice": "Puck", "speaker": "Bob", "language": "en-US"}
    ]
}
```

#### إنشاء الموسيقى

إنشاء موسيقى عالية الجودة من الطلبات النصية باستخدام نماذج Lyria 3 تتيح واجهة Interactions API استخدام مقاطع قصيرة وأغانٍ كاملة تتضمّن مقاطع صوتية وكلمات وترتيبات موسيقية.

للحصول على دليل كامل حول إنشاء الموسيقى، بما في ذلك الكلمات المخصّصة والتحكّم في التوقيت وتحويل الصور إلى موسيقى، يُرجى الاطّلاع على [إنشاء الموسيقى باستخدام Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="Create a 30-second cheerful acoustic folk song with "
          "guitar and harmonica.",
)

for output in interaction.outputs:
    if output.type == "audio":
        print(f"Generated audio with mime_type: {output.mime_type}")
        with open("music.mp3", "wb") as f:
            f.write(base64.b64decode(output.data))
    elif output.type == "text":
        print(f"Lyrics: {output.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'Create a 30-second cheerful acoustic folk song with ' +
           'guitar and harmonica.',
});

for (const output of interaction.outputs) {
    if (output.type === 'audio') {
        console.log(`Generated audio with mime_type: ${output.mime_type}`);
        fs.writeFileSync('music.mp3', Buffer.from(output.data, 'base64'));
    } else if (output.type === 'text') {
        console.log(`Lyrics: ${output.text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "Create a 30-second cheerful acoustic folk song with guitar and harmonica."
}'
```

لإنشاء أغانٍ كاملة (تصل مدتها إلى 4 دقائق تقريبًا)، استخدِم نموذج `lyria-3-pro-preview`:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. "
          "Starts with a solo piano intro, builds through sweeping "
          "strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'An epic cinematic orchestral piece about a journey home. ' +
           'Starts with a solo piano intro, builds through sweeping ' +
           'strings, and climaxes with a massive wall of sound.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."
}'
```

## إمكانات بالذكاء الاصطناعي الوكيل

تم تصميم Interactions API لإنشاء الوكلاء والتفاعل معهم، وهي تتضمّن ميزات استدعاء الدوال والأدوات المضمّنة والمخرجات المنظَّمة وبروتوكول سياق النموذج (MCP).

### الوكلاء

يمكنك استخدام وكلاء متخصصين، مثل `deep-research-preview-04-2026`، لتنفيذ المهام المعقّدة. لمزيد من المعلومات حول "وكيل Deep Research" في Gemini، يُرجى الاطّلاع على دليل [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar).

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the Deep Research Agent
initial_interaction = client.interactions.create(
    input="Research the history of the Google TPUs with a focus on 2025 and 2026.",
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started. Interaction ID: {initial_interaction.id}")

# 2. Poll for results
while True:
    interaction = client.interactions.get(initial_interaction.id)
    print(f"Status: {interaction.status}")

    if interaction.status == "completed":
        print("\nFinal Report:\n", interaction.outputs[-1].text)
        break
    elif interaction.status in ["failed", "cancelled"]:
        print(f"Failed with status: {interaction.status}")
        break

    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Start the Deep Research Agent
const initialInteraction = await client.interactions.create({
    input: 'Research the history of the Google TPUs with a focus on 2025 and 2026.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started. Interaction ID: ${initialInteraction.id}`);

// 2. Poll for results
while (true) {
    const interaction = await client.interactions.get(initialInteraction.id);
    console.log(`Status: ${interaction.status}`);

    if (interaction.status === 'completed') {
        console.log('\nFinal Report:\n', interaction.outputs[interaction.outputs.length - 1].text);
        break;
    } else if (['failed', 'cancelled'].includes(interaction.status)) {
        console.log(`Failed with status: ${interaction.status}`);
        break;
    }

    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the Deep Research Agent
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of the Google TPUs with a focus on 2025 and 2026.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID with the ID from the previous interaction)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### الأدوات واستدعاء الدوال

يوضّح هذا القسم كيفية استخدام ميزة "استدعاء الدوال" لتحديد أدوات مخصّصة وكيفية استخدام أدوات Google المضمّنة ضمن Interactions API.

#### استدعاء الدالة

### Python

```
from google import genai

client = genai.Client()

# 1. Define the tool
def get_weather(location: str):
    """Gets the weather for a given location."""
    return f"The weather in {location} is sunny."

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
        },
        "required": ["location"]
    }
}

# 2. Send the request with tools
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool]
)

# 3. Handle the tool call
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Tool Call: {output.name}({output.arguments})")
        # Execute tool
        result = get_weather(**output.arguments)

        # Send result back
        interaction = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": result
            }]
        )
        print(f"Response: {interaction.outputs[-1].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Define the tool
const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

// 2. Send the request with tools
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool]
});

// 3. Handle the tool call
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Tool Call: ${output.name}(${JSON.stringify(output.arguments)})`);

        // Execute tool (Mocked)
        const result = `The weather in ${output.arguments.location} is sunny.`;

        // Send result back
        interaction = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id:interaction.id,
            input: [{
                type: 'function_result',
                name: output.name,
                call_id: output.id,
                result: result
            }]
        });
        console.log(`Response: ${interaction.outputs[interaction.outputs.length - 1].text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
            },
            "required": ["location"]
        }
    }]
}'

# Handle the tool call and send result back (Replace INTERACTION_ID and CALL_ID)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "previous_interaction_id": "INTERACTION_ID",
#     "input": [{
#         "type": "function_result",
#         "name": "get_weather",
#         "call_id": "FUNCTION_CALL_ID",
#         "result": "The weather in Paris is sunny."
#     }]
# }'
```

##### استدعاء الدالة مع الحالة من جهة العميل

إذا كنت لا تريد استخدام الحالة من جهة الخادم، يمكنك إدارة كل ذلك من جهة العميل.

### Python

```
from google import genai
client = genai.Client()

functions = [
    {
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
            "type": "object",
            "properties": {
                "attendees": {"type": "array", "items": {"type": "string"}},
                "date": {"type": "string", "description": "Date of the meeting (e.g., 2024-07-29)"},
                "time": {"type": "string", "description": "Time of the meeting (e.g., 15:00)"},
                "topic": {"type": "string", "description": "The subject of the meeting."},
            },
            "required": ["attendees", "date", "time", "topic"],
        },
    }
]

history = [{"role": "user","content": [{"type": "text", "text": "Schedule a meeting for 2025-11-01 at 10 am with Peter and Amir about the Next Gen API."}]}]

# 1. Model decides to call the function
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=history,
    tools=functions
)

# add model interaction back to history
history.append({"role": "model", "content": interaction.outputs})

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name} with arguments {output.arguments}")

        # 2. Execute the function and get a result
        # In a real app, you would call your function here.
        # call_result = schedule_meeting(**json.loads(output.arguments))
        call_result = "Meeting scheduled successfully."

        # 3. Send the result back to the model
        history.append({"role": "user", "content": [{"type": "function_result", "name": output.name, "call_id": output.id, "result": call_result}]})

        interaction2 = client.interactions.create(
            model="gemini-3-flash-preview",
            input=history,
        )
        print(f"Final response: {interaction2.outputs[-1].text}")
    else:
        print(f"Output: {output}")
```

### JavaScript

```
// 1. Define the tool
const functions = [
    {
        type: 'function',
        name: 'schedule_meeting',
        description: 'Schedules a meeting with specified attendees at a given time and date.',
        parameters: {
            type: 'object',
            properties: {
                attendees: { type: 'array', items: { type: 'string' } },
                date: { type: 'string', description: 'Date of the meeting (e.g., 2024-07-29)' },
                time: { type: 'string', description: 'Time of the meeting (e.g., 15:00)' },
                topic: { type: 'string', description: 'The subject of the meeting.' },
            },
            required: ['attendees', 'date', 'time', 'topic'],
        },
    },
];

const history = [
    { role: 'user', content: [{ type: 'text', text: 'Schedule a meeting for 2025-11-01 at 10 am with Peter and Amir about the Next Gen API.' }] }
];

// 2. Model decides to call the function
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: history,
    tools: functions
});

// add model interaction back to history
history.push({ role: 'model', content: interaction.outputs });

for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Function call: ${output.name} with arguments ${JSON.stringify(output.arguments)}`);

        // 3. Send the result back to the model
        history.push({ role: 'user', content: [{ type: 'function_result', name: output.name, call_id: output.id, result: 'Meeting scheduled successfully.' }] });

        const interaction2 = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            input: history,
        });
        console.log(`Final response: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
    }
}
```

##### نتائج الدالة المتعددة الوسائط

يقبل الحقل `result` في `function_result` إما سلسلة عادية أو مصفوفة من عناصر `TextContent` و`ImageContent`. يتيح لك ذلك عرض صور، مثل لقطات الشاشة أو الرسوم البيانية، إلى جانب النص من استدعاءات الدوال، ما يتيح للنموذج التفكير في الناتج المرئي.

### Python

```
import base64
from google import genai

client = genai.Client()

functions = [
    {
        "type": "function",
        "name": "take_screenshot",
        "description": "Takes a screenshot of a specified website.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The URL to take a screenshot of."},
            },
            "required": ["url"],
        },
    }
]

# 1. Model decides to call the function
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you take a screenshot of https://google.com and tell me what you see?",
    tools=functions
)

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name}({output.arguments})")

        # 2. Execute the function and load the image
        # Replace with actual function call, pseudo code for reading image from disk
        with open("screenshot.png", "rb") as f:
            base64_image = base64.b64encode(f.read()).decode("utf-8")

        # 3. Return a multimodal result (text + image)
        call_result = [
            {"type": "text", "text": "Screenshot captured successfully."},
            {"type": "image", "mime_type": "image/png", "data": base64_image}
        ]

        response = client.interactions.create(
            model="gemini-3-flash-preview",
            tools=functions,
            previous_interaction_id=interaction.id,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": call_result
            }]
        )
        print(f"Response: {response.outputs[-1].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const functions = [
    {
        type: 'function',
        name: 'take_screenshot',
        description: 'Takes a screenshot of a specified website.',
        parameters: {
            type: 'object',
            properties: {
                url: { type: 'string', description: 'The URL to take a screenshot of.' },
            },
            required: ['url'],
        },
    }
];

// 1. Model decides to call the function
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Can you take a screenshot of https://google.com and tell me what you see?',
    tools: functions
});

for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Function call: ${output.name}(${JSON.stringify(output.arguments)})`);

        // 2. Execute the function and load the image
        // Replace with actual function call, pseudo code for reading image from disk
        const base64Image = fs.readFileSync('screenshot.png').toString('base64');

        // 3. Return a multimodal result (text + image)
        const callResult = [
            { type: 'text', text: 'Screenshot captured successfully.' },
            { type: 'image', mime_type: 'image/png', data: base64Image }
        ];

        const response = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            tools: functions,
            previous_interaction_id: interaction.id,
            input: [{
                type: 'function_result',
                name: output.name,
                call_id: output.id,
                result: callResult
            }]
        });
        console.log(`Response: ${response.outputs[response.outputs.length - 1].text}`);
    }
}
```

### REST

```
# 1. Send request with tools (will return a function_call)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Can you take a screenshot of https://google.com and tell me what you see?",
    "tools": [{
        "type": "function",
        "name": "take_screenshot",
        "description": "Takes a screenshot of a specified website.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The URL to take a screenshot of."}
            },
            "required": ["url"]
        }
    }]
}'

# 2. Send multimodal result back (Replace INTERACTION_ID, CALL_ID, and BASE64_IMAGE)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "tools": [{"type": "function", "name": "take_screenshot", "description": "Takes a screenshot of a specified website.", "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}],
#     "previous_interaction_id": "INTERACTION_ID",
#     "input": [{
#         "type": "function_result",
#         "name": "take_screenshot",
#         "call_id": "CALL_ID",
#         "result": [
#             {"type": "text", "text": "Screenshot captured successfully."},
#             {"type": "image", "mime_type": "image/png", "data": "BASE64_IMAGE"}
#         ]
#     }]
# }'
```

#### الأدوات المضمّنة

يتضمّن Gemini أدوات مدمجة، مثل
[تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[تحديد المصدر باستخدام "بحث صور Google"](#image-search-grounding) و[استخدام "خرائط Google" كمصدر](#grounding-with-google-maps) و[تنفيذ الرمز البرمجي](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) و[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar).

##### تحديد المصدر من خلال "بحث Google"

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the last Super Bowl?",
    tools=[{"type": "google_search"}]
)
# Find the text output (not the GoogleSearchResultContent)
text_output = next((o for o in interaction.outputs if o.type == "text"), None)
if text_output:
    print(text_output.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Who won the last Super Bowl?',
    tools: [{ type: 'google_search' }]
});
// Find the text output (not the GoogleSearchResultContent)
const textOutput = interaction.outputs.find(o => o.type === 'text');
if (textOutput) console.log(textOutput.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [{"type": "google_search"}]
}'
```

##### تحديد المصدر باستخدام "بحث صور Google" (لصور Flash 3.1 فقط)

تتيح ميزة تحديد المصدر من خلال صور بحث Google للنماذج استخدام صور الويب التي يتم استرجاعها من خلال صور بحث Google كسياق مرئي لإنشاء الصور. "البحث بالصور" هو نوع بحث جديد ضمن أداة "تحديد المصدر من خلال "بحث Search"" الحالية، ويعمل إلى جانب [بحث الويب](#grounding-with-google-search) العادي.

###### تفعيل ميزة "البحث بالصور"

يمكنك طلب نتائج صور من خلال إضافة `"image_search"` إلى مصفوفة `search_types` الخاصة بالأداة `google_search`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-image-preview",
    input="Search for an image of a vintage gold bitcoin coin.",
    tools=[{
        "type": "google_search",
        "search_types": ["web_search", "image_search"]
    }]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-image-preview',
    input: 'Search for an image of a vintage gold bitcoin coin.',
    tools: [{
        type: 'google_search',
        search_types: ['web_search', 'image_search']
    }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.1-flash-image-preview",
    "input": "Search for an image of a vintage gold bitcoin coin.",
    "tools": [{
        "type": "google_search",
        "search_types": ["web_search", "image_search"]
    }]
}'
```

###### متطلبات العرض الإلزامية

للامتثال [لبنود خدمة &quot;بحث Google&quot;](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search)، يجب أن تتضمّن واجهة المستخدم مستويَين مختلفَين من تحديد المصدر:

1. **تحديد مصدر الإحالة الناجحة في "بحث Google"**

   يجب عرض اقتراحات البحث الخاصة بميزة "التحقّق على Google" المقدَّمة في الحزمة `google_search_result`.

   - **الحقل:** `rendered_content` (HTML/CSS)
   - **الإجراء:** اعرض هذه الشريحة كما هي بالقرب من ردّ النموذج.
2. **إحالة الناشر**

   يجب تقديم رابط يؤدي إلى "الصفحة الحاوية" (الصفحة المقصودة) لكل صورة معروضة.

   - **الحقل:** `url` (تم العثور عليه ضمن الصفيف `result`)
   - **الشرط:** يجب توفير مسار مباشر بنقرة واحدة من الصورة إلى صفحة الويب المصدر التي تحتوي عليها. لا يُسمح باستخدام عارضات الصور الوسيطة أو مسارات النقر المتعدد.

###### التعامل مع الردود المستندة إلى معلومات

يوضّح المقتطف التالي كيفية التعامل مع حِزم الردود المتداخلة لكلّ من بيانات الصور الأولية وبيانات تحديد المصدر الإلزامي.

### Python

```
for output in interaction.outputs:
    # 1. Handle raw multimodal image data
    if output.type == "image":
        print(f"🖼️ Image received: {output.mime_type}")
        # 'data' contains base64-encoded image content
        display_image(output.data, output.mime_type)
    # 2. Handle mandatory Search and Publisher attribution
    elif output.type == "google_search_result":
        # Display Google Search Attribution
        if output.rendered_content:
            render_html_chips(output.rendered_content)

        # Provide Publisher Attribution

        for source in output.result:
            print(f"Source Page: {source['url']}")
```

### JavaScript

```
for (const output of interaction.outputs) {
  // 1. Handle raw multimodal image data
  if (output.type === 'image') {
    console.log(`🖼️ Image received: ${output.mimeType}`);
    // 'data' contains base64-encoded image content
    displayImage(output.data, output.mimeType);
  }
    // 2. Handle mandatory Search and Publisher attribution
    else if (output.type === 'google_search_result') {
      // Display Google Search Attribution
      if (output.renderedContent) {
        renderHtmlChips(output.renderedContent);
      }

      // Provide Publisher Attribution

    for (const source of output.result) {
      console.log(`Source Page: ${source.url}`);
    }
  }
}
```

###### مخطط الناتج المتوقّع

يحتوي **مربع الصورة** (النوع: `"image"`) على البيانات المرئية الأولية التي أنشأها النموذج أو استردّها.

```
{
  "type": "image",
  "mime_type": "image/png",
  "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..." // Base64 content
}
```

تحتوي **كتلة النتائج** (النوع: `"google_search_result"`) على البيانات الوصفية الإلزامية لتحديد المصدر المرتبطة بعملية البحث.

```
{
  "type": "google_search_result",
  "call_id": "search_002",
  "rendered_content": "<div class=\"search-suggestions\">...</div>", // Google Search Attribution

  "result": [
    {
      "url": "https://example.com/source-page", // Publisher Attribution
      "title": "Source Page Title"
    }
  ]
}
```

##### استخدام "خرائط Google" كمصدر

يتيح استخدام &quot;خرائط Google&quot; كمصدر للنماذج استخدام بيانات &quot;خرائط Google&quot; للحصول على سياق مرئي ودبابيس الخرائط والاستكشاف المستند إلى الموقع الجغرافي.

### Python

```
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the best coffee shop near me?",
    tools=[{"type": "google_maps"}]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const client = new GoogleGenAI({});
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What\'s the best coffee shop near me?',
    tools: [{ type: 'google_maps' }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the best coffee shop near me?",
    "tools": [{"type": "google_maps"}]
}'
```

###### متطلبات استخدام الخدمة

عند عرض نتائج من ميزة "استخدام "خرائط Google" كمصدر"، يجب الالتزام [ببنود خدمة "خرائط Google"](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-maps).
يجب إبلاغ المستخدمين بما يلي واستيفاء متطلبات العرض هذه:

- **إبلاغ المستخدم**: يجب أن يتبع المحتوى الذي تم إنشاؤه على الفور مصادر &quot;خرائط Google&quot; المرتبطة به. يجب أن تكون المستندات المصدر قابلة للعرض ضمن تفاعل واحد من المستخدم.
- **روابط العرض**: يمكنك إنشاء معاينة للرابط لكل مصدر (بما في ذلك مقتطفات المراجعات إذا كانت متوفرة).
- **تحديد المصدر على "خرائط Google"**: اتّبِع [إرشادات تحديد المصدر النصي](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar#maps-attribution-guidelines).
- **عرض عنوان المستند المصدر**
- **الرابط إلى المصدر** باستخدام عنوان URL المقدَّم
- **إرشادات تحديد المصدر**: لا تعدّل النص "خرائط Google" (الكتابة بالأحرف اللاتينية الكبيرة، والتفاف النص). منع ترجمة المتصفّح باستخدام `translate="no"`

###### التعامل مع الردّ

يوضّح المقتطف التالي كيفية التعامل مع الردّ من خلال استخراج النص والاقتباسات المضمّنة (بما في ذلك مقتطفات المراجعات) لاستيفاء متطلبات العرض.

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "place_citation":
                    # Display place citation
                    print(f"- {annotation['name']} (Google Maps): {annotation['url']}")
                    # Display review snippets if available
                    if "review_snippets" in annotation:
                        for snippet in annotation["review_snippets"]:
                            print(f"  - Review: {snippet['title']} ({snippet['url']})")
    elif output.type == "google_maps_result":
        # You can also access the raw place data here if needed for map pins
        pass
```

### JavaScript

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'place_citation') {
                    console.log(`- ${annotation.name} (Google Maps): ${annotation.url}`);
                    if (annotation.review_snippets) {
                        for (const snippet of annotation.review_snippets) {
                            console.log(`  - Review: ${snippet.title} (${snippet.url})`);
                        }
                    }
                }
            }
        }
    }
}
```

###### مخطط الناتج المتوقّع

توقَّع مخطط الإخراج التالي عند استخدام Grounding with Google Maps.

تحتوي **كتلة النتائج** (النوع: `"google_maps_result"`) على بيانات المكان المنظَّمة.

```
{
  "type": "google_maps_result",
  "call_id": "maps_001",
  "result": {
    "places": [
      {
        "place_id": "ChIJ...",
        "name": "Blue Bottle Coffee", // Google Maps Source
        "url": "https://maps.google.com/?cid=...", // Google Maps Link
        "review_snippets": [
          {
            "title": "Amazing single-origin selections",
            "url": "https://maps.google.com/...",
            "review_id": "def456"
          }
        ]
      }
    ],
    "widget_context_token": "widgetcontent/..."
  },
  "signature": "..."
}
```

يحتوي **مربع النص** (النوع: `"text"`) على المحتوى الذي تم إنشاؤه مع التعليقات التوضيحية المضمّنة.

```
{
  "type": "text",
  "text": "Blue Bottle Coffee (4.5★) on Mint Plaza was rated highly online...",
  "annotations": [
    {
      "type": "place_citation",
      "place_id": "ChIJ...",
      "name": "Blue Bottle Coffee", // Google Maps Source
      "url": "https://maps.google.com/?cid=...", // Google Maps Link
      "review_snippets": [
        {
          "title": "Amazing single-origin selections",
          "url": "https://maps.google.com/...",
          "review_id": "def456"
        }
      ],
      "start_index": 0,
      "end_index": 42
    }
  ]
}
```

##### تنفيذ الرمز البرمجي

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}]
)
print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }]
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}]
}'
```

##### سياق عنوان URL

يتيح تحديد المصدر باستخدام سياق عنوان URL للنموذج قراءة عناوين URL العلنية المقدَّمة في الطلب أو قائمة الأدوات.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize the content of https://www.wikipedia.org/",
    tools=[{"type": "url_context"}]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize the content of https://www.wikipedia.org/',
    tools: [{ type: 'url_context' }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize the content of https://www.wikipedia.org/",
    "tools": [{"type": "url_context"}]
}'
```

###### التعامل مع الردّ

يوضّح المقتطف التالي كيفية التعامل مع الردّ من خلال استخراج النص والاقتباسات المضمّنة (النوع `url_citation`).

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "url_citation":
                    print(f"- {annotation['title']}: {annotation['url']}")
```

### JavaScript

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'url_citation') {
                    console.log(`- ${annotation.title}: ${annotation.url}`);
                }
            }
        }
    }
}
```

###### مخطط الناتج المتوقّع

توقَّع مخطط الناتج التالي عند استخدام سياق عنوان URL.

يحتوي **حظر المكالمة** (النوع: `"url_context_call"`) على عنوان URL الذي حاول النموذج قراءته.

```
{
  "type": "url_context_call",
  "id": "browse_001",
  "arguments": {
    "urls": ["https://www.wikipedia.org/"]
  },
  "signature": "EkYKIGY5OT..."
}
```

يحتوي **قسم النتائج** (النوع: `"url_context_result"`) على حالة الاسترداد.

```
{
  "type": "url_context_result",
  "call_id": "browse_001",
  "result": {
    "url": "https://www.wikipedia.org/",
    "status": "URL_RETRIEVAL_STATUS_SUCCESS"
  },
  "signature": "EkYKIGY5OT..."
}
```

يحتوي **مربع النص** على النص الذي تم إنشاؤه والاستشهادات المضمَّنة.

```
{
  "type": "text",
  "text": "Wikipedia is a free online encyclopedia...",
  "annotations": [
    {
      "type": "url_citation",
      "url": "https://www.wikipedia.org/",
      "title": "Wikipedia — Main Page",
      "start_index": 0,
      "end_index": 42
    }
  ]
}
```

##### استخدام الكمبيوتر

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-2.5-computer-use-preview-10-2025",
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[{
        "type": "computer_use",
        "environment": "browser",
        "excludedPredefinedFunctions": ["drag_and_drop"]
    }]
)

# The response will contain tool calls (actions) for the computer interface
# or text explaining the action
for output in interaction.outputs:
    print(output)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-2.5-computer-use-preview-10-2025',
    input: 'Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.',
    tools: [{
        type: 'computer_use',
        environment: 'browser',
        excludedPredefinedFunctions: ['drag_and_drop']
    }]
});

// The response will contain tool calls (actions) for the computer interface
// or text explaining the action
interaction.outputs.forEach(output => console.log(output));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-computer-use-preview-10-2025",
    "input": "Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    "tools": [{
        "type": "computer_use",
        "environment": "browser",
        "excludedPredefinedFunctions": ["drag_and_drop"]
    }]
}'
```

###### معالجة نتائج الدالة Computer Use

بما أنّ "استخدام الكمبيوتر" هو حلقة أدوات من جهة العميل، عليك تنفيذ الإجراء (مثل فتح متصفّح) وإرسال النتيجة إلى النموذج. عند إرسال `function_result` لإجراءات مثل `open_web_browser`، احرص على تمرير استجابة عنوان URL في قائمة النتائج كما هو موضّح أدناه:

```
{
  "type": "function_result",
  "name": "open_web_browser",
  "call_id": "5q6h0z70",
  "result": [
    {
      "type": "text",
      "text": "{\"url\": \"https://google.com\", \"safety_acknowledgement\":true}"
    },
    {
      "type": "image",
      "data": "iVBORw0KGgoAAAANSUhEUgAA...",
      "mime_type": "image/png"
    }
  ]
}
```

##### البحث عن ملف

تتيح ميزة "تحديد المصدر" من خلال "البحث في الملفات" للنموذج البحث في الملفات التي حمّلتها في "متاجر البحث في الملفات".

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about the book 'I, Claudius'",
    tools=[{"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]}]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "Tell me about the book 'I, Claudius'",
    tools: [{ type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me about the book 'I, Claudius'",
    "tools": [{"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]}]
}'
```

###### التعامل مع الردّ

يوضّح المقتطف التالي كيفية التعامل مع الردّ من خلال استخراج النص والاقتباسات المضمّنة (النوع `file_citation`).

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "file_citation":
                    print(f"- {annotation['file_name']} ({annotation['document_uri']}):")
                    print(f"  Snippet: {annotation['source']}")
```

### JavaScript

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'file_citation') {
                    console.log(`- ${annotation.fileName} (${annotation.documentUri}):`);
                    console.log(`  Snippet: ${annotation.source}`);
                }
            }
        }
    }
}
```

###### مخطط الناتج المتوقّع

توقَّع مخطط الإخراج التالي عند استخدام "البحث في الملفات".

يحتوي **حظر المكالمات** (النوع: `"file_search_call"`) على البيانات الوصفية للمكالمة.

```
{
  "type": "file_search_call",
  "id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

يحتوي **مربع النتائج** (النوع: `"file_search_result"`) على البيانات الوصفية للنتائج.

```
{
  "type": "file_search_result",
  "call_id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

يحتوي **مربع النص** على النص الذي تم إنشاؤه والاستشهادات المضمَّنة.

```
{
  "type": "text",
  "text": "The book 'I, Claudius' is a historical novel by Robert Graves...",
  "annotations": [
    {
      "type": "file_citation",
      "document_uri": "fileSearchStores/my-store-name/documents/abc",
      "file_name": "book_summaries.pdf",
      "source": "Claudius is the narrator of this historical novel...",
      "start_index": 0,
      "end_index": 60
    }
  ]
}
```

#### الجمع بين الأدوات المضمّنة واستخدام الدوال

يمكنك استخدام [الأدوات المضمّنة واستدعاء الدوال](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar) معًا في الطلب نفسه.

### Python

```
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

tools = [
    {"type": "google_search"},  # Built-in tool
    get_weather                 # Custom tool (callable)
]

# Turn 1: Initial request with both tools enabled
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name} (ID: {output.id})")
        # Execute your custom function locally
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        # Turn 2: Provide the function result back to the model.
        # Passing `previous_interaction_id` automatically circulates the
        # built-in Google Search context (and thought signatures) from Turn 1
        interaction_2 = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": json.dumps(result)
            }]
        )

        for output in interaction_2.outputs:
            if output.type == "text":
                print(output.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool              // Custom tool
];

// Turn 1: Initial request with both tools enabled
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const output of interaction.outputs) {
    if (output.type == "function_call") {
        console.log(`Function call: ${output.name} (ID: ${output.id})`);
        // Execute your custom function locally
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        // Turn 2: Provide the function result back to the model.
        // Passing `previous_interaction_id` automatically circulates the
        // built-in Google Search context (and thought signatures) from Turn 1
        const interaction_2 = await client.interactions.create({
            model: "gemini-3-flash-preview",
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: "function_result",
                name: output.name,
                call_id: output.id,
                result: JSON.stringify(result)
            }]
        });

        for (const output_2 of interaction_2.outputs) {
            if (output_2.type == "text") {
                console.log(output_2.text);
            }
        }
    }
}
```

### REST

```
# Turn 1: Initial request with both tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the northernmost city in the United States? What is the weather like there today?",
    "tools": [
        {"type": "google_search"},
        {
            "type": "function",
            "name": "get_weather",
            "description": "Gets the weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
                },
                "required": ["location"]
            }
        }
    ]
}'

# Assuming Turn 1 returns a function_call for get_weather,
# replace INTERACTION_ID and CALL_ID with values from Turn 1 response.
# Turn 2: Provide the function result back to the model.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "tools": [
        {"type": "google_search"},
        {
            "type": "function",
            "name": "get_weather",
            "description": "Gets the weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
                },
                "required": ["location"]
            }
        }
    ],
    "input": [{
        "type": "function_result",
        "name": "get_weather",
        "call_id": "CALL_ID",
        "result": "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"
    }]
}'
```

##### فهم تداول سياق الأداة

تتيح الإصدارات 3 من Gemini والإصدارات الأحدث **تداول سياق الأدوات** للحفاظ على "ذاكرة" موثوقة للإجراءات من جهة الخادم. عندما يتم تشغيل أداة مدمجة (مثل &quot;بحث Google&quot;)، تنشئ واجهة برمجة التطبيقات أجزاء `toolCall` و`toolResponse` محدّدة. تحتوي هذه الأجزاء على السياق الدقيق الذي يحتاج إليه النموذج للتوصل إلى استنتاجات بشأن تلك النتائج في الجولة التالية.

- **الاحتفاظ بالحالة (يُنصح به)**: إذا كنت تستخدم `previous_interaction_id`، ستتولّى واجهة برمجة التطبيقات إدارة هذا التداول تلقائيًا.
- **بلا حالة**: إذا كنت تدير السجلّ يدويًا، يجب تضمين هذه الحظر
  بالضبط كما تم عرضها من خلال واجهة برمجة التطبيقات في مصفوفة الإدخال.

### بروتوكول سياق النموذج عن بُعد (MCP)

تسهّل عملية دمج [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) عن بُعد عملية تطوير الوكيل من خلال السماح لواجهة برمجة التطبيقات Gemini API باستدعاء الأدوات الخارجية المستضافة على الخوادم البعيدة مباشرةً.

### Python

```
import datetime
from google import genai

client = genai.Client()

mcp_server = {
    "type": "mcp_server",
    "name": "weather_service",
    "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
}

today = datetime.date.today().strftime("%d %B %Y")

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="What is the weather like in New York today?",
    tools=[mcp_server],
    system_instruction=f"Today is {today}."
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const mcpServer = {
    type: 'mcp_server',
    name: 'weather_service',
    url: 'https://gemini-api-demos.uc.r.appspot.com/mcp'
};

const today = new Date().toDateString();

const interaction = await client.interactions.create({
    model: 'gemini-2.5-flash',
    input: 'What is the weather like in New York today?',
    tools: [mcpServer],
    system_instruction: `Today is ${today}.`
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-flash",
    "input": "What is the weather like in New York today?",
    "tools": [{
        "type": "mcp_server",
        "name": "weather_service",
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }],
    "system_instruction": "Today is '"$(date +"%du%Bt%Y")"' YYYY-MM-DD>."
}'
```

**ملاحظات مهمّة:**

- لا يعمل MCP البعيد إلا مع خوادم HTTP قابلة للبث (لا تتوافق مع خوادم SSE)
- لا تعمل ميزة "التحكّم عن بُعد في MCP" مع نماذج Gemini 3 (ستتوفّر هذه الميزة قريبًا)
- يجب ألا تتضمّن أسماء خادم MCP الرمز "-" (استخدِم أسماء خادم snake\_case بدلاً من ذلك)

### الناتج المنظَّم (مخطّط JSON)

فرض إخراج JSON محدّد من خلال توفير مخطّط JSON في المَعلمة
`response_format` وهي مفيدة في مهام مثل الإشراف أو التصنيف أو استخراج البيانات.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal, Union
client = genai.Client()

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"]

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format=ModerationResult.model_json_schema(),
)

parsed_output = ModerationResult.model_validate_json(interaction.outputs[-1].text)
print(parsed_output)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import { z } from 'zod';
const client = new GoogleGenAI({});

const moderationSchema = z.object({
    decision: z.union([
        z.object({
            reason: z.string().describe('The reason why the content is considered spam.'),
            spam_type: z.enum(['phishing', 'scam', 'unsolicited promotion', 'other']).describe('The type of spam.'),
        }).describe('Details for content classified as spam.'),
        z.object({
            summary: z.string().describe('A brief summary of the content.'),
            is_safe: z.boolean().describe('Whether the content is safe for all audiences.'),
        }).describe('Details for content classified as not spam.'),
    ]),
});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format: z.toJSONSchema(moderationSchema),
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    "response_format": {
        "type": "object",
        "properties": {
            "decision": {
                "type": "object",
                "properties": {
                    "reason": {"type": "string", "description": "The reason why the content is considered spam."},
                    "spam_type": {"type": "string", "description": "The type of spam."}
                },
                "required": ["reason", "spam_type"]
            }
        },
        "required": ["decision"]
    }
}'
```

### الجمع بين الأدوات والمخرجات المنظَّمة

يمكنك الجمع بين الأدوات المضمّنة والناتج المنظَّم للحصول على كائن JSON موثوق به استنادًا إلى المعلومات التي تستردّها إحدى الأدوات.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal, Union

client = genai.Client()

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"]

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format=ModerationResult.model_json_schema(),
    tools=[{"type": "url_context"}]
)

parsed_output = ModerationResult.model_validate_json(interaction.outputs[-1].text)
print(parsed_output)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import { z } from 'zod'; // Assuming zod is used for schema generation, or define manually
const client = new GoogleGenAI({});

const obj = z.object({
    winning_team: z.string(),
    score: z.string(),
});
const schema = z.toJSONSchema(obj);

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Who won the last euro?',
    tools: [{ type: 'google_search' }],
    response_format: schema,
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last euro?",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "object",
        "properties": {
            "winning_team": {"type": "string"},
            "score": {"type": "string"}
        }
    }
}'
```

## الميزات المتقدمة

تتوفّر أيضًا ميزات متقدّمة إضافية تمنحك المزيد من المرونة
في استخدام Interactions API.

### البث

تلقّي الردود بشكل تدريجي أثناء إنشائها

عندما تكون القيمة `stream=true`، لا يتضمّن الحدث النهائي `interaction.complete` المحتوى الذي تم إنشاؤه في الحقل `outputs`. ويحتوي فقط على البيانات الوصفية للاستخدام والحالة النهائية. يجب تجميع أحداث `content.delta` من جهة العميل لإعادة إنشاء الرد الكامل أو وسيطات استدعاء الأداة.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain quantum entanglement in simple terms.",
    stream=True
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
        elif chunk.delta.type == "thought_summary":
            print(getattr(chunk.delta.content, "text", ""), end="", flush=True)
    elif chunk.event_type == "interaction.complete":
        print(f"\n\n--- Stream Finished ---")
        print(f"Total Tokens: {chunk.interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text' && 'text' in chunk.delta) {
            process.stdout.write(chunk.delta.text);
        } else if (chunk.delta.type === 'thought_summary' && chunk.delta.content) {
            process.stdout.write(chunk.delta.content.text || '');
        }
    } else if (chunk.event_type === 'interaction.complete') {
        console.log('\n\n--- Stream Finished ---');
        console.log(`Total Tokens: ${chunk.interaction.usage.total_tokens}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
}'
```

#### أنواع أحداث البث

عند تفعيل البث، تعرض واجهة برمجة التطبيقات أحداثًا يتم إرسالها من الخادم (SSE). يحتوي كل حدث على حقل `event_type` يشير إلى الغرض منه. تتوفّر القائمة الكاملة لأنواع الأحداث في [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction).

| نوع الحدث | الوصف |
| --- | --- |
| `interaction.start` | الحدث الأول تحتوي على التفاعل `id` و`status` الأولي (`in_progress`). |
| `interaction.status_update` | تشير إلى التغييرات في الحالة (مثل `in_progress`). |
| `content.start` | تضع علامة على بداية مجموعة إخراج جديدة. يحتوي على `index` والمحتوى `type` (مثل `text` و`thought`). |
| `content.delta` | تعديلات المحتوى التدريجية يحتوي على البيانات الجزئية التي تمّت فهرستها باستخدام `delta.type`. |
| `content.stop` | تضع هذه السمة علامة على نهاية كتلة الإخراج في `index`. |
| `interaction.complete` | الحدث النهائي يتضمّن `id` و`status` و`usage` وبيانات وصفية. **ملاحظة:** `outputs` هي `None`، لذا عليك إعادة إنشاء النتائج من أحداث `content.*`. |
| `error` | يشير إلى حدوث خطأ. يتضمّن `error.code` و`error.message`. |

#### إعادة إنشاء عنصر Interaction من أحداث البث

على عكس الردود غير المتدفقة، فإنّ الردود المتدفقة **لا** تحتوي على مصفوفة
`outputs`. يجب إعادة إنشاء النتائج من خلال تجميع المحتوى من أحداث `content.delta`.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Write a haiku about Python programming.",
    stream=True
)

# Accumulate outputs by index
outputs = {}
usage = None

for chunk in stream:
    if chunk.event_type == "content.start":
        outputs[chunk.index] = {"type": chunk.content.type}

    elif chunk.event_type == "content.delta":
        output = outputs[chunk.index]
        if chunk.delta.type == "text":
            output["text"] = output.get("text", "") + chunk.delta.text
        elif chunk.delta.type == "thought_signature":
            output["signature"] = chunk.delta.signature
        elif chunk.delta.type == "thought_summary":
            output["summary"] = output.get("summary", "") + getattr(chunk.delta.content, "text", "")

    elif chunk.event_type == "interaction.complete":
        usage = chunk.interaction.usage

# Final outputs list (sorted by index)
final_outputs = [outputs[i] for i in sorted(outputs.keys())]
print(f"\n\nOutputs: {final_outputs}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Write a haiku about Python programming.',
    stream: true,
});

// Accumulate outputs by index
const outputs = new Map();
let usage = null;

for await (const chunk of stream) {
    if (chunk.event_type === 'content.start') {
        outputs.set(chunk.index, { type: chunk.content.type });

    } else if (chunk.event_type === 'content.delta') {
        const output = outputs.get(chunk.index);
        if (chunk.delta.type === 'text') {
            output.text = (output.text || '') + chunk.delta.text;
            process.stdout.write(chunk.delta.text);
        } else if (chunk.delta.type === 'thought_signature') {
            output.signature = chunk.delta.signature;
        } else if (chunk.delta.type === 'thought_summary') {
            output.summary = (output.summary || '') + (chunk.delta.content?.text || '');
        }

    } else if (chunk.event_type === 'interaction.complete') {
        usage = chunk.interaction.usage;
    }
}

// Final outputs list (sorted by index)
const finalOutputs = [...outputs.entries()]
    .sort((a, b) => a[0] - b[0])
    .map(([_, output]) => output);
console.log(`\n\nOutputs:`, finalOutputs);
```

#### طلبات أدوات البث

عند استخدام أدوات مع البث، ينشئ النموذج طلبات الدوال كسلسلة من أحداث `content.delta` في البث. على عكس النص، يتم تقديم وسيطات الأدوات ككائنات JSON كاملة ضمن حدث `content.delta` واحد. إذا كانت مصفوفة
`outputs` فارغة في حدث `interaction.complete` أثناء البث، عليك تسجيل طلبات الأدوات من الفروق كما هو موضّح أدناه.

### Python

```
from google import genai
import json

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state"}
        },
        "required": ["location"]
    }
}

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool],
    stream=True
)

# A map to capture tool calls by their ID as they arrive
function_calls = {}

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text" and chunk.delta.text:
            print(chunk.delta.text, end="", flush=True)

        elif chunk.delta.type == "function_call":
            print(f"\nExecuting {chunk.delta.name} immediately...")
            # result = my_tools[chunk.delta.name](**chunk.delta.arguments)
            function_calls[chunk.delta.id] = chunk.delta

    elif chunk.event_type == "interaction.complete":
        print("\n\nAll tools executed. Stream finished.")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state' }
        },
        required: ['location']
    }
};

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool],
    stream: true,
});

const toolCalls = new Map();

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text' && chunk.delta.text) {
            process.stdout.write(chunk.delta.text);

        } else if (chunk.delta.type === 'function_call') {
            console.log(`\nExecuting ${chunk.delta.name} immediately...`);
            // const result = myTools[chunk.delta.name](chunk.delta.arguments);
            toolCalls.set(chunk.delta.id, chunk.delta);
        }
    } else if (chunk.event_type === 'interaction.complete') {
        console.log('\n\nAll tools executed. Stream finished.');
    }
}
```

### REST

```
# When streaming via SSE, capture function_call data from content.delta events.
# The 'arguments' field arrives as a complete JSON object once generated.

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

### التهيئة

تخصيص سلوك النموذج باستخدام `generation_config`

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story about a brave knight.",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 500,
        "thinking_level": "low",
    }
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story about a brave knight.',
    generation_config: {
        temperature: 0.7,
        max_output_tokens: 500,
        thinking_level: 'low',
    }
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a story about a brave knight.",
    "generation_config": {
        "temperature": 0.7,
        "max_output_tokens": 500,
        "thinking_level": "low"
    }
}'
```

### جارٍ التفكير

تستخدم نماذج Gemini 2.5 والإصدارات الأحدث عملية استدلال داخلية تُعرف باسم "التفكير"
قبل إنشاء ردّ. يساعد ذلك النموذج في تقديم إجابات أفضل للمهام المعقّدة، مثل الرياضيات والترميز والاستدلال المتعدّد الخطوات.

#### مستوى التفكير

تتيح لك المَعلمة `thinking_level` التحكّم في عمق الاستنتاج في النموذج:

| المستوى | الوصف | النماذج المتوافقة |
| --- | --- | --- |
| `minimal` | يتطابق هذا الخيار مع الإعداد "بدون تفكير" لمعظم طلبات البحث. في بعض الحالات، قد تفكّر النماذج بشكل بسيط جدًا. يقلّل من زمن الانتقال والتكلفة. | **نماذج Flash فقط**   (مثل Gemini 3 Flash) |
| `low` | الاستدلال البسيط الذي يعطي الأولوية لوقت الاستجابة وتوفير التكاليف عند اتّباع التعليمات البسيطة والمحادثة | **جميع نماذج التفكير** |
| `medium` | تفكير متوازن لمعظم المهام | **نماذج Flash فقط**   (مثل Gemini 3 Flash) |
| `high` | **(تلقائي)** يزيد من عمق التفكير. قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى الرمز المميز الأول، ولكن سيكون الناتج أكثر دقة. | **جميع نماذج التفكير** |

#### ملخّصات التفكير

يتم تمثيل عملية التفكير التي يجريها النموذج على شكل **مربّعات أفكار** (`type: "thought"`) في نواتج الردود. يمكنك التحكّم في ما إذا كنت تريد تلقّي ملخّصات قابلة للقراءة من قِبل البشر حول عملية التفكير باستخدام المَعلمة `thinking_summaries`:

| القيمة | الوصف |
| --- | --- |
| `auto` | **(الإعداد التلقائي)** لعرض ملخّصات الأفكار عند توفّرها |
| `none` | تؤدي إلى إيقاف ملخّصات الأفكار. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Solve this step by step: What is 15% of 240?",
    generation_config={
        "thinking_level": "high",
        "thinking_summaries": "auto"
    }
)

for output in interaction.outputs:
    if output.type == "thought":
        print(f"Thinking: {output.summary}")
    elif output.type == "text":
        print(f"Answer: {output.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Solve this step by step: What is 15% of 240?',
    generation_config: {
        thinking_level: 'high',
        thinking_summaries: 'auto'
    }
});

for (const output of interaction.outputs) {
    if (output.type === 'thought') {
        console.log(`Thinking: ${output.summary}`);
    } else if (output.type === 'text') {
        console.log(`Answer: ${output.text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Solve this step by step: What is 15% of 240?",
    "generation_config": {
        "thinking_level": "high",
        "thinking_summaries": "auto"
    }
}'
```

يحتوي كل قسم من أقسام الأفكار على حقل `signature` (تجزئة تشفيرية لحالة الاستدلال الداخلية) وحقل `summary` اختياري (ملخّص قابل للقراءة من قِبل الإنسان حول استدلال النموذج). تظهر `signature` دائمًا، ولكن قد يحتوي قسم الأفكار على توقيع فقط بدون ملخّص في الحالات التالية:

- **الطلبات البسيطة**: لم يقدّم النموذج أسبابًا كافية لإنشاء ملخّص
- ‫**`thinking_summaries: "none"`**: تم إيقاف الملخّصات بشكل صريح

يجب أن يتعامل الرمز دائمًا مع كتل الأفكار التي يكون فيها `summary` فارغًا أو غير متوفّر. عند إدارة سجلّ المحادثات يدويًا (وضع عدم الاحتفاظ بالحالة)، يجب تضمين كتل الأفكار مع توقيعاتها في الطلبات اللاحقة للتحقّق من صحتها.

### العمل باستخدام الملفات

#### العمل باستخدام الملفات البعيدة

الوصول إلى الملفات باستخدام عناوين URL عن بُعد مباشرةً في طلب البيانات من واجهة برمجة التطبيقات

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "image",
            "uri": "https://github.com/<github-path>/cats-and-dogs.jpg",
        },
        {"type": "text", "text": "Describe what you see."}
    ],
)
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        {
            type: 'image',
            uri: 'https://github.com/<github-path>/cats-and-dogs.jpg',
        },
        { type: 'text', text: 'Describe what you see.' }
    ],
});
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {
            "type": "image",
            "uri": "https://github.com/<github-path>/cats-and-dogs.jpg"
        },
        {"type": "text", "text": "Describe what you see."}
    ]
}'
```

#### العمل باستخدام Gemini Files API

حمِّل الملفات إلى [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) من Gemini
قبل استخدامها.

### Python

```
from google import genai
import time
import requests
client = genai.Client()

# 1. Download the file
url = "https://github.com/philschmid/gemini-samples/raw/refs/heads/main/assets/cats-and-dogs.jpg"
response = requests.get(url)
with open("cats-and-dogs.jpg", "wb") as f:
    f.write(response.content)

# 2. Upload to Gemini Files API
file = client.files.upload(file="cats-and-dogs.jpg")

# 3. Wait for processing
while client.files.get(name=file.name).state != "ACTIVE":
    time.sleep(2)

# 4. Use in Interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "image",
            "uri": file.uri,
        },
        {"type": "text", "text": "Describe what you see."}
    ],
)
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
import fetch from 'node-fetch';
const client = new GoogleGenAI({});

// 1. Download the file
const url = 'https://github.com/philschmid/gemini-samples/raw/refs/heads/main/assets/cats-and-dogs.jpg';
const filename = 'cats-and-dogs.jpg';
const response = await fetch(url);
const buffer = await response.buffer();
fs.writeFileSync(filename, buffer);

// 2. Upload to Gemini Files API
const myfile = await client.files.upload({ file: filename, config: { mimeType: 'image/jpeg' } });

// 3. Wait for processing
while ((await client.files.get({ name: myfile.name })).state !== 'ACTIVE') {
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// 4. Use in Interaction
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'image', uri: myfile.uri, },
        { type: 'text', text: 'Describe what you see.' }
    ],
});
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    }
}
```

### REST

```
# 1. Upload the file (Requires File API setup)
# See https://ai.google.dev/gemini-api/docs/files for details.
# Assume FILE_URI is obtained from the upload step.

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "image", "uri": "FILE_URI"},
        {"type": "text", "text": "Describe what you see."}
    ]
}'
```

### فئات استنتاج Flex وPriority

يمكنك استخدام مستويات الاستدلال مع Interactions API لتحسين الأداء بما يتناسب مع احتياجات أحمال العمل المختلفة:

- ‫[Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar) (`flex`) لتحسين التكلفة، وخصم% 50 على الأسعار العادية
- [الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) (`priority`) لتحسين وقت الاستجابة، وهي فئة الخدمة الأعلى موثوقية.

### Python

```
import google.genai as genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.outputs[-1].text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
 import { GoogleGenAI } from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const interaction = await client.interactions.create({
             model: 'gemini-3-flash-preview',
             input: 'Analyze this dataset for trends...',
             service_tier: 'flex'
         });
         console.log(interaction.outputs[interaction.outputs.length - 1].text);
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }
 }
 await main();
```

### REST

```
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
 -H "Content-Type: application/json" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -d '{
     "model": "gemini-3-flash-preview",
     "input": "Analyze this dataset for trends...",
     "service_tier": "flex"
 }'
```

### نموذج البيانات

يمكنك الاطّلاع على مزيد من المعلومات حول نموذج البيانات في [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar#data-models). في ما يلي نظرة عامة عالية المستوى على المكوّنات الرئيسية.

#### التفاعل

| الموقع | النوع | الوصف |
| --- | --- | --- |
| `id` | `string` | المعرّف الفريد للتفاعل |
| `model` / `agent` | `string` | النموذج أو الوكيل المستخدَم يمكن تقديم واحد فقط. |
| `input` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=ar#data-models) | المدخلات المقدَّمة |
| `outputs` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=ar#data-models) | ردود النموذج |
| `tools` | [`Tool[]`](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Tool) | الأدوات المستخدَمة |
| `previous_interaction_id` | `string` | معرّف التفاعل السابق لتوفير السياق |
| `stream` | `boolean` | تُستخدَم لتحديد ما إذا كان التفاعل يتم من خلال البث. |
| `status` | `string` | الحالة: `completed` أو `in_progress` أو `requires_action` أو `failed` أو غير ذلك |
| `background` | `boolean` | تُستخدَم لتحديد ما إذا كان التفاعل في وضع الخلفية. |
| `store` | `boolean` | تُستخدَم لتحديد ما إذا كان يجب تخزين التفاعل. القيمة التلقائية: `true` اضبط الخيار على `false` لإيقاف هذه الميزة. |
| `usage` | [الاستخدام](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction) | استخدام الرموز المميزة لطلب التفاعل |

## الطُرز والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| معاينة Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite-preview` |
| معاينة Gemini 3.1 Pro | الطراز | `gemini-3.1-pro-preview` |
| معاينة Gemini 3 Flash | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| معاينة مقطع Lyria 3 | الطراز | `lyria-3-clip-preview` |
| معاينة Lyria 3 Pro | الطراز | `lyria-3-pro-preview` |
| معاينة Deep Research | الوكيل | `deep-research-pro-preview-12-2025` |
| معاينة Deep Research | الوكيل | `deep-research-preview-04-2026` |
| معاينة Deep Research | الوكيل | `deep-research-max-preview-04-2026` |

## طريقة عمل Interactions API

تم تصميم Interactions API حول مورد مركزي هو
[**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction).
يمثّل `Interaction` دورة كاملة في محادثة أو مهمة. يعمل هذا السجلّ كسجلّ للجلسة، ويتضمّن السجلّ الكامل للتفاعل، بما في ذلك جميع البيانات التي أدخلها المستخدِم وأفكار النموذج واستدعاءات الأدوات ونتائج الأدوات ومخرجات النموذج النهائية.

عند إجراء طلب إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، فإنّك
تنشئ مورد `Interaction` جديدًا.

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في مكالمة لاحقة باستخدام المَعلمة `previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثات، ما يوفّر عليك عناء إعادة إرسال سجلّ المحادثات بأكمله.

يتم الاحتفاظ فقط بسجلّ المحادثات (المدخلات والمخرجات) باستخدام `previous_interaction_id`. المَعلمات الأخرى **محدودة بنطاق التفاعل**
ولا تنطبق إلا على التفاعل المحدّد الذي يتم إنشاؤه حاليًا:

- `tools`
- `system_instruction`
- ‫`generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

وهذا يعني أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. تكون إدارة الحالة من جهة الخادم اختيارية، ويمكنك أيضًا التشغيل في وضع بلا حالة من خلال إرسال سجلّ المحادثة الكامل في كل طلب.

### تخزين البيانات والاحتفاظ بها

يتم تلقائيًا تخزين جميع عناصر Interaction (`store=true`) من أجل تبسيط استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`) والتنفيذ في الخلفية (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **المستوى المدفوع**: يتم الاحتفاظ بالتفاعلات لمدة **55 يومًا**.
- **الطبقة المجانية**: يتم الاحتفاظ بالتفاعلات لمدة **يوم واحد**.

إذا كنت لا تريد ذلك، يمكنك ضبط `store=false` في طلبك. يختلف عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف مساحة التخزين لأي تفاعل. يُرجى العِلم أنّ `store=false` غير متوافق مع `background=true` ويمنع استخدام `previous_interaction_id` في المحادثات اللاحقة.

يمكنك حذف التفاعلات المخزّنة في أي وقت باستخدام طريقة الحذف المتوفّرة في [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). لا يمكنك حذف التفاعلات إلا إذا كنت تعرف رقم تعريف التفاعل.

وبعد انتهاء صلاحية فترة التخزين، سيتم حذف بياناتك تلقائيًا.

تتم معالجة عناصر التفاعل وفقًا [للبنود](https://ai.google.dev/gemini-api/terms?hl=ar).

## أفضل الممارسات

- **نسبة نتيجة ذاكرة التخزين المؤقت**: يتيح استخدام `previous_interaction_id` لمواصلة المحادثات للنظام الاستفادة بسهولة أكبر من التخزين المؤقت الضمني لسجلّ المحادثات، ما يحسّن الأداء ويقلّل التكاليف.
- **مزج التفاعلات**: يمكنك مزج التفاعلات بين الوكيل والنموذج ومطابقتها ضمن محادثة واحدة. على سبيل المثال، يمكنك استخدام وكيل متخصص، مثل وكيل &quot;البحث المعمّق&quot;، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي لتنفيذ مهام المتابعة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## حزم SDK

يمكنك استخدام أحدث إصدار من حِزم تطوير البرامج (SDK) من Google GenAI للوصول إلى واجهة برمجة التطبيقات Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `1.55.0` والإصدارات الأحدث.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `1.33.0` والإصدارات الأحدث.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حِزم SDK على صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **حالة الإصدار التجريبي**: تتوفّر Interactions API في إصدار تجريبي/معاينة. قد تتغيّر الميزات والمخططات.
- **التحكّم عن بُعد في MCP**: لا يتيح Gemini 3 التحكّم عن بُعد في MCP، ولكن ستتوفّر هذه الميزة قريبًا.

## التغييرات التي قد تؤدي إلى أعطال

تتوفّر واجهة Interactions API حاليًا في مرحلة تجريبية مبكرة. نعمل حاليًا على تطوير وتحسين إمكانات واجهة برمجة التطبيقات ومخططات الموارد وواجهات حزمة تطوير البرامج (SDK) استنادًا إلى الاستخدام الفعلي وملاحظات المطوّرين.

نتيجةً لذلك، **قد تحدث تغييرات غير متوافقة مع الإصدارات السابقة**.
قد تشمل التعديلات تغييرات على ما يلي:

- مخططات الإدخال والإخراج
- توقيعات طرق حزمة SDK وبُنى العناصر
- سلوكيات الميزات المحدّدة

بالنسبة إلى أحمال العمل في مرحلة الإنتاج، عليك مواصلة استخدام واجهة برمجة التطبيقات القياسية
[`generateContent`](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar). ويظل هذا المسار هو المسار المقترَح لعمليات النشر الثابتة، وسيستمر تطويره وصيانته بشكل نشط.

## الملاحظات

تُعدّ ملاحظاتك مهمة جدًا لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن أخطاء أو طلب ميزات في [منتدى مطوّري الذكاء الاصطناعي من Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- جرِّب [دفتر ملاحظات التشغيل السريع لواجهة Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).
- [مزيد من المعلومات حول "وكيل Deep Research" في Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
