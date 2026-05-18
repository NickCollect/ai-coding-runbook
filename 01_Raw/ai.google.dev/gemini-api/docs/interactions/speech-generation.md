---
source_url: https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=zh-TW
fetched_at: 2026-05-18T05:05:26.600778+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 生成文字轉語音檔案 (TTS)

Gemini API 可使用 Gemini 文字轉語音 (TTS) 生成功能，將文字輸入內容轉換為單人或多人語音。文字轉語音 (TTS) 生成功能*[可控](#controllable)*，也就是說，你可以使用自然語言建構互動，並引導音訊的*風格*、*口音*、*語速*和*語氣*。

TTS 功能與[Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) 提供的語音生成功能不同，後者專為互動式非結構化音訊，以及多模態輸入和輸出內容而設計。雖然 Live API 非常適合動態對話情境，但透過 Gemini API 進行文字轉語音則適用於需要準確朗讀文字，並精細控制樣式和聲音的情境，例如生成 Podcast 或有聲書。

本指南說明如何從文字產生單一說話者和多位說話者的音訊。

## 事前準備

請務必使用具備 Gemini 文字轉語音 (TTS) 功能的 Gemini 2.5 模型變體，如「[支援的模型](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=zh-tw#supported-models)」一節所述。為獲得最佳結果，請考慮哪種模型最適合您的特定用途。

建議您 [在 AI Studio 中測試 Gemini 2.5 TTS 模型]

## 單一說話者文字轉語音

如要將文字轉換為單一說話者的音訊，請將回應模式設為「音訊」，並傳遞含有語音名稱的 `speech_config` 物件。你必須從預先建構的[輸出語音](#voices)中選擇語音名稱。

這個範例會將模型的輸出音訊儲存為 Wave 檔案：

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

data = None
for step in interaction.steps:
    for content_block in step.content:
        if content_block.type == "audio":
            data = base64.b64decode(content_block.data)
            break
    if data:
        break
wave_file('out.wav', data)
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
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
   });

   let data = null;
   for (const step of interaction.steps) {
      for (const contentBlock of step.content) {
         if (contentBlock.type === 'audio') {
            data = contentBlock.data;
            break;
         }
      }
      if (data) break;
   }
   const audioBuffer = Buffer.from(data, 'base64');
   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## 多位說話者文字轉語音

如要使用多說話者音訊，您需要 `multi_speaker_voice_config` 物件，並將每個說話者 (最多 2 位) 設定為 `speaker_voice_config`。您必須使用與[提示](#controllable)中相同的名稱定義每個 `speaker`：

### Python

```
from google import genai
import wave
import base64

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

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_modalities=["audio"],
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

data = None
for step in interaction.steps:
   for content_block in step.content:
      if content_block.type == "audio":
         data = base64.b64decode(content_block.data)
         break
   if data:
      break
wave_file('out.wav', data)
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
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   let data = null;
   for (const step of interaction.steps) {
      for (const contentBlock of step.content) {
         if (contentBlock.type === 'audio') {
            data = contentBlock.data;
            break;
         }
      }
      if (data) break;
   }
   const audioBuffer = Buffer.from(data, 'base64');
   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_modalities": ["audio"],
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## 使用提示控制語音風格

無論是單人還是多人 TTS，都可以使用自然語言提示詞控制風格、語氣、口音和語速。舉例來說，在單一說話者的提示中，你可以說：

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

在多位說話者的提示詞中，請提供每位說話者的姓名和對應的轉錄稿。你也可以個別為每位揚聲器提供指引：

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

試著使用符合你想傳達風格或情緒的[語音選項](#voices)，進一步強調重點。舉例來說，在先前的提示中，*土衛二*的氣音可能強調「疲倦」和「無聊」，而*帕克*的歡快語氣則可與「興奮」和「快樂」相輔相成。

## 生成提示，將文字轉換為語音

文字轉語音模型只會輸出音訊，但您可以先使用[其他模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)生成轉錄稿，然後將轉錄稿傳遞至文字轉語音模型，讓模型朗讀內容。

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3-flash-preview",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.steps[-1].content[0].text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_modalities=["audio"],
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)

# ...Code to stream or save the output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3-flash-preview",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.steps.at(-1).content[0].text,
   response_modalities: ['audio'],
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## 語音選項

TTS 模型在 `voice_name` 欄位中支援下列 30 個語音選項：

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *Bright* | **Puck** - *Upbeat* | **Charon** - *獲得了實用的資訊* |
| **韓國** - *公司* | **Fenrir** - *興奮* | **Leda** -- *青春* |
| **Orus** -- *Firm* | **Aoede** - *Breezy* | **Callirrhoe** - *隨和* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** - *輕鬆* | **Algieba** - *平滑* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** - *Gravelly* | **Rasalgethi** - *實用資訊* |
| **Laomedeia** - *Upbeat* | **Achernar** - *柔和* | **Alnilam** - *Firm* |
| **Schedar** -- *Even* | **Gacrux** - *成人內容* | **Pulcherrima** -- *轉寄* |
| **Achird** - *Friendly* | **Zubenelgenubi** - *Casual* | **Vindemiatrix** - *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** - *知識豐富* | **Sulafat** -- *溫暖* |

你可以在

## 支援的語言

文字轉語音模型會自動偵測輸入語言。支援的語言如下：

| 語言 | BCP-47 代碼 | 語言 | BCP-47 代碼 |
| --- | --- | --- | --- |
| 阿拉伯文 | ar | 菲律賓文 | fil |
| 孟加拉文 | bn | 芬蘭文 | fi |
| 荷蘭文 | nl | 加里西亞文 | gl |
| 英文 | en | 喬治亞文 | ka |
| 法文 | fr | 希臘文 | el |
| 德文 | de | 古吉拉特文 | gu |
| 北印度文 | hi | 海地克里奧爾文 | ht |
| 印尼文 | id | 希伯來文 | 他 |
| 義大利文 | it | 匈牙利文 | hu |
| 日文 | ja | 冰島文 | 為 |
| 韓文 | ko | 爪哇語 | 爪哇文 |
| 馬拉地文 | mr | 卡納達文 | kn |
| 波蘭文 | pl | 貢根文 | kok |
| 葡萄牙文 | pt | 寮文 | lo |
| 羅馬尼亞文 | ro | 拉丁 | la |
| 俄文 | ru | 拉脫維亞文 | lv |
| 西班牙文 | es | 立陶宛文 | lt |
| 泰米爾文 | ta | 盧森堡文 | lb |
| 泰盧固文 | te | 馬其頓文 | mk |
| 泰文 | th | 邁蒂利文 | mai |
| 土耳其文 | tr | 馬達加斯加文 | mg |
| 烏克蘭文 | uk | 馬來文 | 毫秒 |
| 越南文 | vi | 馬拉雅拉姆文 | ml |
| 南非荷蘭文 | af | 蒙古文 | mn |
| 阿爾巴尼亞文 | sq | 尼泊爾文 | ne |
| 阿姆哈拉文 | am | 挪威文 (巴克摩) | nb |
| 亞美尼亞文 | hy | 挪威文 (新挪威文) | nn |
| 亞塞拜然文 | az | 歐利亞文 | 或 |
| 巴斯克文 | eu | 普什圖文 | ps |
| 白俄羅斯語 | be | 波斯文 | fa |
| 保加利亞文 | bg | 旁遮普文 | pa |
| 緬甸文 | my | 塞爾維亞文 | sr |
| 加泰隆尼亞文 | ca | 信德文 | sd |
| 宿霧文 | ceb | 錫蘭文 | si |
| 中文 (國語) | cmn | 斯洛伐克文 | sk |
| 克羅埃西亞文 | 時 | 斯洛維尼亞文 | sl |
| 捷克文 | cs | 史瓦西里文 | sw |
| 丹麥文 | da | 瑞典文 | sv |
| 愛沙尼亞文 | et | 烏都文 | ur |

## 支援的模型

| 型號 | 單一說話者 | 多位說話者 |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=zh-tw) | ✔️ | ✔️ |
| [Gemini 2.5 Flash 預先發布版 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=zh-tw) | ✔️ | ✔️ |
| [Gemini 2.5 Pro 預先發布版 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=zh-tw) | ✔️ | ✔️ |

## 提示撰寫指南

**Gemini 原生語音生成 Text-to-Speech (TTS)** 模型與傳統 TTS 模型不同，它使用的大型語言模型***不僅知道要說什麼，也知道該怎麼說***。

您可以將進階提示視為模型要遵循的系統指令。這項功能可為模型提供更多脈絡，並控管模型效能。

如要解鎖這項功能，使用者可以將自己視為導演，為虛擬配音員設定場景。如要製作提示詞，建議考慮下列元件：**聲音設定檔** (定義角色的核心特徵和原型)、**場景說明** (建立實體環境和情緒「氛圍」)，以及**導演附註** (提供更精確的表演指導，包括風格、口音和節奏控制)。

使用者可以提供細微的指令，例如精確的地域口音、特定的副語言特徵 (例如氣音) 或語速，運用模型的脈絡感知能力，生成高度動態、自然且富有表現力的音訊。為獲得最佳效能，建議**轉錄稿**和導演提示詞保持一致，*讓「誰說了什麼」*與「說了什麼」和「怎麼說」相符。

本指南旨在提供基本指引，並激發您在使用 Gemini TTS 音訊生成功能開發音訊體驗時的靈感。我們很期待看到你的創作！

### 音訊標記

標記是 `[whispers]` 或 `[laughs]` 等內嵌修飾符，可精細控管放送方式。你可以使用這些提示變更轉錄稿中某一行或某個部分的語氣、步調和情緒氛圍。你也可以使用這些音效，在表演中加入感嘆詞和其他非語言聲音，例如 `[cough]`、`[sighs]` 或 `[gasp]`。

我們無法提供標記的完整清單，建議您嘗試使用不同的情緒和表情，看看輸出結果有何變化。

如果轉錄稿不是英文，建議您仍使用英文音訊標記，以獲得最佳結果。

**善用音訊標記**

為展現音訊標記可帶來的多樣性，我們提供一系列範例，內容都相同，但傳達方式會因使用的標記而異。

你可以在行首加入標記，改變朗讀的強調方式，讓講者顯得興奮、無聊或不情願：

- `[excitedly]`你好，我是新的文字轉語音模型，可以透過多種方式說話。你今天想做什麼呢？
- `[bored]`你好，我是全新的文字轉語音模型…
- `[reluctantly]`你好，我是全新的文字轉語音模型…

標記也可以用來改變朗讀速度，或結合速度和強調：

- `[very fast]`你好，我是全新的文字轉語音模型…
- `[very slow]`你好，我是全新的文字轉語音模型…
- `[sarcastically, one painfully slow word at a time]`你好，我是新的文字轉語音模型…

你也可以精確控制特定段落，例如以氣音說出某個部分，並大聲說出另一個部分。

- `[whispers]`你好，我是新的文字轉語音模型，`[shouting]`可以透過多種方式說話。`[whispers]` 今天需要什麼協助嗎？

您也可以嘗試任何創意構想：

- `[like a cartoon dog]`你好，我是全新的文字轉語音模型…
- `[like dracula]`你好，我是全新的文字轉語音模型…

常用的標記包括：

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

標記可快速控制轉錄稿的傳送方式。如要進一步控管，可以將這些提示詞與情境提示詞結合，設定表演的整體基調和氛圍。

### 提示結構

完善的提示應包含下列元素，共同打造出色的演出：

- **音訊設定檔** - 為語音建立角色，定義角色身分、原型和任何其他特徵，例如年齡、背景等。
- **場景**：設定舞台。描述實體環境和「氛圍」。
- **導演筆記** - 提供成效指引，方便你細分虛擬藝人應注意的重要指示。例如風格、呼吸、節奏、咬字和口音。
- **情境範例**：為模型提供情境起點，讓虛擬演員自然進入您設定的場景。
- **轉錄稿**：模型會朗讀的文字。為獲得最佳成效，請注意轉錄稿主題和寫作風格應與你提供的指示相關。
- **音訊標記**：可插入轉錄稿的修飾符，用於變更文字部分的傳達方式，例如 `[whispers]` 或 `[shouting]`。

完整提示範例：

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
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### 詳細的提示策略

將提示的每個元素細分成以下內容：

#### 音訊格式設定

簡要描述角色的個性。

- **名稱**：為角色命名有助於模型掌握角色特徵，並提升效能。設定場景和情境時，請使用角色名稱
- **角色**：在場景中扮演的角色核心身分和原型，例如電台 DJ、Podcast 創作者、新聞記者等。

範例：

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### 場景

設定場景的背景資訊，包括地點、情境和環境細節，以確立基調和氛圍。描述角色周遭發生的情況，以及這些情況對角色的影響。場景會為整個互動提供環境背景資訊，並以細膩自然的方式引導表演。

範例：

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

#### 導演附註

這個重要章節包含具體的成效指引。您可以略過所有其他元素，但建議您加入這個元素。

請只定義對效能有重要影響的項目，並小心不要過度指定。如果嚴格規則過多，模型創意就會受到限制，成效也可能因此變差。根據具體的演出規則，平衡角色和場景說明。

最常見的指示是**風格、速度和口音**，但模型不限於這些指示，也不需要這些指示。您可以視需要加入自訂指令，涵蓋對成效有幫助的其他詳細資料，並盡可能詳細說明。

例如：

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**樣式：**

設定生成語音的語氣和風格。包括歡快、活力充沛、放鬆、無聊等情緒，引導表演。請盡可能詳細說明，並視需要提供詳細資料：*「熱情洋溢，聽眾應該感覺自己是盛大熱鬧社群活動的一份子。」*比「充滿活力和熱情」更貼切。

你甚至可以嘗試配音產業的熱門用語，例如「聲音微笑」。你可以視需要疊加多種風格特徵。

範例：

簡單情緒

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

複雜

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**口音：**

描述所選口音。描述得越具體，結果就越切合需求。例如，使用「*英國克羅伊登的英式英語口音*」而非「*英國口音*」。

範例：

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**使用速度：**

整部作品的整體節奏和節奏變化。

範例：

簡潔

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

複雜

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**歡迎試試**

在 [TTS 應用程式](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=zh-tw)中試試這些範例，讓 Gemini 帶你體驗導演的感覺。請參考以下訣竅，錄製出色的歌唱表演：

- 請務必確保提示內容一致，因為腳本和指示是打造優質表演的關鍵。
- 不必鉅細靡遺地描述所有內容，有時讓模型填補空白處，反而能產生更自然的結果。(就像才華洋溢的演員)
- 如果遇到瓶頸，不妨請 Gemini 協助撰寫劇本或演出。

## 限制

- 文字轉語音模型只能接收文字輸入內容，並生成音訊輸出內容。
- TTS 工作階段的[脈絡窗口](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)限制為 3.2 萬個權杖。
- 如需語言支援資訊，請參閱「[語言](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=zh-tw#languages)」一節。
- TTS 不支援串流。

使用 Gemini 3.1 Flash TTS 預先發布版模型生成語音時，須遵守下列限制：

- **語音與提示指令不一致：**模型輸出內容不一定會完全符合所選的說話者，因此音訊聽起來可能與預期不同。為避免語氣不一致 (例如低沉的男聲試圖模仿年輕女孩的聲音)，請確保提示詞的書面語氣和情境與所選講者的個人資料自然一致。
- **較長輸出內容的品質：**如果生成的輸出內容超過幾分鐘，語音品質和一致性可能會開始下降。建議將轉錄稿分割成較小的片段。
- **偶爾會傳回文字詞元：**模型偶爾會傳回文字詞元，而非音訊詞元，導致伺服器因 `500` 錯誤而無法處理要求。由於這類情況只會在極少數要求中隨機發生，因此您應在應用程式中實作自動重試邏輯，以便處理這些要求。
- **提示分類器誤拒：**模糊不清的提示詞可能無法觸發語音合成分類器，導致要求遭拒 (`PROHIBITED_CONTENT`)，或導致模型大聲朗讀風格指示和導演筆記。請加入清楚的前言，指示模型合成語音，並明確標示實際語音轉錄稿的開頭，藉此驗證提示。

## 後續步驟

- Gemini 的 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) 提供互動式音訊生成選項，可與其他模態交錯使用。
- 如要使用音訊*輸入*，請參閱「[音訊理解](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=zh-tw)」指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-09 (世界標準時間)。"],[],[]]
