---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=ko
fetched_at: 2026-06-08T05:38:25.908662+00:00
title: "Gemini API \ub77c\uc774\ube0c\ub7ec\ub9ac \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 라이브러리

Gemini API로 빌드할 때는 **Google 생성형 AI SDK**를 사용하는 것이 좋습니다.
프로덕션에 즉시 사용 가능한 공식 라이브러리인 Google 생성형 AI SDK는 가장 널리 사용되는 프로그래밍 언어용으로 개발 및 유지보수됩니다. [일반 제공](https://ai.google.dev/gemini-api/docs/libraries?hl=ko#new-libraries)되며 모든 공식 문서와 예시에 사용됩니다.

Gemini API를 처음 사용하는 경우 [빠른 시작 가이드](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)에 따라 시작하세요.

## 언어 지원 및 설치

Google GenAI SDK는 Python, JavaScript/TypeScript, Go, Java 언어로 제공됩니다. 패키지 관리자를 사용하여 각 언어의 라이브러리를 설치하거나 GitHub 저장소를 방문하여 자세히 알아볼 수 있습니다.

### Python

- 라이브러리: [`google-genai`](https://pypi.org/project/google-genai)
- GitHub 저장소: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- 설치: `pip install google-genai`

### 자바스크립트

- 라이브러리: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- GitHub 저장소: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- 설치: `npm install @google/genai`

### Go

- 라이브러리: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- GitHub 저장소: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- 설치: `go get google.golang.org/genai`

### 자바

- 라이브러리: `google-genai`
- GitHub 저장소: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- 설치: Maven을 사용하는 경우 종속 항목에 다음을 추가합니다.

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- 라이브러리: `Google.GenAI`
- GitHub 저장소: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- 설치: `dotnet add package Google.GenAI`

## 정식 버전

2025년 5월 현재 Google GenAI SDK는 지원되는 모든 플랫폼에서 정식 버전 (GA)에 도달했으며 Gemini API에 액세스하는 데 권장되는 라이브러리입니다.
안정적이고 프로덕션 용도로 완전히 지원되며 적극적으로 유지 관리됩니다.
최신 기능에 액세스할 수 있으며 Gemini와 함께 작동할 때 최고의 성능을 제공합니다.

기존 라이브러리 중 하나를 사용하는 경우 Gemini를 사용하여 최신 기능에 액세스하고 최상의 성능을 얻을 수 있도록 마이그레이션하는 것이 좋습니다. 자세한 내용은 [기존 라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko#previous-sdks) 섹션을 참고하세요.

## 기존 라이브러리 및 이전

기존 라이브러리 중 하나를 사용하는 경우 [새 라이브러리로 마이그레이션](https://ai.google.dev/gemini-api/docs/migrate?hl=ko)하는 것이 좋습니다.

기존 라이브러리는 최신 기능 (예: [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko) 및 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ko))에 대한 액세스를 제공하지 않으며 2025년 11월 30일부로 지원 중단됩니다.

각 기존 라이브러리의 지원 상태는 다음 표에 자세히 설명되어 있습니다.

| 언어 | 기존 라이브러리 | 지원 상태 | 권장 라이브러리 |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | 활성 상태로 유지되지 않음 | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | 활성 상태로 유지되지 않음 | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | 활발하게 유지되지 않음 | `google.golang.org/genai` |
| **Dart 및 Flutter** | `google_generative_ai` | 활발하게 유지되지 않음 | [Genkit Dart](https://genkit.dev/docs/dart/get-started/) 또는 [Firebase AI Logic](https://pub.dev/packages/firebase_ai) 사용 |
| **Swift** | `generative-ai-swift` | 활성 상태로 유지되지 않음 | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ko) 사용 |
| **Android** | `generative-ai-android` | 활발하게 유지되지 않음 | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ko) 사용 |

**Java 개발자 참고:** Gemini API용 기존 Google 제공 Java SDK가 없으므로 이전 Google 라이브러리에서 이전할 필요가 없습니다. [언어 지원 및 설치](#install) 섹션에서 새 라이브러리를 바로 시작할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-28(UTC)"],[],[]]
