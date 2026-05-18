---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=tr
fetched_at: 2026-05-18T05:09:26.314544+00:00
title: "OpenAI uyumlulu\u011fu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# OpenAI uyumluluğu

Gemini modellerine, OpenAI kitaplıkları (Python ve TypeScript/JavaScript) ile REST API kullanılarak erişilebilir. Bunun için üç satır kodu güncellemeniz ve [Gemini API anahtarınızı](https://aistudio.google.com/apikey?hl=tr) kullanmanız gerekir. OpenAI kitaplıklarını kullanmıyorsanız [Gemini API'yi doğrudan](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr) çağırmanızı öneririz.

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

Neler değişti? Yalnızca üç satır!

- **`api_key="GEMINI_API_KEY"`**: "`GEMINI_API_KEY`" yerine [Google AI Studio](https://aistudio.google.com?hl=tr)'da alabileceğiniz gerçek Gemini API anahtarınızı girin.
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** Bu, OpenAI kitaplığına istekleri varsayılan URL yerine Gemini API uç noktasına göndermesini söyler.
- **`model="gemini-3-flash-preview"`**: Uyumlu bir Gemini modeli seçin

## Düşünen

Gemini modelleri, karmaşık sorunları çözmek için eğitilir. Bu sayede akıl yürütme yetenekleri önemli ölçüde gelişir. Gemini API, modelin ne kadar düşüneceği üzerinde ayrıntılı kontrol sağlayan [düşünme parametreleriyle](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) birlikte gelir.

Farklı Gemini modellerinin farklı muhakeme yapılandırmaları vardır. Bu modellerin OpenAI'ın muhakeme çalışmalarıyla nasıl eşlendiğini aşağıdaki tabloda görebilirsiniz:

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

`reasoning_effort` belirtilmemişse Gemini, modelin varsayılan [düzeyini](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#levels) veya [bütçesini](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#set-budget) kullanır.

Düşünme özelliğini devre dışı bırakmak istiyorsanız 2.5 modelleri için `reasoning_effort` değerini `"none"` olarak ayarlayabilirsiniz. Gemini 2.5 Pro veya 3 modellerinde muhakeme özelliği devre dışı bırakılamaz.

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

Gemini düşünme modelleri [düşünce özetleri](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#summaries) de oluşturur.
İsteğinize Gemini alanları eklemek için [`extra_body`](#extra-body) alanını kullanabilirsiniz.

`reasoning_effort` ve `thinking_level`/`thinking_budget` işlevlerinin çakıştığını, bu nedenle aynı anda kullanılamayacağını unutmayın.

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

Gemini 3, sohbet tamamlama API'lerinde düşünce imzaları için OpenAI uyumluluğunu destekler. Tam örneği [Düşünce imzaları](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr#openai) sayfasında bulabilirsiniz.

## Canlı Yayın

Gemini API, [akış yanıtlarını](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=tr#generate-a-text-stream) destekler.

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

## İşlev çağırma

İşlev çağrısı, üretken modellerden yapılandırılmış veri çıkışları almanızı kolaylaştırır ve [Gemini API'de desteklenir](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=tr).

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

## Görüntü anlama

Gemini modelleri, yerel olarak çok formatlıdır ve [birçok yaygın görüntü görevinde](https://ai.google.dev/gemini-api/docs/vision?hl=tr) sınıfının en iyi performansını sunar.

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

## Resim üretin

`gemini-2.5-flash-image` veya `gemini-3-pro-image-preview` kullanarak resim oluşturun. Desteklenen parametreler arasında `prompt`, `model`, `n`, `size` ve `response_format` yer alır. Burada veya [`extra_body`](#extra-body) bölümünde listelenmeyen diğer tüm parametreler, uyumluluk katmanı tarafından sessizce yoksayılır.

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

## Video oluşturma

Sora ile uyumlu `veo-3.1-generate-preview` uç noktasını kullanarak `/v1/videos` ile video oluşturun. Desteklenen üst düzey parametreler `prompt` ve `model`'dir. `duration_seconds`, `image` ve `aspect_ratio` gibi ek parametreler `extra_body` ile birlikte iletilmelidir. Kullanılabilir tüm parametreler için [`extra_body`](#extra-body) bölümüne bakın.

Video oluşturma, tamamlanma durumu için yoklayabileceğiniz bir işlem kimliği döndüren uzun süreli bir işlemdir.

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

### Video durumunu kontrol etme

Video üretme işlemi eşzamansızdır. Durumu yoklamak ve tamamlandığında nihai video URL'sini almak için `GET /v1/videos/{id}` kullanın:

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

## Ses yorumlama

Ses girişini analiz etme:

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

## Yapılandırılmış çıkış

Gemini modelleri, JSON nesnelerini [tanımladığınız herhangi bir yapıda](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) çıkış olarak verebilir.

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

## Yerleştirmeler

Metin yerleştirmeleri, metin dizelerinin ilişkisini ölçer ve [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) kullanılarak oluşturulabilir. Çok formatlı yerleştirmeler için `gemini-embedding-2-preview`, yalnızca metin yerleştirmeleri için `gemini-embedding-001` kullanabilirsiniz.

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

OpenAI kitaplığını kullanarak [toplu işler](https://ai.google.dev/gemini-api/docs/batch-mode?hl=tr) oluşturabilir, bunları gönderebilir ve durumlarını kontrol edebilirsiniz.

JSONL dosyasını OpenAI giriş biçiminde hazırlamanız gerekir. Örneğin:

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3-flash-preview", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Batch için OpenAI uyumluluğu, toplu iş oluşturmayı, iş durumunu izlemeyi ve toplu iş sonuçlarını görüntülemeyi destekler.

Yükleme ve indirme için uyumluluk şu anda desteklenmemektedir. Bunun yerine, aşağıdaki örnekte [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=tr#input-file) kullanılırken olduğu gibi [dosya](https://ai.google.dev/gemini-api/docs/files?hl=tr) yükleme ve indirme için `genai` istemcisi kullanılmaktadır.

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

OpenAI SDK, [Batch API ile yerleştirme oluşturmayı](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#batch-embeddings) da destekler. Bunu yapmak için `create` yönteminin `endpoint` alanını bir yerleştirme uç noktasıyla, JSONL dosyasındaki `url` ve `model` anahtarlarını da değiştirin:

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

Tam bir örnek için OpenAI uyumluluk yemek kitabının [Toplu yerleştirme oluşturma](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb) bölümüne bakın.

## Esnek ve öncelikli çıkarım

Gemini API, ad ve mantık açısından OpenAI'ın `service_tier` parametresiyle eşleşir. Hem Flex hem de Priority çıkarım katmanları için sınırları zorlar ve trafiği sorunsuz bir şekilde yönlendirir.

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

Açıkça atanmadığında `service_tier` varsayılan olarak `standard` olur. Bu, OpenAI için `default` değerine eşittir.
[Optimizasyon](https://ai.google.dev/gemini-api/docs/optimization?hl=tr) belgelerinde çıkarım katmanları hakkında daha fazla bilgi edinin.

## `extra_body` ile Gemini özelliklerini etkinleştirme

Gemini tarafından desteklenen ve OpenAI modellerinde bulunmayan ancak `extra_body` alanı kullanılarak etkinleştirilebilen çeşitli özellikler vardır.

| Parametre | Tür | Uç nokta | Açıklama |
| --- | --- | --- | --- |
| **`cached_content`** | Metin | Sohbet | Gemini'ın genel içerik önbelleğine karşılık gelir. |
| **`thinking_config`** | Nesne | Sohbet | Gemini'ın ThinkingConfig'ine karşılık gelir. |
| **`aspect_ratio`** | Metin | Resimler | Çıkış en boy oranı (ör. `"16:9"`, `"1:1"`, `"9:16"`). |
| **`generation_config`** | Nesne | Resimler | Gemini oluşturma yapılandırma nesnesi (ör. `{"responseModalities": ["IMAGE"], "candidateCount": 2}`). |
| **`safety_settings`** | Liste | Resimler | Özel güvenlik eşiği filtreleri (ör. `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`). |
| **`tools`** | Liste | Resimler | Temellendirmeyi (ör. `[{"google_search": {}}]`) etkinleştirir. Yalnızca `gemini-3-pro-image-preview` için geçerlidir. |
| **`aspect_ratio`** | Metin | Video | Çıkış videosunun boyutları (yatay için `16:9`, dikey için `9:16`). Belirtilmemişse `size` kaynağındaki haritalar. |
| **`resolution`** | Metin | Video | Çıkış çözünürlüğü (`720p`, `1080p`, `4K`). Not: `1080p` ve `4K`, yükseltme işlem hattını tetikler. |
| **`duration_seconds`** | Tamsayı | Video | Üretim uzunluğu (değerler: `4`, `6`, `8`). `reference_images`, enterpolasyon veya uzatma kullanılırken `8` olmalıdır. |
| **`frame_rate`** | Metin | Video | Video çıkışı için kare hızı (ör. `"24"`). |
| **`input_reference`** | Metin | Video | Video üretimi için referans girişi. |
| **`extend_video_id`** | Metin | Video | Uzatılacak mevcut videonun kimliği. |
| **`negative_prompt`** | Metin | Video | Hariç tutulacak öğeler (ör. `"shaky camera"`). |
| **`seed`** | Tamsayı | Video | Belirleyici oluşturma için tam sayı. |
| **`style`** | Metin | Video | Görsel stil (`cinematic` varsayılan, `creative` sosyal medya için optimize edilmiş). |
| **`person_generation`** | Metin | Video | İnsanların oluşturulmasını kontrol eder (`allow_adult`, `allow_all`, `dont_allow`). |
| **`reference_images`** | Liste | Video | Stil/karakter referansı için en fazla 3 resim (base64 öğeleri). |
| **`image`** | Metin | Video | Video oluşturma işlemini koşullandırmak için Base64 kodlu başlangıç giriş resmi. |
| **`last_frame`** | Nesne | Video | Ara değer bulma için son resim (ilk kare olarak `image` gerektirir). |

### `extra_body` ile ilgili örnek

`extra_body` kullanarak `cached_content` ayarlama örneğini aşağıda bulabilirsiniz:

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

## Modelleri listeleyin

Kullanılabilir Gemini modellerinin listesini alma:

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

## Model alma

Gemini modelini alma:

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

## Mevcut sınırlamalar

Özellik desteğini genişletirken OpenAI kitaplıkları için destek hâlâ beta sürümündedir.

Desteklenen parametreler, yakında kullanıma sunulacak özellikler veya Gemini'ı kullanmaya başlarken karşılaştığınız sorunlar hakkında sorularınız varsa [Geliştirici Forumumuza](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr) katılın.

## Sırada ne var?

Daha ayrıntılı örnekler için [OpenAI Compatibility Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=tr)'imizi deneyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-13 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-13 UTC."],[],[]]
