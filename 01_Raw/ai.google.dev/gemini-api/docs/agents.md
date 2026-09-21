---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=ko
fetched_at: 2026-09-21T05:48:04.096328+00:00
title: "\uc5d0\uc774\uc804\ud2b8 \uac1c\uc694 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 에이전트 개요

Gemini API의 관리형 에이전트는 구성 가능한 에이전트 하네스를 제공합니다. 단일 API 호출은 에이전트가 추론하고, 코드를 실행하고, 파일을 관리하고, 웹을 자율적으로 탐색하는 Linux 샌드박스를 프로비저닝합니다.

[rocket\_launch

빠른 시작

첫 번째 에이전트 호출을 하고, 응답을 스트리밍하고, 맞춤 에이전트를 빌드합니다.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)
[smart\_toy

Antigravity 에이전트

기본 에이전트의 기능, 도구, 멀티모달 입력, 가격 책정](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)
[experiment

AI Studio의 에이전트

코드를 작성하지 않고 에이전트의 프로토타입을 제작할 수 있는 시각적 플레이그라운드입니다.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ko)

## 사용 가능한 관리형 에이전트

- **[Antigravity agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)**: Gemini 3.8 Flash로 빌드된 범용 관리형 에이전트입니다. Google에서 호스팅하는 안전한 Linux 샌드박스 내에서 코드를 실행하고, 파일을 관리하고, 웹을 검색합니다. `agent_config`를 사용하여 기본 모델 (예: Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash)을 구성하고 자체 안내, 기술, 데이터로 확장하여 [맞춤 에이전트를 빌드](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko)할 수 있습니다.
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)**: 시장 분석, 실사, 문헌 검토와 같은 사용 사례를 위해 다단계 연구 작업을 계획, 실행, 종합하는 자율 연구 에이전트입니다.

## 보안 및 권장사항

모든 에이전트는 OS 수준에서 격리된 샌드박스 환경에서 실행됩니다.
샌드박스는 기본적으로 아웃바운드 네트워크 액세스가 무제한입니다. 허용 목록을 사용하여 네트워크 액세스를 제한하거나 사용 중지할 수 있습니다.

### 네트워크 액세스

기본적으로 환경에는 제한 없는 아웃바운드 네트워크 액세스 권한이 있습니다. `network` 허용 목록을 사용하여 아웃바운드 트래픽을 특정 도메인 또는 와일드카드 패턴으로 제한합니다. 구성 세부정보는 [네트워크 허용 목록](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ko#network_allow_list) (AI Studio) 또는 [네트워크 규칙](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko#with_network_rules)(API)을 참고하세요.

### 외부 도구 및 API

외부 도구와 API를 연결하여 에이전트를 확장할 수 있습니다. 신뢰할 수 있는 출처의 도구만 사용하고 필요한 최소한의 권한으로 범위를 지정합니다. 보안 비밀을 관리 사용자 인증 정보로 저장하고 ID로 참조하여 이그레스 프록시가 요청 시에 삽입하고 샌드박스 내부에 노출되지 않도록 합니다. 에이전트는 액세스할 수 있는 사용자 인증 정보를 사용할 수 있으므로 전체 범위를 부여하려는 사용자 인증 정보만 제공하세요.

- 최소 권한 서비스 계정 또는 API 키를 사용합니다.
- 수명이 긴 키보다 수명이 짧은 토큰을 선호합니다.
- 전체 범위를 부여할 의향이 있는 사용자 인증 정보만 제공하세요.
- 정기적인 일정에 따라 사용자 인증 정보를 순환합니다.

사용자 인증 정보 유형 및 관리 작업은 [사용자 인증 정보](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ko)를 참고하세요. 허용 목록 규칙에서 인라인으로 헤더를 설정할 수도 있습니다([네트워크 구성](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#network-configuration) 참고).

### 인간의 감독

특히 데이터를 수정하거나 외부 시스템과 상호작용하는 작업의 경우 출력을 배포하기 전에 항상 확인하세요 (생성된 코드, 데이터 변환, 구성 변경사항).

## 가격 책정

관리형 에이전트는 Gemini 모델 토큰 및 도구 사용량에 기반한 [사용한 만큼만 지불 모델](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#pricing-for-agents)을 사용합니다. 단일 상호작용은 여러 추론 루프를 트리거할 수 있으며, 일반적으로 100,000~3,000,000개의 토큰을 소비합니다. 환경 컴퓨팅은 미리보기 기간 동안 **청구되지 않습니다**. 작업별 분석은 [예상 비용](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko#availability-and-pricing)을 참고하세요. 관리형 에이전트는 무료 비율 제한 및 사용량 할당량이 있는 무료 등급에서도 사용할 수 있습니다.

## 한도

| 한도 | 설명 |
| --- | --- |
| **환경 전체 기간** | 환경은 7일 동안 비활성 상태가 되면 영구적으로 삭제됩니다. |
| **VM 스핀다운** | VM은 리소스를 절약하기 위해 잠시 활동이 없으면 종료됩니다. 다음 요청은 콜드 스타트로 상태를 복원합니다. |
| **사전 설치된 소프트웨어** | Python 3.12 및 Node.js 22가 설치된 Ubuntu 기반 환경 환경의 기본 이미지에 관한 자세한 내용은 [사전 설치된 소프트웨어](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#pre-installed-software)를 참고하세요. |
| **최대 상담사 수** | 관리 에이전트는 최대 1,000개까지 보유할 수 있습니다. |

## 에이전트 프레임워크

다음 프레임워크와 SDK를 사용하여 Gemini로 에이전트를 빌드할 수도 있습니다.

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=ko): 그래프 구조를 사용하여 상태 저장 복잡한 애플리케이션 흐름과 멀티 에이전트 시스템을 빌드합니다.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=ko): RAG가 강화된 워크플로를 위해 Gemini 에이전트를 비공개 데이터에 연결합니다.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=ko): 협업적이고 롤플레잉을 하는 자율 AI 에이전트를 조정합니다.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ko): JavaScript/TypeScript로 AI 기반 사용자 인터페이스 및 에이전트를 빌드합니다.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): 상호 운용 가능한 AI 에이전트를 빌드하고 오케스트레이션하기 위한 오픈소스 프레임워크입니다.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=ko): Google Antigravity를 지원하는 동일한 도구, 에이전트 루프, 컨텍스트 관리를 사용하여 자율 AI 에이전트를 빌드합니다. Python으로 프로그래밍할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-18(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-18(UTC)"],[],[]]
