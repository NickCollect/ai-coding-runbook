---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko
fetched_at: 2026-10-05T06:43:02.155783+00:00
title: "Google \uc9c0\ub3c4\ub97c \uc0ac\uc6a9\ud55c \uadf8\ub77c\uc6b4\ub529 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google 지도를 사용한 그라운딩

Google 지도 기반 그라운딩은 Gemini의 생성 기능을 Google 지도의 풍부하고 사실에 기반한 최신 데이터와 연결합니다. 이 기능을 사용하면 개발자가 위치 인식 기능을 애플리케이션에 쉽게 통합할 수 있습니다. 사용자 쿼리에 지도 데이터와 관련된 컨텍스트가 있는 경우 Gemini 모델은 Google 지도를 활용하여 사용자가 지정한 위치 또는 대략적인 위치와 관련된 사실에 기반한 최신 답변을 제공합니다.

- **정확하고 위치를 인식하는 대답:** 지리적으로 구체적인 질문에 대해 Google 지도의 광범위하고 최신 데이터를 활용합니다.
- **맞춤설정 강화:** 사용자가 제공한 위치를 기반으로 추천 및 정보를 맞춤설정합니다.

## 시작하기

이 예시에서는 Google 지도 기반 그라운딩을 애플리케이션에 통합하여 사용자 질문에 정확하고 위치 인식 응답을 제공하는 방법을 보여줍니다. 프롬프트는 선택적 사용자 위치와 함께 현지 추천을 요청하여 Gemini 모델이 Google 지도 데이터를 사용할 수 있도록 합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What are the best Italian restaurants within a 15-minute walk from here?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and annotations
    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google 지도 기반 그라운딩 작동 방식

Google 지도 기반 그라운딩은 지도 API를 그라운딩 소스로 사용하여 Gemini API를 Google 지리 생태계와 통합합니다. 사용자의 질문에 지리적 맥락이 포함된 경우 Gemini 모델은 Google 지도 기반 그라운딩 도구를 호출할 수 있습니다. 그러면 모델이 제공된 위치와 관련된 Google 지도 데이터를 기반으로 응답을 생성할 수 있습니다.

이 프로세스에는 일반적으로 다음이 포함됩니다.

1. **사용자 쿼리:** 사용자가 애플리케이션에 쿼리를 제출합니다. 여기에는 지리적 컨텍스트 (예: '내 주변 카페', '샌프란시스코 박물관')가 포함될 수 있습니다.
2. **도구 호출:** 지리적 의도를 인식한 Gemini 모델이 Google 지도 기반 그라운딩 도구를 호출합니다. 이 도구에는 사용자의 `latitude` 및 `longitude`이 선택적으로 제공될 수 있습니다. 이 도구는 텍스트 검색 도구이며, 로컬 쿼리 ('내 주변')는 좌표를 사용하는 반면 구체적이거나 비로컬 쿼리는 명시적 위치의 영향을 받지 않을 가능성이 높다는 점에서 지도에서 검색하는 것과 유사하게 작동합니다.
3. **데이터 검색:** Google 지도 기반 그라운딩 서비스는 Google 지도에 관련 정보 (예: 장소, 리뷰, 사진, 주소, 영업시간)를 쿼리합니다.
4. **그라운딩된 생성:** 검색된 지도 데이터는 Gemini 모델의 대답에 반영되어 사실적 정확성과 관련성을 보장합니다.
5. **대답 및 주석:** 모델은 Google 지도 소스에 연결되는 인라인 주석이 포함된 텍스트 대답을 반환하므로 개발자가 인용을 표시할 수 있습니다.

## Google 지도 기반 그라운딩을 사용하는 이유 및 조건

Google 지도 기반 그라운딩은 정확하고 최신이며 위치별 정보가 필요한 애플리케이션에 적합합니다. 전 세계 2억 5천만 개 이상의 장소로 구성된 Google 지도의 광범위한 데이터베이스를 기반으로 관련성 높은 맞춤 콘텐츠를 제공하여 사용자 환경을 개선합니다.

