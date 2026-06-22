---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-CN
fetched_at: 2026-06-22T06:26:37.680820+00:00
title: "\u901f\u7387\u9650\u5236 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 速率限制

速率限制用于控制您在给定时间范围内可以向 Gemini API 发出的请求数。这些限制有助于确保公平使用、防范滥用行为，并帮助所有用户维持系统性能。

[在 AI Studio 中查看有效速率限制](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=zh-cn)

## 速率限制的运作方式

速率限制通常从以下三个维度进行衡量：

- 每分钟请求数 (**RPM**)
- 每分钟 token 数（输入）(**TPM**)
- 每日请求数 (**RPD**)

我们会根据每项限制评估您的用量，如果超出任何一项限制，系统都会触发速率限制错误。例如，如果您的 RPM 限制为 20，那么在一分钟内发出 21 个请求会导致错误，即使您未超出 TPM 或其他限制也是如此。

速率限制按项目应用，而不是按 API 密钥应用。每天的请求数（**RPD**）配额会在太平洋时间午夜重置。

限额因所用模型而异，并且部分限额仅适用于特定模型。例如，每分钟生成的图片数 (IPM) 仅针对能够生成图片的模型（Nano Banana）计算，但在概念上与 TPM 类似。其他模型可能设有每日 token 数量上限 (TPD)。

实验性模型和预览版模型的速率限制更为严格。

## 使用层级

速率限制与项目的用量层级相关联。随着 API 用量和支出的增加，您将自动升级到具有更高速率限制的更高层级。

第 2 级和第 3 级的资格条件是根据与您的项目相关联的结算账号在 Google Cloud 服务（包括但不限于 Gemini API）上的累计总支出确定的。

