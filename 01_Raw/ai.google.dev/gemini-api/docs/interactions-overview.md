---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko
fetched_at: 2026-07-27T04:34:55.247109+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Interactions API

Interactions API는 Gemini 모델 및 에이전트로 빌드하는 가장 좋은 방법입니다. 2026년 6월부터 정식 버전으로 제공되며 모든 신규 프로젝트에 권장됩니다. 이제 기존 [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ko) API는 레거시로 간주되지만 계속해서 완벽하게 지원됩니다.

## Interactions API를 사용해야 하는 이유

- **모든 애플리케이션을 위한 범용 인터페이스**: 싱글턴 텍스트 생성, 멀티모달 이해, 구조화된 출력, 도구 오케스트레이션, 에이전트 워크플로 등 모든 사용 사례를 위한 표준 인터페이스로 설계되었습니다.
- **모델 및 에이전트를 위한 단일 API**: 표준 Gemini 모델과 전문 에이전트 (예: Deep Research 및 맞춤 관리 에이전트)를 직접 호출하기 위한 통합 엔드포인트 및 패턴입니다.
- **기본 제공되는 새로운 기능**: `previous_interaction_id`를 사용하는 선택적 서버 측 대화 상태, 디버깅 및 UI 렌더링을 위한 관찰 가능한 실행 단계, `background=true`를 사용하는 장기 실행 작업을 위한 [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)과 같은 기능
- **높은 캐시 적중률로 비용 절감**: 멀티턴 대화를 사용할 때 선택적 서버 측 상태 관리를 사용하면 턴 간에 더 효율적인 컨텍스트 캐싱이 가능해 토큰 비용이 절감됩니다.
- **새 기능 출시 위치**: 앞으로 모든 새로운 모델, 멀티모달 기능, 도구, 에이전트 기능은 Interactions API에서 출시됩니다.

