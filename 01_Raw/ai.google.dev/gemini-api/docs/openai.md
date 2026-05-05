---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=ar
fetched_at: 2026-05-05T19:51:30.353442+00:00
title: "\u0627\u0644\u062a\u0648\u0627\u0641\u0642 \u0645\u0639 OpenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التوافق مع OpenAI

يمكن الوصول إلى نماذج Gemini باستخدام مكتبات OpenAI (Python وTypeScript /
Javascript) بالإضافة إلى REST API، وذلك من خلال تعديل ثلاثة أسطر من الرمز البرمجي
واستخدام مفتاح [Gemini API](https://aistudio.google.com/apikey?hl=ar). إذا لم تكن تستخدم مكتبات OpenAI، ننصحك باستدعاء
[Gemini API مباشرةً](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

ما الذي تغيّر؟ ثلاثة أسطر فقط!

- **`api_key="GEMINI_API_KEY"`**: استبدِل "`GEMINI_API_KEY`" بمفتاح Gemini
  API الفعلي، الذي يمكنك الحصول عليه في [Google AI Studio](https://aistudio.google.com?hl=ar).
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** يطلب هذا السطر من مكتبة OpenAI إرسال الطلبات إلى نقطة نهاية Gemini API بدلاً من عنوان URL التلقائي.
- **`model="gemini-3-flash-preview"`**: اختَر نموذج Gemini متوافقًا

## جارٍ التفكير

تم تدريب نماذج Gemini على التفكير في المشاكل المعقّدة، ما يؤدي إلى تحسين كبير في عملية الاستدلال. تتضمّن Gemini API مَعلمات [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar) التي تمنحك تحكّمًا دقيقًا
في مقدار التفكير الذي سيجريه النموذج.

تتضمّن نماذج Gemini المختلفة إعدادات استدلال مختلفة، ويمكنك الاطّلاع على كيفية ربطها بجهود OpenAI في مجال الاستدلال على النحو التالي:

| `reasoning_effort` (OpenAI) | `thinking_level` (‫Gemini 3.1 Pro) | `thinking_level` (‫Gemini 3.1 Flash-Lite) | `thinking_level` (‫Gemini 3 Flash) | `thinking_budget` (‫Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

[[إذا لم يتم تحديد `reasoning_effort`، يستخدم Gemini المستوى أو الميزانية التلقائية للنموذج.](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#levels)](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#set-budget)

إذا أردت إيقاف التفكير، يمكنك ضبط `reasoning_effort` على `"none"` لنماذج
2.5. لا يمكن إيقاف الاستدلال لنماذج Gemini 2.5 Pro أو 3.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    reasoning_effort: "low",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

تنتج نماذج التفكير في Gemini أيضًا [ملخّصات للأفكار](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#summaries).
يمكنك استخدام الحقل [`extra_body`](#extra-body) لتضمين حقول Gemini
في طلبك.

يُرجى العِلم أنّ `reasoning_effort` و`thinking_level`/`thinking_budget` تتداخلان في الوظائف، لذا لا يمكن استخدامهما في الوقت نفسه.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[{"role": "user", "content": "Explain to me how AI works"}],
    extra_body={
      'extra_body': {
        "google": {
          "thinking_config": {
            "thinking_level": "low",
            "include_thoughts": True
          }
        }
      }
    }
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [{role: "user", content: "Explain to me how AI works",}],
    extra_body: {
      "google": {
        "thinking_config": {
          "thinking_level": "low",
          "include_thoughts": true
        }
      }
    }
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3-flash-preview",
        "messages": [{"role": "user", "content": "Explain to me how AI works"}],
        "extra_body": {
          "google": {
            "thinking_config": {
              "thinking_level": "low",
              "include_thoughts": true
            }
          }
        }
      }'
```

يتوافق Gemini 3 مع OpenAI لتوقيعات الأفكار في واجهات برمجة التطبيقات لإكمال المحادثات. يمكنك الاطّلاع على المثال الكامل في صفحة [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar#openai).

## البث

[تتيح Gemini API بث الردود.](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=ar#generate-a-text-stream)

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {   "role": "user",
        "content": "Hello!"
    }
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
      {
          "role": "system",
          "content": "You are a helpful assistant."
      },
      {
          "role": "user",
          "content": "Hello!"
      }
    ],
    stream: true,
  });

  for await (const chunk of completion) {
    console.log(chunk.choices[0].delta.content);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3-flash-preview",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## استدعاء الدالة

تسهّل عليك ميزة "استدعاء الدالة" الحصول على بيانات منظَّمة من
النماذج التوليدية، وهي [متاحة في Gemini API](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=ar).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}]
response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}];
  const tools = [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. Chicago, IL",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
          },
        }
      }
  ];

  const response = await openai.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: messages,
    tools: tools,
    tool_choice: "auto",
  });

  console.log(response);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
  "model": "gemini-3-flash-preview",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Chicago today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. Chicago, IL"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

## فهم الصور

نماذج Gemini هي نماذج متعددة الوسائط بشكل أساسي وتقدّم أفضل أداء في فئتها على
[العديد من مهام الرؤية الشائعة](https://ai.google.dev/gemini-api/docs/vision?hl=ar).

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")

response = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

### JavaScript

```
import OpenAI from "openai";
import fs from 'fs/promises';

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function encodeImage(imagePath) {
  try {
    const imageBuffer = await fs.readFile(imagePath);
    return imageBuffer.toString('base64');
  } catch (error) {
    console.error("Error encoding image:", error);
    return null;
  }
}

async function main() {
  const imagePath = "Path/to/agi/image.jpeg";
  const base64Image = await encodeImage(imagePath);

  const messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": `data:image/jpeg;base64,${base64Image}`
          },
        },
      ],
    }
  ];

  try {
    const response = await openai.chat.completions.create({
      model: "gemini-3-flash-preview",
      messages: messages,
    });

    console.log(response.choices[0]);
  } catch (error) {
    console.error("Error calling Gemini API:", error);
  }
}

main();
```

### REST

```
bash -c '
  base64_image=$(base64 -i "Path/to/agi/image.jpeg");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3-flash-preview\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"What is in this image?\" },
            {
              \"type\": \"image_url\",
              \"image_url\": { \"url\": \"data:image/jpeg;base64,${base64_image}\" }
            }
          ]
        }
      ]
    }"
