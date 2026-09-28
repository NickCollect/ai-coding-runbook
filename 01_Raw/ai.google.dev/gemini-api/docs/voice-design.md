---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=zh-TW
fetched_at: 2026-09-28T06:26:20.012996+00:00
title: "\u8a9e\u97f3\u8a2d\u8a08 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 語音設計

語音設計功能可讓您使用 Gemini API Voices 端點 (`POST /v1beta/voices`)，根據自然語言描述建立全新的永久語音角色。您不必受限於預先建構的語音或錄製參考音訊，而是可以描述角色的年齡、音色、口音和基本發音方式，並取得可重複使用的 `voice_...` ID，儲存至專案中。

如要快速設計、試聽及反覆調整自訂語音，請使用 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=zh-tw) 中的互動式**語音設計**工作室。您可以透過文字提示詞生成自訂角色、使用範例指令碼測試角色，並直接將產生的 `voice_...` ID 複製到應用程式程式碼中。

[在 Google AI Studio 中試用](https://aistudio.google.com/generate-speech?hl=zh-tw)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-tw) (`gemini-3.8-flash-tts`) 和 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-tw) (`gemini-3.8-flash-lite-tts`) 皆支援語音設計。

## 建立設計的聲音

使用 Google GenAI SDK (`google-genai` 2.25.0 以上版本 / `@google/genai` 2.24.0 以上版本) 或 REST API，根據文字說明建立自訂語音。對於 `"prompted"` 語音，`voices.create` (`CreateVoice`) 和 `voices.get` (`GetVoice`) 都會傳回僅供輸出的 `sample_audio` 欄位 (`mime_type: "audio/wav"`，採用 Base64 編碼的 `data`)，因此您可以立即試聽生成的語音：

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## 語音設計的運作方式

1. **建立提示語音：**呼叫 `voices.create` (`POST /v1beta/voices`)
   搭配 `type="prompted"` 和 `store=True`。
2. **接收永久 `voice_id` 和 `sample_audio` 預覽：**API 會生成聲音身分，並將其儲存在專案中，然後傳回永久 ID (例如 `voice_abc123...`) 和 `sample_audio` (`mime_type: "audio/wav"`，以 Base64 編碼的 `data`)，其中包含生成的聲音預覽音訊。
3. **合成語音：**在合成要求中，將 `voice_id` 傳遞至接受語音名稱的任何位置。

## 以設計的聲音合成語音

建立語音後，請將其 `id` (`voice_...`) 傳遞至 Interactions API，以生成語音：

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
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## 管理語音

您隨時可以使用 Voices API 列出、篩選、檢查及刪除儲存的聲音 (如需所有篩選器參數，請參閱「[擴充語音庫和篩選](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw#voice-library)」)。

- **儲存空間限制和存留時間：**有狀態語音 (`store=True`，在提示和複製語音之間共用) 的限制為**每個專案 200 個語音**，且**存留時間為 1 年**。
- **`sample_audio` 支援情形：** `voices.create()` (`CreateVoice`) 和 `voices.get()` (`GetVoice`) 會為 `"prompted"` 語音填入 `sample_audio` (`mime_type:
  "audio/wav"`，採用 Base64 編碼的 `data`)。為保持產品資訊輕量化，`voices.list()` (`ListVoices`) 會省略 `sample_audio` (且 `sample_audio` 會針對 `"replicated"` 和 `"prebuilt"` 語音取消設定)。

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 語音設計的提示最佳做法

- **將永久性聲音特徵放在 Voice 設計中，而非 `style`：**在 `voices.create` 中建立語音時，定義不可變更的特徵，例如年齡、性別、音色、音質和地域口音。
- **保留 `speech_metadata.style`，用於表達情緒：**建立自訂聲音後，使用簡短的 `style` 提示 (例如 `"whispered urgently"` 或 `"cheerful and energetic"`) 逐步引導演出，同時保留說話者的核心特徵。
- **具體簡潔：**清楚的 1 至 2 句描述 (例如「30 多歲的體育播報員，聲音清脆有活力，帶有中西部口音」) 比矛盾或過長的段落，更能產生清晰一致的結果。

## 後續步驟

- 瞭解如何使用[語音複製](https://ai.google.dev/gemini-api/docs/voice-replication?hl=zh-tw)功能，複製現有音箱的聲音。
- 如要瞭解回合層級樣式、內嵌標記和多說話者對話，請參閱[文字轉語音指南](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-24 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-24 (世界標準時間)。"],[],[]]