기본적으로 Interactions API는 요청을 저장하므로 `previous_interaction_id`를 사용하여 서버 측 상태 관리 기능을 활용할 수 있습니다. `store=false`를 설정하여 상태 비저장 동작을 선택할 수 있습니다. 자세한 내용은 [데이터 보관](#data-storage-retention) 섹션을 참고하세요.

## 시작하기

- **코딩 에이전트 설정**: **Gemini Docs MCP**에 연결하고 `gemini-interactions-api` 스킬을 설치하여 어시스턴트가 최신 개발자 문서와 권장사항에 직접 액세스할 수 있도록 합니다. 자세한 단계는 [코딩 에이전트 설정 가이드](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko)를 참고하세요.
- **`generateContent`에서 이전**: 기존 통합이 있는 경우 [이전 가이드](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ko)에 따라 Interactions API로 전환하세요.
- **시작하기**: [Interactions API 시작하기 가이드](https://ai.google.dev/gemini-api/docs/get-started?hl=ko)의 단계를 따릅니다.

### 기능 가이드

이 가이드를 통해 Interactions API의 구체적인 기능을 살펴보세요. 이 페이지의 전환 버튼을 사용하여 generateContent API와 Interactions API 간에 전환할 수 있습니다.

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko)
- [이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)
- [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko)
- [오디오 이해](https://ai.google.dev/gemini-api/docs/audio?hl=ko)
- [동영상 이해](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko)
- [문서 처리](https://ai.google.dev/gemini-api/docs/document-processing?hl=ko)
- [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)
- [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)
- [Deep Research 에이전트](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)
- [유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)
- [우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)

## Interactions API 작동 방식

Interactions API는 핵심 리소스인 [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ko#Resource:Interaction)를 중심으로 합니다. `Interaction`는 대화 또는 작업의 완전한 턴을 나타냅니다. **실행 단계**의 시간순서로 상호작용의 전체 기록을 포함하는 세션 레코드 역할을 합니다. 이러한 단계에는 모델 생각, 서버 측 또는 클라이언트 측 도구 호출 및 결과 (예: `function_call` 및 `function_result`), 최종 `model_output`가 포함됩니다. 저장된 리소스 (`interactions.get`를 통해 검색됨)에는 전체 컨텍스트를 위한 `user_input` 단계도 포함되지만 `interactions.create` 응답은 모델 생성 단계만 반환합니다.

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ko#CreateInteraction)에 대한 호출을 하면 새 `Interaction` 리소스가 생성됩니다.

### 서버 측 상태 관리

`previous_interaction_id` 매개변수를 사용하여 후속 호출에서 완료된 상호작용의 `id`를 사용하여 대화를 계속할 수 있습니다. 서버는 이 ID를 사용하여 대화 기록을 가져오므로 전체 채팅 기록을 다시 보낼 필요가 없습니다.

`previous_interaction_id` 파라미터는 `previous_interaction_id`를 사용하여 대화 기록 (입력 및 출력)만 보존합니다. 다른 매개변수는 **상호작용 범위**이며 현재 생성 중인 특정 상호작용에만 적용됩니다.

- `tools`
- `system_instruction`
- `generation_config` (`thinking_level`, `temperature` 등 포함)

즉, 이러한 매개변수를 적용하려면 새 상호작용마다 다시 지정해야 합니다. 이 서버 측 상태 관리는 선택사항입니다. 각 요청에서 전체 대화 기록을 전송하여 상태 비저장 모드로 작동할 수도 있습니다.

### 데이터 스토리지 및 보관

기본적으로 API는 서버 측 상태 관리 기능 (`previous_interaction_id` 사용), [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko) (`background=true` 사용) 및 관측 가능성 목적의 사용을 간소화하기 위해 모든 상호작용 객체 (`store=true`)를 저장합니다.

- **유료 등급**: 시스템에서 상호작용을 **55일** 동안 보관합니다.
- **무료 등급**: 시스템에서 **1일** 동안 상호작용을 보관합니다.

이를 원치 않는 경우 요청에서 `store=false`를 설정하면 됩니다. 이 컨트롤은 상태 관리와 별개이며 모든 상호작용에 대해 저장소를 선택 해제할 수 있습니다. 하지만 `store=false`은 [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)과 호환되지 않으며 후속 턴에 `previous_interaction_id`을 사용할 수 없습니다.

유료 등급 프로젝트의 경우 [AI Studio](https://aistudio.google.com/logs?hl=ko)에서 보관 기간을 구성하여 7일, 14일, 28일 또는 55일 후에 프로젝트 스토리지에서 삭제할 로그를 자동으로 표시할 수 있습니다. 보관 기간이 짧으면 이전 대화 검색에 영향을 미칠 수 있습니다.

상호작용 ID가 필요한 [`delete`](https://ai.google.dev/api/interactions-api?hl=ko#deleteInteraction) 메서드를 프로그래매틱 방식으로 사용하여 언제든지 저장된 상호작용을 삭제할 수 있습니다. [AI Studio](https://aistudio.google.com/logs?hl=ko)에서 프로젝트 스토리지에서의 삭제를 비롯한 저장된 상호작용 로그를 확인하고 관리할 수도 있습니다.

보관 기간이 만료되면 데이터가 자동으로 삭제됩니다.

상호작용 객체는 [약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 따라 처리됩니다.

### AI Studio에서 상호작용 보기

API는 유료 등급 프로젝트에 대해 `store=true`로 실행된 Interactions API 요청을 저장합니다. [Google AI Studio의 로그 페이지](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=ko)에서 직접 확인할 수 있습니다. 자세한 내용은 [로그 가이드](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko)를 참고하세요.

## 권장사항

- **캐시 적중률**: 암시적 캐싱은 스테이트풀 모드와 스테이트리스 모드 모두에서 지원됩니다 ([빠른 시작](https://ai.google.dev/gemini-api/docs/get-started?hl=ko#4_multi-turn_conversations) 참고). `previous_interaction_id` (상태 저장)를 사용하여 대화를 계속하면 시스템에서 대화 기록에 대한 암시적 캐싱을 더 쉽게 활용할 수 있으므로 성능이 향상되고 비용이 절감됩니다.
- **상호작용 혼합**: 대화 내에서 에이전트와 모델 상호작용을 자유롭게 혼합할 수 있습니다. 예를 들어 심층 조사 에이전트와 같은 전문 에이전트를 사용하여 초기 데이터 수집을 수행한 다음 표준 Gemini 모델을 사용하여 요약 또는 재형식 지정과 같은 후속 작업을 수행하여 이러한 단계를 `previous_interaction_id`와 연결할 수 있습니다.

## 지원되는 모델 및 에이전트

| 모델 이름 | 유형 | 모델 ID |
| --- | --- | --- |
| Gemini 3.5 Flash | 모델 | `gemini-3.5-flash` |
| Gemini 3.1 Pro 프리뷰 | 모델 | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | 모델 | `gemini-3.1-flash-lite` |
| Gemini 3 Flash 프리뷰 | 모델 | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | 모델 | `gemini-2.5-pro` |
| Gemini 2.5 Flash | 모델 | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | 모델 | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | 모델 | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | 모델 | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS 프리뷰 | 모델 | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | 모델 | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | 모델 | `gemma-4-26b-a4b-it` |
| Lyria 3 클립 미리보기 | 모델 | `lyria-3-clip-preview` |
| Lyria 3 Pro 프리뷰 | 모델 | `lyria-3-pro-preview` |
| Deep Research 미리보기 | 에이전트 | `deep-research-preview-04-2026` |
| Deep Research 미리보기 | 에이전트 | `deep-research-max-preview-04-2026` |
| Antigravity 미리보기 | 에이전트 | `antigravity-preview-05-2026` |

## SDK

최신 버전의 Google 생성형 AI SDK를 사용하여 Interactions API에 액세스할 수 있습니다.

- Python에서는 `2.3.0` 버전부터 `google-genai` 패키지입니다.
- JavaScript에서는 `2.3.0` 버전부터 `@google/genai` 패키지입니다.

[라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 페이지에서 SDK를 설치하는 방법을 자세히 알아보세요.

## 제한사항

- **원격 MCP**: Gemini 3는 원격 MCP를 지원하지 않습니다. 곧 지원될 예정입니다.
- **멀티턴 모델 호환성**: 대화에서 서로 다른 모델 (상태 저장 또는 상태 비저장)을 혼합할 때 후속 모델은 이전 모델의 출력 모달리티를 입력으로 지원해야 합니다. 예를 들어 `gemini-3.1-flash-image`를 사용하여 이미지를 생성하는 경우 이미지 입력을 허용하지 않는 모델 (예: 텍스트 전용 모델 또는 Lyria와 같은 음악 생성 모델)과의 대화를 계속할 수 없습니다.

다음 기능은 [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ko) API에서 지원되지만 Interactions API에서는 **아직 사용할 수 없습니다**.

- **[동영상 메타데이터](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko)**: 동영상 이해를 위해 클리핑 간격과 맞춤 프레임 속도를 설정하는 데 사용되는 `video_metadata` 필드입니다.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**
- **[자동 함수 호출 (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ko#automatic_function_calling_python_only)**
- **[명시적 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**: 서버 측 암시적 캐싱은 `previous_interaction_id`를 통해 Interactions API에서 사용할 수 있습니다.
- **[안전 설정](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko)**: Interactions API에서는 맞춤 안전 설정이 지원되지 않습니다.

## 의견

여러분의 의견은 Interactions API 개발에 매우 중요합니다.
[Google AI 개발자 커뮤니티 포럼](https://discuss.ai.google.dev/c/gemini-api/4?hl=ko)에서 의견을 공유하거나 버그를 신고하거나 기능을 요청하세요.

## 다음 단계

- [상호작용 API 빠른 시작 노트북](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ko)을 사용해 보세요.
- [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)에 대해 자세히 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-16(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-16(UTC)"],[],[]]
