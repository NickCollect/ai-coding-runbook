---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=ko
fetched_at: 2026-05-11T05:05:10.311648+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 키 사용

Gemini API를 사용하려면 API 키가 필요합니다. 이 페이지에서는 Google AI Studio에서 키를 만들고 관리하는 방법과 코드에서 키를 사용하도록 환경을 설정하는 방법을 설명합니다.

[Gemini API 키 만들기 또는 보기](https://aistudio.google.com/app/apikey?hl=ko)

## API 키

[Google AI Studio](https://aistudio.google.com/app/apikey?hl=ko) **API 키** 페이지에서 모든 Gemini API 키를 만들고 관리할 수 있습니다.

API 키가 있으면 Gemini API에 연결하는 다음과 같은 옵션이 있습니다.

- [API 키를 환경 변수로 설정](#set-api-env-var)
- [API 키를 명시적으로 제공](#provide-api-key-explicitly)

초기 테스트의 경우 API 키를 하드코딩할 수 있지만 안전하지 않으므로 일시적으로만 하드코딩해야 합니다. API
키를 하드코딩하는 예는 [API 키를 명시적으로 제공](#provide-api-key-explicitly) 섹션에서 확인할 수 있습니다.

## Google Cloud 프로젝트

[Google Cloud 프로젝트](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ko)
는 Gemini API와 같은 Google Cloud 서비스를 사용하고,
결제를 관리하고, 공동작업자와 권한을 제어하는 데 기본이 됩니다. Google AI Studio는 Google Cloud 프로젝트에 대한 경량 인터페이스를 제공합니다.

아직 생성된 프로젝트가 없는 경우 새 프로젝트를 만들거나 Google Cloud에서 Google AI Studio로 프로젝트를 가져와야 합니다. Google AI Studio의 **프로젝트** 페이지에는 Gemini API를 사용할 수 있는 충분한 권한이 있는 모든 키가 표시됩니다. 자세한 내용은 [프로젝트 가져오기](#import-projects) 섹션을 참고하세요.

### 기본 프로젝트

신규 사용자의 경우 서비스 약관에 동의하면 Google AI Studio에서 사용 편의를 위해 기본 Google Cloud 프로젝트와 API 키를 생성합니다. Google AI Studio에서 이
프로젝트의 이름을 변경하려면**프로젝트** 뷰로 이동하여
**대시보드**에서 프로젝트 옆에 있는 점 3개 설정 버튼을 클릭하고
**프로젝트 이름 바꾸기**를 선택합니다. 기존 사용자 또는 이미 Google Cloud 계정이 있는 사용자는 기본 프로젝트가 생성되지 않습니다.

## 프로젝트 가져오기

각 Gemini API 키는 Google Cloud 프로젝트와 연결됩니다. 기본적으로 Google AI Studio는 모든 Cloud 프로젝트를 표시하지 않습니다. **프로젝트 가져오기** 대화상자에서 이름 또는 프로젝트 ID를 검색하여 원하는 프로젝트를 가져와야 합니다. 액세스할 수 있는 프로젝트의 전체 목록을 보려면 Cloud Console을 방문하세요.

아직 가져온 프로젝트가 없는 경우 다음 단계에 따라 Google Cloud 프로젝트를 가져오고 키를 만드세요.

1. [Google AI Studio](https://aistudio.google.com?hl=ko)로 이동합니다.
2. 왼쪽 측면 패널에서 **대시보드** 를 엽니다.
3. **프로젝트** 를 선택합니다.
4. **프로젝트** 페이지에서 **프로젝트 가져오기** 버튼을 선택합니다.
5. 가져오려는 Google Cloud 프로젝트를 검색하고 선택한 후 **가져오기** 버튼을 선택합니다.

프로젝트를 가져온 후 **대시보드** 메뉴에서 **API 키** 페이지로 이동하여 방금 가져온 프로젝트에서 API 키를 만듭니다.

## 제한사항

다음은 Google AI Studio에서 API 키와 Google Cloud 프로젝트를 관리하는 데 적용되는 제한사항입니다.

- Google AI Studio **프로젝트** 페이지에서 한 번에 최대 10개의 프로젝트를 만들 수 있습니다.
- 프로젝트와 키의 이름을 지정하고 이름을 바꿀 수 있습니다.
- **API 키** 및 **프로젝트** 페이지에는 최대 100개의 키와 50개의 프로젝트가 표시됩니다.
- 제한이 없거나 Generative Language API로 제한된 API 키만 표시됩니다.

API 키 수정 및
제한을 비롯하여 프로젝트에 대한 추가 관리 액세스 권한을 얻으려면
[Google Cloud 콘솔 사용자 인증 정보 페이지](https://console.cloud.google.com/apis/credentials?hl=ko)를 방문하세요.
Cloud Console에서 프로젝트를 선택하고 기존 API 키를 클릭한 후 **Generative Language API** 로 제한할 수 있습니다.

## API 키를 환경 변수로 설정

환경 변수 `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY`를 설정하면
API 키가
[Gemini API 라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 중 하나를 사용할 때 클라이언트에서 자동으로 선택됩니다. 이러한 변수 중 하나만 설정하는 것이 좋지만 둘 다 설정된 경우 `GOOGLE_API_KEY`가 우선합니다.

REST API 또는 브라우저에서 JavaScript를 사용하는 경우 API 키를 명시적으로 제공해야 합니다.

다음은 다양한 운영체제에서 API 키를 로컬에서 환경 변수 `GEMINI_API_KEY`로 설정하는 방법입니다.

### Linux/macOS - Bash

Bash는 일반적인 Linux 및 macOS 터미널 구성입니다. 다음 명령어를 실행하여 구성 파일이 있는지 확인할 수 있습니다.

```
~/.bashrc
```

응답이 'No such file or directory'인 경우 다음 명령어를 실행하여 이 파일을 만들고 열거나 `zsh`를 사용해야 합니다.

```
touch ~/.bashrc
open ~/.bashrc
```

다음으로 내보내기 명령어를 추가하여 API 키를 설정해야 합니다.

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

파일을 저장한 후 다음을 실행하여 변경사항을 적용합니다.

```
source ~/.bashrc
```

### macOS - Zsh

Zsh는 일반적인 Linux 및 macOS 터미널 구성입니다. 다음 명령어를 실행하여 구성 파일이 있는지 확인할 수 있습니다.

```
~/.zshrc
```

응답이 'No such file or directory'인 경우 다음 명령어를 실행하여 이 파일을 만들고 열거나 `bash`를 사용해야 합니다.

```
touch ~/.zshrc
open ~/.zshrc
```

다음으로 내보내기 명령어를 추가하여 API 키를 설정해야 합니다.

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

파일을 저장한 후 다음을 실행하여 변경사항을 적용합니다.

```
source ~/.zshrc
```

### Windows

1. 검색창에서 '환경 변수'를 검색합니다.
2. **시스템 설정** 을 수정하도록 선택합니다. 이 작업을 수행할지 확인해야 할 수도 있습니다.
3. 시스템 설정 대화상자에서 **환경 변수** 라는 버튼을 클릭합니다.
4. **사용자 변수** (현재 사용자의 경우) 또는 **시스템 변수** (머신을 사용하는 모든 사용자에게 적용됨)에서 **새로 만들기...** 를 클릭합니다.
5. 변수 이름을 `GEMINI_API_KEY`로 지정합니다. Gemini API 키를 변수 값으로 지정합니다.
6. **확인** 을 클릭하여 변경사항을 적용합니다.
7. 새 터미널 세션 (cmd 또는 Powershell)을 열어 새 변수를 가져옵니다.

## API 키를 명시적으로 제공

경우에 따라 API 키를 명시적으로 제공할 수 있습니다. 예를 들면 다음과 같습니다.

- 간단한 API 호출을 수행하고 API 키를 하드코딩하는 것이 좋습니다.
- Gemini API 라이브러리에서 환경 변수를 자동으로 검색하는 데 의존하지 않고 명시적으로 제어하고 싶습니다.
- 환경 변수가 지원되지 않는 환경(예: 웹)을 사용하거나 REST 호출을 하고 있습니다.

다음은 Interactions API를 사용하여 API 키를 명시적으로 제공하는 방법의 예입니다.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

## API 키를 안전하게 보호

Gemini API 키를 비밀번호처럼 취급하세요. 키가 손상되면 다른 사용자가 프로젝트의 할당량을 사용하고, 결제가 사용 설정된 경우 요금이 발생하며, 파일과 같은 비공개 데이터에 액세스할 수 있습니다.

### 중요한 보안 규칙

- **키를 기밀로 유지**: Gemini용 API 키는 애플리케이션이 사용하는 민감한 정보에 액세스할 수 있습니다.

  - **소스 제어에 API 키를 커밋하지 마세요.** Git과 같은 버전 제어 시스템에 API 키를 체크인하지 마세요.
  - **API 키를 클라이언트 측에서 노출하지 마세요.** 프로덕션 환경에서 웹 또는 모바일 앱에서 API 키를 직접 사용하지 마세요. 클라이언트 측 코드의 키(JavaScript/TypeScript 라이브러리 및 REST 호출 포함)는 추출될 수 있습니다.
- **액세스 제한**: 가능한 경우 API 키 사용을 특정 IP 주소, HTTP
  리퍼러 또는 Android/iOS 앱으로 제한합니다.
- **사용 제한**: 각 키에 필요한 API만 사용 설정합니다.
- **정기적으로 감사 실행**: API 키를 정기적으로 감사하고 주기적으로 순환합니다.

### 권장사항

- **API 키로 서버 측 호출 사용** API 키를 사용하는 가장 안전한 방법은 키를 기밀로 유지할 수 있는 서버 측 애플리케이션에서 Gemini API를 호출하는 것입니다.
- **클라이언트 측 액세스에 임시 토큰 사용 (Live API만 해당):** Live API에 직접 클라이언트 측 액세스하려면 임시 토큰을 사용할 수 있습니다. 보안 위험이 낮고 프로덕션에 적합할 수 있습니다. 자세한 내용은
  [임시 토큰](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ko) 가이드를
  참고하세요.
- **키에 제한사항 추가 고려:** API 키 제한사항을 추가하여 키의 권한을 제한할 수 있습니다
  [API 키 제한사항](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=ko#add-api-restrictions)을 추가하여.
  이렇게 하면 키가 유출되더라도 잠재적인 피해를 최소화할 수 있습니다.

일반적인 권장사항은 이
[지원 도움말](https://support.google.com/googleapi/answer/6310037?hl=ko)을 참조하세요.

## API 키 생성 문제 해결

Google AI Studio에서 **API 키 만들기** 버튼이 사용할 수 없으며
"*이 프로젝트에서 키를 만들 권한이 없습니다*"라는 메시지가 표시될 수 있습니다.

이 문제는 프로젝트 내에서 새 키를 생성하는 데 필요한 권한이 없을 때 발생합니다.

- **`resourcemanager.projects.get`**: AI Studio에서 프로젝트의 존재를 확인할 수 있습니다.
- **`apikeys.keys.create`**: API 키 자체를 생성할 수 있습니다.
- **`serviceusage.services.enable`**: 프로젝트에서 Gemini API가 활성 상태인지 확인하는 데 필요합니다.

권한을 수정하려면 프로젝트 관리자 또는 프로젝트가 [조직](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ko)에 속한 경우 조직 관리자에게 위에 나열된 권한이 있는 역할 (예: 프로젝트 편집자 또는 맞춤 역할)을 부여해 달라고 요청하세요.

프로젝트에 대한 관리 액세스 권한이 없는 경우 조직과 연결되지 않은 새 프로젝트를 만들어 키를 생성할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-07(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-07(UTC)"],[],[]]
