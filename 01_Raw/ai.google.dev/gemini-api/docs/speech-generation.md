---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-CN
fetched_at: 2026-10-12T06:50:34.779247+00:00
title: "\u6587\u5b57\u8f6c\u8bed\u97f3\u751f\u6210 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 文字转语音生成 (TTS)

Gemini API 可以使用 Gemini 文字转语音 (TTS) 生成功能将文本输入转换为单人或多人语音。文字转语音生成是*[可控](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#controllable)*的，这意味着您可以结合使用结构化对话轮次元数据 (`speech_metadata`) 和内嵌语音标记来指导音频的*风格*、*口音*、*语速*和*音调*。

TTS 功能不同于通过 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 提供的语音生成功能，后者专为交互式非结构化音频以及多模态输入和输出而设计。虽然 Live API 在动态对话上下文中表现出色，但通过 Gemini API 实现的 TTS 专为需要精确朗读文本并对风格和声音进行精细控制的场景而量身打造，例如播客或有声读物生成。

本指南将向您展示如何使用 [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn) (`gemini-3.8-flash-tts`) 和 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) (`gemini-3.8-flash-lite-tts`) 从文本生成单人语音和多人语音。

## 准备工作

请确保您使用的是[支持的模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#supported-models)部分中列出的 Gemini TTS 模型，并升级到最新的 Google GenAI SDK（Python 版为 `google-genai >= 2.25.0`，JavaScript/TypeScript 版为 `@google/genai >= 2.24.0`），或者使用 REST API。为获得最佳结果，请查看[何时使用哪种模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#when-to-use-which-model)，以便为您的工作负载选择最佳模型。

在开始构建之前，您可能会发现[在 AI Studio 中测试 Gemini TTS 模型](https://aistudio.google.com/generate-speech?hl=zh-cn)很有用。

## 单说话者 TTS

如需使用 Gemini 3.8 TTS 模型将文本转换为单人语音音频，请在 `input` 中传递逐字转写内容，使用 `speech_metadata` 注释附加轮次级样式，并在 `generation_config.speech_config` 中配置语音。您可以从预建的[语音选项](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#voices)、扩展语音库 (`GET /v1beta/voices`)、自定义[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn) ID (`voice_...`) 或[语音复刻](https://ai.google.dev/gemini-api/docs/voice-replication?hl=zh-cn) ID（`voice_...` 或可选的无状态 `voicekey_...`）中选择语音。

此示例将模型生成的默认 WAV 输出音频 (`audio/wav`) 直接保存到文件中：

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

在 Python 和 JavaScript SDK 中，您可以使用 `interaction.output_audio` 便捷属性检索生成的音频数据，该属性会返回上次生成的音频块（在原始 REST JSON 响应中，base64 编码的音频存储在 `steps[].content[].data` 中）。如需详细了解便捷属性，请参阅[互动概览](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn#convenience-properties)。

## 多说话人 TTS

对于多说话人对话，请在 `speech_config.speakers` 中配置两个说话人，并将每个轮次作为单独的文本项传递，其中包含 `speech_metadata` 注释，用于指定 `speaker` 和可选的轮次级 `style`。请注意，`speech_config` 接受数组 (`[{"voice": "..."}]`) 进行单说话人生成，接受对象 (`{"speakers": [...]}`) 进行多说话人生成：

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "TTS the following conversation between Joe and Jane:\n" +
        "Joe: How's it going today Jane?\n" +
        "Jane: Not too bad, how about you?"

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Joe"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Jane"), Voice: genai.Ptr("Puck")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(prompt),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## 使用元数据和标记控制语音风格

Gemini 3.8 TTS 会将 `text` 字段严格视为逐字转写内容。如需控制朗读效果，但不希望系统朗读舞台说明，请按范围拆分指令：

- **持续的轮次级交付 (`speech_metadata.style`)**：将适用于整个轮次的情感、交付风格、韵律、节奏和音量放在 `style` 字段中（例如 `"style": "whispered urgently"`、`"style": "out of breath"` 或 `"style": "warm and enthusiastic"`）。
- **时间点事件（内嵌标记）**：使用尖括号（例如 `"Wait... <short pause> did you hear that? <sigh>"` 或 `"Excuse me <cough> as I was saying..."`）将短暂的非语音声音爆发或停顿直接放置在转写内容中。

如需了解全面的最佳实践，请参阅[提示指南](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#prompting-guide)。

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    transcriptRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "Generate a short transcript around 100 words that reads " +
                    "like it was clipped from a podcast by excited herpetologists. " +
                    "The hosts names are Dr. Anya and Liam.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var transcript string
    if transcriptRes.Interaction.OutputText != nil {
        transcript = *transcriptRes.Interaction.OutputText
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Dr. Anya"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Liam"), Voice: genai.Ptr("Puck")},
        })),
    }

    ttsRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(transcript),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = ttsRes
}
```

## 流式语音生成

您可以通过设置 `stream: true` 来在合成音频时对其进行流式传输。与返回包含 RIFF 标头的完整 WAV 文件的单次请求不同，**流式请求默认返回不含标头的原始 16 位有符号小端线性 PCM (`audio/l16`，24 kHz，单声道) 块**，因此音频块可以连续播放或串联，而无需容器标头。

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## 音频输出格式

Gemini 3.8 TTS 模型使用不同的默认音频格式，具体取决于请求是单次请求还是流式请求：

- **一元请求 (`stream=False`)**：返回完整的 **WAV (`audio/wav`)** 音频，其中包含标准 RIFF 标头（24 kHz、单声道、16 位有符号小端字节序 PCM）。您可以直接将解码后的音频字节保存到 `.wav` 文件，而无需手动添加 WAV 标头。
- **流式请求 (`stream=True`)**：默认返回**无标头的原始线性 PCM (`audio/l16`)** 块（24 kHz、单声道、16 位有符号小端字节序 PCM），以便可以连续流式传输或串联块，而无需在每个块上添加容器标头。

如需请求其他音频编码或采样率，请在 `response_format` 内配置 `mime_type` 和可选的 `sample_rate`：

| 格式 | `mime_type` 值 | 说明 |
| --- | --- | --- |
| **WAV** *（一元默认）* | `"audio/wav"` | 带有 RIFF 标头的未压缩 WAV 文件（16 位有符号小端字节序 PCM、单声道、24 kHz 默认）。一元请求的默认值。 |
| **原始 PCM (L16)** *（流式传输默认）* | `"audio/l16"` | 未压缩、无标头的 16 位有符号小端字节序线性 PCM 音频（24 kHz，单声道）。流式传输请求的默认值。 |
| **Mu-law** | `"audio/mulaw"` | 8 位 G.711 mu-law 编码音频（常用于北美和日本的电话/IVR 系统）。 |
| **A-law** | `"audio/alaw"` | 8 位 G.711 A-law 编码音频（通常用于欧洲和国际电话系统）。 |

您还可以指定以赫兹为单位的 `sample_rate`（例如 `24000`、`16000` 或 `8000`）。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
            Stream:           genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if audioDelta := stepDelta.GetDeltaAudio(); audioDelta != nil && audioDelta.Data != nil {
                audioData, err := base64.StdEncoding.DecodeString(*audioDelta.Data)
                if err != nil {
                    log.Fatal(err)
                }
                // Process the audio chunk (e.g. play it or write to a file)
                _ = audioData
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## 语音选项

Gemini 3.8 TTS 支持四种选择或创建语音的方式：

1. **预建的 Studio 语音**：下表中列出的 30 种精选语音。
2. **扩展语音库**：使用 `client.voices.list()` (`GET /v1beta/voices`) 可访问数百种其他语音，涵盖多种语言、口音和角色原型。
3. **[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)**：在 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中通过自然语言描述生成自定义声音角色，或使用 `POST /v1beta/voices`（`type="prompted"`，该函数会在 `CreateVoice` 和 `GetVoice` 中返回持久性 `voice_...` ID 和 `sample_audio` WAV 预览）。
4. **[语音复刻](https://ai.google.dev/gemini-api/docs/voice-replication?hl=zh-cn)**：在 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中或使用 `POST /v1beta/voices`（`type="replicated"`，默认情况下为持久性 `store=True`，或可选的无状态 `store=False`）复刻参考音频和同意音频中的说话者语音。

### 自定义语音限制和 TTL

| 语音类型 | 存储模式 | 配额 / 限制 | 保留期限 (TTL) |
| --- | --- | --- | --- |
| **有状态语音**（`voice_...`，提示或复制） | `store=True` | **每个项目 200 个声音**（在提示声音和复制声音之间共享） | **自上次使用起 1 年\*** |
| **无状态语音键**（`voicekey_...`，已复制） | `store=False` | 由客户端管理 | **7 天** |

\* **TTL 延期**：每次积极使用该声音（通过该声音合成语音或将其用作混音的基础声音）时，1 年的保留期限都会重置。如果某个声音闲置 1 年，系统会自动将其删除。

### 预建语音

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *明亮* | **Puck** - *欢快* | **Charon** - *信息丰富* |
| **Kore** -- *坚定* | **Fenrir** - *易兴奋* | **Leda** - *青春* |
| **Orus** - *公司* | **Aoede** - *Breezy* | **Callirrhoe** - *轻松* |
| **Autonoe** - *明亮* | **Enceladus** - *气声* | **Iapetus** -- *清晰* |
| **Umbriel** - *随和* | **Algieba** - *平滑* | **Despina** - *平滑* |
| **Erinome** -- *清除* | **Algenib** -- *Gravelly* | **Rasalgethi** - *信息丰富* |
| **Laomedeia** - *欢快* | **Achernar** - *柔和* | **Alnilam** - *坚定* |
| **Schedar** - *均匀* | **Gacrux** - *成熟* | **Pulcherrima** - *转发* |
| **Achird** - *友好* | **Zubenelgenubi** - *休闲* | **Vindemiatrix** - *柔和* |
| **Sadachbia** - *活泼* | **Sadaltager** - *知识渊博* | **Sulafat** - *偏高* |

### 扩展的语音库和过滤功能

除了上表中列出的 30 种精选工作室语音外，**扩展语音库**还提供了数百种其他语音，涵盖多种语言、地区口音、角色人物和领域。您可以在 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中以交互方式浏览、过滤和试听完整的语音库，也可以使用 `client.voices.list()`（`GET /v1beta/voices`，使用 `google-genai` 2.25.0+ / `@google/genai` 2.24.0+）以编程方式查询语音库。

`ListVoices` 会返回您的自定义存储语音（按最新到最旧的顺序排列），然后返回符合过滤条件的预构建目录语音。如果为列表过滤条件传递了多个值，系统会返回与该过滤条件中的**任何**值匹配的声音 (`OR`)，而不同的过滤条件参数会与 `AND` 结合使用：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47 语言标记（例如 `["en-US", "en-GB"]`）。不区分大小写的完全匹配。 |
| `region_code` | `list[str]` | ISO 3166-1 alpha-2 或联合国 M.49 地区代码（例如 `["US", "GB"]`）。 |
| `accent` | `list[str]` | 区域口音描述符（例如 `["American", "British"]`）。 |
| `gender` | `list[str]` | 感知到的性别表达（`"female"`、`"male"` 或 `"neutral"`）。 |
| `pitch` | `list[str]` | 人声音调分类（`"low"`、`"medium"` 或 `"high"`）。 |
| `persona` | `list[str]` | 声音角色或角色原型（例如 `["Warm, Friendly"]`、`["Narrator"]`）。 |
| `contexts`（REST 中的 `context`） | `list[str]` | 最佳使用网域（例如 `["Audiobook", "Conversational", "News"]`）。 |
| `type`（在 Python 中为 `type_`） | `list[str]` | 按语音来源过滤：`"prebuilt"`、`"prompted"`（[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)）或 `"replicated"`（[语音复刻](https://ai.google.dev/gemini-api/docs/voice-replication?hl=zh-cn)）。 |
| `search` | `str` | 自由文本子字符串搜索不区分大小写，可匹配 `display_name` 和 `description`。 |
| `page_size` | `int` | 每页返回的声音数量上限（默认值为 `50`，最大值为 `1000`）。 |
| `page_token` | `str` | 来自 `response.next_page_token` 的令牌，用于获取下一页结果。 |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## 支持的语言

TTS 模型会自动检测输入语言。
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn) (`gemini-3.8-flash-tts`) 支持**超过 130 种语言**，而 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) (`gemini-3.8-flash-lite-tts`) 支持**超过 100 种语言**：

| 语言 | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| 亚齐语（阿拉伯文字） | ✔️ | ✔️ |
| 南非荷兰语 | ✔️ | ✔️ |
| 阿坎语 | ✔️ | ✔️ |
| 阿姆哈拉语 | ✔️ | ✔️ |
| 亚美尼亚语 | ✔️ | ✔️ |
| 阿萨姆语 | ✔️ | ✔️ |
| 阿瓦德语 | ✔️ | ✔️ |
| 巴厘语 | ✔️ | ✔️ |
| 孟加拉语 | ✔️ | ✔️ |
| 班查语（阿拉伯文字） | ✔️ | — |
| 班查语（拉丁文字） | ✔️ | ✔️ |
| 巴什基尔语 | ✔️ | — |
| 巴斯克语 | ✔️ | ✔️ |
| 白俄罗斯语 | ✔️ | ✔️ |
| 奔巴语 | ✔️ | — |
| 博杰普尔语 | ✔️ | ✔️ |
| 波斯尼亚语 | ✔️ | ✔️ |
| 布吉文 | ✔️ | ✔️ |
| 保加利亚语 | ✔️ | ✔️ |
| 缅甸语 | ✔️ | — |
| 粤语 | ✔️ | ✔️ |
| 加泰罗尼亚语 | ✔️ | ✔️ |
| 宿务语 | ✔️ | ✔️ |
| 中部库尔德语 | ✔️ | ✔️ |
| 恰蒂斯加尔语 | ✔️ | ✔️ |
| 中文（汉字） | ✔️ | ✔️ |
| 中文（繁体） | ✔️ | ✔️ |
| 克里米亚鞑靼语 | ✔️ | — |
| 克罗地亚语 | ✔️ | ✔️ |
| 捷克 | ✔️ | ✔️ |
| 丹麦语 | ✔️ | ✔️ |
| 荷兰语 | ✔️ | ✔️ |
| 迪尤拉语 | ✔️ | — |
| 宗卡语 | ✔️ | — |
| 阿拉伯语（埃及） | ✔️ | ✔️ |
| 英语 | ✔️ | ✔️ |
| 爱沙尼亚语 | ✔️ | ✔️ |
| 菲律宾语 | ✔️ | ✔️ |
| 芬兰语 | ✔️ | — |
| 法语 | ✔️ | ✔️ |
| 加利西亚语 | ✔️ | ✔️ |
| 干达语 | ✔️ | ✔️ |
| 格鲁吉亚语 | ✔️ | ✔️ |
| 德语 | ✔️ | ✔️ |
| 希腊语 | ✔️ | ✔️ |
| 瓜拉尼人 | ✔️ | — |
| 古吉拉特语 | ✔️ | ✔️ |
| 海地克里奥尔语 | ✔️ | ✔️ |
| 喀尔喀蒙古语 | ✔️ | ✔️ |
| 豪萨语 | ✔️ | ✔️ |
| 希伯来语 | ✔️ | ✔️ |
| 印地语 | ✔️ | ✔️ |
| 匈牙利语 | ✔️ | ✔️ |
| 冰岛语 | ✔️ | ✔️ |
| 伊博语 | ✔️ | — |
| 伊洛果语 | ✔️ | ✔️ |
| 印度尼西亚语 | ✔️ | ✔️ |
| 伊朗波斯语 | ✔️ | ✔️ |
| 意大利语 | ✔️ | ✔️ |
| 日语 | ✔️ | ✔️ |
| 爪哇语 | ✔️ | ✔️ |
| 卡拜尔语 | ✔️ | — |
| 卡姆巴语 | ✔️ | ✔️ |
| 卡纳达语 | ✔️ | ✔️ |
| 克什米尔语（阿拉伯文字） | ✔️ | ✔️ |
| 克什米尔语（梵文） | ✔️ | ✔️ |
| 哈萨克语 | ✔️ | ✔️ |
| 高棉语 | ✔️ | ✔️ |
| 吉库尤语 | ✔️ | ✔️ |
| 卢旺达语 | ✔️ | ✔️ |
| 刚果语 | ✔️ | ✔️ |
| 韩语 | ✔️ | ✔️ |
| 吉尔吉斯语 | ✔️ | ✔️ |
| 老挝语 | ✔️ | ✔️ |
| 拉特加莱语 | ✔️ | — |
| 林加拉语 | ✔️ | ✔️ |
| 立陶宛语 | ✔️ | — |
| 卢森堡语 | ✔️ | — |
| 马其顿语 | ✔️ | ✔️ |
| 摩揭陀语 | ✔️ | ✔️ |
| 迈蒂利语 | ✔️ | ✔️ |
| 马拉雅拉姆语 | ✔️ | ✔️ |
| 马耳他语 | ✔️ | ✔️ |
| 曼尼普尔语 | ✔️ | ✔️ |
| 马拉地语 | ✔️ | ✔️ |
| 米南佳保语（阿拉伯文字） | ✔️ | ✔️ |
| 米南佳保语（拉丁文字） | ✔️ | — |
| 米佐语 | ✔️ | ✔️ |
| 尼泊尔语（单独的语言） | ✔️ | ✔️ |
| 尼日利亚富拉语 | ✔️ | ✔️ |
| 阿塞拜疆北部 | ✔️ | ✔️ |
| 北索托语 | ✔️ | ✔️ |
| 乌兹别克北部 | ✔️ | ✔️ |
| 挪威博克马尔语 | ✔️ | ✔️ |
| 挪威语（尼诺斯克语） | ✔️ | ✔️ |
| 尼昂加语 | ✔️ | ✔️ |
| 奥克斯坦语 | ✔️ | — |
| 奥里亚语（单个语言） | ✔️ | ✔️ |
| 邦阿西楠语 | ✔️ | — |
| 波斯语（阿富汗） | ✔️ | ✔️ |
| 波兰语 | ✔️ | ✔️ |
| 葡萄牙语 | ✔️ | ✔️ |
| 旁遮普语 | ✔️ | ✔️ |
| 罗马尼亚语 | ✔️ | ✔️ |
| 俄语 | ✔️ | ✔️ |
| 桑塔利语 | ✔️ | ✔️ |
| 塞尔维亚语 | ✔️ | ✔️ |
| 信德语 | ✔️ | — |
| 僧伽罗语 | ✔️ | ✔️ |
| 斯洛伐克语 | ✔️ | ✔️ |
| 斯洛文尼亚语 | ✔️ | — |
| 索马里语 | ✔️ | — |
| 南阿塞拜疆语 | ✔️ | ✔️ |
| 南部普什图语 | ✔️ | ✔️ |
| 南索托语 | ✔️ | — |
| 西班牙语 | ✔️ | ✔️ |
| 标准阿拉伯语（阿拉伯文字） | ✔️ | ✔️ |
| 标准阿拉伯语（拉丁文字） | ✔️ | ✔️ |
| 标准拉脱维亚语 | ✔️ | ✔️ |
| 标准马来语 | ✔️ | ✔️ |
| 斯瓦希里语（单个语言） | ✔️ | — |
| 斯瓦特语 | ✔️ | — |
| 瑞典语 | ✔️ | — |
| 塔吉克语 | ✔️ | — |
| 泰米尔语 | ✔️ | ✔️ |
| 泰卢固语 | ✔️ | ✔️ |
| 泰语 | ✔️ | — |
| 提格里尼亚语 | ✔️ | — |
| 阿尔巴尼亚语托斯克方言 | ✔️ | — |
| 土耳其语 | ✔️ | ✔️ |
| 维吾尔语 | ✔️ | — |
| 越南语 | ✔️ | ✔️ |

## 支持的模型

| 模型 | 一位说话者 | 多说话人 | 语音设计 | 语音复刻 |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=zh-cn) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro 预览版 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=zh-cn) | ✔️ | ✔️ | — | — |

### 何时使用哪种模型

Gemini 3.8 TTS 模型具有完全相同的 API 架构和提示格式，因此您只需更改一个参数即可在它们之间切换：

- **如果需要优先考虑最高声音保真度、细致的表演
  和富有表现力的控制，请使用 [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn)
  (`gemini-3.8-flash-tts`)**。它非常适合工作室级创意工作、复杂的多人对话、大量人声爆发标记、难以发音的词语、区域性或少数民族方言，以及需要稳定的人声和环境音的长篇旁白。
- **使用 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) (`gemini-3.8-flash-lite-tts`)** 作为 `gemini-3.1-flash-tts-preview` 的快速、经济高效的替代方案。它经过优化，可用于大批量生成内容、创建对话式语音智能体级联、实现大声朗读功能、可靠地进行语音复刻，以及处理主要语言的日常单人语音。

### 迁移指南

如果您要从 `gemini-3.1-flash-tts-preview` 或更早版本的 Gemini TTS 模型迁移到 Gemini 3.8 TTS，请注意以下事项：

1. **将回合级指令移至 `speech_metadata`**：Gemini 3.8 TTS 会将输入文本严格视为逐字转写内容。将持续交付说明（`style` - 例如 `"whispering"`、`"out of breath"` 或 `"speaking slowly"`）和说话人标签 (`speaker`) 移至结构化 `speech_metadata` 注释中，而不是将舞台说明嵌入到转写文本中。
2. **仅将尖括号内嵌标记用于时间点上的发声事件**：使用尖括号（例如 `<laugh>`、`<sigh>`、`<cough>`、`<breath>` 或 `<short pause>`）将短暂的非语音发声和停顿内嵌在转写中。避免使用音效标记（例如掌声或砰砰声），并将朗读风格放在 `speech_metadata.style` 中。
3. **在多说话人请求的每个回合中指定 `speaker`**：多说话人请求
   的每个回合都必须在
   `speech_metadata` 内明确包含 `speaker`，且 与配置的说话人之一相匹配。
4. **使用语音设计预先设计角色**：使用在[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)中创建的自定义语音替换多段落 `"Audio Profile"` 或 `"Director's Notes"` 代码块，然后通过 TTS 请求传递该 `voice_...` ID，并使用最少的 `style` 字符串或空字符串。
5. **在一元请求中考虑默认 WAV (`audio/wav`) 输出**：与 `gemini-3.1-flash-tts-preview` 及更早版本的 TTS 模型（默认返回无标头的原始 PCM `audio/l16`）不同，Gemini 3.8 TTS 默认针对一元请求返回带有标准 RIFF 标头的 WAV 音频 (`audio/wav`)。
   - 如果您的代码之前将原始 PCM 字节封装在 WAV 标头中（例如，使用 Python 的 `wave` 模块或 `ffmpeg`），请移除手动标头封装，并将返回的字节直接写入 `.wav` 文件。
   - 如果您的流水线需要无标头的原始 PCM、mu-law 或 A-law 音频，请将 `response_format.mime_type` 明确设置为 `"audio/l16"`、`"audio/mulaw"` 或 `"audio/alaw"`（例如，在 Interactions API 中为 `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}`，或在 `generateContent` 中为 `AUDIO_L16`）。请参阅[音频输出格式](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#audio-output-formats)。

## 提示指南

Gemini 3.8 TTS 模型将输入文本严格视为**逐字转写内容**。与之前将舞台说明嵌入纯文本中的预览模型不同，Gemini 3.8 TTS 将持续的回合级说明 (`speech_metadata`) 与时间点内嵌语音标记分开。

### 样式字段与内嵌标记

按范围拆分性能指令：

- **回合级交付 (`speech_metadata.style`)**：将持续交付属性（例如情绪、韵律、整体节奏或交付风格（如 `"whispering"`、`"out of breath"`、`"muttering"` 或 `"sarcastic"`））放入 `speech_metadata` 的 `style` 字段中。为了在对话轮次中打造稳定一致的角色和表演，请在[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)中预先设计角色，并仅使用 `style` 进行可选的轮次级调整。
- **时间点事件（内嵌标记）**：使用尖括号（`<cough>`、`<breath>`、`<sigh>`、`<short pause>`）将短暂的非语音声音爆发、呼吸或停顿内嵌在转写内容中。使用尖括号 (`<...>`) 可获得最高音质，并且应仅标记人声，而非非人声的音效。

| 范围 | 放置位置 | 示例 |
| --- | --- | --- |
| **回合级**（在整个回合中持续存在） | `speech_metadata.style` | `"angry tone"`、`"speaking rapidly"`、`"out of breath"`、`"whispers"`、`"sarcastic"` |
| **时间点**（在特定字词处发生） | 内嵌在 `text` 中（`<...>`） | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### 节奏和停顿

您可以从以下三个精细程度级别控制节奏和静音：

- **标点符号和省略号**：使用逗号、短划线 (`--`) 和省略号 (`...`) 来模拟自然对话中的犹豫。
- **内嵌暂停标记**：在脚本中说话者应暂停的确切位置插入 `<short pause>` 或 `<long pause>`：
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **回合级语速**：在 `speech_metadata` 中设置 `"style": "speaking rapidly"` 或 `"style": "speaking slowly"`，以控制整个回合的说话速率。

### 韵律和音调

使用 **`speech_metadata.style`** 控制整个对话轮次的韵律、音调和语调（例如 `"style": "high pitch, cheerful and excited inflection"` 或 `"style": "monotone and flat"`）。如果情绪或韵律在对话中发生变化，请将脚本拆分为单独的轮次，并为每个轮次指定不同的 `style` 值。

### 强调方式

在转写内容中将特定字词大写，并结合标点符号和内嵌语音标记，以便在关键字上自然地施加语音重音：

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### 爆发性发声和非语音声音

使用尖括号 (`<...>`) 将非语音的人声内嵌在声音应出现的准确位置。建议的人声标记包括：

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### 后通道和重叠语音

在多说话人对话中，将听者的反应用竖线字符 (`|reaction|`) 括起来，放在说话人的回合内，以创建自然的后通道或重叠的语音，而无需为每个反应另起一个回合。

- **简短的后通道交流**：在主动发言者的发言轮次中，添加简短的听众反应（`|oh hmm|`、`|oh really?|`、`|absolutely|`）：
  - **第 1 轮（发言者 A）**： `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **第 2 轮（演讲者 B）**： `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **第 3 轮（演讲者 A）**： `"Then let's ship it |absolutely| and watch the dashboards."`
- **重叠和交错的语音**：使用多个竖线分隔符来模拟两位发言者同时或交错的语音（最好与 `gemini-3.8-flash-tts` 搭配使用）：
  - **同步倒计时/合唱**： `"Let's surprise him on three |ok| ready?"`，然后是 `"one. two. three. |happy| happy |birthday| birthday!"`
  - **完全重叠的音箱**： `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### 各代之间的一致性以及应避免的事项

