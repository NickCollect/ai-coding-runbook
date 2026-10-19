---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-CN
fetched_at: 2026-10-19T05:56:02.240746+00:00
title: "\u6570\u636e\u8bb0\u5f55\u548c\u5171\u4eab \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 数据记录和共享

本页面概述了
[Gemini API 日志](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)的存储和管理。这些日志是已启用结算功能的项目的受支持 Gemini API 调用的开发者拥有的
API 数据。日志涵盖了从用户请求到模型响应的整个过程。
这些日志是您的 Google Cloud 项目的私有日志，与仅出于 [滥用行为监控](https://ai.google.dev/gemini-api/docs/usage-policies?hl=zh-cn)目的而保留的任何
日志
分开。

## 可共享的数据

作为 Project Owner，您可以选择启用 Gemini API 调用的日志记录功能，以供自己使用，或用于向 Google 提供反馈和共享数据，帮助我们不断改进模型。

启用日志记录功能后，您可以选择贡献以下数据，以改进产品和训练模型，帮助我们构建对各个领域和用例的开发者都持续有价值的 AI 系统：

- **数据集**： 使用 Google AI Studio 的“日志和数据集”界面，从受支持的 Gemini API 调用中选择您感兴趣的日志（请求、响应、元数据等）；通过包含在数据集中贡献，并且可以在创建数据集期间选择退出。
- **反馈**： 查看日志时，您可以提供反馈，包括点赞和踩的评分以及您提供的任何书面评论。

[当您与 Google 共享数据集时，该数据集中的日志（包括
请求和响应）将按照我们的
[“非付费服务”](https://developers.google.com/terms?hl=zh-cn)条款进行处理，这意味着该数据集可能会用于开发和改进 Google
产品、服务和机器学习技术，包括改进和
训练我们的模型。](https://ai.google.dev/gemini-api/terms?hl=zh-cn#data-use-unpaid)**请勿包含个人信息、敏感信息或机密信息。**

## 我们如何使用您的数据

日志的默认最长保留期限为 55 天。在此期限之后，日志会自动标记为待删除。您可以在 AI Studio
中更新项目的存储保留期限，以便在 7 天、14 天、28 天或 55 天后自动将日志标记为待删除。

[您可以创建数据集](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)，以便在设定的保留期限之外保留您感兴趣的日志
，以用于下游用例，并选择贡献数据以改进模型。存储在数据集中的日志没有设定的保留期限。

默认情况下，由于日志记录功能仅适用于已启用结算功能的项目，
因此日志中的提示和响应不会用于产品改进或
开发，这符合我们的 [数据使用条款](https://developers.google.com/terms?hl=zh-cn)
。

如果您选择与 Google 共享日志数据集，这些数据集将用作真实演示数据，以便我们更好地了解 AI 系统和应用所使用的各种领域和情境。这些数据可能会用于提高模型质量，并为未来模型和服务的训练和评估提供信息。这些数据将按照我们的[非付费服务](https://ai.google.dev/gemini-api/terms?hl=zh-cn#data-use-unpaid)数据使用
条款进行处理。

因此，人工审核员可能会阅读、批注和处理您共享的 API 输入和输出。在将数据用于模型改进之前，Google
会在此过程中采取措施保护用户隐私， 包括在审核员看到数据或添加批注前，先解除这些数据与您的 Google 账号、API 密钥和云项目的关联。

## 数据权限

选择接受贡献 API 数据即表示您确认已授予 Google 处理和使用本文档中所述数据的必要权限。**请勿贡献包含通过付费服务获得的敏感信息、机密信息或专有信息的日志**
。
您按照 API 条款中的“[内容提交](https://developers.google.com/terms?hl=zh-cn#b_submission_of_content)”部分向 Google 授予的许可的适用范围，将在与我们的使用行为相关的适用法律要求的范围内，延伸至您提交给这些服务的任何内容（例如提示，包括关联的系统说明、缓存的内容以及图片、视频或文档等文件）以及任何生成的回答。

## 数据共享和反馈

您可以选择接受共享数据作为示例，帮助我们推进 AI 研究前沿、Gemini API 和 Google AI Studio，以便我们不断改进各种情境下的模型，并构建对各个领域和用例的开发者都持续有价值的 AI 系统。

### Gemini API Contributor 层级

通过 Gemini Contributor 层级，开发者可以获得部分模型的代币费用折扣，以换取使用这些模型的数据来提供、改进和开发 Google
产品、服务和机器学习技术的权限。

开发者可以获得部分模型高达 50% 的代币费用折扣，同时享受与[标准 API](https://ai.google.dev/gemini-api/docs/optimization?hl=zh-cn)相同的
实时性能。支持的模型如下：

| 模型 | Contributor 层级 |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-4-argon) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.8-flash) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-3.5-flash-lite) | ✔️ |

**数据使用**：

- 为项目启用 Contributor 层级后，您在项目中使用参与
  模型的数据将按照我们的
  “[非付费服务](https://ai.google.dev/gemini-api/terms?hl=zh-cn#unpaid-services)”
  条款使用。由于您的数据将用于改进 Google 产品和机器学习技术，因此请勿提交敏感信息或个人信息。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-14。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-14。"],[],[]]
