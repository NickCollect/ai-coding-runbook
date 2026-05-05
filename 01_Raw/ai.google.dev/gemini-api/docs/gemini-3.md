---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ko
fetched_at: 2026-05-05T20:09:14.931454+00:00
title: "Gemini 3 \uac1c\ubc1c\uc790 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 3 개발자 가이드

Gemini 3는 최첨단 추론을 기반으로 구축된, 현재까지 가장 지능적인 모델 제품군입니다. 이 모델은 에이전트형 워크플로, 자율 코딩, 복잡한 멀티모달 작업을 정교하게 처리하여 어떠한 아이디어든 실현할 수 있도록 설계되었습니다.
이 가이드에서는 Gemini 3 모델 계열의 주요 기능과 이를 최대한 활용하는 방법을 설명합니다.

[Gemini 3.1 Pro 프리뷰 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=ko)
[Gemini 3 Flash 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=ko)
[Nano Banana 2 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=ko)

[Gemini 3 앱 컬렉션](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ko)을 살펴보고 모델이 고급 추론, 자율 코딩, 복잡한 멀티모달 작업을 어떻게 처리하는지 확인하세요.

다음과 같이 몇 줄의 코드로 시작하세요.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Gemini 3 시리즈 소개

Gemini 3.1 Pro는 다양한 모달리티에 걸쳐 폭넓은 세계 지식과 고급 추론이 필요한 복잡한 작업에 가장 적합합니다.

Gemini 3 Flash는 최신 3시리즈 모델로, Flash의 속도와 가격으로 Pro 수준의 인텔리전스를 제공합니다.

Nano Banana Pro (Gemini 3 Pro Image라고도 함)는 Google의 최고 품질 이미지 생성 모델이며, Nano Banana 2 (Gemini 3.1 Flash Image라고도 함)는 대량, 고효율, 저가형 모델입니다.

Gemini 3.1 Flash-Lite는 비용 효율적인 모델과 대용량 작업을 위해 빌드된 주력 모델입니다.

현재 모든 Gemini 3 모델은 프리뷰 버전으로 제공됩니다.

| 모델 ID | 컨텍스트 윈도우 (내 / 외부) | 지식 단절 | 가격 책정 (입력 / 출력)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite-preview** | 1백만 / 64,000 | 2025년 1월 | $0.25 (텍스트, 이미지, 동영상), $0.50 (오디오) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | 2025년 1월 | $0.25 (텍스트 입력) / $0.067 (이미지 출력)\*\* |
| **gemini-3.1-pro-preview** | 1백만 / 64,000 | 2025년 1월 | 2달러 / 12달러 (<200,000개 토큰)   4달러 / 18달러 (>200,000개 토큰) |
| **gemini-3-flash-preview** | 1백만 / 64,000 | 2025년 1월 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025년 1월 | $2 (텍스트 입력) / $0.134 (이미지 출력)\*\* |

*\* 별도로 명시되지 않는 한 가격은 토큰 100만 개당 가격입니다.*
*\*\* 이미지 가격은 해상도에 따라 다릅니다. 자세한 내용은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.*

자세한 한도, 가격, 추가 정보는 [모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)를 참고하세요.

## Gemini 3의 새로운 API 기능

Gemini 3에는 개발자가 지연 시간, 비용, 멀티모달 충실도를 더 세밀하게 제어할 수 있도록 설계된 새로운 파라미터가 도입되었습니다.

### 사고 수준

Gemini 3 시리즈 모델은 기본적으로 동적 사고를 사용하여 프롬프트를 통해 추론합니다. 대답을 생성하기 전에 모델의 내부 추론 프로세스의 **최대** 깊이를 제어하는 `thinking_level` 파라미터를 사용할 수 있습니다. Gemini 3는 이러한 수준을 엄격한 토큰 보장이 아닌 사고를 위한 상대적 허용치로 취급합니다.

`thinking_level`이 지정되지 않은 경우 Gemini 3의 기본값은 `high`입니다. 복잡한 추론이 필요하지 않은 경우 더 빠르고 지연 시간이 짧은 대답을 위해 모델의 사고 수준을 `low`로 제한할 수 있습니다.

