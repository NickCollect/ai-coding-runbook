---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=zh-CN
fetched_at: 2026-09-07T05:37:08.013536+00:00
title: "\u5c06\u5de5\u5177\u4e0e Gemini API \u642d\u914d\u4f7f\u7528 \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 将工具与 Gemini API 搭配使用

工具扩展了 Gemini 模型的功能，使其能够在现实世界中采取行动、访问实时信息并执行复杂的计算任务。模型可以通过 [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=zh-cn) 在标准请求-响应互动和实时流式传输会话中使用工具。

工具是模型可用于回答查询的特定功能（例如 Google 搜索或代码执行）。Gemini API 提供了一套全托管式内置工具，您也可以使用[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)定义自定义工具。

如需构建多步骤、以目标为导向的系统，请参阅[代理概览](https://ai.google.dev/gemini-api/docs/agents?hl=zh-cn)。

## 可用的内置工具

| 工具 | 说明 | 使用场景 |
| --- | --- | --- |
| [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn) | 以当前事件和网络上的事实为依据来提供回答，从而减少幻觉。 | 回答有关近期事件的问题，通过各种来源验证事实。 |
| [Google 地图](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn) | 构建位置感知助理，该助理可以查找地点、获取路线，并提供丰富的本地背景信息。 | 规划包含多个经停点的旅游行程，根据用户条件查找本地商家。 |
| [代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn) | 允许模型编写和运行 Python 代码，以准确解决数学问题或处理数据。 | 解决复杂的数学方程式，精确处理和分析文本数据。 |
| [网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn) | 指示模型读取和分析特定网页或文档中的内容。 | 根据特定网址或文档回答问题，检索不同网页中的信息。 |
| [计算机使用（预览版）](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn) | 使 Gemini 能够查看屏幕并生成与 Web 浏览器界面互动的操作（客户端执行）。 | 自动执行重复性基于 Web 的工作流，测试 Web 应用界面。 |
| [文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn) | 为自己的文档编制索引并进行搜索，以启用检索增强生成 (RAG)。 | 搜索技术手册，基于专有数据回答问题。 |

如需详细了解与特定工具相关的费用，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#pricing_for_tools)。

## 工具执行方式

借助工具，模型可以在对话期间请求执行操作。具体流程因工具是内置（由 Google 管理）还是自定义（由您管理）而有所不同。

### 内置工具流程

对于内置工具（Google 搜索、Google 地图、网址上下文、文件搜索、代码执行），整个流程都在一次 API 调用中完成：

1. **您**发送提示：“GOOG 最新股价的平方根是多少？”
2. **Gemini** 确定需要使用工具，并在 Google 的服务器上执行这些工具（例如，搜索股票价格，然后运行 Python 代码来计算平方根）。
3. **Gemini** 会根据工具结果发送最终答案。

### 自定义工具流程（函数调用）

对于自定义工具和“计算机使用”，您的应用会处理执行：

1. **您**发送提示以及函数（工具）声明。
2. **Gemini** 可能会发回结构化 JSON 来调用特定函数（例如 `{"name": "get_order_status", "args": {"order_id": "123"}}`），并且始终带有唯一的 `id`。
3. **您**可以在应用或环境中执行该函数。
4. **您**将函数结果（与函数调用具有相同的 `id`）发送回 Gemini。
5. **Gemini** 会使用这些结果来生成最终回答或其他工具调用。

如需了解详情，请参阅[函数调用指南](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)。

### 结合使用内置工具和自定义工具的流程

对于结合使用内置工具和自定义工具（函数调用）的请求，模型会使用[工具上下文循环](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)来协调不同环境中的执行：

1. **您**发送提示并声明要启用的内置工具和自定义函数，同时设置一个标志以开启组合支持。
2. **Gemini** 会执行内置工具，并在生成任何客户端函数调用时将控制权交给用户（先执行哪个取决于提示和模型做出的决定）。它会返回包含以下内容的响应：
   - 确认工具调用
   - 工具响应的结果（如果模型生成了两个并行函数调用，则此结果可能位于 JSON 之后）
   - 用于调用函数的结构化 JSON
   - 加密的思考特征，用于保留上下文
3. **您**可以在应用或环境中执行该函数。
4. **您**返回 Gemini 回答的所有部分，以及您的函数调用结果。
5. **Gemini** 会使用所有组合的上下文生成最终回答。

请参阅[工具组合指南](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)，了解如何启用对内置工具和自定义工具组合的支持，以及上下文循环的示例。

## 结构化输出与函数调用

Gemini 提供了两种生成结构化输出的方法。当模型需要通过连接到您自己的工具或数据系统来执行中间步骤时，请使用[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)。如果您严格要求模型的最终回答遵循特定架构（例如用于呈现自定义界面），请使用[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)。

## 使用工具生成结构化输出

您可以将[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)与内置工具相结合，以确保基于外部数据或计算的模型回答仍遵循严格的架构。

如需查看代码示例，请参阅[使用工具生成结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=zh-cn#structured_outputs_with_tools)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-08-19。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-08-19。"],[],[]]
