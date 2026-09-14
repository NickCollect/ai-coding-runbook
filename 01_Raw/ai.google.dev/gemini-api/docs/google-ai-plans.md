---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=ko
fetched_at: 2026-09-14T05:43:26.897270+00:00
title: "Google AI \uc694\uae08\uc81c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)

의견 보내기

# Google AI 요금제

AI Studio에서 Google AI 구독 요금제를 사용하세요.

Google AI Pro 및 Ultra 구독 요금제는 무료 등급에 비해 AI Studio에서 프로토타입 제작 및 개발을 위한 모델 액세스 권한과 비율 제한이 더 높습니다.

Google AI 요금제에 가입하려면 Google AI Studio 내에서 왼쪽 탐색 메뉴의 **업그레이드** 버튼을 클릭하여 직접 업그레이드하면 됩니다. 또는
[Google AI 요금제 페이지](https://one.google.com/about/google-ai-plans/?hl=ko)를 방문하여 가입할 수도 있습니다.

## 개요

Google AI Pro 및 Ultra 구독을 사용하면 개발자가 Google AI Studio Playground에서 유료 모델과 더 높은 비율 제한을 활용하고, 바이브 코딩을 위한 [빌드 모드](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=ko)의 코드 어시스턴트와 같은 기능을 사용할 수 있습니다. [[구독자는 Playground 및 빌드 인터페이스에서 사용할 수 있는 무료 등급보다 높은 기준 일일 할당량 허용치를 받습니다.](https://aistudio.google.com/prompts/new_chat?hl=ko)](https://aistudio.google.com/apps?hl=ko) 일일 한도는 롤링 시간 창이 아닌 재설정을 사용하여 적용되므로 Cloud Billing으로 프로덕션 규모 개발로 전환하기 전에 원활한 개발 환경을 보장합니다.

| 계획 | AI Studio 사용량 | 모델 액세스 및 이점 |
| --- | --- | --- |
| **무료** | 적당한 할당량 | 기본 한도 및 액세스 권한이 제공되며, 업그레이드하여 더 많은 혜택을 누릴 수 있습니다. |
| **AI Pro** | 더 높은 할당량 | Gemini Pro, Nano Banana, Lyria와 같은 프리미엄 모델에 액세스할 수 있습니다. |
| **AI Ultra** | 최고 할당량 | 프로토타입 제작, 개발, 고급 프런티어 모델을 위한 최고 한도입니다. |

## Gemini API 사용량

AI Studio에서 일일 기준 구독 할당량이 소진되면 Gemini API의 요청당 사용량에 대해 Cloud 결제가 사용 설정된 Gemini API 키를 사용하여 워크플로를 계속할 수 있습니다.
프로젝트 및 API 키의 Gemini API 사용량은
[AI Studio 대시보드](https://aistudio.google.com/projects?hl=ko)에서 확인할 수 있습니다.

Google Cloud Platform (GCP) 프로젝트가 있고 Cloud Billing이 사용 설정된 구독자는 [Google Developer Program](https://developers.google.com/program?hl=ko)에서 Gemini API를 비롯한 Cloud 서비스에 대해 월간 Cloud 크레딧을 받을 수 있습니다. 선불 및 후불 사용량과 청구는 변경되지 않습니다. 선불 결제를 사용하는 사용자의 경우 프로모션 크레딧을 활성화하려면 AI Studio에서 0달러를 초과하는 유료 잔액이 필요합니다. 자격 요건을 충족하는 Google Cloud 크레딧이 있는 경우 먼저 적용됩니다.
[자세히 알아보기](https://ai.google.dev/gemini-api/docs/billing?hl=ko#billing-plans).

Google AI 구독 통합은 고급 실험 및 개발의 진입 장벽을 낮춥니다. 하지만 대규모 프로덕션
배포의 경우 Google Cloud 프로젝트,
[Google Cloud 스타터 등급](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=ko),
Gemini API 키를 사용하는 것이 좋습니다.

## 제한사항 및 호환성

- **AI Studio UI 전용:** 개발자 사용을 위한 Google AI 요금제 혜택은 Google AI Studio 웹 인터페이스 내에서만 적용됩니다. Gemini API를 직접 사용하는 경우(예: API 키 또는 외부 애플리케이션 사용) 별도로 청구되고 관리됩니다. 하지만 다른 Google
  제품에서 구독을 사용할 수 있습니다 ([Google AI 요금제](https://one.google.com/about/google-ai-plans/?hl=ko) 참고).
- **API 청구와 다름:** AI Studio용 Google AI 요금제는 개발 및 프로덕션 API 사용량을 포함하는 [Gemini API 사용량 등급](https://ai.google.dev/gemini-api/docs/billing?hl=ko)과 별개입니다.
- **Google One 크레딧:** [Google One AI 크레딧](https://support.google.com/googleone/answer/16287445?hl=ko)은 AI Studio 내에서 지원되지 않으며 Google Cloud 크레딧과 중복되지 않는 별도의 크레딧 시스템입니다.
- **에이전트 액세스:** AI Studio 내의 에이전트 (Deep Research 및 Antigravity 미리보기)에 대한 액세스 권한은 Google AI 요금제에 포함되지 않으며 [유료 API 키](https://ai.google.dev/gemini-api/docs/billing?hl=ko#setup-billing)가 필요합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-08-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-08-19(UTC)"],[],[]]