请遵循以下准则，以确保在对话轮次之间保持稳定的声音身份：

- **在语音设计中提前设计角色，而不是使用长样式块**：
  长篇 `"Audio Profile"` 段落和多项目符号 `"Director's Notes"` 是从早期模型沿用下来的，也是导致语音漂移的最常见原因。
  在[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)中提前运用同样的创意直觉，生成持久的自定义 `voice_...` 人格，然后通过 TTS 调用传递该语音 ID。
- **依靠语音参考实现稳定性（省略元指令）**：Gemini 3.8 TTS 模型经过训练，可先锚定音频参考。
  请勿添加指示模型保持声音稳定的指令（例如 `"do not switch speaker identity"` 或 `"maintain identical timbre"`）- 额外的提示文本会增加漂移。舍弃不必要的风格指令，让模型在语音参考提供的稳定点附近自然变化。
- **请勿尝试更改 `style` 中不可变的说话人特征**：避免在 `speech_metadata.style` 中添加年龄、性别、姓名或永久性口音变化。
  您可以从扩展语音库中选择一种地区性语音，也可以使用[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)功能创建一种语音。

### 推荐的工作流程

1. **一次性打造角色**：在[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)中创建角色，或从扩展语音库中选择与目标语言和角色相符的地区性语音。
2. **撰写包含语流不畅的自然口语转写内容**：为了尽可能自然，请将 `text` 撰写为真实的口语转写内容，包括自然的对话语流不畅和犹豫（例如，`"Oh uh yeah I think... hm, so that's interesting"`）。
3. **先测试纯 TTS**：先使用空的 `style` 字段合成脚本，大多数请求根本不需要 `style` 指令。
4. **仅为调整添加简短的 `style` 提示**：仅为需要进行特定投放调整的轮次添加简明的 `style` 字符串（例如 `"casual, friendly"` 或 `"muttering, then reassuring"`），并在需要保持一致基准时，在各个轮次中重复使用该简短字符串。

