---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-CN
fetched_at: 2026-09-21T05:58:19.208201+00:00
title: "\u95ee\u9898\u6392\u67e5\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 问题排查指南

本指南可帮助您诊断和解决调用 Gemini API 时出现的常见问题。您可能会遇到来自 Gemini API 后端服务或客户端 SDK 的问题。我们的客户端 SDK 在以下代码库中开源：

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

如果您遇到 API 密钥问题，请按照 [API 密钥设置指南](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)验证您是否已正确设置 API 密钥。

## 错误代码

如需查看所有错误代码（包括 HTTP 状态代码、生成内容遭拒代码和内容错误代码）的完整参考文档，请参阅 [API 错误](https://ai.google.dev/gemini-api/docs/api-errors?hl=zh-cn)页面。

## 重试策略

如果您收到指示您应重试请求的错误（例如 `429 RESOURCE_EXHAUSTED` 或 `503 UNAVAILABLE`），我们建议您实现指数退避算法。这意味着您会在第一次重试之前等待一小段时间，然后逐渐增加后续重试之间的等待时间。

Gemini API 的官方客户端 SDK（例如 [Python SDK](https://github.com/googleapis/python-genai)）默认包含指数退避算法自动重试逻辑，用于处理暂时性错误，例如超时、网络问题和速率限制（`429` 和 `5xx` 状态代码）。例如，Python SDK 会自动重试暂时性错误，最多重试 4 次，初始延迟时间约为 1 秒，最长延迟时间为 60 秒。

如果您要直接发出 REST API 请求或自定义重试逻辑，请遵循以下最佳实践，以提高请求成功率并防止服务过载：

- **使用指数退避算法**：在第一次重试之前等待一小段时间（例如 1 秒），然后以指数方式增加延迟时间（例如 2 秒、4 秒、8 秒）。
- **添加抖动**：在延迟中添加随机“抖动”，以帮助防止所有客户端在完全相同的时间重试。
- **针对特定错误进行重试**：仅针对暂时性错误（例如 `429`、`408` 或 `5xx`）进行重试。请勿针对客户端错误（例如 `400`、`402` 或 `403`）进行重试，因为这些错误表示存在无效的 API 密钥、预付款用完或语法错误等问题。
- **设置重试次数上限**：定义重试次数上限，以防止无限循环。

## 检查 API 调用是否存在模型参数错误

验证模型参数是否在以下值范围内：

|  |  |
| --- | --- |
| **模型形参** | **值（范围）** |
| 候选对象数量 | 1-8（整数） |
| 温度 | 0.0-1.0 |
| 输出 token 数量上限 | 您可以使用[模型页面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)确定所用模型的词元数量上限。 |
| TopP | 0.0-1.0 |

除了检查参数值之外，还要确保您使用的是正确的 [API 版本](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-cn)（例如 `/v1` 或 `/v1beta`）和支持所需功能的型号。例如，如果某项功能处于 Beta 版发布阶段，则仅在 `/v1beta` API 版本中可用。

## 检查您是否拥有合适的型号

确认您使用的是我们[模型页面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)上列出的受支持型号。

## 使用思考模型时延迟时间更长或 token 用量更高

延迟时间或 token 用量之所以会增加，通常是因为 Gemini 3.x 模型默认启用了思考功能。已弃用的 Gemini 2.5 模型也使用默认思考模式。

思考模型会生成内部推理令牌，以提高质量。这种推理过程会增加响应延迟时间和总令牌消耗量。

如果您优先考虑降低延迟时间或需要最大限度地降低费用，可以降低思考水平或关闭思考功能。

如需了解配置详情和查看代码示例，请参阅[思维指南](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#thinking-levels)。

## 安全问题

如果您看到系统提示某个提示因 API 调用中的安全设置而被屏蔽，请根据您在 API 调用中设置的过滤条件检查该提示。

如果您看到 `BlockedReason.OTHER`，则表示相应查询或回答可能违反了[服务条款](https://ai.google.dev/terms?hl=zh-cn)，或者不受支持。

## 朗诵问题

如果您发现模型因“RECITATION”原因而停止生成输出，则表示模型输出可能与某些数据相似。如需解决此问题，请尽量使提示 / 上下文保持唯一性，并使用较高的温度。

## 重复令牌问题

如果您看到重复的输出令牌，请尝试以下建议，以帮助减少或消除这些令牌。

| 说明 | 原因 | 建议的解决方法 |
| --- | --- | --- |
| Markdown 表格中的连字符重复出现 | 如果表格内容较长，模型会尝试创建视觉上对齐的 Markdown 表格，此时可能会出现这种情况。不过，Markdown 中的对齐方式对于正确渲染而言并非必需。 | 在提示中添加说明，为模型提供有关生成 Markdown 表格的具体指南。提供符合这些准则的示例。您还可以尝试调节温度。对于生成代码或 Markdown 表格等结构化程度很高的输出，较高的温度值（>= 0.8）效果更好。  以下是一组您可以添加到提示中的准则示例，以防止出现此问题：     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Markdown 表格中的重复令牌 | 与重复的连字符类似，当模型尝试直观地对齐表格内容时，就会出现这种情况。Markdown 中的对齐方式不是正确渲染的必要条件。 | - 尝试向系统提示添加以下指令：      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 尝试调整温度。较高的温度（>= 0.8）通常有助于消除输出中的重复或重复内容。 |
| 结构化输出中存在重复的换行符 (`\n`) | 当模型输入包含 Unicode 或转义序列（例如 `\u` 或 `\t`）时，可能会导致出现重复的换行符。 | - 检查提示中是否存在禁止使用的转义序列，并将其替换为 UTF-8 字符。例如，JSON 示例中的 `\u` 转义序列可能会导致模型也在其输出中使用这些序列。 - 指示模型允许的转义。添加如下所示的系统指令：      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 使用结构化输出时文本重复 | 如果模型输出的字段顺序与定义的结构化架构不同，可能会导致文本重复。 | - 请勿在提示中指定字段的顺序。 - 将所有输出字段设为必需字段。 |
| 重复的工具调用 | 如果模型丢失了之前想法的上下文，并且/或者调用了它被迫调用的不可用端点，就可能会出现这种情况。 | 指示模型在思考过程中保持状态。 将以下内容添加到系统指令的末尾：    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 不属于结构化输出的重复文本 | 如果模型卡在无法解决的请求上，就会出现这种情况。 | - 如果开启了思考功能，请避免在指令中明确指示如何思考问题。只需要求提供最终输出即可。 - 尝试将温度调高到 0.8 或更高。 - 添加“简洁明了”“不要重复”或“只提供一次答案”等指令。 |

## 已遭屏蔽或无法正常使用的 API 密钥

本部分介绍了如何检查 Gemini API 密钥是否被屏蔽，以及如何处理这种情况。

### 了解密钥被屏蔽的原因

我们发现了一个漏洞，导致部分 API 密钥可能已公开泄露。为了保护您的数据并防止未经授权的访问，我们已主动阻止这些已知泄露的密钥访问 Gemini API。

### 确认您的密钥是否会受到影响

如果您的密钥被泄露，您将无法再将该密钥与 Gemini API 搭配使用。您可以使用 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-cn) 查看是否有任何 API 密钥被禁止调用 Gemini API，并生成新密钥。尝试使用这些密钥时，您可能还会看到系统返回以下错误：

```
Your API key was reported as leaked. Please use another API key.
```

### 针对被屏蔽的 API 密钥采取的操作

您应使用 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-cn) 为 Gemini API 集成生成新的 API 密钥。我们强烈建议您检查 API 密钥管理实践，确保新密钥安全无虞，不会公开。

### 因存在漏洞而产生的意外费用

[提交结算支持请求](https://console.cloud.google.com/support/chat?hl=zh-cn)。
我们的结算团队正在处理此问题，我们会尽快通知您最新进展。

### Google 针对泄露密钥采取的安全措施

**如果我的 API 密钥泄露，Google 将如何帮助我保护账号免遭费用超支和滥用？**

- 我们正逐步过渡到以下模式：当您使用 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-cn) 请求新密钥时，系统会签发 API 密钥，该密钥默认仅限用于 Google AI Studio，且不接受来自其他服务的密钥。这有助于防止任何意外的跨密钥使用。
- 我们默认会屏蔽泄露并与 Gemini API 一起使用的 API 密钥，以帮助防止滥用费用和应用数据。
- 您将能够在 [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=zh-cn) 中查看 API 密钥的状态，并且当我们发现您的 API 密钥泄露时，我们会主动通知您立即采取行动。

## 改进模型输出

如需获得更高质量的模型输出，请尝试撰写结构更清晰的提示。[提示工程指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn)页面介绍了一些基本概念、策略和最佳实践，可帮助您入门。

## 了解令牌限制

请仔细阅读我们的 [Token 指南](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)，更好地了解如何统计 token 及其限制。

## 已知问题

- 该 API 仅支持部分精选语言。以不支持的语言提交提示可能会生成意外甚至被屏蔽的回答。如需了解最新信息，请参阅[支持的语言](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#supported-languages)。

## 提交 bug

如果您有任何疑问，请加入 [Google AI 开发者论坛](https://discuss.ai.google.dev?hl=zh-cn)参与讨论。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-20。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-20。"],[],[]]
