---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=ko
fetched_at: 2026-07-27T04:38:01.843379+00:00
title: "\ub370\uc774\ud130 \ub85c\uae45 \ubc0f \uacf5\uc720 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 데이터 로깅 및 공유

이 페이지에서는 결제가 사용 설정된 프로젝트의 지원되는 Gemini API 호출에서 개발자가 소유한
API 데이터인
[Gemini API 로그](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko)의 저장 및 관리에 대해 설명합니다. 로그는 사용자의 요청부터 모델의 응답까지 전체 프로세스를 포함합니다.
[Google Cloud 프로젝트에 비공개인 이러한 로그는 악용 모니터링 목적으로만 보유되는 로그와는 별개입니다.](https://ai.google.dev/gemini-api/docs/usage-policies?hl=ko)

## 공유할 수 있는 데이터

프로젝트 소유자는 자체 사용을 위해 또는 Google에 의견을 제공하고 공유하여 Google이 모델을 지속적으로 개선할 수 있도록 Gemini API 호출의 로깅을 선택할 수 있습니다.

로깅을 사용 설정하면 제품 개선 및 모델 학습을 위해 다음 데이터를 제공하여 다양한 분야와 사용 사례에서 개발자에게 계속해서 유용한 AI 시스템을 구축하는 데 도움이 될 수 있습니다.

- **데이터 세트:** Google AI Studio의 로그 및 데이터 세트 인터페이스를 사용하여 지원되는 Gemini API 호출에서 관심 있는 로그 (요청, 응답, 메타데이터 등)를 선택합니다. 데이터 세트에 포함하여 제공되며 데이터 세트 생성 중에 선택 해제할 수 있습니다.
- **의견:** 로그를 검토할 때 의견을 제공할 수 있습니다. 여기에는 좋아요 및 싫어요 평가와 작성한 의견이 포함됩니다.

데이터 세트를 Google과 공유하면 요청 및 응답을 포함한 해당 데이터 세트의 로그가
저희
[약관](https://developers.google.com/terms?hl=ko)의
"[무료 서비스](https://ai.google.dev/gemini-api/terms?hl=ko#data-use-unpaid)"에 따라 처리됩니다.
즉, 데이터 세트는 모델 개선 및
학습을 포함하여 Google
제품, 서비스, 머신러닝 기술을 개발하고 개선하는 데 사용될 수 있습니다. **개인 정보, 민감한 정보 또는 기밀 정보를 포함하지 마세요.**

## Google에서 데이터를 사용하는 방식

로그는 기본적으로 최대 55일 동안 보관됩니다. 이 기간이 지나면 로그는 삭제 대상으로 자동 표시됩니다. AI Studio에서 프로젝트의 저장소 보관 기간을 업데이트하여 7일, 14일, 28일 또는 55일 후에 로그를 삭제 대상으로 자동 표시할 수 있습니다.

[데이터 세트](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko)를 만들어 다운스트림 사용 사례에 대한 설정된 보관 기간을 초과하여 관심 있는 로그를 보관하고
모델 개선에 선택적으로 기여할 수 있습니다. 데이터 세트에 저장된 로그에는 설정된 보관 기간이 없습니다.

기본적으로 로깅은 결제가 사용 설정된 프로젝트에서만 사용할 수 있으므로
로그 내의 프롬프트와 응답은 제품 개선 또는
개발에 사용되지 않습니다. 이는 데이터 사용에 관한 [약관](https://developers.google.com/terms?hl=ko)
에 따릅니다.

로그의 데이터 세트를 Google과 공유하도록 선택하면 이러한 데이터 세트는 AI 시스템 및 애플리케이션이 사용되는 다양한 도메인과 컨텍스트를 더 잘 이해하기 위한 실제 데모 데이터로 사용됩니다. 이 데이터는 모델 품질을 개선하고 향후 모델 및 서비스의 학습 및 평가에 영향을 미칠 수 있습니다. [이 데이터는 무료 서비스의 데이터 사용
약관에 따라 처리됩니다.](https://ai.google.dev/gemini-api/terms?hl=ko#data-use-unpaid)

따라서 인적 검토자는 공유하는 API 입력 및 출력을 읽고, 주석을 달고, 처리할 수 있습니다. 데이터가 모델 개선에 사용되기 전에 Google은 이러한 과정에서 사용자 개인 정보를 보호하기 위한 조치를 취합니다. 여기에는 검토자가 이 데이터를 보거나 주석을 작성하기 전에 Google 계정, API 키, Cloud 프로젝트에서 이 데이터의 연결을 해제하는 조치가 포함됩니다.

## 데이터 권한

API 데이터 제공을 선택하면 Google이 이 문서에 설명된 대로 데이터를 처리하고 사용할 수 있는 필요한 권한이 있음을 확인하는 것입니다. **유료 서비스를 통해 얻은 민감한 정보, 기밀 정보 또는 독점 정보가 포함된 로그는 제공하지 마세요**.
'[콘텐츠 제출](https://developers.google.com/terms?hl=ko#b_submission_of_content)' 조항에 따라 Google에 부여한 라이선스도 Google의 사용에 대한 관련 법규에 따라 요구되는 범위 내에서 '서비스' 및 생성된 답변에 제출한 콘텐츠 (예: 이미지, 동영상, 문서 등 관련 파일, 캐시된 콘텐츠, 시스템 안내를 포함한 프롬프트)로 확장됩니다.

## 데이터 공유 및 의견

데이터를 예시로 공유하도록 선택하면 AI 연구, Gemini API, Google AI Studio의 발전에 도움이 될 수 있습니다. 이를 통해 다양한 컨텍스트에서 모델을 지속적으로 개선하고 다양한 분야와 사용 사례에서 개발자에게 계속해서 유용한 AI 시스템을 구축할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-09(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-09(UTC)"],[],[]]
