---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=ko
fetched_at: 2026-08-03T04:39:42.226145+00:00
title: "\uc2dc\uc791\ud558\uae30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 시작하기

이 가이드에서는 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)를 사용하여 Gemini API를 시작하는 방법을 설명합니다. 1분 이내에 첫 번째 API 호출을 하고 텍스트 생성, 멀티모달 이해, 이미지 생성, 구조화된 출력, 도구, 함수 호출, 에이전트, 백그라운드 실행을 살펴봅니다.

Interactions API는 [Python](https://github.com/googleapis/python-genai) 및 [JavaScript](https://github.com/googleapis/js-genai) SDK와 REST를 통해 사용할 수 있습니다.

## 1. API 키 가져오기

Gemini API를 사용하려면 요청을 인증하고, 보안 한도를 적용하고, 계정의 사용량을 추적하는 API 키가 있어야 합니다.

- Google AI Studio는 신규 사용자를 위해 프로젝트와 API 키를 자동으로 생성합니다.
  [API 키 페이지](https://aistudio.google.com/api-keys?hl=ko)에서 복사할 수 있습니다.
- 새 키가 필요한 경우 AI Studio에서 **API 키 만들기**를 클릭하고 대화상자에 따라 새 키-프로젝트 쌍을 추가합니다.

[Gemini API 키 만들기](https://aistudio.google.com/apikey?hl=ko)

키를 환경 변수로 설정합니다.

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### 유료 등급으로 업그레이드

유료 등급으로 업그레이드하면 비율 제한이 증가하며 Cloud Billing을 설정해야 합니다.

- AI Studio [API 키](https://aistudio.google.com/api-keys?hl=ko) 또는 [프로젝트](https://aistudio.google.com/projects?hl=ko) 페이지에서 **결제 설정**을 클릭합니다.
- Cloud Billing 대화상자에 따라 결제 계정을 만들거나 연결하고, 지급 수단을 추가하고, 유료 크레딧으로 최소 10달러 (또는 해당 통화)를 선불합니다.
- [Google AI Studio](https://aistudio.google.com/usage?hl=ko)의 **대시보드** > **사용량**에서 API 사용량을 확인합니다.

자세한 내용은 [결제 페이지](https://ai.google.dev/gemini-api/docs/billing?hl=ko)를 참고하세요.

## 2. SDK 설치 및 첫 번째 호출 만들기

SDK를 설치하고 단일 API 호출로 텍스트를 생성합니다.

### Python

SDK를 설치합니다.

```
pip install -U google-genai
```

클라이언트를 초기화하고 요청을 합니다.

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### 자바스크립트

SDK를 설치합니다.

```
npm install @google/genai
```

클라이언트를 초기화하고 요청을 합니다.

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**대답:**

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
  "model": "gemini-3.6-flash",
}
```

REST를 사용하면 API는 메타데이터, 사용 통계, 턴의 단계별 기록이 포함된 전체 `Interaction` 리소스를 반환합니다.

SDK는 전체 응답을 노출하는 동시에 최종 출력에 직접 액세스할 수 있는 `interaction.output_text`, `interaction.output_image`과 같은 편의 속성도 제공합니다. [상호작용 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)에서 응답 구조에 대해 자세히 알아보거나 [텍스트 생성 가이드](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko)에서 시스템 안내 및 생성 구성에 대해 자세히 알아보세요.

## 3. 대답 스트리밍

더 원활한 상호작용을 위해 대답이 생성되는 대로 스트리밍하세요. 각 `step.delta` 이벤트는 즉시 표시할 수 있는 텍스트 청크를 제공합니다.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

스트리밍 시 서버는 서버 전송 이벤트 (SSE) 스트림으로 응답합니다. 각 이벤트에는 유형과 JSON 데이터가 포함됩니다.

**대답:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

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

스트리밍 이벤트 및 델타 유형 처리에 관한 자세한 내용은 [스트리밍 상호작용 가이드](https://ai.google.dev/gemini-api/docs/streaming?hl=ko)를 참고하세요.

## 4. 멀티턴 대화

Interactions API는 다음 두 가지 접근 방식으로 멀티턴 대화를 지원합니다.

- **상태 저장 (권장)**: `previous_interaction_id`를 사용하여 서버에서 대화를 계속합니다. 서버에서 기록을 관리하고 캐싱을 최적화해야 하는 대부분의 채팅 및 에이전트 워크플로에 적합합니다.
- **스테이트리스**: 각 요청에서 이전 턴 (중간 모델 사고 및 도구 단계 포함)을 모두 전달하여 클라이언트에서 대화 기록을 관리합니다.

### 상태 저장 (권장)

`previous_interaction_id`를 전달하여 상호작용을 연결합니다. 서버에서 전체 대화 기록을 관리합니다.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### 스테이트리스(Stateless)

클라이언트 측에서 `store=false`를 설정하고 대화 기록을 관리합니다. 모델에서 생성된 모든 단계 (`thought` 및 `function_call` 단계 포함)를 수신된 그대로 유지하고 다시 전송해야 합니다.

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
    model="gemini-3.6-flash",
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
    model="gemini-3.6-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### 자바스크립트

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
  model: "gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**대답:**

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
  "model": "gemini-3.6-flash"
}
```

두 번째 상호작용에서는 새로운 단계만 포함하지만 이전 턴의 컨텍스트에 기반한 완전한 응답 객체를 반환합니다. [멀티턴 대화 가이드](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#multi-turn-conversations)에서 상태 유지에 대해 자세히 알아보거나 클라이언트 측 기록 관리를 위해 [스테이트리스 모드](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#stateless-conversations)를 살펴보세요.

## 5. 멀티모달 이해

Gemini 모델은 이미지, 오디오, 동영상, 문서를 기본적으로 이해합니다. 단일 요청에서 텍스트와 함께 미디어를 전달합니다.

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
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**대답:**

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
  "model": "gemini-3.6-flash",
}
```

[이미지 이해 가이드](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko)에서 이미지, 동영상, 오디오 파일을 전달하는 방법을 알아보세요.

[hearing

오디오 이해

오디오 파일의 스크립트를 작성하거나, 요약하거나, 오디오 파일에 관한 질문에 답변합니다.](https://ai.google.dev/gemini-api/docs/audio?hl=ko)
[videocam

동영상 이해

동영상 콘텐츠를 분석하고, 이벤트를 찾고, 동작을 설명합니다.](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko)
[description

문서 처리

PDF 및 기타 문서 형식에서 정보를 추출합니다.](https://ai.google.dev/gemini-api/docs/document-processing?hl=ko)

## 6. 멀티모달 생성

Gemini는 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko) 이미지 모델을 사용하여 기본적으로 이미지를 생성할 수 있습니다.

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

### 자바스크립트

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

**대답:**

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

모델이 이미지를 생성하면 `steps` 배열 내 단계와 `output_image` 편의 속성을 통해 base64로 인코딩된 이미지 데이터를 반환합니다. [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)에서 가로세로 비율, 이미지 편집, 참조에 대해 알아보세요.

[record\_voice\_over

음성 생성

Gemini 3.1 Flash TTS로 표현력이 풍부한 다중 화자 음성을 생성하세요.](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)
[music\_note

음악 생성

Lyria 3로 클립과 전체 길이 노래를 만드세요.](https://ai.google.dev/gemini-api/docs/music-generation?hl=ko)

## 7. 구조화된 출력 사용

정의한 스키마와 일치하는 JSON을 반환하도록 모델을 구성합니다. 구조화된 출력은 [Pydantic](https://docs.pydantic.dev/latest/) (Python) 및 [Zod](https://zod.dev/) (JavaScript)와 함께 작동합니다.

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
    model="gemini-3.6-flash",
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

### 자바스크립트

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
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**대답:**

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
  "model": "gemini-3.6-flash",
}
```

출력 텍스트 블록에는 요청된 스키마를 정확하게 준수하는 유효한 JSON 문자열이 포함되어 있습니다. 더 복잡한 구조와 재귀 스키마를 정의하는 방법을 알아보려면 [구조화된 출력 가이드](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)를 참고하세요.

## 8. 도구 사용하기

Google 검색을 사용하여 모델의 대답을 실시간 정보에 그라운딩합니다. API는 자동으로 검색하고, 결과를 처리하고, 인용을 반환합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**대답:**

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
  "model": "gemini-3.6-flash",
}
```

검색 단계는 상호작용 기록에 자세히 설명되어 있으며 최종 출력에는 웹 소스를 가리키는 인라인 인용이 포함됩니다.

[Google 검색 그라운딩 가이드](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)에서 검색 인용을 추출하는 방법을 알아보거나 [도구 조합 가이드](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)에서 여러 도구를 결합하는 방법을 알아보세요.

[code

코드 실행

안전한 샌드박스 Borg 환경에서 Python 코드를 실행합니다.](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)
[link

URL 컨텍스트

웹페이지 콘텐츠에서 대답을 그라운딩하기 위해 공개 웹 URL을 직접 전달합니다.](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)
[search

파일 검색

업로드된 문서와 미디어 파일을 색인화하고 검색합니다.](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)
[map

Google 지도

실제 지리 공간 및 위치 데이터를 기반으로 대답을 그라운딩합니다.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)
[computer

컴퓨터 사용

브라우저 자동화 및 화면 상호작용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)

## 9. 자체 함수 호출

함수 호출을 사용하면 모델을 코드에 연결할 수 있습니다. 함수의 이름과 매개변수를 선언하면 모델이 호출 시기를 결정하고 구조화된 인수를 반환하며, 개발자는 이를 로컬에서 실행하고 결과를 다시 전송합니다.

### 상태 저장 (권장)

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
        model="gemini-3.6-flash",
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

### 자바스크립트

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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

### 스테이트리스(Stateless)

클라이언트 측에서 대화 기록을 관리하고 `store=false`를 설정하여 상태 비저장 모드에서 함수 호출을 사용할 수도 있습니다. 스테이트리스(Stateless) 모드에서는 각 후속 요청의 `input` 필드에 대화의 전체 기록을 전달해야 합니다. 이 기록에는 다음이 포함되어야 합니다.

1. 초기 `user_input` 단계입니다.
2. 턴 1에서 반환된 모든 모델 생성 단계 (`thought` 및 `function_call` 단계 포함)가 수신된 그대로입니다.
3. 실행된 함수의 출력이 포함된 `function_result` 단계

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
        model="gemini-3.6-flash",
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

### 자바스크립트

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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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
    \"model\": \"gemini-3.6-flash\",
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

**대답:**

1턴에서 모델은 상태가 `requires_action`이고 `function_call` 단계가 포함된 응답을 반환합니다.

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
  "model": "gemini-3.6-flash"
}
```

함수를 로컬로 실행하고 결과를 제출하면 (2번째 턴) 최종 완료된 상호작용이 반환됩니다.

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
  "model": "gemini-3.6-flash",
}
```

병렬 함수 호출 또는 함수 선택 모드와 같은 고급 기능은 [함수 호출 가이드](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)를 참고하세요.

## 10. 관리 에이전트 실행

관리형 에이전트는 코드 실행 및 파일 관리와 같은 도구에 액세스할 수 있는 원격 샌드박스에서 실행됩니다. `model` 대신 `agent`를 전달하고 `environment="remote"`를 설정합니다.

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

### 자바스크립트

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

자체 안내, 기술, 데이터 소스를 사용하여 [맞춤 에이전트](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko)를 정의하고 저장할 수도 있습니다.

[rocket\_launch

빠른 시작

첫 번째 에이전트 통화를 하고, 응답을 스트리밍하고, 맞춤 에이전트를 빌드합니다.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)
[smart\_toy

Antigravity 에이전트

기본 에이전트의 기능, 도구, 멀티모달 입력, 가격 책정](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)
[experiment

AI Studio의 에이전트

코드를 작성하지 않고 에이전트의 프로토타입을 제작할 수 있는 시각적 플레이그라운드입니다.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ko)

## 11. 백그라운드에서 작업 실행

`background=True`를 설정하여 긴 작업을 비동기적으로 실행합니다. `interactions.get()`로 결과를 폴링합니다. 자세한 내용은 [백그라운드 실행 가이드](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)를 참고하세요.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

**대답:**

초기 응답은 상태 `in_progress`로 즉시 반환됩니다.

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.6-flash"
}
```

백그라운드 작업이 완전히 실행되면 상호작용 상태를 확인하여 다음을 반환합니다.

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
  "model": "gemini-3.6-flash",
}
```

[백그라운드 실행 가이드](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)에서 모델과 에이전트를 비동기적으로 실행하는 방법을 알아보세요.

## 다음 단계

- [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko): 장기 실행 작업을 비동기식으로 실행하고 상태를 관리합니다.
- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko): 시스템 요청 사항, 생성 구성, 고급 텍스트 패턴
- [이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko): 가로세로 비율, 이미지 수정, 스타일 참조
- [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko): 분류, 객체 감지, 시각적 Q&A
- [생각하기](https://ai.google.dev/gemini-api/docs/thinking?hl=ko): 복잡한 작업에 생각의 사슬 추론을 사용합니다.
- [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko): 병렬, 구성, 제한된 함수 모드
- [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko): 그라운딩, 인용, 추천 검색어
- [관리 에이전트](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko): 코드 실행 및 파일 관리가 포함된 사전 빌드된 에이전트입니다.
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko): 계획 및 합성을 통한 자율적인 다단계 연구
- [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko): JSON 스키마, 열거형, 재귀 유형 정의

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