| 사고 수준 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 설명 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 지원되지 않음 | 지원됨 (기본값) | 지원됨 | 대부분의 질문에 대해 '생각하지 않음' 설정과 일치합니다. 모델이 복잡한 코딩 작업에 대해 매우 최소한으로 생각할 수 있습니다. 채팅 또는 높은 처리량 애플리케이션의 지연 시간을 최소화합니다. `minimal`는 사고가 꺼져 있음을 보장하지 않습니다. |
| **`low`** | 지원됨 | 지원됨 | 지원됨 | 지연 시간과 비용을 최소화합니다. 간단한 지시 수행, 채팅 또는 고처리량 애플리케이션에 가장 적합합니다. |
| **`medium`** | 지원됨 | 지원됨 | 지원됨 | 대부분의 작업에 균형 잡힌 사고를 제공합니다. |
| **`high`** | 지원됨 (기본값, 동적) | 지원됨 (동적) | 지원됨 (기본값, 동적) | 추론 깊이를 극대화합니다. 모델이 첫 번째 (사고하지 않는) 출력 토큰에 도달하는 데 시간이 훨씬 더 오래 걸릴 수 있지만, 출력은 더 신중하게 추론됩니다. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### 미디어 해상도

Gemini 3는 `media_resolution` 파라미터를 통해 멀티모달 비전 처리에 대한 세밀한 제어 기능을 제공합니다. 해상도가 높을수록 모델이 작은 텍스트를 읽거나 세부 요소를 식별하는 능력을 향상시키지만, 토큰 사용량과 지연 시간이 증가합니다.
`media_resolution` 파라미터는 **입력 이미지 또는 동영상 프레임당 할당되는 최대 토큰 수**를 결정합니다.

이제 각 미디어 파트별로 또는 전역적으로 해상도를 `media_resolution_low`, `media_resolution_medium`, `media_resolution_high`, `media_resolution_ultra_high`로 설정할 수 있습니다 (`generation_config`를 통해, 초고화질에는 전역 설정이 지원되지 않음). 지정하지 않으면 모델은 미디어 유형에 따라 최적의 기본값을 사용합니다.

**권장 설정**

| 미디어 유형 | 권장 설정 | 최대 토큰 수 | 사용 안내 |
| --- | --- | --- | --- |
| **이미지** | `media_resolution_high` | 1120 | 최대 품질을 보장하기 위해 대부분의 이미지 분석 작업에 권장됩니다. |
| **PDF** | `media_resolution_medium` | 560 | 문서 이해에 최적화되어 있으며 품질은 일반적으로 `medium`에서 포화됩니다. `high`로 늘려도 표준 문서의 OCR 결과가 개선되는 경우는 거의 없습니다. |
| **동영상** (일반) | `media_resolution_low` (또는 `media_resolution_medium`) | 70 (프레임당) | **참고:** 동영상의 경우 컨텍스트 사용을 최적화하기 위해 `low` 및 `medium` 설정이 동일하게 (70개 토큰) 처리됩니다. 이는 대부분의 동작 인식 및 설명 작업에 충분합니다. |
| **동영상** (텍스트 중심) | `media_resolution_high` | 280 (프레임당) | 사용 사례에 밀도 높은 텍스트 (OCR) 또는 동영상 프레임 내의 작은 세부정보를 읽는 작업이 포함된 경우에만 필요합니다. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### 온도

모든 Gemini 3 모델의 경우 온도 파라미터를 기본값인 `1.0`으로 유지할 것을 적극 권장합니다.

이전 모델에서는 창의성과 결정성 간 균형을 위해 온도 조정이 도움이 되었지만, Gemini 3의 추론 기능은 기본 설정에 최적화되어 있습니다. 온도를 변경하여 (1.0 미만으로 설정) 복잡한 수학적 또는 추론 작업에서 루핑이나 성능 저하와 같은 예기치 않은 동작이 발생할 수 있습니다.

