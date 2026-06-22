---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ko
fetched_at: 2026-06-22T06:25:10.849492+00:00
title: "Google \uc0dd\uc131\ud615 AI SDK\ub97c \uc0ac\uc6a9\ud558\uc5ec Gemini Live API \uc2dc\uc791\ud558\uae30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google 생성형 AI SDK를 사용하여 Gemini Live API 시작하기

Gemini Live API를 사용하면 Gemini 모델과 실시간 양방향 상호작용이 가능하며 오디오, 동영상, 텍스트 입력과 네이티브 오디오 출력을 지원합니다. 이 가이드에서는 서버에서 Google 생성형 AI SDK를 사용하여 API와 통합하는 방법을 설명합니다.

[Google AI Studio에서 Live API 사용해 보기mic](https://aistudio.google.com/live?hl=ko)
[GitHub에서 샘플 앱 클론code](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[코딩 에이전트 기술 사용하기terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko)

## 개요

Gemini Live API는 실시간 통신에 WebSockets를 사용합니다. `google-genai` SDK는 이러한 연결을 관리하기 위한 고급 비동기 인터페이스를 제공합니다.

주요 개념

- **세션**: 모델에 대한 영구 연결입니다.
- **구성**: 모달리티 (오디오/텍스트), 음성, 시스템 안내를 설정합니다.
- **실시간 입력**: 오디오 및 동영상 프레임을 blob으로 전송합니다.

## Live API에 연결

API 키로 Live API 세션을 시작합니다.

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## 텍스트 전송 중

텍스트는 `send_realtime_input` (Python) 또는 `sendRealtimeInput` (자바스크립트)을 사용하여 전송할 수 있습니다.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## 오디오 전송

오디오는 원시 PCM 데이터 (원시 16비트 PCM 오디오, 16kHz, 리틀 엔디안)로 전송해야 합니다.

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

클라이언트 기기 (예: 브라우저)에서 오디오를 가져오는 방법의 예는
[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70)의 포괄적인 예시를 참고하세요.

## 동영상 전송 중

동영상 프레임은 특정 프레임 속도 (초당 최대 1프레임)로 개별 이미지 (예: JPEG 또는 PNG)로 전송됩니다.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

클라이언트 기기 (예: 브라우저)에서 동영상을 가져오는 방법의 예는 [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120)의 포괄적인 예시를 참고하세요.

## 오디오 수신 중

모델의 오디오 응답은 데이터 청크로 수신됩니다.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

GitHub의 샘플 앱을 참고하여 서버에서 오디오를 [수신](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98)하고 브라우저에서 [재생](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174)하는 방법을 알아보세요.

## 텍스트 수신 중

사용자 입력과 모델 출력의 스크립트는 서버 콘텐츠에서 확인할 수 있습니다.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## 도구 호출 처리

API는 도구 호출 (함수 호출)을 지원합니다. 모델이 도구 호출을 요청하면 함수를 실행하고 응답을 다시 전송해야 합니다.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## 다음 단계

- 음성 활동 감지 및 네이티브 오디오 기능을 비롯한 주요 기능 및 구성은 전체 Live API [기능](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko) 가이드를 참고하세요.
- [도구 사용](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko) 가이드를 참고하여 Live API를 도구 및 함수 호출과 통합하는 방법을 알아보세요.
- 장기 실행 대화를 관리하려면 [세션 관리](https://ai.google.dev/gemini-api/docs/live-session?hl=ko) 가이드를 참고하세요.
- [클라이언트-서버 애플리케이션에서 보안 인증을 하려면 [임시 토큰](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ko) 가이드를 참고하세요.](#implementation-approach)
- 기본 WebSockets API에 관한 자세한 내용은 [WebSockets API 참조](https://ai.google.dev/api/live?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
