---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=zh-CN
fetched_at: 2026-05-18T05:14:39.643685+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 上下文缓存

在典型的 AI 工作流程中，您可能会反复将相同的输入令牌传递给模型。Gemini API 提供隐式缓存，以优化性能和成本。

## 隐式缓存

对于所有 Gemini 2.5 及更新型号，隐式缓存默认处于启用状态。如果您的请求命中缓存，我们会自动将节省的费用返还给您。您无需执行任何操作即可启用此功能。下表列出了每种模型进行上下文缓存所需的最低输入 token 数：

| 模型 | 最低 token 限制 |
| --- | --- |
| Gemini 3 Flash 预览版 | 1024 |
| Gemini 3 Pro 预览版 | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

如要提高隐式缓存命中的几率，可以：

- 尝试将较大且常见的内容放置在提示的开头
- 尝试在短时间内发送具有相似前缀的请求

您可以在回答对象的 `usage_metadata` (Python) 或 `usageMetadata` (JavaScript) 字段中查看缓存命中的 token 数量。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-07。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-07。"],[],[]]