애플리케이션에서 다음 작업을 수행해야 하는 경우 Google 지도 기반 그라운딩을 사용해야 합니다.

- 지역별 질문에 대해 완전하고 정확한 답변을 제공합니다.
- 대화형 여행 플래너와 현지 가이드를 구축하세요.
- 위치 및 음식점이나 상점과 같은 사용자 선호도를 기반으로 관심 장소를 추천합니다.
- 소셜, 소매 또는 음식 배달 서비스를 위한 위치 인식 환경을 만드세요.

Google 지도를 사용한 그라운딩은 '가장 가까운 커피숍'을 찾거나 길을 안내받는 등 근접성과 현재 사실 데이터가 중요한 사용 사례에서 뛰어납니다.

## 사용 사례

Google 지도 기반 그라운딩은 다양한 위치 인식 사용 사례를 지원합니다.

### 장소 관련 질문 처리

특정 장소에 관해 자세한 질문을 하면 Google 사용자 리뷰 및 기타 지도 데이터를 기반으로 답변을 받을 수 있습니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Is there a cafe near the corner of 1st and Main that has outdoor seating?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### 위치 기반 맞춤설정 제공

사용자의 선호도와 특정 지역에 맞게 맞춤설정된 추천을 받습니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Which family-friendly restaurants near here have the best playground reviews?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(30.2672),
                        Longitude: genai.Ptr(-97.7431),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### 여행 일정 계획 지원

여행 애플리케이션에 적합한 다양한 위치에 관한 정보와 경로가 포함된 여러 날짜의 계획을 생성합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### 자바스크립트

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
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

    prompt := "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput(prompt),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(37.78193),
                        Longitude: genai.Ptr(-122.40476),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // ... code to process response
    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## 서비스 사용 요구사항

이 섹션에서는 Google 지도 그라운딩에 대한 서비스 사용 요구사항을 설명합니다.

### 사용자에게 Google 지도 소스 사용 알림

각 Google 지도 그라운딩 결과와 함께 각 대답을 지원하는 `model_output` 단계의 콘텐츠 블록에 소스 주석이 표시됩니다. 다음 메타데이터가 반환됩니다.

- 소스 URL
- 이름

Google 지도 기반 그라운딩 결과를 표시할 때는 연결된 Google 지도 소스를 명시하고 사용자에게 다음 사항을 알려야 합니다.

- Google 지도 소스는 해당 소스를 뒷받침하는 생성된 콘텐츠 직후에 따라와야 합니다. 이렇게 생성된 콘텐츠를 Google 지도 그라운딩 결과라고도 합니다.
- Google 지도 소스는 단일 사용자 상호작용 내에서 확인 가능해야 합니다.

### Google 지도 소스를 Google 지도 링크와 함께 표시

각 소스 주석에 대해 다음 요구사항에 따라 링크 미리보기를 생성해야 합니다.

