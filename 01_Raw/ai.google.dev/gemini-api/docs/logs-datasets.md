---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-CN
fetched_at: 2026-05-05T20:47:05.726948+00:00
title: "\u65e5\u5fd7\u548c\u6570\u636e\u96c6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 日志和数据集

本指南包含开始为现有 Gemini API 应用启用日志记录所需的一切信息。在本指南中，您将了解如何在 Google AI Studio
信息中心内查看现有或新应用的日志，以便更好地了解模型行为以及用户与应用互动的方式。使用日志记录来观察、调试，并 *选择性地与 Google
分享使用情况反馈，以帮助改进 Gemini 在开发者使用场景中的表现*。[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-cn)

所有 `GenerateContent` 和 `StreamGenerateContent` API 调用（包括通过 [OpenAI 兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)端点进行的调用）均受支持。

## 1. 在 Google AI Studio 中启用日志记录

在开始之前，请确保您拥有一个已启用结算功能的项目。

1. 在 Google [AI Studio](https://aistudio.google.com/logs?hl=zh-cn) 中打开“日志”页面。
2. 从下拉菜单中选择您的项目，然后按“启用”按钮，即可默认启用所有请求的日志记录。

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=zh-cn)

您可以为所有项目或特定项目启用或停用日志记录，并随时通过 Google AI Studio 更改这些偏好设置。

## 2. 在 AI Studio 中查看日志

1. 前往 [AI Studio](https://aistudio.google.com/logs?hl=zh-cn)。
2. 选择您已启用日志记录的项目。
3. 您应该会看到日志以反向时间顺序显示在表格中。

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

点击条目即可查看请求和响应对的完整页面视图。您可以检查完整提示、Gemini 的全卷答完的回答以及上一轮的上下文。请注意，每个项目的默认存储空间上限为
1,000 条日志，而未保存在数据集中的日志将在 55 天后过期。如果您的项目达到存储空间上限，系统会提示您删除日志。

## 3. 整理和共享数据集

- 在日志表格中，找到顶部的过滤条件栏，选择要过滤的属性。
- 在过滤后的日志视图中，使用复选框选择全部或部分日志。
- 点击列表顶部显示的“创建数据集”按钮。
- 为新数据集添加描述性名称和说明（可选）。
- 您将看到刚刚创建的数据集，其中包含整理后的日志集。
- 将数据集导出为 CSV、JSONL 文件或 Google 表格，以进行进一步分析。

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

数据集可用于多种不同的使用场景。

- **整理挑战集**： 推动未来的改进，以解决您希望 AI 改进的领域。
- **整理样本集**： 例如，从实际使用情况中提取样本，以生成来自其他模型的响应；或者收集边缘情况，以便在部署前进行例行检查。
- **评估集**： 这些集合代表了重要功能在实际使用中的情况，可用于与其他模型或系统指令迭代进行比较。

您可以选择将数据集作为演示示例进行分享，从而帮助推动 AI 研究、Gemini API 和 Google AI Studio 的发展。这样，我们就可以在各种背景下改进模型，并创建对许多领域和应用的开发者都有用的 AI 系统

## 后续步骤和测试内容

现在您已启用日志记录，可以尝试以下操作：

- **使用会话记录进行原型设计**： 利用 [AI Studio Build](https://aistudio.google.com/apps?hl=zh-cn) 来编写代码应用，并添加 API 密钥以启用用户日志记录。
- **使用 Gemini Batch API 重新运行日志**： 使用数据集进行响应抽样
  和模型或应用逻辑评估，方法是通过
  [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) 重新运行日志。

## 兼容性

目前不支持以下内容的日志记录：

- Imagen 和 Veo 模型
- Gemini 嵌入模型
- 包含视频、GIF 或 PDF 的输入

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-04-29。"],[],[]]
