---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=zh-CN
fetched_at: 2026-10-12T07:02:30.971374+00:00
title: "Gemini API \u4f18\u5316\u548c\u63a8\u7406 \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini API 优化和推理

Gemini API 提供多种优化机制，可帮助您根据具体的工作负载需求平衡速度、成本和可靠性。无论您是构建实时对话机器人，还是运行繁重的离线数据处理流水线，选择合适的范式都可以显著降低成本或提升性能。

| 功能 | 标准 | Flex | 优先级 | 批量 | 缓存 |
| --- | --- | --- | --- | --- | --- |
| **价格** | 全价 | 5 折优惠 | 比标准版多 75% 到 100% | 5 折优惠 | 90% 的折扣 + 按比例计算的 token 存储费用 |
| **延迟时间** | 秒到分钟 | 分钟数（目标为 1-15 分钟） | 秒 | 最长 24 小时 | 首 token 延迟更短 |
| **可靠性** | 高 / 中高 | 尽力而为（可舍弃） | 高（不可脱落） | 高（针对吞吐量） | 不适用 |
| **接口** | 同步 | 同步 | 同步 | 异步 | 保存的状态 |
| **最佳使用场景** | 常规应用工作流程 | 非紧急的顺序链 | 正式版面向用户的应用 | 海量数据集、离线评估 | 针对同一文件的重复查询 |

## 推理服务层级（同步）

您可以在标准生成调用中传递 `service_tier` 参数，从而在可靠性优化和成本优化的同步流量之间切换。

### 标准推理（默认）

标准层级是顺序生成内容的默认选项。
它可提供正常的响应时间，无需额外付费或排长队。

- **可靠性**：标准严重程度
- **价格**：标准价格。
- **最适合**：大多数日常互动式应用。

### 优先推理（延迟时间优化型）

[优先](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)处理会将您的请求路由到高严重性计算队列。此类流量严格来说不可舍弃（永远不会被其他层级抢占），并且可靠性最高。如果您超出动态优先级限制，系统会将请求降级为标准处理，而不是因错误而失败。

- **可靠性**：最高严重程度
- **价格**：比标准费率高 75% 至 100%。
- **最适合**：客户聊天机器人、实时欺诈检测和业务关键型 Copilot。

### Flex 推理（费用优化）

[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)利用机会性非高峰算力容量，与标准费率相比可节省 50% 的费用。请求会同步处理，这意味着您无需重写代码来管理批处理对象。由于它是“可舍弃”的流量，因此如果系统遇到标准流量高峰，请求可能会被抢占。

- **可靠性**：无保证，可舍弃的关键性
- **价格**：标准价格的 50%（按令牌数结算）。
- **最适合**：多步骤 Agentic Workflows（其中调用 N+1 依赖于调用 N 的输出）、后台 CRM 更新和离线评估。

## Batch API（批量、异步）

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn) 旨在以标准费用 50% 的价格异步处理大量请求。您可以以内嵌字典的形式提交请求，也可以使用 JSONL 输入文件（最大 2 GB）。它使用后台吞吐量队列处理请求，目标周转时间为 24 小时。

- **可靠性**：可舍弃，但具有 24 小时自动重试和排队系统
- **价格**：标准价格的 50%。
- **最适合用于**：预处理海量数据集、运行周期性回归测试套件，以及生成大量图片或嵌入内容。

## 上下文缓存（节省输入）

当较短的请求重复引用大量初始上下文时，可以使用[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)。

- **隐式缓存**：在 Gemini 2.5 及更新型号上自动启用。
  如果您的请求基于常见提示前缀命中现有缓存，系统会传递节省的费用。
- **显式缓存**：您可以手动创建具有特定存留时间 (TTL) 的缓存对象。创建后，您可以在后续请求中引用缓存的令牌，以避免重复传递相同的语料库载荷。
- **价格**：根据缓存词元数量和存储时长 (TTL) 计费。
- **最适合**：有大量系统指令的聊天机器人、对较长的视频文件进行的重复分析，或针对大型文档集的查询。

## 通过 agentic 处理降低视频输入成本

对于长视频内容，智能体处理可以将输入令牌费用最多降低 88%，同时提高回答质量。模型不会以 1 FPS 的速率提取每一帧（静态处理），而是动态搜索视频，加载与提示相关的转写内容和/或帧和/或音频。对于延迟至关重要的短视频片段（时长不到 5 分钟），静态处理可能会提供更快的首 token 延迟时间 (TTFT)，因为代理模式在开始生成之前会进行内部推理和工具往返。

如需将智能体处理与 Gemini 3.8 Flash、3.6 Flash 或 3.5 Flash Lite 搭配使用，请在视频输入中设置 `processing: "agentic"` (Interactions API) 或 `media_processing: "AGENTIC"` (GenerateContent API)。如果模型不支持代理处理，则会返回错误。

如需查看代码示例，请参阅[智能体视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#agentic-video-understanding)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-09。"],[],[]]
