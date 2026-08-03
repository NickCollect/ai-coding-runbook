---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=zh-CN
fetched_at: 2026-08-03T04:36:27.342725+00:00
title: "Gemini API \u4e2d\u7684\u89c6\u9891\u751f\u6210 \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini API 中的视频生成

Gemini API 提供两种用于生成视频的模型：[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=zh-cn) 和 [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=zh-cn)。
每种模式都适用于不同的工作流程。

将 Gemini Omni Flash 用作视频生成的默认模型。它可提供出色的视频连贯性、多输入源推理（同时支持文本、图片、音频和视频输入）、角色一致性、事实准确性，以及多轮对话式编辑（例如元素替换或透视变化）。需要使用场景扩展、最后一帧控制或与旧版流水线集成等特定功能。

## Gemini Omni Flash

Gemini Omni Flash 是一款快速的多模态模型，可用于生成视频和进行对话式视频编辑。它擅长快速将文本提示和图片转换为短视频，并允许您使用 Interactions API 在多个回合中优化结果。

[开始使用 Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=zh-cn)

## Veo 3.1

Veo 3.1 是一种可生成包含原生音频的视频的模型。它通过 `generateContent` API 支持视频扩展、帧特定生成和基于图像的指导等功能。

[开始使用 Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=zh-cn)

## 视频理解

如果您需要提取和分析现有视频内容，而不是生成新视频，请参阅[视频理解指南](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-30。"],[],[]]
