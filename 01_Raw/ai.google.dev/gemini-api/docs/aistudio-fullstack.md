---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-CN
fetched_at: 2026-05-05T13:21:44.557004+00:00
title: "\u5728 Google AI Studio \u4e2d\u5f00\u53d1\u5168\u6808\u5e94\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

- [首页](https://ai.google.dev/gemini-api/docs/首页)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文档](https://ai.google.dev/gemini-api/docs/文档)

发送反馈

# 在 Google AI Studio 中开发全栈应用

Google AI Studio 现已支持全栈开发，让您能够构建超出客户端原型范围的应用。借助服务器端运行时，您可以管理密文、连接到外部
API，并打造实时多人游戏体验。

## 服务器端运行时

Google AI Studio 应用现在可以包含服务器端组件 (Node.js)。
借助此功能，您可以：

- **执行服务器端逻辑**：运行不应向
  客户端公开的代码。
- **访问 npm 软件包**：[Antigravity Agent](https://ai.google.dev/gemini-api/docs/Antigravity Agent)
  可以安装和使用来自庞大 npm 生态系统的软件包。
- **处理密文**：安全地使用 API 密钥和凭据。

### 使用 npm 软件包

您无需手动运行 `npm install`。只需让 Agent 添加需要软件包的功能，它就会处理安装和导入。

**示例**：>“使用 `axios` 从外部 API 获取数据。”

## 安全地管理密文

借助服务器端代码和密文管理，您现在可以构建与外界互动的应用。

- **第三方 API**：连接到 Stripe、SendGrid 或自定义
  REST API 等服务。
- **数据库**：连接到外部数据库（例如，通过 Supabase、Firebase、
  或 MongoDB Atlas），以便在会话结束后保留数据。

在构建实际应用时，您通常需要连接到需要 API 密钥的第三方服务（例如 Twilio、Slack 或数据库）。您可以按照以下步骤手动添加密钥：

1. **添加密文**：前往 Google AI Studio 中的**设置** 菜单，然后找到
   “密文”部分。
2. **存储密钥**：在此处添加 API 密钥或密文令牌。
3. **在代码中访问**：Agent 可以编写安全访问这些
   密文的服务器端代码（通常通过环境变量），确保这些密文永远不会暴露给客户端浏览器。

在需要时，Agent 还会显示聊天中的卡片，提示您在需要新密文或在项目的 env 变量中检测到新密钥时添加密钥。

### Firebase 集成，用于数据库和身份验证

Google AI Studio 现在可以通过
[Firebase 集成](https://ai.google.dev/gemini-api/docs/Firebase 集成)轻松地向
应用添加数据库或身份验证。
Antigravity Agent
可以自动为您配置以下服务：

- **Firestore 数据库**：一种灵活且可伸缩的 NoSQL 云数据库，用于存储和同步数据，以便进行客户端及服务器端的开发。
- **Firebase Authentication**：允许用户使用“使用 Google 账号登录”流程安全地登录您的
  应用。

只需让 Agent“向我的应用添加数据库”或“设置 Google 登录”，它就会为您处理必要的配置和代码生成。

Firebase 允许您免费开始使用，并可选择在您准备好使用更多配额或使用付费功能时，通过付费账号进行扩容。

### 设置 OAuth

密文管理的一个主要用例是设置 OAuth 以连接到其他网站或应用。当您的提示包含有关连接到需要 OAuth
身份验证的第三方应用的说明时，Agent 将提供有关如何为该应用设置 OAuth 的说明。这些说明将包含配置 OAuth
应用所需的回调网址。
您还可以在“设置”面板的**集成** 下找到回调网址。

## 打造多人游戏体验

全栈运行时支持实时协作功能。

- **实时状态**：您可以让 Agent 构建“实时
  聊天”“协作白板”或“多人游戏”等功能。
- **同步会话**：服务器管理状态，允许多个用户
  实时与同一应用实例互动。

**提示示例**：>“将其设为多人游戏，让玩家可以看到彼此的光标。”

### 测试多人游戏应用的提示

您可以通过两种方式测试多人游戏模式，然后再部署应用。

1. 在多个标签页中以 Google AI Studio 构建模式打开应用。在构建模式下开发时，您的应用位于开发容器中。在多个标签页中打开应用可让您模拟多个玩家使用您的应用。
2. 使用右上角的**分享** 菜单与他人分享应用。然后，使用**分享** 菜单的**集成** 标签页中的**共享网址** ，与您已分享应用给的玩家一起使用该应用。

## 最佳做法

- **密文安全性**：对于敏感密钥，请始终使用密文管理器。
  切勿在文件中硬编码这些密钥。
- **关注点分离**：将界面逻辑保留在客户端框架
  (React/Angular) 中，并将业务逻辑/数据处理保留在服务器端。
- **错误处理**：确保服务器端代码能够稳健地处理来自外部 API 调用的错误
  ，以防止应用崩溃。

## 后续步骤

- [在 Google AI Studio 中构建应用](https://ai.google.dev/gemini-api/docs/在 Google AI Studio 中构建应用)
- [应用库](https://ai.google.dev/gemini-api/docs/应用库)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://ai.google.dev/gemini-api/docs/知识共享署名 4.0 许可)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://ai.google.dev/gemini-api/docs/Apache 2.0 许可)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://ai.google.dev/gemini-api/docs/Google 开发者网站政策)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？