'
```

## إنشاء صورة

يمكنك إنشاء صورة باستخدام `gemini-2.5-flash-image` أو `gemini-3-pro-image-preview`. تشمل المَعلمات المتوافقة `prompt` و`model` و`n` و`size` و`response_format`. سيتم تجاهل أي مَعلمات أخرى غير مُدرَجة هنا أو في قسم [`extra_body`](#extra-body) بدون إشعار من قِبل طبقة التوافق.

### Python

```
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="a portrait of a sheepadoodle wearing a cape",
    response_format='b64_json',
    n=1,
)

for image_data in response.data:
  image = Image.open(BytesIO(base64.b64decode(image_data.b64_json)))
  image.show()
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const image = await openai.images.generate(
    {
      model: "gemini-2.5-flash-image",
      prompt: "a portrait of a sheepadoodle wearing a cape",
      response_format: "b64_json",
      n: 1,
    }
  );

  console.log(image.data);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
        "model": "gemini-2.5-flash-image",
        "prompt": "a portrait of a sheepadoodle wearing a cape",
        "response_format": "b64_json",
        "n": 1,
      }'
```

## إنشاء فيديو

يمكنك إنشاء فيديو باستخدام `veo-3.1-generate-preview` من خلال نقطة النهاية `/v1/videos` المتوافقة مع Sora. المَعلمتان المتوافقتان على المستوى الأعلى هما `prompt` و`model`. يجب تمرير المَعلمات الإضافية، مثل `duration_seconds` و`image` و`aspect_ratio`، باستخدام `extra_body`. راجِع قسم [`extra_body`](#extra-body)
للاطّلاع على جميع المَعلمات المتاحة.

إنشاء الفيديو هو عملية تشغيل طويلة المدى تعرض رقم تعريف عملية يمكنك إجراء طلبات بحث عنه لمعرفة ما إذا اكتملت:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Returns a Long Running Operation (status: processing)
response = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="A cinematic drone shot of a waterfall",
)

print(f"Operation ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Returns a Long Running Operation (status: processing)
    const response = await openai.videos.create({
        model: "veo-3.1-generate-preview",
        prompt: "A cinematic drone shot of a waterfall",
    });

    console.log(`Operation ID: ${response.id}`);
    console.log(`Status: ${response.status}`);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=A cinematic drone shot of a waterfall"
```

