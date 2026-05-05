---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=ko
fetched_at: 2026-05-05T19:47:07.494343+00:00
title: "\ud30c\ud2b8\ub108 \ubc0f \ub77c\uc774\ube0c\ub7ec\ub9ac \ud1b5\ud569 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 파트너 및 라이브러리 통합

이 가이드에서는 Gemini API를 기반으로 라이브러리, 플랫폼, 게이트웨이를 빌드하기 위한 아키텍처 전략을 간략하게 설명합니다. 공식 생성형 AI SDK, Direct API (REST/gRPC), OpenAI 호환성 레이어를 사용하는 것 간의 기술적 절충점을 자세히 설명합니다.

오픈소스 프레임워크, 엔터프라이즈 게이트웨이, SaaS 애그리게이터와 같은 다른 개발자를 위한 도구를 빌드하고 종속 항목 위생, 번들 크기 또는 기능 패리티에 맞게 최적화해야 하는 경우 이 가이드를 사용하세요.

## 파트너 통합이란 무엇인가요?

파트너는 Gemini API와 최종 사용자 개발자 간의 통합을 빌드하는 모든 사람입니다. Google은 파트너를 네 가지 원형으로 분류합니다. 가장 일치하는 항목을 식별하면 올바른 통합 경로를 선택하는 데 도움이 됩니다.

#### 생태계 프레임워크

- **대상:** 오픈소스 프레임워크 (예: LangChain, LlamaIndex, Spring AI) 또는 언어별 클라이언트의 관리자입니다.
- **목표:** 광범위한 호환성입니다. 사용자가 선택한 모든 환경에서 충돌을 일으키지 않고 라이브러리가 작동하도록 하려고 합니다.

#### 런타임 및 에지 플랫폼

- **대상:** 코드 실행이 제한된 환경에서 발생하는 SaaS 플랫폼, AI 게이트웨이 또는 클라우드 인프라 제공업체 (예: Vercel, Cloudflare, Zapier)입니다.
- **목표:** 성능입니다. 지연 시간이 짧고 번들 크기가 최소화되며 콜드 스타트가 빨라야 합니다.

#### 애그리게이터

- **대상:** 여러 LLM 제공업체 (예: OpenAI, Anthropic, Google)의 액세스를 단일 인터페이스로 정규화하는 플랫폼, 프록시 또는 내부 '모델 가든'입니다.
- **목표:** 이식성과 균일성입니다.

#### 엔터프라이즈 게이트웨이

- **대상:** 수백 명의 내부 개발자를 위한 '최적의 경로'를 빌드하는 대기업의 내부 플랫폼 엔지니어링팀입니다.
- **목표:** 표준화, 거버넌스, 통합 인증입니다.

## 한눈에 비교하기

