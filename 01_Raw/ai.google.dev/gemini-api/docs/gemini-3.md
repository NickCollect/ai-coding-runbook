---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ko
fetched_at: 2026-11-02T07:27:30.352352+00:00
title: "Gemini 3 \uac1c\ubc1c\uc790 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon을 지금 이용 가능합니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)

의견 보내기

# Gemini 3 개발자 가이드

Gemini 3는 현존 최고 수준(SOTA)의 추론을 기반으로 구축된, 현재까지 가장 지능적인 모델 제품군입니다. 이 모델은 Agentic Workflows, 자율 코딩, 복잡한 멀티모달 작업을 정교하게 처리하여 어떠한 아이디어든 실현할 수 있도록 설계되었습니다.
이 가이드에서는 Gemini 3 모델 제품군의 주요 기능과 이를 최대한 활용하는 방법을 설명합니다.

[Gemini 3 앱 컬렉션](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ko)을 살펴보고 모델이 고급 추론, 자율 코딩, 복잡한 멀티모달 작업을 처리하는 방법을 확인하세요.

다음과 같이 몇 줄의 코드로 시작하세요.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(
            InteractionsInput.of(
                "Find the race condition in this multi-threaded C++ snippet: [code here]"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Find the race condition in this multi-threaded C++ snippet: [code here]"),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Gemini 3 시리즈 소개

Gemini 3.1 Pro는 다양한 모달리티에 걸쳐 광범위한 세계 지식과 고급 추론이 필요한 복잡한 작업에 가장 적합합니다.

Gemini 3 Flash는 최신 3시리즈 모델로, Flash의 속도와 가격으로 Pro 수준의 인텔리전스를 제공합니다.

Nano Banana Pro (Gemini 3 Pro Image라고도 함)는 Google의 최고 품질 이미지 생성 모델이며, Nano Banana 2 (Gemini 3.1 Flash Image라고도 함)는 대량, 고효율, 저가형 모델입니다.

Gemini 3.1 Flash-Lite는 비용 효율적인 모델과 대량 작업을 위해 빌드된 워크호스 모델입니다.

모든 Gemini 3 모델은 현재 프리뷰 버전으로 제공됩니다.

| 모델 ID | 컨텍스트 윈도우 (In / Out) | 지식 단절 | 가격 책정 (입력 / 출력)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | 2025년 1월 | $0.25 (텍스트, 이미지, 동영상), $0.50 (오디오) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | 2025년 1월 | $0.25 (텍스트 입력) / $0.067 (이미지 출력)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | 2025년 1월 | 2달러 / 12달러 (<200,000개 토큰)   4달러 / 18달러 (>200,000개 토큰) |
| **gemini-3-flash-preview** | 1M / 64k | 2025년 1월 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025년 1월 | $2 (텍스트 입력) / $0.134 (이미지 출력)\*\* |

*\* 가격은 별도로 명시되지 않는 한 토큰 100만 개당 가격입니다.*
*\*\* 이미지 가격은 해상도에 따라 다릅니다. 자세한 내용은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.*

자세한 한도, 가격 책정, 추가 정보는 [모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)를 참고하세요.

## Gemini 3의 새로운 API 기능

Gemini 3는 개발자가 지연 시간, 비용, 멀티모달 충실도를 더 효과적으로 제어할 수 있도록 설계된 새로운 파라미터를 도입합니다.

### 사고 수준

Gemini 3 시리즈 모델은 기본적으로 동적 사고를 사용하여 프롬프트를 통해 추론합니다. 대답을 생성하기 전에 모델의 내부 추론 프로세스의 **최대** 깊이를 제어하는 `thinking_level` 매개변수를 사용할 수 있습니다. Gemini 3는 이러한 수준을 엄격한 토큰 보장이 아닌 사고를 위한 상대적 허용치로 취급합니다.

`thinking_level`이 지정되지 않으면 Gemini 3의 기본값은 `high`입니다. 복잡한 추론이 필요하지 않은 경우 더 빠르고 지연 시간이 짧은 대답을 위해 모델의 사고 수준을 `low`로 제한할 수 있습니다.

| 사고 수준 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 설명 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 지원되지 않음 | 지원됨 (기본값) | 지원됨 | 대부분의 질문에 대해 '생각하지 않음' 설정과 일치합니다. 모델이 복잡한 코딩 작업에 대해 매우 최소한으로 생각할 수 있습니다. 채팅 또는 높은 처리량 애플리케이션의 지연 시간을 최소화합니다. `minimal`는 생각 끄기를 보장하지 않습니다. |
| **`low`** | 지원됨 | 지원됨 | 지원됨 | 지연 시간과 비용을 최소화합니다. 간단한 지시 수행, 채팅 또는 고처리량 애플리케이션에 가장 적합합니다. |
| **`medium`** | 지원됨 | 지원됨 | 지원됨 | 대부분의 작업에 균형 잡힌 사고를 제공합니다. |
| **`high`** | 지원됨 (기본값, 동적) | 지원됨 (동적) | 지원됨 (기본값, 동적) | 추론 깊이를 극대화합니다. 모델이 첫 번째 (사고가 아닌) 출력 토큰에 도달하는 데 시간이 훨씬 더 오래 걸릴 수 있지만, 출력은 더 신중하게 추론됩니다. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("How does AI work?"))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.LOW)
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("How does AI work?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### 온도

모든 Gemini 3 모델의 경우 온도 파라미터를 기본값인 `1.0`으로 유지할 것을 적극 권장합니다.

이전 모델에서는 창의성과 결정성 간 균형을 위해 온도 조정이 도움이 되었지만, Gemini 3의 추론 기능은 기본 설정에 최적화되어 있습니다. 온도를 변경하여 (1.0 미만으로 설정) 복잡한 수학적 또는 추론 작업에서 루핑이나 성능 저하와 같은 예기치 않은 동작이 발생할 수 있습니다.

### 생각 서명

Gemini 3 모델은 생각 서명을 사용하여 API 호출 전반에서 추론 컨텍스트를 유지합니다. 이러한 서명은 모델의 내부 사고 과정을 암호화한 표현입니다.

- **상태 저장 모드 (권장)**: 상태 저장 모드 (`previous_interaction_id` 제공)에서 Interactions API를 사용하면 서버에서 대화 기록과 생각 서명을 자동으로 관리합니다.
- **상태 비저장 모드**: 대화 기록을 수동으로 관리하는 경우 진위성을 검증하기 위해 후속 요청에 서명이 포함된 사고 블록을 포함해야 합니다.

자세한 내용은 [생각 서명](https://ai.google.dev/gemini-api/docs/thinking?hl=ko) 페이지를 참고하세요.`

### 도구를 사용한 구조화된 출력

Gemini 3 모델을 사용하면 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)을 [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko), [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)과 같은 기본 제공 도구와 결합할 수 있습니다.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("winner", Map.of("type", "string", "description", "The name of the winner."));
properties.put(
    "final_match_score", Map.of("type", "string", "description", "The final match score."));
properties.put(
    "scorers",
    Map.of(
        "type", "array",
        "items", Map.of("type", "string"),
        "description", "The name of the scorer."));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "string"},
                "description": "The name of the scorer.",
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
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

