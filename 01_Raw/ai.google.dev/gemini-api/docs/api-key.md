---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=ko
fetched_at: 2026-09-28T06:35:28.816373+00:00
title: "Gemini API \ud0a4 \uc0ac\uc6a9 \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 키 사용

Gemini API를 사용하려면 요청을 인증해야 합니다. 표준 또는 승인 API 키를 사용하여 인증할 수 있습니다.

[Gemini API 키 만들기 또는 보기](https://aistudio.google.com/apikey?hl=ko)

## API 키 유형: 표준과 승인

API 키는 Gemini API에 대한 액세스를 제공하지만 보안 특성은 다릅니다. Gemini API는 보안을 강화하기 위해 표준 API 키에서 승인 키로 전환하고 있습니다.

- **표준 API 키**: 청구 및 할당량 목적으로 요청을 Google Cloud 프로젝트와 연결합니다. 표준 키는 호출자를 식별하지 않으므로 지원할 수 있는 권한 및 액세스 제어의 세부사항이 제한됩니다.
- **승인 (auth) 키**: Google Cloud 서비스 계정에 직접 바인딩됩니다. 승인 키를 사용하면 바인딩된 서비스 계정의 ID로 요청이 처리되므로 세부적인 액세스 제어가 가능합니다. 승인 키는 기본적으로 Generative Language API(Gemini API)로 제한되며, Google 시스템에서 감지한 유출된 키의 사용을 신속하게 중단하는 신속한 유출 키 시행을 제공합니다.

안전한 사용을 위해 Gemini API가 표준 키에서 인증 키로 이동합니다.

- **인증 키 기본값**: 2026년 5월 28일부터 Google AI Studio에서 생성된 모든 새 API 키는 인증 키로 자동 생성됩니다.
- **제한되지 않은 키 거부됨**: Gemini API에서 **제한되지 않은 표준 키**의 요청을 거부합니다. 명시적 제한사항이 적용된 표준 API 키는 계속 작동합니다. 이 제한은 공개적으로 공유되거나 다른 서비스에 연결될 수 있는 키의 무단 사용을 방지합니다.

## Google AI Studio에서 API 키 관리

[Google AI Studio](https://aistudio.google.com/apikey?hl=ko)에서 프로젝트와 키를 직접 관리할 수 있습니다.

### Google Cloud 프로젝트

모든 Gemini API 키는 [Google Cloud 프로젝트](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ko)와 연결됩니다.
Google Cloud 프로젝트는 결제, 공동작업자, 권한을 관리합니다. Google AI Studio는 이러한 프로젝트에 액세스할 수 있는 경량 인터페이스를 제공합니다.

- **기본 프로젝트**: 신규 사용자의 경우 서비스 약관에 동의하면 Google AI Studio에서 기본 Google Cloud 프로젝트와 API 키를 자동으로 생성합니다. 대시보드의 **프로젝트** 뷰로 이동하여 이 프로젝트의 이름을 바꿀 수 있습니다.
- **기존 프로젝트**: Google Cloud 계정이 이미 있는 경우 AI Studio에서 기본 프로젝트를 만들지 않습니다. 대신 기존 프로젝트를 가져와야 합니다.

### 프로젝트 가져오기

기본적으로 Google AI Studio에는 모든 Google Cloud 프로젝트가 표시되지 않습니다. 사용할 프로젝트를 가져와야 합니다.

1. [Google AI Studio](https://aistudio.google.com?hl=ko)로 이동합니다.
2. 왼쪽 패널에서 **대시보드**를 열고 **프로젝트**를 선택합니다.
3. **프로젝트 가져오기** 버튼을 클릭합니다.
4. 가져올 Google Cloud 프로젝트를 검색하여 선택한 다음 **가져오기**를 클릭합니다.
5. 가져온 후 대시보드의 **API 키** 페이지로 이동하여 해당 프로젝트에서 키를 만듭니다.

### 키 생성 권한 문제 해결

**API 키 만들기** 버튼을 사용할 수 없고 *'이 프로젝트에서 키를 만들 권한이 없습니다'*라는 메시지가 표시되면 필요한 IAM 권한이 없는 것입니다.

Google Cloud 프로젝트 또는 조직 관리자에게 다음 권한이 포함된 역할 (예: 프로젝트 편집자)을 부여해 달라고 요청하세요.

- `resourcemanager.projects.get`: AI Studio에서 프로젝트를 확인할 수 있습니다.
- `apikeys.keys.create`: 키 생성을 허용합니다.
- `serviceusage.services.enable`: Generative Language API가 사용 설정되어 있는지 확인합니다.
- `iam.serviceAccounts.create`: 연결된 서비스 계정을 만드는 데 필요합니다.
- `iam.serviceAccountApiKeyBindings.create`: 서비스 계정을 API 키에 바인딩합니다.

관리 액세스 권한을 얻을 수 없는 경우 조직과 연결되지 않은 새 Google Cloud 프로젝트를 만들어 키를 생성할 수 있습니다.

## 환경 설정

키가 있으면 애플리케이션에서 안전하게 사용할 수 있도록 환경을 구성합니다.

### 옵션 1: 환경 변수 사용 (권장)

`GEMINI_API_KEY` 또는 `GOOGLE_API_KEY` 환경 변수를 설정합니다. Gemini API 클라이언트 라이브러리는 이러한 변수를 자동으로 감지하고 사용합니다. 두 가지 모두 설정된 경우 `GOOGLE_API_KEY`가 우선 적용됩니다.

운영체제를 선택하여 변수를 설정합니다.

### Linux/macOS - Bash

bash 구성 파일이 있는지 확인합니다.

```
~/.bashrc
```

그렇지 않은 경우 하나를 만들어 엽니다.

```
touch ~/.bashrc && open ~/.bashrc
```

파일 끝에 내보내기 명령어를 추가합니다.

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

파일을 저장한 후 변경사항을 적용합니다.

```
source ~/.bashrc
```

### macOS - Zsh

zsh 구성 파일이 있는지 확인합니다.

```
~/.zshrc
```

그렇지 않은 경우 하나를 만들어 엽니다.

```
touch ~/.zshrc && open ~/.zshrc
```

내보내기 명령어를 추가합니다.

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

파일을 저장한 후 변경사항을 적용합니다.

```
source ~/.zshrc
```

### Windows

1. Windows 검색창에서 '환경 변수'를 검색합니다.
2. 시스템 속성 대화상자에서 **환경 변수**를 클릭합니다.
3. **사용자 변수** 또는 **시스템 변수**에서 **새로 만들기…**를 클릭합니다.
4. 변수 이름을 `GEMINI_API_KEY`로, 값을 API 키로 설정합니다.
5. **확인**을 클릭하여 저장합니다. 새 터미널 세션을 열어 변수를 로드합니다.

### 옵션 2: 코드에서 API 키 명시적으로 제공

클라이언트를 초기화할 때 API 키를 명시적으로 전달할 수 있습니다. 환경 변수를 사용할 수 없는 경우에만 이렇게 하세요.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few sentences."),
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## 보안 및 보안 비밀 관리

Gemini API 키를 비밀번호처럼 취급하세요. 보안이 침해되면 다른 사용자가 프로젝트의 할당량을 사용하고, 예기치 않은 청구 요금이 발생하며, 비공개 리소스에 액세스할 수 있습니다.

### 중요 보안 규칙

- **키를 기밀로 유지**: Git과 같은 소스 제어 시스템에 API 키를 체크인하지 마세요.
- **프로덕션에서 클라이언트 측에 키를 노출하지 마세요**: 웹 또는 모바일 앱에 API 키를 직접 하드 코딩하지 마세요. 클라이언트 측 코드에서 컴파일된 키는 사용자가 추출할 수 있습니다. 클라이언트 측 앱을 보호하려면 백엔드 프록시 서버를 실행하여 실제 API 호출을 수행하세요.

### 보안 비밀 관리 권장사항

- **환경 변수**: 구성 파일이 아닌 환경 변수에서 키를 읽습니다.
- **Secret Manager**: 프로덕션의 경우 [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=ko)와 같은 보안 비밀 저장소에 키를 저장합니다.
- **결제 알림**: Google Cloud 콘솔에서 결제 알림을 설정하여 사용량 또는 비용이 급증하는 경우 알림을 받습니다.

### 유출 대응 체크리스트

API 키가 유출되었다고 의심되는 경우 다음 단계를 따르세요.

1. **새 키 생성**: Google AI Studio 또는 Cloud 콘솔에서 대체 키를 만듭니다.
2. **애플리케이션 업데이트**: 새 키를 사용하여 코드를 배포합니다.
3. **도용된 키 사용 중지 또는 삭제**: 새 키가 확인되면 Cloud Console에서 유출된 키를 사용 중지합니다. 애플리케이션 다운타임을 방지하려면 새 키가 완전히 활성화될 때까지 이전 키를 삭제하지 마세요.
4. **사용량 감사**: Google Cloud 콘솔에서 결제 로그와 API 사용량을 확인하여 승인되지 않은 활동을 식별합니다.

## 키 제한 및 보안

API 키에 제한사항을 추가하면 키가 손상되었을 때 발생할 수 있는 피해를 최소화할 수 있습니다.

### 요청 출처 제한 적용

출처 제한사항은 키를 사용할 수 있는 IP 주소, 웹사이트 또는 애플리케이션을 제한합니다.

1. [Google Cloud 콘솔 사용자 인증 정보 페이지](https://console.cloud.google.com/apis/credentials?hl=ko)로 이동합니다.
2. 프로젝트를 선택하고 제한하려는 API 키의 이름을 클릭합니다.
3. **애플리케이션 제한사항**에서 **IP 주소** (또는 환경에 적합한 제한 유형)를 선택합니다.
4. 허용된 IP 주소 또는 범위를 지정한 다음 **저장**을 클릭합니다.

### 제한되지 않은 표준 API 키 보호

Gemini API를 계속 사용하려면 제한되지 않은 키를 보호해야 합니다.

#### 방법 A: Gemini API로만 키 제한 (AI Studio)

Gemini API에만 키를 사용하는 경우 AI Studio에서 직접 보안을 설정하세요.

1. [Google AI Studio](https://aistudio.google.com/api-keys?hl=ko)의 **API 키** 페이지에서 **제한 없음** 라벨이 표시된 키를 찾습니다.
2. 라벨 위로 마우스를 가져가고 대화상자에서 **제한 추가**를 클릭합니다.
3. **Gemini API로만 제한**을 선택합니다.
4. **키 제한**을 클릭하여 확인합니다.

#### 방법 B: 다른 서비스의 키 제한 (Google Cloud 콘솔)

키가 다른 Google API와 공유되는 경우 (권장하지 않음) Cloud 콘솔에서 제한합니다. **참고: 이 제한사항이 적용된 후에는 이 키를 사용하는 Gemini API 요청이 실패합니다.**

1. [Google Cloud 콘솔 사용자 인증 정보 페이지](https://console.cloud.google.com/apis/credentials?hl=ko)로 이동합니다.
2. 프로젝트와 API 키를 선택합니다.
3. **API 제한사항**에서 **API 제한사항 선택** 드롭다운을 사용하여 이 키로 액세스할 API를 선택합니다. **Generative Language API**는 선택하지 마세요.
4. **저장**을 클릭합니다. Gemini API를 계속 사용하려면 AI Studio에서 별도의 제한된 키를 만드세요.

### 휴면 키 차단

2026년 5월 7일부터 Gemini API는 장기간 휴면 상태인 무제한 API 키를 차단합니다. 이러한 키는 AI Studio에 **차단됨** 태그로 표시됩니다. 계속하려면 새 키를 생성하거나 기존 제한된 키를 사용해야 합니다.

## 인증 키로 이전

새 인증 API 키를 만들고 애플리케이션을 업데이트하려면 다음 단계를 따르세요.

1. [AI Studio API 키 페이지](https://aistudio.google.com/api-keys?hl=ko)로 이동합니다.
2. **키 유형** 열을 확인하여 **스탠더드**로 표시된 키를 식별합니다.
3. **API 키 만들기**를 클릭하여 새 키를 생성합니다. AI Studio에서 새로 생성된 모든 키는 인증 키로 자동 생성됩니다.
4. 새 인증 API 키를 복사합니다.
5. 새 인증 API 키를 사용하도록 애플리케이션 코드, 환경 변수, 배포 구성을 업데이트합니다.
6. 애플리케이션을 테스트하여 새 키로 올바르게 작동하는지 확인합니다.
7. 확인되면 오용을 방지하기 위해 이전 트래픽 키를 삭제하거나 취소합니다.

## 제한사항

Google AI Studio에는 다음과 같은 프로젝트 및 키 관리 제한사항이 적용됩니다.

- Google AI Studio **프로젝트** 페이지에서 한 번에 최대 10개의 프로젝트를 만들 수 있습니다.
- **API 키** 및 **프로젝트** 페이지에는 최대 100개의 키와 50개의 프로젝트가 표시됩니다.
- 제한이 없거나 Generative Language API (Gemini API)로만 제한된 API 키만 표시됩니다.

고급 프로젝트 관리 또는 다른 제한사항이 있는 키를 수정하려면 [Google Cloud 콘솔 사용자 인증 정보 페이지](https://console.cloud.google.com/apis/credentials?hl=ko)를 사용하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-25(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-25(UTC)"],[],[]]
