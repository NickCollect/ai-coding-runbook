---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=ko
fetched_at: 2026-06-01T06:05:52.999725+00:00
title: "Google AI Studio\uc5d0\uc11c \ubc30\ud3ec \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google AI Studio에서 배포

Google AI Studio를 사용하면 빌드 모드에서 바로 풀 스택 애플리케이션을 배포할 수 있습니다. 이를 통해 프로토타입에서 관리되고 확장 가능한 프로덕션 환경으로 빠르게 이동할 수 있습니다.

## 배포 옵션

AI Studio 빌드 모드에서 애플리케이션을 배포하기 위한 요구사항은 사용하는 등급에 따라 다릅니다.

- [**Google Cloud Starter Tier**](https://docs.cloud.google.com/docs/starter-tier?hl=ko): Google Cloud 프로젝트나 결제 계정을 설정하지 않고 최대 2개의 전체 스택 애플리케이션을 게시할 수 있습니다.
- **표준 배포**: AI Studio 계정에 연결된 Google Cloud 프로젝트가 필요하며 해당 프로젝트에서 결제가 사용 설정되어 있어야 합니다.

## Starter 등급 정보

Google Cloud Starter Tier를 사용하면 전체 Google Cloud 환경이나 결제 계정을 설정하지 않고도 Google AI Studio에서 Google Cloud에 애플리케이션을 직접 배포할 수 있습니다.

Google AI Studio 배포마다 Cloud Run에 해당 서비스가 생성됩니다. Google AI Studio에서 스타터 등급으로 배포된 서비스에는 다음 제한사항이 적용됩니다.

- 최대 2개의 서비스를 배포할 수 있습니다.
- 서비스가 [단일 Cloud Run 리전](https://docs.cloud.google.com/run/docs/locations?hl=ko)에 배포됩니다.

## 시작 단계 등급 배포 단계

빌드 모드에서 앱을 설계한 후 스타터 등급으로 배포합니다.

1. 오른쪽 상단에 있는 **게시** 버튼을 클릭합니다.
2. **시작하기**를 클릭합니다.
3. **앱 게시**를 클릭합니다.

배포가 완료되면 AI Studio에서 라이브 애플리케이션에 액세스할 수 있는 Cloud Run URL을 제공합니다.

## 표준 배포

애플리케이션이 발전함에 따라 Starter 등급을 초과하는 기능(예: 더 높은 할당량, 증가된 컴퓨팅 리소스, Starter 등급에서 사용할 수 없는 기타 Google Cloud 제품)이 필요할 수 있습니다. 이러한 기능을 사용하려면 완전 관리형 Starter 등급 프로젝트를 표준 Google Cloud 프로젝트로 변환하면 됩니다.

이렇게 하면 진행 상황을 잃지 않고 원활하게 확장할 수 있습니다. 단계에 따라 [Cloud Billing 계정을 만들고](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=ko#create-new-billing-account), 표준 Google Cloud 서비스 약관을 공식적으로 수락하고, [표준 Google Cloud 프로젝트로 업그레이드](https://docs.cloud.google.com/docs/starter-tier?hl=ko#upgradee)합니다.
자세한 내용은 [유료 계정 설정](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=ko#paid-setup)을 참고하세요.

결제 등급에 대해 자세히 알아보려면 [결제](https://ai.google.dev/gemini-api/docs/billing?hl=ko)를 참고하세요.

## 애플리케이션 삭제

앱이 더 이상 필요하지 않은 경우 다음 안내에 따라 Google AI Studio에서 삭제할 수 있습니다.

1. Google AI Studio에서 [앱 페이지](https://aistudio.google.com/app/apps?hl=ko)로 이동합니다.
2. 왼쪽 메뉴에서 **앱**을 선택합니다.
3. 삭제하려는 앱 위로 포인터를 가져갑니다.
4. 행의 오른쪽에 있는 휴지통 아이콘을 클릭하여 앱을 삭제합니다.

## 다음 단계

- [Google Cloud Starter 등급](https://docs.cloud.google.com/docs/starter-tier?hl=ko)에 대해 자세히 알아보세요.
- Gemini API의 [결제](https://ai.google.dev/gemini-api/docs/billing?hl=ko)에 대해 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-16(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-16(UTC)"],[],[]]