### 생각 서명

Gemini 3는 [사고 서명](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ko)을 사용하여 API 호출 전반에서 추론 컨텍스트를 유지합니다. 이러한 서명은 모델의 내부 사고 과정을 암호화한 표현입니다. 모델이 추론 기능을 유지하도록 하려면 요청에서 이러한 서명을 수신된 그대로 모델에 다시 반환해야 합니다.

- **함수 호출 (엄격):** API는 '현재 턴'에 엄격한 검증을 적용합니다. 서명이 누락되면 400 오류가 발생합니다.
- **텍스트/채팅:** 유효성 검사가 엄격하게 적용되지는 않지만 서명을 누락하면 모델의 추론 및 대답 품질이 저하됩니다.
- **이미지 생성/편집 (엄격)**: API는 `thoughtSignature`을 포함한 모든 모델 부분에 엄격한 검증을 적용합니다. 서명이 누락되면 400 오류가 발생합니다.

#### 함수 호출 (엄격한 유효성 검사)

Gemini가 `functionCall`를 생성할 때 `thoughtSignature`를 사용하여 다음 턴에서 도구의 출력을 올바르게 처리합니다. '현재 턴'에는 마지막 표준 **User** `text` 메시지 이후에 발생한 모든 모델 (`functionCall`) 및 사용자 (`functionResponse`) 단계가 포함됩니다.

- **단일 함수 호출:** `functionCall` 부분에 서명이 포함됩니다. 반환해야 합니다.
- **병렬 함수 호출:** 목록의 첫 번째 `functionCall` 부분에만 서명이 포함됩니다. 부품은 받은 순서대로 정확하게 반품해야 합니다.
- **다단계 (순차적):** 모델이 도구를 호출하고, 결과를 수신하고, (동일한 턴 내에서) *다른* 도구를 호출하는 경우 **두** 함수 호출 모두 서명이 있습니다. 기록에 누적된 **모든** 서명을 반환해야 합니다.

#### 텍스트 및 스트리밍

표준 채팅 또는 텍스트 생성의 경우 서명이 표시되지 않을 수 있습니다.

- **스트리밍 아님**: 대답의 최종 콘텐츠 부분에 `thoughtSignature`가 포함될 수 있지만 항상 포함되는 것은 아닙니다. 반환된 경우 최상의 성능을 유지하기 위해 다시 보내야 합니다.
- **스트리밍**: 서명이 생성되면 빈 텍스트 부분이 포함된 최종 청크에 도착할 수 있습니다. 텍스트 필드가 비어 있더라도 스트림 파서가 서명을 확인하도록 합니다.

#### 이미지 생성 및 수정

`gemini-3-pro-image-preview` 및 `gemini-3.1-flash-image-preview`의 경우 생각 서명은 대화 기반 수정에 매우 중요합니다. 모델에 이미지를 수정해 달라고 요청하면 이전 턴의 `thoughtSignature`를 사용하여 원본 이미지의 구성과 논리를 이해합니다.

- **수정:** 서명은 대답의 생각 (`text` 또는 `inlineData`) 후 첫 번째 부분과 모든 후속 `inlineData` 부분에 보장됩니다. 오류를 방지하려면 이러한 서명을 모두 반환해야 합니다.

#### 코드 예시

#### 다단계 함수 호출 (순차적)

사용자가 한 번에 두 가지 별도의 단계 (항공편 확인 -> 택시 예약)가 필요한 질문을 합니다.   
  
**1단계: 모델이 항공편 도구를 호출합니다.**  
모델이 서명 `<Sig_A>`를 반환합니다.

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**2단계: 사용자가 항공편 결과를 전송함**  
모델의 사고 흐름을 유지하려면 `<Sig_A>`를 다시 전송해야 합니다.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  { 
    "role": "model", 
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} }, 
        "thoughtSignature": "<Sig_A>" // REQUIRED
      } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**3단계: 모델이 택시 도구를 호출함**  
