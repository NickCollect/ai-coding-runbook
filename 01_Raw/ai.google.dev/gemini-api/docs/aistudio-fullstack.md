---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-CN
fetched_at: 2026-06-29T05:29:24.230392+00:00
title: "\u5728 Google AI Studio \u4e2d\u5f00\u53d1\u5168\u6808\u5e94\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 在 Google AI Studio 中开发全栈应用

Google AI Studio 现已支持全栈开发，让您能够构建超出客户端原型范围的应用。借助服务器端运行时，您可以管理 Secret、连接到外部 API，以及打造实时多人游戏体验。

## 服务器端运行时

Google AI Studio 应用现在可以包含服务器端组件 (Node.js)。
借助此功能，您可以：

- **执行服务器端逻辑**：运行不应向
  客户端公开的代码。
- **访问 npm 软件包**：[Antigravity 智能体](https://antigravity.google/docs/agent?hl=zh-cn)
  可以从庞大的 npm 生态系统中安装和使用软件包。
- **处理 Secret**：安全地使用 API 密钥和凭据。

### 使用 npm 软件包

您无需手动运行 `npm install`。只需让智能体添加需要软件包的功能，它就会处理安装和导入。

**示例**：>“使用 `axios` 从外部 API 提取数据。”

## 安全地管理 Secret

借助服务器端代码和 Secret 管理功能，您现在可以构建与外界互动的应用。

### Gemini API 密钥

当您创建使用 Gemini API 的新应用时，AI Studio 会自动将 `GEMINI_API_KEY` 配置为服务器端 Secret，无需手动设置。您可以在“设置”中的 **Secrets** 面板中查看此密钥。应用的 Gemini API 调用是使用此密钥通过服务器端代码进行的，因此绝不会在浏览器中公开。

### 第三方 API 密钥

对于其他服务，您可以手动添加 API 密钥：

- **第三方 API**：连接到 Stripe、SendGrid 或自定义
  REST API 等服务。
- **数据库**：连接到外部数据库（例如，通过 Supabase、Firebase、
  或 MongoDB Atlas），以便在会话结束后保留数据。

在构建实际应用时，您通常需要连接到需要 API 密钥的第三方服务（例如 Twilio、Slack 或数据库）。您可以按照以下步骤手动添加密钥：

1. **添加 Secret**：前往 Google AI Studio 中的**设置** 菜单，然后找到
   “Secrets”部分。
2. **存储密钥**：在此处添加您的 API 密钥或 Secret 令牌。
3. **在代码中访问**：智能体可以编写服务器端代码，以安全地访问这些
   Secret（通常通过环境变量），确保它们绝不会向客户端浏览器公开。

在需要时，智能体还会在聊天中显示一张卡片，提示您在需要新 Secret 或在项目的 env 变量中检测到新密钥时添加密钥。

### Firebase 集成，用于数据库和身份验证

Google AI Studio 现在可以通过
[Firebase 集成](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=zh-cn)轻松地向
应用添加数据库或身份验证。
Antigravity 智能体可以自动为您配置和设置以下服务：

- **Firestore 数据库**：一种灵活且可扩缩的 NoSQL 云数据库，用于存储
  和同步数据，以便进行客户端及服务器端的开发。
- **Firebase Authentication**：让用户可以使用“使用 Google 账号登录”流程安全地登录您的
  应用。

只需让智能体“向我的应用添加数据库”或“设置 Google 登录”，它就会为您处理必要的配置和代码生成。

Firebase 可让您免费开始使用，并可选择在您准备好使用更多配额或使用付费功能时，通过付费账号进行扩缩。

## Google Workspace API

借助 Google AI Studio，您可以构建连接到 Google Workspace API 的应用，以便用户可以在应用中使用真实数据：电子邮件、电子表格、文档、日历活动等。您不再需要设置 Google Cloud 云项目、配置 OAuth 或手动管理 API。

### 运作方式

您可以通过以下两种方式添加 Workspace 集成：

- **在聊天面板中进行描述**：只需在底部的聊天面板中告知智能体您想要的内容。例如，*“构建一个费用跟踪器，将收据记录到我的 Google 表格”*或*“创建一个信息中心，用于汇总我的未读 Gmail 邮件。”*
- **从集成面板中进行选择**：在构建模式的右侧边栏中打开**集成**面板，然后启用您要连接的 Workspace 应用。

添加 Workspace 应用后，AI Studio 会自动执行以下操作：

1. 为您的应用连接必要的 Google API。
2. 生成用于调用 API 的服务器端代码。
3. 添加安全的“使用 Google 账号登录”流程，以便应用的最终用户可以授权访问自己的数据。

### 支持的应用

以下 Google Workspace 应用可用：

| 应用 | 您可以构建的内容 |
| --- | --- |
| Google 日历 | 读取、创建和管理活动及日历 |
| Google Chat | 读取对话和群组聊天室并与之互动 |
| Google 文档 | 创建、读取、更新和设置文档格式 |
| Google 云端硬盘 | 整理、搜索和管理文件及文件夹 |
| Google 表单 | 创建调查问卷、更新问题和检索回答 |
| Gmail | 读取、发送和管理电子邮件内容 |
| Google Keep | 管理记事、清单和附件 |
| Google Meet | 安排和管理视频通话 |
| 通讯录 | 同步和管理联系人 |
| Google 表格 | 读取、写入和设置电子表格数据格式 |
| Google 幻灯片 | 创建和修改演示文稿 |
| Google Tasks | 创建、管理和整理任务 |

### 身份验证和权限

作为构建者，您无需配置 OAuth 客户端、管理凭据或设置 Google Cloud 项目。AI Studio 会为您处理所有这些事宜。

集成了 Workspace API 的应用使用“使用 Google 账号登录”对最终用户进行身份验证。当用户打开您的应用时，系统会提示他们登录并授予应用所需的特定权限（例如，对其日历的只读权限，或编辑电子表格的权限）。您的应用只能访问使用该应用的人员的数据。每位用户都会授权访问自己的账号。

### 示例提示

以下这些方法可帮助您开始使用 Workspace 集成：

- *“构建一个应用，用于读取我的 Google 日历，并在
  Gmail 中为每次会议起草准备电子邮件。”*
- *“创建一个工具，用于获取 Google 文档，并在 Google 幻灯片中生成 5 张幻灯片的摘要
  演示文稿。”*
- *“创建一个费用跟踪器，用于让我上传收据，让 Gemini 提取
  详细信息，并在我的 Google 表格中记录新行。”*

### 设置 OAuth

Secret 管理的一个主要用例是设置 OAuth 以连接到其他网站或应用。当您的提示包含有关连接到需要 OAuth 身份验证的第三方应用的说明时，智能体会提供有关如何为该应用设置 OAuth 的说明。这些说明将包含配置 OAuth 应用所需的回调网址。
您还可以在“设置”面板的**集成** 下找到回调网址。

## 打造多人游戏体验

全栈运行时支持实时协作功能。

- **实时状态**：您可以让智能体构建“实时
  聊天”“协作白板”或“多人游戏”等功能。
- **同步会话**：服务器管理状态，允许多个用户
  实时与同一应用实例互动。

**提示示例**：>“将其设为多人游戏，让玩家可以看到彼此的光标。”

### 测试多人游戏应用的提示

您可以通过以下两种方式测试多人游戏模式，然后再部署应用。

1. 在多个标签页中以 Google AI Studio 构建模式打开应用。在构建模式下开发时，您的应用位于开发容器中。在多个标签页中打开应用可让您模拟多个玩家使用您的应用。
2. 使用右上角的**分享** 菜单与他人分享应用。然后，使用**分享** 菜单的**集成** 标签页中的**分享的网址** ，以便与您分享了应用的其他玩家一起使用该应用。

## 最佳做法

- **Gemini API 调用**：您的 `GEMINI_API_KEY` 会自动配置为
  服务器端 Secret。使用此密钥通过服务器端代码进行 Gemini API 调用。您可以在 **Secrets** 面板中查看它。
- **Secret 安全性**：对于敏感密钥，请始终使用 Secret 管理器。
  切勿在文件中对它们进行硬编码。
- **关注点分离**：将界面逻辑保留在客户端框架
  (React/Angular) 中，并将业务逻辑/数据处理保留在服务器端。
- **错误处理**：确保服务器端代码能够稳健地处理来自外部 API 调用的错误
  ，以防止应用崩溃。

## 后续步骤

- [在 Google AI Studio 中构建应用](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-cn)
- [从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)
- [应用库](https://aistudio.google.com/apps?source=showcase&hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-19。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-19。"],[],[]]
