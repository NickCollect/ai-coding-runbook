---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko
fetched_at: 2026-05-05T20:41:20.982261+00:00
title: "\ube44\uc728 \uc81c\ud55c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 비율 제한

비율 제한은 지정된 기간 내에 Gemini API에 요청할 수 있는 요청 수를 규제합니다. 이러한 제한은 공정한 사용을 유지하고, 악용을 방지하며, 모든 사용자를 위해 시스템 성능을 유지하는 데 도움이 됩니다.

[AI Studio에서 활성 비율 제한 보기](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ko)

## 비율 제한의 작동 방식

비율 제한은 일반적으로 다음 세 가지 측정기준으로 측정됩니다.

- 분당 요청 수 (**RPM**)
- 분당 토큰 수 (입력) (**TPM**)
- 일일 요청 수 (**RPD**)

사용량은 각 제한에 대해 평가되며, 제한을 초과하면 비율 제한 오류가 발생합니다. 예를 들어 RPM 제한이 20인 경우 TPM 또는 기타 제한을 초과하지 않았더라도 1분 이내에 21개의 요청을 하면 오류가 발생합니다.

비율 제한은 API 키별이 아닌 프로젝트별로 적용됩니다. 일일 요청 수 (**RPD**) 할당량은 태평양 표준시 자정에 재설정됩니다.

제한은 사용 중인 특정 모델에 따라 다르며 일부 제한은 특정 모델에만 적용됩니다. 예를 들어 분당 이미지 수(IPM)는 이미지를 생성할 수 있는 모델(Nano Banana)에 대해서만 계산되지만 개념적으로 TPM과 유사합니다. 다른 모델에는 일일 토큰 수 제한 (TPD)이 있을 수 있습니다.

비율 제한은 실험 모델 및 미리보기 모델에 더 제한적입니다.

## 사용 등급

비율 제한은 프로젝트의 사용 등급과 연결됩니다. API 사용량과 지출이 증가하면 비율 제한이 증가된 상위 등급으로 자동 업그레이드됩니다.

등급 2 및 3의 자격 요건은 프로젝트에 연결된 결제 계정의 Google Cloud 서비스 (Gemini API를 포함하되 이에 국한되지 않음)에 대한 누적 총 지출을 기준으로 합니다.

