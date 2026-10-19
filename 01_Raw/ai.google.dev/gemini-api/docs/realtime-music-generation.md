---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-TW
fetched_at: 2026-10-19T05:52:40.721818+00:00
title: "\u4f7f\u7528 Lyria RealTime \u5373\u6642\u751f\u6210\u97f3\u6a02 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Lyria RealTime 即時生成音樂

Gemini API 採用 [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=zh-tw)，可存取最先進的即時串流音樂生成模型。開發人員可藉此建構應用程式，讓使用者以互動方式創作、持續引導及演奏樂器音樂。

Lyria RealTime 音樂生成功能會使用 [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)，建立持續性的雙向低延遲串流連線。

如要體驗 Lyria RealTime 的功能，請在 AI Studio 中使用「提示 DJ」或「MIDI DJ」應用程式。

## 生成及控制音樂

Lyria RealTime 的運作方式與 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw) 類似，都是使用 Websocket 與模型維持即時通訊。

以下程式碼示範如何生成音樂：

### Python

這個範例會使用 `client.aio.live.music.connect()` 初始化 Lyria RealTime 工作階段，然後使用 `session.set_weighted_prompts()` 傳送初始提示，並使用 `session.set_music_generation_config` 傳送初始設定，使用 `session.play()` 開始生成音樂，並設定 `receive_audio()` 來處理收到的音訊區塊。

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1beta'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

這個範例會使用 `client.live.music.connect()` 初始化 Lyria RealTime 工作階段，然後透過 `session.setWeightedPrompts()` 傳送初始提示，並使用 `session.setMusicGenerationConfig` 設定初始設定，透過 `session.play()` 開始生成音樂，並設定 `onMessage` 回呼來處理收到的音訊區塊。

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1beta" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

然後使用 `session.play()`、`session.pause()`、`session.stop()` 和 `session.reset_context()` 啟動、暫停、停止或重設工作階段。

## 即時引導音樂

你可以傳送提示並即時更新生成參數，即時引導音樂生成。

### 提示 Lyria RealTime

在串流期間，你隨時可以傳送新的 `WeightedPrompt` 訊息，改變生成的音樂。模型會根據新輸入內容順暢轉換。

提示必須採用正確格式，包含 `text` (實際提示) 和 `weight`。`weight` 可以是 `0` 以外的任何值。`1.0` 通常是不錯的起點。

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

請注意，大幅變更提示時，模型轉換可能會有些突然，因此建議傳送中間權重值給模型，實作某種淡入淡出效果。

### 更新設定

您可以即時更新音樂生成參數，引導音樂生成。您無法只更新參數，必須設定整個設定，否則其他欄位會重設為預設值。

由於更新 BPM 或音階會大幅改變模型，您也需要使用 `reset_context()` 重設模型的情境，才能將新設定納入考量。這不會停止串流，但會是硬性轉換。其他參數則不需要。

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## 提示詞：Lyria RealTime

