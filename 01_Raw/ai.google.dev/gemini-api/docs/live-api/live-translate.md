---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=zh-TW
fetched_at: 2026-09-21T05:57:48.383765+00:00
title: "\u4f7f\u7528 Gemini Live API \u9032\u884c\u5373\u6642\u7ffb\u8b6f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini Live API 進行即時翻譯

Gemini Live API 支援 70 多種語言的低延遲即時語音翻譯，使用的模型為 [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=zh-tw)。設定 Live API 的翻譯設定後，您就能以一種語言串流音訊，並以另一種語言接收翻譯後的音訊輸出內容，實現流暢的即時語音翻譯。

[在 Google AI Studio 中試用即時翻譯mic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=zh-tw)
[從 GitHub 複製範例應用程式code](https://github.com/google-gemini/gemini-live-api-examples)
[使用程式碼編寫代理程式技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw#gemini-live-api-dev)

## 真人服務專員與即時翻譯

兩者都使用 Live API，但即時翻譯的心智模型與對話式即時服務專員互動不同。

| 線上服務專員 | 即時翻譯 |
| --- | --- |
| **模型會扮演助理的角色。**並聽從您的指示採取行動。 | **模型會擔任口譯員。**這項功能會以即時翻譯管道的形式運作。 |
| **使用回合制互動。**依賴暫停、意圖偵測和處理中斷。 | **使用連續串流處理。**在講者說話時即時翻譯，不必等待輪流發言。 |
| **支援工具和代理程式。**原生支援函式呼叫、Google 搜尋和指令。 | **僅支援翻譯。**純粹的低延遲翻譯，不支援工具或指令。 |
| **完全支援多模態。**支援文字、音訊、影片和圖片輸入內容。 | **音訊受限。**為確保嚴格的即時延遲時間門檻，輸入內容僅限音訊。 |
| **精細設定。**使用生成、語音、工具和系統指令。 | **簡化設定程序。**設定 `target_language_code` 和切換鈕，例如 `echo_target_language`。 |

## 開始使用

以下範例說明如何初始化用戶端，並透過翻譯設定連線至 Live API。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSocket

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## 正在傳送音訊

如要串流語音輸入內容以進行翻譯，請傳送原始的小端序 16 位元 PCM 音訊。

- **輸入音訊格式**：16 kHz 的原始 16 位元 PCM (單聲道，小端序)。
- **輸出音訊格式**：24 kHz 的原始 16 位元 PCM (單聲道，小端序)。
- **區塊大小和延遲時間**：以 100 毫秒的區塊傳送音訊。

下列範例說明如何將音訊區塊傳送至工作階段。

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

### WebSocket

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## 設定

如要啟用翻譯功能，您必須在工作階段設定期間，於 `generationConfig` 中指定 `translationConfig`。

### 設定訊息設定

`generationConfig` 支援下列欄位來啟用轉錄稿：

- **`inputAudioTranscription`**：這個物件 (如有) 可讓模型傳送輸入音訊的文字轉錄稿。
- **`outputAudioTranscription`**：如果存在這個物件，模型就能傳送輸出 (翻譯) 音訊的文字轉錄稿。

`translationConfig` 支援下列欄位：

- **`targetLanguageCode`**：模型要翻譯成的語言的 [BCP-47 語言代碼](#supported-languages) (例如波蘭文為 `"pl"`，西班牙文為 `"es"`)。預設為 `"en"`。
- **`echoTargetLanguage`**：布林值，指出如何處理已為目標語言的輸入音訊。如果設為 `true`，模型會以目標語言回應輸入音訊。如果設為 `false`，當輸入的語音已是目標語言時，模型會保持靜音。預設為 `false`。

以下是設定訊息結構的範例：

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## 在用戶端應用程式中使用臨時權杖

對於用戶端對伺服器應用程式，您可以使用[臨時權杖](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-tw) (目前為 `v1beta` 版)，避免公開 API 金鑰。

使用即時翻譯功能時，如果採用臨時權杖：

1. 您必須使用 `v1beta` 端點。
2. **鎖定設定：**根據預設，您應在伺服器上的權杖建立限制中指定 `translationConfig`。這可確保翻譯設定已鎖定，且用戶端無法竄改。
3. **解除設定：**如要在用戶端設定 `translationConfig` (例如讓使用者選擇目標語言)，您必須從權杖建立要求中省略這項設定，並改為設定 `"lock_additional_fields": []`。這樣一來，用戶端就能設定 `translationConfig`。

### 建立受限的暫時權杖

下列範例說明如何建立具有翻譯限制的臨時權杖。

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
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
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## 限制

- **輸入模式**：翻譯功能僅支援音訊輸入。不支援文字輸入。
- **語音複製**：複製的語音可能不一致。長時間暫停後，聲音可能會改變；根據語音的開頭方式，系統可能會指派錯誤的性別；在多位講者快速對話時，系統可能會卡在一個聲音。
- **語言偵測**：語言偵測功能難以辨識口音很重、相似的語言 (例如西班牙文和葡萄牙文)，或是快速切換的語言。**注意：**這項操作只會影響輸入內容的轉錄稿，語言代碼和最終翻譯內容仍應正確無誤。
- **背景音訊**：模型會濾除噪音和音樂，產生乾淨的語音，但可能無法忽略所有背景音訊。
- **Echo Target Language**：如果輸入音訊已是目標語言，`echoTargetLanguage: true`、背景噪音或音樂可能會在翻譯音訊中產生失真。

## 支援的語言

即時翻譯功能支援下列語言。

| 語言 | BCP-47 代碼 | 語言 | BCP-47 代碼 |
| --- | --- | --- | --- |
| 南非荷蘭文 | af | 哈薩克文 | kk |
| 阿肯文 | ak | 高棉文 | 公里 |
| 阿爾巴尼亞文 | sq | 盧旺達文 | rw |
| 阿姆哈拉文 | am | 韓文 | ko |
| 阿拉伯文 | ar | 寮文 | lo |
| 亞美尼亞文 | hy | 拉脫維亞文 | lv |
| 亞塞拜然文 | az | 立陶宛文 | lt |
| 巴斯克文 | eu | 馬其頓文 | mk |
| 白俄羅斯語 | be | 馬來文 | 毫秒 |
| 孟加拉文 | bn | 馬拉雅拉姆文 | ml |
| 保加利亞文 | bg | 馬拉地文 | mr |
| 緬甸文 (緬甸) | my | 蒙古文 | mn |
| 加泰隆尼亞文 | ca | 尼泊爾文 | ne |
| 中文 (簡體) | zh-Hans | 挪威文 | no, nb |
| 繁體中文 (台灣) | zh-Hant | 波斯文 | fa |
| 克羅埃西亞文 | 時 | 波蘭文 | pl |
| 捷克文 | cs | 葡萄牙文 (巴西) | pt-BR |
| 丹麥文 | da | 葡萄牙文 (葡萄牙) | pt-PT |
| 荷蘭語 | nl | 旁遮普文 | pa |
| 英語 | en | 羅馬尼亞文 | ro |
| 愛沙尼亞文 | et | 俄語 | ru |
| 菲律賓文 | fil | 塞爾維亞文 | sr |
| 芬蘭文 | fi | 信德文 | sd |
| 法文 | fr | 錫蘭文 | si |
| 加里西亞文 | gl | 斯洛伐克文 | sk |
| 喬治亞文 | ka | 斯洛維尼亞文 | sl |
| 德文 | de | 西班牙語 | es |
| 希臘文 | el | 巽他文 | su |
| 古吉拉特文 | gu | 史瓦西里文 | sw |
| 豪薩文 | ha | 瑞典文 | sv |
| 希伯來文 | 他 | 泰米爾文 | ta |
| 北印度文 | hi | 泰盧固文 | te |
| 匈牙利文 | hu | 泰文 | th |
| 冰島文 | 為 | 土耳其文 | tr |
| 印尼文 | id | 烏克蘭文 | uk |
| 義大利文 | it | 烏都語 | ur |
| 日文 | ja | 烏茲別克文 | uz |
| 爪哇語 | jv | 越南語 | vi |
| 卡納達文 | kn | 祖魯文 | zu |

## 後續步驟

- 請參閱完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-tw)指南。
- 請參閱「[開始使用 SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-tw)」指南。
- 請參閱「[開始使用 WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-tw)」指南。
- 如要在用戶端對伺服器應用程式中進行安全驗證，請參閱「[暫時性權杖](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-tw)」指南。
- 從 GitHub 複製 [Live API examples](https://github.com/google-gemini/gemini-live-api-examples)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-23 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-23 (世界標準時間)。"],[],[]]
