---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ko
fetched_at: 2026-08-10T03:15:34.332209+00:00
title: "Gemini Developer API\uc640 Gemini Enterprise Agent Platform \ube44\uad50 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Developer API와 Gemini Enterprise Agent Platform 비교

Gemini로 생성형 AI 솔루션을 개발할 때 Google에서는 [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ko)와 [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ko)라는 두 가지 API 제품을 제공합니다.

Gemini Developer API는 Gemini 기반 애플리케이션을 빌드, 프로덕션화, 확장하는 가장 빠른 방법을 제공합니다. 특정 엔터프라이즈 컨트롤이 필요한 경우가 아니라면 대부분의 개발자는 Gemini 개발자 API를 사용해야 합니다.

Gemini Enterprise Agent Platform은 Google Cloud Platform에서 지원하는 생성형 AI 애플리케이션을 빌드하고 배포하기 위한 엔터프라이즈 지원 기능 및 서비스의 포괄적인 생태계를 제공합니다.

최근 이러한 서비스 간의 마이그레이션이 간소화되었습니다. 이제 통합된 [Google 생성형 AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)를 통해 Gemini Developer API와 Gemini Enterprise Agent Platform API에 모두 액세스할 수 있습니다.

## 코드 비교

이 페이지에는 텍스트 생성을 위한 Gemini Developer API와 Gemini Enterprise Agent Platform 빠른 시작의 코드 비교가 나란히 표시되어 있습니다.

### Python

`google-genai` 라이브러리를 통해 Gemini Developer API와 Gemini Enterprise Agent Platform 서비스에 모두 액세스할 수 있습니다. `google-genai` 설치 방법에 대한 안내는 [라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 페이지를 참고하세요.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript 및 TypeScript

`@google/genai` 라이브러리를 통해 Gemini Developer API와 Gemini Enterprise Agent Platform 서비스에 모두 액세스할 수 있습니다. `@google/genai` 설치 방법에 대한 안내는 [라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 페이지를 참고하세요.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

`google.golang.org/genai` 라이브러리를 통해 Gemini Developer API와 Gemini Enterprise Agent Platform 서비스에 모두 액세스할 수 있습니다. `google.golang.org/genai` 설치 방법에 대한 안내는 [라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 페이지를 참고하세요.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### 기타 사용 사례 및 플랫폼

다른 플랫폼 및 사용 사례는 [Gemini 개발자 API 문서](https://ai.google.dev/gemini-api/docs?hl=ko) 및 [Gemini Enterprise Agent Platform 문서](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ko)의 사용 사례별 가이드를 참고하세요.

## 마이그레이션 고려사항

마이그레이션 시 다음 사항에 유의하세요.

- 인증하려면 Google Cloud 서비스 계정을 사용해야 합니다. 자세한 내용은 [Gemini Enterprise Agent Platform 문서](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ko)를 참고하세요.
- 기존 Google Cloud 프로젝트(API 키를 생성하는 데 사용한 동일한 프로젝트)를 사용하거나 [새 Google Cloud 프로젝트를 만들](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ko) 수 있습니다.
- 지원되는 리전은 Gemini Developer API와 Gemini Enterprise Agent Platform API 간에 다를 수 있습니다. [Google Cloud의 생성형 AI가 지원되는 리전](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=ko) 목록을 참고하세요.
- Google AI Studio에서 만든 모든 모델은 Gemini Enterprise Agent Platform에서 재학습을 거쳐야 합니다.

Gemini Developer API에 Gemini API 키를 더 이상 사용할 필요가 없으면 보안 권장사항에 따라 삭제합니다.

API 키를 삭제하는 방법은 다음과 같습니다.

1. [Google Cloud API 사용자 인증 정보](https://console.cloud.google.com/apis/credentials?hl=ko) 페이지를 엽니다.
2. 삭제할 API 키를 찾아 **작업** 아이콘을 클릭합니다.
3. **API 키 삭제**를 선택합니다.
4. **사용자 인증 정보 삭제** 모달에서 **삭제**를 선택합니다.

   API 키 삭제가 반영되기까지 몇 분 정도 걸립니다. 키 삭제가
   완료되면, 삭제된 API 키를 사용하는 모든 트래픽이 거부됩니다.

## 다음 단계

- Gemini Enterprise Agent Platform의 생성형 AI 솔루션에 대해 자세히 알아보려면 [Gemini Enterprise Agent Platform의 생성형 AI 개요](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-22(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-22(UTC)"],[],[]]
