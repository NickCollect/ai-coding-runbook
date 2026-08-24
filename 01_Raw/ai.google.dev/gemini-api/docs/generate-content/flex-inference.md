---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=ko
fetched_at: 2026-08-24T02:34:53.001022+00:00
title: "\ud50c\ub809\uc2a4 \ucd94\ub860 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 플렉스 추론

설명: Flex 추론 등급으로 비용을 최적화하는 방법을 알아봅니다.

Gemini Flex API는 가변 지연 시간과 최선형 가용성을 제공하는 대신 표준 요금보다 50% 저렴한 추론 등급입니다. 동기식 처리가 필요하지만 표준 API의 실시간 성능은 필요하지 않은 지연 시간 허용 워크로드용으로 설계되었습니다.

## Flex 사용 방법

Flex 등급을 사용하려면 요청 본문에서 `service_tier`를 `flex`로 지정합니다. 기본적으로 이 필드를 생략하면 요청에서 표준 등급을 사용합니다.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.6-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Flex 추론 작동 방식

[Gemini Flex 추론은 표준 API와 Batch API의 24시간
처리 시간 간의 격차를 해소합니다.](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 비수기 '삭제 가능한' 컴퓨팅 용량을 활용하여 백그라운드 작업 및 순차적 워크플로를 위한 비용 효율적인 솔루션을 제공합니다.

| 기능 | Flex | 우선순위 | 표준 | 일괄 |
| --- | --- | --- | --- | --- |
| **가격 책정** | 50% 할인 | 표준보다 75~100% 더 높음 | 정상가 | 50% 할인 |
| **지연 시간** | 분 (1~15분 목표) | 낮음 (초) | 수 초에서 수 분 | 최대 24시간 |
| **안정성** | 최선형 (삭제 가능) | 높음 (삭제 불가) | 높음/보통/높음 | 높음 (처리량) |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 |

### 주요 이점

- **비용 효율성**: 비프로덕션 평가, 백그라운드 에이전트, 데이터 보강에 상당한 비용 절감 효과가 있습니다.
- **낮은 마찰**: 일괄 객체, 작업 ID, 폴링을 관리할 필요가 없습니다. 기존 요청에 단일 매개변수를 추가하기만 하면 됩니다.
- **동기식 워크플로**: 다음 요청이 이전 요청의 출력에 종속되는 순차적 API 체인에 적합하므로 에이전트 워크플로에 일괄 처리보다 더 유연합니다.

### 사용 사례

- **오프라인 평가**: 'LLM-as-a-judge' 회귀 테스트 또는 리더보드 실행
- **백그라운드 에이전트**: 지연 시간이 허용되는 CRM 업데이트, 프로필 작성, 콘텐츠 조정과 같은 순차적 작업
- **예산 제약이 있는 연구**: 제한된 예산으로 많은 토큰이 필요한 학술 실험

### 비율 제한

[Flex 추론 트래픽은 일반 [비율 제한](https://aistudio.google.com/rate-limit?hl=ko)에 포함되며
Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)와 같은 확장된 비율 제한을 제공하지 않습니다.

### 삭제 가능한 용량

Flex 트래픽은 우선순위가 낮게 처리됩니다. 표준 트래픽이 급증하면 우선순위가 높은 사용자의 용량을 확보하기 위해 Flex 요청이 선점되거나 삭제될 수 있습니다. 우선순위가 높은 추론을 찾고 있다면
[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)을 확인하세요.

### 오류 코드

Flex 용량을 사용할 수 없거나 시스템이 정체된 경우 API는 표준 오류 코드를 반환합니다.

- **503 서비스를 사용할 수 없음**: 현재 시스템이 사용 한도에 도달했습니다.
- **429 너무 많은 요청**: 비율 제한 또는 리소스 소진

### 클라이언트 책임

- **서버 측 대체 없음**: 예기치 않은 요금이 청구되지 않도록 Flex 용량이
  가득 차면 시스템에서 Flex 요청을 표준 등급으로
  자동 업그레이드하지 않습니다.
- **재시도**: 지수 백오프를 사용하여 자체 클라이언트 측 재시도 로직을 구현해야 합니다.
- **제한 시간**: Flex 요청이 대기열에 있을 수 있으므로 연결이 조기에 종료되지 않도록 클라이언트 측 제한 시간을 10분 이상으로 늘리는 것이 좋습니다.

## 제한 시간 창 조정

REST API 및 클라이언트 라이브러리에 요청별 제한 시간을 구성할 수 있으며 클라이언트 라이브러리를 사용하는 경우에만 전역 제한 시간을 구성할 수 있습니다.

클라이언트 측 제한 시간이 의도한 서버 대기 창 (예: Flex 대기열의 경우 600초 이상)을 포함하는지 항상 확인하세요. SDK는 제한 시간 값을 밀리초 단위로 예상합니다.

### 요청별 제한 시간

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.6-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.6-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.6-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.6-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.6-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

REST 호출을 할 때 HTTP 헤더와 `curl` 옵션을 조합하여 제한 시간을 제어할 수 있습니다.

- **`X-Server-Timeout` 헤더 (서버 측 제한 시간)**: 이 헤더는 Gemini API 서버에 선호하는 제한 시간 (기본값 600초)을 제안합니다. 서버는 이를 준수하려고 시도하지만 보장되지는 않습니다. 값은 초 단위여야 합니다.
- **`--max-time`의 `curl`(클라이언트 측 제한 시간)**: `curl --max-time
  <seconds>` 옵션은 전체 작업이 완료될 때까지 `curl`
  이(가) 대기하는 총 시간(초)에 대한 엄격한 한도를 설정합니다. 이는 클라이언트 측 보호 조치입니다.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### 전역 제한 시간

특정 `genai.Client` 인스턴스(클라이언트 라이브러리만 해당)를 통해 이루어진 모든 API 호출에 기본 제한 시간을 적용하려면 `http_options` 및 `genai.types.HttpOptions`를 사용하여 클라이언트를 초기화할 때 이를 구성할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.6-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
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
            return client.models.generate_content(
                model="gemini-3.6-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.6-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.6-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.6-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## 가격 책정

Flex 추론은 [표준 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)의 50% 로 가격이 책정되며
토큰당 청구됩니다.

## 지원되는 모델

다음 모델은 Flex 추론을 지원합니다.

| 모델 | Flex 추론 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 3 Pro Image 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 다음 단계

Gemini의 다른 [추론 및 최적화](https://ai.google.dev/gemini-api/docs/optimization?hl=ko) 옵션에 대해 알아보세요.

- [매우 짧은 지연 시간을 위한](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko) 우선순위 추론
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 24시간 이내 비동기 처리를 위한
- [입력 토큰 비용 절감을 위한 컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