모델은 `<Sig_A>`를 통해 항공편 지연을 기억하고 이제 택시를 예약하기로 결정합니다. *새* 서명 `<Sig_B>`를 생성합니다.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**4단계: 사용자가 택시 결과를 보냄**  
턴을 완료하려면 `<Sig_A>` 및 `<Sig_B>` 전체 체인을 다시 보내야 합니다.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### 병렬 함수 호출

사용자가 '파리와 런던의 날씨를 확인해 줘'라고 요청합니다. 모델이 하나의 대답에 두 개의 함수 호출을 반환합니다.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### 텍스트/컨텍스트 내 추론 (유효성 검사 없음)

사용자가 외부 도구 없이 컨텍스트 내 추론이 필요한 질문을 합니다. 엄격하게 검증되지는 않지만 서명을 포함하면 모델이 후속 질문에 대한 추론 체인을 유지하는 데 도움이 됩니다.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### 이미지 생성 및 편집

이미지 생성의 경우 서명이 엄격하게 검증됩니다. **첫 번째 부분** (텍스트 또는 이미지)과 **이후의 모든 이미지 부분**에 표시됩니다. 다음 턴에 모두 반환해야 합니다.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### 다른 모델에서 이전

다른 모델 (예: Gemini 2.5)에서 대화 추적을 전송하거나 Gemini 3에서 생성되지 않은 맞춤 함수 호출을 삽입하는 경우 유효한 서명이 없습니다.

이러한 특정 시나리오에서 엄격한 유효성 검사를 우회하려면 필드를 `"thoughtSignature": "context_engineering_is_the_way
to_go"`라는 특정 더미 문자열로 채우세요.

### 도구를 사용한 구조화된 출력

Gemini 3 모델을 사용하면 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)을 [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko), [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)과 같은 기본 제공 도구와 결합할 수 있습니다.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 이미지 생성

Gemini 3.1 Flash Image 및 Gemini 3 Pro Image를 사용하면 텍스트 프롬프트에서 이미지를 생성하고 수정할 수 있습니다. 추론을 사용하여 프롬프트를 '생각'하고, [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 그라운딩을 사용하기 전에 날씨 예보나 주식 차트와 같은 실시간 데이터를 가져와 고화질 이미지를 생성할 수 있습니다.

**새로운 기능 및 개선된 기능:**

- **4K 및 텍스트 렌더링:** 최대 2K 및 4K 해상도로 선명하고 읽기 쉬운 텍스트와 다이어그램을 생성합니다.
- **그라운딩된 생성:** `google_search` 도구를 사용하여 사실을 확인하고 실제 정보를 기반으로 이미지를 생성합니다. Gemini 3.1 Flash Image에서 Google *이미지* 검색을 사용한 그라운딩을 사용할 수 있습니다.
- **대화 기반 수정:** 변경사항을 요청하는 간단한 질문 (예: '배경을 일몰로 바꿔줘')을 통해 멀티턴 이미지 편집 이 워크플로는 **생각 서명**을 사용하여 턴 간에 시각적 컨텍스트를 유지합니다.

종횡비, 편집 워크플로, 구성 옵션에 관한 자세한 내용은 [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)를 참고하세요.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K"
        )
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "imageConfig": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
    }
  }'
