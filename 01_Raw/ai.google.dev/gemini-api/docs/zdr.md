---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=zh-CN
fetched_at: 2026-07-06T05:14:27.221385+00:00
title: "Gemini Developer API \u4e2d\u7684\u96f6\u6570\u636e\u4fdd\u7559 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Developer API 中的零数据保留

本页面详细介绍了 Gemini Developer API 中通常所说的“零数据保留”。

## 训练限制

如 [Gemini API 服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn) 中所述，当您
使用付费服务时，Google 不会使用您的提示（包括关联的系统
说明、缓存的内容以及图片、视频或文档等文件）或
回答来改进我们的产品。付费服务的定义见
[此处](https://ai.google.dev/gemini-api/terms?hl=zh-cn#paid-services)。

## 客户数据保留和实现零数据保留

在以下场景和条件下，客户数据通常会保留有限的时间。若要实现零数据保留，客户必须在以下各个方面采取特定措施或避免使用特定功能：

- **用于滥用行为监控的提示日志记录**：如[Gemini API
  附加服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn)中所述，对于付费服务，Google
  会在有限的一段时间内记录提示和回答，仅用于检测
  违反[使用限制
  政策](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-cn)的行为。当您针对特定项目的 ZDR 请求获得批准后，所有用户内容（提示和回答）和可识别的元数据（例如 IP 地址和 Google 账号 ID）都会在记录之前清除。生成的记录会被标记为已清理，并且不包含任何可识别的用户数据，确保与 Gemini Enterprise Agent Platform 零数据保留保持一致。
- **依托 Google 搜索进行接地**：如[Gemini API 附加
  服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn#grounding-with-google-search)中所述，Google
  会存储提示、上下文信息和生成的输出内容三十 (30)
  天，以用于创建有依据的结果和搜索建议。
  这些存储的信息可用于调试和测试支持接地的系统。**如果您使用“依托 Google 搜索进行接地”，则无法禁止存储此信息。**
- **Grounding with Google Maps**：如 [Gemini API 附加服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn)中所述，Google 会存储提示、上下文信息和生成的输出内容三十 (30) 天，以用于创建有依据的结果。这些存储的信息可能仅用于可靠性工程，例如在出现服务问题时进行调试。**如果您使用“Grounding with Google Maps”，则无法禁止存储此信息。**
- **Interactions API**：Interactions API 可管理对话的活跃状态，以实现多轮对话。**默认情况下，Interactions API 会启用状态存储** 。为确保零数据足迹，您必须在 API 请求中将 `store` 参数显式设置为 `false`，以选择停用默认状态保留。
- **Live API**：此有状态 API 通过存储
  对话状态来实现实时重新连接。若要实现零数据保留，**请勿配置 SessionResumptionConfig** 。如果生成了会话句柄，对话状态（包括文本、音频和视频）最多会保留 24 小时。
- **File API 存储**：借助 File API，用户可以上传大型素材资源。
  文件会以静态方式存储，直到用户删除或过期为止。
  File API 的使用与 ZDR 日志记录无关；用户必须手动删除文件，以确保零数据足迹。
- **显式上下文缓存**：用户可以使用 `cached_content` 字段手动缓存大型数据集（例如
  长视频或文档库）。虽然这些请求的日志遵循 ZDR 丢弃政策，但缓存的上下文本身会使用用户定义的 `ttl` 或 `expire_time` 进行存储。若要实现绝对零数据足迹，请勿使用 cached\_content 功能。
- **隐式内存缓存**：默认情况下，Gemini 模型会将数据缓存在
  内存中，以缩短延迟时间并降低开发者的费用。此数据严格存储在 RAM 中（而非静态存储），在项目级层进行隔离，并且 TTL 为 24 小时。
  **这不会违反零数据保留。**

## 后续步骤

- 了解[生成式 AI 使用限制
  政策](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-cn)。
- 查看 [Gemini API 附加服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn)。
- 如果您需要企业级自助式 ZDR 控制功能，请参阅 [Gemini Enterprise Agent Platform
  零数据保留
  指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-28。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-28。"],[],[]]
