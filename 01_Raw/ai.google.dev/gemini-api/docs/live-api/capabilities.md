---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-CN
fetched_at: 2026-06-08T05:28:00.101532+00:00
title: "Live API \u529f\u80fd\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Live API 功能指南

这是一份全面的指南，介绍了 Live API 提供的功能和配置。
如需查看常见应用场景的概览和示例代码，请参阅[开始使用 Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 页面。

## 准备工作

- **熟悉核心概念**：如果您尚未这样做，请先阅读[开始使用 Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)  页面。
  本文将向您介绍 Live API 的基本原理、运作方式以及不同的[实现方法](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn#implementation-approach)。
- **在 AI Studio 中试用 Live API**：在开始构建之前，您可能会发现试用 [Google AI Studio](https://aistudio.google.com/app/live?hl=zh-cn) 中的 Live API 非常有用。如需在 Google AI Studio 中使用实时 API，请选择 **Stream**。

## 模型对比

下表总结了 [Gemini 3.1 Flash Live 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=zh-cn)和 [Gemini 2.5 Flash Live 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=zh-cn)模型之间的主要区别：

| 功能 | Gemini 3.1 Flash Live 预览版 | Gemini 2.5 Flash 实时预览 |
| --- | --- | --- |
| **[思考型](#native-audio-output-thinking)** | 使用 `thinkingLevel` 通过 `minimal`、`low`、`medium` 和 `high` 等设置来控制思考深度。默认值为 `minimal`，以优化最低延迟。请参阅[思维水平和预算](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#levels-budgets)。 | 使用 `thinkingBudget` 设置思考 token 的数量。默认情况下，系统会启用动态思考。将 `thinkingBudget` 设置为 `0` 即可停用。请参阅[思维水平和预算](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#levels-budgets)。 |
| **[接收响应](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentservercontent)** | 单个服务器事件可以同时包含多个内容部分（例如 `inlineData` 和转写内容）。确保您的代码处理每个事件中的所有部分，以免遗漏内容。 | 每个服务器事件仅包含一个内容部分。各个部分通过单独的事件进行传递。 |
| **[客户内容](#incremental-updates)** | `send_client_content` 仅支持为初始上下文历史记录提供种子数据（需要在会话配置中设置 `initial_history_in_client_content`）。如需在对话期间发送文本更新，请改用 `send_realtime_input`。 | 在整个对话过程中，`send_client_content` 都可用于发送增量内容更新和建立上下文。 |
| **[开启覆盖](https://ai.google.dev/api/live?hl=zh-cn#turncoverage)** | 默认为 `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`。模型的回合包括检测到的音频活动和所有视频帧。 | 默认为 `TURN_INCLUDES_ONLY_ACTIVITY`。模型的回答仅包含检测到的活动。 |
| **[自定义 VAD](#disable-automatic-vad)**（`activity_start`/`activity_end`） | 支持。停用自动 VAD，并手动发送 `activityStart` 和 `activityEnd` 消息来控制轮流边界。 | 支持。停用自动 VAD，并手动发送 `activityStart` 和 `activityEnd` 消息来控制轮流边界。 |
| **[自动 VAD 配置](#configure-automatic-vad)** | 支持。配置 `start_of_speech_sensitivity`、`end_of_speech_sensitivity`、`prefix_padding_ms` 和 `silence_duration_ms` 等参数。 | 支持。配置 `start_of_speech_sensitivity`、`end_of_speech_sensitivity`、`prefix_padding_ms` 和 `silence_duration_ms` 等参数。 |
| **[异步函数调用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn#async-function-calling)** (`behavior: NON_BLOCKING`) | 不支持。函数调用只能按顺序进行。在您发送工具响应之前，模型不会开始回答。 | 支持。在函数声明中将 `behavior` 设置为 `NON_BLOCKING`，以便模型在函数运行时继续互动。通过 `scheduling` 参数（`INTERRUPT`、`WHEN_IDLE` 或 `SILENT`）控制模型如何处理响应。 |
| **[主动音频](#proactive-audio)** | 不受支持 | 支持。启用后，如果输入内容不相关，模型可以主动决定不做出回答。在 `proactivity` 配置中将 `proactive_audio` 设置为 `true`（需要 `v1alpha`）。 |
| **[共情对话](#affective-dialog)** | 不受支持 | 支持。模型会调整回答风格，以匹配输入内容的情绪表达和语气。在会话配置中将 `enable_affective_dialog` 设置为 `true`（需要 `v1alpha`）。 |

如需从 Gemini 2.5 Flash Live 迁移到 Gemini 3.1 Flash Live，请参阅[迁移指南](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=zh-cn#migrating)。

## 建立连接

以下示例展示了如何使用 API 密钥创建连接：

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

### JavaScript

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

## 互动模式

以下部分提供了 Live API 中提供的不同输入和输出模态的示例和支持上下文。

### 发送音频

音频需要以原始 PCM 数据（原始 16 位 PCM 音频，16kHz，小端序）的形式发送。

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

### 音频格式

Live API 中的音频数据始终是原始的小端字节序 16 位 PCM。音频输出始终使用 24kHz 的采样率。输入音频的原始采样率为 16kHz，但 Live API 会在需要时重新采样，因此可以发送任何采样率。如需传达输入音频的采样率，请将每个包含音频的 [Blob](https://ai.google.dev/api/caching?hl=zh-cn#Blob) 的 MIME 类型设置为类似 `audio/pcm;rate=16000` 的值。

### 接收音频

模型以数据块的形式返回音频回答。

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

### 正在发送短信

您可以使用 `send_realtime_input` (Python) 或 `sendRealtimeInput` (JavaScript) 发送文本。

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

### 正在发送视频

视频帧以特定帧速率（每秒最多 1 帧）作为单独的图片（例如 JPEG 或 PNG）发送。

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

#### 增量内容更新

使用增量更新来发送文本输入、建立会话上下文或恢复会话上下文。对于简短的上下文，您可以发送逐轮互动来表示确切的事件序列：

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

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

对于较长的上下文，建议提供单个消息摘要，以释放上下文窗口，以便进行后续互动。如需了解加载会话上下文的其他方法，请参阅[会话恢复](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn#session-resumption)。

### 音频转录

除了模型回答之外，您还可以收到音频输出和音频输入的转写内容。

如需启用模型音频输出的转写功能，请在设置配置中发送 `output_audio_transcription`。转写语言是从模型的回答中推断出来的。

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

### JavaScript

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

如需启用模型音频输入的转写功能，请在设置配置中发送 `input_audio_transcription`。

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

### JavaScript

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

### 更改语音和语言

[原生音频输出](#native-audio-output)模型支持我们的[文字转语音 (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#voices) 模型提供的任何语音。您可以在 [AI Studio](https://aistudio.google.com/app/live?hl=zh-cn) 中试听所有声音。

如需指定语音，请在 `speechConfig` 对象中设置语音名称，作为会话配置的一部分：

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API 支持[多种语言](#supported-languages)。[原生音频输出](#native-audio-output)模型会自动选择合适的语言，不支持明确设置语言代码。

## 原生音频功能

我们最新的模型支持[原生音频输出](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=zh-cn)，可提供自然、逼真的语音和改进的多语言性能。

### 正在思考

Gemini 3.1 模型使用 `thinkingLevel` 来控制思维深度，并提供 `minimal`、`low`、`medium` 和 `high` 等设置。默认值为 `minimal`，以优化为最低延迟时间。Gemini 2.5 模型使用 `thinkingBudget` 来设置思考 token 的数量。如需详细了解级别与预算之间的关系，请参阅[思考级别和预算](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#levels-budgets)。

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

### JavaScript

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

此外，您还可以在配置中将 `includeThoughts` 设置为 `true`，以启用思路总结。如需了解详情，请参阅[思考总结](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#summaries)：

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

### JavaScript

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

### 共情对话

借助此功能，Gemini 可以根据输入内容的情绪表达和语气调整回答风格。

如需使用共情对话，请在设置消息中将 API 版本设置为 `v1alpha`，并将 `enable_affective_dialog` 设置为 `true`：

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### 主动音频

启用此功能后，如果内容不相关，Gemini 可以主动决定不做出回应。

如需使用该功能，请将 API 版本设置为 `v1alpha`，在设置消息中配置 `proactivity` 字段，并将 `proactive_audio` 设置为 `true`：

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## 语音活动检测 (VAD)

语音活动检测 (VAD) 可让模型识别用户何时在说话。这对于创建自然对话至关重要，因为这使用户可以随时中断模型。

当 VAD 检测到中断时，系统会取消并舍弃正在进行的生成操作。会话历史记录中仅保留已发送给客户端的信息。服务器随后会发送一条 [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=zh-cn#bidigeneratecontentservercontent) 消息来报告中断情况。

然后，Gemini 服务器会舍弃所有待处理的函数调用，并发送一条 `BidiGenerateContentServerContent` 消息，其中包含已取消调用的 ID。

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

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

### 自动 VAD

默认情况下，模型会对连续的音频输入流自动执行 VAD。可以使用[设置配置](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentSetup)的 [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=zh-cn#RealtimeInputConfig.AutomaticActivityDetection) 字段配置 VAD。

当音频串流暂停超过一秒时（例如，因为用户关闭了麦克风），应发送 [`audioStreamEnd`](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) 事件来清空所有已缓存的音频。客户端可以随时恢复发送音频数据。

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

### JavaScript

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

使用 `send_realtime_input`，API 将根据 VAD 自动响应音频。虽然 `send_client_content` 会按顺序将消息添加到模型上下文，但 `send_realtime_input` 针对响应速度进行了优化，但会牺牲确定性排序。

### 自动 VAD 配置

如需更精细地控制 VAD 活动，您可以配置以下参数。如需了解详情，请参阅 [API 参考文档](https://ai.google.dev/api/live?hl=zh-cn#automaticactivitydetection)。

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

### JavaScript

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

### 停用自动 VAD

或者，您也可以在设置消息中将 `realtimeInputConfig.automaticActivityDetection.disabled` 设置为 `true`，以停用自动 VAD。在此配置中，客户端负责检测用户语音，并在适当的时间发送 [`activityStart`](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) 和 [`activityEnd`](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) 消息。此配置中未发送 `audioStreamEnd`，而是会通过 `activityEnd` 消息标记任何流中断。

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

### JavaScript

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

### 了解 VAD 参数及其对质量的影响

使用自动 VAD 时，有两个关键参数可控制音频在发送到模型之前如何分段为语音轮次：

- **`prefixPaddingMs`**：在检测到语音之前要包含的音频量（以毫秒为单位）。这种“回溯”可确保模型捕获完整的语音开始，包括可能在 VAD 触发器之前开始的第一个音节。值为 `0` 可能会导致字词开头被剪掉。
- **`silenceDurationMs`**：服务器在静默状态下等待多长时间后结束语音轮次。此值决定了系统对句子中自然停顿（例如思考、呼吸或子句边界）的容忍程度。

#### `silenceDurationMs` 对音质的影响

`silenceDurationMs` 值会直接影响模型接收到的音频块的大小和完整性，以供模型进行处理：

- **建议（500 毫秒 - 800 毫秒）**：可实现良好的平衡 - 模型接收完整且包含丰富上下文的音频块，同时保持合理的延迟时间。服务器的内部默认值为大约 800 毫秒。
- **过低（例如 100 毫秒到 200 毫秒）**：系统会在自然停顿期间结束语音轮次，从而将单个话语拆分为多个小音频片段。模型会单独接收这些片段，从而丢失片段间的上下文，导致转写和回答质量下降。
- **过高（例如，2000 毫秒以上）**：用户停止说话后，系统会等待很长时间，从而增加模型响应前的感知延迟。

#### 手动（客户端）VAD 的最佳实践

当您停用自动 VAD 并通过自己的客户端语音检测来管理 `activityStart`/`activityEnd` 信号时，请注意，服务器的内置音频缓冲机制会被绕过。这意味着：

1. **无语音前缓冲区**：服务器不再在检测到的语音开始之前预先添加音频。客户端应在发送 `activityStart` 之前包含足够的音频上下文。
2. **无静音容忍度**：服务器会立即对您的 `activityEnd` 信号做出响应，无需额外等待。如果客户端 VAD 使用激进的语音结束阈值（例如 200 毫秒的静音），则在自然停顿期间，语音可能会在句子中途被切断。

如需使用手动 VAD 来保持音质，请在客户端的语音活动检测器中使用至少 **500 毫秒**的语音结束静音阈值。低于此值的阈值通常会导致音频片段化，从而降低转写和模型响应质量。

## Token 计数

您可以在返回的服务器消息的 [usageMetadata](https://ai.google.dev/api/live?hl=zh-cn#usagemetadata) 字段中找到消耗的 token 总数。

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

### JavaScript

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

## 媒体分辨率

您可以在会话配置中设置 `mediaResolution` 字段，以指定输入媒体的媒体分辨率：

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## 限制

在规划项目时，请考虑 Live API 的以下限制。

### 回答模式

原生音频模型仅支持 `AUDIO` 回答模态。如果您需要以文本形式获取模型响应，请使用[输出音频转写](#audio-transcription)功能。

### 客户端身份验证

Live API 默认仅提供服务器到服务器的身份验证。如果您要使用[客户端到服务器的方法](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn#implementation-approach)来实现 Live API 应用，则需要使用[临时令牌](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-cn)来降低安全风险。

### 会话时长

纯音频会话时长不得超过 15 分钟，音频加视频会话时长不得超过 2 分钟。
不过，您可以配置不同的[会话管理技术](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn)，以无限延长会话时长。

### 上下文窗口

会话的上下文窗口限制为：

- 对于[原生音频输出](#native-audio-output)模型，为 12.8 万个 token
- 其他 Live API 模型的令牌数量为 32,000

## 支持的语言

Live API 支持以下 97 种语言。

| 语言 | BCP-47 代码 | 语言 | BCP-47 代码 |
| --- | --- | --- | --- |
| 南非荷兰语 | `af` | 拉脱维亚语 | `lv` |
| 阿坎语 | `ak` | 立陶宛语 | `lt` |
| 阿尔巴尼亚语 | `sq` | 马其顿语 | `mk` |
| 阿姆哈拉语 | `am` | 马来语 | `ms` |
| 阿拉伯语 | `ar` | 马拉雅拉姆语 | `ml` |
| 亚美尼亚语 | `hy` | 马耳他语 | `mt` |
| 阿萨姆语 | `as` | 毛利语 | `mi` |
| 阿塞拜疆语 | `az` | 马拉地语 | `mr` |
| 巴斯克语 | `eu` | 蒙古语 | `mn` |
| 白俄罗斯语 | `be` | 尼泊尔语 | `ne` |
| 孟加拉语 | `bn` | 挪威语 | `no` |
| 波斯尼亚语 | `bs` | 奥里亚语 | `or` |
| 保加利亚语 | `bg` | 奥罗莫语 | `om` |
| 缅甸语 | `my` | 普什图语 | `ps` |
| 加泰罗尼亚语 | `ca` | 波斯语 | `fa` |
| 宿务语 | `ceb` | 波兰语 | `pl` |
| 中文 | `zh` | 葡萄牙语 | `pt` |
| 克罗地亚语 | `hr` | 旁遮普语 | `pa` |
| 捷克语 | `cs` | 克丘亚语 | `qu` |
| 丹麦语 | `da` | 罗马尼亚语 | `ro` |
| 荷兰语 | `nl` | 罗曼什语 | `rm` |
| 英语 | `en` | 俄语 | `ru` |
| 爱沙尼亚语 | `et` | 塞尔维亚语 | `sr` |
| 法罗语 | `fo` | 信德语 | `sd` |
| 菲律宾语 | `fil` | 僧伽罗语 | `si` |
| 芬兰语 | `fi` | 斯洛伐克语 | `sk` |
| 法语 | `fr` | 斯洛文尼亚语 | `sl` |
| 加利西亚语 | `gl` | 索马里语 | `so` |
| 格鲁吉亚语 | `ka` | 南索托语 | `st` |
| 德语 | `de` | 西班牙语 | `es` |
| 希腊语 | `el` | 斯瓦希里语 | `sw` |
| 古吉拉特语 | `gu` | 瑞典语 | `sv` |
| 豪萨语 | `ha` | 塔吉克语 | `tg` |
| 希伯来语 | `iw` | 泰米尔语 | `ta` |
| 印地语 | `hi` | 泰卢固语 | `te` |
| 匈牙利语 | `hu` | 泰语 | `th` |
| 冰岛语 | `is` | 茨瓦纳语 | `tn` |
| 印度尼西亚语 | `id` | 土耳其语 | `tr` |
| 爱尔兰语 | `ga` | 土库曼语 | `tk` |
| 意大利语 | `it` | 乌克兰语 | `uk` |
| 日语 | `ja` | 乌尔都语 | `ur` |
| 卡纳达语 | `kn` | 乌兹别克语 | `uz` |
| 哈萨克语 | `kk` | 越南语 | `vi` |
| 高棉语 | `km` | 威尔士语 | `cy` |
| 卢旺达语 | `rw` | 西弗里西亚语 | `fy` |
| 韩语 | `ko` | 沃洛夫语 | `wo` |
| 库尔德语 | `ku` | 约鲁巴语 | `yo` |
| 吉尔吉斯语 | `ky` | 祖鲁语 | `zu` |
| 老挝语 | `lo` |  |  |

## 后续步骤

- 请参阅[工具使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn)和[会话管理](https://ai.google.dev/gemini-api/docs/live-session?hl=zh-cn)指南，了解有关如何有效使用 Live API 的重要信息。
- 在 [Google AI Studio](https://aistudio.google.com/app/live?hl=zh-cn) 中试用 Live API。
- 如需详细了解 Live API 模型，请参阅“模型”页面上的 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-native-audio)。
- 您可以尝试 [Live API 食谱](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=zh-cn)、[Live API 工具食谱](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=zh-cn)和 [Live API 快速入门脚本](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py)中的更多示例。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-01。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-01。"],[],[]]
