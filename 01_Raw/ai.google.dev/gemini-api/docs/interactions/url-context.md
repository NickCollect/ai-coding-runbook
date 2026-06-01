---
source_url: https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ko
fetched_at: 2026-06-01T06:09:29.869664+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# URL 컨텍스트

[URL 컨텍스트 도구를 사용하면 URL 형식으로 모델에 추가 컨텍스트를 제공할 수 있습니다. 요청에 URL을 포함하면 모델은 제한사항 섹션에 나열된 URL 유형이 아닌 경우 해당 페이지의 콘텐츠에 액세스하여 응답에 정보를 제공하고 응답을 개선합니다.](#limitations)

URL 컨텍스트 도구는 다음과 같은 태스크에 유용합니다.

- **데이터 추출**: 여러 URL에서 가격, 이름 또는 주요
  결과와 같은 특정 정보를 가져옵니다.
- **문서 비교**: 여러 보고서, 기사 또는 PDF를 분석하여
  차이점을 파악하고 추세를 추적합니다.
- **콘텐츠 종합 및 생성**: 여러 소스 URL의 정보를 결합하여 정확한 요약, 블로그 게시물 또는 보고서를 생성합니다.
- **코드 및 문서 분석**: GitHub 저장소 또는 기술 문서를 가리켜 코드를 설명하거나, 설정 안내를 생성하거나, 질문에 답변합니다.

다음 예에서는 서로 다른 웹사이트의 두 가지 레시피를 비교하는 방법을 보여줍니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## 작동 방식

URL 컨텍스트 도구는 2단계 검색 프로세스를 사용하여 속도, 비용, 최신 데이터 액세스의 균형을 맞춥니다. URL을 제공하면 도구는 먼저 내부 색인 캐시에서 콘텐츠를 가져오려고 시도합니다. 이는 고도로 최적화된 캐시 역할을 합니다. URL이 색인에서 제공되지 않는 경우 (예: 매우 새로운 페이지인 경우) 도구는 자동으로 실시간 가져오기를 실행합니다.
이렇게 하면 URL에 직접 액세스하여 콘텐츠를 실시간으로 가져올 수 있습니다.

## 다른 도구와 결합

URL 컨텍스트 도구를 다른 도구와 결합하여 더 강력한 워크플로를 만들 수 있습니다.

[Gemini 3 모델](#supported-models)은 기본 제공 도구
(URL 컨텍스트와 같은)를 커스텀 도구 (함수 호출)와 결합하는 것을 지원합니다. 도구 조합
 페이지에서 자세히 알아보세요.

### 검색을 사용한 그라운딩

URL 컨텍스트와
[Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/grounding?hl=ko)이 모두 사용 설정되면
모델은 검색 기능을 사용하여
온라인에서 관련 정보를 찾은 다음 URL 컨텍스트 도구를 사용하여
찾은 페이지를 더 심층적으로 이해할 수 있습니다. 이 접근 방식은 광범위한 검색과 특정 페이지의 심층 분석이 모두 필요한 프롬프트에 유용합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## 응답 이해

모델이 URL 컨텍스트 도구를 사용하면 텍스트 응답에 텍스트 콘텐츠 블록에 인라인 `url_citation` 주석이 포함됩니다. 각 주석은 응답 텍스트의 세그먼트를 (`start_index` 및 `end_index`를 통해) 파생된 소스 URL에 연결합니다. 이는 애플리101}케이션에서 인용을 표시하는 기본 방법입니다. 인용을 추출하는 방법은 위의 [기본 예시](#get-started)를 참고하세요.

응답에는 각 URL 검색 시도 (상태, 검색된 URL)에 관한 메타데이터가 포함된 `url_context_result` 단계도 포함됩니다. 이는 주로 디버깅에 유용합니다.

### 안전 확인

시스템은 URL이 안전 표준을 충족하는지 확인하기 위해 URL에 대한 콘텐츠 검토를 수행합니다. URL이 이 검사를 통과하지 못하면 해당
`url_context_result` 단계에 `status`가 `"unsafe"`로 표시됩니다.

### 토큰 수

프롬프트에 지정한 URL에서 검색된 콘텐츠는 입력 토큰의 일부로 계산됩니다. 상호작용의 `usage` 객체에서 토큰 수를 확인할 수 있습니다. 다음은 그 예시입니다.

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

토큰당 가격은 사용된 모델에 따라 다릅니다. 자세한 내용은
[가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko) 페이지를 참고하세요.

## 지원되는 모델

| 모델 | URL 컨텍스트 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 권장사항

- **특정 URL 제공**: 최상의 결과를 얻으려면 모델이 분석할 콘텐츠의 직접 URL을 제공하세요. 모델은 중첩된 링크의 콘텐츠가 아닌 제공된 URL의 콘텐츠만 검색합니다.
- **접근성 확인**: 제공하는 URL이 로그인해야 하거나 페이월 뒤에 있는
  페이지로 연결되지 않는지 확인합니다.
- **전체 URL 사용**: 프로토콜을 포함한 전체 URL을 제공합니다
  (예: google.com 대신 https://www.google.com).

## 제한사항

- 요청 한도: 이 도구는 요청당 최대 20개의 URL을 처리할 수 있습니다.
- URL 콘텐츠 크기: 단일 URL에서 검색된 콘텐츠의 최대 크기는 34MB입니다.
- 공개 접근성: URL은 웹에서 공개적으로 액세스할 수 있어야 합니다.
  localhost 주소 (예: localhost, 127.0.0.1), 비공개 네트워크, 터널링 서비스 (예: ngrok, pinggy)는 지원되지 않습니다.
- Gemini API만 해당: URL 컨텍스트는 Gemini Enterprise Agent Platform을 통해서가 아니라 Gemini API에서만 사용할 수 있습니다.

### 지원되는 콘텐츠 유형과 지원되지 않는 콘텐츠 유형

이 도구는 다음 콘텐츠 유형의 URL에서 콘텐츠를 추출할 수 있습니다.

- 텍스트 (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- 이미지 (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

다음 콘텐츠 유형은 지원되지 **않습니다**.

- 페이월 콘텐츠
- YouTube 동영상 ([동영상 이해](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ko#youtube) 참고
  YouTube URL을 처리하는 방법은)
- Google Docs 또는 스프레드시트와 같은 Google Workspace 파일
- 동영상 및 오디오 파일

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-28(UTC)"],[],[]]
