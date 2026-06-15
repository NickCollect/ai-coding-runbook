---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=zh-TW
fetched_at: 2026-06-15T06:33:08.612629+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Lyria 3 生成音樂

Lyria 3 是 Google 的音樂生成模型系列，可透過 Gemini API 使用。使用 Lyria 3，你可以根據文字提示或圖片生成高品質的 44.1 kHz 立體聲音訊。這些模型可提供結構一致的內容，包括人聲、歌詞時間碼和完整樂器編曲。

Lyria 3 系列包含兩種模型：

| 型號 | 模型 ID | 適用情境 | 時間長度 | 輸出 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短片、循環播放、預覽 | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | 包含主歌、副歌和橋段的完整歌曲 | 幾分鐘 (可使用提示控制) | MP3 |

這兩款模型都可透過新的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) 使用，支援多模態輸入 (文字和圖片)，並產生 **44.1 kHz 高精準度立體聲**音訊。

## 生成音樂短片

Lyria 3 Clip 模型一律會生成 **30 秒**片段。如要生成短片，請使用文字提示呼叫 `interactions.create` 方法。回覆一律會包含生成的歌詞和歌曲結構，以及 `steps` 架構中的音訊。

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
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

您可以使用 `interaction.output_audio` 屬性擷取生成的音樂資料，該屬性會傳回最後生成的音訊區塊。您也可以使用 `interaction.output_text` 屬性擷取歌曲的歌詞和結構。如要進一步瞭解便利性屬性，請參閱「[互動總覽](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw#convenience-properties)」。

## 生成完整歌曲

使用 `lyria-3-pro-preview` 模型生成幾分鐘的完整歌曲。Pro 模型可瞭解音樂結構，並創作具有不同段落、副歌和橋段的樂曲。如要調整時長，可以在提示中指定 (例如「創作 2 分鐘的歌曲」)，或使用[時間戳記](#timing)定義結構。

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
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## 選取輸出格式

根據預設，Lyria 3 模型會以 **MP3** 格式生成音訊。如果是 Lyria 3 Pro，您也可以設定 `response_format`，要求以 **WAV** 格式輸出。

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## 剖析回應

Lyria 3 的回覆會在 `steps` 架構中包含多個內容區塊。互動會傳回一系列步驟，其中 `model_output` 步驟包含生成的內容。文字內容區塊包含生成的歌詞，或是歌曲結構的 JSON 說明。`audio` 類型的內容區塊包含 Base64 編碼的音訊資料。

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

#### 交錯顯示歌詞和音樂

由於 Lyria 3 的輸出內容相當複雜，包含生成歌詞 (文字) 和歌曲本身 (音訊) 的個別步驟和區塊，因此建議使用便利性屬性，快速取得結果。

不過，如果您想以程式輔助方式，全面控管伺服器傳回的原始步驟時間軸 (例如在收到個別內容區塊時記錄)，可以手動疊代 `steps`：

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

## 根據圖片生成音樂

Lyria 3 支援多模態輸入內容，你可以在 `input` 清單中提供最多 **10 張圖片**和文字提示詞，模型就會根據視覺內容創作音樂。

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
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## 提供自訂歌詞

你可以自行撰寫歌詞，並加入提示。使用 `[Verse]`、`[Chorus]` 和 `[Bridge]` 等區段標記，協助模型瞭解歌曲結構：

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## 控制時間和結構

你可以使用時間戳記，指定歌曲在特定時間點的確切動作。這項功能有助於控制樂器進入的時間、歌詞的傳送時間，以及歌曲的進展方式：

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## 生成配樂

如要生成背景音樂、遊戲配樂或任何不需要人聲的音樂，可以提示模型生成純音樂曲目：

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## 生成不同語言的音樂

Lyria 3 會以提示的語言生成歌詞。如要生成法文歌詞的歌曲，請用法文撰寫提示。模型會調整語音風格和發音，配合所選語言。

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
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## 模型智慧

Lyria 3 會分析提示程序，根據提示透過音樂結構 (前奏、主歌、副歌、橋段等) 推理。這項程序會在生成音訊前執行，確保結構一致性和音樂性。

## 提示撰寫指南

提示越具體，結果就越符合需求。你可以加入以下內容，引導系統生成圖片：

- **類型**：指定類型或類型組合 (例如「lo-fi hip hop」、「jazz fusion」、「cinematic orchestral」)。
- **樂器**：指明樂器名稱 (例如「Fender Rhodes 鋼琴」、「滑音吉他」、「TR-808 鼓機」)。
- **BPM**：設定節奏 (例如「120 BPM」、「70 BPM 左右的慢節奏」)。
- **調性/音階**：指定調性 (例如「G 大調」、「D 小調」)。
- **情緒和氛圍**：使用描述性形容詞 (例如「懷舊」、「激進」、「空靈」、「夢幻」)。
- **結構**：使用 `[Verse]`、`[Chorus]`、`[Bridge]`、`[Intro]`、`[Outro]` 或時間戳記等標記，控制歌曲的進展。
- **長度**：短片模型一律會生成 30 秒的短片。如果是 Pro 版，請在提示中指定預期長度 (例如「創作 2 分鐘的歌曲」)，或使用時間戳記控制長度。

### 提示詞範例

以下列舉幾個有效的提示：

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 最佳做法

- **先使用 Clip 進行疊代。**使用速度較快的 `lyria-3-clip-preview` 模型測試提示，再使用 `lyria-3-pro-preview` 生成完整長度的內容。
- 提供**清楚明確**的說明，模糊不清的提示會產生一般結果。提及樂器、BPM、調性、情境和結構，以獲得最佳輸出內容。
- **語言相符。**以所需語言輸入提示。
- **使用章節標記。**`[Verse]`、`[Chorus]`、`[Bridge]` 標記可為模型提供明確的結構。
- **歌詞和指示請分開提供。**提供自訂歌詞時，請清楚區隔歌詞和音樂方向指示。

## 限制

- **安全性**：所有提示都會經過安全篩選器檢查。如果提示觸發篩選器，系統就會封鎖提示。包括要求特定藝人聲音的提示，或是生成受著作權保護的歌詞。
- **浮水印**：所有生成的音訊都會加上 [SynthID 音訊浮水印](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-tw)，以利識別。這種浮水印人耳無法辨識，不會影響聆聽體驗。
- **多輪編輯**：音樂生成是單輪程序。目前版本的 Lyria 3 不支援透過多個提示，反覆編輯或修正生成的片段。
- **長度**：Clip 模型一律會生成 30 秒的短片。Pro 模型會生成幾分鐘的歌曲，確切時長取決於提示。
- **決定性**：即使使用相同提示，每次呼叫的結果也可能不同。

## 後續步驟

- 查看 Lyria 3 模型的[定價](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=zh-tw)，
- 使用 Lyria RealTime [即時串流音樂生成](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=zh-tw)，
- 使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=zh-tw)生成多人對話，
- 瞭解如何生成[圖片](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=zh-tw)或[影片](https://ai.google.dev/gemini-api/docs/interactions/video?hl=zh-tw)，
- 瞭解 Gemini 如何[解讀音訊檔案](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=zh-tw)、
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/interactions/live?hl=zh-tw) 與 Gemini 即時對話。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