Gemini 3.1 Flash Image 및 Gemini 3 Pro Image를 사용하면 텍스트 프롬프트에서 이미지를 생성하고 수정할 수 있습니다. 추론을 사용하여 프롬프트를 '생각'하고 [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 그라운딩을 사용하기 전에 날씨 예보나 주식 차트와 같은 실시간 데이터를 가져와 고화질 이미지를 생성할 수 있습니다.

**새로운 기능 및 개선된 기능:**

- **4K 및 텍스트 렌더링:** 최대 2K 및 4K 해상도로 선명하고 읽기 쉬운 텍스트와 다이어그램을 생성합니다.
- **그라운딩된 생성:** `google_search` 도구를 사용하여 사실을 확인하고 실제 정보를 기반으로 이미지를 생성합니다. Gemini 3.1 Flash Image에서 Google *이미지* 검색을 사용한 그라운딩을 사용할 수 있습니다.
- **대화형 편집:** 변경사항을 요청하기만 하면 멀티턴 이미지 편집이 가능합니다 (예: '배경을 일몰로 바꿔줘'). 이 워크플로는 **생각 서명**을 사용하여 턴 간에 시각적 컨텍스트를 유지합니다.

가로세로 비율, 편집 워크플로, 구성 옵션에 관한 자세한 내용은 [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)를 참고하세요.

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageResponseFormat;
import com.google.genai.gaos.models.interactions.ImageResponseFormatAspectRatio;
import com.google.genai.gaos.models.interactions.ImageResponseFormatImageSize;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Optional;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-pro-image-preview"))
        .input(InteractionsInput.of("Generate an infographic of the current weather in Tokyo."))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    ImageResponseFormat.builder()
                        .aspectRatio(ImageResponseFormatAspectRatio.ONE_HUNDRED_AND_SIXTY_NINE)
                        .imageSize(ImageResponseFormatImageSize.FOUR_K)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

Optional<ImageContent> generatedImage = interaction.outputImage();
if (generatedImage.isPresent() && generatedImage.get().data().isPresent()) {
  byte[] imageBytes = Base64.getDecoder().decode(generatedImage.get().data().get());
  Files.write(Paths.get("weather_tokyo.png"), imageBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

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
            Model: interactions.Model("gemini-3-pro-image-preview"),
            Input: interactions.NewInteractionsInput("Generate an infographic of the current weather in Tokyo."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.ImageResponseFormat{
                    AspectRatio: interactions.ImageResponseFormatAspectRatioOneHundredAndSixtyNine.ToPointer(),
                    ImageSize:   interactions.ImageResponseFormatImageSize("4K").ToPointer(),
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if generatedImage := res.Interaction.GetOutputImage(); generatedImage != nil && generatedImage.Data != nil {
        imageBytes, err := base64.StdEncoding.DecodeString(*generatedImage.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("weather_tokyo.png", imageBytes, 0644); err != nil {
            log.Fatal(err)
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
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**응답 예시**

![날씨 도쿄](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ko)

### 이미지를 사용한 코드 실행

Gemini 3 Flash는 시각을 정적인 시선이 아닌 적극적인 조사로 취급할 수 있습니다. 추론과 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 결합하여 모델은 계획을 수립한 다음 Python 코드를 작성하고 실행하여 이미지를 단계별로 확대, 자르기, 주석 추가 또는 조작하여 대답을 시각적으로 뒷받침합니다.

**사용 사례:**

- **확대 및 검사:** 모델은 세부정보가 너무 작을 때 (예: 멀리 있는 게이지 또는 일련번호를 읽는 경우) 이를 암시적으로 감지하고 더 높은 해상도로 영역을 잘라 다시 검사하는 코드를 작성합니다.
- **시각적 수학 및 플로팅:** 모델은 코드를 사용하여 다단계 계산을 실행할 수 있습니다 (예: 영수증의 항목 합산 또는 추출된 데이터에서 Matplotlib 차트 생성).
- **이미지 주석:** 모델이 이미지에 직접 화살표, 경계 상자 또는 기타 주석을 그려 '이 항목은 어디에 있어야 하나요?'와 같은 공간 관련 질문에 답변할 수 있습니다.

시각적 사고를 사용 설정하려면 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 도구로 구성하세요. 모델은 필요할 때 코드를 사용하여 이미지를 조작합니다.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

URL url = new URL("https://goo.gle/instrument-img");
byte[] imageBytes;
try (InputStream is = url.openStream()) {
  imageBytes = is.readAllBytes();
}
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder()
                        .text("Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println("Text: " + ((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().flatMap(args -> args.code()).ifPresent(code -> System.out.println("Code: " + code));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println("Output: " + resultStep.result().orElse(""));
  }
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    httpRes, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer httpRes.Body.Close()
    imageBytes, err := io.ReadAll(httpRes.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Zoom into the expression pedals and tell me how many pedals are there?",
                }),
            }),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Text:", textContent.Text)
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if callStep.Arguments.Code != nil {
                fmt.Println("Code:", *callStep.Arguments.Code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println("Output:", resultStep.Result)
        }
    }
}
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

이미지를 사용한 코드 실행에 관한 자세한 내용은 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko#images)을 참고하세요.

### 멀티모달 함수 응답

[멀티모달 함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#multimodal)을 사용하면 사용자 함수 응답에 멀티모달 객체를 포함할 수 있어 모델의 함수 호출 기능을 더욱 효과적으로 활용할 수 있습니다. 표준 함수 호출은 텍스트 기반 함수 응답만 지원합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.FunctionResultSubcontent;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> itemProp = new HashMap<>();
itemProp.put("type", "string");
itemProp.put("description", "The name or description of the item ordered (e.g., 'instrument').");

Map<String, Object> properties = new HashMap<>();
properties.put("item_name", itemProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("item_name"));

Function getImageTool =
    Function.builder()
        .name("get_image")
        .description("Retrieves the image file reference for a specific order item.")
        .parameters(parameters)
        .build();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "Use the get_image tool to show me the instrument I ordered last month."))
        .tools(Arrays.asList(getImageTool))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction1.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  System.out.println("Tool Call: " + fcStep.name().orElse(""));

  URL url = new URL("https://goo.gle/instrument-img");
  byte[] imageBytes;
  try (InputStream is = url.openStream()) {
    imageBytes = is.readAllBytes();
  }
  String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

  List<FunctionResultSubcontent> subcontents = new ArrayList<>();
  subcontents.add(TextContent.builder().text("instrument.jpg").build());
  subcontents.add(
      ImageContent.builder()
          .mimeType(ImageContentMimeType.IMAGE_JPEG)
          .data(base64ImageData)
          .build());

  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(FunctionResultStepResultUnion.of(subcontents))
          .build();

  CreateModelInteraction req2 =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(getImageTool))
          .previousInteractionId(interaction1.id().orElse(""))
          .build();

  Interaction interaction2 =
      client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
  System.out.println("Final model response: " + interaction2.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    getImageTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_image"),
        Description: genai.Ptr("Retrieves the image file reference for a specific order item."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "item_name": map[string]any{
                    "type":        "string",
                    "description": "The name or description of the item ordered (e.g., 'instrument').",
                },
            },
            "required": []string{"item_name"},
        },
    })

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("Use the get_image tool to show me the instrument I ordered last month."),
            Tools: []interactions.Tool{getImageTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res1.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Println("Tool Call:", fcStep.Name)

            httpRes, err := http.Get("https://goo.gle/instrument-img")
            if err != nil {
                log.Fatal(err)
            }
            defer httpRes.Body.Close()
            imageBytes, err := io.ReadAll(httpRes.Body)
            if err != nil {
                log.Fatal(err)
            }
            base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{
                        Text: "instrument.jpg",
                    }),
                    interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                        MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                        Data:     genai.Ptr(base64ImageData),
                    }),
                }),
            })

            res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res1.Interaction.ID,
                    Tools:                 []interactions.Tool{getImageTool},
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if res2.Interaction.OutputText != nil {
                fmt.Println("Final model response:", *res2.Interaction.OutputText)
            }
            break
        }
    }
}
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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### 기본 제공 도구와 함수 호출 결합

