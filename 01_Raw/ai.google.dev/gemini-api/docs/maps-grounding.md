---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko
fetched_at: 2026-05-05T20:42:38.023151+00:00
title: "Google \uc9c0\ub3c4\ub97c \uc0ac\uc6a9\ud55c \uadf8\ub77c\uc6b4\ub529 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google 지도를 사용한 그라운딩

Google 지도 기반 그라운딩은 Gemini의 생성 기능을 Google 지도의 풍부하고 사실에 기반한 최신 데이터와 연결합니다. 이 기능을 사용하면 개발자가 위치 인식 기능을 애플리케이션에 쉽게 통합할 수 있습니다. 사용자 질문에 지도 데이터와 관련된 맥락이 있는 경우 Gemini 모델은 Google 지도를 활용하여 사용자가 지정한 위치 또는 대략적인 위치와 관련된 사실에 기반한 최신 답변을 제공합니다.

- **정확한 위치 인식 응답:** 지리적으로 구체적인 질문에 Google 지도의 광범위하고 최신 데이터를 활용합니다.
- **개인화 개선:** 사용자 제공 위치를 기반으로 추천 및 정보를 맞춤설정합니다.
- **컨텍스트 정보 및 위젯:** 생성된 콘텐츠와 함께 대화형 Google 지도 위젯을 렌더링하는 컨텍스트 토큰

## 시작하기

이 예시에서는 Google 지도 기반 그라운딩을 애플리케이션에 통합하여 사용자 질문에 정확한 위치 인식 응답을 제공하는 방법을 보여줍니다. 프롬프트는 선택적 사용자 위치와 함께 현지 추천을 요청하여 Gemini 모델이 Google 지도 데이터를 사용할 수 있도록 합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Google 지도 기반 그라운딩 작동 방식

Google 지도 기반 그라운딩은 Maps API를 그라운딩 소스로 사용하여 Gemini API를 Google 지리 생태계와 통합합니다. 사용자의 질문에 지리적 맥락이 포함된 경우 Gemini 모델은 Google 지도 기반 그라운딩 도구를 호출할 수 있습니다. 그러면 모델이 제공된 위치와 관련된 Google 지도 데이터를 기반으로 그라운딩된 대답을 생성할 수 있습니다.

이 프로세스에는 일반적으로 다음이 포함됩니다.

1. **사용자 쿼리:** 사용자가 애플리케이션에 쿼리를 제출합니다. 여기에는 지리적 컨텍스트 (예: '내 주변 카페', '샌프란시스코 박물관')가 포함될 수 있습니다.
2. **도구 호출:** 지리적 의도를 인식한 Gemini 모델이 Google 지도 기반 그라운딩 도구를 호출합니다. 이 도구에는 선택적으로 사용자의 `latitude` 및 `longitude`이 제공될 수 있습니다. 이 도구는 텍스트 검색 도구이며, 로컬 쿼리 ('내 주변')는 좌표를 사용하는 반면 구체적이거나 비로컬 쿼리는 명시적 위치의 영향을 받지 않을 가능성이 높다는 점에서 지도에서 검색하는 것과 유사하게 작동합니다.
3. **데이터 검색:** Google 지도 기반 그라운딩 서비스는 Google 지도에 관련 정보 (예: 장소, 리뷰, 사진, 주소, 영업시간)를 쿼리합니다.
4. **그라운딩된 생성:** 검색된 지도 데이터는 Gemini 모델의 대답에 정보를 제공하여 사실적 정확성과 관련성을 보장합니다.
5. **대답 및 위젯 토큰:** 모델이 Google 지도 소스에 대한 인용이 포함된 텍스트 대답을 반환합니다. 선택적으로 API 응답에는 `google_maps_widget_context_token`도 포함될 수 있으므로 개발자가 시각적 상호작용을 위해 애플리케이션에서 컨텍스트 Google 지도 위젯을 렌더링할 수 있습니다.

## Google 지도 기반 그라운딩을 사용해야 하는 이유 및 조건

Google 지도 기반 그라운딩은 정확하고 최신이며 위치별 정보가 필요한 애플리케이션에 적합합니다. 전 세계 2억 5천만 개 이상의 장소로 구성된 Google 지도의 광범위한 데이터베이스를 기반으로 관련성 높은 맞춤 콘텐츠를 제공하여 사용자 환경을 개선합니다.

애플리케이션에서 다음 작업을 수행해야 하는 경우 Google 지도 기반 그라운딩을 사용해야 합니다.

