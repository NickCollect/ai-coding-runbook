---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=ko
fetched_at: 2026-07-27T04:48:43.427070+00:00
title: "Gemini API\uc758 \ub3d9\uc601\uc0c1 \uc0dd\uc131 \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API의 동영상 생성

Gemini API는 동영상 생성에 사용할 수 있는 두 가지 모델인
[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ko)와 [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=ko)를 제공합니다.
각 모델은 서로 다른 워크플로를 위해 설계되었습니다.

동영상 생성의 기본 모델로 Gemini Omni Flash를 사용하세요. 이 모델은 우수한 동영상 일관성, 다중 입력 추론 (텍스트, 이미지, 오디오, 동영상 입력을 동시에 지원), 캐릭터 일관성, 사실 정확성, 멀티턴 대화 기반 수정 (예: 요소 대체 또는 관점 변경)을 제공합니다. 장면 확장, 마지막 프레임 제어 또는 기존 파이프라인과의 통합과 같은 특정 기능이 필요한 경우 Veo 3.1을 사용하세요.

## Gemini Omni Flash

Gemini Omni Flash는 동영상 생성 및 대화 기반 동영상 수정을 위한 빠른 멀티모달 모델입니다. 이 모델은 텍스트 프롬프트와 이미지를 짧은 동영상으로 빠르게 변환하는 데 탁월하며 Interactions API를 사용하여 여러 턴에 걸쳐 결과를 세부적으로 조정할 수 있습니다.

[Gemini Omni Flash 시작하기 →](https://ai.google.dev/gemini-api/docs/omni?hl=ko)

## Veo 3.1

Veo 3.1은 기본 오디오로 동영상을 생성하는 모델입니다. `generateContent` API를 통해 동영상 확장, 프레임별 생성, 이미지 기반 방향과 같은 기능을 지원합니다.

[Veo 3.1 시작하기 →](https://ai.google.dev/gemini-api/docs/veo?hl=ko)

## 동영상 이해

새 동영상을 생성하는 대신 기존 동영상 콘텐츠를 수집하고 분석해야 하는 경우 [동영상 이해 가이드](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-30(UTC)"],[],[]]