Lyria RealTime 會使用加權提示詞，動態融合音樂類型、樂器和情緒。如要瞭解提示詞引導策略、關鍵字標記詞彙和完整提示詞範例，請參閱 [Lyria 提示詞指南](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=zh-tw#realtime-prompting)。

## 最佳做法

- 用戶端應用程式必須實作完善的音訊緩衝區，確保播放過程順暢。這有助於考量網路抖動和生成延遲的微小變化。
- 有效提示：
  - 文意要明確。使用形容詞描述情境、曲風和樂器。
  - 逐步迭代和引導。請嘗試新增或修改元素，讓音樂更流暢地變形，而不是完全變更提示。
  - 實驗 `WeightedPrompt` 的權重，瞭解新提示對持續生成作業的影響程度。

## 技術詳細資料

本節將詳細說明如何使用 Lyria RealTime 音樂生成功能。

### 規格

- 輸出格式：原始 16 位元 PCM 音訊
- 取樣率：48kHz
- 聲道：2 (立體聲)

### 控制項

傳送含有下列內容的訊息，即可即時影響音樂生成：

- `WeightedPrompt`：描述音樂概念、類型、樂器、情緒或特徵的文字字串。您可以提供多個提示，混合不同風格的影響。如要進一步瞭解如何以最佳方式提示 Lyria RealTime，請參閱[上文](#steer-music)。
- `MusicGenerationConfig`：音樂生成程序的設定，會影響輸出音訊的特徵。參數
  include：
  - `guidance`：(浮點數) 範圍：`[0.0, 6.0]`。預設值：`4.0`。
    控制模型遵守提示詞的嚴格程度。引導值越高，越能遵守提示，但轉場效果會更突兀。
  - `bpm`：(int) 範圍：`[60, 200]`。
    設定要生成的音樂每分鐘節拍數。你必須停止/播放或重設模型的脈絡，模型才會將新的 BPM 納入考量。
  - `density`：(浮點數) 範圍：`[0.0, 1.0]`。
    控制音符/聲音的密度。值越低，生成的音樂越稀疏；值越高，生成的音樂越「忙碌」。
  - `brightness`：(浮點數) 範圍：`[0.0, 1.0]`。
    調整音質。值越高，音訊聽起來就越「明亮」，通常會強調高頻率。
  - `scale`：(列舉) 設定生成音樂的音階 (調性和模式)。請使用 SDK 提供的[`Scale` 列舉值](#scale-enum)。您需要停止/播放或重設模型考量的內容，才能納入新的比例。
  - `mute_bass`：(bool) 預設值：`False`。
    控制模型是否要降低輸出內容的低音。
  - `mute_drums`：(bool) 預設值：`False`。
    控制模型輸出內容是否要減少輸出內容的鼓聲。
  - `only_bass_and_drums`：(bool) 預設值：`False`。
    引導模型只輸出貝斯和鼓聲。
  - `music_generation_mode`：(列舉) 指出模型應著重於`QUALITY` (預設值) 或`DIVERSITY`。也可以設為 `VOCALIZATION`，讓模型將人聲生成為另一種樂器 (新增為提示)。
- `PlaybackControl`：控制播放作業的指令，例如播放、暫停、停止或重設內容。

如果沒有提供 `bpm`、`density`、`brightness` 和 `scale` 的值，模型會根據初始提示決定最佳做法。

您也可以在 `MusicGenerationConfig` 中自訂更多傳統參數，例如 `temperature` (0.0 至 3.0，預設為 1.1)、`top_k` (1 至 1000，預設為 40) 和 `seed` (0 至 2147483647，預設為隨機選取)。

#### 擴大規模列舉值

模型可接受的所有比例值如下：

| 列舉值 | 音階 / 調性 |
| --- | --- |
| `C_MAJOR_A_MINOR` | C 大調 / A 小調 |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | 降 D 大調 / 降 B 小調 |
| `D_MAJOR_B_MINOR` | D 大調 / B 小調 |
| `E_FLAT_MAJOR_C_MINOR` | 降 E 大調 / C 小調 |
| `E_MAJOR_D_FLAT_MINOR` | E 大調 / C♯/D♭ 小調 |
| `F_MAJOR_D_MINOR` | F 大調 / D 小調 |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | 降 G 大調 / 降 E 小調 |
| `G_MAJOR_E_MINOR` | G 大調 / E 小調 |
| `A_FLAT_MAJOR_F_MINOR` | 降 A 大調 / F 小調 |
| `A_MAJOR_G_FLAT_MINOR` | A 大調 / F♯/G♭ 小調 |
| `B_FLAT_MAJOR_G_MINOR` | 降 B 大調 / G 小調 |
| `B_MAJOR_A_FLAT_MINOR` | B 大調 / G♯/A♭ 小調 |
| `SCALE_UNSPECIFIED` | 預設 / 由模型判斷 |

該模型可以引導播放音符，但無法區分相對調。因此每個列舉都會對應相對應的主要和次要版本。舉例來說，`C_MAJOR_A_MINOR` 對應鋼琴的所有白鍵，`F_MAJOR_D_MINOR` 則對應所有白鍵，但降 B 除外。

### 限制

- 純音樂：模型只會生成純音樂。
- 安全：系統會透過安全篩選機制檢查提示，如果提示觸發篩選器，系統會忽略提示，並在輸出內容的 `filtered_prompt` 欄位中提供說明。
- 浮水印：根據我們的[負責任的 AI 技術](https://ai.google/responsibility/principles/?hl=zh-tw) 原則，輸出音訊一律會加上浮水印，以利識別。

## 後續步驟

- 使用 [Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-tw) 生成完整歌曲和人聲音軌，
- 瞭解如何使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)生成多位說話者的對話，而非音樂。
- 瞭解如何生成[圖片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)或[影片](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)，
- Gemini 無法生成音樂或音訊，但可以[瞭解音訊檔案](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw)，
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw) 與 Gemini 即時對話。

如需更多程式碼範例和教學課程，請參閱[教戰手冊](https://github.com/google-gemini/cookbook)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-18 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-18 (世界標準時間)。"],[],[]]