| 使用层 | 资格赛 | [结算层级上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#tier-spend-caps) |
| --- | --- | --- |
| **免费** | [有效项目](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#google-cloud-projects)或免费试用 | 不适用 |
| **第 1 层级** | [设置并关联有效的结算账号](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#setup-billing) | $250 |
| **第 2 层级支持人员** | 支付了 100 美元 + 自首次成功付款时起已满 3 天 | 2000 美元 |
| **第 3 层级支持人员** | 支付了 1,000 美元 + 自首次成功付款时起已满 30 天 | 20,000 美元至 100,000 美元以上 |

虽然满足所述资格条件通常足以获得批准，但在极少数情况下，升级申请可能会因审核过程中发现的其他因素而被拒绝。

此系统有助于维护 Gemini API 平台对所有用户的安全性和完整性。

## Gemini API 速率限制

速率限制取决于多种因素（例如您的用量层级），您可以在 Google AI Studio 中查看这些限制。随着您的会员等级和账号状态随时间变化，费率限制会自动更新。

[在 AI Studio 中查看有效速率限制](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=zh-cn)

指定的速率限制无法保证，实际容量可能会有所不同。

## 优先级推理速率限制

[优先](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)消耗量有自己的速率限制，即使该消耗量计入总体互动流量速率限制也是如此。**默认速率限制为：每种模型和层级的[标准速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)的 0.3 倍**

## Batch API 速率限制

[批量 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn) 请求有自己的速率限制，与非批量 API 调用分开。

- **并发批量请求数**：100
- **输入文件大小上限**：2 GB
- **文件存储空间上限**：20 GB
- **每个模型的排队 token 数**：**批量排队 token 数**表格列出了针对给定模型，所有有效批量作业可排队进行批量处理的最大 token 数。

### 第 1 层级

| 模型 | 批量加入队列的 token 数 |
| --- | --- |
| 文本输出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 预览版 | 5000000 |
| Gemini 3.1 Flash-Lite | 1000 万 |
| Gemini 3.1 Flash-Lite 预览版 | 1000 万 |
| Gemini 3.5 Flash | 3,000,000 |
| Gemini 3.5 Flash | 3,000,000 |
| Gemini 2.5 Pro | 5000000 |
| Gemini 2.5 Pro TTS | 25000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash 预览版 | 3,000,000 |
| Gemini 2.5 Flash Image 预览版 | 3,000,000 |
| Gemini 2.5 Flash TTS | 100000 |
| Gemini 2.5 Flash-Lite | 1000 万 |
| Gemini 2.5 Flash-Lite 预览版 | 1000 万 |
| Gemini 2.0 Flash | 1000 万 |
| Gemini 2.0 Flash 图片 | 3,000,000 |
| Gemini 2.0 Flash-Lite | 1000 万 |
| 多模态生成模型 | | | | |
| Gemini 3.1 Flash Image 预览版 🍌 | 100 万 |
| Gemini 3 Pro Image 预览版 🍌 | 200 万 |
| 嵌入模型 | | | | |
| Gemini Embedding | 50 万 |

### 第 2 层级

| 模型 | 批量加入队列的 token 数 |
| --- | --- |
| 文本输出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 预览版 | 500,000,000 |
| Gemini 3.1 Flash-Lite | 500,000,000 |
| Gemini 3.1 Flash-Lite 预览版 | 500,000,000 |
| Gemini 3.5 Flash | 400,000,000 |
| Gemini 3.5 Flash | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash 预览版 | 400,000,000 |
| Gemini 2.5 Flash Image 预览版 | 400,000,000 |
| Gemini 2.5 Flash TTS | 100000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.5 Flash-Lite 预览版 | 500,000,000 |
| Gemini 2.0 Flash | 10 亿 |
| Gemini 2.0 Flash 图片 | 400,000,000 |
| Gemini 2.0 Flash-Lite | 10 亿 |
| 多模态生成模型 | | | | |
| Gemini 3.1 Flash Image 预览版 🍌 | 250,000,000 |
| Gemini 3 Pro Image 预览版 🍌 | 270,000,000 |
| 嵌入模型 | | | | |
| Gemini Embedding | 5000000 |

### 第 3 级

| 模型 | 批量加入队列的 token 数 |
| --- | --- |
| 文本输出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 预览版 | 10 亿 |
| Gemini 3.1 Flash-Lite | 10 亿 |
| Gemini 3.1 Flash-Lite 预览版 | 10 亿 |
| Gemini 3.5 Flash | 10 亿 |
| Gemini 3.5 Flash | 10 亿 |
| Gemini 2.5 Pro | 10 亿 |
| Gemini 2.5 Pro TTS | 100 万 |
| Gemini 2.5 Flash | 10 亿 |
| Gemini 2.5 Flash 预览版 | 10 亿 |
| Gemini 2.5 Flash Image 预览版 | 10 亿 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash-Lite | 10 亿 |
| Gemini 2.5 Flash-Lite 预览版 | 10 亿 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash 图片 | 10 亿 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| 多模态生成模型 | | | | |
| Gemini 3.1 Flash Image 预览版 🍌 | 750,000,000 |
| Gemini 3 Pro Image 预览版 🍌 | 10 亿 |
| 嵌入模型 | | | | |
| Gemini Embedding | 1000 万 |

## 如何升级到更高级别

如需从免费层级过渡到付费层级，您必须先[在 AI Studio 中设置结算信息](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。

一旦您的项目满足[指定条件](#usage-tiers)，系统便会自动将其升级到下一层级。从免费层级升级到第 1 层级通常会立即生效，而后续的层级升级会在 10 分钟内生效。前往 AI Studio 中的[“项目”页面](https://aistudio.google.com/projects?hl=zh-cn)，查看您的层级。

## 申请提高速率限制

每种模型变体都有关联的速率限制（每分钟请求数，RPM）。
如需详细了解这些速率限制，请参阅 [AI Studio 速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)页面。

[申请提高付费层级的速率限制](https://forms.gle/ETzX94k8jf7iSotH9)

我们无法保证一定会提高您的速率限制，但会尽力审核您的请求。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-28。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-28。"],[],[]]
