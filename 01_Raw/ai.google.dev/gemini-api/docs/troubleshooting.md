---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ko
fetched_at: 2026-05-05T13:25:26.297653+00:00
title: "\ubb38\uc81c \ud574\uacb0 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/문서)

의견 보내기

# 문제 해결 가이드

이 가이드를 사용하여 Gemini API를 호출할 때 발생하는 일반적인 문제를 진단하고 해결하세요. Gemini API 백엔드 서비스 또는 클라이언트 SDK에서 문제가 발생할 수 있습니다. 클라이언트 SDK는 다음 저장소에서 오픈소스로 제공됩니다.

- [python-genai](https://ai.google.dev/gemini-api/docs/python-genai)
- [js-genai](https://ai.google.dev/gemini-api/docs/js-genai)
- [go-genai](https://ai.google.dev/gemini-api/docs/go-genai)

API 키 문제가 발생하면 [API 키 설정 가이드](https://ai.google.dev/gemini-api/docs/API 키 설정 가이드)에 따라 API 키를 올바르게 설정했는지 확인하세요.

## Gemini API 백엔드 서비스 오류 코드

다음 표에는 발생할 수 있는 일반적인 백엔드 오류 코드와 원인 설명, 문제 해결 단계가 나와 있습니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP 코드** | **상태** | **설명** | **예** | **해결 방법** |
| 400 | INVALID\_ARGUMENT | 요청 본문의 형식이 잘못되었습니다. | 요청에 오타가 있거나 필수 입력란이 누락되었습니다. | 요청 형식, 예시, 지원되는 버전은 [API 참조](https://ai.google.dev/gemini-api/docs/API 참조)를 확인하세요. 이전 엔드포인트에서 최신 API 버전의 기능을 사용하면 오류가 발생할 수 있습니다. |
| 400 | FAILED\_PRECONDITION | 거주 국가에서는 Gemini API 무료 등급을 이용할 수 없습니다. Google AI Studio에서 프로젝트에 결제를 사용 설정하세요. | 무료 등급이 지원되지 않는 리전에서 요청을 하고 있으며 Google AI Studio에서 프로젝트에 결제를 사용 설정하지 않았습니다. | Gemini API를 사용하려면 [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio)를 사용하여 유료 요금제를 설정해야 합니다. |
| 403 | PERMISSION\_DENIED | API 키에 필요한 권한이 없습니다. | 잘못된 API 키를 사용하고 있습니다. [적절한 인증](https://ai.google.dev/gemini-api/docs/적절한 인증)을 거치지 않고 조정된 모델을 사용하려고 합니다. | API 키가 설정되어 있고 올바른 액세스 권한이 있는지 확인합니다. 조정된 모델을 사용하려면 적절한 인증을 거쳐야 합니다. |
| 404 | NOT\_FOUND | 요청한 리소스를 찾을 수 없습니다. | 요청에서 참조된 이미지, 오디오 또는 동영상 파일을 찾을 수 없습니다. | API 버전에 대해 [요청의 모든 매개변수가 유효한지](https://ai.google.dev/gemini-api/docs/요청의 모든 매개변수가 유효한지) 확인합니다. |
| 429 | RESOURCE\_EXHAUSTED | 비율 제한을 초과했습니다. | 무료 등급 Gemini API로 분당 너무 많은 요청을 보내고 있습니다. | 모델의 [속도 제한](https://ai.google.dev/gemini-api/docs/속도 제한) 내에 있는지 확인합니다. 필요한 경우 [할당량 상향 조정을 요청](https://ai.google.dev/gemini-api/docs/할당량 상향 조정을 요청)합니다. |
| 500 | 내부 | Google 측에서 예기치 않은 오류가 발생했습니다. | 입력 컨텍스트가 너무 깁니다. | [Gemini API 상태 페이지](https://ai.google.dev/gemini-api/docs/Gemini API 상태 페이지)에서 진행 중인 사고가 있는지 확인합니다. 입력 컨텍스트를 줄이거나 다른 모델 (예: Gemini 2.5 Pro에서 Gemini 2.5 Flash로)로 일시적으로 전환하여 작동하는지 확인합니다. 또는 잠시 기다렸다가 요청을 다시 시도하세요. 다시 시도한 후에도 문제가 지속되면 Google AI Studio의 **의견 보내기** 버튼을 사용하여 신고해 주세요. |
| 503 | 현재 구매할 수 없음 | 서비스가 일시적으로 과부하되거나 다운되었을 수 있습니다. | 서비스의 용량이 일시적으로 부족합니다. | [Gemini API 상태 페이지](https://ai.google.dev/gemini-api/docs/Gemini API 상태 페이지)에서 진행 중인 사고가 있는지 확인합니다. 일시적으로 다른 모델 (예: Gemini 2.5 Pro에서 Gemini 2.5 Flash로)로 전환하여 작동하는지 확인합니다. 또는 잠시 기다렸다가 요청을 다시 시도하세요. 다시 시도한 후에도 문제가 지속되면 Google AI Studio의 **의견 보내기** 버튼을 사용하여 신고해 주세요. |
| 504 | DEADLINE\_EXCEEDED | 서비스가 기한 내에 처리를 완료할 수 없습니다. | 프롬프트 (또는 컨텍스트)가 너무 커서 제때 처리할 수 없습니다. | 이 오류를 방지하려면 클라이언트 요청에서 'timeout'을 더 크게 설정하세요. |

## 모델 매개변수 오류가 있는지 API 호출 확인

모델 파라미터가 다음 값 범위 내에 있는지 확인합니다.

|  |  |
| --- | --- |
| **모델 매개변수** | **값 (범위)** |
| 후보 수 | 1~8 (정수) |
| 온도 | 0.0~1.0 |
| 최대 출력 토큰 | [모델 페이지](https://ai.google.dev/gemini-api/docs/모델 페이지)를 사용하여 사용 중인 모델의 최대 토큰 수를 확인합니다. |
| TopP | 0.0~1.0 |

매개변수 값을 확인하는 것 외에도 필요한 기능을 지원하는 올바른 [API 버전](https://ai.google.dev/gemini-api/docs/API 버전) (예: `/v1` 또는 `/v1beta`)과 모델을 사용하고 있는지 확인하세요. 예를 들어 기능이 베타 버전인 경우 `/v1beta` API 버전에서만 사용할 수 있습니다.

## 올바른 모델이 있는지 확인

[모델 페이지](https://ai.google.dev/gemini-api/docs/모델 페이지)에 나열된 지원되는 모델을 사용하고 있는지 확인합니다.

## 2.5 모델의 지연 시간 또는 토큰 사용량이 더 높음

2.5 Flash 및 Pro 모델에서 지연 시간 또는 토큰 사용량이 더 높은 경우 품질을 향상하기 위해 **사고가 기본적으로 사용 설정**되어 있기 때문일 수 있습니다. 속도를 우선시하거나 비용을 최소화해야 하는 경우 생각을 조정하거나 사용 중지할 수 있습니다.

안내 및 샘플 코드는 [생각 페이지](https://ai.google.dev/gemini-api/docs/생각 페이지)를 참고하세요.

## 안전 문제

API 호출의 안전 설정으로 인해 프롬프트가 차단된 경우 API 호출에서 설정한 필터를 기준으로 프롬프트를 검토하세요.

`BlockedReason.OTHER`가 표시되면 질문 또는 대답이 [서비스 약관](https://ai.google.dev/gemini-api/docs/서비스 약관)을 위반하거나 지원되지 않는 것일 수 있습니다.

## 인용 문제

인용 이유로 인해 모델이 출력을 중지하는 경우 모델 출력이 특정 데이터와 유사할 수 있음을 의미합니다. 이 문제를 해결하려면 프롬프트 / 컨텍스트를 최대한 고유하게 만들고 더 높은 온도를 사용해 보세요.

## 반복적인 토큰 문제

출력 토큰이 반복되는 경우 다음 제안을 따라 토큰을 줄이거나 없애 보세요.

| 설명 | 원인 | 추천 해결 방법 |
| --- | --- | --- |
| 마크다운 표에서 하이픈이 반복됨 | 모델이 시각적으로 정렬된 마크다운 테이블을 만들려고 할 때 테이블의 콘텐츠가 길면 이 문제가 발생할 수 있습니다. 하지만 마크다운의 정렬은 올바른 렌더링에 필요하지 않습니다. | 프롬프트에 안내를 추가하여 마크다운 표를 생성하기 위한 구체적인 가이드라인을 모델에 제공합니다. 이러한 가이드라인을 따르는 예를 제공합니다. 온도를 조정해 볼 수도 있습니다. 코드를 생성하거나 마크다운 표와 같은 매우 구조화된 출력을 생성하는 경우 온도가 높을수록 (>= 0.8) 더 나은 결과를 얻을 수 있습니다.  다음은 이 문제를 방지하기 위해 프롬프트에 추가할 수 있는 가이드라인의 예시입니다.     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| 마크다운 표의 반복 토큰 | 반복되는 하이픈과 마찬가지로 모델이 표의 콘텐츠를 시각적으로 정렬하려고 할 때 발생합니다. 마크다운의 정렬은 올바른 렌더링에 필요하지 않습니다. | - 시스템 프롬프트에 다음과 같은 요청 사항을 추가해 보세요.      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 온도를 조정해 보세요. 온도가 높을수록 (>= 0.8) 일반적으로 출력에서 반복이나 중복을 없애는 데 도움이 됩니다. |
| 구조화된 출력에서 반복되는 줄바꿈 (`\n`) | 모델 입력에 유니코드나 `\u`, `\t`와 같은 이스케이프 시퀀스가 포함되면 줄바꿈이 반복될 수 있습니다. | - 프롬프트에서 금지된 이스케이프 시퀀스를 확인하고 UTF-8 문자로 대체합니다. 예를 들어 JSON 예시에 있는 `\u` 이스케이프 시퀀스로 인해 모델이 출력에서도 이를 사용할 수 있습니다. - 허용된 이스케이프에 관해 모델에 안내합니다. 다음과 같은 시스템 안내를 추가합니다.      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 구조화된 출력을 사용할 때 텍스트가 반복됨 | 모델 출력의 필드 순서가 정의된 구조화된 스키마와 다르면 텍스트가 반복될 수 있습니다. | - 프롬프트에서 필드의 순서를 지정하지 마세요. - 모든 출력 필드를 필수 항목으로 만듭니다. |
| 반복적인 도구 호출 | 이 문제는 모델이 이전 생각의 맥락을 잃거나 사용할 수 없는 엔드포인트를 호출해야 하는 경우에 발생할 수 있습니다. | 모델에 사고 과정 내에서 상태를 유지하도록 지시합니다. 시스템 요청 사항 끝에 다음을 추가합니다.    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 구조화된 출력에 포함되지 않는 반복적인 텍스트 | 모델이 해결할 수 없는 요청에 갇히면 이 문제가 발생할 수 있습니다. | - 사고가 사용 설정된 경우, 문제에 대해 생각하는 방법을 안내에 명시적으로 지시하지 마세요. 최종 출력을 요청하기만 하면 됩니다. - 온도를 0.8 이상으로 높여 보세요. - '간결하게 작성해', '반복하지 마', '답변은 한 번만 제공해'와 같은 요청 사항을 추가합니다. |

## 차단되거나 작동하지 않는 API 키

이 섹션에서는 Gemini API 키가 차단되었는지 확인하는 방법과 차단된 경우 취해야 할 조치를 설명합니다.

### 키가 차단된 이유 이해하기

일부 API 키가 공개적으로 노출되었을 수 있는 취약점이 확인되었습니다. 데이터를 보호하고 무단 액세스를 방지하기 위해 Google은 유출된 것으로 알려진 키가 Gemini API에 액세스하지 못하도록 사전 조치를 취했습니다.

### 키가 영향을 받는지 확인하기

키가 유출된 것으로 알려진 경우 더 이상 Gemini API에서 해당 키를 사용할 수 없습니다. [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio)를 사용하여 Gemini API 호출이 차단된 API 키가 있는지 확인하고 새 키를 생성할 수 있습니다. 이러한 키를 사용하려고 하면 다음 오류가 반환될 수도 있습니다.

```
Your API key was reported as leaked. Please use another API key.
```

### 차단된 API 키에 대한 작업

[Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio)를 사용하여 Gemini API 통합을 위한 새 API 키를 생성해야 합니다. 새 키가 안전하게 유지되고 공개적으로 노출되지 않도록 API 키 관리 관행을 검토하는 것이 좋습니다.

### 취약점으로 인한 예상치 못한 요금

[결제 지원 케이스를 제출](https://ai.google.dev/gemini-api/docs/결제 지원 케이스를 제출)합니다.
Google 결제팀에서 이 문제를 해결하기 위해 노력하고 있으며, 최대한 빨리 업데이트를 알려드리겠습니다.

### 유출된 키에 대한 Google의 보안 조치

**API 키가 유출되면 Google은 비용 초과 및 악용으로부터 내 계정을 어떻게 보호하나요?**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio)를 사용하여 새 키를 요청할 때 API 키를 발급하는 방향으로 나아가고 있습니다. 이 API 키는 기본적으로 Google AI Studio로만 제한되며 다른 서비스의 키는 허용되지 않습니다.
  이렇게 하면 의도하지 않은 교차 키 사용을 방지할 수 있습니다.
- 비용 및 애플리케이션 데이터의 악용을 방지하기 위해 유출되어 Gemini API와 함께 사용되는 API 키는 기본적으로 차단됩니다.
- [Google AI Studio](https://ai.google.dev/gemini-api/docs/Google AI Studio)에서 API 키의 상태를 확인할 수 있으며, 즉각적인 조치를 위해 API 키가 유출된 것으로 확인되면 선제적으로 알려드릴 것입니다.

## 모델 출력 개선

모델 출력의 품질을 높이려면 더 구조화된 프롬프트를 작성해 보세요. [프롬프트 엔지니어링 가이드](https://ai.google.dev/gemini-api/docs/프롬프트 엔지니어링 가이드) 페이지에서는 시작하는 데 도움이 되는 몇 가지 기본 개념, 전략, 권장사항을 소개합니다.

## 토큰 한도 이해하기

[토큰 가이드](https://ai.google.dev/gemini-api/docs/토큰 가이드)를 읽고 토큰 수와 한도를 파악하세요.

## 알려진 문제

- API는 일부 언어만 지원합니다. 지원되지 않는 언어로 프롬프트를 제출하면 예상치 못한 응답이 생성되거나 응답이 차단될 수 있습니다. [사용 가능한 언어](https://ai.google.dev/gemini-api/docs/사용 가능한 언어)에서 업데이트를 확인하세요.

## 버그 신고

궁금한 점이 있으면 [Google AI 개발자 포럼](https://ai.google.dev/gemini-api/docs/Google AI 개발자 포럼)에서 토론에 참여하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-30(UTC)

의견을 전달하고 싶나요?