### الاطّلاع على حالة الفيديو

يتم إنشاء الفيديو بشكل غير متزامن. استخدِم `GET /v1/videos/{id}` للاطّلاع على الحالة واسترداد عنوان URL النهائي للفيديو عند اكتماله:

### Python

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Poll until video is ready
video_id = response.id  # From the create call
while True:
    video = client.videos.retrieve(video_id)
    if video.status == "completed":
        print(f"Video URL: {video.url}")
        break
    elif video.status == "failed":
        print(f"Generation failed: {video.error}")
        break
    print(f"Status: {video.status}. Waiting...")
    time.sleep(10)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Poll until video is ready
    const videoId = response.id;  // From the create call
    while (true) {
        const video = await openai.videos.retrieve(videoId);
        if (video.status === "completed") {
            console.log(`Video URL: ${video.url}`);
            break;
        } else if (video.status === "failed") {
            console.log(`Generation failed: ${video.error}`);
            break;
        }
        console.log(`Status: ${video.status}. Waiting...`);
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos/VIDEO_ID" \
  -H "Authorization: Bearer $GEMINI_API_KEY"
```

## فهم الصوت

يمكنك تحليل الإدخال الصوتي:

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("/path/to/your/audio/file.wav", "rb") as audio_file:
  base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio",
        },
        {
              "type": "input_audio",
              "input_audio": {
                "data": base64_audio,
                "format": "wav"
          }
        }
      ],
    }
  ],
)

print(response.choices[0].message.content)
```

### JavaScript

```
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

const audioFile = fs.readFileSync("/path/to/your/audio/file.wav");
const base64Audio = Buffer.from(audioFile).toString("base64");

async function main() {
  const response = await client.chat.completions.create({
    model: "gemini-3-flash-preview",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Transcribe this audio",
          },
          {
            type: "input_audio",
            input_audio: {
              data: base64Audio,
              format: "wav",
            },
          },
        ],
      },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### REST

```
bash -c '
  base64_audio=$(base64 -i "/path/to/your/audio/file.wav");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3-flash-preview\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"Transcribe this audio file.\" },
            {
              \"type\": \"input_audio\",
              \"input_audio\": {
                \"data\": \"${base64_audio}\",
                \"format\": \"wav\"
              }
            }
          ]
        }
      ]
    }"
'
```

## ناتج منظَّم

يمكن لنماذج Gemini عرض كائنات JSON بأي [بنية تحدّدها](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar).

### Python

```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### JavaScript

```
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai"
});

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.chat.completions.parse({
  model: "gemini-3-flash-preview",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## التضمينات

تقيس تضمينات النصوص مدى الصلة بين السلاسل النصية ويمكن إنشاؤها
باستخدام [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar). يمكنك استخدام `gemini-embedding-2-preview` للتضمينات المتعددة الوسائط أو `gemini-embedding-001` للتضمينات النصية فقط.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="gemini-embedding-2-preview"
)

print(response.data[0].embedding)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const embedding = await openai.embeddings.create({
    model: "gemini-embedding-2-preview",
    input: "Your text string goes here",
  });

  console.log(embedding);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/embeddings" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
    "input": "Your text string goes here",
    "model": "gemini-embedding-2-preview"
  }'
```

## Batch API

