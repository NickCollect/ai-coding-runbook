---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=zh-CN
fetched_at: 2026-10-19T05:58:19.450136+00:00
title: "\u4f7f\u7528 Gemini Live API \u8fdb\u884c\u5b9e\u65f6\u7ffb\u8bd1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini Live API 进行实时翻译

Gemini Live API 支持使用 [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=zh-cn) 模型在 70 多种语言之间进行低延迟的实时语音翻译。通过使用翻译设置配置 Live API，您可以以一种语言流式传输音频，并以另一种语言接收翻译后的音频输出，从而实现无缝的实时语音翻译。

[在 Google AI Studio 中试用实时翻译mic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=zh-cn)
[从 GitHub 克隆示例应用code](https://github.com/google-gemini/gemini-live-api-examples)
[使用编码代理技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn#gemini-live-api-dev)

## 人工客服与实时翻译

虽然两者都使用 Live API，但实时翻译的心理模型与对话式实时代理互动不同。

| 人工客服 | 实时翻译 |
| --- | --- |
| **模型充当助理。**它会倾听、推理并代表您采取行动。 | **模型充当翻译。**它的行为类似于实时翻译管道。 |
| **使用基于轮流的互动。**依赖于暂停、意图检测和处理中断。 | **使用连续流处理。**在说话者说话时进行翻译，无需等待轮流。 |
| **支持工具和代理。**原生支持函数调用、Google 搜索和说明。 | **仅支持翻译。**纯低延迟翻译；不支持工具或说明。 |
| **完全多模态。**支持文本、音频、视频和图片输入。 | **音频受限。**输入仅限于音频，以确保严格的实时延迟阈值。 |
| **精细配置。**使用生成、语音、工具和系统说明。 | **简化配置。**设置 `target_language_code` 和 `echo_target_language` 等切换开关。 |

## 开始使用

以下示例演示了如何初始化客户端并使用翻译配置连接到 Live API。

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

### WebSockets

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

## 发送音频

如需流式传输语音输入以进行翻译，请发送原始的小端序 16 位 PCM 音频。

- **输入音频格式**：原始 16 位 PCM，采样率 16kHz（单声道，小端序）。
- **输出音频格式**：原始 16 位 PCM，采样率 24kHz（单声道，小端序）。
- **块大小和延迟时间**：以 100 毫秒的块发送音频。

以下示例展示了如何向会话发送音频块。

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

### WebSockets

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

## 配置

如需启用翻译，您必须在会话设置期间在 `generationConfig` 中指定 `translationConfig`。

### 设置消息配置

`generationConfig` 支持以下字段以启用转录：

- **`inputAudioTranscription`**：一个对象，如果存在，则允许模型发送输入音频的文本转录。
- **`outputAudioTranscription`**：一个对象，如果存在，则允许模型发送输出（翻译后的）音频的文本转录。

`translationConfig` 支持以下字段：

- **`targetLanguageCode`**：您希望模型翻译成的语言的 [BCP-47 语言代码](#supported-languages)（例如，波兰语为 `"pl"`，西班牙语为 `"es"`）。默认值为 `"en"`。
- **`echoTargetLanguage`**：一个布尔值，用于指示应如何处理已采用目标语言的输入音频。如果设置为 `true`，模型将回显（鹦鹉学舌）已采用目标语言的输入音频。如果设置为 `false`，当输入语音已采用目标语言时，模型将保持静默。默认值为 `false`。

以下是设置消息结构的示例：

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

## 在客户端应用中使用临时令牌

对于客户端到服务器的应用，您可以使用 [临时令牌](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-cn)（目前为 `v1beta`）来避免公开您的 API 密钥。

将临时令牌与实时翻译搭配使用时：

1. 您必须使用 `v1beta` 端点。
2. **锁定配置** ：默认情况下，您应在服务器上的令牌创建限制条件中指定 `translationConfig`。这样可确保翻译配置被锁定，并且客户端无法篡改。
3. **解锁配置**：如果您希望能够在客户端设置 `translationConfig`（例如，让用户选择自己的目标语言），则必须从令牌创建请求中省略该配置，并改为设置 `"lock_additional_fields": []`。这样会解锁 `translationConfig` 以在客户端设置。

### 创建受限的临时令牌

以下示例演示了如何创建具有翻译限制条件的临时令牌。

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

- **输入模态**：翻译仅支持音频输入。不支持文本输入。
- **语音复制**：语音复制可能不一致。语音可能会在长时间暂停后发生变化，根据语音的开头分配错误的性别，或者在快速的多说话者对话期间停留在一种语音上。
- **语言检测**：语言检测难以处理重口音、相似语言（例如西班牙语与葡萄牙语）或快速语言切换。**注意** ：这只会影响输入转录。语言代码和最终翻译仍应准确无误。
- **背景音频**：该模型旨在过滤掉噪声和音乐以生成清晰的语音，但并非所有背景音频都可能会被忽略。
- **回显目标语言**：当 `echoTargetLanguage: true` 时，如果输入音频已采用目标语言，背景噪声或音乐可能会在翻译后的音频中引入伪影。

## 支持的语言

实时翻译支持以下语言。

| 语言 | BCP-47 代码 | 语言 | BCP-47 代码 |
| --- | --- | --- | --- |
| 南非荷兰语 | af | 哈萨克语 | kk |
| Akan | ak | 高棉语 | km |
| 阿尔巴尼亚语 | sq | 卢旺达语 | rw |
| 阿姆哈拉语 | am | 韩语 | ko |
| 阿拉伯语 | ar | 老挝语 | lo |
| 亚美尼亚语 | hy | 拉脱维亚语 | lv |
| 阿塞拜疆语 | az | 立陶宛语 | lt |
| 巴斯克语 | eu | 马其顿语 | mk |
| 白俄罗斯语 | be | 马来语 | ms |
| 孟加拉语 | bn | 马拉雅拉姆语 | ml |
| 保加利亚语 | bg | 马拉地语 | mr |
| 缅甸语（缅甸） | my | 蒙古语 | mn |
| 加泰罗尼亚语 | ca | 尼泊尔语 | ne |
| 中文（简体） | zh-Hans | 挪威语 | no、nb |
| 繁体中文 (台湾) | zh-Hant | 波斯语 | fa |
| 克罗地亚语 | hr | 波兰语 | pl |
| 捷克语 | cs | 葡萄牙语（巴西） | pt-BR |
| 丹麦语 | da | 葡萄牙语（葡萄牙） | pt-PT |
| 荷兰语 | nl | 旁遮普语 | pa |
| 英语 | en | 罗马尼亚语 | ro |
| 爱沙尼亚语 | et | 俄语 | ru |
| 菲律宾语 | fil | 塞尔维亚语 | sr |
| 芬兰语 | fi | 信德语 | sd |
| 法语 | fr | 僧伽罗语 | si |
| 加利西亚语 | gl | 斯洛伐克语 | sk |
| 格鲁吉亚语 | ka | 斯洛文尼亚语 | sl |
| 德语 | de | 西班牙语 | es |
| 希腊语 | el | 巽他语 | su |
| 古吉拉特语 | gu | 斯瓦希里语 | sw |
| 豪萨语 | ha | 瑞典语 | sv |
| 希伯来语 | he | 泰米尔语 | ta |
| 印地语 | hi | 泰卢固语 | te |
| 匈牙利语 | hu | 泰语 | th |
| 冰岛语 | is | 土耳其语 | tr |
| 印度尼西亚语 | id | 乌克兰语 | uk |
| 意大利语 | it | 乌尔都语 | ur |
| 日语 | ja | 乌兹别克语 | uz |
| 爪哇语 | jv | 越南语 | vi |
| 卡纳达语 | kn | 祖鲁语 | zu |

## 后续步骤

- 阅读完整的 Live API [功能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-cn)指南。
- 阅读 [SDK 使用入门](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-cn) 指南。
- 阅读 [WebSocket 使用入门](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-cn) 指南。
- 阅读[临时令牌](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-cn)指南，了解如何在客户端到服务器的应用中进行安全身份验证。
- 从 GitHub 克隆 [Live API 示例](https://github.com/google-gemini/gemini-live-api-examples)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-23。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-23。"],[],[]]