- 각 소스는 Google 지도에서 제공한 것임을 명시하고 Google 지도의 텍스트 [저작자 표시 지침](#maps-attribution-guidelines)을 따라야 합니다.
- 응답에 포함된 소스 이름을 표시해야 합니다.
- 주석의 `url`를 사용하여 소스에 연결해야 합니다.

### Google 지도 텍스트 저작자 표시 가이드라인

Google 지도의 텍스트 저작자 소스를 표시할 때는 다음 가이드라인을 따라야 합니다.

- Google 지도 텍스트를 어떤 방식으로도 수정하지 마세요.
  - Google 지도의 대소문자를 변경하지 마세요.
  - Google 지도를 여러 줄로 나누어 표시하지 마세요.
  - Google 지도를 다른 언어로 현지화하지 마세요.
  - 브라우저가 Google 지도를 번역하지 못하도록 HTML 속성 translate="no"를 사용해야 합니다.

일부 Google 지도 데이터 제공업체 및 해당 라이선스 조건에 대한 자세한 내용은 [Google 지도 및 Google 어스 법적 고지](https://www.google.com/help/legalnotices_maps/?hl=ko)를 참고하세요.

## 권장사항

- **사용자 위치 제공:** 가장 관련성 높은 맞춤형 대답을 얻으려면 사용자의 위치를 알 때 항상 `google_maps` 도구 구성에 `latitude` 및 `longitude`를 포함하세요.
- **최종 사용자에게 알림:** 특히 도구가 사용 설정된 경우 Google 지도 데이터가 사용자의 질문에 답변하는 데 사용된다는 점을 최종 사용자에게 명확하게 알립니다.
- **필요하지 않을 때 사용 중지:** Google 지도 기반 그라운딩은 기본적으로 사용 중지되어 있습니다. 성능과 비용을 최적화하려면 쿼리에 명확한 지리적 컨텍스트가 있는 경우에만 사용 설정 (`"tools": [{"type": "google_maps"}]`)하세요.

## 제한사항

- Google 지도 기반 그라운딩은 현재 영어 프롬프트와 응답만 지원합니다.
- 일부 지역에서는 이 도구를 사용하지 못할 수 있습니다.
- 결과는 위치 정확도와 사용 가능한 지도 데이터에 따라 달라질 수 있습니다.
- **지리적 범위:** Google 지도 기반 그라운딩은 전 세계에서 사용할 수 있습니다.
- **기본 상태:** Google 지도 기반 그라운딩 도구는 기본적으로 사용 중지되어 있습니다.
  API 요청에서 명시적으로 사용 설정해야 합니다.

## 가격 및 비율 제한

Google 지도 기반 그라운딩 가격은 모델 생성에 따라 다릅니다.

- **Gemini 3 모델:** 모델이 실행하기로 결정한 각 **검색어**에 대해 프로젝트에 요금이 청구됩니다. 단일 **검색 프롬프트** (모델에 대한 API 요청)로 인해 모델이 필요한 정보를 찾기 위해 여러 검색어를 실행할 수 있습니다. 이러한 각 쿼리는 도구의 청구 가능한 사용으로 계산됩니다.
- **Gemini 2.5 및 이전 모델:** 프로젝트에 **검색 프롬프트**당 요금이 청구됩니다.
  프롬프트가 Google 지도 그라운딩 결과를 하나 이상 성공적으로 반환하는 경우에만 요청에 요금이 청구됩니다. 모델이 해당 결과를 얻기 위해 내부적으로 수행한 개별 검색 쿼리의 수는 상관없습니다.

자세한 가격 정보는 [Gemini API 가격 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.

## 지원되는 모델

다음 모델은 Google 지도 기반 그라운딩을 지원합니다.

| 모델 | Google 지도를 사용한 그라운딩 |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ko) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=ko) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ko) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ko) | ✔️ |
| [Gemini 3.1 Pro 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko) | ✔️ |
| [Gemini 3 Flash 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ko) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ko) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ko) | ✔️ |

## 지원되는 도구 조합

[Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) (Gemini 3.5 Flash 이상 모델에서 지원)과 같은 다른 내장 도구와 함께 Google 지도 기반 그라운딩을 사용하여 더 복잡한 사용 사례를 지원할 수 있습니다. Gemini 3 모델은 이러한 기본 제공 도구를 맞춤 도구 (함수 호출)와 결합하는 것도 지원합니다. [도구 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko) 페이지에서 자세히 알아보세요.

## 다음 단계

- [사용 가능한 다른 도구](https://ai.google.dev/gemini-api/docs/tools?hl=ko)에 대해 알아보세요.
- 책임감 있는 AI 권장사항 및 Gemini API의 안전 필터에 대해 자세히 알아보려면 [안전 설정 가이드](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-24(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-24(UTC)"],[],[]]
