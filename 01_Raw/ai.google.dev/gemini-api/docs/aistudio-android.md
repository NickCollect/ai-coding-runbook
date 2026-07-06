---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=ko
fetched_at: 2026-07-06T05:12:40.730683+00:00
title: "Google AI Studio\uc5d0\uc11c Android \uc571 \ube4c\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google AI Studio에서 Android 앱 빌드

Google AI Studio를 사용하면 자연어 프롬프트에서 네이티브 Android 앱을 빌드할 수 있습니다. 원하는 앱을 설명하면
[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko#antigravity-agent)
가 완전한 Kotlin 및 [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=ko)
프로젝트를 생성합니다. 브라우저에서 브라우저 기반 Android 에뮬레이터에서 앱을 미리 보고, 실제 기기에 설치하고, 테스트를 위해 게시할 수 있습니다.

## 시작하기

Android 앱 빌드를 시작하려면 다음 단계를 따르세요.

1. 왼쪽 탐색 패널을 사용하여 Google AI Studio의 [빌드 모드](https://aistudio.google.com/apps?hl=ko)로 이동합니다.
2. 플랫폼 선택 도구에서 **Android** 를 선택합니다.
3. 빌드하려는 앱을 설명하는 프롬프트를 입력합니다 (예: *"로컬 저장소가 있는 일일 작업 현황표 만들기"* 또는 *"간단한 계산기 빌드"*).
4. 에이전트가 프로젝트를 생성하고 브라우저 기반 Android 에뮬레이터에서 실행합니다.

그런 다음 웹 환경과 마찬가지로 채팅 패널을 사용하여 앱을 반복할 수 있습니다. 에이전트는 Android 프로젝트의 모든 파일을 관리하고 코드베이스 전반에 변경사항을 전파합니다.

## 브라우저 기반 Android 에뮬레이터

Android 에뮬레이터는 클라우드에서 완전히 실행되고 브라우저로 스트리밍됩니다.
Android SDK, Android 스튜디오 또는 로컬 에뮬레이터를 설치할 필요가 없습니다.

에뮬레이터는 다음을 제공합니다.

- **Pixel과 유사한 기기 시뮬레이션**: 실제 기기에서와 마찬가지로 앱을 탭하고 스크롤하고 상호작용합니다.
- **회전 지원**: 세로 모드와 가로 모드 간에 전환합니다.
- **실시간 미리보기**: 에이전트가 코드를 변경하면 앱이 다시 빌드되고
  에뮬레이터가 자동으로 새로고침됩니다.

### 에뮬레이터 제한사항

브라우저 기반 에뮬레이터는 모든 하드웨어 기능을 지원하지 않습니다. 에뮬레이터에서는 다음을 사용할 수 없습니다.

- 카메라 및 사진 캡처
- NFC 및 블루투스
- GPS (위치가 시뮬레이션됨)
- Google Play 서비스 (Google 로그인, 지도, 기타 Play 서비스 기능은 실제 기기에서 작동하지만 에뮬레이터에서는 작동하지 않음)

## ADB가 있는 기기에 설치

USB를 사용하여 컴퓨터에 연결된 실제 Android 기기에 빌드된 APK를 직접 설치할 수 있습니다. 이 방법은
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=ko)를 사용하여
브라우저를 통해 기기와 통신합니다. 로컬 ADB 설치는 필요하지 않습니다.

### 기본 요건

- WebUSB를 지원하는 Chrome 또는 Edge 브라우저
- [개발자 옵션 및 USB 디버깅이 사용 설정된 Android 기기](https://developer.android.com/studio/debug/dev-options?hl=ko)
- 기기를 컴퓨터에 연결하는 USB 케이블

### 기기에 앱 설치

1. 미리보기 패널에서 **기기에 설치** 를 클릭합니다.
2. 브라우저의 USB 기기 선택 도구에서 Android 기기를 선택합니다.
3. APK가 전송되어 기기에 설치됩니다.
4. 앱이 자동으로 실행됩니다.

## Play 스토어에 게시

Android 앱을
[Google Play Console](https://play.google.com/console?hl=ko) 내부
테스트 트랙에 게시하여 최대 100명의 테스터에게 앱을 배포할 수 있습니다.

### 기본 요건

- [Google Play 개발자 계정](https://play.google.com/console/signup?hl=ko)
  (일회성 등록 수수료 25달러 필요)
- Play Console에서 개발자 프로필을 작성해야 합니다.

### 앱 게시

1. Google AI Studio에서 **설정 > 게시** 를 엽니다.
2. **Play 스토어에 게시** 를 클릭합니다.
3. Google Play 개발자 계정으로 인증합니다.
4. AI Studio에서 APK에 서명하고, 앱 등록정보를 만들거나 새 버전을 업로드하고, 내부 테스트 트랙에 게시합니다.
5. 테스터와 공유할 링크를 받습니다.

AI Studio는 관리형 키 저장소를 사용하여 APK 서명을 자동으로 관리합니다. 나중에 Play Console에서 앱 등록정보 (아이콘, 스크린샷, 설명)를 맞춤설정할 수 있습니다.

## 생성되는 항목

Android 앱을 빌드하면 에이전트가 다음과 같은 구조의 표준 Gradle 기반 프로젝트를 생성합니다.

- **빌드 구성**: `build.gradle.kts` 파일 (프로젝트 및 앱 수준)
  Kotlin DSL 사용
- **UI 레이어**: [Material 3](https://developer.android.com/develop/ui/compose?hl=ko) 테마가 적용된 [Jetpack Compose](https://m3.material.io/) 구성요소
- **아키텍처**: ViewModel 및 데이터
  클래스가 있는 단일 활동 아키텍처
- **리소스**: `AndroidManifest.xml`, 드로어블, 문자열, 기타 Android
  리소스

에이전트는 필요에 따라 Maven 및 Google 저장소에서 패키지를 추가하여 Gradle 종속 항목을 자동으로 관리합니다.

미리보기 패널의 **코드** 탭을 사용하여 생성된 코드를 보고 수정할 수 있습니다. Android 스튜디오에서 개발을 계속하려면 프로젝트를 **ZIP 파일** 로 다운로드하세요.

## 제한사항

AI Studio의 Android 앱 빌드에는 다음과 같은 제한사항이 있습니다.

### 플랫폼 제한사항

- **클라이언트 측 전용**: Android 앱에는 서버 측 구성요소가 포함되지 않습니다.
  서버 런타임 (보안 비밀 관리, 멀티플레이어, Firebase, Google Workspace API)이 필요한 기능은 사용할 수 없습니다.
- **단일 활동 아키텍처**: 단일 활동, 단일 모듈
  프로젝트만 지원됩니다.
- **Jetpack Compose 전용**: 앱은 Kotlin 및 Jetpack Compose를 사용합니다. 자바 및 XML 레이아웃은 지원되지 않습니다.
- **NDK 또는 네이티브 코드 없음**: C 및 C++ 코드는 지원되지 않습니다.
- **Wear OS 또는 Android TV 없음**: 휴대전화 및 태블릿 폼 팩터만
  지원됩니다.

### 내보내기 제한사항

- **ZIP 다운로드만 가능**: 프로젝트를 ZIP 파일로 다운로드할 수 있습니다. Android 프로젝트에는 아직 GitHub 내보내기를 사용할 수 없습니다.

## 다음 단계

- [Google AI Studio에서 앱 빌드](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko)
- [전체 스택 앱 개발](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko) (웹)
- [앱 갤러리](https://aistudio.google.com/apps?source=showcase&hl=ko)에서 예시 보기

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-19(UTC)"],[],[]]
