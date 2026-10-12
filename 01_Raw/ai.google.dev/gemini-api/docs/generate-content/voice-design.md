---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=zh-CN
fetched_at: 2026-10-12T06:52:52.657310+00:00
title: "\u8bed\u97f3\u8bbe\u8ba1 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 语音设计

借助语音设计，您可以使用 Gemini API Voices 端点 (`POST /v1beta/voices`) 通过自然语言描述来创建全新的持久性声音角色。您无需局限于预建的语音或录制参考音频，只需描述角色的年龄、音色、口音和基准发音，即可获得保存到项目中的可重复使用的 `voice_...` ID。

在 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=zh-cn) 中使用交互式**语音设计**工作室，可以快速设计、试听和迭代自定义语音。您可以根据文本提示生成自定义角色，使用示例脚本对其进行测试，然后将生成的 `voice_...` ID 直接复制到应用代码中。

[在 Google AI Studio 中试用](https://aistudio.google.com/generate-speech?hl=zh-cn)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-cn) (`gemini-3.8-flash-tts`) 和 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=zh-cn) (`gemini-3.8-flash-lite-tts`) 均支持语音设计。

## 创建设计的语音

使用 Google GenAI SDK（`google-genai` 2.25.0+ / `@google/genai` 2.24.0+）或 REST API，根据文本说明创建自定义语音。对于 `"prompted"` 语音，`voices.create` (`CreateVoice`) 和 `voices.get` (`GetVoice`) 都会返回仅输出的 `sample_audio` 字段（`mime_type: "audio/wav"`，以 base64 编码的 `data`），以便您可以立即试听生成的语音：

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

## 语音设计的工作原理

1. **创建提示语音**：使用 `type="prompted"` 和 `store=True` 调用 `voices.create` (`POST /v1beta/voices`)。
2. **接收持久性 `voice_id` 和 `sample_audio` 预览**：API 会生成声音身份，将其存储在您的项目中，并返回永久性 ID（例如 `voice_abc123...`）以及 `sample_audio`（`mime_type: "audio/wav"`，base64 编码的 `data`），其中包含为该声音生成的预览音频。
3. **合成语音**：调用 `generateContent` 时，传入 `speechConfig.voiceConfig.voice` 中的 `voice_id`。

## 使用您设计的语音合成语音

在调用 `generateContent` 时，传入 `voiceConfig.voice` 中返回的 `id` (`voice_...`)：

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## 管理声音

您可以随时使用 Voices API 列出、过滤、检查和删除已存储的声音（有关所有过滤参数，请参阅[扩展语音库和过滤](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-cn#voice-library)）。

- **存储空间限制和 TTL**：有状态的声音（`store=True`，在提示的声音和复制的声音之间共享）的限制为**每个项目 200 个声音**，并且**存留时间 (TTL) 为 1 年**。
- **`sample_audio` 可用性**： `voices.create()` (`CreateVoice`) 和 `voices.get()` (`GetVoice`) 会为 `"prompted"` 语音填充 `sample_audio`（`mime_type:
  "audio/wav"`，base64 编码的 `data`）。为了保持列表的轻量级，`voices.list()` (`ListVoices`) 会省略 `sample_audio`（对于 `"replicated"` 和 `"prebuilt"` 语音，`sample_audio` 未设置）。

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

## 语音设计的提示最佳实践

- **将永久性声音特征放在 Voice 设计中，而不是 `style` 中**：在 `voices.create` 中创建声音时，定义不可变的特征，例如年龄、性别、音色、声音质感和地区口音。
- **预留 `speech_metadata.style` 用于表达情境情绪**：创建自定义声音后，使用简短的 `style` 提示（例如 `"whispered urgently"` 或 `"cheerful and energetic"`）来引导逐轮表演，而不会改变说话者的核心身份。
- **内容要具体且简洁**：清晰的 1-2 句话描述（例如*“一位 30 多岁的体育播报员，声音清脆有力，略带中西部口音”*）比矛盾或过长的段落能生成更清晰、更一致的结果。

## 后续步骤

- 了解如何在[语音复刻](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=zh-cn)中复刻现有说话者的声音。
- 如需了解回合级样式、内嵌标记和多发言人对话，请参阅[文字转语音指南](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-24。"],[],[]]
