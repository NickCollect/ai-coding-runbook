---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=ko
fetched_at: 2026-05-25T05:24:38.672667+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Flex 추론

Gemini Flex API는 가변 지연 시간과 최선형 가용성을 제공하는 대신 표준 요금보다 50% 저렴한 추론 계층입니다. 동기식 처리가 필요하지만 표준 API의 실시간 성능은 필요하지 않은 지연 시간 허용 워크로드용으로 설계되었습니다.

## Flex 사용 방법

Flex 계층을 사용하려면 요청에서 `service_tier`를 `flex`로 지정하세요. 기본적으로 이 필드를 생략하면 요청에서 표준 계층을 사용합니다.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Flex 추론 작동 방식

[Gemini Flex 추론은 표준 API와 Batch API의 24시간
처리 시간 간의 격차를 해소합니다.](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 비수기 '삭제 가능한' 컴퓨팅 용량을 활용하여 백그라운드 작업 및 순차적 워크로드에 비용 효율적인 솔루션을 제공합니다.

| 기능 | Flex | 우선순위 | 표준 | 일괄 |
| --- | --- | --- | --- | --- |
| **가격 책정** | 50% 할인 | 표준보다 75~100% 더 높음 | 정상가 | 50% 할인 |
| **지연 시간** | 분 (1~15분 목표) | 짧음 (초) | 초에서 분 | 최대 24시간 |
| **안정성** | 최선형 (삭제 가능) | 높음 (삭제 불가) | 높음/보통/높음 | 높음 (처리량) |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 |

### 주요 이점

- **비용 효율성**: 프로덕션 이외 평가, 백그라운드 에이전트, 데이터 보강에 상당한 비용 절감 효과가 있습니다.
- **낮은 마찰**: 기존 요청에 단일 매개변수를 추가하기만 하면 됩니다.
- **동기식 워크로드**: 다음 요청이 이전 요청의 출력에 종속되는 순차적 API 체인에 적합하며, 에이전트 워크로드에 일괄보다 더 유연합니다.

### 사용 사례

- **오프라인 평가**: 'LLM-as-a-judge' 회귀 테스트 또는 리더보드 실행
- **백그라운드 에이전트**: 지연 시간이 허용되는 CRM 업데이트, 프로필 작성, 콘텐츠 조정과 같은 순차적 작업
- **예산 제약이 있는 연구**: 제한된 예산으로 많은 토큰이 필요한 학술 실험

### 비율 제한

[Flex 추론 트래픽은 일반 [비율 제한](https://aistudio.google.com/rate-limit?hl=ko)에 포함되며
Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)와 같은 확장된 비율 제한을 제공하지 않습니다.

### 삭제 가능한 용량

Flex 트래픽은 우선순위가 낮게 처리됩니다. 표준 트래픽이 급증하면 우선순위가 높은 사용자의 용량을 확보하기 위해 Flex 요청이 선점되거나 삭제될 수 있습니다. 우선순위가 높은 추론을 찾고 있다면
[우선순위 추론](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ko)을 확인하세요.

### 오류 코드

Flex 용량을 사용할 수 없거나 시스템이 정체된 경우 API는 표준 오류 코드를 반환합니다.

- **503 서비스를 사용할 수 없음**: 시스템이 현재 용량에 도달했습니다.
- **429 요청한 횟수가 너무 많음**: 비율 제한 또는 리소스 소진

### 클라이언트 책임

- **서버 측 대체 없음**: 예기치 않은 요금이 청구되지 않도록 Flex 용량이 가득 찬 경우 시스템에서 Flex 요청을 표준 계층으로 자동 업그레이드하지 않습니다.
- **재시도**: 지수 백오프를 사용하여 자체 클라이언트 측 재시도 로직을 구현해야 합니다.
- **제한 시간**: Flex 요청이 대기열에 있을 수 있으므로 조기에 연결이 종료되지 않도록 클라이언트 측 제한 시간을 10분 이상으로 늘리는 것이 좋습니다.

## 제한 시간 창 조정

REST API 및 클라이언트 라이브러리에 요청별 제한 시간을 구성할 수 있습니다.
클라이언트 측 제한 시간이 의도한 서버 대기 시간 창 (예: Flex 대기열의 경우 600초 이상)을 항상 포함하도록 하세요. SDK는 제한 시간 값을 밀리초 단위로 예상합니다.

### 요청별 제한 시간

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## 재시도 구현

Flex는 삭제 가능하고 503 오류로 인해 실패하므로 실패한 요청을 계속하기 위해 재시도 로직을 선택적으로 구현하는 예는 다음과 같습니다.

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## 가격 책정

Flex 추론은 [표준 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)의 50% 로 가격이 책정되며
토큰당 청구됩니다.

## 지원되는 모델

다음 모델은 Flex 추론을 지원합니다.

| 모델 | Flex 추론 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 다음 단계

- [매우 짧은 지연 시간을 위한](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ko) 우선순위 추론
- [토큰](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ko): 토큰 이해하기

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-19(UTC)"],[],[]]
