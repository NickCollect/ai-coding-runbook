---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=zh-CN
fetched_at: 2026-08-10T03:11:56.141613+00:00
title: "Gemini Robotics ER 2 \u6d41\u5f0f\u9884\u89c8\u7248 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Robotics ER 2 流式预览版

Gemini Robotics ER 2 Streaming 是一种机器人视觉语言模型 (VLM)，经过优化，可使用 Live API 进行实时文本流式传输。它接受文本、图片、视频和音频输入，并支持通过函数调用进行双向流式传输。

[在 Google AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=zh-cn)

## 文档

如需全面了解功能，请访问[机器人 Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) 页面。

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card模型代码 | `gemini-robotics-er-2-preview` |
| save支持的数据类型 | **输入**  文本、图片、视频、音频  **输出**  文本 |
| token\_autoToken 限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65,536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用方案 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不支持  **[优先推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不支持 |
| 123版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览版：`gemini-robotics-er-2-preview` |
| calendar\_month最新更新时间 | 2026 年 7 月 |
| id\_card模型卡片 | [模型卡片](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-cn) |

### Gemini Robotics ER 2 Streaming 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card模型代码 | `gemini-robotics-er-2-streaming-preview` |
| save支持的数据类型 | **输入**  文本、图片、视频、音频  **输出**  文本 |
| token\_autoToken 限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65,536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  不支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  不支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  不支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  不支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  不支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  不支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  不支持 |
| speed使用方案 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  不支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不支持  **[优先推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不支持 |
| 123版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览版：`gemini-robotics-er-2-streaming-preview` |
| calendar\_month最新更新时间 | 2026 年 7 月 |
| id\_card模型卡片 | [模型卡片](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-cn) |

### Gemini Robotics ER 1.6 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card模型代码 | `gemini-robotics-er-1.6-preview` |
| save支持的数据类型 | **输入**  文本、图片、视频、音频  **输出**  文本 |
| token\_autoToken 限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65,536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用方案 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不支持  **[优先推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不支持 |
| 123版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览版：`gemini-robotics-er-1.6-preview` |
| calendar\_month最新更新时间 | 2025 年 12 月 |
| cognition\_2知识截点 | 2025 年 1 月 |

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