### 多轮对话和语音代理

构建实时对话式语音代理或多轮对话应用时：

- 在 LLM 文本块到达时，**每次轮次进行一次 TTS 调用**。
- 让配置的 `voice`（预构建、设计的 `voice_...` 或复制的 `voice_...` / `voicekey_...`）在对话轮次之间传递发言者的身份，而无需在每个轮次中重新发送长字符角色。
- 将每轮对话的 `style` 字段留空，或为整个对话发送一个简短的常量字符串（例如 `"casual, friendly"`）。
- 将较长的智能体回答拆分为较短的对话轮次，而不是使用更强烈的风格提示。

## 限制

- TTS 模型接受纯文本输入，并生成纯音频输出。
- 单次请求多说话人生成 (`speech_config.speakers`) 最多支持 2 位说话人，且使用预建语音。若要在多角色对话中组合自定义设计 (`voice_...`) 或复制 (`voice_...` / `voicekey_...`) 的声音，请单独合成每个说话者的发言。
  由于一元请求默认返回带有 44 字节 RIFF 标头的 `audio/wav`，因此请请求原始 PCM (`{"type": "audio", "mime_type": "audio/l16"}`) 或从每个回合中剥离 WAV 标头，然后再连接 24 kHz PCM 音频帧。
- **自定义语音存储空间限制和 TTL**：
  - **有状态的声音（`store=True`，提示或复制）**：每个项目最多 **200 个声音**，**1 年 TTL**（存留时间）。
  - **无状态语音密钥（`store=False`、`voicekey_...`）**： **7 天的 TTL**（存留时间）。
- 如需了解语言覆盖范围，请参阅[支持的语言](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#languages)部分。

## 后续步骤

- 借助[语音设计](https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-cn)，使用自然语言创建自定义声音角色。
- 在[语音复刻](https://ai.google.dev/gemini-api/docs/voice-replication?hl=zh-cn)中复刻现有说话者的声音。
- 在 [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn) 和 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) 模型页面上比较模型规范。
- 通过 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 探索交互式双向音频。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-02。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-02。"],[],[]]