| 사용 등급 | 검증 | [결제 등급 한도](https://ai.google.dev/gemini-api/docs/billing?hl=ko#tier-spend-caps) |
| --- | --- | --- |
| **무료** | [활성 프로젝트](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#google-cloud-projects) 또는 무료 체험판 | 해당 사항 없음 |
| **등급 1** | [활성 결제 계정 설정 및 연결](https://ai.google.dev/gemini-api/docs/billing?hl=ko#setup-billing) | $250 |
| **등급 2** | 첫 번째 결제 완료 후 $100 + 3일 | $2,000 |
| **등급 3** | 첫 번째 결제 완료 후 $1,000 + 30일 | $20,000~$100,000 이상 |

명시된 자격 요건을 충족하는 것이 일반적으로 승인에 충분하지만 드물게 검토 과정에서 확인된 다른 요인에 따라 업그레이드 요청이 거부될 수 있습니다.

이 시스템은 모든 사용자를 위해 Gemini API 플랫폼의 보안과 무결성을 유지하는 데 도움이 됩니다.

## Gemini API 비율 제한

비율 제한은 다양한 요인 (예: 사용 등급)에 따라 다르며 Google AI Studio에서 확인할 수 있습니다. 시간이 지남에 따라 등급과 계정 상태가 변경되면 비율 제한이 자동으로 업데이트됩니다.

[AI Studio에서 활성 비율 제한 보기](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ko)

지정된 비율 제한은 보장되지 않으며 실제 용량은 다를 수 있습니다.

## 우선순위 추론 비율 제한

[우선순위](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko) 소비는 전체 대화형 트래픽
비율 제한에 소비가 집계되더라도 자체 비율
제한을 유지합니다. **기본 비율 제한은 각 모델 및 등급의 [표준 비율 제한](https://aistudio.google.com/rate-limit?hl=ko)의 0.3배입니다.**

## 일괄 API 비율 제한

[일괄 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko) 요청에는 일괄 처리되지 않은 API 호출과는 별도로 자체 비율
제한이 적용됩니다.

- **동시 일괄 요청:** 100
- **입력 파일 크기 제한:** 2GB
- **파일 저장용량 제한:** 20GB
- **모델당 큐에 추가된 토큰:** **큐에 추가된 일괄 토큰** 표에는 특정 모델의 모든 활성 일괄 작업에서 일괄 처리를 위해 큐에 추가할 수 있는 최대 토큰 수가 나와 있습니다.

### 등급 1

| 모델 | 큐에 추가된 일괄 토큰 |
| --- | --- |
| 텍스트 출력 모델 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro 프리뷰 | 5,000,000 |
| Gemini 3.1 Flash-Lite 프리뷰 | 10,000,000 |
| Gemini 3 Flash 프리뷰 | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash 프리뷰 | 3,000,000 |
| Gemini 2.5 Flash 이미지 프리뷰 | 3,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 10,000,000 |
| Gemini 2.5 Flash-Lite 프리뷰 | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash 이미지 | 3,000,000 |
| Gemini 2.0 Flash-Lite | 10,000,000 |
| 멀티모달 생성 모델 | | | | |
| Gemini 3.1 Flash 이미지 프리뷰 🍌 | 1,000,000 |
| Gemini 3 Pro 이미지 프리뷰 🍌 | 2,000,000 |
| 임베딩 모델 | | | | |
| Gemini 임베딩 | 500,000 |

### 등급 2

| 모델 | 큐에 추가된 일괄 토큰 |
| --- | --- |
| 텍스트 출력 모델 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro 프리뷰 | 500,000,000 |
| Gemini 3.1 Flash-Lite 프리뷰 | 500,000,000 |
| Gemini 3.1 Flash 프리뷰 | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash 프리뷰 | 400,000,000 |
| Gemini 2.5 Flash 이미지 프리뷰 | 400,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.5 Flash-Lite 프리뷰 | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash 이미지 | 400,000,000 |
| Gemini 2.0 Flash-Lite | 1,000,000,000 |
| 멀티모달 생성 모델 | | | | |
| Gemini 3.1 Flash 이미지 프리뷰 🍌 | 250,000,000 |
| Gemini 3 Pro 이미지 프리뷰 🍌 | 270,000,000 |
| 임베딩 모델 | | | | |
| Gemini 임베딩 | 5,000,000 |

### 등급 3

| 모델 | 큐에 추가된 일괄 토큰 |
| --- | --- |
| 텍스트 출력 모델 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro 프리뷰 | 1,000,000,000 |
| Gemini 3.1 Flash-Lite 프리뷰 | 1,000,000,000 |
| Gemini 3.1 Flash 프리뷰 | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Gemini 2.5 Flash 프리뷰 | 1,000,000,000 |
| Gemini 2.5 Flash 이미지 프리뷰 | 1,000,000,000 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Gemini 2.5 Flash-Lite 프리뷰 | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash 이미지 | 1,000,000,000 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| 멀티모달 생성 모델 | | | | |
| Gemini 3.1 Flash 이미지 프리뷰 🍌 | 750,000,000 |
| Gemini 3 Pro 이미지 프리뷰 🍌 | 1,000,000,000 |
| 임베딩 모델 | | | | |
| Gemini 임베딩 | 10,000,000 |

## 다음 등급으로 업그레이드하는 방법

무료 등급에서 유료 등급으로 전환하려면 먼저
[AI Studio에서 결제를 설정해야 합니다](https://ai.google.dev/gemini-api/docs/billing?hl=ko).

프로젝트가 [지정된 기준](#usage-tiers)을 충족하면 다음 등급으로
자동 업그레이드됩니다. 무료 등급에서 등급 1로의 등급 업그레이드는 일반적으로 즉시 적용되며 후속 등급 업그레이드는 10분 이내에 적용됩니다. AI Studio의 [프로젝트 페이지](https://aistudio.google.com/projects?hl=ko)로 이동하여 등급을 확인하세요.

## 비율 제한 상향 요청

각 모델 변형에는 연결된 비율 제한 (분당 요청 수, RPM)이 있습니다.
이러한 비율 제한에 대한 자세한 내용은
[AI Studio 비율 제한](https://aistudio.google.com/rate-limit?hl=ko) 페이지를 참고하세요.

[유료 등급 비율 제한 상향 요청](https://forms.gle/ETzX94k8jf7iSotH9)

비율 제한 상향을 보장하지는 않지만 요청을 검토하기 위해 최선을 다하겠습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-28(UTC)"],[],[]]
