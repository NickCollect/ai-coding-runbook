---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko
fetched_at: 2026-06-22T06:25:03.362487+00:00
title: "Google AI Studio\uc5d0\uc11c \uc571 \ube4c\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google AI Studio에서 앱 빌드

[[이 페이지에서는 Google AI Studio를 사용하여 Nano Banana, Live API 같은 Gemini의 최신 기능을 테스트하는 앱을 빠르게 빌드 또는 '바이브
코딩'하고 배포하는 방법을 설명합니다.](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)](https://ai.google.dev/gemini-api/docs/live?hl=ko) Google AI Studio는 풀 스택 런타임으로 **웹 앱** 을 빌드하고 Kotlin 및 Jetpack Compose로 **네이티브 Android 앱** 을 빌드하는 것을 모두 자연어 프롬프트를 통해 지원합니다.

## 시작하기

Google AI Studio의 [빌드 모드](https://aistudio.google.com/apps?hl=ko)에서 바이브 코딩을 시작하세요. 다음과 같은 몇 가지 방법으로 빌드를 시작할 수 있습니다.

- **프롬프트로 시작**: 빌드 모드에서 입력 상자를 사용하여 빌드하려는 항목에 관한 설명을 입력합니다. AI 칩을 선택하여 이미지 생성 또는 Google 지도 데이터와 같은 특정 기능을 프롬프트에 추가합니다. 음성 텍스트 변환 버튼을 사용하여 원하는 내용을 말할 수도 있습니다.
- **"운이 좋다면" 버튼**: 창의적인 아이디어가 필요하면 "운이
  좋다면" 버튼을 사용하세요. Gemini가 시작할 수 있는 프로젝트 아이디어가 포함된 프롬프트를 생성합니다.
- **갤러리에서 프로젝트 리믹스**: [앱
  갤러리](https://aistudio.google.com/apps?source=showcase&hl=ko)에서 프로젝트를 열고 **앱 복사**를 선택합니다.

프롬프트를 실행하면 필요한 코드와 파일이 생성되고 앱의 실시간 미리보기가 오른쪽에 표시됩니다.

## 생성되는 항목

프롬프트를 실행하면 AI Studio가 완전한 애플리케이션을 만듭니다. 플랫폼 선택 도구를 사용하여 **웹 앱** 또는 **네이티브 Android 앱** 을 빌드하도록 선택할 수 있습니다.

**웹 앱** (기본값)의 경우 AI Studio는 다음을 포함하는 풀 스택 환경을 만듭니다.

- **클라이언트 측**: 웹 프런트엔드 (React가 기본값)입니다.
- **서버 측**: 보안 API 호출,
  데이터베이스 연결, npm 패키지 사용을 허용하는 Node.js 런타임입니다.

**Android 앱**의 경우 AI Studio는 브라우저 기반 에뮬레이터에서 미리 보고, 실제 기기에 설치하고,
테스트를 위해 Play 스토어에 게시할 수 있는 Kotlin 및 Jetpack Compose 프로젝트를 생성합니다. [Android 앱 빌드에 관해 자세히 알아보세요](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=ko).

오른쪽 미리보기 창에서 **코드** 탭을 선택하여 생성된 코드를 볼 수 있습니다. **Antigravity 에이전트** 는 스택 전반에서 여러 파일을 지능적으로 관리하여 변경사항이 올바르게 전파되도록 합니다.

### Antigravity 에이전트

**Antigravity 에이전트**는 [Google
Antigravity](https://antigravity.google?hl=ko) 내의 기본 AI 기능이며 이제
에이전트 하네스의 핵심 구성요소가 Google AI Studio의 빌드 모드 환경을 지원합니다. 전체 프로젝트의 컨텍스트를 유지하고, 여러 파일을 관리하고, 복잡한 안내를 이해하여 강력한 풀 스택 애플리케이션을 빌드함으로써 단순한 코드 생성을 넘어섭니다.

주요 기능은 다음과 같습니다.

- **컨텍스트 인식**: 이전 프롬프트 및 파일 상태의 컨텍스트를 유지합니다.
- **다중 파일 관리**: 여러 파일의 종속 항목을 처리합니다.
- **확인된 실행**: 코드 업데이트를 확인하여 환각을 줄입니다.

## 풀 스택 기능

Google AI Studio는 최신 웹 생태계의 강력한 기능을 활용하여 클라이언트 측 프로토타입 이상의 항목을 빌드할 수 있도록 지원합니다.

- **서버 측 런타임 및 npm**: npm 패키지의 방대한 라이브러리를 사용합니다. 에이전트는 앱에 필요한 패키지 (예: 데이터 시각화 또는 API 클라이언트를 위한 특정 라이브러리)를 자동으로 식별하고 설치합니다. 원하는 경우 특정 패키지를 요청할 수도 있습니다.
- **보안 비밀 관리**: **설정** 메뉴에 API 키와 보안 비밀을 안전하게 저장합니다. 서버 측 코드에서 액세스할 수 있으므로 클라이언트 측 노출로부터 안전하게 보호됩니다.
- **멀티플레이어**: AI Studio 내에서 직접 실시간 공동작업 환경을 빌드합니다. 서버 측 런타임은 사용자가 함께 상호작용하는 데 필요한 상태와 연결을 관리합니다.
- **Firebase Firestore 및 인증**: Firestore 데이터베이스 (영구 데이터 저장소) 및 Firebase 인증('Google 계정으로 로그인'을 비롯한 로그인 흐름)을 비롯한 Firebase를 자동으로 프로비저닝하고 설정합니다.
  에이전트는 전체 설정 프로세스를 처리하고 이러한 서비스의 앱에서 코드를 작성하기도 합니다.
- **Google Workspace 통합**: Gmail, Sheets, Docs, Drive, Calendar 등과 같은 Google Workspace
  API에 앱을 연결합니다. AI Studio는 모든 OAuth 구성을 자동으로 처리합니다.

[풀 스택 앱 개발에 관해 자세히 알아보세요.](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko)

### Android 앱

Kotlin 및 Jetpack Compose를 사용하여 네이티브 Android 앱을 빌드할 수도 있습니다.
브라우저 기반 Android 에뮬레이터에서 앱을 미리 보고, 브라우저에서 ADB를 사용하여 실제 기기에 설치하고, 내부 테스트를 위해 Play 스토어에 게시합니다.

[Android 앱 빌드에 관해 자세히 알아보세요.](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=ko)

## 계속 빌드하세요

Google AI Studio에서 애플리케이션의 초기 코드를 생성하면 다음과 같이 계속 개선할 수 있습니다.

### Google AI Studio에서 빌드

- **Gemini로 반복**: **빌드 모드** 의 채팅 패널을 사용하여 Gemini에게
  수정, 새 기능 추가 또는 스타일 변경을 요청합니다.
- **코드 직접 수정**: 미리보기 패널에서 **코드 탭**을 열어
  실시간으로 수정합니다.

### 외부에서 개발

더 고급 워크플로의 경우 코드를 내보내고 원하는 환경에서 작업할 수 있습니다.

- **다운로드 및 로컬 개발**: 생성된 코드를 **ZIP
  파일**로 내보내고 코드 편집기로 가져옵니다.
- **GitHub로 푸시**: 코드를 **GitHub 저장소**로 푸시하여 기존 개발 및
  배포 프로세스와 통합합니다.

## 주요 특징

Google AI Studio에는 빌드 프로세스를 직관적이고 시각적으로 만드는 여러 기능이 포함되어 있습니다.

- **풀 스택 앱 만들기 및 반복**: 프롬프트만으로 풀 스택 앱을 만들고 채팅 또는 **주석 모드**를 통해 반복합니다. 주석 모드를 사용하면 앱의 UI 부분을 강조표시하고 원하는 변경사항을 설명할 수 있습니다.
- **앱 공유 및 배포**: 다른 사용자와 창작물을 공유하여
  공동작업하거나 작업을 선보일 수 있습니다. 공유할 때 API 호출은 사용량 한도에 포함됩니다. 유료 모델을 사용하는 경우 비용이 발생할 수 있습니다. 그런 다음 앱이 준비되면 Cloud Run에 배포합니다.
- **앱 갤러리**: 앱 갤러리는 프로젝트 아이디어의 시각적 라이브러리를 제공합니다.
  Gemini로 가능한 작업을 둘러보고, 애플리케이션을 즉시 미리 보고, 리믹스하여 나만의 애플리케이션을 만들 수 있습니다.

## 앱 배포 또는 보관처리

애플리케이션이 준비되면 배포할 수 있습니다.

- **Cloud Run**: 애플리케이션을 확장 가능한 서비스로 배포합니다.
  [Google Cloud Run](https://cloud.google.com/run?hl=ko)의 가격은 사용량에 따라 적용될 수 있습니다. 배포에 관해 자세히 알아보려면
  [Google AI Studio에서 배포](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ko)를 참고하세요.
- **GitHub**: 프로젝트를 GitHub 저장소로 내보냅니다.

## 제한사항

이 섹션에는 Google AI Studio의 빌드 모드에 적용되는 현재 제한사항이 나와 있습니다.

### API 키 관리

Gemini API를 사용하는 새 앱을 만들면 AI Studio가 Gemini API 키를 앱의 서버 측 환경에서 보안 비밀로 자동으로 구성합니다.
이 키는 **보안 비밀** 패널에서 보고 관리할 수 있습니다.

- **자동 설정**: `GEMINI_API_KEY`가 자동으로 설정되므로 빌드를 시작하기 위해 수동으로
  구성할 필요가 없습니다.
- **서버 측 전용**: API 키는 서버 측 런타임에 삽입되며
  클라이언트 측 코드에는 포함되지 않습니다.
- **기존 앱**: 2026년 5월 14일 이전에 빌드된 앱의 경우 다음에 앱의 Gemini 기능을 수정할 때 에이전트가
  Gemini API 통합을 권장되는
  서버 측 접근 방식으로 자동으로 업그레이드합니다.

### Google AI Studio 외부 배포

- **Cloud Run**: AI Studio에서 Cloud Run에 배포하면 API 키가
  서버 측 환경에 안전하게 포함됩니다. 배포된 앱은 모든 사용자의 Gemini API 호출에 API 키를 사용합니다.
- **ZIP 다운로드**: 앱을 ZIP 파일로 다운로드하여 다른 곳에서 운영하려면 호스팅 환경에서 `GEMINI_API_KEY` 환경 변수를 설정해야 합니다. 앱의 Gemini API 호출은 서버 측 코드에서 이루어지므로 키가 최종 사용자에게 노출되지 않습니다.

### 앱 공유 시 오류

앱을 공유하고 최종 사용자가 공유 URL을 사용할 때 **403 액세스 제한됨** 오류가 발생하면 다음 중 한 가지 이유 때문일 수 있습니다.

- **브라우저 확장 프로그램**: Privacy Badger와 같은 개인 정보 보호 확장 프로그램이 앱을 차단할 수 있습니다. 오류를 방지하려면 확장 프로그램을 사용 중지하세요.
- **빌드 문제**: 현재 코드에 문제가 있을 수 있습니다. 에이전트에게 '현재 코드의 빌드 문제를 해결'하도록 프롬프트를 표시한 후 URL을 다시 공유합니다.

## FAQ

### AI Studio의 빌드란 무엇인가요?

AI Studio 빌드는 간단한 프롬프트에서 Gemini를 사용하는 프로덕션 지원 AI 기반 애플리케이션으로 전환할 수 있도록 설계된 플랫폼입니다. 프롬프트로 빌드하려는 항목을 설명하면 Gemini가 앱을 생성합니다. 갤러리를 둘러보며 Gemini API로 가능한 작업을 확인하고 앱을 리믹스하여 나만의 앱을 만들 수도 있습니다.

### 빌드에서 Gemini API 키를 어떻게 처리하나요?

Gemini API를 사용하는 앱을 만들면 AI Studio가 Gemini API 키를 서버 측 보안 비밀로 자동으로 설정합니다. 앱의 Gemini API 호출은 이 키를 사용하여 서버 측 코드에서 이루어지므로 브라우저에 노출되지 않습니다. API 키는 설정의 **보안 비밀** 패널에서 볼 수 있습니다.

### 앱을 공유할 때 API 키가 노출되나요?

아니요. API 키는 서버 측 보안 비밀로 저장되며 클라이언트 측 코드에는 포함되지 않습니다. 앱을 공유하면 다른 사용자가 앱을 사용할 수 있지만 API 키는 볼 수 없습니다.

다른 사용자와 앱을 공유할 때 API 호출은 사용량 한도에 포함됩니다.
유료 모델을 사용하는 경우 비용이 발생할 수 있습니다. AI Studio는 설정 중에 앱에 비용이 발생할 수 있는 경우 공유하기 전에 미리 알려줍니다.

### 내 앱을 볼 수 있는 사용자는 누구인가요?

기본적으로 앱은 비공개입니다. 다른 사용자와 앱을 공유하여 앱을 사용하도록 할 수 있습니다. 앱을 공유하는 사용자는 앱의 코드를 보고 자신의 용도로 포크할 수 있습니다. 수정 권한으로 앱을 공유하면 다른 사용자가 앱의 코드를 수정할 수 있습니다.

### AI Studio 외부에서 앱을 실행할 수 있나요?

예. AI Studio에서
[Cloud Run](https://cloud.google.com/run?hl=ko)에 앱을 배포하면
서버 측 환경에 API 키가 안전하게 구성된 공개 URL이 앱에 제공됩니다. 앱을 ZIP 파일로 다운로드하여 다른 곳에서 호스팅할 수도 있습니다. 호스팅 환경에서 `GEMINI_API_KEY` 환경 변수를 설정해야 합니다. Gemini API 호출은 서버 측 코드에서 이루어지므로 키가 안전하게 유지됩니다.

배포 옵션에 관해 자세히 알아보려면 [Google AI Studio에서 배포](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ko)를 참고하세요.

### 자체 도구로 로컬에서 앱을 개발한 후 여기에 공유할 수 있나요?

이 기능은 아직 사용할 수 없습니다. Google은 앞으로 더 많은 앱 사용 사례를 지원할 수 있기를 기대하고 있습니다. 구체적인 의견이 있으면 언제든지 의견을 보내주세요.

### 앱에서 데이터베이스 또는 기타 저장소를 사용하려면 어떻게 해야 하나요?

AI Studio 앱은 Cloud Run 컨테이너에서 실행되는 표준 앱입니다. 동적 IP 범위에서 액세스를 방지하는 방화벽이 없는 한 네트워크를 통해 연결할 수 있는 모든 저장소 솔루션을 사용할 수 있습니다.

Google은 앞으로 AI Studio 내에서 직접 구성할 수 있는 저장소에 대한 직접 지원을 추가하기 위해 노력하고 있습니다.

### 마이크, 웹캠, 기타 Navigator API에 액세스하려면 어떻게 해야 하나요?

시청자가 앱의 웹캠 또는 기타
기기 사용을 인식하도록 하려면 앱이 이러한 [Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator)에 액세스하기 전에 추가 확인이 필요합니다.
앱 제작자는 이러한 권한 요청을 앱의 `metadata.json` 파일에 추가할 수 있습니다. 예를 들면 다음과 같습니다.

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

`requestFramePermissions`에 지원되는 값은
표준 [정책 제어 기능](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md)의 하위 집합입니다.

### 앱에서 GitHub를 사용하려면 어떻게 해야 하나요?

AI Studio의 GitHub 통합을 사용하면 작업용 저장소를 만들고 최신 변경사항을 커밋할 수 있습니다. 현재 원격 변경사항 가져오기는 지원되지 않습니다.

### 다른 사용자에게 내 앱에 대한 수정 액세스 권한을 부여할 수 있나요?

아직 지원되지 않지만 곧 지원될 예정입니다.

### 내 앱이 정책 위반으로 신고된 이유는 무엇인가요?

Google에는 앱이 Google 정책을 준수하는지 자동으로 검토하는 시스템이 있습니다. 앱이 Google 정책을 위반하는 것으로 확인되면 AI Studio에서 앱이 삭제됩니다. 정책 위반에는 다음이 포함되나 이에 국한되지 않습니다.

- 멀웨어, 피싱 또는 명의 도용이 포함된 앱
- 아동 성적 학대 이미지 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 괴롭힘 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 증오심 표현에 대한 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 인신매매 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 음란물 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 폭력 및 유혈 콘텐츠 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱
- 유해하거나 위험한 정책을 위반하는 콘텐츠를 표시하거나 배포하는 앱

앱이 정책 위반으로 신고되었으며 오류라고 생각되면 이의신청을 제출할 수 있습니다. Google 정책을 반복적으로 위반하면 AI Studio에 대한 액세스가 해지될 수 있습니다.

### 앱 개발자로서의 책임은 무엇인가요?

다시 한번 말씀드리지만 애플리케이션의 소유자로서 애플리케이션의 동작과 처리하는 모든 데이터에 대한 책임은 본인에게 있습니다. 여기에는 다음이 포함됩니다.

- **법규 준수 및 서드 파티 권리:** 앱이 모든 관련 법규를 준수하고 지식 재산권 및 개인 정보 보호 권리를 비롯한 타인의 권리를 침해하지 않도록 합니다.
- **콘텐츠 모니터링:** 앱에서 사용하는
  다른 서비스에 추가 약관 준수가 적용될 수 있습니다. 예를 들어
  [Google Cloud 서비스 약관](https://cloud.google.com/terms?hl=ko)은
  Firestore에 적용되며 서드 파티 콘텐츠를 호스팅하는 고객이 금지된 콘텐츠 (예: 불법
  콘텐츠)를 정의하는 정책을 게시하고 해당 불법 콘텐츠의 존재 여부를 모니터링하도록 요구합니다.
- **안전한 구현:** 애플리케이션이 오용되지 않도록 필요한 보호 조치 및 중재 도구를 구현합니다.

서비스 약관의 [사용 제한사항](https://ai.google.dev/gemini-api/terms?hl=ko#use-restrictions)
을 숙지하세요.

### AI Studio의 앱 갤러리에 있는 앱에는 어떤 약관이 적용되나요?

달리 명시되지 않는 한 [Gemini API 추가 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)
은 AI Studio의 앱 갤러리에 소개된 앱의 사용에 적용됩니다.

## 다음 단계

- [풀 스택 앱 개발](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko) (웹)
- [Android 앱 빌드](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=ko)
- [앱 갤러리](https://aistudio.google.com/apps?source=showcase&hl=ko)에서 예시를 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-19(UTC)"],[],[]]
