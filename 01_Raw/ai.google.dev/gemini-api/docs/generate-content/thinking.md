---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ko
fetched_at: 2026-08-03T04:35:23.044948+00:00
title: "Gemini \uc0dd\uac01 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 생각

[Gemini 3 및 2.5 시리즈 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko)은 추론 및 다단계
계획 기능을 크게 개선하는 내부
"사고 과정"을 사용하므로 코딩, 고급 수학, 데이터 분석과 같은 복잡한 작업에 매우 효과적입니다.

이 가이드에서는 Gemini API를 사용하여 Gemini의 사고 기능을 사용하는 방법을 보여줍니다.

## 사고를 통한 콘텐츠 생성

사고 모델로 요청을 시작하는 것은 다른 콘텐츠 생성 요청과 비슷합니다. [주요 차이점은 다음 [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#text-input) 예에서와 같이 `model` 필드에 사고 지원](#supported-models) 모델 중 하나를 지정하는 데 있습니다.

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## 사고 요약

사고 요약은 모델의 원시 사고를 요약한 버전으로, 모델의 내부 추론 과정에 대한 통찰력을 제공합니다. 사고 수준과 예산은 사고 요약이 아닌 모델의 원시 사고에 적용됩니다.

요청 구성에서 `includeThoughts`를 `true`로 설정하여 사고 요약을 사용 설정할 수 있습니다. 그런 다음 `response` 매개변수의 `parts`를 반복하고 `thought` 불리언을 확인하여 요약에 액세스할 수 있습니다.

다음은 스트리밍 없이 사고 요약을 사용 설정하고 검색하는 방법을 보여주는 예입니다. 이 예에서는 대답과 함께 단일 최종 사고 요약을 반환합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

다음은 스트리밍과 함께 사고를 사용하는 예입니다. 이 예에서는 생성 중에 롤링 증분 요약을 반환합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.6-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## 사고 제어

Gemini 모델은 기본적으로 동적 사고를 수행하여 사용자 요청의 복잡성에 따라 추론 노력을 자동으로 조정합니다.
하지만 특정 지연 시간 제약조건이 있거나 모델이 평소보다 더 깊은 추론을 수행해야 하는 경우 매개변수를 사용하여 사고 동작을 제어할 수 있습니다(선택사항).

### 사고 수준 (Gemini 3)

Gemini 3 모델 이상에 권장되는 `thinkingLevel` 매개변수를 사용하면 추론 동작을 제어할 수 있습니다.

다음 표에서는 각 모델 유형의 `thinkingLevel` 설정을 자세히 설명합니다.

| 사고 수준 | Gemini 3.6 및 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 및 3.1 Flash-Lite | Gemini 3.1 Flash-Lite 이미지 | Gemini 3 Flash | 설명 |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | 지원됨 | 지원되지 않음 | 지원됨 (기본값) | 지원됨 (기본값) | 지원됨 | 대부분의 쿼리에 '사고 없음' 설정과 일치합니다. 참고: `minimal`은 사고가 사용 중지되었음을 보장하지 않습니다. 모델은 복잡한 작업에 대해 매우 최소한으로 추론할 수 있습니다. |
| **`low`** | 지원됨 | 지원됨 | 지원됨 | 지원되지 않음 | 지원됨 | 지연 시간과 비용을 최소화합니다. |
| **`medium`** | 지원됨 (기본값) | 지원됨 | 지원됨 | 지원되지 않음 | 지원됨 | 대부분의 작업에 대한 균형 잡힌 사고입니다. |
| **`high`** | 지원됨 (동적) | 지원됨 (기본값, 동적) | 지원됨 (동적) | 지원됨 (동적) | 지원됨 (기본값, 동적) | 추론 깊이를 극대화합니다. 모델이 첫 번째 (사고 없음) 출력 토큰에 도달하기까지 시간이 더 오래 걸릴 수 있지만, 출력은 더 신중하게 추론됩니다. |

다음 예에서는 사고 수준을 설정하는 방법을 보여줍니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Gemini 3.1 Pro에서는 사고를 사용 중지할 수 없습니다. Gemini 3 Flash 및 Flash-Lite
도 전체 사고 사용 중지를 지원하지 않습니다.
사고 수준을 지정하지 않으면 Gemini는 Gemini 3 모델의
기본 사고 수준 (예: `"high"`의 경우 Gemini 3.1 Pro, `"medium"`의 경우 Gemini 3.5 Flash)을 사용합니다.

Gemini 2.5 시리즈 모델은 `thinkingLevel`을 지원하지 않습니다. 대신 `thinkingBudget`을 사용하세요.

### 사고 예산

Gemini 2.5 시리즈와 함께 도입된 `thinkingBudget` 매개변수는 추론에 사용할 특정 사고 토큰 수를 모델에 안내합니다.

다음은 각 모델 유형의 `thinkingBudget` 구성 세부정보입니다.
`thinkingBudget`을 0으로 설정하여 사고를 사용 중지할 수 있습니다.
`thinkingBudget`을 -1로 설정하면
**동적 사고**가 사용 설정됩니다. 즉, 모델이 요청의 복잡성에 따라 예산을 조정합니다.

| 모델 | 기본 설정 (사고 예산이 설정되지 않음) | 범위 | 사고 사용 중지 | 동적 사고 사용 설정 |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | 동적 사고 | `128`~`32768` | 해당 사항 없음: 사고를 사용 중지할 수 없음 | `thinkingBudget = -1` (기본값) |
| **2.5 Flash** | 동적 사고 | `0`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (기본값) |
| **2.5 Flash 프리뷰** | 동적 사고 | `0`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (기본값) |
| **2.5 Flash Lite** | 모델이 생각하지 않음 | `512`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite 프리뷰** | 모델이 생각하지 않음 | `512`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 프리뷰** | 동적 사고 | `0`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (기본값) |
| **2.5 Flash Live 네이티브 오디오 프리뷰 (2025년 9월)** | 동적 사고 | `0`~`24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (기본값) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

프롬프트에 따라 모델이 토큰 예산을 초과하거나 부족할 수 있습니다.

## 생각 서명

Gemini API는 상태 비저장 API이므로 모델은 모든 API 요청을 독립적으로 처리하며 멀티턴 상호작용에서 이전 턴의 사고 컨텍스트에 액세스할 수 없습니다.

멀티턴 상호작용에서 사고 컨텍스트를 유지할 수 있도록 Gemini는 모델의 내부 사고 과정을 암호화한 표현인 생각 서명을 반환합니다.

- **Gemini 2.5 모델**은 사고가 사용 설정되어 있고
  요청에 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#thinking)(특히 [함수 선언](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#step-2))이 포함된 경우 생각 서명을 반환합니다.
- **Gemini 3 모델** 은 모든 유형의 [파트](https://ai.google.dev/api/caching?hl=ko#Part)에 대해 생각 서명을 반환할 수 있습니다.
  수신된 대로 모든 서명을 다시 전달하는 것이 좋지만 함수 호출 서명의 경우 *필수* 입니다. 자세한 내용은
  [생각 서명](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ko) 페이지를
  참고하세요.

함수 호출과 관련하여 고려해야 할 다른 사용 제한사항은 다음과 같습니다.

- 서명은 응답의 다른 부분(예: 함수 호출 또는 텍스트 파트) 내에서 모델로부터 반환됩니다.
  [후속 턴에서 모든 파트가 포함된](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#step-4)
  전체 대답을 모델에 반환합니다.
- 서명이 있는 파트를 함께 연결하지 마세요.
- 서명이 있는 부분을 서명이 없는 부분과 병합하지 마세요.

## 가격 책정

사고가 사용 설정되면 대답 가격은 출력 토큰과 사고 토큰의 합계입니다. `thoughtsTokenCount` 필드에서 생성된 총 사고 토큰 수를 확인할 수 있습니다.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

[사고 모델은 최종 대답의 품질을 개선하기 위해 전체 사고를 생성한 다음 사고 과정에 대한 통찰력을 제공하기 위해 요약을 출력합니다.](#summaries) 따라서 가격은 API에서 요약만 출력되더라도 모델이 요약을 생성하기 위해 생성해야 하는 전체 사고 토큰을 기준으로 합니다.

토큰에 관한 자세한 내용은 [토큰 집계](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)
가이드를 참고하세요.

## 권장사항

이 섹션에는 사고 모델을 효율적으로 사용하는 방법에 관한 몇 가지 안내가 포함되어 있습니다.
항상 그렇듯이 Google의 [프롬프트 작성 안내 및 권장사항](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko)을 따르면 최상의 결과를 얻을 수 있습니다.

### 디버깅 및 스티어링

- **추론 검토**: 사고 모델에서 예상한 대답을 얻지 못하는 경우 Gemini의 사고 요약을 신중하게 분석하는 것이 도움이 될 수 있습니다.
  작업을 세분화하고 결론에 도달한 방법을 확인하고 이 정보를 사용하여 올바른 결과로 수정할 수 있습니다.
- **추론에 안내 제공**: 특히 긴
  출력을 원하는 경우 프롬프트에 안내를 제공하여 모델이 사용하는
  [사고의 양](#set-budget)을 제한할 수 있습니다. 이렇게 하면 대답에 더 많은 토큰 출력을 예약할 수 있습니다.

### 작업 복잡성

- **간단한 작업 (사고 사용 중지 가능):** 사실 검색 또는 분류와 같이 복잡한 추론이 필요하지 않은 간단한 요청의 경우 사고가 필요하지 않습니다. 예를 들면 다음과 같습니다.
  - 'DeepMind는 어디에서 설립되었나요?'
  - '이 이메일은 회의를 요청하는 것인가요, 아니면 정보를 제공하는 것인가요?'
- **중간 작업 (기본값/일부 사고):** 많은 일반적인 요청은 단계별 처리 또는 더 깊은 이해를 통해 이점을 얻을 수 있습니다. Gemini는 다음과 같은 작업에 사고 기능을 유연하게 사용할 수 있습니다.
  - 광합성과 성장을 비유합니다.
  - 전기 자동차와 하이브리드 자동차를 비교 및 대조합니다.
- **어려운 작업 (최대 사고 기능):** 복잡한 수학 문제 해결 또는 코딩 작업과 같은 매우 복잡한 문제의 경우 높은 사고 예산을 설정하는 것이 좋습니다. 이러한 유형의 작업에는 모델이 전체 추론 및 계획 기능을 사용해야 하며, 대답을 제공하기 전에 많은 내부 단계가 포함되는 경우가 많습니다. 예를 들면 다음과 같습니다.
  - AIME 2025에서 문제 1을 해결합니다. 17b가 97b의 약수인 모든 정수 밑 b > 9의 합을 구합니다.
  - 사용자 인증을 포함하여 실시간 주식 시장 데이터를 시각화하는 웹 애플리케이션용 Python 코드를 작성합니다. 가능한 한 효율적으로 만듭니다.

## 지원되는 모델, 도구, 기능

사고 기능은 모든 3 및 2.5 시리즈 모델에서 지원됩니다.
모델 개요 페이지에서 모든 모델 기능을 확인할 수 있습니다.

사고 모델은 Gemini의 모든 도구 및 기능과 호환됩니다. 이를 통해 모델은 외부 시스템과 상호작용하거나, 코드를 실행하거나, 실시간 정보에 액세스하여 결과를 추론 및 최종 대답에 통합할 수 있습니다.

[사고 Cookbook][Colab]에서 사고 모델로 도구를 사용하는 예시를 사용해 볼 수 있습니다.

## 다음 단계

- 사고 범위는 [OpenAI 호환성](https://ai.google.dev/gemini-api/docs/openai?hl=ko#thinking) 가이드에서 확인할 수 있습니다.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
