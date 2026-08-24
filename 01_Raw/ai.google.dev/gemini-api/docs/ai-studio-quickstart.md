---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=zh-CN
fetched_at: 2026-08-24T02:26:51.508632+00:00
title: "Google AI Studio \u5feb\u901f\u5165\u95e8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Google AI Studio 快速入门

[Google AI Studio](https://aistudio.google.com/?hl=zh-cn) 让您可以快速尝试
各种模型，使用不同的提示进行试验。准备好构建后，您
可以选择“获取代码”和首选编程语言，以
使用 [Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn)。

## 提示和设置

Google AI Studio 提供了多个提示界面，这些界面专为不同的使用场景而设计。本指南介绍了用于打造
对话式体验的**聊天提示**。这种提示技术允许多次输入
和响应，以生成输出。您可以参阅下面的
[聊天提示示例了解详情](#chat_example)。
其他选项包括**实时流式传输**、**视频生成**等
。

AI Studio 还提供了 **运行设置** 面板，您可以在其中调整 [模型参数](https://ai.google.dev/docs/prompting-strategies?hl=zh-cn#model-parameters)、[安全设置](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)，以及开启 [结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)、[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)、[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)和 [接地](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)等工具。

## 聊天提示示例：构建自定义聊天应用

如果您使用过
[Gemini](https://gemini.google.com/?hl=zh-cn)等通用聊天机器人，那么您一定亲身体验过
生成式 AI 模型在开放式对话中的强大功能。虽然这些通用聊天机器人很有用，但通常需要针对特定使用场景进行定制。

例如，您可能想要构建一个客户服务聊天机器人，该机器人仅支持有关公司产品的对话。您可能想要构建一个以特定语气或风格说话的聊天机器人：一个会讲很多笑话、像诗人一样押韵或在回答中使用大量表情符号的机器人。

此示例向您展示了如何使用 Google AI Studio 构建一个友好的聊天机器人，该机器人会像居住在木星卫星欧罗巴上的外星人一样进行交流。

### 第 1 步 - 创建聊天提示

如需构建聊天机器人，您需要提供用户与聊天机器人之间互动的示例，以引导模型提供您所需的响应。

如需创建聊天提示，请执行以下操作：

1. 打开 [Google AI Studio](https://aistudio.google.com/?hl=zh-cn)。默认情况下，**游乐场** 会打开并显示新的聊天提示。
2. 点击右上角的**运行设置** tune以展开面板，然后找到[**系统指令**](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#system-instructions)输入字段。将以下内容粘贴到文本输入字段中：

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

添加系统指令后，通过与模型聊天来开始测试您的应用：

1. 在标有**输入内容...**的文本输入框中，输入用户可能会提出的问题或
   意见。例如：

   **用户**：

   ```
   What's the weather like?
   ```
2. 点击**运行** 按钮以获取聊天机器人的响应。此响应可能类似于以下内容：

   **模型**：

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### 第 2 步 - 教您的机器人更好地聊天

通过提供一条指令，您就能够构建一个基本的欧罗巴外星人聊天机器人。但是，一条指令可能不足以确保模型响应的一致性和质量。如果没有更具体的指令，模型对有关天气的问题的响应往往会很长，并且可能会自行其是。

通过向系统指令添加内容来自定义聊天机器人的语气：

1. 开始新的聊天提示，或使用相同的聊天提示。聊天会话开始后，系统指令可以修改。
2. 在**系统指令** 部分中，将您已有的指令更改为以下内容：

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. 重新输入您的问题（`What's the weather like?`），然后点击**运行**
   按钮。如果您没有开始新的聊天，您的响应可能如下所示：

   **模型**：

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

您可以使用这种方法为聊天机器人添加更多深度。提出更多问题、修改答案并提高聊天机器人的质量。继续添加或修改指令，并测试它们如何改变聊天机器人的行为。

### 第 3 步 - 后续步骤

与其他提示类型类似，在您对提示原型感到满意后，可以使用**获取代码** 按钮开始编码，也可以保存提示以供日后使用并与他人分享。

## 深入阅读

- 如果您已准备好开始编码，请参阅 [API
  快速入门指南](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn)。
- 如需了解如何编写更好的提示，请查看[提示设计
  指南](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
