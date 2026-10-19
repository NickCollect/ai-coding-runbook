---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=zh-CN
fetched_at: 2026-10-19T05:47:18.962738+00:00
title: "Google AI \u65b9\u6848 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Google AI 方案

在 AI Studio 中使用您的 Google AI 订阅方案。

与免费层级相比，Google AI Pro 和 Ultra 订阅方案提供了更广泛的模型访问权限，并提高了在 AI Studio 中进行原型设计和开发的速率限制。

如需订阅 Google AI 方案，您可以直接在 Google AI Studio 中升级，只需点击左侧导航菜单中的**升级**按钮即可。或者，您也可以访问 [Google AI 方案页面](https://one.google.com/about/google-ai-plans/?hl=zh-cn)进行订阅。

## 概览

订阅 Google AI Pro 和 Ultra 后，开发者可以在 Google AI Studio Playground 中解锁付费模型和更高的速率限制，并使用[构建模式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-cn)中的编码辅助等功能进行氛围编程 (vibe coding)。订阅者可获得高于免费层级的每日基准配额，可在 [Playground](https://aistudio.google.com/prompts/new_chat?hl=zh-cn) 和[构建](https://aistudio.google.com/apps?hl=zh-cn)界面中使用。每日限额通过重置而非滚动时间窗口来强制执行，从而确保在过渡到使用 Cloud Billing 进行生产规模开发之前获得顺畅的开发体验。

| 方案 | AI Studio 用量 | 模型访问权限和福利 |
| --- | --- | --- |
| **免费** | 适中配额 | 基础限额和访问权限，可选择升级以获取更多。 |
| **AI Pro** | 更高配额 | 使用 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-cn)、Gemini Pro、Nano Banana 和 Lyria 等高级模型。 |
| **AI Ultra** | 最高配额 | 在原型设计、开发和使用 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-cn) 等高级前沿模型方面享有最高用量上限。 |

## Gemini API 用量

当 AI Studio 中的每日基准订阅配额用尽时，您可以使用启用了 Cloud Billing 的 Gemini API 密钥继续工作流，直接按请求付费使用 Gemini API。您可以在 [AI Studio 信息中心](https://aistudio.google.com/projects?hl=zh-cn)内查看项目和 API 密钥的 Gemini API 使用情况。

订阅者如果拥有 Google Cloud Platform (GCP) 项目并启用了 Cloud Billing，则有资格通过 [Google 开发者计划](https://developers.google.com/program?hl=zh-cn)每月获得 Cloud 赠金，用于抵扣 Gemini API 等 Cloud 服务的使用费。预付费和后付费的使用和结算方式保持不变。对于采用预付款结算方式的用户，AI Studio 中的付费余额必须大于 0 美元，才能激活赠金。系统将优先抵扣符合条件的 Google Cloud 赠金（如有）。
[了解详情](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#billing-plans)。

Google AI 订阅方案集成降低了高级实验和开发的准入门槛。不过，对于大规模生产部署，建议使用 Google Cloud 项目、[Google Cloud 新手体验层级](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=zh-cn)和 Gemini API 密钥。

## 限制和兼容性

- **仅限 AI Studio 界面**：Google AI 方案的开发者用量福利仅适用于 Google AI Studio 网页界面。直接使用 Gemini API（例如使用 API 密钥或外部应用）需单独计费和管理。不过，您可以在其他 Google 产品中使用您的订阅（请参阅 [Google AI 方案](https://one.google.com/about/google-ai-plans/?hl=zh-cn)）。
- **与 API 结算不同**：AI Studio 的 Google AI 方案与 [Gemini API 用量层级](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)是分开的，后者涵盖开发和生产 API 用量。
- **Google One 点数**：[Google One AI 点数](https://support.google.com/googleone/answer/16287445?hl=zh-cn)是一个单独的点数系统，AI Studio 不支持该系统，并且该系统与 Google Cloud 赠金不重叠。
- **Gemini 4 Argon 访问权限**：免费方案不提供 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-cn)。
- **代理访问权限**：Google AI 方案不包含对 AI Studio 中代理（Deep Research 和 Antigravity 预览版）的访问权限，需要[付费 API 密钥](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#setup-billing)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-16。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-16。"],[],[]]
