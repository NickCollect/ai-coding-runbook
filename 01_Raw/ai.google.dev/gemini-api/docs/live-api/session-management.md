---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-CN
fetched_at: 2026-09-21T05:50:27.386884+00:00
title: "\u4f7f\u7528 Live API \u8fdb\u884c\u4f1a\u8bdd\u7ba1\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Live API 进行会话管理

在 Live API 中，会话是指通过同一连接持续流式传输输入和输出的持久
连接（详细了解[其工作原理](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)）。
这种独特的会话设计可实现低延迟并支持独特的功能，但也可能会带来一些挑战，例如会话时间限制和提前终止。
本指南介绍了克服使用 Live API 时可能出现的会话管理挑战的策略。

## 会话生命周期

如果不进行压缩，仅限音频的会话时长上限为 15 分钟，音频-视频会话时长上限为 2 分钟。超出这些限制
将会终止会话（以及连接），但您可以使用
[上下文窗口压缩](#context-window-compression)将会话时长延长至
无限。

连接的生命周期也有限制，约为 10 分钟。连接终止时，会话也会终止。在这种情况下，您可以使用
[会话恢复](#session-resumption)功能将单个会话配置为在多个连接中保持活跃状态。
您还会在连接结束前收到 [GoAway 消息](#goaway-message)，以便采取进一步的操作。

## 上下文窗口压缩

如需延长会话时长并避免连接突然终止，您可以
在会话配置中设置 [contextWindowCompression](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
字段，以启用上下文窗口压缩。

在 [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=zh-cn#contextwindowcompressionconfig) 中，您可以配置
[滑动窗口机制](https://ai.google.dev/api/live?hl=zh-cn#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
和[触发压缩的令牌数量](https://ai.google.dev/api/live?hl=zh-cn#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
。

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## 会话恢复

如需防止服务器定期重置 WebSocket
连接时会话终止，请在 [设置配置](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentSetup)中配置 [sessionResumption](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
字段。

传递此配置会导致服务器发送 [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=zh-cn#SessionResumptionUpdate) 消息，您可以通过将上次恢复令牌作为后续连接的 [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=zh-cn#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) 传递来恢复会话。

恢复令牌在上次会话终止后 2 小时内有效。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## 在会话断开连接之前接收消息

服务器会发送 [GoAway](https://ai.google.dev/api/live?hl=zh-cn#GoAway) 消息，表明当前
连接即将终止。此消息包含 [timeLeft](https://ai.google.dev/api/live?hl=zh-cn#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left)，
表示剩余时间，让您可以在
连接终止为 ABORTED 之前采取进一步的操作。

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## 在生成完成后接收消息

服务器会发送 [generationComplete](https://ai.google.dev/api/live?hl=zh-cn#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
消息，表明模型已完成生成响应。

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## 后续步骤

如需了解更多使用 Live API 的方法，请参阅完整
[的功能](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)指南、
工具[使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn)页面或
[Live API 食谱](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-17。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-17。"],[],[]]
