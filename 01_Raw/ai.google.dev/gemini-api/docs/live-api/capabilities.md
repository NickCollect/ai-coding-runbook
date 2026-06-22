---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko
fetched_at: 2026-06-22T06:27:13.696666+00:00
title: "Live API \uae30\ub2a5 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Live API 기능 가이드

Live API에서 사용할 수 있는 기능과 구성을 다루는 포괄적인 가이드입니다.
일반적인 사용 사례의 개요와 샘플 코드는 [Live API 시작하기](https://ai.google.dev/gemini-api/docs/live?hl=ko) 페이지를 참고하세요.

## 시작하기 전에

- **핵심 개념 숙지:** 아직 하지 않았다면 먼저 [Live API 시작하기](https://ai.google.dev/gemini-api/docs/live?hl=ko)  페이지를 읽어보세요. Live API의 기본 원리, 작동 방식, 다양한 [구현 접근 방식](https://ai.google.dev/gemini-api/docs/live?hl=ko#implementation-approach)을 소개합니다.
- **AI Studio에서 Live API 사용해 보기:** 빌드를 시작하기 전에 [Google AI Studio](https://aistudio.google.com/app/live?hl=ko)에서 Live API를 사용해 보는 것이 유용할 수 있습니다. Google AI Studio에서 Live API를 사용하려면 **스트림**을 선택하세요.

## 모델 비교

다음 표는 [Gemini 3.1 Flash Live 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ko) 모델과 [Gemini 2.5 Flash Live 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=ko) 모델의 주요 차이점을 요약한 것입니다.

| 기능 | Gemini 3.1 Flash 실시간 프리뷰 | Gemini 2.5 Flash 실시간 미리보기 |
| --- | --- | --- |
| **[사고](#native-audio-output-thinking)** | `thinkingLevel`를 사용하여 `minimal`, `low`, `medium`, `high`과 같은 설정으로 사고 깊이를 제어합니다. 기본값은 가장 짧은 지연 시간을 위해 최적화된 `minimal`입니다. [생각하기 수준 및 예산](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#levels-budgets)을 참고하세요. | `thinkingBudget`을 사용하여 사고 토큰 수를 설정합니다. 동적 사고 모드는 기본적으로 사용 설정되어 있습니다. `thinkingBudget`을 `0`로 설정하여 사용 중지합니다. [생각하기 수준 및 예산](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#levels-budgets)을 참고하세요. |
| **[응답 수신](https://ai.google.dev/api/live?hl=ko#bidigeneratecontentservercontent)** | 단일 서버 이벤트에는 여러 콘텐츠 부분이 동시에 포함될 수 있습니다 (예: `inlineData` 및 스크립트). 콘텐츠가 누락되지 않도록 각 이벤트에서 코드에 모든 부분이 처리되는지 확인하세요. | 각 서버 이벤트에는 콘텐츠 부분이 하나만 포함됩니다. 부분은 별도의 이벤트로 전송됩니다. |
| **[클라이언트 콘텐츠](#incremental-updates)** | `send_client_content`는 초기 컨텍스트 기록 시딩에만 지원됩니다 (세션 구성에서 `initial_history_in_client_content` 설정 필요). 대화 중에 텍스트 업데이트를 보내려면 대신 `send_realtime_input`를 사용하세요. | `send_client_content`은(는) 대화 전반에서 증분 콘텐츠 업데이트를 전송하고 컨텍스트를 설정하는 데 지원됩니다. |
| **[커버리지 사용 설정](https://ai.google.dev/api/live?hl=ko#turncoverage)** | 기본값은 `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`입니다. 모델의 턴에는 감지된 오디오 활동과 모든 동영상 프레임이 포함됩니다. | 기본값은 `TURN_INCLUDES_ONLY_ACTIVITY`입니다. 모델의 턴에는 감지된 활동만 포함됩니다. |
| **[맞춤 VAD](#disable-automatic-vad)** (`activity_start`/`activity_end`) | 지원됨. 자동 VAD를 사용 중지하고 `activityStart` 및 `activityEnd` 메시지를 수동으로 전송하여 턴 경계를 제어합니다. | 지원됨. 자동 VAD를 사용 중지하고 `activityStart` 및 `activityEnd` 메시지를 수동으로 전송하여 턴 경계를 제어합니다. |
| **[자동 VAD 구성](#configure-automatic-vad)** | 지원됨. `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms`, `silence_duration_ms`과 같은 매개변수를 구성합니다. | 지원됨. `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms`, `silence_duration_ms`과 같은 매개변수를 구성합니다. |
| **[비동기 함수 호출](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko#async-function-calling)** (`behavior: NON_BLOCKING`) | 지원되지 않음 함수 호출은 순차적으로만 가능합니다. 도구 응답을 전송할 때까지 모델이 응답을 시작하지 않습니다. | 지원됨. 함수가 실행되는 동안 모델이 계속 상호작용하도록 함수 선언에서 `behavior`을 `NON_BLOCKING`로 설정합니다. `scheduling` 파라미터 (`INTERRUPT`, `WHEN_IDLE` 또는 `SILENT`)를 사용하여 모델이 대답을 처리하는 방식을 제어합니다. |
| **[능동적 오디오](#proactive-audio)** | 지원되지 않음 | 지원됨. 이 기능을 사용 설정하면 입력 콘텐츠가 관련성이 없는 경우 모델이 선제적으로 응답하지 않기로 결정할 수 있습니다. `proactivity` 구성에서 `proactive_audio`를 `true`로 설정합니다 (`v1alpha` 필요). |
| **[공감형 대화](#affective-dialog)** | 지원되지 않음 | 지원됨. 모델이 입력의 표현과 어조에 맞게 대답 스타일을 조정합니다. 세션 구성에서 `enable_affective_dialog`을 `true`로 설정합니다 (`v1alpha` 필요). |

Gemini 2.5 Flash Live에서 Gemini 3.1 Flash Live로 마이그레이션하려면 [마이그레이션 가이드](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ko#migrating)를 참고하세요.

## 연결 설정

다음 예시는 API 키로 연결을 만드는 방법을 보여줍니다.

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### 자바스크립트

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
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

## 상호작용 모달리티

다음 섹션에서는 Live API에서 사용할 수 있는 다양한 입력 및 출력 모달리티의 예시와 지원 컨텍스트를 제공합니다.

### 오디오 전송

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

### 자바스크립트

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### 오디오 형식

Live API의 오디오 데이터는 항상 원시 리틀 엔디언 16비트 PCM입니다. 오디오 출력은 항상 24kHz의 샘플링 레이트를 사용합니다. 입력 오디오는 기본적으로 16kHz이지만 Live API는 필요한 경우 리샘플링하므로 모든 샘플링 레이트를 전송할 수 있습니다. 입력 오디오의 샘플링 속도를 전달하려면 각 오디오 포함 [Blob](https://ai.google.dev/api/caching?hl=ko#Blob)의 MIME 유형을 `audio/pcm;rate=16000`와 같은 값으로 설정하세요.

### 오디오 수신

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

### 자바스크립트

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

### 텍스트 전송 중

텍스트는 `send_realtime_input` (Python) 또는 `sendRealtimeInput` (JavaScript)를 사용하여 전송할 수 있습니다.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### 자바스크립트

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### 동영상 전송 중

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

### 자바스크립트

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### 증분 콘텐츠 업데이트

증분 업데이트를 사용하여 텍스트 입력을 전송하거나, 세션 컨텍스트를 설정하거나, 세션 컨텍스트를 복원합니다. 짧은 컨텍스트의 경우 정확한 이벤트 순서를 나타내기 위해 차례대로 상호작용을 보낼 수 있습니다.

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### 자바스크립트

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

컨텍스트가 긴 경우 후속 상호작용을 위해 컨텍스트 윈도우를 확보할 수 있도록 단일 메시지 요약을 제공하는 것이 좋습니다. 세션 컨텍스트를 로드하는 다른 방법은 [세션 재개](https://ai.google.dev/gemini-api/docs/live-session?hl=ko#session-resumption)를 참고하세요.

### 오디오 스크립트

모델 응답 외에도 오디오 출력과 오디오 입력의 스크립트를 모두 받을 수 있습니다.

모델의 오디오 출력 스크립트를 사용 설정하려면 설정 구성에서 `output_audio_transcription`를 전송합니다. 스크립트 언어는 모델의 대답에서 추론됩니다.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### 자바스크립트

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

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
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

모델의 오디오 입력 스크립트를 사용 설정하려면 설정 구성에서 `input_audio_transcription`를 전송합니다.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### 자바스크립트

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### 음성 및 언어 변경

[네이티브 오디오 출력](#native-audio-output) 모델은 [텍스트 음성 변환 (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko#voices) 모델에 사용할 수 있는 모든 음성을 지원합니다. [AI Studio](https://aistudio.google.com/app/live?hl=ko)에서 모든 음성을 들을 수 있습니다.

음성을 지정하려면 세션 구성의 일부로 `speechConfig` 객체 내에서 음성 이름을 설정합니다.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API는 [여러 언어](#supported-languages)를 지원합니다.
[네이티브 오디오 출력](#native-audio-output) 모델은 적절한 언어를 자동으로 선택하며 언어 코드를 명시적으로 설정하는 것은 지원하지 않습니다.

## 네이티브 오디오 기능

최신 모델에는 자연스럽고 사실적인 음성과 향상된 다국어 성능을 제공하는 [네이티브 오디오 출력](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ko)이 적용되어 있습니다.

### 생각 중

Gemini 3.1 모델은 `thinkingLevel`를 사용하여 사고 깊이를 제어하며, `minimal`, `low`, `medium`, `high`와 같은 설정을 사용합니다. 기본값은 `minimal`로 가장 짧은 지연 시간에 최적화되어 있습니다. Gemini 2.5 모델은 대신 `thinkingBudget`를 사용하여 사고 토큰 수를 설정합니다. 수준과 예산의 차이에 관한 자세한 내용은 [수준과 예산의 차이](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#levels-budgets)를 참고하세요.

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### 자바스크립트

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

또한 구성에서 `includeThoughts`을 `true`로 설정하여 생각 요약을 사용 설정할 수 있습니다. 자세한 내용은 [생각 요약](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#summaries)을 참고하세요.

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### 자바스크립트

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### 공감형 대화

이 기능을 사용하면 Gemini가 입력된 표현과 말투에 맞게 대답 스타일을 조정할 수 있습니다.

공감형 대화를 사용하려면 API 버전을 `v1alpha`로 설정하고 설정 메시지에서 `enable_affective_dialog`를 `true`로 설정하세요.

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### 자바스크립트

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### 능동적 오디오

이 기능을 사용 설정하면 콘텐츠가 관련성이 없는 경우 Gemini가 선제적으로 대답하지 않기로 결정할 수 있습니다.

이를 사용하려면 API 버전을 `v1alpha`로 설정하고 설정 메시지에서 `proactivity` 필드를 구성하고 `proactive_audio`를 `true`로 설정합니다.

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### 자바스크립트

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## 실시간 번역

Live API는 음성 대화의 실시간, 짧은 지연 시간 번역을 지원합니다. 이 기능을 사용하면 실시간 음성-음성 번역 애플리케이션을 빌드할 수 있습니다.

자세한 내용과 예시는 [실시간 번역 가이드](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ko)를 참고하세요.

## 음성 활동 감지 (VAD)

음성 활동 감지 (VAD)를 사용하면 모델이 사람이 말하는 시점을 인식할 수 있습니다. 사용자가 언제든지 모델을 중단할 수 있어 이는 자연스러운 대화를 만드는 데 필수적입니다.

VAD가 중단을 감지하면 진행 중인 생성이 취소되고 삭제됩니다. 클라이언트에 이미 전송된 정보만 세션 기록에 보관됩니다. 그런 다음 서버는 [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=ko#bidigeneratecontentservercontent) 메시지를 전송하여 중단을 보고합니다.

그런 다음 Gemini 서버는 대기 중인 함수 호출을 삭제하고 취소된 호출의 ID가 포함된 `BidiGenerateContentServerContent` 메시지를 전송합니다.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### 자바스크립트

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### 자동 VAD

기본적으로 모델은 연속 오디오 입력 스트림에서 VAD를 자동으로 실행합니다. VAD는 [설정 구성](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentSetup)의 [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=ko#RealtimeInputConfig.AutomaticActivityDetection) 필드로 구성할 수 있습니다.

오디오 스트림이 1초 이상 일시중지되면 (예: 사용자가 마이크를 끈 경우) [`audioStreamEnd`](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) 이벤트를 전송하여 캐시된 오디오를 플러시해야 합니다. 클라이언트는 언제든지 오디오 데이터 전송을 재개할 수 있습니다.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### 자바스크립트

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

`send_realtime_input`를 사용하면 API가 VAD에 따라 오디오에 자동으로 응답합니다. `send_client_content`는 순서대로 모델 컨텍스트에 메시지를 추가하는 반면 `send_realtime_input`는 결정론적 순서를 희생하여 응답성을 위해 최적화됩니다.

### 자동 VAD 구성

VAD 활동을 더 세부적으로 제어하려면 다음 매개변수를 구성하면 됩니다. 자세한 내용은 [API 참조](https://ai.google.dev/api/live?hl=ko#automaticactivitydetection)를 확인하세요.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### 자바스크립트

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### 자동 VAD 사용 중지

또는 설정 메시지에서 `realtimeInputConfig.automaticActivityDetection.disabled`를 `true`로 설정하여 자동 VAD를 사용 중지할 수 있습니다. 이 구성에서 클라이언트는 사용자 음성을 감지하고 적절한 시간에 [`activityStart`](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) 및 [`activityEnd`](https://ai.google.dev/api/live?hl=ko#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) 메시지를 전송해야 합니다. 이 구성에서는 `audioStreamEnd`가 전송되지 않습니다. 대신 스트림의 모든 중단은 `activityEnd` 메시지로 표시됩니다.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### VAD 매개변수와 품질에 미치는 영향 이해

자동 VAD를 사용할 때 오디오가 모델로 전송되기 전에 음성 턴으로 분할되는 방식을 제어하는 두 가지 주요 매개변수는 다음과 같습니다.

- **`prefixPaddingMs`**: 음성이 감지되기 *전*에 포함할 오디오의 양입니다. 이 '룩백'을 통해 모델은 VAD가 트리거되기 전에 시작될 수 있는 첫 번째 음절을 포함하여 음성의 전체 시작을 캡처할 수 있습니다. 값이 `0`이면 단어의 시작 부분이 잘릴 수 있습니다.
- **`silenceDurationMs`**: 음소거 상태에서 서버가 음성 턴을 종료하기 전에 대기하는 시간입니다. 이는 시스템이 자연스러운 문장 중간 일시중지 (예: 생각, 호흡 또는 절 경계)를 얼마나 허용하는지 결정합니다.

#### `silenceDurationMs`이 음질에 미치는 영향

`silenceDurationMs` 값은 모델이 처리를 위해 수신하는 오디오 청크의 크기와 완전성에 직접적인 영향을 미칩니다.

- **권장 (500ms~800ms):** 모델이 완전하고 맥락이 풍부한 오디오 청크를 수신하면서 지연 시간을 적절하게 유지합니다. 서버의 내부 기본값은 약 800ms입니다.
- **너무 낮음 (예: 100ms~200ms):** 시스템이 자연스러운 일시중지 중에 음성 턴을 종료하여 단일 발화를 여러 개의 작은 오디오 프래그먼트로 분할합니다. 모델은 이러한 프래그먼트를 개별적으로 수신하여 프래그먼트 간 컨텍스트가 손실되고 전사 및 응답 품질이 낮아집니다.
- **너무 높음 (예: 2,000ms 이상):** 사용자가 말을 멈춘 후 시스템이 오랫동안 대기하여 모델이 응답하기 전에 인지된 지연 시간이 증가합니다.

#### 수동 (클라이언트 측) VAD 권장사항

자동 VAD를 사용 중지하고 자체 클라이언트 측 음성 감지에서 `activityStart`/`activityEnd` 신호를 관리하는 경우 서버의 내장 오디오 버퍼링 메커니즘이 우회됩니다. 이는 다음을 의미합니다.

1. **음성 전 버퍼 없음:** 서버에서 감지된 음성 시작 전에 더 이상 오디오를 추가하지 않습니다. 클라이언트는 `activityStart`를 전송하기 전에 충분한 오디오 컨텍스트를 포함해야 합니다.
2. **무음 허용 없음:** 서버는 추가 대기 없이 `activityEnd` 신호에 즉시 반응합니다. 클라이언트 측 VAD가 적극적인 음성 종료 임계값 (예: 200ms의 무음)을 사용하는 경우 자연스러운 일시중지 중에 음성이 문장 중간에 잘릴 수 있습니다.

수동 VAD로 오디오 품질을 유지하려면 클라이언트의 음성 활동 감지기에서 최소 **500ms**의 발화 종료 무음 임계값을 사용하세요.
이 값 미만의 임계값은 텍스트 변환 및 모델 응답 품질을 저하시키는 오디오 조각화를 유발하는 경우가 많습니다.

## 토큰 수

반환된 서버 메시지의 [usageMetadata](https://ai.google.dev/api/live?hl=ko#usagemetadata) 필드에서 사용된 총 토큰 수를 확인할 수 있습니다.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### 자바스크립트

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## 미디어 해상도

세션 구성의 일부로 `mediaResolution` 필드를 설정하여 입력 미디어의 미디어 해상도를 지정할 수 있습니다.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### 자바스크립트

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## 제한사항

프로젝트를 계획할 때는 Live API의 다음 제한사항을 고려하세요.

### 응답 모달리티

네이티브 오디오 모델은 `AUDIO` 응답 형식만 지원합니다. 모델 응답이 텍스트로 필요한 경우 [출력 오디오 스크립트](#audio-transcription) 기능을 사용하세요.

### 클라이언트 인증

Live API는 기본적으로 서버 간 인증만 제공합니다. [클라이언트-서버 접근 방식](https://ai.google.dev/gemini-api/docs/live?hl=ko#implementation-approach)을 사용하여 Live API 애플리케이션을 구현하는 경우 [일시적 토큰](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ko)을 사용하여 보안 위험을 완화해야 합니다.

### 세션 시간

오디오 전용 세션은 15분으로 제한되며 오디오와 동영상이 함께 있는 세션은 2분으로 제한됩니다.
하지만 세션 기간을 무제한으로 연장하기 위해 다양한 [세션 관리 기법](https://ai.google.dev/gemini-api/docs/live-session?hl=ko)을 구성할 수 있습니다.

### 컨텍스트 윈도우

세션의 컨텍스트 윈도우 한도는 다음과 같습니다.

- [네이티브 오디오 출력](#native-audio-output) 모델의 경우 128,000개 토큰
- 기타 Live API 모델의 경우 32,000개 토큰

## 지원 언어

Live API는 다음 97개 언어를 지원합니다.

| 언어 | BCP-47 코드 | 언어 | BCP-47 코드 |
| --- | --- | --- | --- |
| 아프리칸스어 | `af` | 라트비아어 | `lv` |
| 아칸어 | `ak` | 리투아니아어 | `lt` |
| 알바니아어 | `sq` | 마케도니아어 | `mk` |
| 암하라어 | `am` | 말레이어 | `ms` |
| 아랍어 | `ar` | 말라얄람어 | `ml` |
| 아르메니아어 | `hy` | 몰타어 | `mt` |
| 아삼어 | `as` | 마오리어 | `mi` |
| 아제르바이잔어 | `az` | 마라타어 | `mr` |
| 바스크어 | `eu` | 몽골어 | `mn` |
| 벨라루스어 | `be` | 네팔어 | `ne` |
| 뱅골어 | `bn` | 노르웨이어 | `no` |
| 보스니아어 | `bs` | 오리야어 | `or` |
| 불가리아어 | `bg` | 오로모어 | `om` |
| 버마어 | `my` | 파슈토어 | `ps` |
| 카탈로니아어 | `ca` | 페르시아어 | `fa` |
| 세부아노어 | `ceb` | 폴란드어 | `pl` |
| 중국어 | `zh` | 포르투갈어 | `pt` |
| 크로아티아어 | `hr` | 펀자브어 | `pa` |
| 체코어 | `cs` | 케추아어 | `qu` |
| 덴마크어 | `da` | 루마니아어 | `ro` |
| 네덜란드어 | `nl` | 로만시어 | `rm` |
| 영어 | `en` | 러시아어 | `ru` |
| 에스토니아어 | `et` | 세르비아어 | `sr` |
| 페로어 | `fo` | 신드어 | `sd` |
| 필리핀어 | `fil` | 싱할라어 | `si` |
| 핀란드어 | `fi` | 슬로바키아어 | `sk` |
| 프랑스어 | `fr` | 슬로베니아어 | `sl` |
| 갈리시아어 | `gl` | 소말리어 | `so` |
| 조지아어 | `ka` | 소토어(남부) | `st` |
| 독일어 | `de` | 스페인어 | `es` |
| 그리스어 | `el` | 스와힐리어 | `sw` |
| 구자라트어 | `gu` | 스웨덴어 | `sv` |
| 하우사어 | `ha` | 타지크어 | `tg` |
| 히브리어 | `iw` | 타밀어 | `ta` |
| 힌디어 | `hi` | 텔루구어 | `te` |
| 헝가리어 | `hu` | 태국어 | `th` |
| 아이슬란드어 | `is` | 츠와나어 | `tn` |
| 인도네시아어 | `id` | 튀르키예어 | `tr` |
| 아일랜드어 | `ga` | 투르크멘어 | `tk` |
| 이탈리아어 | `it` | 우크라이나어 | `uk` |
| 일본어 | `ja` | 우르두어 | `ur` |
| 칸나다어 | `kn` | 우즈베크어 | `uz` |
| 카자흐어 | `kk` | 베트남어 | `vi` |
| 크메르어 | `km` | 웨일즈어 | `cy` |
| 키냐르완다어 | `rw` | 서프리지아어 | `fy` |
| 한국어 | `ko` | 월로프어 | `wo` |
| 쿠르드어 | `ku` | 요루바어 | `yo` |
| 키르기스어 | `ky` | 줄루어 | `zu` |
| 라오어 | `lo` |  |  |

## 다음 단계

- Live API를 효과적으로 사용하는 데 필요한 정보는 [도구 사용](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko) 및 [세션 관리](https://ai.google.dev/gemini-api/docs/live-session?hl=ko) 가이드를 참고하세요.
- [Google AI Studio](https://aistudio.google.com/app/live?hl=ko)에서 Live API를 사용해 보세요.
- Live API 모델에 대한 자세한 내용은 모델 페이지의 [Gemini 2.5 Flash 네이티브 오디오](https://ai.google.dev/gemini-api/docs/models?hl=ko#gemini-2.5-flash-native-audio)를 참고하세요.
- [Live API 설명서](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ko), [Live API 도구 설명서](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=ko), [Live API 시작 스크립트](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py)에서 더 많은 예시를 확인하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-09(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-09(UTC)"],[],[]]
