---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=ko
fetched_at: 2026-05-05T13:10:46.143526+00:00
title: "Gemini API \ub77c\uc774\ube0c\ub7ec\ub9ac \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/문서)

의견 보내기

# Gemini API 라이브러리

Gemini API로 빌드할 때는 **Google 생성형 AI SDK** 를 사용하는 것이 좋습니다.
Google 생성형 AI SDK는 가장 널리 사용되는 프로그래밍 언어용으로 Google에서 개발 및 유지보수하는 프로덕션에 즉시 사용 가능한 공식 라이브러리입니다. [정식 버전으로 제공되며 모든 공식
문서 및 예에서 사용됩니다.](https://ai.google.dev/gemini-api/docs/정식 버전으로 제공되며 모든 공식문서 및 예에서 사용됩니다.)

Gemini API를 처음 사용하는 경우 [빠른 시작 가이드](https://ai.google.dev/gemini-api/docs/빠른 시작 가이드)에 따라 시작하세요.

## 언어 지원 및 설치

Google 생성형 AI SDK는 Python, JavaScript/TypeScript, Go, Java 언어로 제공됩니다. 패키지 관리자를 사용하여 각 언어의 라이브러리를 설치하거나 GitHub 저장소를 방문하여 추가로 참여할 수 있습니다.

### Python

- 라이브러리: [`google-genai`](https://ai.google.dev/gemini-api/docs/`google-genai`)
- GitHub 저장소: [googleapis/python-genai](https://ai.google.dev/gemini-api/docs/googleapis/python-genai)
- 설치: `pip install google-genai`

### JavaScript

- 라이브러리: [`@google/genai`](https://ai.google.dev/gemini-api/docs/`@google/genai`)
- GitHub 저장소: [googleapis/js-genai](https://ai.google.dev/gemini-api/docs/googleapis/js-genai)
- 설치: `npm install @google/genai`

### Go

- 라이브러리: [`google.golang.org/genai`](https://ai.google.dev/gemini-api/docs/`google.golang.org/genai`)
- GitHub 저장소: [googleapis/go-genai](https://ai.google.dev/gemini-api/docs/googleapis/go-genai)
- 설치: `go get google.golang.org/genai`

### Java

- 라이브러리: `google-genai`
- GitHub 저장소: [googleapis/java-genai](https://ai.google.dev/gemini-api/docs/googleapis/java-genai)
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
- GitHub 저장소: [googleapis/dotnet-genai](https://ai.google.dev/gemini-api/docs/googleapis/dotnet-genai)
- 설치: `dotnet add package Google.GenAI`

## 정식 버전

2025년 5월을 기준으로 Google 생성형 AI SDK는 지원되는 모든 플랫폼에서 정식 버전 (GA)에 도달했으며 Gemini API에 액세스하는 데 권장되는 라이브러리입니다.
안정적이고 프로덕션 용도로 완전히 지원되며 적극적으로 유지보수됩니다.
최신 기능에 대한 액세스를 제공하며 Gemini와 함께 작업할 때 최고의 성능을 제공합니다.

기존 라이브러리 중 하나를 사용하고 있다면 최신 기능에 액세스하고 Gemini와 함께 작업할 때 최고의 성능을 얻을 수 있도록 마이그레이션하는 것이 좋습니다. 자세한 내용은 [기존 라이브러리](https://ai.google.dev/gemini-api/docs/기존 라이브러리) 섹션을 검토하세요.

## 기존 라이브러리 및 마이그레이션

기존 라이브러리 중 하나를 사용하고 있다면 새 라이브러리로 마이그레이션하는 것이 좋습니다.

기존 라이브러리는 최신 기능 (예:
[Live API](https://ai.google.dev/gemini-api/docs/Live API) 및 [Veo](https://ai.google.dev/gemini-api/docs/Veo))에 대한 액세스를 제공하지 않으며
2025년 11월 30일에 지원 중단됩니다.

각 기존 라이브러리의 지원 상태는 다음 표에 자세히 설명되어 있습니다.

| 언어 | 기존 라이브러리 | 지원 상태 | 권장 라이브러리 |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | 적극적으로 유지보수되지 않음 | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | 적극적으로 유지보수되지 않음 | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | 적극적으로 유지보수되지 않음 | `google.golang.org/genai` |
| **Dart 및 Flutter** | `google_generative_ai` | 적극적으로 유지보수되지 않음 | [Genkit Dart](https://ai.google.dev/gemini-api/docs/Genkit Dart) 또는 [Firebase AI Logic](https://ai.google.dev/gemini-api/docs/Firebase AI Logic) 사용 |
| **Swift** | `generative-ai-swift` | 적극적으로 유지보수되지 않음 | [Firebase AI Logic](https://ai.google.dev/gemini-api/docs/Firebase AI Logic) 사용 |
| **Android** | `generative-ai-android` | 적극적으로 유지보수되지 않음 | [Firebase AI Logic](https://ai.google.dev/gemini-api/docs/Firebase AI Logic) 사용 |

**Java 개발자 참고사항:** Gemini API용으로 Google에서 제공하는 기존 Java SDK가 없으므로 이전 Google 라이브러리에서 마이그레이션할 필요가 없습니다. [언어 지원 및 설치](https://ai.google.dev/gemini-api/docs/언어 지원 및 설치)
섹션의 새 라이브러리로 바로 시작할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?
