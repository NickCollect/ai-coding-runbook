---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko
fetched_at: 2026-10-05T06:27:56.231505+00:00
title: "Live API\ub97c \uc0ac\uc6a9\ud55c \uc138\uc158 \uad00\ub9ac \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Live API를 사용한 세션 관리

Live API에서 세션은 입력 및 출력이 동일한
연결을 통해 지속적으로 스트리밍되는 영구
연결을 나타냅니다 ([작동 방식](https://ai.google.dev/gemini-api/docs/live?hl=ko)에 대해 자세히 알아보기).
이 고유한 세션 설계는 지연 시간이 짧고 고유한 기능을 지원하지만 세션 시간 제한 및 조기 종료와 같은 문제를 일으킬 수도 있습니다.
이 가이드에서는 Live API를 사용할 때 발생할 수 있는 세션 관리 문제를 해결하기 위한 전략을 다룹니다.

## 세션 수명

압축이 없으면 오디오 전용 세션은 15분으로 제한되고 오디오-동영상 세션은 2분으로 제한됩니다. 이러한 제한을 초과하면
세션 (따라서 연결)이 종료되지만
[컨텍스트 윈도우 압축](#context-window-compression)을 사용하여 세션을
무제한으로 확장할 수 있습니다.

연결 수명도 약 10분으로 제한됩니다. 연결이 종료되면 세션도 종료됩니다. 이 경우
세션 재개
[를 사용하여](#session-resumption) 여러 연결에서 활성 상태를 유지하도록 단일 세션을 구성할 수 있습니다.
또한 연결이 종료되기 전에 [GoAway 메시지](#goaway-message)를 수신하여 추가 조치를 취할 수 있습니다.

## 컨텍스트 윈도우 압축

세션을 더 길게 사용 설정하고 갑작스러운 연결 종료를 방지하려면 세션 구성의 일부로 [contextWindowCompression](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) 필드를 설정하여 컨텍스트 윈도우 압축을 사용 설정하면 됩니다.

[ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=ko#contextwindowcompressionconfig)에서
[슬라이딩 윈도우 메커니즘](https://ai.google.dev/api/live?hl=ko#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
과 [압축을 트리거하는 토큰 수](https://ai.google.dev/api/live?hl=ko#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
를 구성할 수 있습니다.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## 세션 재개

서버가 WebSocket
연결을 주기적으로 재설정할 때 세션이 종료되지 않도록 하려면 [sessionResumption](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
필드를 [설정 구성](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentSetup) 내에서 구성합니다.

이 구성을 전달하면 서버가 [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=ko#SessionResumptionUpdate) 메시지를 전송합니다. 이 메시지는 후속 연결의 마지막 재개 토큰을 [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=ko#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)로 전달하여 세션을 재개하는 데 사용할 수 있습니다.

재개 토큰은 마지막 세션 종료 후 2시간 동안 유효합니다.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## 세션 연결 해제 전에 메시지 수신

서버는 현재 연결이 곧 종료됨을 알리는 [GoAway](https://ai.google.dev/api/live?hl=ko#GoAway) 메시지를 보냅니다. 이 메시지에는 남은 시간을 나타내는 [timeLeft](https://ai.google.dev/api/live?hl=ko#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left)가 포함되어 있으며 연결이 ABORTED로 종료되기 전에 추가 조치를 취할 수 있습니다.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## 생성이 완료되면 메시지 수신

서버는 모델이 응답 생성을 완료했음을 알리는 [generationComplete](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
메시지를 보냅니다.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## 다음 단계

전체
[기능](https://ai.google.dev/gemini-api/docs/live?hl=ko) 가이드,
[도구 사용](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko) 페이지 또는
[Live API Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ko)에서 Live API를 사용하는 다양한 방법을 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-17(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-17(UTC)"],[],[]]
