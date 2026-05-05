---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko
fetched_at: 2026-05-05T20:00:57.203500+00:00
title: "Google AI Studio\uc5d0\uc11c \ud480 \uc2a4\ud0dd \uc571 \uac1c\ubc1c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

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

`npm install`을 수동으로 실행할 필요가 없습니다. 에이전트에게 패키지가 필요한 기능을 추가해 달라고 요청하기만 하면 에이전트가 설치 및 가져오기를 처리합니다.

**예**: > "`axios`를 사용하여 외부 API에서 데이터를 가져옵니다."

## 보안 비밀 안전하게 관리

이제 서버 측 코드와 보안 비밀 관리를 통해 전 세계와 상호작용하는 앱을 빌드할 수 있습니다.

- **서드 파티 API**: Stripe, SendGrid 또는 커스텀
  REST API와 같은 서비스에 연결합니다.
- **데이터베이스**: 외부 데이터베이스 (예: Supabase, Firebase,
  또는 MongoDB Atlas를 통해)에 연결하여 세션 외에 데이터를 유지합니다.

실제 앱을 빌드할 때는 API 키가 필요한 서드 파티 서비스(예: Twilio, Slack 또는 데이터베이스)에 연결해야 하는 경우가 많습니다. 다음 단계에 따라 키를 수동으로 추가할 수 있습니다.

1. **보안 비밀 추가**: Google AI Studio의 **설정** 메뉴로 이동하여 보안 비밀 섹션을 찾습니다.
2. **키 저장**: 여기에 API 키 또는 보안 비밀 토큰을 추가합니다.
3. **코드에서 액세스**: 에이전트는 이러한
   보안 비밀에 안전하게 액세스하는 서버 측 코드를 작성할 수 있습니다 (일반적으로 환경 변수를 통해). 이렇게 하면 보안 비밀이 클라이언트 측 브라우저에
   노출되지 않습니다.

필요한 경우 에이전트는 새 보안 비밀이 필요하거나 프로젝트의 env 변수에서 새 키가 감지될 때마다 키를 추가하라는 메시지를 표시하는 카드를 채팅에 표시합니다.

### 데이터베이스 및 인증을 위한 Firebase 통합

이제 Google AI Studio를 사용하면 Firebase 통합을 통해 앱에 데이터베이스 또는 인증을 쉽게 추가할 수 있습니다.
Antigravity 에이전트는 다음 서비스를 자동으로 프로비저닝하고 설정할 수 있습니다.

- **Firestore 데이터베이스**: 클라이언트 및 서버 측 개발을 위한 데이터를 저장하고 동기화하기 위한 유연하고 확장 가능한 NoSQL 클라우드 데이터베이스입니다.
- **Firebase 인증**: 사용자가 Google 계정으로 로그인 흐름을 사용하여 애플리케이션에 안전하게 로그인할 수 있도록 합니다.

에이전트에게 '앱에 데이터베이스 추가' 또는 'Google 로그인 설정'을 요청하기만 하면 에이전트가 필요한 구성 및 코드 생성을 처리합니다.

Firebase를 사용하면 무료로 시작할 수 있으며, 할당량을 늘리거나 유료 기능을 사용할 준비가 되면 유료 계정으로 확장할 수 있습니다.

### OAuth 설정

보안 비밀 관리의 주요 사용 사례 중 하나는 OAuth를 설정하여 다른 웹사이트 또는 앱에 연결하는 것입니다. 프롬프트에 OAuth 인증이 필요한 서드 파티 앱에 연결하는 방법에 관한 안내가 포함되어 있으면 에이전트가 해당 애플리케이션에 OAuth를 설정하는 방법을 안내합니다. 이 안내에는 OAuth 애플리케이션을 구성하는 데 필요한 콜백 URL이 포함됩니다.
콜백 URL은 설정 패널의 **통합** 에서도 찾을 수 있습니다.

## 멀티플레이어 환경 빌드

풀 스택 런타임은 실시간 공동작업 기능을 지원합니다.

- **실시간 상태**: 에이전트에게 "실시간
  채팅", "공동 화이트보드" 또는 "멀티플레이어 게임"과 같은 기능을 빌드해 달라고 요청할 수 있습니다.
- **동기화된 세션**: 서버가 상태를 관리하므로 여러 사용자가
  동일한 애플리케이션 인스턴스와 실시간으로 상호작용할 수 있습니다.

**프롬프트 예시**: > "플레이어가 서로의 커서를 볼 수 있는 멀티플레이어 게임으로 만들어 줘."

### 멀티플레이어 앱 테스트를 위한 팁

앱을 배포하기 전에 두 가지 방법으로 멀티플레이어 모드를 테스트할 수 있습니다.

1. 여러 탭에서 Google AI Studio 빌드 모드로 앱을 엽니다. 빌드 모드에서 개발할 때 앱은 개발 컨테이너에 있습니다. 여러 탭에서 앱을 열면 앱을 사용하는 여러 플레이어를 시뮬레이션할 수 있습니다.
2. 오른쪽 상단의 **공유** 메뉴를 사용하여 다른 사용자와 앱을 공유합니다. 그런 다음 **공유** 메뉴의 **통합** 탭에서 **공유 URL** 을 사용하여 앱을 공유한 플레이어와 함께 앱을 사용합니다.

## 권장사항

- **보안 비밀 보안**: 민감한 키에는 항상 보안 비밀 관리자를 사용합니다.
  파일에 하드 코딩하지 마세요.
- **관심사 분리**: UI 로직은 클라이언트 측 프레임워크
  (React/Angular)에, 비즈니스 로직/데이터 처리는 서버 측에 유지합니다.
- **오류 처리**: 서버 측 코드가 외부 API 호출의 오류를 강력하게 처리하여 앱이 비정상 종료되지 않도록 합니다.

## 다음 단계

- [Google AI Studio에서 앱 빌드](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko)
- [앱 갤러리](https://aistudio.google.com/apps?source=showcase&hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
