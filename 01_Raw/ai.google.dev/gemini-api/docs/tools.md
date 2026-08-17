---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=ko
fetched_at: 2026-08-17T02:24:28.999019+00:00
title: "Gemini API\ub85c \ub3c4\uad6c \uc0ac\uc6a9 \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API로 도구 사용

도구를 사용하면 Gemini 모델의 기능을 확장하여 실제 세계에서 조치를 취하고, 실시간 정보에 액세스하고, 복잡한 계산 작업을 실행할 수 있습니다. 모델은 표준 요청-응답 상호작용과
[Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko)를 사용하는 실시간 스트리밍 세션 모두에서 도구를 사용할 수 있습니다.

도구는 모델이 쿼리에 대답하는 데 사용할 수 있는 특정 기능 (예: Google 검색 또는 코드 실행)입니다. Gemini API는 완전
관리형 기본 제공 도구 모음을 제공하거나 [함수
호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)을 사용하여 커스텀 도구를 정의할 수 있습니다.

다단계의 목표 지향 시스템을 빌드하려면 [에이전트
개요](https://ai.google.dev/gemini-api/docs/agents?hl=ko)를 참고하세요.

## 사용 가능한 기본 제공 도구

| 도구 | 설명 | 사용 사례 |
| --- | --- | --- |
| [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) | 웹의 최신 이벤트와 사실에 대답을 그라운딩하여 할루시네이션을 줄입니다. | 최근 이벤트에 관한 질문에 대답하고 다양한 소스로 사실을 확인합니다. |
| [Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko) | 장소를 찾고, 길을 찾고, 풍부한 지역 컨텍스트를 제공할 수 있는 위치 인식 어시스턴트를 빌드합니다. | 여러 정류장이 있는 여행 일정을 계획하고 사용자 기준에 따라 지역 비즈니스를 찾습니다. |
| [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko) | 모델이 Python 코드를 작성하고 실행하여 수학 문제를 해결하거나 데이터를 정확하게 처리할 수 있도록 합니다. | 복잡한 수학 방정식을 풀고 텍스트 데이터를 정확하게 처리하고 분석합니다. |
| [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko) | 모델이 특정 웹페이지 또는 문서의 콘텐츠를 읽고 분석하도록 안내합니다. | 특정 URL 또는 문서를 기반으로 질문에 대답하고 여러 웹페이지에서 정보를 검색합니다. |
| [컴퓨터 사용 (미리보기)](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko) | Gemini가 화면을 보고 웹브라우저 UI와 상호작용하는 작업을 생성할 수 있도록 합니다 (클라이언트 측 실행). | 반복적인 웹 기반 워크플로를 자동화하고 웹 애플리케이션 사용자 인터페이스를 테스트합니다. |
| [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) | 자체 문서를 색인 생성하고 검색하여 검색 증강 생성 (RAG)을 사용 설정합니다. | 기술 매뉴얼을 검색하고 독점 데이터에 대해 질의 응답합니다. |

특정 도구와 관련된 비용에 관한 자세한 내용은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#pricing_for_tools)
를 참고하세요.

## 도구 실행 작동 방식

도구를 사용하면 모델이 대화 중에 작업을 요청할 수 있습니다. 도구가 기본 제공 (Google에서 관리)인지 커스텀 (사용자가 관리)인지에 따라 흐름이 다릅니다.

### 기본 제공 도구 흐름

기본 제공 도구 (Google 검색, Google 지도, URL 컨텍스트, 파일 검색, 코드 실행)의 경우 전체 프로세스가 하나의 API 호출 내에서 발생합니다.

1. **사용자** 가 'GOOG의 최신 주가는 얼마인가요?'라는 프롬프트를 보냅니다.
2. **Gemini** 는 도구가 필요하다고 판단하고 Google 서버에서 도구를 실행합니다(예: 주가를 검색한 다음 Python 코드를 실행하여 제곱근을 계산).
3. **Gemini** 는 도구 결과를 기반으로 최종 대답을 다시 보냅니다.

### 커스텀 도구 흐름 (함수 호출)

커스텀 도구 및 컴퓨터 사용의 경우 애플리케이션에서 실행을 처리합니다.

1. **사용자** 가 함수 (도구) 선언과 함께 프롬프트를 보냅니다.
2. **Gemini** 는 항상 고유한 `id`와 함께 특정 함수를 호출하기 위해 구조화된 JSON을 다시 보낼 수 있습니다
   (예: `{"name": "get_order_status", "args": {"order_id": "123"}}`)
   .
3. **사용자** 가 애플리케이션 또는 환경에서 함수를 실행합니다.
4. **사용자** 가 함수 호출과 동일한 `id`로 함수 결과를 Gemini에 다시 보냅니다.
5. **Gemini** 는 결과를 사용하여 최종 대답 또는 다른 도구 호출을 생성합니다.

자세한 내용은 [함수 호출 가이드](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)를 참고하세요.

### 기본 제공 도구와 커스텀 도구 흐름 결합

[기본 제공 도구와 커스텀 도구 (함수 호출)를 결합하는 요청의 경우 모델은 도구 컨텍스트 순환을 사용하여 여러 환경에서 실행을 조정합니다.](https://ai.google.dev/gemini-api/docs/toold-combination?hl=ko)

1. **사용자** 가 프롬프트를 보내고 사용 설정하려는 기본 제공 도구와 커스텀 함수를 선언하여 조합 지원을 사용 설정하는 플래그를 설정합니다.
2. **Gemini** 는 기본 제공 도구를 실행하고 클라이언트 측 함수 호출이 생성되면 사용자에게 양보합니다 (먼저 실행되는 것은 프롬프트와 모델이 결정하는 내용에 따라 다름). 다음과 같은 대답을 다시 보냅니다.
   - 도구 호출 확인
   - 도구 대답 결과 (모델이 두 개의 병렬 함수 호출을 생성한 경우 JSON 다음에 올 수 있음)
   - 함수를 호출하는 구조화된 JSON
   - 컨텍스트를 보존하기 위한 암호화된 생각 서명
3. **사용자** 가 애플리케이션 또는 환경에서 함수를 실행합니다.
4. **사용자** 가 Gemini의 대답과 함수 호출 결과의 모든 부분을 반환합니다.
5. **Gemini** 는 결합된 모든 컨텍스트를 사용하여 최종 대답을 생성합니다.

기본 제공 도구와 커스텀 도구 조합 지원을 사용 설정하는 방법과 컨텍스트 순환 예시는 [도구 조합 가이드](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)를 참고하세요.

## 구조화된 출력과 함수 호출 비교

Gemini는 구조화된 출력을 생성하는 두 가지 방법을 제공합니다. 모델이 자체 도구 또는 데이터 시스템에 연결하여 중간 단계를 실행해야 하는 경우 [함수
호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)을 사용합니다. 모델의 최종 대답이 특정 스키마를 엄격하게 준수해야 하는 경우(예: 커스텀 UI 렌더링)
[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)을 사용합니다.

## 도구를 사용한 구조화된 출력

[구조화된 출력을 기본 제공 도구와 결합하여 외부 데이터 또는 계산을 기반으로 하는 모델 대답이 엄격한 스키마를 계속 준수하도록 할 수 있습니다.](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)

코드 예시는 [도구를 사용한 구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=ko#structured_outputs_with_tools)
을 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-31(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-31(UTC)"],[],[]]
