---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ko
fetched_at: 2026-09-28T06:16:05.274724+00:00
title: "\uc5f0\uad6c\uc6a9 Gemini\ub85c \ud0d0\uc0c9 \uc18d\ub3c4 \ub192\uc774\uae30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)

# 연구용 Gemini로 탐색 속도 높이기

[Gemini API 키 받기](https://aistudio.google.com/apikey?hl=ko)

Gemini 모델은 여러 분야에서 기초 연구를 발전시키는 데 사용할 수 있습니다.
다음은 연구를 위해 Gemini를 탐색할 수 있는 방법입니다.

- **모델 출력 분석 및 제어**: 추가 분석을 위해 `CitationMetadata`과 같은 도구를 사용하여 모델에서 생성된 응답 후보를 검사할 수 있습니다. `responseSchema`, `topP`, `topK`와 같은 모델 생성 및 출력 옵션을 구성할 수도 있습니다. [자세히 알아보기](https://ai.google.dev/api/generate-content?hl=ko)
- **멀티모달 입력**: Gemini는 이미지, 오디오, 동영상을 처리할 수 있어 다양한 흥미로운 연구 방향을 지원합니다. [자세히 알아보기](https://ai.google.dev/gemini-api/docs/vision?hl=ko)
- **긴 컨텍스트 기능**: Gemini 3.0 Flash와 Pro에는 100만 개의 토큰 컨텍스트 윈도우가 제공됩니다. [자세히 알아보기](https://ai.google.dev/gemini-api/docs/long-context?hl=ko)
- **Grow with Google**: API와 Google AI Studio를 통해 프로덕션 사용 사례에 맞는 Gemini 모델에 빠르게 액세스하세요. Google Cloud 기반 플랫폼을 찾고 있다면 Gemini Enterprise Agent Platform에서 추가 지원 인프라를 제공할 수 있습니다.

학술 연구를 지원하고 최첨단 연구를 추진하기 위해 Google은 [Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ko#gemini-academic-program)을 통해 과학자 및 학술 연구자에게 Gemini API 크레딧에 대한 액세스 권한을 제공합니다.

## Gemini 시작하기

Gemini API와 Google AI Studio를 사용하면 Google의 최신 모델을 사용하고 아이디어를 확장 가능한 애플리케이션으로 전환할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("How large is the universe?"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("How large is the universe?"),
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## 추천 학자

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ko)

'Google의 연구에서는 Gemini를 시각적 언어 모델 (VLM)로 조사하고 견고성 및 안전성 관점에서 다양한 환경에서의 에이전트 행동을 조사합니다. 지금까지 VLM 에이전트가 컴퓨터 작업을 수행할 때 팝업 창과 같은 방해 요소에 대한 Gemini의 견고성을 평가했으며, Gemini를 활용하여 동영상 입력을 기반으로 소셜 상호작용, 시간적 이벤트, 위험 요소를 분석했습니다.'

[Diyi Yang 웹사이트](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ko)

"Gemini Pro와 Flash는 긴 컨텍스트 윈도우를 통해 개방형 어휘 모바일 조작 프로젝트인 OK-Robot에서 Google을 지원해 왔습니다. Gemini를 사용하면 로봇의 '메모리'(이 경우 긴 작동 시간 동안 로봇이 이전에 관찰한 내용)에 대해 복잡한 자연어 질문과 명령을 내릴 수 있습니다. 또한 Mahi Shafiullah와 저는 Gemini를 사용하여 로봇이 실제 환경에서 실행할 수 있는 코드로 작업을 분해하고 있습니다.'

[Lerrel Pinto 웹사이트](https://www.lerrelpinto.com/)

## Gemini 학술 프로그램

[지원되는 국가](https://ai.google.dev/gemini-api/docs/available-regions?hl=ko)의 자격 요건을 갖춘 학술 연구자 (예: 교수진, 직원, 박사 과정 학생)는 연구 프로젝트에 사용할 Gemini API 크레딧과 더 높은 비율 제한을 신청할 수 있습니다. 이 지원을 통해 과학 실험의 처리량을 높이고 연구를 발전시킬 수 있습니다.

다음 섹션의 연구 분야에 특히 관심이 있지만 다양한 과학 분야의 지원을 환영합니다.

- **평가 및 벤치마크**: 사실성, 안전성, 지침 준수, 추론, 계획과 같은 영역에서 강력한 성능 신호를 제공할 수 있는 커뮤니티에서 승인한 평가 방법입니다.
- **인류를 위한 과학적 발견 가속화**: 희귀 질환 및 소외 질환, 실험 생물학, 재료 과학, 지속 가능성과 같은 분야를 포함한 학제간 과학 연구에서 AI의 잠재적 적용.
- **구체화 및 상호작용**: 대규모 언어 모델을 활용하여 구체화된 AI, 주변 상호작용, 로봇 공학, 인간-컴퓨터 상호작용 분야의 새로운 상호작용을 조사합니다.
- **새로운 기능**: 추론 및 계획을 개선하는 데 필요한 새로운 에이전트 기능을 살펴보고 추론 중에 기능을 확장하는 방법 (예: Gemini Flash 활용)을 알아봅니다.
- **멀티모달 상호작용 및 이해**: 다양한 작업에서 분석, 추론, 계획을 위한 멀티모달 파운데이션 모델의 격차와 기회를 파악합니다.

자격 요건: 유효한 교육 기관 또는 학술 연구 기관에 소속된 개인 (교수진, 연구원 또는 이에 상응하는 직책)만 신청할 수 있습니다. API 액세스 및 크레딧은 Google의 재량에 따라 부여 및 삭제됩니다. Google에서는 매월 신청을 검토합니다.

### Gemini API로 연구 시작하기

[지금 신청하기](https://forms.gle/HMviQstU8PxC5iCt5)

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-24(UTC)

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-24(UTC)"],[],[]]
