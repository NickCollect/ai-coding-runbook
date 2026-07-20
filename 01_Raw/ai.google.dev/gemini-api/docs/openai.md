---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=hi
fetched_at: 2026-07-20T04:33:36.302951+00:00
title: "OpenAI \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u0915\u0947 \u0938\u093e\u0925 \u0915\u093e\u092e \u0915\u0930\u0924\u093e \u0939\u0948 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# OpenAI की सुविधा के साथ काम करता है

OpenAI की लाइब्रेरी (Python और TypeScript /
Javascript) के साथ-साथ, REST API का इस्तेमाल करके Gemini के मॉडल ऐक्सेस किए जा सकते हैं. इसके लिए, आपको कोड की तीन लाइनों को अपडेट करना होगा
और अपने [Gemini API पासकोड](https://aistudio.google.com/apikey?hl=hi) का इस्तेमाल करना होगा. अगर OpenAI की लाइब्रेरी का इस्तेमाल नहीं किया जा रहा है, तो हमारा सुझाव है कि
आप
[Gemini API को सीधे तौर पर कॉल करें](https://ai.google.dev/gemini-api/docs/get-started?hl=hi).

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

क्या बदला है? सिर्फ़ तीन लाइनें!

- **`api_key="GEMINI_API_KEY"`**: "`GEMINI_API_KEY`" को अपने Gemini
  API पासकोड से बदलें. यह पासकोड, [Google AI Studio](https://aistudio.google.com?hl=hi) में पाया जा सकता है.
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** इससे OpenAI की लाइब्रेरी को यह निर्देश मिलता है कि वह अनुरोधों को डिफ़ॉल्ट यूआरएल के बजाय, Gemini API एंडपॉइंट पर भेजे.
- **`model="gemini-3.5-flash"`**: Gemini का कोई ऐसा मॉडल चुनें जो इस सुविधा के साथ काम करता हो

## सूझ-बूझ वाला मॉडल

Gemini के मॉडल को मुश्किल समस्याओं को हल करने के लिए ट्रेन किया गया है. इससे, तर्क करने की क्षमता में काफ़ी सुधार होता है. Gemini API में, [सूझ-बूझ वाले पैरामीटर](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) शामिल हैं. इनसे यह तय किया जा सकता है कि मॉडल को किसी समस्या को हल करने में कितना समय लगेगा.

Gemini के अलग-अलग मॉडल में, तर्क करने के लिए अलग-अलग कॉन्फ़िगरेशन होते हैं. यहां बताया गया है कि ये कॉन्फ़िगरेशन, OpenAI के तर्क करने की कोशिशों से कैसे मैप होते हैं:

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

अगर `reasoning_effort` तय नहीं किया जाता है, तो Gemini, मॉडल के
डिफ़ॉल्ट [लेवल](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#levels) या [बजट](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#set-budget) का इस्तेमाल करता है.

अगर आपको सूझ-बूझ वाली सुविधा बंद करनी है, तो
2.5 मॉडल के लिए, `reasoning_effort` को `"none"` पर सेट करें. Gemini 2.5 Pro या 3 मॉडल के लिए, तर्क करने की सुविधा बंद नहीं की जा सकती.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
    "model": "gemini-3.5-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Gemini के सूझ-बूझ वाले मॉडल, [सोच-समझकर जवाब देते हैं](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#summaries).
अपने अनुरोध में Gemini के फ़ील्ड शामिल करने के लिए, [`extra_body`](#extra-body) फ़ील्ड का इस्तेमाल किया जा सकता है.

ध्यान दें कि `reasoning_effort` और `thinking_level`/`thinking_budget` की सुविधाएं एक जैसी हैं. इसलिए, इनका इस्तेमाल एक साथ नहीं किया जा सकता.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "model": "gemini-3.5-flash",
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

Gemini 3, चैट पूरी करने वाले एपीआई में, सोच-समझकर जवाब देने की सुविधा के लिए, OpenAI के साथ काम करता है. सोच-समझकर जवाब देने की सुविधा के बारे में पूरी जानकारी, इस [पेज](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi#openai) पर देखी जा सकती है.

## स्ट्रीमिंग

Gemini API, [स्ट्रीमिंग के ज़रिए जवाब देने की सुविधा](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=hi#generate-a-text-stream) के साथ काम करता है.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      "model": "gemini-3.5-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## फ़ंक्शन कॉल करना

[फ़ंक्शन कॉल करने की सुविधा से, जनरेटिव मॉडल से स्ट्रक्चर्ड डेटा आउटपुट पाना आसान हो जाता है. यह सुविधा, Gemini API में उपलब्ध है.](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=hi)

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
  model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
  "model": "gemini-3.5-flash",
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

Gemini के मॉडल, स्वाभाविक तौर पर मल्टीमॉडल होते हैं. साथ ही, ये विज़न से जुड़े कई सामान्य टास्क में
[बेहतरीन परफ़ॉर्मेंस देते हैं](https://ai.google.dev/gemini-api/docs/vision?hl=hi).

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
  model="gemini-3.5-flash",
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
      model: "gemini-3.5-flash",
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
      \"model\": \"gemini-3.5-flash\",
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

`gemini-2.5-flash-image` या `gemini-3-pro-image-preview` का इस्तेमाल करके कोई इमेज जनरेट करें. `prompt`, `model`, `n`, `size`, और `response_format` जैसे पैरामीटर इस्तेमाल किए जा सकते हैं. यहां या [`extra_body`](#extra-body) सेक्शन में शामिल न किए गए अन्य पैरामीटर को, कंपैटिबिलिटी लेयर अनदेखा कर देगी.

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

## एक वीडियो जनरेट करो

Sora के साथ काम करने वाले `/v1/videos` एंडपॉइंट के ज़रिए, `veo-3.1-generate-preview` का इस्तेमाल करके कोई वीडियो जनरेट करें. टॉप-लेवल के `prompt` और `model` पैरामीटर इस्तेमाल किए जा सकते हैं. `duration_seconds`, `image`, और `aspect_ratio` जैसे अतिरिक्त पैरामीटर, `extra_body` के साथ पास किए जाने चाहिए. सभी उपलब्ध पैरामीटर देखने के लिए, [`extra_body`](#extra-body) सेक्शन
देखें.

वीडियो जनरेट करने में ज़्यादा समय लगता है. यह सुविधा, एक ऑपरेशन आईडी दिखाती है. इस आईडी की मदद से, वीडियो जनरेट होने की प्रोसेस की स्थिति देखी जा सकती है.

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

वीडियो जनरेट करने की प्रोसेस एसिंक्रोनस होती है. वीडियो जनरेट होने की प्रोसेस की स्थिति देखने और वीडियो जनरेट होने के बाद, उसका फ़ाइनल यूआरएल पाने के लिए, `GET /v1/videos/{id}` का इस्तेमाल करें:

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

## ऑडियो की बारीक़ी से पहचान

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
      \"model\": \"gemini-3.5-flash\",
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

Gemini के मॉडल, आपकी तय की गई किसी भी [स्ट्रक्चर में JSON ऑब्जेक्ट आउटपुट कर सकते हैं](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi).

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
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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

टेक्स्ट एंबेडिंग से, टेक्स्ट स्ट्रिंग के बीच के संबंध का पता चलता है. इसे [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) का इस्तेमाल करके जनरेट किया जा सकता है.
मल्टीमॉडल एंबेडिंग के लिए `gemini-embedding-2-preview` या सिर्फ़ टेक्स्ट एंबेडिंग के लिए `gemini-embedding-001` का इस्तेमाल किया जा सकता है.

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

OpenAI की लाइब्रेरी का इस्तेमाल करके, [बैच जॉब](https://ai.google.dev/gemini-api/docs/batch-mode?hl=hi) बनाए जा सकते हैं, उन्हें सबमिट किया जा सकता है, और उनकी स्थिति देखी जा सकती है.

इसके लिए, आपको JSONL फ़ाइल को OpenAI के इनपुट फ़ॉर्मैट में तैयार करना होगा. उदाहरण के लिए:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

बैच के लिए OpenAI की कंपैटिबिलिटी की मदद से, बैच बनाया जा सकता है, जॉब की स्थिति पर नज़र रखी जा सकती है, और बैच के नतीजे देखे जा सकते हैं.

फ़िलहाल, अपलोड और डाउनलोड के लिए कंपैटिबिलिटी की सुविधा उपलब्ध नहीं है. [इसके बजाय, यहां दिए गए उदाहरण में, फ़ाइलें अपलोड और डाउनलोड करने के लिए `genai` क्लाइंट का इस्तेमाल किया गया है. यह तरीका, Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=hi#input-file) का इस्तेमाल करने के दौरान भी लागू होता है.](https://ai.google.dev/gemini-api/docs/files?hl=hi)

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

OpenAI SDK की मदद से, [Batch API का इस्तेमाल करके एंबेडिंग भी जनरेट की जा सकती हैं](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi#batch-embeddings). इसके लिए, JSONL फ़ाइल में `create` तरीके के `endpoint` फ़ील्ड को एंबेडिंग एंडपॉइंट के साथ-साथ, `url` और `model` कुंजियों को बदलें:

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

पूरे उदाहरण के लिए, OpenAI की कंपैटिबिलिटी कुकबुक का [बैच एंबेडिंग जनरेशन](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)
सेक्शन देखें.

## Flex और Priority इन्फ़रेंस

Gemini API, नाम और लॉजिक के मामले में OpenAI के `service_tier` पैरामीटर से मेल खाता है. यह Flex और Priority इन्फ़रेंस टियर, दोनों के लिए सीमाएं लागू करता है और ट्रैफ़िक को सही तरीके से डायरेक्ट करता है.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

अगर `service_tier` को साफ़ तौर पर असाइन नहीं किया जाता है, तो यह डिफ़ॉल्ट रूप से `standard` पर सेट होता है. यह OpenAI के लिए `default` के बराबर है.
इन्फ़रेंस टियर के बारे में ज़्यादा जानने के लिए, [ऑप्टिमाइज़ेशन](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) से जुड़ा दस्तावेज़ पढ़ें.

## `extra_body` का इस्तेमाल करके, Gemini की सुविधाएं चालू करना

Gemini की कई ऐसी सुविधाएं हैं जो OpenAI के मॉडल में उपलब्ध नहीं हैं. हालांकि, `extra_body` फ़ील्ड का इस्तेमाल करके, इन सुविधाओं को चालू किया जा सकता है.

| पैरामीटर | टाइप | एंडपॉइंट | ब्यौरा |
| --- | --- | --- | --- |
| **`cached_content`** | टेक्स्ट | Chat | यह Gemini के सामान्य कॉन्टेंट कैश से जुड़ा है. |
| **`thinking_config`** | ऑब्जेक्ट | Chat | यह Gemini के ThinkingConfig से जुड़ा है. |
| **`aspect_ratio`** | टेक्स्ट | इमेज | आउटपुट आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात). जैसे, `"16:9"`, `"1:1"`, `"9:16"`. |
| **`generation_config`** | ऑब्जेक्ट | इमेज | Gemini जनरेशन कॉन्फ़िग ऑब्जेक्ट. जैसे, `{"responseModalities": ["IMAGE"], "candidateCount": 2}`. |
| **`safety_settings`** | सूची | इमेज | सुरक्षा थ्रेशोल्ड के लिए कस्टम फ़िल्टर. जैसे, `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`. |
| **`tools`** | सूची | इमेज | ग्राउंडिंग की सुविधा चालू करता है. जैसे, `[{"google_search": {}}]`. यह सुविधा, सिर्फ़ `gemini-3-pro-image-preview` के लिए उपलब्ध है. |
| **`aspect_ratio`** | टेक्स्ट | वीडियो | आउटपुट वीडियो के डाइमेंशन (`16:9` लैंडस्केप के लिए, `9:16` पोर्ट्रेट के लिए). अगर यह तय नहीं किया जाता है, तो `size` से मैप होता है. |
| **`resolution`** | टेक्स्ट | वीडियो | आउटपुट रिज़ॉल्यूशन (`720p`, `1080p`, `4K`). ध्यान दें: `1080p` और `4K` से अपसैंपलर पाइपलाइन ट्रिगर होती है. |
| **`duration_seconds`** | पूर्णांक | वीडियो | जनरेशन की अवधि (वैल्यू: `4`, `6`, `8`). `reference_images`, इंटरपोलेशन या एक्सटेंशन का इस्तेमाल करते समय, इसकी वैल्यू `8` होनी चाहिए. |
| **`frame_rate`** | टेक्स्ट | वीडियो | वीडियो आउटपुट के लिए फ़्रेम रेट. जैसे, `"24"`. |
| **`input_reference`** | टेक्स्ट | वीडियो | वीडियो जनरेट करने के लिए रेफ़रंस इनपुट. |
| **`extend_video_id`** | टेक्स्ट | वीडियो | पहले से मौजूद किसी वीडियो को बढ़ाने के लिए उसका आईडी. |
| **`negative_prompt`** | टेक्स्ट | वीडियो | शामिल न किए जाने वाले आइटम. जैसे, `"shaky camera"`. |
| **`seed`** | पूर्णांक | वीडियो | डिटरमिनिस्टिक जनरेशन के लिए पूर्णांक. |
| **`style`** | टेक्स्ट | वीडियो | विज़ुअल स्टाइलिंग (`cinematic` डिफ़ॉल्ट, सोशल मीडिया के लिए ऑप्टिमाइज़ किया गया `creative`). |
| **`person_generation`** | टेक्स्ट | वीडियो | लोगों की इमेज जनरेट करने की सुविधा को कंट्रोल करता है (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | सूची | वीडियो | स्टाइल/कैरेक्टर रेफ़रंस के लिए ज़्यादा से ज़्यादा तीन इमेज (base64 ऐसेट). |
| **`image`** | टेक्स्ट | वीडियो | वीडियो जनरेट करने की प्रोसेस को कंडीशन करने के लिए, base64 कोड में बदली गई शुरुआती इनपुट इमेज. |
| **`last_frame`** | ऑब्जेक्ट | वीडियो | इंटरपोलेशन के लिए फ़ाइनल इमेज (`image` को पहले फ़्रेम के तौर पर इस्तेमाल करना ज़रूरी है). |

### `extra_body` का इस्तेमाल करने का उदाहरण

`cached_content` सेट करने के लिए, `extra_body` का इस्तेमाल करने का उदाहरण यहां दिया गया है:

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.5-flash",
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

## मॉडल की सूची पाना

उपलब्ध Gemini मॉडल की सूची पाना:

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

## कोई मॉडल वापस पाना

Gemini का कोई मॉडल वापस पाना:

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.5-flash")
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
  const model = await openai.models.retrieve("gemini-3.5-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.5-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## मौजूदा सीमाएं

फ़िलहाल, OpenAI की लाइब्रेरी के लिए सहायता की सुविधा बीटा वर्शन में है. हम इस सुविधा को बेहतर बनाने पर काम कर रहे हैं.

अगर आपको काम करने वाले पैरामीटर, आने वाली सुविधाओं या Gemini का इस्तेमाल शुरू करने में आ रही
किसी समस्या के बारे में कुछ पूछना है, तो हमारे [डेवलपर फ़ोरम](https://discuss.ai.google.dev/c/gemini-api/4?hl=hi) में शामिल हों.

## आगे क्या करना है

ज़्यादा जानकारी वाले
उदाहरण देखने के लिए, हमारी [OpenAI कंपैटिबिलिटी Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=hi) आज़माएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
