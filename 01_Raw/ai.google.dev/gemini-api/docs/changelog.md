---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=zh-CN
fetched_at: 2026-07-27T04:42:21.658554+00:00
title: "\u7248\u672c\u8bf4\u660e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 版本说明

本页面记录了 Gemini API 的更新。

## 2026 年 7 月 6 日

- 为 Interactions API 提供[开发者日志](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)支持：现在可以在 [AI Studio 信息中心](https://aistudio.google.com/logs?hl=zh-cn)中查看受支持的 Interactions API 调用的日志。

## 2026 年 6 月 30 日

- **Gemini Omni Flash（公开预览版）**：于 `gemini-omni-flash-preview` 发布，是一款高性能多模态模型，旨在实现高速视频生成和对话式视频编辑。借助 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn)，您可以根据文本说明生成 3-10 秒的 720p 视频，或为静态图片添加动画效果，然后以对话方式编辑和优化输出内容。如需开始使用，请参阅 [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=zh-cn) 指南和 [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=zh-cn) 模型卡片。
- 发布了 `gemini-3.1-flash-lite-image`（Nano Banana 2 Lite），这是我们内置的多模态模型，经过优化，可实现超低延迟和经济高效的图片生成和编辑。请参阅 [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=zh-cn) 模型卡片和[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)指南。

## 2026 年 6 月 24 日

- **电脑使用**：在 Gemini 3.5 Flash 中推出了[电脑使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)工具的公开预览版支持。此版本包含基于 intent 的简化操作、对浏览器、移动设备和桌面环境的内置支持、可配置的安全政策，以及高级提示注入检测功能。

## 2026 年 6 月 17 日

