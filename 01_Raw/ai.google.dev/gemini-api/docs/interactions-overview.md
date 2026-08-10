---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-CN
fetched_at: 2026-08-10T03:23:55.347127+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Interactions API

Interactions API 是使用 Gemini 模型和智能体进行构建的最佳方式。截至 2026 年 6 月，此功能已全面推出，建议所有新项目使用。虽然现在已将其视为旧版 API，但原始的 [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=zh-cn) API 仍完全受支持。

## 为什么要使用 Interactions API？

- **适用于所有应用的通用接口**：设计为适用于各种用例的标准接口，包括单轮文本生成、多模态理解、结构化输出、工具编排和代理工作流。
- **适用于模型和代理的单一 API**：一个统一的端点和模式，可用于直接调用标准 Gemini 模型以及专用代理（例如 Deep Research 和自定义托管代理）。
- **开箱即用的新功能**：包括使用 `previous_interaction_id` 的可选服务器端对话状态、用于调试和界面渲染的可观测执行步骤，以及使用 `background=true` 的长时间运行任务的[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)。
- **以更低的费用实现更高的缓存命中率**：使用多轮对话时，可选的服务器端状态管理功能可实现更高效的跨轮上下文缓存，从而降低 token 费用。
- **新功能发布平台**：未来，所有新模型、多模态功能、工具和智能体功能都将在 Interactions API 上发布。