**글로벌 권장사항:** 모든 파트너는 선택한 경로와 관계없이 [`x-goog-api-client`
헤더](#client-id)를 전송해야 합니다.

| 다음과 같은 경우... | 권장 경로 | 주요 이점 | 주요 절충점 | 권장사항 |
| --- | --- | --- | --- | --- |
| **엔터프라이즈 게이트웨이, 생태계 프레임워크** | **[Google 생성형 AI SDK](#genai-sdk)** | **Gemini Enterprise Agent Platform 패리티 및 속도.** 유형, 인증, 복잡한 기능 (예: 파일 업로드)을 기본적으로 처리합니다. Google Cloud로 원활하게 마이그레이션합니다. | **종속 항목 가중치.** 전이적 종속 항목은 복잡하고 제어할 수 없습니다. 지원되는 언어 (Python/Node/Go/Java)로 제한됩니다. | **버전 잠금.** 팀 간의 안정성을 보장하기 위해 내부 기본 이미지에서 SDK 버전을 고정합니다. |
| **생태계 프레임워크, 에지 플랫폼, 애그리게이터** | **[Direct API](#rest)**  *(REST / gRPC)* | **종속 항목 없음.** HTTP 클라이언트와 정확한 번들 크기를 제어합니다. 모든 API 및 모델 기능에 대한 전체 액세스 권한입니다. | **개발자 오버헤드가 높습니다.** JSON 구조는 깊이 중첩될 수 있으며 엄격한 수동 유효성 검사 및 유형 검사가 필요합니다. | **OpenAPI 사양을 사용합니다.** 수동으로 작성하는 대신 공식 사양을 사용하여 유형 생성을 자동화합니다. |
| **텍스트 기반 워크플로만 필요한 OpenAI SDK를 사용하는 애그리게이터**  *(레거시 이식성을 위해 최적화)* | **[OpenAI 호환성](#openai)** | **즉시 이식성.** 기존 OpenAI 호환 코드 또는 라이브러리를 재사용합니다. | **기능 한도.** 모델별 기능 (네이티브 동영상, 캐싱)을 사용하지 못할 수 있습니다. | **마이그레이션 계획.** 빠른 유효성 검사에 사용하지만 전체 API 기능을 위해 Direct API로 업그레이드할 계획입니다. |

## Google 생성형 AI SDK 통합

프레임워크의 경우 [Google 생성형 AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)
를 구현하는 것이 지원되는
언어의 코드 줄 수가 가장 적기 때문에 가장 간단한 경로인 경우가 많습니다.

내부 플랫폼팀의 경우 기본 제공 항목은 제품 엔지니어가 보안 정책을 준수하면서 빠르게 이동할 수 있도록 하는 '최적의 경로'인 경우가 많습니다.

**혜택:**

- **Gemini Enterprise Agent Platform 마이그레이션을 위한 통합 인터페이스:** 내부 개발자는 API 키 (Gemini API)를 사용하여 프로토타입을 만들고 프로덕션 규정 준수를 위해 Gemini Enterprise Agent Platform (IAM)에 배포하는 경우가 많습니다. SDK는 이러한 인증 차이를 추상화합니다.
  마찬가지로 프레임워크의 경우 하나의 코드 경로를 구현하고 두 개의 사용자 집합을 지원할 수 있습니다.
- **클라이언트 측 도우미:** SDK에는 복잡한 작업의 상용구 코드를 줄이는 관용적 유틸리티가 포함되어 있습니다.
  - *예:* 프롬프트에서 `PIL` 이미지 객체를 직접 지원, 자동 함수 호출, 포괄적인 유형
- **Day-zero 기능 액세스:** 새로운 API 기능은 SDK를 통해 출시 시점에 제공됩니다.
- **코드 생성 지원 개선:** 로컬 SDK 설치는 유형 정의 및 독스트링을 코딩 어시스턴트 (예: Cursor, Copilot)에 노출합니다.
  이 컨텍스트는 원시 REST 요청을 생성하는 것보다 코드 생성 정확도를 개선합니다.

**절충점:**

- **종속 항목 가중치 및 복잡성:** SDK에는 자체 종속 항목이 있으므로 번들 크기가 커지고 공급망 위험이 발생할 수 있습니다.
- **버전 관리:** 새로운 API 기능은 최소 SDK 버전에 고정되는 경우가 많습니다.
  새로운 기능이나 모델에 액세스하려면 사용자에게 업데이트를 푸시해야 할 수 있으며, 이 경우 사용자에게 영향을 미치는 전이적 종속 항목을 변경해야 할 수 있습니다.
- **프로토콜 한도:** SDK는 기본 API의 경우 HTTPS만 지원하고 Live API의 경우 WebSocket (WSS)만 지원합니다. gRPC는 상위 수준 SDK 클라이언트를 사용하여 지원되지 않습니다.
- **언어 지원:** SDK는 *현재* 언어 버전을 지원합니다. EOL 버전 (예: Python 3.9)을 지원해야 하는 경우 포크를 유지해야 합니다.

**권장사항:**

- **버전 잠금:** 팀 간의 안정성을 보장하기 위해 내부 기본 이미지에서 SDK 버전을 고정합니다.

## API 직접 통합

수천 명의 개발자에게 라이브러리를 배포하거나, 제한된 환경에서 실행하거나, Gemini의 최첨단 기능이 필요한 애그리게이터를 빌드하는 경우 REST 또는 gRPC를 사용하여 API와 직접 통합해야 할 수 있습니다.

**혜택:**

- **전체 기능 액세스:** OpenAI 호환성 레이어와 달리 API를 직접 사용하면 파일 API에 업로드, 콘텐츠 캐싱 생성, 양방향 Live API 사용과 같은 Gemini 전용 기능을 사용할 수 있습니다.
- **최소 종속 항목:** 크기 또는 감사 비용으로 인해 종속 항목이 민감한 환경입니다. `fetch`와 같은 표준 라이브러리 또는 `httpx`와 같은 래퍼를 통해 API를 직접 사용하면 라이브러리가 경량으로 유지됩니다.
- **언어에 구애받지 않음:** 언어 제한이 없으므로 Rust, PHP, Ruby와 같이 SDK에서 다루지 않는 언어의 유일한 경로입니다.
- **성능:** Direct API에는 초기화 오버헤드가 없으므로 서버리스 함수의 콜드 스타트가 최소화됩니다.

**절충점:**

- **수동 Gemini Enterprise Agent Platform 구현:** SDK와 달리 API를 직접 사용하면 AI Studio (API 키)와 Gemini Enterprise Agent Platform (IAM) 간의 인증 차이가 자동으로 처리되지 않습니다. 두 환경을 모두 지원하려면 별도의 인증 핸들러를 구현해야 합니다.
- **기본 유형 또는 도우미 없음:** 요청 객체에 대한 코드 완성 또는 컴파일 시간 검사를 직접 구현하지 않으면 사용할 수 없습니다. 클라이언트 '도우미'(예: 함수-스키마 변환기)가 없으므로 이 로직을 직접 수동으로 작성해야 합니다.

**권장사항**

Google은 라이브러리의 유형 정의를 생성하는 데 사용할 수 있는 기계 가독형 사양을 제공하므로 수동으로 작성할 필요가 없습니다. 빌드 프로세스 중에 사양을 다운로드하고 유형을 생성하고 컴파일된 코드를 제공합니다.

- **엔드포인트:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## OpenAI SDK 통합

모델별 기능보다 통합 스키마 (OpenAI Chat Completions)를 우선시하는 플랫폼인 경우 이 경로가 가장 빠릅니다.

**혜택:**

- **마찰이 적음:** `baseURL` 및 `apiKey`를 변경하여 Gemini 지원을 추가할 수 있는 경우가 많습니다. 새 코드를 작성하지 않고 Gemini 지원을 추가하여 'Bring Your Own Key' 구현을 통합하는 빠른 방법입니다.
- **제약 조건:** 이 경로는 OpenAI SDK로 제한되고 파일 API와 같은 고급 Gemini 기능이 필요하지 않거나 Google 검색을 사용한 그라운딩과 같은 도구에 대한 지원을 수동으로 추가하지 않는 경우에만 권장됩니다.

**절충점:**

- **기능 제한사항:** 호환성 레이어는 핵심 Gemini 기능에 제한사항을 제공합니다. 사용 가능한 서버 측 도구는 플랫폼마다 다르며 Gemini API 도구와 함께 작동하려면 수동으로 처리해야 할 수 있습니다.
- **번역 오버헤드:** OpenAI 스키마가 Gemini의 아키텍처에 1:1로 매핑되지 않으므로 호환성 레이어를 사용하면 사용자 '검색' 도구를 올바른 플랫폼 도구에 매핑하는 것과 같이 해결하기 위해 추가 구현 작업이 필요한 몇 가지 복잡성이 발생합니다.
  상당한 양의 특수 처리가 필요한 경우 각 플랫폼에 전용 SDK 또는 API를 사용하는 것이 더 가치가 있을 수 있습니다.

**권장사항**

가능한 경우 Gemini API와 직접 통합합니다. 하지만 호환성을 극대화하려면 다양한 제공업체를 인식하고 도구 및 메시지 매핑을 처리할 수 있는 라이브러리를 사용하는 것이 좋습니다.

## 모든 파트너를 위한 권장사항: 클라이언트 식별

플랫폼 또는 라이브러리로 Gemini API를 호출할 때는 `x-goog-api-client` 헤더를 사용하여 클라이언트를 식별해야 합니다.

이렇게 하면 Google에서 특정 트래픽 세그먼트를 식별할 수 있으며 라이브러리에서 특정 오류 패턴이 생성되는 경우 디버깅을 지원하기 위해 연락할 수 있습니다.

`company-product/version` 형식 (예: `acme-framework/1.2.0`)을 사용합니다.

### 구현 예

### 생성형 AI SDK

API 클라이언트를 제공하면 SDK가 자동으로 커스텀 헤더를 내부 헤더에 추가합니다.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## 다음 단계

- [라이브러리 개요](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)를 방문하여
  생성형 AI SDK에 대해 알아보세요.
- [API 참조](https://ai.google.dev/api?hl=ko) 찾아보기
- [OpenAI 호환성 가이드](https://ai.google.dev/gemini-api/docs/openai?hl=ko) 읽어보기

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
