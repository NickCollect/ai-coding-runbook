---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=ko
fetched_at: 2026-09-21T05:56:35.608701+00:00
title: "OpenAI \ud638\ud658\uc131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# OpenAI 호환성

코드 3줄을 업데이트하고 [Gemini API 키](https://aistudio.google.com/apikey?hl=ko)를 사용하여 REST API와 함께 OpenAI 라이브러리 (Python 및 TypeScript/JavaScript)를 통해 Gemini 모델에 액세스할 수 있습니다. 아직 OpenAI 라이브러리를 사용하고 있지 않다면 [Gemini API를 직접 호출](https://ai.google.dev/gemini-api/docs/get-started?hl=ko)하는 것이 좋습니다.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

변경사항 단 3줄이면 됩니다.

- **`api_key="GEMINI_API_KEY"`**: [Google AI Studio](https://aistudio.google.com?hl=ko)에서 가져올 수 있는 실제 Gemini API 키로 '`GEMINI_API_KEY`'를 바꿉니다.
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** OpenAI 라이브러리에 기본 URL 대신 Gemini API 엔드포인트에 요청을 전송하도록 지시합니다.
- **`model="gemini-3.6-flash"`**: 호환되는 Gemini 모델을 선택합니다.

## 사고

Gemini 모델은 복잡한 문제를 해결하도록 학습되어 추론 능력이 크게 향상되었습니다. Gemini API에는 모델이 얼마나 사고할지 세부적으로 제어할 수 있는 [사고 파라미터](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)가 제공됩니다.

Gemini 모델마다 추론 구성이 다릅니다. OpenAI의 추론 노력과 어떻게 매핑되는지 다음을 참고하세요.

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

`reasoning_effort`가 지정되지 않으면 Gemini는 모델의 기본 [수준](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#levels) 또는 [예산](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#set-budget)을 사용합니다.

사고를 사용 중지하려면 2.5 모델의 경우 `reasoning_effort`를 `"none"`로 설정하면 됩니다. Gemini 2.5 Pro 또는 3 모델에서는 추론을 사용 중지할 수 없습니다.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Gemini 사고 모델은 [사고 요약](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#summaries)도 생성합니다.
[`extra_body`](#extra-body) 필드를 사용하여 요청에 Gemini 필드를 포함할 수 있습니다.

`reasoning_effort`와 `thinking_level`/`thinking_budget`는 기능이 중복되므로 동시에 사용할 수 없습니다.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
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

Gemini 3는 채팅 완성 API에서 사고 서명에 대한 OpenAI 호환성을 지원합니다. 전체 예는 [생각 서명](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ko#openai) 페이지에서 확인할 수 있습니다.

## 스트리밍

Gemini API는 [스트리밍 응답](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=ko#generate-a-text-stream)을 지원합니다.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.6-flash",
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

### 자바스크립트

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## 함수 호출

함수 호출을 사용하면 생성형 모델에서 구조화된 데이터 출력을 더 쉽게 가져올 수 있는데, 이는 [Gemini API에서 지원](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=ko)됩니다.

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
  model="gemini-3.6-flash",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### 자바스크립트

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
    model: "gemini-3.6-flash",
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
  "model": "gemini-3.6-flash",
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

## 이미지 이해

Gemini 모델은 네이티브 멀티모달이며 [다양한 일반적인 비전 작업](https://ai.google.dev/gemini-api/docs/vision?hl=ko)에서 동급 최고의 성능을 제공합니다.

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
  model="gemini-3.6-flash",
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

### 자바스크립트

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
      model: "gemini-3.6-flash",
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
      \"model\": \"gemini-3.6-flash\",
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

## 이미지 생성

`gemini-2.5-flash-image` 또는 `gemini-3-pro-image-preview`를 사용하여 이미지를 생성해 줘. 지원되는 매개변수에는 `prompt`, `model`, `n`, `size`, `response_format`이 있습니다. 여기에 나열되지 않거나 [`extra_body`](#extra-body) 섹션에 나열되지 않은 다른 매개변수는 호환성 레이어에서 자동으로 무시됩니다.

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

### 자바스크립트

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

## 동영상 생성

Sora 호환 `/v1/videos` 엔드포인트를 통해 `veo-3.1-generate-preview`를 사용하여 동영상을 생성합니다. 지원되는 최상위 매개변수는 `prompt` 및 `model`입니다. `duration_seconds`, `image`, `aspect_ratio`과 같은 추가 매개변수는 `extra_body`와 함께 전달해야 합니다. 사용 가능한 모든 매개변수는 [`extra_body`](#extra-body) 섹션을 참고하세요.

동영상 생성은 완료 여부를 폴링할 수 있는 작업 ID를 반환하는 장기 실행 작업입니다.

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

### 자바스크립트

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

### 동영상 상태 확인

동영상 생성은 비동기식입니다. `GET /v1/videos/{id}`를 사용하여 상태를 폴링하고 완료되면 최종 동영상 URL을 가져옵니다.

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

### 자바스크립트

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

## 오디오 이해

오디오 입력 분석:

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
    model="gemini-3.6-flash",
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

### 자바스크립트

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
    model: "gemini-3.6-flash",
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
      \"model\": \"gemini-3.6-flash\",
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

## 구조화된 출력

Gemini 모델은 [내가 정의한 구조](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)로 JSON 객체를 출력할 수 있습니다.

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
    model="gemini-3.6-flash",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### 자바스크립트

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
  model: "gemini-3.6-flash",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## 임베딩

텍스트 임베딩은 텍스트 문자열의 관련성을 측정하며 [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko)를 사용하여 생성할 수 있습니다. 멀티모달 임베딩에는 `gemini-embedding-2-preview`를 사용하고 텍스트 전용 임베딩에는 `gemini-embedding-001`를 사용할 수 있습니다.

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

### 자바스크립트

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

OpenAI 라이브러리를 사용하여 [일괄 작업](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ko)을 만들고, 제출하고, 상태를 확인할 수 있습니다.

OpenAI 입력 형식으로 JSONL 파일을 준비해야 합니다. 예를 들면 다음과 같습니다.

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.6-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.6-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Batch의 OpenAI 호환성은 배치 생성, 작업 상태 모니터링, 배치 결과 보기를 지원합니다.

업로드 및 다운로드 호환성은 현재 지원되지 않습니다. 대신 다음 예에서는 Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ko#input-file)를 사용할 때와 마찬가지로 `genai` 클라이언트를 사용하여 [파일](https://ai.google.dev/gemini-api/docs/files?hl=ko)을 업로드하고 다운로드합니다.

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

OpenAI SDK는 [Batch API를 사용한 임베딩 생성](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko#batch-embeddings)도 지원합니다. 이렇게 하려면 `create` 메서드의 `endpoint` 필드를 삽입 엔드포인트로 바꾸고 JSONL 파일의 `url` 및 `model` 키도 바꿉니다.

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

전체 예시는 OpenAI 호환성 쿡북의 [일괄 삽입 생성](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb) 섹션을 참고하세요.

## Flex 및 우선순위 추론

Gemini API는 이름과 로직이 OpenAI의 `service_tier` 파라미터와 일치하며, Flex 및 Priority 추론 등급 모두에 대해 제한을 적용하고 트래픽을 적절하게 안내합니다.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.6-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

명시적으로 할당되지 않은 경우 `service_tier`는 `standard`로 기본 설정되며, 이는 OpenAI의 경우 `default`와 동일합니다.
[최적화](https://ai.google.dev/gemini-api/docs/optimization?hl=ko) 문서에서 추론 티어에 대해 자세히 알아보세요.

## `extra_body`로 Gemini 기능 사용 설정하기

Gemini에서 지원되지만 OpenAI 모델에서는 사용할 수 없는 몇 가지 기능이 있으며, `extra_body` 필드를 사용하여 사용 설정할 수 있습니다.

| 매개변수 | 유형 | 엔드포인트 | 설명 |
| --- | --- | --- | --- |
| **`cached_content`** | 텍스트 | 채팅 | Gemini의 일반 콘텐츠 캐시에 해당합니다. |
| **`thinking_config`** | 객체 | 채팅 | Gemini의 ThinkingConfig에 해당합니다. |
| **`aspect_ratio`** | 텍스트 | 이미지 | 출력 가로세로 비율 (예: `"16:9"`, `"1:1"`, `"9:16"`) |
| **`generation_config`** | 객체 | 이미지 | Gemini 생성 구성 객체 (예: `{"responseModalities": ["IMAGE"], "candidateCount": 2}`) |
| **`safety_settings`** | 목록 | 이미지 | 맞춤 안전 기준 필터 (예: `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`) |
| **`tools`** | 목록 | 이미지 | 그라운딩 (예: `[{"google_search": {}}]`)을 사용 설정합니다. `gemini-3-pro-image-preview`에만 해당합니다. |
| **`aspect_ratio`** | 텍스트 | 동영상 | 출력 동영상의 크기 (가로 모드의 경우 `16:9`, 세로 모드의 경우 `9:16`) 지정하지 않으면 `size`에서 매핑됩니다. |
| **`resolution`** | 텍스트 | 동영상 | 출력 해상도 (`720p`, `1080p`, `4K`). 참고: `1080p` 및 `4K`는 업샘플러 파이프라인을 트리거합니다. |
| **`duration_seconds`** | 정수 | 동영상 | 생성 길이 (값: `4`, `6`, `8`). `reference_images`, 보간 또는 확장을 사용하는 경우 `8`여야 합니다. |
| **`frame_rate`** | 텍스트 | 동영상 | 동영상 출력의 프레임 속도입니다 (예: `"24"`). |
| **`input_reference`** | 텍스트 | 동영상 | 동영상 생성을 위한 참조 입력입니다. |
| **`extend_video_id`** | 텍스트 | 동영상 | 연장할 기존 동영상의 ID입니다. |
| **`negative_prompt`** | 텍스트 | 동영상 | 제외할 항목 (예: `"shaky camera"`) |
| **`seed`** | 정수 | 동영상 | 결정론적 생성을 위한 정수입니다. |
| **`style`** | 텍스트 | 동영상 | 시각적 스타일 (`cinematic` 기본값, `creative` 소셜 미디어 최적화). |
| **`person_generation`** | 텍스트 | 동영상 | 인물 생성 (`allow_adult`, `allow_all`, `dont_allow`)을 제어합니다. |
| **`reference_images`** | 목록 | 동영상 | 스타일/캐릭터 참조용 이미지 (base64 확장 소재) 최대 3개 |
| **`image`** | 텍스트 | 동영상 | 동영상 생성을 조건화하기 위한 base64로 인코딩된 초기 입력 이미지입니다. |
| **`last_frame`** | 객체 | 동영상 | 보간을 위한 최종 이미지입니다 (`image`가 첫 번째 프레임으로 필요함). |

### `extra_body` 사용 예시

다음은 `extra_body`를 사용하여 `cached_content`를 설정하는 예입니다.

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.6-flash",
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

## 모델 나열

사용 가능한 Gemini 모델 목록을 가져옵니다.

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

### 자바스크립트

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

## 모델 가져오기

Gemini 모델을 가져옵니다.

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.6-flash")
print(model.id)
```

### 자바스크립트

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3.6-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.6-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## 현재 제한사항

기능 지원을 확대하고는 있지만, OpenAI 라이브러리 지원은 아직 베타 버전입니다.

지원되는 매개변수, 예정된 기능에 관해 궁금한 점이 있거나 Gemini를 시작하는 데 문제가 있는 경우 [개발자 포럼](https://discuss.ai.google.dev/c/gemini-api/4?hl=ko)에 참여하세요.

## 다음 단계

[OpenAI 호환성 Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=ko)을 사용해 더 자세한 예시를 살펴보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-12(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-12(UTC)"],[],[]]