- 지역별 질문에 대해 완전하고 정확한 대답을 제공합니다.
- 대화형 여행 계획 도구와 현지 가이드를 빌드하세요.
- 위치 및 음식점이나 상점과 같은 사용자 환경설정을 기반으로 관심 장소를 추천합니다.
- 소셜, 소매 또는 음식 배달 서비스를 위한 위치 인식 환경을 만드세요.

Google 지도 기반 그라운딩은 '가장 가까운 커피숍'을 찾거나 길을 안내받는 등 근접성과 현재 사실 데이터가 중요한 사용 사례에서 뛰어납니다.

## API 메서드 및 매개변수

Google 지도 기반 그라운딩은 Gemini API를 통해 [`generateContent`](https://ai.google.dev/api/generate-content?hl=ko) 메서드 내의 도구로 노출됩니다. 요청의 `tools` 매개변수에 [`googleMaps`](https://ai.google.dev/api/caching?hl=ko#GoogleMaps) 객체를 포함하여 Google 지도 기반 그라운딩을 사용 설정하고 구성합니다.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

[`googleMaps`](https://ai.google.dev/api/caching?hl=ko#GoogleMaps) 도구는 불리언 `enableWidget` 파라미터를 추가로 허용할 수 있으며, 이는 [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=ko#GroundingMetadata) 필드가 대답에 반환되는지 여부를 제어하는 데 사용됩니다. 이를 사용하여 [컨텍스트 Places 위젯](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=ko)을 표시할 수 있습니다.

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
}
```

또한 이 도구는 컨텍스트 위치를 `toolConfig`로 전달하는 것을 지원합니다.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### 그라운딩 응답 이해하기

Google 지도 데이터로 대답이 성공적으로 그라운딩되면 대답에 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ko#GroundingMetadata) 필드가 포함됩니다.
이 구조화된 데이터는 서비스 사용 요구사항을 충족할 뿐만 아니라 애플리케이션에서 주장을 확인하고 풍부한 인용 환경을 구축하는 데 필수적입니다.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

Gemini API는 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ko#GroundingMetadata)와 함께 다음 정보를 반환합니다.

- `groundingChunks`: `maps` 소스 (`uri`, `placeId`, `title`)가 포함된 객체의 배열입니다.
- `groundingSupports`: 모델 응답 텍스트를 `groundingChunks`의 소스에 연결하는 청크 배열입니다. 각 청크는 텍스트 범위 (`startIndex` 및 `endIndex`로 정의됨)를 하나 이상의 `groundingChunkIndices`에 연결합니다. 인라인 인용을 만드는 데 필요한 키입니다.
- `googleMapsWidgetContextToken`: [맥락에 맞는 장소 위젯](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=ko)을 렌더링하는 데 사용할 수 있는 텍스트 토큰입니다.

텍스트에 인라인 인용을 렌더링하는 방법을 보여주는 코드 스니펫은 Google 검색을 사용한 그라운딩 문서의 [예시](https://ai.google.dev/gemini-api/docs/google-search?hl=ko#attributing_sources_with_inline_citations)를 참고하세요.

### Google 지도 컨텍스트 위젯 표시

반환된 `googleMapsWidgetContextToken`를 사용하려면 [Google Maps JavaScript API를 로드](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=ko)해야 합니다.

## 사용 사례

Google 지도 기반 그라운딩은 다양한 위치 인식 사용 사례를 지원합니다. 다음 예에서는 다양한 프롬프트와 파라미터가 Google 지도 기반 그라운딩을 활용하는 방법을 보여줍니다. Google 지도 그라운딩 결과의 정보는 실제 상황과 다를 수 있습니다.

### 장소 관련 질문 처리

특정 장소에 관해 자세한 질문을 하면 Google 사용자 리뷰 및 기타 지도 데이터를 기반으로 답변을 받을 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### 위치 기반 맞춤설정 제공

사용자의 선호도와 특정 지역에 맞게 맞춤 추천을 받습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### 여행 일정 계획 지원

여행 애플리케이션에 적합한 다양한 위치에 관한 정보와 경로가 포함된 여러 날짜의 계획을 생성합니다.

이 예에서는 Google 지도 도구에서 위젯을 사용 설정하여 `googleMapsWidgetContextToken`가 요청되었습니다. 사용 설정하면 반환된 토큰을 사용하여 Google Maps JavaScript API의 `<gmp-places-contextual> component`를 사용하여 컨텍스트 장소 위젯을 렌더링할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

위젯이 렌더링되면 다음과 같이 표시됩니다.

![렌더링된 지도 위젯의 예](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=ko)

## 서비스 사용 요구사항

이 섹션에서는 Google 지도 그라운딩에 대한 서비스 사용 요구사항을 설명합니다.

### 사용자에게 Google 지도 소스 사용 알림

각 Google 지도 그라운딩 결과와 함께 각 응답을 지원하는 `groundingChunks`의 소스가 수신됩니다. 다음 메타데이터도 반환됩니다.

- 소스 URI
- 제목
- ID

Google 지도 기반 그라운딩 결과를 표시할 때는 연결된 Google 지도 소스를 명시하고 사용자에게 다음 사항을 알려야 합니다.

- Google 지도 소스는 해당 소스를 뒷받침하는 생성된 콘텐츠 직후에 따라와야 합니다. 이렇게 생성된 콘텐츠를 Google 지도 그라운딩 결과라고도 합니다.
- Google 지도 소스는 단일 사용자 상호작용 내에서 확인 가능해야 합니다.

### Google 지도 소스를 Google 지도 링크와 함께 표시

`groundingChunks`와 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 내의 각 소스에 대해 다음 요구사항에 따라 링크 미리보기를 생성해야 합니다.

- 각 소스는 Google 지도에서 제공한 것임을 명시하고 Google 지도의 텍스트 [저작자 표시 지침](#maps-attribution-guidelines)을 따라야 합니다.
- 응답에 포함된 소스 제목을 표시해야 합니다.
- 응답에 제공된 `uri` 또는 `googleMapsUri`를 사용하여 소스에 연결해야 합니다.

아래 이미지는 소스와 Google 지도 링크를 표시하기 위한 최소 요구사항을 보여줍니다.

![소스가 표시된 응답 포함 프롬프트](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=ko)

또한 소스 보기 영역은 접을 수 있습니다.

![응답과 소스가 접힌 프롬프트](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=ko)

선택사항: 링크 미리보기를 다음과 같은 추가 콘텐츠로 보강할 수 있습니다.

- Google 지도 텍스트 저작자 표시 앞에 [Google 지도 파비콘](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=ko)을 삽입합니다.
- 소스 URL에서 제공되는 사진(예: `og:image`)을 표시합니다.

일부 Google 지도 데이터 제공업체 및 해당 라이선스 조건에 대한 자세한 내용은 [Google 지도 및 Google 어스 법적 고지](https://www.google.com/help/legalnotices_maps/?hl=ko)를 참고하세요.

### Google 지도 텍스트 저작자 표시 가이드라인

Google 지도의 텍스트 저작자 소스를 표시할 때는 다음 가이드라인을 따라야 합니다.

- Google 지도 텍스트를 어떤 방식으로도 수정하지 마세요.
  - Google 지도의 대소문자를 변경하지 마세요.
  - Google 지도를 여러 줄로 나누어 표시하지 마세요.
  - Google 지도를 다른 언어로 현지화하지 마세요.
  - 브라우저가 Google 지도를 번역하지 못하도록 HTML 속성 translate="no"를 사용해야 합니다.
- 다음 표에 설명된 대로 Google 지도 텍스트 스타일을 지정해야 합니다.

| 속성 | 스타일 |
| --- | --- |
| `Font family` | Roboto. 글꼴 로드는 선택사항입니다. |
| `Fallback font family` | 제품에서 이미 사용 중인 sans serif 본문 글꼴 또는 'Sans-Serif'를 지정해 기본 시스템 글꼴을 호출합니다. |
| `Font style` | 보통 |
| `Font weight` | 400 |
| `Font color` | 흰색, 검정(#1F1F1F) 또는 회색(#5E5E5E). 배경 대비를 고려해 접근성 비율(4.5:1)을 유지해야 합니다. |
| `Font size` | - 최소 글꼴 크기: 12sp - 최대 글꼴 크기: 16sp - sp에 대해 자세히 알아보려면 [Material Design 웹사이트](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)의 글꼴 크기 단위를 참고하세요. |
| `Spacing` | 보통 |

#### 예시 CSS

다음 CSS는 흰색 또는 밝은 배경에서 Google 지도를 적절한 타이포그래픽 스타일과 색상으로 렌더링합니다.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### 컨텍스트 토큰, 장소 ID, 리뷰 ID

Google 지도 데이터에는 컨텍스트 토큰, 장소 ID, 리뷰 ID가 포함됩니다. 다음 응답 데이터를 캐시, 저장, 내보내기할 수 있습니다.

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Google 지도 기반 그라운딩 약관에 명시된 캐싱 제한사항은 적용되지 않습니다.

### 금지된 활동 및 지역

Google 지도 기반 그라운딩은 안전하고 신뢰할 수 있는 플랫폼을 유지하기 위해 특정 콘텐츠 및 활동에 추가 제한을 둡니다. [약관](https://ai.google.dev/gemini-api/terms?hl=ko#grounding-with-google-maps)의 사용 제한 외에도 다음 사항에 동의합니다.

- 응급 대응 서비스를 비롯한 고위험 활동에 Google 지도 기반 그라운딩을 사용하지 않습니다.
- '금지 지역'에서 Google 지도 그라운딩을 제공하는 애플리케이션을 배포하거나 마케팅하지 않습니다. 현재 금지된 지역은 다음과 같습니다.

  - 중국
  - 크리미아
  - 쿠바
  - 도네츠크 인민공화국
  - 이란
  - 루한스크 인민공화국
  - 북한
  - 시리아
  - 베트남

  이 목록은 때때로 업데이트될 수 있습니다.

## 권장사항

- **사용자 위치 제공:** 가장 관련성 높은 맞춤형 대답을 위해 사용자의 위치를 알 수 있는 경우 항상 `googleMapsGrounding` 구성에 `user_location` (위도 및 경도)를 포함하세요.
- **Google 지도 컨텍스트 위젯 렌더링:** 컨텍스트 위젯은 Gemini API 응답에 포함된 컨텍스트 토큰인 `googleMapsWidgetContextToken`을 사용하여 렌더링됩니다. 이 토큰을 활용하면 Google 지도의 시각적 콘텐츠를 렌더링할 수 있습니다. 컨텍스트 위젯에 대한 자세한 내용은 Google 개발자 가이드의 [Google 지도 기반 그라운딩 위젯](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=ko)을 참고하세요.
- **최종 사용자에게 알림:** 특히 도구가 사용 설정된 경우 Google 지도 데이터가 사용자의 질문에 답변하는 데 사용된다는 사실을 최종 사용자에게 명확하게 알립니다.
- **지연 시간 모니터링:** 대화형 애플리케이션의 경우 그라운딩된 대답의 P95 지연 시간이 허용 가능한 기준점 내에 유지되어 원활한 사용자 환경을 유지해야 합니다.
- **필요하지 않을 때 사용 중지:** Google 지도 기반 그라운딩은 기본적으로 사용 중지되어 있습니다. 성능과 비용을 최적화하려면 쿼리에 명확한 지리적 컨텍스트가 있는 경우에만 사용 설정 (`"tools": [{"googleMaps": {}}]`)하세요.

## 제한사항

- **지리적 범위:** Google 지도 기반 그라운딩은 전 세계에서 사용할 수 있습니다.
- **모델 지원:** [지원되는 모델](#supported-models) 섹션을 참고하세요.
- **멀티모달 입력/출력:** 현재 Google 지도 기반 그라운딩은 텍스트 및 컨텍스트 지도 위젯을 넘어 멀티모달 입력 또는 출력을 지원하지 않습니다.
- **기본 상태:** Google 지도 기반 그라운딩 도구는 기본적으로 사용 중지되어 있습니다.
  API 요청에서 명시적으로 사용 설정해야 합니다.

## 가격 및 비율 제한

Google 지도 기반 그라운딩 가격은 쿼리를 기반으로 합니다. 현재 요금은 **그라운딩된 프롬프트 1,000개당 25달러**입니다. 무료 등급에서는 일일 최대 500개의 요청도 사용할 수 있습니다. 프롬프트가 하나 이상의 Google 지도 그라운딩 결과 (즉, 하나 이상의 Google 지도 소스를 포함하는 결과)를 성공적으로 반환하는 경우에만 요청이 할당량에 포함됩니다. 단일 요청에서 Google 지도에 여러 쿼리가 전송되면 비율 제한에 대해 하나의 요청으로 계산됩니다.

자세한 가격 정보는 [Gemini API 가격 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.

## 지원되는 모델

다음 모델은 Google 지도 기반 그라운딩을 지원합니다.

| 모델 | Google 지도를 사용한 그라운딩 |
| --- | --- |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=ko) | ✔️ |

## 지원되는 도구 조합

Gemini 3 모델은 내장 도구 (예: Google 지도 기반 그라운딩)와 맞춤 도구 (함수 호출)의 조합을 지원합니다. [도구 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko) 페이지에서 자세히 알아보세요.

## 다음 단계

- [Gemini API 설명서의 Google 검색을 사용한 그라운딩](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ko)을 사용해 보세요.
- [사용 가능한 다른 도구](https://ai.google.dev/gemini-api/docs/tools?hl=ko)에 대해 알아보세요.
- 책임감 있는 AI 권장사항 및 Gemini API의 안전 필터에 대해 자세히 알아보려면 [안전 설정 가이드](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
