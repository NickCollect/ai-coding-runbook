---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko
fetched_at: 2026-05-05T20:08:40.984391+00:00
title: "\ubbf8\ub514\uc5b4 \ud574\uc0c1\ub3c4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 미디어 해상도

`media_resolution` 매개변수는 미디어 입력에 할당된 **최대 토큰 수** 를 결정하여 Gemini API가 이미지, 동영상, PDF 문서와 같은 미디어 입력을 처리하는 방식을 제어하므로 응답 품질과 지연 시간 및 비용 간의 균형을 맞출 수 있습니다. 다양한 설정, 기본값, 토큰과의 상호 관계는 [토큰 수](#token-counts) 섹션을 참고하세요.

미디어 해상도는 다음 두 가지 방법으로 구성할 수 있습니다.

- [부분별](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko#per-part-media-resolution) (Gemini 3만 해당)
- [전체](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko#global-media-resolution) `generateContent` 요청에 대해 전역적으로 (모든 멀티모달 모델)

## 부분별 미디어 해상도 (Gemini 3만 해당)

Gemini 3을 사용하면 요청 내에서 개별 미디어 객체의 미디어 해상도를 설정하여 토큰 사용을 세부적으로 최적화할 수 있습니다. 단일 요청에서 해상도 수준을 혼합할 수 있습니다. 예를 들어 복잡한 다이어그램에는 고해상도를 사용하고 간단한 컨텍스트 이미지에는 저해상도를 사용합니다. 이 설정은 특정 부분의 전역 구성을 재정의합니다. 기본 설정은 [토큰 수](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko#token-counts) 섹션을 참고하세요.

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### 자바스크립트

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## 전역 미디어 해상도

`GenerationConfig`를 사용하여 요청의 모든 미디어 부분에 기본 해상도를 설정할 수 있습니다. 이 기능은 모든 멀티모달 모델에서 지원됩니다. 요청에 전역 설정과 [부분별 설정](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ko#per-part-media-resolution)이 모두 포함된 경우 해당 특정 항목에 부분별 설정이 우선 적용됩니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## 사용 가능한 해상도 값

Gemini API는 미디어 해상도에 대해 다음 수준을 정의합니다.

- `MEDIA_RESOLUTION_UNSPECIFIED`: 기본 설정입니다. 이 수준의 토큰 수는 Gemini 3과 이전 Gemini 모델 간에 크게 다릅니다.
- `MEDIA_RESOLUTION_LOW`: 토큰 수가 적어 처리 속도가 빠르고 비용이 저렴하지만 세부정보가 적습니다.
- `MEDIA_RESOLUTION_MEDIUM`: 세부정보, 비용, 지연 시간 간의 균형입니다.
- `MEDIA_RESOLUTION_HIGH`: 토큰 수가 많아 모델이 사용할 수 있는 세부정보가 많지만 지연 시간과 비용이 증가합니다.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (부분별만 해당): 토큰 수가 가장 많으며 특정
  사용 사례(예: [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko))에 필요합니다.

`MEDIA_RESOLUTION_HIGH`는 대부분의 사용 사례에서 최적의 성능을 제공합니다.

이러한 각 수준에 대해 생성되는 정확한 토큰 수는 **미디어 유형** (이미지, 동영상, PDF)과 **모델 버전** 에 따라 다릅니다.

## 토큰 수

아래 표에는 모델 계열별로 각 `media_resolution` 값과 미디어 유형에 대한 대략적인 토큰 수가 요약되어 있습니다.

**Gemini 3 모델**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **이미지** | **동영상** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (기본값) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + 기본 텍스트 |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + 기본 텍스트 |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + 기본 텍스트 |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | 해당 사항 없음 | 해당 사항 없음 |

**Gemini 2.5 모델**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **이미지** | **동영상** | **PDF (스캔됨)** | **PDF (기본)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (기본값) | 256 + 화면 이동 및 스캔 (~2048) | 256 | 256 + OCR | 256 + 기본 텍스트 |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + 기본 텍스트 |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + 기본 텍스트 |
| `MEDIA_RESOLUTION_HIGH` | 256 + 화면 이동 및 스캔 | 256 | 256 + OCR | 256 + 기본 텍스트 |

## 적절한 해상도 선택

- **기본값 (`UNSPECIFIED`):** 기본값으로 시작합니다. 가장 일반적인 사용 사례에서 품질, 지연 시간, 비용 간의 적절한 균형을 위해 조정됩니다.
- **`LOW`:** 비용과 지연 시간이 가장 중요하고 세부정보가 덜 중요한 시나리오에 사용합니다.
- **`MEDIUM` / `HIGH`:** 태스크에서 미디어 내의 복잡한 세부정보를 이해해야 하는 경우 해상도를 높입니다. 이는 복잡한 시각적 분석, 차트 읽기 또는 밀도 높은 문서 이해에 필요한 경우가 많습니다.
- **`ULTRA HIGH`** - 부분별 설정에만 사용할 수 있습니다. 컴퓨터 사용과 같은 특정 사용 사례 또는 테스트에서 `HIGH`보다 명확한 개선이 확인되는 경우에 권장됩니다.
- **부분별 제어 (Gemini 3):** 토큰 사용을 최적화합니다. 예를 들어 이미지가 여러 개인 프롬프트에서 복잡한 다이어그램에는 `HIGH`를 사용하고 더 간단한 컨텍스트 이미지에는 `LOW` 또는 `MEDIUM`을 사용합니다.

**권장 설정**

다음은 지원되는 각 미디어 유형에 권장되는 미디어 해상도 설정을 나열한 것입니다.

|  |  |  |  |
| --- | --- | --- | --- |
| **미디어 유형** | **권장 설정** | **최대 토큰 수** | **사용 가이드** |
| **이미지** | `MEDIA_RESOLUTION_HIGH` | 1120 | 최대 품질을 보장하기 위해 대부분의 이미지 분석 작업에 권장됩니다. |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | 문서 이해에 최적입니다. 품질은 일반적으로 `medium`에서 포화됩니다. `high`로 늘려도 표준 문서의 OCR 결과가 개선되는 경우는 거의 없습니다. |
| **동영상** (일반) | `MEDIA_RESOLUTION_LOW` (또는 `MEDIA_RESOLUTION_MEDIUM`) | 70 (프레임당) | **참고:** 동영상의 경우 컨텍스트 사용을 최적화하기 위해 `low` 및 `medium` 설정이 동일하게 처리됩니다 (토큰 70개). 이는 대부분의 동작 인식 및 설명 작업에 충분합니다. |
| **동영상** (텍스트가 많은 경우) | `MEDIA_RESOLUTION_HIGH` | 280 (프레임당) | 사용 사례에 밀도 높은 텍스트 (OCR) 또는 동영상 프레임 내의 작은 세부정보를 읽는 것이 포함된 경우에만 필요합니다. |

품질, 지연 시간, 비용 간의 최적의 절충점을 찾으려면 항상 다양한 해상도 설정이 특정 애플리케이션에 미치는 영향을 테스트하고 평가하세요.

## 버전 호환성 요약

- `MediaResolution` 열거형은 미디어 입력을 지원하는 모든 모델에서 사용할 수 있습니다.
- 각 열거형 수준과 연결된 토큰 수는 Gemini 3 모델과 이전 Gemini 버전 간에 **다릅니다**.
- 개별 `Part` 객체에서 `media_resolution`을 설정하는 것은 **Gemini 3 모델에만 해당** 됩니다.

## 다음 단계

- [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko), [동영상 이해](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko),
  [문서 이해](https://ai.google.dev/gemini-api/docs/document-processing?hl=ko) 가이드에서 Gemini API의 멀티모달 기능에 대해 자세히 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
