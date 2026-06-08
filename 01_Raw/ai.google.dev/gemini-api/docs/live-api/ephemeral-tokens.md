---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ko
fetched_at: 2026-06-08T05:31:58.758879+00:00
title: "\uc784\uc2dc \ud1a0\ud070 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 임시 토큰

단기 토큰은 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)을 통해 Gemini
API에 액세스하기 위한 단기 인증 토큰입니다. 사용자의 기기에서 API로 직접 연결할 때
보안을 강화하도록 설계되었습니다 (a
[클라이언트-서버](https://ai.google.dev/gemini-api/docs/live?hl=ko#implementation-approach)
구현). 표준 API 키와 마찬가지로 단기 토큰은 웹브라우저 또는 모바일 앱과 같은 클라이언트 측 애플리케이션에서 추출할 수 있습니다. 하지만 단기 토큰은 빠르게 만료되고 제한될 수 있으므로 프로덕션 환경에서 보안 위험을 크게 줄입니다. 클라이언트 측 애플리케이션에서 Live API에 직접 액세스할 때 API 키 보안을 강화하기 위해 단기 토큰을 사용해야 합니다.

## 단기 토큰 작동 방식

단기 토큰의 작동 방식은 다음과 같습니다.

1. 클라이언트 (예: 웹 앱)가 백엔드로 인증합니다.
2. 백엔드가 Gemini API의 프로비저닝 서비스에서 단기 토큰을 요청합니다.
3. Gemini API가 단기 토큰을 발급합니다.
4. 백엔드가 Live API에 대한 WebSocket 연결을 위해 클라이언트에 토큰을 전송합니다. API 키를 단기 토큰으로 교체하여 이 작업을 실행할 수 있습니다.
5. 그러면 클라이언트가 토큰을 API 키인 것처럼 사용합니다.

![임시 토큰 개요](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=ko)

이렇게 하면 클라이언트 측에 배포된 장기 API 키와 달리 토큰이 추출되더라도 단기적이므로 보안이 강화됩니다. 클라이언트가 데이터를 Gemini로 직접 전송하므로 지연 시간도 개선되고 백엔드가 실시간 데이터를 프록시할 필요가 없습니다.

## 단기 토큰 만들기

다음은 Gemini에서 단기 토큰을 가져오는 방법을 보여주는 간단한 예입니다.
기본적으로 이 요청의 토큰 (`newSessionExpireTime`)을 사용하여 새 Live API 세션을 시작하는 데 1분이 주어지고 해당 연결을 통해 메시지를 전송하는 데 30분이 주어집니다 (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

`expireTime` 값 제약조건, 기본값, 기타 필드 사양은
[API 참조](https://ai.google.dev/api/live?hl=ko#ephemeral-auth-tokens)를 확인하세요.
`expireTime` 기간 내에 10분마다 호출을 다시 연결하려면
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=ko#session-resumption)이 필요합니다 (`uses: 1`인 경우에도 동일한 토큰으로 실행할 수 있음).

단기 토큰을 구성 집합에 잠글 수도 있습니다. 이는 애플리케이션의 보안을 더욱 개선하고 시스템 안내를 서버 측에 유지하는 데 유용할 수 있습니다.

### Python

```
from google import genai

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

필드의 하위 집합을 잠글 수도 있습니다. 자세한 내용은 [SDK 문서](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
를 참고하세요.

## 단기 토큰으로 Live API에 연결

단기 토큰이 있으면 API 키인 것처럼 사용합니다. 하지만 Live API에서만 작동하고 API의 `v1alpha` 버전에서만 작동합니다.

[단기 토큰을 사용하면 클라이언트-서버 구현 접근 방식을 따르는 애플리케이션
을 배포할 때만 가치가 추가됩니다.](https://ai.google.dev/gemini-api/docs/live?hl=ko#implementation-approach)

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

자세한 예는 [Live API 시작하기](https://ai.google.dev/gemini-api/docs/live?hl=ko)를 참고하세요.

## 권장사항

- `expire_time` 매개변수를 사용하여 짧은 만료 기간을 설정합니다.
- 토큰이 만료되어 프로비저닝 프로세스를 다시 시작해야 합니다.
- 자체 백엔드의 보안 인증을 확인합니다. 단기 토큰은 백엔드 인증 방법만큼만 안전합니다.
- 일반적으로 이 경로는 일반적으로 안전한 것으로 간주되므로 백엔드-Gemini 연결에 단기 토큰을 사용하지 않는 것이 좋습니다.

## 제한사항

현재 단기 토큰은 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)와만 호환됩니다.

## 다음 단계

- 자세한 내용은 단기 토큰에 관한 Live API [참조](https://ai.google.dev/api/live?hl=ko#ephemeral-auth-tokens)
  를 읽어보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-29(UTC)"],[],[]]