Gemini 3에서는 동일한 API 호출에서 기본 제공 도구 (예: Google 검색, URL 컨텍스트, [기타](https://ai.google.dev/gemini-api/docs/tools?hl=ko))와 맞춤 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) 도구를 사용할 수 있어 더 복잡한 워크플로가 가능합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> cityProp = new HashMap<>();
cityProp.put("type", "string");
cityProp.put("description", "The city and state, e.g. Utqiaġvik, Alaska");

Map<String, Object> properties = new HashMap<>();
properties.put("city", cityProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("city"));

Function getWeather =
    Function.builder()
        .name("getWeather")
        .description("Gets the weather for a requested city.")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "What is the northernmost city in the United States? What's the weather like there today?"))
        .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(
              FunctionResultStepResultUnion.of(
                  "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"))
          .build();

  CreateModelInteraction finalRequest =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
          .previousInteractionId(interaction.id().orElse(""))
          .build();

  Interaction finalInteraction =
      client.interactions.create(CreateInteractionRequestBody.of(finalRequest)).interaction().get();
  System.out.println(finalInteraction.outputText().orElse(""));
}
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

    getWeather := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("getWeather"),
        Description: genai.Ptr("Gets the weather for a requested city."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "city": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. Utqiaġvik, Alaska",
                },
            },
            "required": []string{"city"},
        },
    })

    tools := []interactions.Tool{
        interactions.NewTool(interactions.GoogleSearch{}),
        getWeather,
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("What is the northernmost city in the United States? What's the weather like there today?"),
            Tools: tools,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"response": "Very cold. 22 degrees Fahrenheit."}`),
            })

            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res.Interaction.ID,
                    Tools:                 tools,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
            break
        }
    }
}
```

