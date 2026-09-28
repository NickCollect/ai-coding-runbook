---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=ko
fetched_at: 2026-09-28T06:29:32.389477+00:00
title: "\uc6b0\uc120\uc21c\uc704 \ucd94\ub860 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)

의견 보내기

# 우선순위 추론

설명: 우선순위 추론 등급으로 지연 시간을 최적화하는 방법을 알아봅니다.

Gemini Priority API는 지연 시간이 짧고 최고 수준의 안정성이 필요한 비즈니스에 중요한 워크로드를 위해 설계된 프리미엄 추론 등급입니다. 우선순위 등급 트래픽은 표준 API 및 Flex 등급 트래픽보다 우선순위가 높습니다.

우선순위 추론은 [Tier 2 & Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=ko#about-billing) 사용자가 GenerateContent API
및 Interactions API 엔드포인트에서 사용할 수 있습니다.

## 우선순위 사용 방법

우선순위 등급을 사용하려면 요청 본문의 `service_tier` 필드를 `priority`로 설정합니다. 필드가 생략되면 기본 등급은 표준입니다.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## 우선순위 추론 작동 방식

우선순위 추론은 요청을 중요도가 높은 컴퓨팅 대기열로 라우팅하여 사용자 대상 애플리케이션에 예측 가능하고 빠른 성능을 제공합니다. 기본 메커니즘은 동적 한도를 초과하는 트래픽에 대한 표준 처리로의 점진적인 서버 측 다운그레이드입니다. 이렇게 하면 요청이 실패하는 대신 애플리케이션 안정성이 보장됩니다.

| 기능 | 우선순위 | 표준 | Flex | 일괄 |
| --- | --- | --- | --- | --- |
| **가격 책정** | 표준보다 75~100% 더 높음 | 정상가 | 50% 할인 | 50% 할인 |
| **지연 시간** | 초 | 수 초에서 수 분 | 분 (1~15분 목표) | 최대 24시간 |
| **안정성** | 높음 (삭제 불가) | 높음 / 중간-높음 | 최대한 노력 (삭제 가능) | 높음 (처리량) |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 |

### 주요 이점

- **지연 시간 단축**: 대화형
  사용자 대상 AI 도구의 초 단위 응답 시간을 위해 설계되었습니다.
- **높은 안정성**: 트래픽은 중요도가 가장 높은 것으로 처리되며
  엄격하게 삭제할 수 없습니다.
- **점진적 대처**: 동적 한도를 초과하는 트래픽 급증은 실패하는 대신 처리를 위해
  자동으로 표준 등급으로 다운그레이드되어
  서비스 중단을 방지합니다.
- **낮은 마찰**: 표준 및 Flex 등급과 동일한 동기식 `generateContent` 메서드를 사용합니다.

### 사용 사례

우선순위 처리는 성능과 안정성이 가장 중요한 비즈니스에 중요한 워크플로에 적합합니다.

- **대화형 AI 애플리케이션**: 사용자가 프리미엄을 지불하고 빠르고 일관된 응답을 기대하는 고객 서비스 챗봇 및 코파일럿입니다.
- **실시간 의사결정 엔진**: 실시간 티켓 분류 또는 사기 감지와 같이 안정성이 높고 지연 시간이 짧은
  결과가 필요한 시스템입니다.
- **프리미엄 고객 기능**: 유료 고객에게 더 높은 서비스
  수준 목표 (SLO)를 보장해야 하는 개발자입니다.

### 비율 제한

우선순위 소비는 소비가 [전체 대화형 트래픽 비율 제한](https://aistudio.google.com/rate-limit?hl=ko)에
포함되더라도 자체 비율 제한을 유지합니다. 우선순위 추론의 기본 비율 제한은 **모델 / 등급의 표준 비율 제한의 0.3배** 입니다.

### 점진적 다운그레이드 로직

정체로 인해 우선순위 한도를 초과하는 경우 오버플로 요청은 503 또는 429 오류로 실패하는 대신 표준 처리로 **자동으로 점진적으로** 다운그레이드됩니다. 다운그레이드된 요청은 우선순위 프리미엄 요금이 아닌 표준 요금으로 청구됩니다.

### 클라이언트 책임

- **응답 모니터링**: 개발자는 요청이 `x-gemini-service-tier`
  로 자주 다운그레이드되는지 감지하기 위해 API 응답의
  헤더를 모니터링해야 합니다.`standard`
- **재시도**: 클라이언트는
  표준 오류(예: `DEADLINE_EXCEEDED`)에 대해 재시도 로직/지수 백오프를 구현해야 합니다.

## 가격 책정

우선순위 추론은 [표준 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)보다 75~100% 더 비싸며 토큰당 청구됩니다.

## 지원되는 모델

다음 모델은 우선순위 추론을 지원합니다.

| 모델 | 우선순위 추론 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 미리보기](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 미리보기](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 3 Pro 이미지 미리보기](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash 이미지](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 다음 단계

Gemini의 다른 [추론 및 최적화](https://ai.google.dev/gemini-api/docs/optimization?hl=ko) 옵션에 대해 알아봅니다.

- [비용을 50% 절감하는](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko) Flex 추론
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 24시간 이내에 비동기 처리를 위한
- [입력 토큰 비용 절감을 위한 컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-12(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-12(UTC)"],[],[]]