- **支持语音生成的流式传输**：现在支持通过 `streamGenerateContent`（以及 Interactions API 中的 `stream: true`）为 `gemini-3.1-flash-tts-preview` 模型进行流式传输。如需了解详情，请参阅[文字转语音](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn#streaming)指南。

## 2026 年 6 月 15 日

- **弃用公告**：以下图片生成模型正在被弃用，并将于 **2026 年 8 月 17 日**[关闭](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - **Imagen 4 和 Gemini 3 Image 模型**：

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    如需将代码迁移到更新的稳定版或预览版端点，请参阅 [Gemini 弃用](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn#imagen-models)页面。
- **弃用公告**：以下视频生成模型即将被弃用，并将于 **2026 年 6 月 30 日**[关闭](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - **Veo 型号**：

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    请更新您的集成，以使用 Veo 3.1 预览版模型 ID（`veo-3.1-generate-preview`、`veo-3.1-fast-generate-preview`）或通过 [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=zh-cn) 提供的 3.1 正式版模型，以免服务中断。
- **弃用公告**：实验性 GMP 上下文视图工具（用于“依托 Google 地图进行接地”输出的固定界面）将于 **2026 年 6 月 15 日**[关闭](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

## 2026 年 6 月 1 日

- 以下 Gemini 2.0 模型现已[关闭](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  请改用 [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) 或 [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn)。

## 2026 年 5 月 28 日

- 我们发布了 `gemini-3.1-flash-image` (Nano Banana 2) 和 `gemini-3-pro-image` (Nano Banana Pro)，这是我们原生视觉模型 [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=zh-cn) 和 [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=zh-cn) 的正式版 (GA)。
- **支持视频转图片生成**：您现在可以传递视频文件（通过直接上传或作为公开的 YouTube 网址），将其作为多模态上下文与文本提示一起使用，以生成优质的缩略图、电影级海报或摘要信息图表。此功能仅在 `gemini-3.1-flash-image` 型号上受支持。如需了解详情，请参阅[视频转图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn#video-to-image)指南。
- 弃用公告：`gemini-3.1-flash-image-preview` 和 `gemini-3-pro-image-preview` 模型已弃用，并将于 2026 年 6 月 25 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 5 月 25 日

- `gemini-3.1-flash-lite-preview` 模型已[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。请改用 [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn)。

## 2026 年 5 月 19 日

- `gemini-3.5-flash`发布了 [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) 的正式版 (GA)，这是我们最智能的模型，可在智能体和编码任务中持续提供前沿性能。现在，`gemini-flash-latest` 背后的模型是这个。
- 发布了 **Gemini API 中的托管式智能体**，并进入公开预览阶段。这样一来，开发者便可构建和部署在安全、隔离的 Google 托管式 Linux 沙盒环境中运行的自主有状态智能体。如需了解详情，请参阅[代理概览](https://ai.google.dev/gemini-api/docs/agents?hl=zh-cn)页面和[快速入门](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-cn)。
- 发布了通用 **Antigravity Agent** 受管代理 [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=zh-cn)，目前处于公开预览版阶段。
  Antigravity 智能体可以在其沙盒容器内自主规划、推理、编写和执行代码、管理文件以及浏览网页。如需查看代码示例和规范，请参阅 [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn) 指南。

## 2026 年 5 月 7 日

- 发布了 `gemini-3.1-flash-lite`，即 [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) 的正式版 (GA)，该模型在速度、规模和成本效益方面进行了优化。
- 弃用公告：`gemini-3.1-flash-lite-preview` 模型将于 2026 年 5 月 11 日弃用，并于 2026 年 5 月 25 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 5 月 6 日

- **即将发生的重大变更**：[互动 API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 请求和响应架构（`outputs` → `steps`）以及输出格式配置 (`response_format`) 即将发生变更。新架构将于 **5 月 26 日**成为默认架构，旧版架构将于 **6 月 8 日**移除。
  如需了解详情，请参阅[迁移指南](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn)。

## 2026 年 5 月 5 日

- 更新了**文件搜索**，以支持多模态搜索。您现在可以使用 `gemini-embedding-2` 模型以原生方式嵌入和搜索图片。接地元数据现在包含 `media_id`（用于视觉引用）和 `page_numbers`（用于指示信息来源）。如需了解详情，请参阅[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)指南。

## 2026 年 5 月 4 日

- 在 Gemini API 中推出了事件驱动型 [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-cn) 支持，以取代 Batch API 和长时间运行的操作的轮询工作流。

## 2026 年 4 月 30 日

- `gemini-robotics-er-1.5-preview` 模型已[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。请改用 [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=zh-cn)。

## 2026 年 4 月 22 日

- 已正式发布 (GA) `gemini-embedding-2`。如需了解详情，请参阅[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)页面。

## 2026 年 4 月 21 日

- 发布了新版[深度研究](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn)代理，其中包含协作规划、可视化支持、MCP 服务器集成和文件搜索功能：

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=zh-cn)：专为速度和效率而设计，非常适合流式传输回客户端界面。
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=zh-cn)：自动收集和合成上下文的最大全面性。

## 2026 年 4 月 15 日

- 推出了 [Gemini 3.1 Flash TTS 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=zh-cn)，这是一款经济实惠、富有表现力且可控的文字转语音模型。如需了解详情，请参阅 [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn) 文档。

## 2026 年 4 月 14 日

- 发布了更新后的机器人模型 `gemini-robotics-er-1.6-preview`。
  现在，它具备了新的功能，例如读取乐器，以及改进的空间和物理推理能力。如需了解详情，请参阅 [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn) 页面和[博客](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=zh-cn)。
- 弃用公告：`gemini-robotics-er-1.5-preview` 模型将于 2026 年 4 月 30 日上午 9 点（太平洋标准时间）[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 4 月 2 日

- 已发布 `gemma-4-26b-a4b-it` 和 `gemma-4-31b-it`，可在 [AI Studio](https://aistudio.google.com?hl=zh-cn) 中使用，也可通过 Gemini API 使用，是 [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=zh-cn) 发布的一部分。

## April 1, 2026

- 推出了新的 [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn) 和 [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn) 推理层级，可提供更多选项来优化费用或延迟时间。

## 2026 年 3 月 31 日

- 推出了 Veo 3.1 Lite 预览版 [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=zh-cn)，这是我们最具成本效益的[视频生成](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)模型，专为快速迭代和构建高容量应用而设计。
- `gemini-2.5-flash-lite-preview-09-2025` 模型已关闭。请改用 [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn)。

## 2026 年 3 月 26 日

- 发布了 [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=zh-cn)，这是最新的音频转音频 (A2A) 模型，专为实时对话和语音优先的 AI 应用而设计。请阅读 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn) 文档，开始使用该 API。

## 2026 年 3 月 25 日

- 推出了 [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn) 音乐生成模型：[`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=zh-cn)（30 秒片段）和 [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=zh-cn)（完整歌曲）。这两款模型均可接受文本和图片输入，并生成高品质的 48 kHz 立体声音频。如需了解详情和代码示例，请参阅[音乐生成](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn)指南。

## 2026 年 3 月 23 日

- 在 AI Studio 中推出了[预付款和后付费结算方案](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。现有账号可能会受到影响；如需了解详情，请参阅[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)文档。

## 2026 年 3 月 18 日

- 发布了新的[内置工具和函数调用组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)功能，让您可以在一次 API 调用中使用 Gemini 的内置工具和自定义函数调用工具。
- Gemini 3 模型现在支持[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn#supported_models)。

## 2026 年 3 月 16 日

- 推出了经过改版的[使用层级](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#about-billing)和[结算账号支出上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#tier-spend-caps)，以提升用户结算体验。

## 2026 年 3 月 12 日

- 在 AI Studio 的结算中引入了[项目级支出上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#project-spend-caps)。

## 2026 年 3 月 10 日

- 发布了我们的首个多模态嵌入模型 `gemini-embedding-2-preview`。
  它支持文本、图片、视频、音频和 PDF 输入，可将所有模态映射到统一的嵌入空间中。如需了解详情，请参阅[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)。
- 弃用公告：`gemini-2.5-flash-lite-preview-09-2025` 模型将于 2026 年 3 月 31 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 3 月 9 日

- Gemini 3 Pro 预览版模型已[关闭](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。`gemini-3-pro-preview` 现在指向 [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn)。

## 2026 年 3 月 3 日

- 推出了 Gemini 3.1 Flash-Lite 预览版，这是 Gemini 3 系列中的首款 Flash-Lite 模型。如需了解规格、具体更新和开发者指南，请参阅[模型页面](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn)。

## 2026 年 2 月 26 日

- 推出了 Nano Banana 2（[Gemini 3.1 Flash Image 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=zh-cn)），这是一款高效模型，专为极致速度与大规模量产场景而优化。
- 弃用公告：Gemini 3 Pro（预览版）(`gemini-3-pro-preview`) 将于 2026 年 3 月 9 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 2 月 19 日

- 发布了 [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn)，这是全新 Gemini 3 系列中的最新迭代版本。
- 为同时使用 Bash 和工具进行构建的用户推出了一个单独的端点 `gemini-3.1-pro-preview-customtools`，该端点可以更好地确定自定义工具的优先级。

## 2026 年 2 月 18 日

- 弃用公告：以下模型将于 2026 年 6 月 1 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 2026 年 2 月 17 日

- 以下型号已[停用](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 2026 年 1 月 29 日

- 在 `gemini-3-pro-preview` 和 `gemini-3-flash-preview` 中推出了对“计算机使用”工具的支持。

## 2026 年 1 月 21 日

- 更改了 `latest` 别名：

  - `gemini-pro-latest` 已切换为 `gemini-3-pro-preview`
  - `gemini-flash-latest` 已切换为 `gemini-3-flash-preview`

## 2026 年 1 月 15 日

- 弃用公告：以下模型将于 2026 年 2 月 17 日[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)：

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` 模型已关闭。

## 2026 年 1 月 14 日

- `text-embedding-004` 模型已[关停](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2026 年 1 月 13 日

- 为 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) 添加了 4K 输出分辨率，并为所有分辨率的纵向视频提供了更多支持。

## 2026 年 1 月 12 日

- 推出了模型生命周期功能。现在，部分模型将指定生命周期阶段和弃用时间表。如需了解详情，请参阅以下文档：

  - [模型阶段](https://ai.google.dev/api/generate-content?hl=zh-cn#ModelStatus)

## 2026 年 1 月 8 日

- 推出了对 Cloud Storage 存储分区以及任何公共和私有数据库预签名网址的支持，作为 Gemini API 的数据输入源。文件大小上限也从 20MB 提高到 100MB。如需了解详情，请参阅[文件输入方法指南](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn)。

## 2025 年 12 月 19 日

- 在 v1beta 中对 Interactions API 引入了重大变更。`total_reasoning_tokens` 字段已重命名为 `total_thought_tokens`，以便更好地与思考模型中的“想法”概念保持一致。

## 2025 年 12 月 17 日

- 推出了 Gemini 3 Flash 预览版 `gemini-3-flash-preview`，以远低于大型模型的成本，提供可媲美大型模型的快速前沿级性能。升级了视觉和空间推理能力，以及代理式编码能力。阅读有关部分新功能的文档，包括：

  - [多模态函数响应](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#multimodal)
  - [使用图片执行代码](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn#images)

## 2025 年 12 月 12 日

- 发布了 `gemini-2.5-flash-native-audio-preview-12-2025`，这是 Live API 的新原生音频模型。此更新可提高模型处理复杂工作流程的能力。如需了解详情，请参阅 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn)和 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=zh-cn)。

## 2025 年 12 月 11 日

- 发布了 Interactions API。此 API 提供了与 Gemini 模型和代理交互的统一界面。如需了解详情，请参阅[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 指南。
- 推出了 Gemini Deep Research 智能体预览版。它可以自主规划、执行和汇总多步骤研究任务的结果。如需了解详情，请参阅 [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 指南。

## 2025 年 12 月 10 日

- 推出了对[文字转语音模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)的增强功能，包括 Gemini 2.5 Flash TTS 预览版（经过优化，可实现低延迟）和 Gemini 2.5 Pro TTS 预览版（经过优化，可实现高质量），可提供更丰富的表现力、更精准的语速和更流畅的对话。

## 2025 年 12 月 9 日

- 以下 Gemini Live API 模型现已关闭：
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 2024 年 12 月 5 日

- Gemini 3 的[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)功能将于 2026 年 1 月 5 日开始结算。

## 2025 年 12 月 4 日

- 弃用公告：`gemini-2.5-flash-image-preview` 模型将于 2026 年 1 月 15 日关停。

## 2025 年 12 月 3 日

- 弃用公告：`text-embedding-004` 模型将于 2026 年 1 月 14 日停止服务。

## 2025 年 11 月 20 日

- 发布了 Gemini 3 Pro Image 预览版 `gemini-3-pro-image-preview`，这是 Nano Banana 模型的下一代版本。如需了解详情，请参阅[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)页面。

## 2025 年 11 月 18 日

- 发布了首款 Gemini 3 系列模型 `gemini-3-pro-preview`，这是我们前沿的推理和多模态理解模型，具有强大的智能体和编码能力。

  除了在智能性和性能方面有所改进之外，Gemini 3 Pro 预览版还引入了以下方面的新行为：

  - [媒体分辨率](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn)
  - [思考签名](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn)
  - [思考等级](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#thinking-levels)

  如需了解迁移、新功能和规范，请参阅 [Gemini 3 开发者指南](https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-cn)。

## 2025 年 11 月 11 日

- 弃用公告：以下模型将被关闭：

  - 11 月 12 日：

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 11 月 14 日：

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 2025 年 11 月 10 日

- 以下模型已关闭：

  - `imagen-3.0-generate-002`

  请改用 [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-cn#imagen-4)。如需了解详情，请参阅 [Gemini 弃用表](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)。

## 2025 年 11 月 6 日

- 面向公众预览版发布了文件搜索 API，使开发者能够以自己的数据为依据生成回答。如需了解详情，请参阅新版[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)页面。

## 2025 年 11 月 4 日

- 对于 [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)，图片的输入 token 数已从 1,290 减少到 258，从而降低了图片编辑的费用。
- 弃用公告：以下模型将被关闭：

  - 11 月 18 日：

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 12 月 2 日：

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 12 月 9 日：

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 2025 年 10 月 29 日

- 针对 Gemini API 推出了新的[日志记录和数据集](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)工具。

## 2025 年 10 月 20 日

- 以下 Gemini Live API 模型现已关闭：

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  您可以改用 `gemini-2.5-flash-native-audio-preview-09-2025`。
- 弃用公告：`gemini-2.0-flash-live-001` 和 `gemini-live-2.5-flash-preview` 将于 2025 年 12 月 9 日关闭。

## 2025 年 10 月 17 日

- **Grounding with Google Maps** 现已正式发布。如需了解详情，请参阅[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)文档。

## 2025 年 10 月 15 日

- 发布了 [Veo 3.1 和 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn#veo-3.1) 型号的公开预览版，新增了以下功能：

  - 延长 Veo 创作的视频。
  - 参考最多三张图片来生成视频。
  - 提供第一帧和最后一帧图片，以便生成视频。

  此次发布还新增了更多 Veo 3 输出视频时长选项：4 秒、6 秒和 8 秒。
- 弃用公告：`veo-3.0-generate-preview` 和 `veo-3.0-fast-generate-preview` 将于 2025 年 11 月 12 日关停。

## 2025 年 10 月 7 日

- 发布了 [Gemini 2.5 Computer Use 预览版](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)

## 2025 年 10 月 2 日

- 正式发布 Gemini 2.5 Flash Image：[使用 Gemini 生成图片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)

## 2025 年 9 月 29 日

- 以下 Gemini 1.5 模型现已关闭：
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 2025 年 9 月 25 日

- 发布了 Gemini Robotics-ER 1.5 预览版模型。请参阅[机器人技术概览](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn)，了解如何将该模型用于机器人技术应用。
- 发布了以下预览模型：

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  如需了解详情，请参阅[模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面。

## 2025 年 9 月 23 日

- 发布了 `gemini-2.5-flash-native-audio-preview-09-2025`，这是 Live API 的新原生音频模型，改进了函数调用和语音截断处理。如需了解详情，请参阅 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn)和 [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-native-audio)。

## 2025 年 9 月 16 日

- 弃用公告：以下模型将于 2025 年 10 月关闭：

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  如需详细了解最新的嵌入模型，请参阅[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)页面。

## 2025 年 9 月 10 日

- 发布了对 [Batch API 中的 Embeddings 模型](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn#batch-embedding)的支持，并向 [OpenAI 兼容性库](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn#batch)添加了 Batch API，以便更轻松地开始使用批量查询。

## 2025 年 9 月 9 日

- 发布了 Veo 3 和 Veo 3 Fast 正式版，价格更低，并新增了宽高比、分辨率和种子选项。如需了解详情，请参阅 [Veo 文档](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn#model-features)。

## 2025 年 8 月 26 日

- 发布了最新的原生图片生成模型 [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-image-preview)。

## 2025 年 8 月 18 日

- 正式发布了 [网址 上下文工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)，该工具可用于向提示提供网址作为附加上下文。对将网址上下文与 `gemini-2.0-flash` 模型搭配使用的支持（在实验性发布期间提供）将于一周后停止。

## 2025 年 8 月 14 日

- 正式发布 (GA) 了 Imagen 4 Ultra、Standard 和 Fast 模型。如需了解详情，请参阅 [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-cn) 页面。

## 2025 年 8 月 7 日

- `allow_adult`设置现已在受限地区推出。如需了解详情，请参阅 [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=zh-cn#veo-model-parameters) 页面。

## 2025 年 7 月 31 日

- 针对 Veo 3 预览版模型推出了图像转视频功能。
- 发布了 Veo 3 Fast 预览版模型。
- 如需详细了解 Veo 3，请访问 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) 页面。

## 2025 年 7 月 22 日

- 发布了`gemini-2.5-flash-lite`，这是我们快速、低成本、高性能的 Gemini 2.5 模型。如需了解详情，请参阅 [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-lite)。

## July 17, 2025

- 发布了 `veo-3.0-generate-preview`，这是 Veo 的最新更新，引入了带音频的视频生成功能。如需详细了解 Veo 3，请访问 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) 页面。
- 提高了 Imagen 4 Standard 和 Ultra 的速率限制。如需了解详情，请访问[速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn)页面。

## 2025 年 7 月 14 日

- 发布了 `gemini-embedding-001`，即文本嵌入模型的稳定版。如需了解详情，请参阅[嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)。`gemini-embedding-exp-03-07` 模型将于 2025 年 8 月 14 日弃用。

## 2025 年 7 月 7 日

- 推出了 Gemini API 批量模式。将请求分批发送，并以异步方式进行处理。如需了解详情，请参阅[批量模式](https://ai.google.dev/gemini-api/docs/batch-mode?hl=zh-cn)。

## 2025 年 6 月 26 日

- 预览版模型 `gemini-2.5-pro-preview-05-06` 和 `gemini-2.5-pro-preview-03-25` 现在会重定向到最新的稳定版 `gemini-2.5-pro`。
- `gemini-2.5-pro-exp-03-25`已关机。

## 2025 年 6 月 24 日

- 发布了 Imagen 4 Ultra 和标准预览版模型。如需了解详情，请参阅[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)页面。

## 2025 年 6 月 17 日

- 发布了 `gemini-2.5-pro`，这是我们功能最强大的模型的稳定版，现在还具备自适应思考能力。如需了解详情，请参阅 [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-pro) 和[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)。`gemini-2.5-pro-preview-05-06`将于 2025 年 6 月 26 日重定向到 `gemini-2.5-pro`。
- 发布了 `gemini-2.5-flash`，这是我们的首个稳定版 2.5 Flash 模型。如需了解详情，请参阅 [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash)。
  `gemini-2.5-flash-preview-04-17` 将于 2025 年 7 月 15 日弃用。
- 发布了`gemini-2.5-flash-lite-preview-06-17`，这是一款低成本、高性能的 Gemini 2.5 模型。如需了解详情，请参阅 [Gemini 2.5 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-lite)。

## 2025 年 6 月 5 日

- 发布了 `gemini-2.5-pro-preview-06-05`，这是我们最强大的模型的新版本，现在具有自适应思维能力。如需了解详情，请参阅 [Gemini 2.5 Pro 预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-pro-preview-06-05)和[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)。
  `gemini-2.5-pro-preview-05-06` 将于 2025 年 6 月 26 日重定向到 `gemini-2.5-pro`。

## 2025 年 5 月 27 日

- 最后一个可用的调优模型 Gemini 1.5 Flash 001 已关闭。
  任何模型都不再支持调优。
  请参阅[使用 Gemini API 进行微调](https://ai.google.dev/gemini-api/docs/model-tuning?hl=zh-cn)。

## 2025 年 5 月 20 日

**API 更新：**

- 推出了对使用剪辑间隔和可配置的帧速率采样进行[自定义视频预处理](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#customize-video-processing)的支持。
- 推出了多工具使用功能，支持在同一 `generateContent` 请求中配置[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)和[使用 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)。
- 在 Live API 中推出了对[异步函数调用](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn#async-function-calling)的支持。
- 推出了实验性 [网址 上下文工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)，用于提供网址作为提示的附加背景信息。

**模型更新**：

- 发布了 `gemini-2.5-flash-preview-05-20`，这是一款经过优化的 Gemini [预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#model-versions)模型，具有出色的性价比和自适应思维能力。如需了解详情，请参阅 [Gemini 2.5 Flash 预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-preview)和[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)。
- 发布了 [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-pro-preview-tts) 和 [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-preview-tts) 模型，这些模型能够[生成包含一个或两个说话者的语音](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)。
- 发布了 `lyria-realtime-exp` 模型，该模型可[实时生成音乐](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn)。
- 发布了 `gemini-2.5-flash-preview-native-audio-dialog` 和 `gemini-2.5-flash-exp-native-audio-thinking-dialog`，这是两款支持原生音频输出功能的 Live API 新 Gemini 模型。如需了解详情，请参阅 [Live API 指南](https://ai.google.dev/gemini-api/docs/live-guide?hl=zh-cn#native-audio-output)和 [Gemini 2.5 Flash 原生音频](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-native-audio)。
- 发布了 `gemma-3n-e4b-it` 预览版，可在 [AI Studio](https://aistudio.google.com?hl=zh-cn) 中使用，也可通过 Gemini API 使用，作为 [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=zh-cn) 发布的一部分。

## 2025 年 5 月 7 日

- 发布了 `gemini-2.0-flash-preview-image-generation`，一个用于生成和编辑图片的预览版模型。如需了解详情，请参阅[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)和 [Gemini 2.0 Flash 预览版图片生成](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.0-flash-preview-image-generation)。

## 2025 年 5 月 6 日

- 发布了 `gemini-2.5-pro-preview-05-06`，这是我们功能最强大的模型的新版本，在代码和函数调用方面有所改进。`gemini-2.5-pro-preview-03-25` 将自动指向新版模型。

## 2025 年 4 月 17 日

- 发布了 `gemini-2.5-flash-preview-04-17`，这是一款经过优化的 Gemini [预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#model-versions)模型，具有出色的性价比和自适应思维能力。如需了解详情，请参阅 [Gemini 2.5 Flash 预览版](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-flash-preview)和[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)。

## 2025 年 4 月 16 日

- 为 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.0-flash) 推出了上下文缓存功能。

## 2025 年 4 月 9 日

**模型更新**：

- 发布了 `veo-2.0-generate-001`，一款正式版 (GA) 的文本到视频和图片到视频模型，能够生成细节丰富且富有艺术性的视频。如需了解详情，请参阅 [Veo 文档](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)。
- 发布了 `gemini-2.0-flash-live-001`，即启用了结算功能的 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 模型的公开预览版。

  - **增强的会话管理和可靠性**

    - **会话恢复**：在临时网络中断期间保持会话有效。该 API 现在支持服务器端会话状态存储（最长 24 小时），并提供用于重新连接和从上次中断处继续的句柄 (session\_resumption)。
    - **通过上下文压缩实现更长的会话**：支持超出之前时间限制的扩展互动。配置使用滑动窗口机制的上下文窗口压缩，以自动管理上下文长度，防止因上下文限制而突然终止。
    - **正常断开连接通知**：接收 `GoAway` 服务器消息，指示连接即将关闭，以便在终止之前进行正常处理。
  - **更好地控制互动动态**
  - **可配置的语音活动检测 (VAD)**：选择灵敏度级别，或完全停用自动 VAD，并使用新的客户端事件（`activityStart`、`activityEnd`）进行手动轮流发言控制。
  - **可配置的中断处理**：决定用户输入是否应中断模型的回答。
  - **可配置的轮流覆盖范围**：选择 API 是持续处理所有音频和视频输入，还是仅在检测到最终用户说话时捕获音频和视频输入。
  - **可配置的媒体分辨率**：通过选择输入媒体的分辨率，优化质量或令牌使用情况。
  - **更丰富的输出内容和功能**
  - **更多语音和语言选项**：新增了两种语音和 30 种语言，可用于音频输出。现在，您可以在 `speechConfig` 中配置输出语言。
  - **文本流式传输**：以增量方式接收生成的文本回答，从而更快地向用户显示回答。
  - **token 使用情况报告**：通过服务器消息的 `usageMetadata` 字段中提供的详细 token 数量（按模态和提示或回答阶段细分）深入了解使用情况。

## 2025 年 4 月 4 日

- 发布了 `gemini-2.5-pro-preview-03-25`，这是启用了结算功能的 Gemini 2.5 Pro 公开预览版。您可以继续在免费层级中使用 `gemini-2.5-pro-exp-03-25`。

## 2025 年 3 月 25 日

- 发布了 `gemini-2.5-pro-exp-03-25`，这是一款公开实验版 Gemini 模型，默认情况下始终处于思考模式。
  如需了解详情，请参阅 [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-2.5-pro-preview-03-25)。

## 2025 年 3 月 12 日

**模型更新**：

- 发布了一款实验性 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn#gemini) 模型，能够生成和修改图片。
- 已发布 `gemma-3-27b-it`，可在 [AI Studio](https://aistudio.google.com?hl=zh-cn) 中使用，也可通过 Gemini API 使用，是 [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=zh-cn) 发布的一部分。

**API 更新：**

- 添加了对 [YouTube 网址](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn#youtube)作为媒体来源的支持。
- 添加了对包含小于 20MB 的[内嵌视频](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn#inline-video)的支持。

## 2025 年 3 月 11 日

**SDK 更新：**

- 发布了 [Google Gen AI SDK（适用于 TypeScript 和 JavaScript）](https://googleapis.github.io/js-genai)的公开预览版。

## 2025 年 3 月 7 日

**模型更新**：

- 发布了 `gemini-embedding-exp-03-07`，一款基于 Gemini 的[实验性](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-cn)嵌入模型，目前处于公开预览版阶段。

## 2025 年 2 月 28 日

**API 更新：**

- 为基于 Gemini 2.0 Pro 的实验性模型 `gemini-2.0-pro-exp-02-05` 添加了对[将搜索作为工具](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)的支持。

## 2025 年 2 月 25 日

**模型更新**：

- 发布了 `gemini-2.0-flash-lite`，即 [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-2.0-flash-lite) 的正式版 (GA)，该模型在速度、规模和成本效益方面都经过了优化。

## 2025 年 2 月 19 日

**AI Studio 更新**：

- 支持[其他地区](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)（科索沃、格陵兰和法罗群岛）。

**API 更新：**

- 支持[其他地区](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)（科索沃、格陵兰和法罗群岛）。

## 2025 年 2 月 18 日

**模型更新**：

- Gemini 1.0 Pro 不再受支持。如需查看支持的模型的列表，请参阅 [Gemini 模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)。

## 2025 年 2 月 11 日

**API 更新：**

- 更新了 [OpenAI 库兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)。

## 2025 年 2 月 6 日

**模型更新**：

- 发布了 [Gemini API 中的 Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-cn) 的正式版 (GA) `imagen-3.0-generate-002`。

**SDK 更新：**

- 发布了 [Google Gen AI SDK for Java](https://github.com/googleapis/java-genai) 公开预览版。

## 2025 年 2 月 5 日

**模型更新**：

- 发布了 `gemini-2.0-flash-001`，这是 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-2.0-flash) 的正式版 (GA)，支持纯文本输出。
- 发布了 `gemini-2.0-pro-exp-02-05`，即 Gemini 2.0 Pro 的[实验性](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-cn)公开预览版。
- 发布了 `gemini-2.0-flash-lite-preview-02-05`，这是一款针对成本效益进行优化的实验性公开预览版[模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-2.0-flash-lite)。

**API 更新：**

- 为代码执行添加了[文件输入和图表输出](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn#input-output)支持。

**SDK 更新：**

- 发布了 [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/) 正式版 (GA)。

## 2025 年 1 月 21 日

**模型更新**：

- 发布了 `gemini-2.0-flash-thinking-exp-01-21`，这是 [Gemini 2.0 Flash Thinking 模型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)背后的模型的最新预览版。

## 2024 年 12 月 19 日

**模型更新**：

- 发布了 Gemini 2.0 Flash 思考模式的公开预览版。思考模式是一种测试时间计算模型，可让您在模型生成回答时查看其思考过程，并生成推理能力更强的回答。

  如需详细了解 Gemini 2.0 Flash Thinking 模式，请参阅我们的[概览页面](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=zh-cn)。

## 2024 年 12 月 11 日

**模型更新**：

- 发布了[公开预览版 Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-2.0-flash)。Gemini 2.0 Flash Experimental 的部分功能包括：
  - 速度是 Gemini 1.5 Pro 的两倍
  - 使用 Live API 进行双向流式传输
  - 以文本、图片和语音形式生成多模态回答
  - 通过多轮推理使用内置工具，以使用代码执行、搜索、函数调用等功能

如需详细了解 Gemini 2.0 Flash，请参阅我们的[概览页面](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=zh-cn)。

## 2024 年 11 月 21 日

**模型更新**：

- 发布了 `gemini-exp-1121`，这是一款功能更强大的实验性 Gemini API 模型。

**模型更新**：

- 更新了 `gemini-1.5-flash-latest` 和 `gemini-1.5-flash` 模型别名，以使用 `gemini-1.5-flash-002`。
  - 更改为 `top_k` 参数：`gemini-1.5-flash-002` 模型支持介于 1 和 41（不含）之间的 `top_k` 值。大于 40 的值将更改为 40。

## 2024 年 11 月 14 日

**模型更新**：

- 发布了 `gemini-exp-1114`，这是一款强大的实验性 Gemini API 模型。

## 2024 年 11 月 8 日

**API 更新：**

- 在 OpenAI 库 / REST API 中[添加了对 Gemini 的支持](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)。

## 2024 年 10 月 31 日

**API 更新：**

- 添加了[依托 Google 搜索进行接地的支持](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)。

## 2024 年 10 月 3 日

**模型更新**：

- 发布了 `gemini-1.5-flash-8b-001`，这是我们最小的 Gemini API 模型的稳定版。

## 2024 年 9 月 24 日

**模型更新**：

- 发布了 `gemini-1.5-pro-002` 和 `gemini-1.5-flash-002`，这是 Gemini 1.5 Pro 和 1.5 Flash 的两个全新稳定版，已正式发布。
- 更新了 `gemini-1.5-pro-latest` 模型代码以使用 `gemini-1.5-pro-002`，并更新了 `gemini-1.5-flash-latest` 模型代码以使用 `gemini-1.5-flash-002`。
- 发布了 `gemini-1.5-flash-8b-exp-0924` 以取代 `gemini-1.5-flash-8b-exp-0827`。
- 为 Gemini API 和 AI Studio 发布了[公民诚信安全过滤器](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn#safety-filters)。
- 在 Python 和 NodeJS 中为 Gemini 1.5 Pro 和 1.5 Flash 发布了对两个新参数的支持：[`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=zh-cn#FIELDS.frequency_penalty) 和 [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=zh-cn#FIELDS.presence_penalty)。

## 2024 年 9 月 19 日

**AI Studio 更新**：

- 在模型回答中添加了“我喜欢”和“不喜欢”按钮，以便用户就回答质量提供反馈。

**API 更新：**

- 新增了对 Google Cloud 赠金的支持，现在可将 Google Cloud 赠金用于 Gemini API 用量。

## 2024 年 9 月 17 日

**AI Studio 更新**：

- 添加了**在 Colab 中打开**按钮，可将提示以及运行提示所需的代码导出到 Colab 笔记本。此功能尚不支持使用工具（JSON 模式、函数调用或代码执行）进行提示。

## 2024 年 9 月 13 日

**AI Studio 更新**：

- 新增了对比较模式的支持，可让您比较不同模型和提示的回答，以便找到最适合您应用场景的回答。

## 2024 年 8 月 30 日

**模型更新**：

- Gemini 1.5 Flash 支持[通过模型配置提供 JSON 架构](https://ai.google.dev/gemini-api/docs/json-mode?hl=zh-cn#supply-schema-in-config)。

## 2024 年 8 月 27 日

**模型更新**：

- 发布了以下[实验性模型](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=zh-cn)：
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 2024 年 8 月 9 日

**API 更新：**

- 添加了对 [PDF 处理](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)的支持。

## 2024 年 8 月 5 日

**模型更新**：

- 发布了对 Gemini 1.5 Flash 的微调支持。

## 2024 年 8 月 1 日

**模型更新**：

- 发布了 `gemini-1.5-pro-exp-0801`，即 [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-1.5-pro) 的新实验性版本。

## 2024 年 7 月 12 日

**模型更新**：

- 从 Google AI 服务和工具中移除了对 Gemini 1.0 Pro Vision 的支持。

## 2024 年 6 月 27 日

**模型更新**：

- 正式发布 Gemini 1.5 Pro 的 200 万上下文窗口。

**API 更新：**

- 新增了对[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)的支持。

## 2024 年 6 月 18 日

**API 更新：**

- 添加了对[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)的支持。

## 2024 年 6 月 12 日

**模型更新**：

- Gemini 1.0 Pro Vision 已弃用。

## 2024 年 5 月 23 日

**模型更新**：

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-1.5-pro) (`gemini-1.5-pro-001`) 已发布正式版 (GA)。
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-1.5-flash) (`gemini-1.5-flash-001`) 已正式发布 (GA)。

## 2024 年 5 月 14 日

**API 更新：**

- 为 Gemini 1.5 Pro 推出了 200 万个 token 的上下文窗口（等候名单）。
- 为 Gemini 1.0 Pro 推出了“随用随付”[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)方式，Gemini 1.5 Pro 和 Gemini 1.5 Flash 的结算方式即将推出。
- 为即将推出的 Gemini 1.5 Pro 付费层级提高了速率限制。
- 为 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-cn) 添加了内置视频支持。
- 为 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-cn) 添加了纯文本支持。
- 添加了对并行函数调用的支持，以便一次返回多个调用结果。

## 2024 年 5 月 10 日

**模型更新**：

- 发布了预览版 [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-1.5-flash) (`gemini-1.5-flash-latest`)。

## 2024 年 4 月 9 日

**模型更新**：

- 发布了[预览版 Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-1.5-pro) (`gemini-1.5-pro-latest`)。
- 发布了新的文本嵌入模型 `text-embeddings-004`，该模型支持小于 768 的[弹性嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn#elastic-embedding)大小。

**API 更新：**

- 发布了 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-cn)，用于临时存储媒体文件以用于提示。
- 新增了对使用文本、图片和音频数据发出提示的支持，也称为*多模态*提示。如需了解详情，请参阅[使用媒体内容进行提示](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-cn)。
- 在 Beta 版中发布了[系统指令](https://ai.google.dev/gemini-api/docs/system-instructions?hl=zh-cn)。
- 添加了[函数调用模式](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#function_calling_mode)，用于定义函数调用的执行行为。
- 新增了对 `response_mime_type` 配置选项的支持，该选项可让您以 [JSON 格式](https://ai.google.dev/gemini-api/docs/api-overview?hl=zh-cn#json)请求响应。

## 2024 年 3 月 19 日

**模型更新**：

- 在 Google AI Studio 中或通过 Gemini API [添加了对调优 Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) 的支持。

## 2023 年 12 月 13 日

**模型更新**：

- gemini-pro：适用于各种任务的新文本模型。兼顾能力和效率。
- gemini-pro-vision：适用于各种任务的新型多模态模型。
  兼顾功能和效率。
- embedding-001：新的嵌入模型。
- aqa：一种经过专门调优的新模型，经过训练，可使用文本段落作为依据来回答问题。

如需了解详情，请参阅 [Gemini 模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)。

**API 版本更新**：

- v1：稳定版 API 渠道。
- v1beta：Beta 版。此频道具有可能正在开发中的功能。

如需了解详情，请参阅[“API 版本”主题](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-cn)。

**API 更新：**

- `GenerateContent` 是用于聊天和文本的单个统一端点。
- 可通过 `StreamGenerateContent` 方法进行流式传输。
- 多模态功能：图片是一种新支持的模态
- 新的 Beta 版功能：
  - [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
  - [语义检索器](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=zh-cn)
  - 归因问答 (AQA)
- 更新了候选对象数量：Gemini 模型仅返回 1 个候选对象。
- 不同的 Safety Settings 和 SafetyRating 类别。如需了解详情，请参阅[安全设置](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)。
- 目前尚不支持对 Gemini 模型进行模型调优（正在开发中）。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-09。"],[],[]]
