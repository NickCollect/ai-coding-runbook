---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=ko
fetched_at: 2026-08-24T02:31:27.622526+00:00
title: "API \uc624\ub958 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# API 오류

이 페이지에서는 `GenerateContent` API에서 반환되는 백엔드 오류 코드에 대한 참조를 제공하고, gRPC 오류 응답 형식을 설명하며, 문제 해결 단계를 제공합니다.

## HTTP 오류 코드

다음 표에는 일반적인 백엔드 오류 코드, 원인에 대한 설명, 권장되는 해결 방법이 나와 있습니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP 코드** | **상태** | **설명** | **예** | **솔루션** |
| 400 | INVALID\_ARGUMENT | 요청 본문의 형식이 잘못되었습니다. | 요청에 오타가 있거나 필수 입력란이 누락되었습니다. | 요청 형식, 예, 지원되는 버전은 [API 참조](https://ai.google.dev/api?hl=ko)를 확인하세요. 이전 엔드포인트에서 최신 API 버전의 기능을 사용하면 오류가 발생할 수 있습니다. |
| 400 | FAILED\_PRECONDITION | 거주 국가에서는 Gemini API 무료 등급을 이용할 수 없습니다. Google AI Studio에서 프로젝트에 결제를 사용 설정하세요. | 무료 등급이 지원되지 않는 리전에서 요청을 하고 있으며 Google AI Studio에서 프로젝트에 결제를 사용 설정하지 않았습니다. | Gemini API를 사용하려면 [Google AI Studio](https://aistudio.google.com/apikey?hl=ko)를 사용하여 유료 요금제를 설정해야 합니다. |
| 403 | PERMISSION\_DENIED | API 키에 필요한 권한이 없습니다. | [잘못된 API 키를 사용하고 있습니다. 적절한 인증을 거치지 않고 미세 조정된 모델을 사용하려고 합니다.](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ko) | API 키가 설정되어 있고 올바른 액세스 권한이 있는지 확인합니다. 미세 조정된 모델을 사용하려면 적절한 인증을 거쳐야 합니다. |
| 404 | NOT\_FOUND | 요청한 리소스를 찾을 수 없습니다. | 요청에서 참조된 이미지, 오디오 또는 동영상 파일을 찾을 수 없습니다. | 요청의 모든 매개변수가 API 버전에 유효한지 확인합니다. |
| 429 | RESOURCE\_EXHAUSTED | API의 비율 제한 (RPM, TPM, RPD, 지출 등) 중 하나를 초과했습니다. | 요청을 너무 많이 보내거나, 토큰을 너무 많이 사용하거나, 계정의 결제 내역 및 등급에 대한 지출 기반 한도를 초과하고 있습니다. | 모델의 [비율 제한](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko) 내에 있는지 확인합니다. 잠시 기다렸다가 다시 시도합니다. 요청의 비율 또는 크기를 줄입니다. [필요한 경우 비율 제한 상향 조정을 요청합니다.](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko#request-rate-limit-increase) |
| 499 | CANCELLED | 작업이 취소되었습니다. 대개 호출자에 의해 취소됩니다. | API가 응답을 완료하기 전에 클라이언트가 연결을 닫았습니다. | 클라이언트 또는 네트워크 인프라가 클라이언트 측 제한 시간으로 인해 연결을 너무 일찍 닫는지 확인합니다. |
| 500 | 내부 | Google 측에서 예기치 않은 오류가 발생했습니다. | 입력 컨텍스트가 너무 깁니다. | [Gemini API 상태 페이지](https://aistudio.google.com/status?hl=ko)에서 진행 중인 인시던트를 확인합니다. 입력 컨텍스트를 줄이거나 다른 모델로 일시적으로 전환 (예: Gemini 2.5 Pro에서 Gemini 2.5 Flash로)하여 작동하는지 확인합니다. 또는 잠시 기다렸다가 요청을 다시 시도합니다. 다시 시도한 후에도 문제가 지속되면 Google AI Studio의 **의견 보내기** 버튼을 사용하여 신고해 주세요. |
| 503 | 현재 구매할 수 없음 | 서비스가 일시적으로 과부하되거나 다운되었을 수 있습니다. | 서비스의 용량이 일시적으로 부족합니다. | [Gemini API 상태 페이지](https://aistudio.google.com/status?hl=ko)에서 진행 중인 인시던트를 확인합니다. 다른 모델로 일시적으로 전환 (예: Gemini 2.5 Pro에서 Gemini 2.5 Flash로)하여 작동하는지 확인합니다. 또는 잠시 기다렸다가 요청을 다시 시도합니다. 다시 시도한 후에도 문제가 지속되면 Google AI Studio의 **의견 보내기** 버튼을 사용하여 신고해 주세요. |
| 504 | DEADLINE\_EXCEEDED | 서비스가 기한 내에 처리를 완료할 수 없습니다. | 프롬프트 (또는 컨텍스트)가 너무 커서 제때 처리할 수 없습니다. | 이 오류를 방지하려면 클라이언트 요청에서 '제한 시간'을 더 크게 설정하세요. |

## 오류 응답 형식

`GenerateContent` 요청이 실패하면 API는 HTTP 상태 코드 (예: `400 Bad Request`, `403 Forbidden`, `429 Too Many Requests`)를 설정하고 gRPC 상태 세부정보가 포함된 JSON 응답 본문을 반환합니다.

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `code` | 정수 | HTTP 상태 코드 |
| `message` | 문자열 | 사람이 읽을 수 있는 오류 설명 |
| `status` | 문자열 | `SCREAMING_CASE`의 gRPC 상태 코드 |
| `details` | 배열 | `ErrorInfo` 또는 `LocalizedMessage`와 같은 추가 오류 컨텍스트 |

## 다음 단계

- [API 문제 해결](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ko): 일반적인 문제 및 오류 시나리오를 해결합니다.
- [비율 제한](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko): 요청 한도 및 할당량 처리에 대해 알아봅니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
