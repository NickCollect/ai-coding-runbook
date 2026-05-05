---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=ko
fetched_at: 2026-05-05T19:49:40.593537+00:00
title: "Gemini Developer API\uc758 \ub370\uc774\ud130 \ubcf4\uad00 \uc5c6\uc74c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Developer API의 데이터 보관 없음

이 페이지에서는 Gemini Developer API에서 일반적으로 '제로 데이터 보관'이라고 하는 사항의 세부정보를 간략하게 설명합니다.

## 학습 제한

[Gemini API 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 설명된 대로 '유료 서비스'를 사용하는 경우 Google은 제품 개선을 위해 프롬프트 (관련 시스템 안내, 캐시된 콘텐츠, 이미지, 동영상, 문서 등의 파일 포함) 또는 대답을 사용하지 않습니다. '유료 서비스'는 여기에 정의되어 있습니다
.

## 고객 데이터 보관 및 제로 데이터 보관 달성

고객 데이터는 일반적으로 다음과 같은 시나리오 및 조건에서 제한된 기간 동안 보관됩니다. 제로 데이터 보관을 달성하려면 고객이 다음 각 영역에서 특정 조치를 취하거나 특정 기능을 피해야 합니다.

- [**악용 모니터링을 위한 프롬프트 로깅**: [Gemini API
  추가 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 설명된 대로 '유료 서비스'의 경우 Google
  은 금지된 사용
  정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko) 위반을 감지하기 위해서만 제한된 기간 동안 프롬프트와 대답을 로깅합니다. 특정 프로젝트에 대한 ZDR 요청이 승인되면 로깅 전에 모든 사용자 콘텐츠(프롬프트 및 대답)와 식별 가능한 메타데이터 (예: IP 주소, Google 계정 ID)가 삭제됩니다. 결과 레코드는 삭제된 것으로 표시되며 식별 가능한 사용자 데이터가 포함되지 않아 Gemini Enterprise Agent Platform 제로 데이터 보관과 동일한 수준을 유지합니다.
- **Google 검색을 사용한 그라운딩**: [Gemini API 추가
  서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko#grounding-with-google-search)에 설명된 대로 Google은 그라운딩된 결과 및 추천 검색어를 생성하기 위해 프롬프트, 컨텍스트 정보, 생성된 출력을 30일 동안 저장합니다.
  이 저장된 정보는 그라운딩을 지원하는 시스템의 디버깅 및 테스트에 사용될 수 있습니다. **Google 검색을 사용한 그라운딩을 사용하는 경우 이 정보의 저장을 사용 중지할 방법이 없습니다.**
- **Google 지도 기반 그라운딩**: [Gemini API 추가 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 설명된 대로 Google은 그라운딩된 결과를 생성하기 위해 프롬프트, 컨텍스트 정보, 생성된 출력을 30일 동안 저장합니다. 이 저장된 정보는 서비스 문제 발생 시 디버깅과 같은 안정성 엔지니어링 목적으로만 사용될 수 있습니다.
  **Google 지도 기반 그라운딩을 사용하는 경우 이 정보의 저장을 사용 중지할 방법이 없습니다.**
- **상호작용 API**: 상호작용 API는
  대화의 활성 상태를 관리하여 다중 턴을 지원합니다. **기본적으로 상호작용 API는 상태 저장을 사용 설정합니다**. 데이터 사용 공간을 제로로 유지하려면 API 요청에서 `store` 매개변수를 `false`로 명시적으로 설정하여 기본 상태 보관을 선택 해제해야 합니다.
- **Live API**: 이 스테이트풀(Stateful) API는 대화 상태를 저장하여 실시간 재연결을 지원합니다. 제로 데이터 보관을 달성하려면 **SessionResumptionConfig를 구성하지 마세요**. 세션 핸들이 생성되면 대화 상태 (텍스트, 오디오, 동영상 포함)가 최대 24시간 동안 보관됩니다.
- **파일 API 스토리지**: 파일 API를 사용하면 사용자가 대용량 애셋을 업로드할 수 있습니다.
  파일은 사용자가 삭제하거나 만료될 때까지 저장됩니다.
  파일 API 사용은 ZDR 로깅과 독립적입니다. 사용자는 데이터 사용 공간을 제로로 유지하기 위해 파일을 수동으로 삭제해야 합니다.
- **명시적 컨텍스트 캐싱**: 사용자는 대용량 데이터 세트 (예:
  긴 동영상 또는 문서 라이브러리)를 `cached_content` 필드를 사용하여 수동으로 캐시할 수 있습니다. 이러한 요청의 로그는 ZDR 삭제 정책을 따르지만 캐시된 컨텍스트 자체는 사용자 정의 `ttl` 또는 `expire_time`으로 저장됩니다. 데이터 사용 공간을 완전히 제로로 유지하려면 cached\_content 기능을 사용하지 마세요.
- **암시적 메모리 내 캐싱**: 기본적으로 Gemini 모델은 지연 시간을 줄이고 개발자 비용을 절감하기 위해 데이터를
  메모리에 캐시합니다. 이 데이터는 RAM에만 있고 (저장되지 않음) 프로젝트 수준에서 격리되며 TTL이 24시간입니다.
  **이는 제로 데이터 보관을 위반하지 않습니다.**

## 다음 단계

- [생성형 AI 금지된 사용 정책에 관해 알아보기](https://policies.google.com/terms/generative-ai/use-policy?hl=ko)
- [Gemini API 추가 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko) 검토하기
- 엔터프라이즈급 셀프서비스 ZDR 제어가 필요한 경우 [Gemini Enterprise Agent Platform
  Zero Data Retention
  guide](https://cloud.google.com/gemini-enterprise-agent-platform/models/vertex-ai-zero-data-retention?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
