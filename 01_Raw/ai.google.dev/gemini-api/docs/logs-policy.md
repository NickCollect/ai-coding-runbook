---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-CN
fetched_at: 2026-07-06T05:06:23.399536+00:00
title: "\u6570\u636e\u8bb0\u5f55\u548c\u5171\u4eab \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 数据记录和共享

本页面概述了 [Gemini API 日志](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)的存储和管理，这些日志是已启用结算功能的项目中受支持的 Gemini API 调用的开发者自有 API 数据。日志涵盖了从用户提出请求到模型做出回答的整个过程。

## 1. 可共享的数据

作为项目所有者，您可以选择启用 Gemini API 调用日志记录功能，以便自行使用或向 Google 提供反馈和分享信息，帮助我们不断改进模型。

启用日志记录后，您可以选择贡献以下数据，帮助我们构建对各个领域和用例的开发者都持续有价值的 AI 系统，以改进产品和模型训练：

- **数据集**：使用 Google AI Studio 的“日志和数据集”界面，从受支持的 Gemini API 调用中选择感兴趣的日志（请求、响应、元数据等）；通过包含在数据集中贡献，并在创建数据集期间可以选择退出。
- **反馈**：查看日志时，您可以提供反馈，包括点赞/点踩评分以及您提供的任何书面评论。

如果您与 Google 分享数据集，系统会根据我们针对“[无偿服务](https://ai.google.dev/gemini-api/terms?hl=zh-cn#data-use-unpaid)”的[条款](https://developers.google.com/terms?hl=zh-cn)处理该数据集中的日志（包括请求和响应），这意味着该数据集可能会用于开发和改进 Google 产品、服务和机器学习技术，包括改进和训练我们的模型。**请勿包含个人信息、敏感信息或机密信息。**

## 2. 我们会如何使用您的数据

默认情况下，日志会在 55 天后过期。在此期限过后，这些功能将无法使用。您可以创建数据集，以保留此期限之外的感兴趣或有价值的日志，供下游使用情形使用，并可选择性地为模型改进做出贡献。存储在数据集中的日志没有设置过期日期，但每个项目的默认存储空间上限为 1,000 条日志。

默认情况下，由于日志记录仅适用于已启用结算的项目，因此日志中的提示和回答不会用于产品改进或开发，这符合我们关于数据使用的[条款](https://developers.google.com/terms?hl=zh-cn)。

如果您选择与 Google 分享日志数据集，这些数据集将用作实际演示数据，以便更好地了解 AI 系统和应用所使用的网域和上下文的多样性。这些数据可能会用于提高模型质量，并为未来模型和服务的训练和评估提供信息。我们会根据[免费服务](https://ai.google.dev/gemini-api/terms?hl=zh-cn#data-use-unpaid)的数据使用条款处理这些数据。
因此，人工审核员可能会读取、批注和处理您分享的 API 输入和输出。在将数据用于改进模型之前，Google 会在此过程中采取措施来保护用户隐私。其中包括消除这些数据与您的 Google 账号、API 密钥和云项目的关联，然后才允许审核员查看或添加注释。

## 3. 数据权限

选择贡献 API 数据即表示您确认，您已授予 Google 必要权限，以便 Google 能够按照本文档中的说明处理和使用这些数据。**请勿提供包含通过付费服务获得的敏感信息、机密信息或专有信息的日志**。您根据 API 条款中“[提交内容](https://developers.google.com/terms?hl=zh-cn#b_submission_of_content)”部分向 Google 授予的许可还扩展到您提交给本服务的任何内容（例如提示，包括关联的系统指令、缓存的内容和文件，如图片、视频或文档）以及任何生成的回答，但仅限在适用法律要求我们使用这些内容时。

## 4. 数据共享和反馈

您可以选择分享数据作为示例，帮助我们推进 AI 研究、Gemini API 和 Google AI Studio 的前沿发展，从而使我们能够不断改进各种情境下的模型，并构建在各种领域和使用情形下对开发者都持续有价值的 AI 系统。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-01。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-01。"],[],[]]
