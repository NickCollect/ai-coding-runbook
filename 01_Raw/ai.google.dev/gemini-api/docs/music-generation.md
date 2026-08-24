---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-CN
fetched_at: 2026-08-24T02:28:28.835021+00:00
title: "\u4f7f\u7528 Lyria 3 \u751f\u6210\u97f3\u4e50 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Lyria 3 生成音乐

Lyria 3 是 Google 的音乐创作模型系列，可通过 Gemini API 调用。借助 Lyria 3，您可以根据文本提示或图片生成高质量的 44.1 kHz 立体声音频。这些模型可提供结构连贯的音乐，包括人声、同步歌词及完整的器乐编排。

Lyria 3 系列包含两款型号：

| 模型 | 模型 ID | 适用场景 | 时长 | 输出 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短片、循环播放的视频、预览 | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | 包含主歌、副歌和桥段的完整歌曲 | 几分钟（可通过提示控制） | MP3 |

这两种模型均可通过新的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 使用，支持多模态输入（文本和图片），并生成 **44.1 kHz 高保真立体声**音频。

## 生成音乐片段

Lyria 3 Clip 模型始终生成 **30 秒**的片段。如需生成剪辑，请使用文本提示调用 `interactions.create` 方法。响应始终包含生成的歌词和歌曲结构，以及 `steps` 架构中的音频。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

您可以使用 `interaction.output_audio` 属性检索生成的音乐数据，该属性会返回上次生成的音频块。您还可以使用 `interaction.output_text` 属性检索歌曲的歌词和结构。如需详细了解便捷属性，请参阅[互动概览](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn#convenience-properties)。

## 生成完整歌曲

使用 `lyria-3-pro-preview` 模型生成时长几分钟的完整歌曲。Pro 模型能理解音乐结构，并能创作出具有鲜明主歌、副歌和桥段的乐曲。您可以在提示中指定时长（例如“创作一首 2 分钟的歌曲”），也可以使用[时间戳](#timing)来定义结构，从而影响时长。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## 选择输出格式

默认情况下，Lyria 3 模型会生成 **MP3** 格式的音频。对于 Lyria 3 Pro，您还可以通过设置 `response_format` 以 **WAV** 格式请求输出。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## 解析响应

来自 Lyria 3 的响应包含 `steps` 架构中的多个内容块。互动会返回一系列步骤，其中 `model_output` 步包含生成的内容。文本内容块包含生成的歌词或歌曲结构的 JSON 说明。
类型为 `audio` 的内容块包含 base64 编码的音频数据。

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### 交错显示歌词和音乐

由于 Lyria 3 的输出较为复杂，包含用于生成歌词（文本）和歌曲本身（音频）的单独步骤和代码块，因此便利属性可提供快速且推荐的快捷方式。

不过，如果您想以程序化方式完全控制服务器返回的原始步进时间轴（例如在收到各个内容块时记录它们），可以手动迭代 `steps`：

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## 根据图片生成音乐

Lyria 3 支持多模态输入 - 您可以在 `input` 列表中提供最多 **10 张图片**以及文本提示，模型将根据视觉内容创作音乐。

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## 提供自定义歌词

您可以自行撰写歌词，并将其添加到提示中。使用 `[Verse]`、`[Chorus]` 和 `[Bridge]` 等部分标记来帮助模型了解歌曲结构：

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## 控制时间和结构

您可以使用时间戳来精确指定歌曲中特定时刻发生的情况。这有助于控制乐器何时进入、歌词何时出现以及歌曲的进展方式：

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## 生成纯音乐轨道

对于背景音乐、游戏配乐或不需要人声的任何使用场景，您可以提示模型生成纯乐器曲目：

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## 生成不同语言的音乐

Lyria 3 会根据提示的语言生成歌词。如需生成带有法语歌词的歌曲，请使用法语撰写提示。模型会调整其发音风格和发音，以匹配相应语言。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## 模型智能

Lyria 3 会分析您的提示流程，其中模型会根据您的提示推断音乐结构（前奏、主歌、副歌、桥段等）。此过程在生成音频之前进行，可确保结构连贯性和音乐性。

## 提示指南

提示越具体，结果就越好。以下是您可以添加的内容，以便引导生成：

- **流派**：指定一种流派或多种流派的混合体（例如“低保真嘻哈”“爵士融合”“电影管弦乐”）。
- **乐器**：指明具体乐器（例如“Fender Rhodes 钢琴”“滑棒吉他”“TR-808 鼓机”）。
- **BPM**：设置节奏（例如“120 BPM”“70 BPM 左右的慢节奏”）。
- **调/音阶**：指定音乐调（例如“G 大调”“D 小调”）。
- **曲调和氛围**：使用描述性的形容词（例如“怀旧”“激进”“空灵”“梦幻”）。
- **结构**：使用 `[Verse]`、`[Chorus]`、`[Bridge]`、`[Intro]`、`[Outro]` 等标记或时间戳来控制歌曲的播放进度。
- **时长**：Clip 模型始终生成 30 秒的片段。对于 Pro 版，请在提示中指定预期时长（例如，“创作一首 2 分钟的歌曲”），或使用时间戳来控制时长。

### 示例提示

以下是一些有效提示的示例：

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 最佳做法

- **先使用 Clip 进行迭代。**使用速度更快的 `lyria-3-clip-preview` 模型来测试提示，然后再使用 `lyria-3-pro-preview` 生成完整内容。
- **内容要具体。**模糊的提示会产生一般性的结果。提及乐器、BPM、调、基调和结构，以获得最佳输出。
- **语言匹配。**使用您想要的歌词语言发出提示。
- **使用部分标记。**`[Verse]`、`[Chorus]`、`[Bridge]` 标记为模型提供了清晰的结构，以便模型遵循。
- **将歌词与说明分开。**提供自定义歌词时，请务必将其与音乐指导说明分开。

## 限制

- **安全性**：所有提示都会经过安全过滤器的检查。触发过滤条件的提示将被屏蔽。这包括要求使用特定音乐人声音或生成受版权保护的歌词的提示。
- **水印**：所有生成的音频都包含 [SynthID 音频水印](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-cn)，以便进行识别。这种水印人耳无法察觉，不会影响聆听体验。
- **多轮编辑**：音乐创作是一个单轮过程。在当前版本的 Lyria 3 中，不支持通过多个提示迭代编辑或优化生成的剪辑。
- **时长**：Clip 模型始终生成 30 秒的片段。Pro 模型生成的歌曲时长为几分钟；确切时长会受到提示的影响。
- **确定性**：即使使用相同的提示，不同调用之间的结果也可能会有所不同。

## 后续步骤

- 查看 Lyria 3 模型的[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。
- 不妨试试 Lyria RealTime，体验[实时流式音乐创作](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-cn)。
- 使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)生成多说话人对话。
- 了解如何生成[图片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)或[视频](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)。
- 了解 Gemini 如何[理解音频文件](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)。
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 与 Gemini 进行实时对话。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
