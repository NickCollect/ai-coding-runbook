---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=zh-TW
fetched_at: 2026-11-02T07:16:50.509411+00:00
title: "\u4f7f\u7528 Gemini Live API \u9032\u884c\u5373\u6642\u8f49\u9304 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini Live API 進行即時轉錄

Gemini Live API 支援使用 [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=zh-tw) 模型，進行低延遲、即時的語音轉文字轉錄。透過 WebSockets 連線至 Live API，或使用 Google Gen AI SDK，即可串流傳輸連續音訊輸入，並在語音出現時，即時接收遞增的文字轉錄稿。

[在 Google AI Studio 試用即時轉錄mic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=zh-tw)
[開啟 Colab 教戰手冊code](https://github.com/google-gemini/cookbook)
[使用程式設計代理技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw#gemini-live-api-dev)

開發人員平台 (例如 [Agora](https://docs.agora.io/en/ai/models/asr/gemini)、[Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration)、[LiveKit](https://docs.livekit.io/agents/models/stt/gemini/)、[Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google)、[Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) 和 [Vision Agents](https://visionagents.ai/integrations/stt/gemini)) 運用 Gemini Live API，讓開發人員輕鬆建構及部署高效能的語音介面。這些平台會在幕後管理複雜的即時媒體串流基礎架構，讓開發人員能全心打造使用者體驗。

## 真人服務專員與即時轉錄

雖然兩者都使用 Live API 雙向串流連線，但「即時轉錄」是專用的低延遲語音辨識管道，而非對話式代理。

| 功能 | 線上服務專員 | 即時轉錄 |
| --- | --- | --- |
| **主要作用** | 可聽取、推理及回覆的對話式助理。 | 即時語音轉文字管道，可轉錄傳入的音訊。 |
| **回覆模態** | 語音音訊和文字 (`response_modalities=["AUDIO"]`)。 | 串流文字轉錄 (`response_modalities=["TEXT"]`)。 |
| **互動風格** | 輪流對話，可偵測停頓和中斷。 | 在說話者發言時持續串流處理。 |
| **支援的功能** | 在 `gemini-3.8-live` 啟用呼叫函式、Google 搜尋、系統指令、輸入音訊轉錄和語音偏誤 (`custom_vocabulary`)。 | 語音偏誤 (`custom_vocabulary`)、語言偵測、手動和混合 VAD、智慧轉錄。 |
| **輸入串流** | 多模態：音訊、影片、圖片、文字。 | 音訊輸入 (原始 16 位元 PCM)。 |

## 開始使用

下列範例說明如何使用 `gemini-3.5-transcribe-live` 開啟雙向串流工作階段，並接收即時語音轉錄內容。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSocket

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## 暫定和最終語音轉錄內容

音訊串流傳入 Live API 時，伺服器會在 `server_content` 中發出兩個互補的轉錄欄位：

- **`interim_input_transcription`**：低延遲、推測性的部分假設，會在說話者主動說話時更新。這類部分更新會快速進行，延遲時間極短。使用 `interim_input_transcription` 轉譯回應式即時 UI 字幕或預覽字幕。
- **`input_transcription`**：說話者暫停、輪流結束或語音結束時，系統會發出最終轉錄稿。輸出後，這段文字代表模型對該語音片段的權威轉錄。在智慧語音轉錄模式中，這會包含經過清理和格式化的回覆。

以下範例說明如何顯示串流臨時部分內容，並提交最終轉錄稿：

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSocket

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## 正在傳送音訊

透過有效連線，以原始 16 位元 PCM 音訊串流音訊區塊。

- **音訊格式：**原始 16 位元 PCM，16kHz (單聲道，小端序)。
- **區塊大小：**以 100 毫秒 (1,024 到 2,048 影格) 為單位傳送音訊。
- **MIME 類型：** `audio/pcm;rate=16000` (或相符的取樣率)。

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSocket

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## 語音轉錄功能

### 自動偵測語言

根據預設，省略 `language_codes` 或設定 `language_codes=[]` 會啟用自動語言識別功能。模型會動態偵測語句中的口語，包括多語言對話和交替使用不同語言的情況。

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 特定語言提示

提供明確的 BCP-47 語言代碼 (例如 `["es-ES"]` 代表西班牙文，`["fr-FR"]` 代表法文)，讓系統偏向辨識特定語言 (請參閱[支援的語言](#supported-languages))。

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 自訂詞彙偏誤

在 `custom_vocabulary` 中提供最多 1,000 個詞組、專有名詞、品牌名稱或技術術語，讓語音辨識功能偏向特定術語 (通常最多 100 個術語可達到最佳效果)。

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 智慧轉錄

使用 `input_audio_transcription` 中的 `mode` 參數，設定語音轉錄輸出內容的格式：

- **`VERBATIM` (預設)**：逐字轉錄所有語音內容，保留原始填充詞 (「嗯」、「呃」、「像」)、重複內容和錯誤開頭。
- **`SMART` (智慧轉錄)**：整理轉錄稿並調整結構，提高可讀性：

  - **贅字移除**：移除填充詞、口吃和錯誤開頭。
  - **內嵌自我修正**：自然修正口誤。
  - **結構化格式**：自動設定清單、項目符號、數字、日期和段落分行格式。
  - **文法和大小寫**：自然地調整大小寫和標點符號。

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## 語音活動偵測 (VAD) 策略

### 自動 VAD (預設)

根據預設，伺服器端自動語音活動偵測功能會偵測說話者何時開始和停止說話。

### 混合式 VAD

[混合式 VAD](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-tw#hybrid-vad) 結合伺服器端自動語音開始偵測和用戶端語音結束偵測，實現零延遲的語音結束判定：

1. **伺服器端自動 VAD 仍會保持啟用**，透過前置音訊填補準確偵測語音開頭，防止前端字詞遭到截斷。
2. **用戶端 VAD 偵測到靜音**：當本機裝置端 VAD 偵測到說話者停止說話時，用戶端會立即傳送 `audio_stream_end` 信號。
3. **快速完成**：伺服器會將 `audio_stream_end` 視為立即完成對話的提示，略過預設的伺服器端靜音等待時間，並以最短的延遲時間傳回完成的轉錄稿。
4. **備用**：如果用戶端 VAD 無法觸發，伺服器端 VAD 會自動做為備用。

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### 手動 VAD (即按即說)

如果是對講機介面或即按即說按鈕，請完全停用自動 VAD，並使用 `activity_start` 和 `activity_end` 明確控制對話輪替界線：

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## 用戶端應用程式中的臨時權杖

如果是用戶端對伺服器應用程式 (例如直接從麥克風串流的行動或網頁應用程式)，請使用[臨時權杖](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-tw)，避免在用戶端程式碼中公開 API 金鑰。

在伺服器上建立受限的臨時權杖，然後再啟動用戶端連線：

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## 支援的語言

Gemini 3.5 Transcribe Live 支援下列語言和 BCP-47 語言代碼：

| 語言 | BCP-47 代碼 | 語言 | BCP-47 代碼 |
| --- | --- | --- | --- |
| 南非荷蘭文 | `af-ZA` | 日文 | `ja-JP` |
| 阿姆哈拉文 | `am-ET` | 爪哇語 | `jv-ID` |
| 阿拉伯文 (埃及) | `ar-EG` | 維德角克里奧爾文 | `kea-CV` |
| 亞美尼亞文 | `hy-AM` | 卡納達文 | `kn-IN` |
| 阿薩姆文 | `as-IN` | 哈薩克文 | `kk-KZ` |
| 亞塞拜然文 | `az-AZ` | 韓文 | `ko-KR` |
| 白俄羅斯語 | `be-BY` | 吉爾吉斯文 | `ky-KG` |
| 孟加拉文 (孟加拉) | `bn-BD` | 拉脫維亞文 | `lv-LV` |
| 孟加拉文 (印度) | `bn-IN` | 林格拉文 | `ln-CD` |
| 波士尼亞文 | `bs-BA` | 立陶宛文 | `lt-LT` |
| 保加利亞文 | `bg-BG` | 馬其頓文 | `mk-MK` |
| 保加利亞文 (阿羅馬尼亞文) | `rup-BG` | 馬來文 | `ms-MY` |
| 緬甸文 | `my-MM` | 馬拉雅拉姆文 | `ml-IN` |
| 粵語 (繁體) | `yue-Hant-HK` | 馬爾他文 | `mt-MT` |
| 加泰隆尼亞文 | `ca-ES` | 中文 (簡體) | `cmn-Hans-CN` |
| 宿霧文 | `ceb` | 馬拉地文 | `mr-IN` |
| 中部高棉文 | `km-KH` | 蒙古文 | `mn-MN` |
| 克羅埃西亞文 | `hr-HR` | 尼泊爾文 | `ne-NP` |
| 捷克文 | `cs-CZ` | 挪威文 | `nb-NO` |
| 丹麥文 | `da-DK` | 奧里雅文 | `or-IN` |
| 荷蘭文 | `nl-NL` | 波蘭文 | `pl-PL` |
| 英文 (英國) | `en-GB` | 葡萄牙文 (巴西) | `pt-BR` |
| 英文 (印度) | `en-IN` | 葡萄牙文 (葡萄牙) | `pt-PT` |
| 英文 (美國) | `en-US` | 旁遮普文 | `pa-IN` |
| 愛沙尼亞文 | `et-EE` | 旁遮普文 (古木基文) | `pa-Guru-IN` |
| 波斯文 | `fa-IR` | 羅馬尼亞文 | `ro-RO` |
| 菲律賓文 | `fil-PH` | 俄文 | `ru-RU` |
| 芬蘭文 | `fi-FI` | 塞爾維亞文 | `sr-RS` |
| 法文 | `fr-FR` | 信德文 (阿拉伯字母) | `sd-Arab-IN` |
| 加里西亞文 | `gl-ES` | 斯洛伐克文 | `sk-SK` |
| 喬治亞文 | `ka-GE` | 斯洛維尼亞文 | `sl-SI` |
| 德文 | `de-DE` | 西班牙文 (拉丁美洲) | `es-419` |
| 希臘文 | `el-GR` | 西班牙文 (美國) | `es-US` |
| 古吉拉特文 | `gu-IN` | 斯瓦希里文 (肯亞) | `sw-KE` |
| 豪薩文 | `ha-NG` | 瑞典文 | `sv-SE` |
| 希伯來文 | `he-IL` | 塔吉克文 | `tg-TJ` |
| 北印度文 | `hi-IN` | 泰盧固文 | `te-IN` |
| 匈牙利文 | `hu-HU` | 泰文 | `th-TH` |
| 冰島文 | `is-IS` | 土耳其文 | `tr-TR` |
| 印度英語 | `en-IN` | 烏克蘭文 | `uk-UA` |
| 印尼文 | `id-ID` | 烏茲別克文 | `uz-UZ` |
| 義大利文 | `it-IT` | 越南文 | `vi-VN` |

## 參數參考資料

使用 `input_audio_transcription` 和 `realtime_input_config` 中的欄位設定即時轉錄：

| 參數 | 類型 | 說明 |
| --- | --- | --- |
| `language_codes` | 字串陣列 | BCP-47 語言代碼 (例如 `["en-US"]`)。如果省略或留空 (`[]`)，模型會自動偵測語言，並處理多語言語音。 |
| `custom_vocabulary` | 字串陣列 | 最多可輸入 1,000 個自訂字詞、縮寫、品牌名稱或專有名詞，讓語音辨識功能優先辨識這些字詞。 |
| `mode` | 字串 | 語音轉錄模式：`"VERBATIM"` (預設) 或 `"SMART"` (智慧語音轉錄)。如果設為 `"SMART"`，模型會移除填充詞、設定清單格式，並修正不流暢的語句。 |
| `automatic_activity_detection.disabled` | 布林值 | 設為 `true` 即可停用自動語音活動偵測功能，並手動傳送 `activityStart` 和 `activityEnd` 信號。 |

### 伺服器回應欄位

| 欄位 | 說明 |
| --- | --- |
| `server_content.interim_input_transcription` | 使用者說話時，系統會持續產生低延遲的臨時部分轉錄假設。 |
| `server_content.input_transcription` | 語音轉換完成時，系統會發出最終的權威輸入轉錄稿。 |

## 限制

- **工作階段持續時間：**即時轉錄工作階段支援最長 10 分鐘的連續串流。
- **說話者分類：**直播工作階段不支援說話者分類功能。如要使用語者分段功能，請使用非串流[音訊轉錄](https://ai.google.dev/gemini-api/docs/transcribe?hl=zh-tw#speaker-diarization)端點。
- **字詞層級時間戳記：**Live API 不支援字詞層級時間戳記。Live API 會發出語句層級的時間戳記 (`interim_input_transcription` 和 `input_transcription`)。
- **自訂詞彙：**您最多可以在 `custom_vocabulary` 中提供 1,000 個字詞，但通常最多 100 個字詞的效果最佳。
- **模式相容性：**智慧轉錄 (`"mode": "SMART"`) 會移除填充詞，並根據意圖調整文字格式，但無法與字詞註解搭配使用。

## 後續步驟

- 請參閱 [Gemini Transcribe 說明文件](https://ai.google.dev/gemini-api/docs/transcribe?hl=zh-tw)，瞭解非串流音訊檔案。
- 參閱 [Live API 總覽](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)，瞭解對話式語音代理。
- 參閱[即時翻譯指南](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=zh-tw)，瞭解如何即時翻譯語音。
- 如要瞭解 Live API 串流定價，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-3.5-transcribe-live)。
- 請參閱 [Live API 功能指南](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-29 (世界標準時間)。"],[],[]]
