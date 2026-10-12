---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko
fetched_at: 2026-10-12T06:56:20.875539+00:00
title: "Google AI Studio\uc5d0\uc11c \ud480 \uc2a4\ud0dd \uc571 \uac1c\ubc1c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google AI Studio에서 풀 스택 앱 개발

이제 Google AI Studio에서 풀 스택 개발을 지원하므로 클라이언트 측 프로토타입을 넘어선 애플리케이션을 빌드할 수 있습니다. 서버 측 런타임을 사용하면 보안 비밀을 관리하고, 외부 API에 연결하고, 실시간 멀티플레이어 환경을 빌드할 수 있습니다.

## 서버 측 런타임

이제 Google AI Studio 애플리케이션에 서버 측 구성요소 (Node.js)를 포함할 수 있습니다.
그러면 다음과 같은 이점을 얻을 수 있습니다.

- **서버 측 로직 실행**: 클라이언트에 노출해서는 안 되는 코드를 실행합니다.
- **npm 패키지 액세스**: [Antigravity 에이전트](https://antigravity.google/docs/agent?hl=ko)
  는 광범위한 npm 생태계에서 패키지를 설치하고 사용할 수 있습니다.
- **보안 비밀 처리**: API 키와 사용자 인증 정보를 안전하게 사용합니다.

### npm 패키지 사용

`npm install`을 수동으로 실행할 필요가 없습니다. 에이전트에게 패키지가 필요한 기능을 추가해 달라고 요청하기만 하면 설치 및 가져오기를 처리합니다.

**예**: > "`axios`를 사용하여 외부 API에서 데이터를 가져와 줘."

## 보안 비밀 안전하게 관리

이제 서버 측 코드와 보안 비밀 관리를 통해 세상과 상호작용하는 앱을 빌드할 수 있습니다.

### Gemini API 키

Gemini API를 사용하는 새 앱을 만들면 AI Studio에서 `GEMINI_API_KEY`를 서버 측 보안 비밀로 자동으로 구성하므로 수동으로 설정할 필요가 없습니다. 이 키는 설정의 **보안 비밀** 패널에서 볼 수 있습니다. 앱의 Gemini API 호출은 이 키를 사용하여 서버 측 코드에서 이루어지므로 브라우저에 노출되지 않습니다.

### 서드 파티 API 키

다른 서비스의 경우 API 키를 수동으로 추가할 수 있습니다.

- **서드 파티 API**: Stripe, SendGrid 또는 커스텀
  REST API와 같은 서비스에 연결합니다.
- **데이터베이스**: 외부 데이터베이스 (예: Supabase, Firebase,
  또는 MongoDB Atlas를 통해)에 연결하여 세션 외에 데이터를 유지합니다.

실제 앱을 빌드할 때는 API 키가 필요한 서드 파티 서비스(예: Twilio, Slack 또는 데이터베이스)에 연결해야 하는 경우가 많습니다. 다음 단계에 따라 키를 수동으로 추가할 수 있습니다.

1. **보안 비밀 추가**: Google AI Studio의 **설정** 메뉴로 이동하여 보안 비밀 섹션을 찾습니다.
2. **키 저장**: 여기에 API 키 또는 보안 비밀 토큰을 추가합니다.
3. **코드에서 액세스**: 에이전트는 이러한
   보안 비밀에 안전하게 액세스하는 서버 측 코드를 작성할 수 있습니다 (일반적으로 환경 변수를 통해). 이렇게 하면 클라이언트 측 브라우저에
   노출되지 않습니다.

필요한 경우 에이전트는 새 보안 비밀이 필요하거나 프로젝트의 env 변수에서 새 키가 감지될 때마다 키를 추가하라는 메시지를 표시하는 카드를 채팅에 표시합니다.

### 데이터베이스 및 인증을 위한 Firebase 통합

이제 Google AI Studio를 사용하면 Firebase 통합을 통해 앱에 데이터베이스 또는 인증을 쉽게 추가할 수 있습니다.
Antigravity 에이전트는 다음 서비스를 자동으로 프로비저닝하고 설정할 수 있습니다.

- **Firestore 데이터베이스**: 클라이언트 및 서버 측 개발을 위한 데이터를 저장하고 동기화하기 위한 유연하고 확장 가능한 NoSQL 클라우드 데이터베이스입니다.
- **Firebase 인증**: 사용자가 Google 계정으로 로그인 흐름을 사용하여 애플리케이션에 안전하게 로그인할 수 있도록 합니다.

에이전트에게 '앱에 데이터베이스 추가' 또는 'Google 로그인 설정'을 요청하기만 하면 필요한 구성 및 코드 생성을 처리합니다.

Firebase를 사용하면 무료로 시작할 수 있으며, 할당량을 늘리거나 유료 기능을 사용할 준비가 되면 유료 계정으로 확장할 수 있습니다.

## Google Workspace API

Google AI Studio를 사용하면 Google Workspace API에 연결되는 앱을 빌드할 수 있으므로 사용자는 앱 내에서 이메일, 스프레드시트, 문서, 캘린더 일정 등 실제 데이터를 사용할 수 있습니다. 더 이상 Google Cloud 프로젝트를 설정하거나, OAuth를 구성하거나, API를 수동으로 관리할 필요가 없습니다.

### 작동 방식

다음 두 가지 방법으로 Workspace 통합을 추가할 수 있습니다.

- **채팅 패널에서 설명**: 하단의 채팅 패널에서 원하는 내용을 에이전트에게 알려주기만 하면 됩니다. 예를 들어 *"영수증을 내 Google Sheets에 기록하는 비용 추적기를 빌드해 줘"* 또는 *"읽지 않은 Gmail 메시지를 요약하는 대시보드를 만들어 줘"*와 같이 요청할 수 있습니다.
- **통합 패널에서 선택**: 빌드 모드의 오른쪽 사이드바에서 **통합** 패널을 열고 연결하려는 Workspace 앱을 사용 설정합니다.

Workspace 앱을 추가하면 AI Studio에서 자동으로 다음 작업을 실행합니다.

1. 앱에 필요한 Google API를 연결합니다.
2. API를 호출하는 서버 측 코드를 생성합니다.
3. 앱의 최종 사용자가 자체 데이터에 대한 액세스 권한을 부여할 수 있도록 안전한 'Google 계정으로 로그인' 흐름을 추가합니다.

### 지원되는 앱

다음 Google Workspace 앱을 사용할 수 있습니다.

| 앱 | 빌드할 수 있는 항목 |
| --- | --- |
| Google Calendar | 일정 및 캘린더 읽기, 만들기, 관리 |
| Google Chat | 대화 및 그룹 스페이스 읽기 및 상호작용 |
| Google Docs | 문서 만들기, 읽기, 업데이트, 서식 지정 |
| Google Drive | 파일 및 폴더 정리, 검색, 관리 |
| Google Forms | 설문조사 만들기, 질문 업데이트, 응답 검색 |
| Gmail | 이메일 콘텐츠 읽기, 보내기, 관리 |
| Google Keep | 노트, 목록, 첨부파일 관리 |
| Google Meet | 영상 통화 예약 및 관리 |
| 연락처 | 연락처 동기화 및 관리 |
| Google Sheets | 스프레드시트 데이터 읽기, 쓰기, 서식 지정 |
| Google Slides | 프레젠테이션 만들기 및 수정 |
| Google Tasks | 작업 만들기, 관리, 정리 |

### 인증 및 권한

빌더는 OAuth 클라이언트를 구성하거나, 사용자 인증 정보를 관리하거나, Google Cloud 프로젝트를 설정할 필요가 없습니다. AI Studio에서 이 모든 작업을 처리합니다.

Workspace API가 통합된 앱은 'Google 계정으로 로그인'을 사용하여 최종 사용자를 인증합니다. 사용자가 앱을 열면 로그인하고 앱에 필요한 특정 권한 (예: 캘린더에 대한 읽기 전용 액세스 권한 또는 스프레드시트를 수정하는 기능)을 부여하라는 메시지가 표시됩니다. 앱은 앱을 사용하는 사람의 데이터에만 액세스합니다. 각 사용자는 자신의 계정에 대한 액세스 권한을 부여합니다.

### 프롬프트 예시

다음은 Workspace 통합을 시작하는 데 도움이 되는 몇 가지 아이디어입니다.

- *"내 Google Calendar를 읽고 각 회의에 대한 준비 이메일을
  Gmail에서 작성하는 앱을 빌드해 줘."*
- *"Google Docs를 가져와 Google Slides에서 5페이지 요약
  프레젠테이션을 생성하는 도구를 만들어 줘."*
- *"영수증을 업로드하면 Gemini가 세부정보를 추출하고 내 Google Sheets에 새 행을 기록하는 비용 추적기를 만들어 줘."*

### OAuth 설정

보안 비밀 관리의 주요 사용 사례 중 하나는 OAuth를 설정하여 다른 웹사이트 또는 앱에 연결하는 것입니다. 프롬프트에 OAuth 인증이 필요한 서드 파티 앱에 연결하는 방법에 관한 안내가 포함되어 있으면 에이전트가 해당 애플리케이션에 OAuth를 설정하는 방법을 안내합니다. 이 안내에는 OAuth 애플리케이션을 구성하는 데 필요한 콜백 URL이 포함됩니다.
설정 패널의 **통합** 에서 콜백 URL을 찾을 수도 있습니다.

## 멀티플레이어 환경 빌드

풀 스택 런타임은 실시간 공동작업 기능을 지원합니다.

- **실시간 상태**: 에이전트에게 "실시간
  채팅", "공동 화이트보드" 또는 "멀티플레이어 게임"과 같은 기능을 빌드해 달라고 요청할 수 있습니다.
- **동기화된 세션**: 서버가 상태를 관리하므로 여러 사용자가
  동일한 애플리케이션 인스턴스와 실시간으로 상호작용할 수 있습니다.

**프롬프트 예시**: > "플레이어가 서로의 커서를 볼 수 있는 멀티플레이어 게임을 만들어 줘."

### 멀티플레이어 앱 테스트를 위한 도움말

앱을 배포하기 전에 두 가지 방법으로 멀티플레이어 모드를 테스트할 수 있습니다.

1. 여러 탭에서 Google AI Studio 빌드 모드로 앱을 엽니다. 빌드 모드에서 개발할 때 앱은 개발 컨테이너에 있습니다. 여러 탭에서 앱을 열면 앱을 사용하는 여러 플레이어를 시뮬레이션할 수 있습니다.
2. 오른쪽 상단의 **공유** 메뉴를 사용하여 다른 사용자와 앱을 공유합니다. 그런 다음 **공유** 메뉴의 **통합** 탭에서 **공유 URL** 을 사용하여 앱을 공유한 플레이어와 함께 앱을 사용합니다.

## 권장사항

- **Gemini API 호출**: `GEMINI_API_KEY`는
  서버 측 보안 비밀로 자동 구성됩니다. 이 키를 사용하여 서버 측 코드에서 Gemini API를 호출합니다. **보안 비밀** 패널에서 볼 수 있습니다.
- **보안 비밀 보안**: 민감한 키에는 항상 보안 비밀 관리자를 사용합니다.
  파일에 하드 코딩하지 마세요.
- **관심사 분리**: UI 로직은 클라이언트 측 프레임워크
  (React/Angular)에, 비즈니스 로직/데이터 처리는 서버 측에 유지합니다.
- **오류 처리**: 앱이 비정상 종료되지 않도록 서버 측 코드가 외부 API 호출의 오류를
  강력하게 처리하는지 확인합니다.

## 다음 단계

- [Google AI Studio에서 앱 빌드](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko)
- [Google AI Studio에서 배포](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ko)
- [앱 갤러리](https://aistudio.google.com/apps?source=showcase&hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-08-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-08-19(UTC)"],[],[]]
