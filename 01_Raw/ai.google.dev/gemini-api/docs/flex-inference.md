---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko
fetched_at: 2026-10-12T06:58:27.721505+00:00
title: "\ud50c\ub809\uc2a4 \ucd94\ub860 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 플렉스 추론

Gemini Flex API는 가변 지연 시간과 최선을 다하는 가용성을 제공하는 대신 표준 요금에 비해 비용이 50% 절감되는 추론 등급입니다. 동기식 처리가 필요하지만 표준 API의 실시간 성능은 필요하지 않은 지연 시간 허용 워크로드용으로 설계되었습니다.

## Flex 사용 방법

Flex 등급을 사용하려면 요청에서 `service_tier`을 `flex`로 지정합니다. 이 필드를 생략하면 요청에서 기본적으로 표준 등급을 사용합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Flex 추론 작동 방식

Gemini Flex 추론은 표준 API와 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)의 24시간 처리 시간 간의 격차를 해소합니다. 피크가 아닌 '제어 가능한' 컴퓨팅 용량을 활용하여 백그라운드 작업과 순차적 워크플로를 위한 비용 효율적인 솔루션을 제공합니다.

| 기능 | Flex | 우선순위 | 표준 | 일괄 |
| --- | --- | --- | --- | --- |
| **가격 책정** | 50% 할인 | Standard보다 75~100% 더 많음 | 정상가 | 50% 할인 |
| **지연 시간** | 분 (목표 1~15분) | 낮음 (초) | 수 초에서 수 분 | 최대 24시간 |
| **안정성** | 최대한 노력 (삭제 가능) | 높음 (제거 불가) | 높음 / 중간~높음 | 높음 (처리량) |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 |

### 주요 이점

- **비용 효율성**: 비프로덕션 평가, 백그라운드 에이전트, 데이터 보강에 상당한 절감 효과가 있습니다.
- **마찰 감소**: 기존 요청에 매개변수 하나만 추가하면 됩니다.
- **동기 Workflows**: 다음 요청이 이전 요청의 출력에 종속되는 순차적 API 체인에 적합하며, Agentic Workflows의 경우 Batch보다 유연합니다.

### 사용 사례

- **오프라인 평가**: 'LLM-as-a-judge' 회귀 테스트 또는 리더보드를 실행합니다.
- **백그라운드 에이전트**: CRM 업데이트, 프로필 작성, 콘텐츠 검토와 같이 지연이 허용되는 순차적 작업
- **예산 제약이 있는 연구**: 제한된 예산으로 많은 토큰이 필요한 학술 실험

### 비율 제한

유연한 추론 트래픽은 일반 [비율 제한](https://aistudio.google.com/rate-limit?hl=ko)에 반영되며 [일괄 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)와 같은 확장된 비율 제한은 제공하지 않습니다.

### 절전 가능한 용량

Flex 트래픽은 우선순위가 낮게 처리됩니다. 표준 트래픽이 급증하면 우선순위가 높은 사용자의 용량을 확보하기 위해 Flex 요청이 선점되거나 삭제될 수 있습니다. 우선순위가 높은 추론을 찾고 있다면 [우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)을 확인하세요.

### 오류 코드

Flex 용량을 사용할 수 없거나 시스템이 혼잡한 경우 API는 표준 오류 코드를 반환합니다.

- **503 서비스를 사용할 수 없음**: 현재 시스템이 사용 한도에 도달했습니다.
- **429 너무 많은 요청**: 비율 제한 또는 리소스 소진입니다.

### 고객 책임

- **서버 측 대체 없음**: 예상치 못한 요금이 청구되지 않도록 Flex 용량이 가득 차면 시스템에서 Flex 요청을 자동으로 Standard 등급으로 업그레이드하지 않습니다.
- **재시도**: 지수 백오프를 사용하여 자체 클라이언트 측 재시도 로직을 구현해야 합니다.
- **제한 시간**: Flex 요청이 대기열에 있을 수 있으므로 조기 연결 종료를 방지하려면 클라이언트 측 제한 시간을 10분 이상으로 늘리는 것이 좋습니다.

## 제한 시간 창 조정

REST API 및 클라이언트 라이브러리의 요청별 제한 시간을 구성할 수 있습니다.
클라이언트 측 시간 초과가 의도한 서버 대기 시간 (예: Flex 대기열의 경우 600초 이상)을 포함하는지 항상 확인하세요. SDK는 제한 시간 값을 밀리초 단위로 예상합니다.

### 요청별 제한 시간

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## 재시도 구현

Flex는 삭제 가능하고 503 오류로 실패하므로 실패한 요청을 계속하기 위해 재시도 로직을 선택적으로 구현하는 예는 다음과 같습니다.

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
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
                    model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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
          model: "gemini-3.8-flash",
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

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## 가격 책정

유연한 추론은 [표준 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)의 50% 로 가격이 책정되며 토큰당 청구됩니다.

## 지원되는 모델

다음 모델은 유연한 추론을 지원합니다.

| 모델 | Flex 추론 |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ko) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 다음 단계

- 매우 짧은 지연 시간을 위한 [우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)
- [토큰](https://ai.google.dev/gemini-api/docs/tokens?hl=ko): 토큰을 이해합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-09(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-09(UTC)"],[],[]]
