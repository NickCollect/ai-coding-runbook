---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-CN
fetched_at: 2026-10-19T05:47:29.117597+00:00
title: "\u6392\u67e5 Google AI Studio \u95ee\u9898 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 排查 Google AI Studio 问题

本页提供了一些建议，可帮助您在遇到问题时排查 Google AI Studio 的问题。

## 了解 403 访问受限错误

如果您看到 403 访问受限错误，则表示您使用 Google AI Studio 的方式不符合[服务条款](https://ai.google.dev/terms?hl=zh-cn)。一个常见原因是
您所在的地区不受[支持](https://ai.google.dev/available_regions?hl=zh-cn)。

## 解决 Google AI Studio 上“无内容”响应的问题

如果内容因任何原因被屏蔽，
Google AI Studio 上会显示warning **无内容** 消息。如需查看更多详细信息，
请将指针悬停在 **无内容** 上，然后点击
warning **安全**。

如果响应因[安全设置](https://ai.google.dev/docs/safety_setting?hl=zh-cn)而被屏蔽，并且
您已考虑了用例的[安全风险](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-cn)，则您
可以修改
[安全设置](https://ai.google.dev/docs/safety_setting?hl=zh-cn#safety_settings_in_makersuite)
以影响返回的响应。

如果响应被屏蔽但不是因为安全设置，则查询或
响应可能违反了[服务条款](https://ai.google.dev/terms?hl=zh-cn)，或者不受支持。

## 检查 token 使用情况和限制

当您打开提示时，屏幕底部的**文本预览** 按钮会显示当前用于提示内容的 token 数，以及所用模型的最大 token 数。

## AI Studio 的 Google Cloud IAM 权限

Google Cloud 项目的成员需要特定的 Identity and Access Management (IAM) 权限才能在 Google AI Studio 中执行操作。如需详细了解这些身份，请参阅 [IAM 主账号概览](https://docs.cloud.google.com/iam/docs/principals-overview?hl=zh-cn)。

在关联的 Google Cloud 项目中具有**编辑者** 或**所有者** 角色的用户拥有查看信息中心和管理 Gemini API 密钥的完整权限。具有**查看者** 角色的用户可以查看信息中心和 API 密钥，但无法创建、更新或删除它们。

如需进行更精细的控制，请参阅下表，了解每个 AI Studio 功能所需的特定权限。如需了解如何授予这些权限，请参阅 Google Cloud 文档中的[授予、更改和撤消对资源的访问权限](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=zh-cn)。

| AI Studio 功能 | 必需的 IAM 权限 | 其他要求 |
| --- | --- | --- |
| **搜索项目** （导入项目） | `resourcemanager.projects.get` |  |
| **重命名项目** | `resourcemanager.projects.update` |  |
| **显示配额层级** | 不适用 |  |
| **创建 API 密钥** | 拥有**搜索项目** 权限，并且：  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **列出 API 密钥** | 拥有**搜索项目** 权限，并且：  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud 项目必须启用 [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=zh-cn)。 |
| **重命名 API 密钥** | `apikeys.keys.update` |  |
| **删除 API 密钥** | `apikeys.keys.delete` |  |
| **使用情况信息中心** | 拥有**搜索项目** 权限，并且：  `monitoring.timeSeries.list` |  |
| **速率限制信息中心** | 拥有**使用情况信息中心** 权限，并且：  `cloudquotas.quotas.get` |  |
| **支出（结算上限）** | `billing.resourceCosts.get`（查看支出） `billing.resourcebudgets.read`（查看上限） `billing.resourcebudgets.write`（设置上限） |  |
| **结算信息中心** | `billing.accounts.get` |  |

### 其他访问权限检查

除了 Google Cloud IAM 权限之外，AI Studio 还会执行安全和合规性检查。如果您不符合以下要求，可能会在 AI Studio 界面或 API 响应中遇到 `PERMISSION_DENIED` 或访问限制错误：

- **安全检查**： 您的请求必须通过自动化安全检查。
- **服务条款**： 您必须接受《Google 服务条款》和《生成式 AI 附加服务条款》。
- **受支持的区域**： 您必须位于[受支持的区域](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-cn)。
- **信任与安全**： Google Cloud 项目不得因滥用行为而被标记。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