```

**응답 예시**

![도쿄 날씨](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ko)

### 이미지를 사용한 코드 실행

Gemini 3 Flash는 시각을 정적인 시선이 아닌 적극적인 조사로 취급할 수 있습니다. 추론과 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 결합하여 모델은 계획을 수립한 다음 Python 코드를 작성하고 실행하여 이미지를 단계별로 확대, 자르기, 주석 추가 또는 조작하여 대답을 시각적으로 뒷받침합니다.

**사용 사례:**

- **확대 및 검사:** 모델은 세부정보가 너무 작을 때 (예: 멀리 있는 게이지 또는 일련번호를 읽는 경우) 이를 암시적으로 감지하고 더 높은 해상도로 영역을 잘라내고 다시 검사하는 코드를 작성합니다.
- **시각적 수학 및 플로팅:** 모델은 코드를 사용하여 다단계 계산을 실행할 수 있습니다 (예: 영수증의 항목 합계 또는 추출된 데이터에서 Matplotlib 차트 생성).
- **이미지 주석:** 모델이 이미지에 직접 화살표, 경계 상자 또는 기타 주석을 그려 '이 항목은 어디에 있어야 하나요?'와 같은 공간 관련 질문에 답변할 수 있습니다.

시각적 사고를 사용 설정하려면 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 도구로 구성하세요. 모델은 필요할 때 코드를 사용하여 이미지를 조작합니다.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

이미지를 사용한 코드 실행에 관한 자세한 내용은 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko#images)을 참고하세요.

### 멀티모달 함수 응답

[멀티모달 함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#multimodal)을 사용하면 사용자 함수 응답에 멀티모달 객체를 포함할 수 있어 모델의 함수 호출 기능을 더욱 효과적으로 활용할 수 있습니다. 표준 함수 호출은 텍스트 기반 함수 응답만 지원합니다.

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### 자바스크립트

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### 기본 제공 도구와 함수 호출 결합

Gemini 3에서는 동일한 API 호출에서 기본 제공 도구 (예: Google 검색, URL 컨텍스트, [기타](https://ai.google.dev/gemini-api/docs/tools?hl=ko))와 맞춤 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) 도구를 사용할 수 있어 더 복잡한 워크플로가 가능합니다. [도구 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko) 페이지에서 자세히 알아보세요.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Gemini 2.5에서 마이그레이션

Gemini 3는 현재까지 가장 강력한 모델 제품군이며 Gemini 2.5에 비해 단계적으로 개선되었습니다. 마이그레이션할 때는 다음 사항을 고려하세요.

- **사고:** 이전에 Gemini 2.5가 추론하도록 강제하기 위해 복잡한 프롬프트 엔지니어링 (예: 사고의 연쇄)을 사용한 경우 `thinking_level: "high"` 및 단순화된 프롬프트로 Gemini 3를 사용해 보세요.
- **온도 설정:** 기존 코드에서 온도를 명시적으로 설정하고 있다면(특히 결정적 출력을 위해 낮은 값으로 설정한 경우), 해당 파라미터를 삭제하고 Gemini 3의 기본값인 1.0을 사용하는 것이 좋습니다. 이는 복잡한 작업에서 잠재적인 루핑 문제나 성능 저하를 방지하는 위함입니다.
- **PDF 및 문서 이해:**
  밀도 높은 문서 파싱을 위해 특정 동작에 의존하고 있었다면, 정확도를 유지하기 위해 새로운 `media_resolution_high` 설정을 테스트해 보세요.
- **토큰 소비량:** Gemini 3 기본값으로 마이그레이션하면 PDF의 토큰 사용량은 **증가**할 수 있지만 동영상의 토큰 사용량은 **감소**할 수 있습니다. 기본 해상도 상승으로 인해 요청이 컨텍스트 윈도우를 초과한다면 미디어 해상도를 명시적으로 낮추는 것이 좋습니다.
- **이미지 분할:** 이미지 분할 기능 (객체의 픽셀 수준 마스크 반환)은 Gemini 3 Pro 또는 Gemini 3 Flash에서 지원되지 않습니다. 기본 이미지 분할이 필요한 워크로드의 경우, 사고를 끈 상태의 Gemini 2.5 Flash 또는 [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ko)을 계속 사용하는 것이 좋습니다.
- **컴퓨터 사용:** Gemini 3 Pro 및 Gemini 3 Flash는 [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)을 지원합니다. 2.5 시리즈와 달리 Computer Use 도구에 액세스하기 위해 별도의 모델을 사용할 필요가 없습니다.
- **도구 지원**: 이제 Gemini 3 모델에서 [내장 도구와 함수 호출을 결합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)할 수 있습니다. 이제 Gemini 3 모델에서도 [지도 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)이 지원됩니다.

## OpenAI 호환성

[OpenAI 호환성 레이어](https://ai.google.dev/gemini-api/docs/openai?hl=ko)를 사용하는 경우 표준 파라미터 (OpenAI의 `reasoning_effort`)는 Gemini (`thinking_level`)에 상응하는 파라미터로 자동 매핑됩니다.

## 프롬프트 권장사항

Gemini 3는 추론 모델이므로 프롬프트 작성 방식에도 변화가 필요합니다.

- **정확한 지시:** 입력 프롬프트는 간결하게 작성하세요. Gemini 3는 직접적이고 명확한 지시에 가장 잘 반응합니다. 이전 모델에서 사용되던 장황하거나 지나치게 복잡한 프롬프트 엔지니어링 기법은 과분석을 유발할 수 있습니다.
- **출력 장황도:** 기본적으로 Gemini 3는 덜 장황하며, 직접적이고 효율적인 답변을 제공하는 것을 선호합니다. 사용 사례에 보다 대화형이거나 "수다스러운" 페르소나가 필요한 경우, 프롬프트에서 명시적으로 모델을 유도해야 합니다 (예: "친근하고 말이 많은 조수처럼 설명해 주세요").
- **컨텍스트 관리:** 대규모 데이터 세트 (예: 전체 책, 코드베이스 또는 긴 동영상)로 작업할 때는 데이터 컨텍스트 뒤에 프롬프트 끝에 특정 요청 사항이나 질문을 배치하세요. '위의 정보를 바탕으로...'와 같은 문구로 질문을 시작하여 모델의 추론을 제공된 데이터에 고정합니다.

[프롬프트 엔지니어링 가이드](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko)에서 프롬프트 설계 전략에 대해 자세히 알아보세요.

## FAQ

1. **Gemini 3의 지식 단절 시점은 언제인가요?** Gemini 3 모델의 지식 단절 시점은 2025년 1월입니다. 최신 정보를 확인하려면 [그라운딩 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 도구를 사용하세요.
2. **컨텍스트 윈도우 한도는 어떻게 되나요?** Gemini 3 모델은 최대 100만 토큰의 입력 컨텍스트 윈도우와 최대 64,000의 토큰 출력을 지원합니다.
3. **Gemini 3에 무료 등급이 있나요?** Gemini 3 Flash`gemini-3-flash-preview` 및 3.1 Flash-Lite`gemini-3.1-flash-lite-preview`에는 Gemini API의 무료 등급이 있습니다. Google AI Studio에서 Gemini 3.1 Pro와 3 Flash를 무료로 사용해 볼 수 있지만 Gemini API의 `gemini-3.1-pro-preview`에는 무료 등급이 없습니다.
4. **이전 `thinking_budget` 코드가 계속 작동하나요?** 예, `thinking_budget`는 이전 버전과의 호환성을 위해 계속 지원되지만 더 예측 가능한 성능을 위해 `thinking_level`로 마이그레이션하는 것이 좋습니다. 동일한 요청에서 두 가지를 모두 사용하지 마세요.
5. **Gemini 3는 Batch API를 지원하나요?** 예, Gemini 3는 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)를 지원합니다.
6. **컨텍스트 캐싱이 지원되나요?** 예, Gemini 3에서는 [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)이 지원됩니다.
7. **Gemini 3에서 지원되는 도구는 무엇인가요?** Gemini 3는 [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko), [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko), [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)를 지원합니다. 또한 자체 맞춤 도구와 [기본 제공 도구와의 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)을 위한 표준 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)도 지원합니다.
8. **`gemini-3.1-pro-preview-customtools`이란 무엇인가요?** `gemini-3.1-pro-preview`를 사용하고 있는데 모델이 bash 명령어를 선호하여 맞춤 도구를 무시하는 경우 `gemini-3.1-pro-preview-customtools` 모델을 대신 사용해 보세요. 자세한 내용은 [여기](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko#gemini-31-pro-preview-customtools)를 참고하세요.

## 다음 단계

- [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=ko#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D) 시작하기
- [사고 수준](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=ko#gemini3) 및 사고 예산에서 사고 수준으로 이전하는 방법에 관한 전용 Cookbook 가이드를 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