يمكنك إنشاء [مهام مجمّعة](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ar) وإرسالها والاطّلاع على حالتها
باستخدام مكتبة OpenAI.

عليك إعداد ملف JSONL بتنسيق الإدخال في OpenAI. على سبيل المثال:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

يتوافق Batch مع OpenAI، ما يتيح إنشاء مجموعة ورصد حالة المهمة وعرض نتائج المجموعة.

التوافق مع التحميل والتنزيل غير متاح حاليًا. [بدلاً من ذلك، يستخدم المثال التالي برنامج `genai` لتحميل الملفات وتنزيلها، تمامًا كما هو الحال عند استخدام Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ar#input-file).](https://ai.google.dev/gemini-api/docs/files?hl=ar)

### Python

```
from openai import OpenAI

# Regular genai client for uploads & downloads
from google import genai
client = genai.Client()

openai_client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Upload the JSONL file in OpenAI input format, using regular genai SDK
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

# Create batch
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Wait for batch to finish (up to 24h)
while True:
    batch = client.batches.retrieve(batch.id)
    if batch.status in ('completed', 'failed', 'cancelled', 'expired'):
        break
    print(f"Batch not finished. Current state: {batch.status}. Waiting 30 seconds...")
    time.sleep(30)
print(f"Batch finished: {batch}")

# Download results in OpenAI output format, using regular genai SDK
file_content = genai_client.files.download(file=batch.output_file_id).decode('utf-8')

# See batch_output JSONL in OpenAI output format
for line in file_content.splitlines():
    print(line)
```

تتيح حزمة تطوير البرامج (SDK) من OpenAI أيضًا [إنشاء تضمينات باستخدام Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar#batch-embeddings). لإجراء ذلك، بدِّل حقل `endpoint` في طريقة `create` بنقطة نهاية للتضمينات، بالإضافة إلى المفتاحَين `url` و`model` في ملف JSONL:

```
# JSONL file using embeddings model and endpoint
# {"custom_id": "request-1", "method": "POST", "url": "/v1/embeddings", "body": {"model": "ggemini-embedding-001", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
# {"custom_id": "request-2", "method": "POST", "url": "/v1/embeddings", "body": {"model": "gemini-embedding-001", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}

# ...

# Create batch step with embeddings endpoint
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/embeddings",
    completion_window="24h"
)
```

يمكنك الاطّلاع على مثال كامل في قسم [إنشاء تضمينات مجمّعة](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)
في دليل استخدام التوافق مع OpenAI.

## الاستدلال المرن والاستدلال حسب الأولوية

تطابق Gemini API المَعلمة `service_tier` من OpenAI في الاسم والمنطق، ما يفرض حدودًا ويوجه حركة المرور بشكل مناسب لكل من مستويَي الاستدلال المرن والاستدلال حسب الأولوية.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3-flash-preview",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

إذا لم يتم تحديد `service_tier` بشكل صريح، يتم ضبطها تلقائيًا على `standard`، وهو ما يعادل `default` في OpenAI.
يمكنك التعرّف أكثر على مستويات الاستدلال في مستندات [التحسين](https://ai.google.dev/gemini-api/docs/optimization?hl=ar).

## تفعيل ميزات Gemini باستخدام `extra_body`

تتوفّر عدة ميزات في Gemini لا تتوفّر في نماذج OpenAI، ولكن يمكن تفعيلها باستخدام الحقل `extra_body`.

| المَعلمة | النوع | نقطة نهاية | الوصف |
| --- | --- | --- | --- |
| **`cached_content`** | نص | محادثة | يتطابق مع ذاكرة التخزين المؤقت العامة للمحتوى في Gemini. |
| **`thinking_config`** | عنصر | محادثة | يتطابق مع ThinkingConfig في Gemini. |
| **`aspect_ratio`** | نص | الصور | نسبة العرض إلى الارتفاع للناتج (مثل `"16:9"` أو `"1:1"` أو `"9:16"`) |
| **`generation_config`** | عنصر | الصور | عنصر إعدادات الإنشاء في Gemini (مثل `{"responseModalities": ["IMAGE"], "candidateCount": 2}`) |
| **`safety_settings`** | قائمة | الصور | فلاتر مخصّصة للحدود القصوى للأمان (مثل `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`) |
| **`tools`** | قائمة | الصور | تفعيل الاستناد إلى "بحث Google" (مثل `[{"google_search": {}}]`)، وذلك لنموذج `gemini-3-pro-image-preview` فقط |
| **`aspect_ratio`** | نص | فيديو | أبعاد الفيديو الناتج (`16:9` للفيديوهات الأفقية و`9:16` للفيديوهات العمودية) يتم الربط من `size` إذا لم يتم تحديدها. |
| **`resolution`** | نص | فيديو | درجة الدقة للناتج (`720p` أو `1080p` أو `4K`) ملاحظة: تؤدي `1080p` و`4K` إلى تشغيل سلسلة التعديل التصاعدي. |
| **`duration_seconds`** | عدد صحيح | فيديو | مدة الإنشاء (القيم: `4` أو `6` أو `8`) يجب أن تكون `8` عند استخدام `reference_images` أو الاستيفاء أو الإضافة. |
| **`frame_rate`** | نص | فيديو | عدد اللقطات في الثانية للفيديو الناتج (مثل `"24"`) |
| **`input_reference`** | نص | فيديو | الإدخال المرجعي لإنشاء الفيديو |
| **`extend_video_id`** | نص | فيديو | رقم تعريف فيديو حالي لتمديده |
| **`negative_prompt`** | نص | فيديو | العناصر التي يجب استبعادها (مثل `"shaky camera"`) |
| **`seed`** | عدد صحيح | فيديو | عدد صحيح للإنشاء الحتمي |
| **`style`** | نص | فيديو | النمط المرئي (`cinematic` تلقائيًا، و`creative` للفيديوهات المحسّنة لوسائل التواصل الاجتماعي) |
| **`person_generation`** | نص | فيديو | التحكّم في إنشاء صور تتضمّن أشخاصًا (`allow_adult` أو `allow_all` أو `dont_allow`) |
| **`reference_images`** | قائمة | فيديو | ما يصل إلى 3 صور كمرجع للنمط/الشخصية (مواد عرض base64) |
| **`image`** | نص | فيديو | صورة الإدخال الأولية بترميز base64 لتحديد عملية إنشاء الفيديو |
| **`last_frame`** | عنصر | فيديو | الصورة النهائية للاستيفاء (تتطلّب `image` كإطار أول) |

### مثال على استخدام `extra_body`

في ما يلي مثال على استخدام `extra_body` لضبط `cached_content`:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3-flash-preview",
    n=1,
    messages=[
        {
            "role": "user",
            "content": "Summarize the video"
        }
    ],
    stream=True,
    stream_options={'include_usage': True},
    extra_body={
        'extra_body':
        {
            'google': {
              'cached_content': "cachedContents/0000aaaa1111bbbb2222cccc3333dddd4444eeee"
          }
        }
    }
)

for chunk in stream:
    print(chunk)
    print(chunk.usage.to_dict())
```

## عرض قائمة النماذج

يمكنك الحصول على قائمة بنماذج Gemini المتاحة:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

models = client.models.list()
for model in models:
  print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## استرداد نموذج

يمكنك استرداد نموذج Gemini:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3-flash-preview")
print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3-flash-preview");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3-flash-preview \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## القيود الحالية

لا يزال دعم مكتبات OpenAI في مرحلة تجريبية أثناء توسيع نطاق دعم الميزات.

إذا كانت لديك أسئلة حول المَعلمات المتوافقة أو الميزات القادمة أو واجهت
أي مشاكل في البدء باستخدام Gemini، يُرجى الانضمام إلى [منتدى المطوّرين](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

يمكنك تجربة [Colab المتوافق مع OpenAI](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=ar) للتعرّف على المزيد من الأمثلة التفصيلية.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