默认情况下，Interactions API 会存储请求，以便您可以使用 `previous_interaction_id` 来利用服务器端状态管理功能。您可以通过设置 `store=false` 来选择无状态行为。如需了解详情，请参阅[数据保留](#data-storage-retention)部分。

## 开始使用

- **设置编码智能体**：连接到 **Gemini 文档 MCP** 并安装 `gemini-interactions-api` 技能，让助理直接访问最新的开发者文档和最佳实践。如需了解详细步骤，请参阅[设置编码代理指南](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn)
- **从 `generateContent` 迁移**：如果您有现有的集成，请按照[迁移指南](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-cn)过渡到 Interactions API。
- **使用入门**：按照[Interactions API 使用入门指南](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn)中的步骤操作。

### 功能指南

通过以下指南探索 Interactions API 的具体功能。您可以使用这些页面上的切换开关在 generateContent API 和 Interactions API 之间切换：

- [文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)
- [图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)
- [图片推理](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)
- [音频理解](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)
- [视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn)
- [文件处理](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)
- [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
- [结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)
- [Deep Research 智能体](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn)
- [灵活推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)
- [优先推断](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)

## Interactions API 的运作方式

Interactions API 围绕一个核心资源：[**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=zh-cn#Resource:Interaction)。`Interaction` 表示对话或任务中的完整一轮。它充当会话记录，包含互动的完整历史记录，以**执行步骤**的时间顺序序列表示。这些步骤包括模型想法、服务器端或客户端工具调用和结果（例如 `function_call` 和 `function_result`），以及最终的 `model_output`。存储的资源（通过 `interactions.get` 检索）还包含 `user_input` 完整上下文的步骤，但 `interactions.create` 响应仅返回模型生成的步骤。

当您调用 [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=zh-cn#CreateInteraction) 时，您会创建一个新的 `Interaction` 资源。

### 服务器端状态管理

您可以在后续调用中使用已完成互动的 `id`，通过 `previous_interaction_id` 参数继续对话。服务器会使用此 ID 来检索对话历史记录，从而避免您必须重新发送整个对话历史记录。

`previous_interaction_id` 参数仅使用 `previous_interaction_id` 保留对话历史记录（输入和输出）。其他参数属于**互动级**，仅适用于您当前生成的特定互动：

- `tools`
- `system_instruction`
- `generation_config`（包括 `thinking_level`、`temperature` 等）

这意味着，如果您希望应用这些参数，则必须在每次新互动中重新指定这些参数。这种服务器端状态管理是可选的；您也可以通过在每次请求中发送完整的对话历史记录来以无状态模式运行。

### 数据存储和保留

默认情况下，该 API 会存储所有 Interaction 对象 (`store=true`)，以便简化服务器端状态管理功能（使用 `previous_interaction_id`）、[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)（使用 `background=true`）和可观测性功能的使用。

- **付费层级**：系统会将互动数据保留 **55 天**。
- **免费层级**：系统会将互动数据保留 **1 天**。

如果您不希望这样，可以在请求中设置 `store=false`。此控制措施与状态管理分开；您可以选择不存储任何互动数据。不过，请注意，`store=false` 与[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)不兼容，并且会阻止在后续回合中使用 `previous_interaction_id`。

对于付费级项目，您可以在 [AI Studio](https://aistudio.google.com/logs?hl=zh-cn) 中配置保留期限，以在 7 天、14 天、28 天或 55 天后自动将日志标记为从项目存储空间中删除。较短的保留期限可能会影响过往对话的检索。

您可以随时使用 [`delete`](https://ai.google.dev/api/interactions-api?hl=zh-cn#deleteInteraction) 方法以程序化方式删除已存储的互动记录，但这需要互动 ID。您还可以在 [AI Studio](https://aistudio.google.com/logs?hl=zh-cn) 中查看和管理存储的互动日志，包括从项目存储空间中删除日志。

保留期限结束后，系统会自动删除您的数据。

系统会根据[条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn)处理互动对象。

### 在 AI Studio 中查看互动

对于付费层级的项目，该 API 会存储使用 `store=true` 执行的 Interactions API 请求。您可以直接在 [Google AI Studio 的“日志”页面](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=zh-cn)中查看这些日志。如需了解详情，请参阅[日志指南](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)。

## 最佳做法

- **缓存命中率**：有状态模式和无状态模式均支持隐式缓存（请参阅[快速入门](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn#4_multi-turn_conversations)）。使用 `previous_interaction_id`（有状态）继续对话可让系统更轻松地利用对话历史记录的隐式缓存，从而提高性能并降低费用。
- **混合互动**：您可以灵活地在对话中混合使用智能体互动和模型互动。例如，您可以使用 Deep Research 智能体等专业智能体进行初始数据收集，然后使用标准 Gemini 模型执行后续任务，例如总结或重新格式化，并通过 `previous_interaction_id` 将这些步骤关联起来。

## 支持的模型和代理

| 模型名称 | 类型 | 模型 ID |
| --- | --- | --- |
| Gemini 3.5 Flash | 模型 | `gemini-3.5-flash` |
| Gemini 3 Pro 预览版 | 模型 | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | 模型 | `gemini-3.1-flash-lite` |
| Gemini 3 Flash 预览版 | 模型 | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | 模型 | `gemini-2.5-pro` |
| Gemini 2.5 Flash | 模型 | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | 模型 | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | 模型 | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | 模型 | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS 预览版 | 模型 | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | 模型 | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | 模型 | `gemma-4-26b-a4b-it` |
| Lyria 3 Clip 预览版 | 模型 | `lyria-3-clip-preview` |
| Lyria 3 Pro 预览版 | 模型 | `lyria-3-pro-preview` |
| Deep Research 预览版 | 代理 | `deep-research-preview-04-2026` |
| Deep Research 预览版 | 代理 | `deep-research-max-preview-04-2026` |
| Antigravity 预览 | 代理 | `antigravity-preview-05-2026` |

## SDK

您可以使用最新版本的 Google GenAI SDK 来访问 Interactions API。

- 在 Python 中，这是 `2.3.0` 版本及更高版本中的 `google-genai` 软件包。
- 在 JavaScript 中，这是 `2.3.0` 版本及更高版本的 `@google/genai` 软件包。

如需详细了解如何在[库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)页面上安装 SDK，请参阅相关文档。

## 限制

- **远程 MCP**：Gemini 3 不支持远程 MCP，但很快就会支持。
- **多轮模型兼容性**：在对话（有状态或无状态）中混合使用不同模型时，后续模型必须支持将之前模型的输出模态作为输入。例如，如果您使用 `gemini-3.1-flash-image` 生成图片，则无法继续与不接受图片输入的模型（例如纯文本模型或 Lyria 等音乐生成模型）进行对话。

[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=zh-cn) API 支持以下功能，但 Interactions API **尚不支持**这些功能：

- **[视频元数据](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn)**：`video_metadata` 字段，用于设置剪辑间隔和自定义帧速率，以实现视频理解。
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**
- **[自动函数调用 (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=zh-cn#automatic_function_calling_python_only)**
- **[显式缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**：请注意，服务器端隐式缓存可通过 Interactions API 中的 `previous_interaction_id` 实现。
- **[安全设置](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)**：Interactions API 不支持自定义安全设置。

## 反馈

您的反馈对于开发 Interactions API 至关重要。
欢迎在我们的 [Google AI 开发者社区论坛](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-cn)上分享您的想法、报告 bug 或提出功能请求。

## 后续步骤

- 不妨试试 [Interactions API 快速入门笔记本](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=zh-cn)。
- 详细了解 [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-16。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-16。"],[],[]]