## Gemini 2.5에서 마이그레이션

Gemini 3는 현재까지 가장 강력한 모델 제품군이며 Gemini 2.5에 비해 단계적으로 개선되었습니다. 마이그레이션할 때는 다음 사항을 고려하세요.

- **사고:** 이전에 복잡한 프롬프트 엔지니어링 (예: 사고의 연쇄)을 사용하여 Gemini 2.5가 추론하도록 강제한 경우 `thinking_level: "high"` 및 단순화된 프롬프트로 Gemini 3를 사용해 보세요.
- **온도 설정:** 기존 코드에서 온도를 명시적으로 설정하고 있다면(특히 결정적 출력을 위해 낮은 값으로 설정한 경우), 해당 파라미터를 삭제하고 Gemini 3의 기본값인 1.0을 사용하는 것이 좋습니다. 이는 복잡한 작업에서 잠재적인 루핑 문제나 성능 저하를 방지하는 위함입니다.
- **PDF 및 문서 이해:**
  밀도 높은 문서 파싱을 위해 특정 동작에 의존하고 있었다면, 정확도를 유지하기 위해 새로운 `media_resolution_high` 설정을 테스트해 보세요.
- **토큰 소비량:** Gemini 3 기본값으로 마이그레이션하면 PDF의 토큰 사용량은 **증가**할 수 있지만 동영상의 토큰 사용량은 **감소**할 수 있습니다. 기본 해상도 상승으로 인해 요청이 컨텍스트 윈도우를 초과한다면 미디어 해상도를 명시적으로 낮추는 것이 좋습니다.
- **이미지 분할:** Gemini 3 Pro 또는 Gemini 3 Flash에서는 이미지 분할 기능 (객체의 픽셀 수준 마스크 반환)이 지원되지 않습니다. 기본 제공되는 이미지 분할 기능이 필요한 워크로드의 경우, 사고를 끈 상태의 Gemini 2.5 Flash를 계속 사용하는 것이 좋습니다.
- **컴퓨터 사용:** Gemini 3 Pro 및 Gemini 3 Flash는 [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)을 지원합니다. 2.5 시리즈와 달리 Computer Use 도구에 액세스하기 위해 별도의 모델을 사용할 필요가 없습니다.
- **도구 지원**: 이제 Gemini 3 모델에서 [내장 도구와 함수 호출을 결합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)할 수 있습니다. 이제 Gemini 3 모델에서도 [지도 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)이 지원됩니다.

