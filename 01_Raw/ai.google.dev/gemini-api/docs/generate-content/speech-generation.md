---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-CN
fetched_at: 2026-09-21T05:56:11.663842+00:00
title: "\u6587\u5b57\u8f6c\u8bed\u97f3\u751f\u6210 (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 文字转语音生成 (TTS)

Gemini API 可以使用 Gemini 文字转语音 (TTS) 生成功能将文本输入转换为单个说话者或多个说话者的音频。文字转语音 (TTS) 生成是*[可控](#controllable)*的，这意味着您可以使用自然语言来构建互动，并指导音频的*风格*、*口音*、*语速*和*语气*。

[在 Google AI Studio 中试用](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=zh-cn)

TTS 功能不同于通过 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 提供的语音生成功能，后者专为交互式非结构化音频以及多模态输入和输出而设计。虽然 Live API 在动态对话上下文中表现出色，但通过 Gemini API 实现的 TTS 专门针对需要精确朗读文本并对风格和声音进行精细控制的场景，例如播客或有声读物生成。

本指南介绍了如何根据文本生成单说话者和多说话者音频。

## 准备工作

请务必使用具有 Gemini 文字转语音 (TTS) 功能的 Gemini 模型变体，如[支持的模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#supported-models)部分中所列。为获得最佳效果，请考虑哪种模型最适合您的特定使用情形。

在开始构建之前，您可能会发现[在 AI Studio 中测试 Gemini TTS 模型](https://aistudio.google.com/generate-speech?hl=zh-cn)很有用。

## 单说话者 TTS

如需将文本转换为单人音频，请将响应模态设置为“audio”，并传递一个设置了 `VoiceConfig` 的 `SpeechConfig` 对象。您需要从预建的[输出语音](#voices)中选择一个语音名称。

此示例将模型输出的音频保存到 Wave 文件中：

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## 多说话人 TTS

对于多扬声器音频，您需要一个 `MultiSpeakerVoiceConfig` 对象，其中每个扬声器（最多 2 个）都配置为 `SpeakerVoiceConfig`。您需要使用 [提示](#controllable)中使用的相同名称来定义每个 `speaker`：

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## 通过提示控制说话风格

您可以使用自然语言提示或[音频标记](#transcript-tags)来控制单个说话者和多个说话者的 TTS 风格、语气、口音和语速。
例如，在单人提示中，您可以说：

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

在多位发言者的提示中，为模型提供每位发言者的姓名和相应的转写内容。您还可以单独为每个音箱提供指导：

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

不妨尝试使用与您想要传达的风格或情感相对应的[语音选项](#voices)，以进一步强调。例如，在前面的提示中，*恩克拉多斯*的气息声可能强调“疲倦”和“无聊”，而 *Puck* 的欢快语气可能与“兴奋”和“快乐”相得益彰。

## 生成用于转换为音频的提示

TTS 模型仅输出音频，但您可以先使用[其他模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)生成转写内容，然后将该转写内容传递给 TTS 模型以进行朗读。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.6-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3.6-flash",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## 语音选项

TTS 模型在 `voice_name` 字段中支持以下 30 种语音选项：

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *明亮* | **Puck** - *欢快* | **Charon** - *信息丰富* |
| **Kore** - *坚定* | **Fenrir** - *易兴奋* | **Leda** - *青春* |
| **Orus** - *公司* | **Aoede** - *Breezy* | **Callirrhoe** - *轻松* |
| **Autonoe** - *明亮* | **Enceladus** - *气声* | **Iapetus** - *清晰* |
| **Umbriel** - *随和* | **Algieba** - *平滑* | **Despina** - *平滑* |
| **Erinome** - *清除* | **Algenib** - *Gravelly* | **Rasalgethi** - *信息丰富* |
| **Laomedeia** - *欢快* | **Achernar** - *柔和* | **Alnilam** - *坚定* |
| **Schedar** - *偶数* | **Gacrux** - *成熟* | **Pulcherrima** - *转发* |
| **Achird** - *友好* | **Zubenelgenubi** - *随意* | **Vindemiatrix** - *柔和* |
| **Sadachbia** - *活泼* | **Sadaltager** - *知识渊博* | **Sulafat** - *偏高* |

您可以在 [AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中试听所有语音选项。

## 支持的语言

TTS 模型会自动检测输入语言。支持以下语言：

| 语言 | BCP-47 代码 | 语言 | BCP-47 代码 |
| --- | --- | --- | --- |
| 阿拉伯语 | ar | 菲律宾语 | fil |
| 孟加拉语 | bn | 芬兰语 | fi |
| 荷兰语 | nl | 加利西亚语 | gl |
| 英语 | en | 格鲁吉亚语 | ka |
| 法语 | fr | 希腊语 | el |
| 德语 | de | 古吉拉特语 | gu |
| 印地语 | hi | 海地克里奥尔语 | ht |
| 印度尼西亚语 | id | 希伯来语 | 他 |
| 意大利语 | it | 匈牙利语 | hu |
| 日语 | ja | 冰岛语 | ： |
| 韩语 | ko | 爪哇语 | jv |
| 马拉地语 | mr | 卡纳达语 | kn |
| 波兰语 | pl | 贡根语 | kok |
| 葡萄牙语 | pt | 老挝语 | lo |
| 罗马尼亚语 | ro | 拉丁语 | la |
| 俄语 | ru | 拉脱维亚语 | lv |
| 西班牙语 | es | 立陶宛语 | lt |
| 泰米尔语 | ta | 卢森堡语 | lb |
| 泰卢固语 | te | 马其顿语 | mk |
| 泰语 | th | 迈蒂利语 | mai |
| 土耳其语 | tr | 马尔加什语 | mg |
| 乌克兰语 | uk | 马来语 | 毫秒 |
| 越南语 | vi | 马拉雅拉姆语 | ml |
| 南非荷兰语 | af | 蒙古语 | mn |
| 阿尔巴尼亚语 | sq | 尼泊尔语 | ne |
| 阿姆哈拉语 | am | 挪威语（博克马尔语） | nb |
| 亚美尼亚语 | hy | 挪威语（尼诺斯克语） | nn |
| 阿塞拜疆语 | az | 奥里亚语 | 或 |
| 巴斯克语 | eu | 普什图语 | ps |
| 白俄罗斯语 | be | 波斯语 | fa |
| 保加利亚语 | bg | 旁遮普语 | pa |
| 缅甸语 | my | 塞尔维亚语 | sr |
| 加泰罗尼亚语 | ca | 信德语 | sd |
| 宿务语 | ceb | 僧伽罗语 | si |
| 中文（普通话） | cmn | 斯洛伐克语 | sk |
| 克罗地亚语 | 小时 | 斯洛文尼亚语 | sl |
| 捷克语 | cs | 斯瓦希里语 | sw |
| 丹麦语 | da | 瑞典语 | sv |
| 爱沙尼亚语 | et | 乌尔都语 | ur |

## 支持的模型

| 模型 | 一位说话者 | 多音箱 |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=zh-cn) | ✔️ | ✔️ |
| [Gemini 2.5 Flash 预览版 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=zh-cn) | ✔️ | ✔️ |
| [Gemini 2.5 Pro 预览版 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=zh-cn) | ✔️ | ✔️ |

## 提示指南

**Gemini 原生音频生成文字转语音 (TTS)** 模型与传统 TTS 模型的不同之处在于，它使用的大语言模型不仅知道***要说什么，还知道怎么说***。

该模型开箱即可使用，能够以原生方式解读脚本，并确定您应如何表达台词。不含任何额外提示的简单转写内容听起来很自然。不过，Gemini TTS 还附带了一些可用于引导它的工具。

本指南旨在为开发音频体验提供基本指导，并激发创意。我们将先介绍用于快速内嵌控制的**标记**，然后探索用于全面指导性能的高级**提示结构**。

### 音频标签

标记是内嵌修饰符，例如 `[whispers]` 或 `[laughs]`，可让您对广告投放进行精细控制。您可以使用这些标记来更改转写内容中某行或某部分的语气、节奏和情感氛围。您还可以使用它们在表演中添加感叹词和其他一些非语言声音，例如 `[cough]`、`[sighs]` 或 `[gasp]`。

我们无法提供有关哪些标记有效、哪些标记无效的详尽列表，建议您尝试使用不同的情绪和表达方式，看看输出结果会发生怎样的变化。

如果您的转写内容不是英语，为了获得最佳效果，我们建议您仍然使用英语音频标记。

**巧妙运用音频标记**

为了展示音频标记可带来的各种变化，下面提供了一组示例，这些示例都表达了相同的内容，但传递方式会根据所用的标记而变化。

您可以在行开头添加标记，让朗读者的语气变得兴奋、无聊或不情愿，从而改变朗读的重点：

- `[excitedly]` 大家好，我是一个新的文字转语音模型，可以用多种不同的方式说话。今天需要我做些什么？
- `[bored]` 嗨，我是一个新的文字转语音模型…
- `[reluctantly]` 嗨，我是一个新的文字转语音模型…

您还可以使用标记来改变朗读速度，或将朗读速度与强调效果相结合：

- `[very fast]` 嗨，我是一个新的文字转语音模型…
- `[very slow]` 嗨，我是一个新的文字转语音模型…
- `[sarcastically, one painfully slow word at a time]` 大家好，我是新的文字转语音模型…

您还可以精确控制特定部分，这意味着您可以低声细语地朗读一部分，大声朗读另一部分。

- `[whispers]`大家好，我是一个新的文字转语音模型，`[shouting]`可以用多种不同的方式说话。`[whispers]` 您今天需要什么帮助

您还可以尝试任何您想到的创意：

- `[like a cartoon dog]` 嗨，我是一个新的文字转语音模型…
- `[like dracula]` 嗨，我是一个新的文字转语音模型…

常用标记包括：

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

通过标记，您可以快速轻松地控制转写内容的交付。为了获得更精细的控制，您可以将它们与上下文提示相结合，以设置表演的整体基调和氛围。

### 高级提示

您可以将高级提示视为模型要遵循的系统指令。这是一种为模型提供更多上下文并控制其性能的方法。

一个出色的提示应包含以下要素，这些要素共同构成出色的效果：

- **音频配置文件** - 为语音建立角色，定义角色身份、原型和任何其他特征，例如年龄、背景等。
- **场景** - 设置舞台。描述实体环境和“氛围”。
- **导演笔记** - 效果指南，您可以在其中细分哪些指令对虚拟人才来说是需要注意的重要事项。例如，风格、呼吸、节奏、发音和口音。
- **示例上下文** - 为模型提供上下文起点，以便虚拟演员自然地进入您设置的场景。
- **转写内容** - 模型将朗读的文本。为获得最佳性能，请注意转写内容的主题和写作风格应与您给出的指令相关。
- **音频标记** - 您可以添加到转写内容中的修饰符，用于更改文本相应部分的朗读方式，例如 `[whispers]` 或 `[shouting]`。

完整提示示例：

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### 详细的提示策略

下面我们来详细了解提示的各个要素。

#### 音频配置

简要描述角色的性格。

- **名称**：为角色命名有助于将模型和紧凑的表演联系起来，在设置场景和背景时，请使用角色的名称来指代角色
- **角色。**场景中正在扮演的角色的核心身份和原型。例如，电台 DJ、播客主播、新闻记者等。

示例：

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### 场景

设置场景的背景信息，包括地点、氛围和环境细节，以确定基调和氛围。描述角色周围发生的事情以及这些事情对角色的影响。场景为整个互动提供了环境背景，并以微妙的自然方式引导表演。

示例：

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### 导演备注

此关键部分包含具体的性能指导。您可以跳过所有其他元素，但我们建议您添加此元素。

仅定义对性能至关重要的内容，并注意不要过度指定。过于严格的规则会限制模型的创造力，并可能导致效果不佳。根据具体的表演规则，平衡角色和场景说明。

最常见的指令是**风格、语速和口音**，但模型不限于这些指令，也不要求使用这些指令。您可以随意添加自定义说明，以涵盖对效果至关重要的任何其他细节，并根据需要提供尽可能详细或尽可能简略的说明。

例如：

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**样式**：

设置生成的语音的语气和风格。包括欢快、活力、放松、无聊等，以指导表演。请尽可能详细地描述，并提供必要的细节：*“富有感染力的热情。听众应该感觉自己身处一场盛大而精彩的社区活动中。”*比简单地说“充满活力和热情”效果更好。

您甚至可以尝试配音行业中的热门术语，例如“声音微笑”。您可以根据需要叠加任意数量的样式特征。

示例：

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

更深入

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

复杂

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Accent**：

描述所需的口音。描述越具体，结果就越好。例如，使用“*英国克罗伊登的英式英语口音*”而不是“*英式口音*”。

示例：

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**预算花费进度**：

整个作品的总体节奏和节奏变化。

示例：

简单

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

更深入

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

复杂

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### 转写内容和音频标记

脚本是模型将要朗读的确切字词。音频标记是指方括号中的字词，用于指示某句话应如何说、语气变化或插话。

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**快来试试吧**

在 [AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中亲自尝试这些示例，体验我们的 [TTS 应用](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=zh-cn)，让 Gemini 助您成为导演。请谨记以下提示，以获得出色的演唱效果：

- 请务必确保整个提示连贯一致，因为脚本和指令是打造出色表演的关键。
- 您不必描述所有内容，有时给模型留出填补空白的空间有助于提高自然度。（就像一位才华横溢的演员）
- 如果您在任何时候感到卡壳，都可以让 Gemini 帮您撰写剧本或表演。

## 流式语音生成

您可以流式传输模型生成的音频。这有助于缩短感知延迟时间。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response_stream = client.models.generate_content_stream(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

for chunk in response_stream:
   try:
      data = chunk.candidates[0].content.parts[0].inline_data.data
      # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
      # Process the audio chunk (e.g., play it or write to a file)
   except (IndexError, AttributeError):
      pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        }
    }'
```

## 限制

- TTS 模型只能接收文本输入并生成音频输出。
- 一个 TTS 会话的[上下文窗口](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)限制为 3.2 万个 token。
- 如需了解语言支持，请参阅[语言](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#languages)部分。
- 对于 3.1 版之前的模型，TTS 不支持流式传输（`gemini-3.1-flash-tts-preview` 及更新版本的模型支持流式传输）。

使用 Gemini 3.1 Flash TTS 预览版模型生成语音时，需遵循以下限制：

- **语音与提示指令不一致**：模型的输出可能并不总是与所选的朗读人完全一致，导致音频听起来与预期不同。为避免出现音调不匹配的情况（例如，低沉的男声试图像年轻女孩那样说话），请确保提示的文字语气和上下文与所选发言者的个人资料自然契合。
- **较长输出的质量**：如果生成的输出时长超过几分钟，语音质量和一致性可能会开始下降。建议您将转写内容拆分成较小的块。
- **偶尔返回文本令牌**：模型偶尔会返回文本令牌而不是音频令牌，导致服务器因 `500` 错误而使请求失败。由于这种情况仅在极少数请求中随机发生，因此您应在应用中实现自动重试逻辑来处理这些情况。
- **提示分类器错误拒绝**：模糊的提示可能无法触发语音合成分类器，导致请求被拒绝 (`PROHIBITED_CONTENT`)，或者导致模型大声朗读您的风格说明和导演注释。添加清晰的序言，指示模型合成语音，并明确标记实际语音转写内容的开始位置，从而验证提示。

## 后续步骤

- 不妨试试[音频生成实战宝典](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=zh-cn)。
- Gemini 的 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 提供交互式音频生成选项，您可以将其与其他模态穿插使用。
- 如需了解如何处理音频*输入*，请参阅[音频理解](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
