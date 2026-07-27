---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=zh-CN
fetched_at: 2026-07-27T04:49:24.411590+00:00
title: "Gemini Live API \u6982\u89c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Live API 概览

Live API 支持与 Gemini 进行低延迟、实时的语音和视觉交互。它能够处理连续的音频、图片和文本流，以提供即时、自然逼真的语音回答，从而为用户打造自然的对话体验。

![Live API 概览](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=zh-cn)

[在 Google AI Studio 中试用 Live APImic](https://aistudio.google.com/live?hl=zh-cn)
[从 GitHub 克隆示例应用code](https://github.com/google-gemini/gemini-live-api-examples)
[使用编码代理技能terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn)

## 使用场景

Live API 可用于为各种行业构建实时语音代理，包括：

- **电子商务和零售**：提供个性化推荐的购物助理，以及解决客户问题的支持人员。
- **游戏**：互动式非玩家角色 (NPC)、游戏内帮助助理和游戏内内容的实时翻译。
- **新一代界面**：在机器人、智能眼镜和车辆中提供语音和视频功能。
- **医疗保健**：用于患者支持和教育的健康助手。
- **金融服务**：用于财富管理和投资指导的 AI 顾问。
- **教育**：提供个性化指导和反馈的 AI 导师和学习伙伴。
- **翻译和本地化**：实时、低延迟地翻译语音对话，实现顺畅的多语言交流。

## 主要特性

Live API 提供了一套全面的功能，用于构建强大的语音代理：

- [**多语言支持**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#supported-languages)：支持用 70 种语言进行对话。
- [**打断功能**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#interruptions)：用户可以随时中断模型，以便进行响应式互动。
- [**工具使用**](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn)：集成函数调用和 Google 搜索等工具，实现动态交互。
- [**音频转写**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#audio-transcription)：提供用户输入和模型输出的文本转写内容。
- [**主动音频**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#proactive-audio)：可让您控制模型何时响应以及在哪些情境下响应。
- [**共情对话**](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#affective-dialog)：根据用户输入内容的情绪表达调整回答风格和语气。
- [**实时翻译**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=zh-cn)：支持 70 多种语言的实时语音翻译。

## 技术规范

下表列出了 Live API 的技术规范：

| 类别 | 详细信息 |
| --- | --- |
| 输入模态 | 音频（原始 16 位 PCM 音频，16kHz，小端序）、图片（JPEG <= 1FPS）、文本 |
| 输出模态 | 音频（原始 16 位 PCM 音频，24kHz，小端序） |
| 协议 | 有状态 WebSocket 连接 (WSS) |

## 选择一种实现方法

与 Live API 集成时，您需要选择以下实现方法之一：

- **服务器到服务器**：您的后端使用 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 连接到 Live API。通常，您的客户端会将流数据（音频、视频、文本）发送到您的服务器，然后由服务器将其转发到 Live API。
- **客户端到服务器**：您的前端代码使用 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 直接连接到 Live API 以流式传输数据，从而绕过后端。

## 开始使用

选择与您的开发环境相符的指南：

服务器到服务器

### [GenAI SDK 教程](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-cn)

使用 GenAI SDK 连接到 Gemini Live API，以构建具有 Python 后端的实时多模态应用。

客户端到服务器

### [WebSocket 教程](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=zh-cn)

使用 WebSockets 连接到 Gemini Live API，以构建一个具有 JavaScript 前端和临时令牌的实时多模态应用。

智能体开发套件

### [ADK 教程](https://google.github.io/adk-docs/streaming/)

创建代理，并使用智能体开发套件 (ADK) 流式传输功能来实现语音和视频通信。

## 合作伙伴集成

为了简化实时音频和视频应用的开发，您可以使用通过 WebRTC 或 WebSockets 支持 Gemini Live API 的第三方集成。

[LiveKit

将 Gemini Live API 与 LiveKit 智能体搭配使用。](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

使用 Gemini Live 和 Pipecat 创建实时 AI 聊天机器人。](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion 的 Fishjam

使用 Fishjam 创建实时视频和音频流式传输应用。](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Stream 的 Vision Agent

使用 Vision Agent 构建实时语音和视频 AI 应用。](https://visionagents.ai/integrations/gemini)
[Voximplant

通过 Voximplant 将入站和出站通话连接到 Live API。](https://voximplant.com/products/gemini-client)
[Agora

使用 Agora 构建实时对话式 AI 应用。](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

使用 Firebase AI Logic 开始使用 Gemini Live API。](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-12。"],[],[]]