## OpenAI 호환성

[OpenAI 호환성 레이어](https://ai.google.dev/gemini-api/docs/openai?hl=ko)를 사용하는 경우 표준 파라미터 (OpenAI의 `reasoning_effort`)는 Gemini (`thinking_level`)에 상응하는 파라미터로 자동 매핑됩니다.

## 프롬프트 권장사항

Gemini 3는 추론 모델이므로 프롬프트 작성 방식에도 변화가 필요합니다.

- **정확한 지시:** 입력 프롬프트는 간결하게 작성하세요. Gemini 3는 직접적이고 명확한 지시에 가장 잘 반응합니다. 이전 모델에서 사용되던 장황하거나 지나치게 복잡한 프롬프트 엔지니어링 기법은 과분석을 유발할 수 있습니다.
- **출력 장황도:** 기본적으로 Gemini 3는 덜 장황하며, 직접적이고 효율적인 답변을 제공하는 것을 선호합니다. 보다 대화형이거나 "수다스러운" 스타일의 응답이 필요하다면, 프롬프트에서 명시적으로 모델을 유도해야 합니다 (예: "친근하고 말이 많은 조수처럼 설명해 주세요").
- **컨텍스트 관리:** 대규모 데이터 세트 (예: 전체 책, 코드베이스 또는 긴 동영상)로 작업할 때는 데이터 컨텍스트 뒤에 프롬프트 끝에 특정 요청 사항이나 질문을 배치합니다. '앞의 정보를 바탕으로…'와 같은 문구로 질문을 시작하여 제공된 데이터에 모델의 추론을 고정합니다.

[프롬프트 엔지니어링 가이드](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko)에서 프롬프트 설계 전략에 대해 자세히 알아보세요.

## FAQ

1. **Gemini 3의 지식 단절 시점은 언제인가요?** Gemini 3 모델의 지식 단절 시점은 2025년 1월입니다. 최신 정보를 확인하려면 [그라운딩 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 도구를 사용하세요.
2. **컨텍스트 윈도우 한도는 어떻게 되나요?** Gemini 3 모델은 최대 100만 토큰의 입력 컨텍스트 윈도우와 최대 64,000의 토큰 출력을 지원합니다.
3. **Gemini 3에 무료 등급이 있나요?** Gemini 3 Flash`gemini-3-flash-preview`에는 Gemini API의 무료 등급이 있습니다. Google AI Studio에서는 Gemini 3.1 Pro 및 3 Flash를 무료로 사용해 볼 수 있지만 Gemini API에서는 `gemini-3.1-pro-preview`에 사용할 수 있는 무료 등급이 없습니다.
4. **이전 `thinking_budget` 코드가 계속 작동하나요?** 예, 이전 버전과의 호환성을 위해 `thinking_budget`가 계속 지원되지만 더 예측 가능한 성능을 위해 `thinking_level`로 이전하는 것이 좋습니다. 동일한 요청에서 두 가지를 모두 사용하지 마세요.
5. **Gemini 3는 Batch API를 지원하나요?** 예, Gemini 3는 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)를 지원합니다.
6. **컨텍스트 캐싱이 지원되나요?** 예, Gemini 3에서는 [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)이 지원됩니다.
7. **Gemini 3에서 지원되는 도구는 무엇인가요?** Gemini 3는 [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko), [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko), [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)를 지원합니다. 또한 자체 맞춤 도구와 [기본 제공 도구와의 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)을 위한 표준 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)도 지원합니다.
8. **`gemini-3.1-pro-preview-customtools`란 무엇인가요?** `gemini-3.1-pro-preview`를 사용하고 모델이 bash 명령어를 선호하여 맞춤 도구를 무시하는 경우 `gemini-3.1-pro-preview-customtools` 모델을 대신 사용해 보세요.
   자세한 내용은 [여기][customtools-model]를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-09(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-09(UTC)"],[],[]]
