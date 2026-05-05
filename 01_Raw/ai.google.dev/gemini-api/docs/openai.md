---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=hi
fetched_at: 2026-05-05T20:43:47.181146+00:00
title: "OpenAI \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0938\u093e\u0925 \u0915\u093e\u092e \u0915\u0930\u0924\u093e \u0939\u0948 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# OpenAI की सुविधा के साथ काम करता है

Gemini मॉडल को OpenAI लाइब्रेरी (Python और TypeScript / JavaScript) के साथ-साथ REST API का इस्तेमाल करके ऐक्सेस किया जा सकता है. इसके लिए, आपको कोड की तीन लाइनें अपडेट करनी होंगी और [Gemini API कुंजी](https://aistudio.google.com/apikey?hl=hi) का इस्तेमाल करना होगा. अगर OpenAI लाइब्रेरी का इस्तेमाल पहले से नहीं किया जा रहा है, तो हमारा सुझाव है कि आप [Gemini API को सीधे तौर पर कॉल करें](https://ai.google.dev/gemini-api/docs/quickstart?hl=hi).

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

क्या बदलाव हुए हैं? सिर्फ़ तीन लाइनें!

- **`api_key="GEMINI_API_KEY"`**: "`GEMINI_API_KEY`" को अपने Gemini API पासकोड से बदलें. यह पासकोड आपको [Google AI Studio](https://aistudio.google.com?hl=hi) में मिलेगा.
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** इससे OpenAI लाइब्रेरी को यह पता चलता है कि उसे डिफ़ॉल्ट यूआरएल के बजाय, Gemini API एंडपॉइंट को अनुरोध भेजने हैं.
- **`model="gemini-3-flash-preview"`**: Gemini का ऐसा मॉडल चुनें जो इस सुविधा के साथ काम करता हो

## सूझ-बूझ वाला मॉडल

Gemini मॉडल को मुश्किल समस्याओं के बारे में सोचने के लिए ट्रेन किया गया है. इससे, तर्क करने की क्षमता में काफ़ी सुधार हुआ है. Gemini API में [सोचने के पैरामीटर](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) होते हैं. इनसे यह तय किया जा सकता है कि मॉडल को कितना सोचना है.

Gemini के अलग-अलग मॉडल में, तर्क देने की क्षमता अलग-अलग होती है. OpenAI के तर्क देने की क्षमता के हिसाब से, Gemini के मॉडल की तुलना यहाँ की गई है:

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

अगर कोई `reasoning_effort` नहीं दी गई है, तो Gemini, मॉडल के डिफ़ॉल्ट [लेवल](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#levels) या [बजट](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#set-budget) का इस्तेमाल करता है.

अगर आपको सूझ-बूझ वाली सुविधा बंद करनी है, तो 2.5 मॉडल के लिए `reasoning_effort` को `"none"` पर सेट करें. Gemini 2.5 Pro या 3 मॉडल के लिए, तर्क करने की सुविधा बंद नहीं की जा सकती.

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

Gemini के थिंकिंग मॉडल, [सोच-विचार की खास जानकारी](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#summaries) भी जनरेट करते हैं.
अपने अनुरोध में Gemini फ़ील्ड शामिल करने के लिए, [`extra_body`](#extra-body) फ़ील्ड का इस्तेमाल किया जा सकता है.

ध्यान दें कि `reasoning_effort` और `thinking_level`/`thinking_budget` की सुविधाएं एक जैसी होती हैं. इसलिए, इन्हें एक साथ इस्तेमाल नहीं किया जा सकता.

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

Gemini 3, चैट पूरी करने वाले एपीआई में थॉट सिग्नेचर के लिए OpenAI के साथ काम करता है. पूरा उदाहरण देखने के लिए, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi#openai) पेज पर जाएं.

## स्ट्रीमिंग

Gemini API, [स्ट्रीमिंग रिस्पॉन्स](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=hi#generate-a-text-stream) की सुविधा के साथ काम करता है.

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

## फ़ंक्शन कॉल करने की सुविधा

Function calling की मदद से, जनरेटिव मॉडल से स्ट्रक्चर्ड डेटा आउटपुट पाना आसान हो जाता है. यह सुविधा [Gemini API में उपलब्ध है](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=hi).

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

## इमेज की बारीक़ी से पहचान

Gemini मॉडल, नेटिव तौर पर मल्टीमॉडल होते हैं. साथ ही, [कई सामान्य विज़न टास्क](https://ai.google.dev/gemini-api/docs/vision?hl=hi) में बेहतरीन परफ़ॉर्मेंस देते हैं.

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

## इमेज जनरेट करें

`gemini-2.5-flash-image` या `gemini-3-pro-image-preview` का इस्तेमाल करके इमेज जनरेट करें. `prompt`, `model`, `n`, `size`, और `response_format` जैसे पैरामीटर इस्तेमाल किए जा सकते हैं. यहां या [`extra_body`](#extra-body) सेक्शन में शामिल नहीं किए गए अन्य पैरामीटर को कंपैटिबिलिटी लेयर चुपचाप अनदेखा कर देगी.

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

## वीडियो जनरेट करना

Sora के साथ काम करने वाले `/v1/videos` एंडपॉइंट के ज़रिए, `veo-3.1-generate-preview` का इस्तेमाल करके वीडियो जनरेट करें. `prompt` और `model` को टॉप-लेवल पैरामीटर के तौर पर इस्तेमाल किया जा सकता है. `duration_seconds`, `image`, और `aspect_ratio` जैसे अतिरिक्त पैरामीटर, `extra_body` के साथ पास किए जाने चाहिए. सभी उपलब्ध पैरामीटर के लिए, [`extra_body`](#extra-body) सेक्शन देखें.

वीडियो जनरेट करने की प्रोसेस में ज़्यादा समय लगता है. यह प्रोसेस पूरी होने पर, आपको एक ऑपरेशन आईडी मिलता है. इस आईडी का इस्तेमाल करके, प्रोसेस पूरी होने की स्थिति की जानकारी पाई जा सकती है.

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

### वीडियो की स्थिति देखना

वीडियो जनरेट करने की प्रोसेस एसिंक्रोनस होती है. स्टेटस की जानकारी पाने के लिए `GET /v1/videos/{id}` का इस्तेमाल करें. साथ ही, प्रोसेस पूरी होने पर फ़ाइनल वीडियो यूआरएल पाएं:

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

## ऑडियो को समझना

ऑडियो इनपुट का विश्लेषण करना:

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

## स्ट्रक्चर्ड आउटपुट

Gemini मॉडल, JSON ऑब्जेक्ट को [आपके तय किए गए किसी भी स्ट्रक्चर](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) में आउटपुट कर सकते हैं.

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

## एंबेड करना

टेक्स्ट एम्बेडिंग से, टेक्स्ट स्ट्रिंग के बीच समानता का पता चलता है. इन्हें [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) का इस्तेमाल करके जनरेट किया जा सकता है. मल्टीमॉडल एम्बेडिंग के लिए `gemini-embedding-2-preview` या सिर्फ़ टेक्स्ट वाली एम्बेडिंग के लिए `gemini-embedding-001` का इस्तेमाल किया जा सकता है.

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

OpenAI लाइब्रेरी का इस्तेमाल करके, [बैच जॉब](https://ai.google.dev/gemini-api/docs/batch-mode?hl=hi) बनाए जा सकते हैं. साथ ही, उन्हें सबमिट किया जा सकता है और उनकी स्थिति देखी जा सकती है.

आपको OpenAI के इनपुट फ़ॉर्मैट में JSONL फ़ाइल तैयार करनी होगी. उदाहरण के लिए:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

OpenAI के साथ काम करने की सुविधा के ज़रिए, बैच के लिए ये काम किए जा सकते हैं: बैच बनाना, जॉब की स्थिति को मॉनिटर करना, और बैच के नतीजे देखना.

फ़िलहाल, अपलोड और डाउनलोड करने की सुविधा उपलब्ध नहीं है. इसके बजाय, यहां दिए गए उदाहरण में `genai` क्लाइंट का इस्तेमाल करके [फ़ाइलें](https://ai.google.dev/gemini-api/docs/files?hl=hi) अपलोड और डाउनलोड की गई हैं. ऐसा Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=hi#input-file) का इस्तेमाल करते समय भी किया जाता है.

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

OpenAI SDK, [Batch API की मदद से एम्बेडिंग जनरेट करने](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi#batch-embeddings) की सुविधा भी देता है. इसके लिए, JSONL फ़ाइल में `create` तरीके के `endpoint` फ़ील्ड को एम्बेडिंग एंडपॉइंट के लिए बदलें. साथ ही, `url` और `model` कुंजियों को भी बदलें:

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

पूरे उदाहरण के लिए, OpenAI के साथ काम करने वाले कुकबुक का [बैच एम्बेडिंग जनरेशन](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb) सेक्शन देखें.

## Flex और प्राथमिकता का अनुमान लगाने की सुविधा

Gemini API, नाम और लॉजिक के मामले में OpenAI के `service_tier` पैरामीटर से मेल खाता है. यह Flex और Priority, दोनों इन्फ़्रेंस टियर के लिए सीमाएं लागू करता है और ट्रैफ़िक को सही तरीके से मैनेज करता है.

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

अगर `service_tier` को साफ़ तौर पर असाइन नहीं किया जाता है, तो यह डिफ़ॉल्ट रूप से `standard` पर सेट होता है. यह OpenAI के लिए `default` के बराबर होता है.
[ऑप्टिमाइज़ेशन](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) दस्तावेज़ में, अनुमान के टियर के बारे में ज़्यादा जानें.

## `extra_body` के साथ Gemini की सुविधाएँ चालू करना

Gemini में ऐसी कई सुविधाएँ उपलब्ध हैं जो OpenAI के मॉडल में नहीं हैं. हालाँकि, `extra_body` फ़ील्ड का इस्तेमाल करके इन सुविधाओं को चालू किया जा सकता है.

| पैरामीटर | टाइप | एंडपॉइंट | ब्यौरा |
| --- | --- | --- | --- |
| **`cached_content`** | टेक्स्ट | Chat | यह Gemini की सामान्य कॉन्टेंट कैश मेमोरी से मेल खाती है. |
| **`thinking_config`** | ऑब्जेक्ट | Chat | यह Gemini के ThinkingConfig से मेल खाता है. |
| **`aspect_ratio`** | टेक्स्ट | इमेज | आउटपुट का आसपेक्ट रेशियो (जैसे, `"16:9"`, `"1:1"`, `"9:16"`). |
| **`generation_config`** | ऑब्जेक्ट | इमेज | Gemini जनरेशन कॉन्फ़िगरेशन ऑब्जेक्ट (जैसे, `{"responseModalities": ["IMAGE"], "candidateCount": 2}`). |
| **`safety_settings`** | सूची | इमेज | सुरक्षा थ्रेशोल्ड के कस्टम फ़िल्टर (जैसे, `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`). |
| **`tools`** | सूची | इमेज | ग्राउंडिंग की सुविधा चालू करता है (जैसे, `[{"google_search": {}}]`). यह सिर्फ़ `gemini-3-pro-image-preview` के लिए है. |
| **`aspect_ratio`** | टेक्स्ट | वीडियो | आउटपुट वीडियो के डाइमेंशन (लैंडस्केप के लिए `16:9`, पोर्ट्रेट के लिए `9:16`). अगर कुछ नहीं बताया गया है, तो `size` से मैप किए जाते हैं. |
| **`resolution`** | टेक्स्ट | वीडियो | आउटपुट रिज़ॉल्यूशन (`720p`, `1080p`, `4K`). ध्यान दें: `1080p` और `4K`, अपसैंपलर पाइपलाइन को ट्रिगर करते हैं. |
| **`duration_seconds`** | पूर्णांक | वीडियो | जनरेट किए गए जवाब की लंबाई (वैल्यू: `4`, `6`, `8`). `reference_images`, इंटरपोलेशन या एक्सटेंशन का इस्तेमाल करते समय, इसकी वैल्यू `8` होनी चाहिए. |
| **`frame_rate`** | टेक्स्ट | वीडियो | वीडियो आउटपुट के लिए फ़्रेम रेट (जैसे, `"24"`). |
| **`input_reference`** | टेक्स्ट | वीडियो | वीडियो जनरेट करने के लिए रेफ़रंस इनपुट. |
| **`extend_video_id`** | टेक्स्ट | वीडियो | उस मौजूदा वीडियो का आईडी जिसकी अवधि बढ़ानी है. |
| **`negative_prompt`** | टेक्स्ट | वीडियो | शामिल न किए जाने वाले आइटम (जैसे, `"shaky camera"`). |
| **`seed`** | पूर्णांक | वीडियो | डिटरमिनिस्टिक जनरेशन के लिए पूर्णांक. |
| **`style`** | टेक्स्ट | वीडियो | विज़ुअल स्टाइलिंग (`cinematic` डिफ़ॉल्ट, `creative` सोशल मीडिया के लिए ऑप्टिमाइज़ की गई). |
| **`person_generation`** | टेक्स्ट | वीडियो | इससे लोगों की इमेज जनरेट करने की सुविधा को कंट्रोल किया जाता है (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | सूची | वीडियो | स्टाइल/कैरेक्टर के रेफ़रंस के लिए ज़्यादा से ज़्यादा तीन इमेज (base64 ऐसेट). |
| **`image`** | टेक्स्ट | वीडियो | वीडियो जनरेट करने के लिए, Base64 कोड में बदली गई शुरुआती इनपुट इमेज. |
| **`last_frame`** | ऑब्जेक्ट | वीडियो | इंटरपोलेशन के लिए फ़ाइनल इमेज (इसके लिए, पहले फ़्रेम के तौर पर `image` की ज़रूरत होती है). |

### `extra_body` का इस्तेमाल करने का उदाहरण

यहां `cached_content` को सेट करने के लिए, `extra_body` का इस्तेमाल करने का एक उदाहरण दिया गया है:

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

## मॉडल की सूची बनाना

उपलब्ध Gemini मॉडल की सूची पाने के लिए:

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

## किसी मॉडल को फिर से पाना

Gemini मॉडल को वापस पाएं:

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

## मौजूदा सीमाएं

OpenAI लाइब्रेरी के लिए सहायता अब भी बीटा वर्शन में है. हम इस सुविधा के लिए सहायता उपलब्ध करा रहे हैं.

अगर आपको Gemini के साथ काम करने वाले पैरामीटर, आने वाली सुविधाओं या Gemini का इस्तेमाल शुरू करने से जुड़ी किसी समस्या के बारे में कोई सवाल पूछना है, तो हमारे [डेवलपर फ़ोरम](https://discuss.ai.google.dev/c/gemini-api/4?hl=hi) में शामिल हों.

## आगे क्या करना है

ज़्यादा जानकारी वाले उदाहरणों को समझने के लिए, [OpenAI के साथ काम करने वाले Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=hi) को आज़माएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया."],[],[]]
