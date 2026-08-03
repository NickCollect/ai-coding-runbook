---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ko
fetched_at: 2026-08-03T04:26:30.433170+00:00
title: "Gemini Live API\ub97c \uc0ac\uc6a9\ud55c \uc2e4\uc2dc\uac04 \ubc88\uc5ed \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Live API를 사용한 실시간 번역

Gemini Live API는 [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=ko) 모델을 사용하여 70개 이상의 언어 간에 지연 시간이 짧은 실시간 음성 간 번역을 지원합니다. 번역 설정으로 Live API를 구성하면 한 언어로 오디오를 스트리밍하고 다른 언어로 번역된 오디오 출력을 수신하여 원활한 실시간 음성 간 번역을 지원할 수 있습니다.

[Google AI Studio에서 실시간 번역 사용해 보기mic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=ko)
[GitHub에서 샘플 앱 클론code](https://github.com/google-gemini/gemini-live-api-examples)
[코딩 에이전트 기술 사용terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko#gemini-live-api-dev)

## 실시간 에이전트와 실시간 번역

둘 다 Live API를 사용하지만 실시간 번역의 정신적 모델은 대화형 실시간 에이전트 상호작용과 다릅니다.

| 실시간 에이전트 | 실시간 번역 |
| --- | --- |
| **모델은 어시스턴트 역할을 합니다.** 사용자를 대신하여 듣고, 추론하고, 조치를 취합니다. | **모델은 통역사 역할을 합니다.** 실시간 번역기 파이프라인으로 작동합니다. |
| **턴 기반 상호작용을 사용합니다.** 일시중지, 의도 감지에 의존하고 중단을 처리합니다. | **연속 스트림 처리를 사용합니다.** 화자가 턴을 기다리지 않고 말하는 대로 번역합니다. |
| **도구 및 에이전트를 지원합니다.** 함수 호출, Google 검색, 안내를 기본적으로 지원합니다. | **번역만 지원합니다.** 지연 시간이 짧은 순수 번역이며 도구나 안내를 지원하지 않습니다. |
| **완전한 멀티모달입니다.** 텍스트, 오디오, 동영상, 이미지 입력을 지원합니다. | **오디오가 제한됩니다.** 엄격한 실시간 지연 시간 임계값을 보장하기 위해 입력이 오디오로 제한됩니다. |
| **세부적인 구성입니다.** 생성, 음성, 도구, 시스템 안내를 사용합니다. | **간소화된 구성입니다.** `target_language_code` 및 `echo_target_language`와 같은 전환을 설정합니다. |

## 시작하기

다음 예에서는 클라이언트를 초기화하고 번역 구성으로 Live API에 연결하는 방법을 보여줍니다.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## 오디오 전송

번역을 위해 음성 입력을 스트리밍하려면 원시 리틀 엔디안 16비트 PCM 오디오를 전송합니다.

- **입력 오디오 형식**: 16kHz의 원시 16비트 PCM (모노, little-endian)
- **출력 오디오 형식**: 24kHz의 원시 16비트 PCM (모노, little-endian)
- **청크 크기 및 지연 시간**: 100ms 청크로 오디오를 전송합니다.

다음 예에서는 오디오 청크를 세션으로 전송하는 방법을 보여줍니다.

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## 구성

번역을 사용 설정하려면 세션 설정 중에 `generationConfig` 내에서 `translationConfig`를 지정해야 합니다.

### 설정 메시지 구성

`generationConfig`는 스크립트를 사용 설정하기 위해 다음 필드를 지원합니다.

- **`inputAudioTranscription`**: 있는 경우 모델이 입력 오디오의 텍스트 스크립트를 전송할 수 있도록 하는 객체입니다.
- **`outputAudioTranscription`**: 있는 경우 모델이 출력 (번역된) 오디오의 텍스트 스크립트를 전송할 수 있도록 하는 객체입니다.

`translationConfig`는 다음 필드를 지원합니다.

- **`targetLanguageCode`**: 모델이 번역할 언어의 [BCP-47 언어 코드](#supported-languages)입니다 (예: 폴란드어의 경우 `"pl"`, 스페인어의 경우 `"es"`). 기본값은 `"en"`입니다.
- **`echoTargetLanguage`**: 이미 대상 언어로 되어 있는 입력 오디오를 처리하는 방법을 나타내는 불리언입니다. `true`로 설정하면 모델이 이미 대상 언어로 되어 있는 입력 오디오를 에코 (앵무새)합니다. `false`로 설정하면 입력 음성이 이미 대상 언어로 되어 있을 때 모델이 무음 상태를 유지합니다. 기본값은 `false`입니다.

다음은 설정 메시지 구조의 예입니다.

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## 클라이언트 측 애플리케이션에서 임시 토큰 사용

클라이언트-서버 애플리케이션의 경우 [임시 토큰](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ko) (현재 `v1beta`에 있음)을 사용하여 API 키가 노출되지 않도록 할 수 있습니다.

실시간 번역에서 임시 토큰을 사용하는 경우 다음 안내를 따르세요.

1. `v1beta` 엔드포인트를 사용해야 합니다.
2. **구성 잠금:** 기본적으로 서버의 토큰 생성 제약 조건에서 `translationConfig`를 지정해야 합니다. 이렇게 하면 번역 구성이 잠기고 클라이언트에서 조작할 수 없습니다.
3. **구성 잠금 해제:** 클라이언트 측에서 `translationConfig`를 설정할 수 있도록 하려면 (예: 사용자가 자체 대상 언어를 선택할 수 있도록 하기 위해) 토큰 생성 요청에서 이를 생략하고 대신 `"lock_additional_fields": []`를 설정해야 합니다. 이렇게 하면 클라이언트 측에서 설정할 수 있도록 `translationConfig`가 잠금 해제됩니다.

### 제약 조건이 있는 임시 토큰 만들기

다음 예에서는 번역 제약 조건이 있는 임시 토큰을 만드는 방법을 보여줍니다.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## 제한사항

- **입력 모드**: 번역에는 오디오 입력만 지원됩니다. 텍스트 입력은 지원되지 않습니다.
- **음성 복제**: 음성 복제가 일관되지 않을 수 있습니다. 긴 일시중지 후 음성이 변경되거나, 음성이 시작되는 방식에 따라 잘못된 성별이 할당되거나, 여러 화자가 빠르게 대화하는 동안 한 음성에 갇힐 수 있습니다.
- **언어 감지**: 언어 감지는 강한 악센트, 유사한 언어 (예: 스페인어와 포르투갈어), 빠른 언어 전환에 어려움을 겪습니다. **참고:** 이는 입력 스크립트에만 영향을 미칩니다. 언어 코드와 최종 번역은 여전히 정확해야 합니다.
- **백그라운드 오디오**: 모델은 노이즈와 음악을 필터링하여 깨끗한 음성을 생성하도록 설계되었지만 모든 백그라운드 오디오가 무시되지는 않을 수 있습니다.
- **에코 대상 언어**: `echoTargetLanguage: true`인 경우 입력 오디오가 이미 대상 언어로 되어 있을 때 배경 소음이나 음악으로 인해 번역된 오디오에 아티팩트가 발생할 수 있습니다.

## 지원 언어

실시간 번역에 지원되는 언어는 다음과 같습니다.

| 언어 | BCP-47 코드 | 언어 | BCP-47 코드 |
| --- | --- | --- | --- |
| 아프리칸스어 | af | 카자흐어 | kk |
| Akan | ak | 크메르어 | km |
| 알바니아어 | sq | 키냐르완다어 | rw |
| 암하라어 | am | 한국어 | ko |
| 아랍어 | ar | 라오어 | lo |
| 아르메니아어 | hy | 라트비아어 | lv |
| 아제르바이잔어 | az | 리투아니아어 | lt |
| 바스크어 | eu | 마케도니아어 | mk |
| 벨라루스어 | be | 말레이어 | ms |
| 뱅골어 | bn | 말라얄람어 | ml |
| 불가리아어 | bg | 마라타어 | mr |
| 버마어 (미얀마) | my | 몽골어 | mn |
| 카탈로니아어 | ca | 네팔어 | ne |
| 중국어 (간체) | zh-Hans | 노르웨이어 | no, nb |
| 중국어 (번체) | zh-Hant | 페르시아어 | fa |
| 크로아티아어 | hr | 폴란드어 | pl |
| 체코어 | cs | 포르투갈어 (브라질) | pt-BR |
| 덴마크어 | da | 포르투갈어 (포르투갈) | pt-PT |
| 네덜란드어 | nl | 펀자브어 | pa |
| 영어 | en | 루마니아어 | ro |
| 에스토니아어 | et | 러시아어 | ru |
| 필리핀어 | fil | 세르비아어 | sr |
| 핀란드어 | fi | 신드어 | sd |
| 프랑스어 | fr | 싱할라어 | si |
| 갈리시아어 | gl | 슬로바키아어 | sk |
| 조지아어 | ka | 슬로베니아어 | sl |
| 독일어 | de | 스페인어 | es |
| 그리스어 | el | 순다어 | su |
| 구자라트어 | gu | 스와힐리어 | sw |
| 하우사어 | ha | 스웨덴어 | sv |
| 히브리어 | he | 타밀어 | ta |
| 힌디어 | hi | 텔루구어 | te |
| 헝가리어 | hu | 태국어 | th |
| 아이슬란드어 | is | 튀르키예어 | tr |
| 인도네시아어 | id | 우크라이나어 | uk |
| 이탈리아어 | it | 우르두어 | ur |
| 일본어 | ja | 우즈베크어 | uz |
| 자바어 | jv | 베트남어 | vi |
| 칸나다어 | kn | 줄루어 | zu |

## 다음 단계

- 전체 Live API [기능](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko) 가이드를 읽어보세요.
- [SDK 시작하기](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ko) 가이드를 읽어보세요.
- [WebSocket 시작하기](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ko) 가이드를 읽어보세요.
- 클라이언트-서버 애플리케이션의 보안 인증에 관한 [임시 토큰](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ko) 가이드를 읽어보세요.
- GitHub에서 [Live API 예시](https://github.com/google-gemini/gemini-live-api-examples)를 클론합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-23(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-23(UTC)"],[],[]]
