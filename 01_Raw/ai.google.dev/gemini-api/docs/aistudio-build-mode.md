---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-CN
fetched_at: 2026-10-12T07:02:15.145318+00:00
title: "\u5728 Google AI Studio \u4e2d\u6784\u5efa\u5e94\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 在 Google AI Studio 中构建应用

本页介绍了如何使用 Google AI Studio 快速构建（或“氛围
编程”）和部署应用，以测试 Gemini 的最新功能，例如
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn) 和 [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)。Google AI Studio 支持使用全栈运行时构建 **Web 应用** ，以及使用 Kotlin 和 Jetpack Compose 构建**原生 Android 应用** ，所有这些都可以通过自然语言提示完成。

## 开始使用

在 Google AI Studio 的[“构建”模式](https://aistudio.google.com/apps?hl=zh-cn)下开始氛围编程。您可以通过以下几种方式开始构建：

- **从提示开始**：在“构建”模式下，使用输入框输入您要构建的内容的
  说明。选择“AI 芯片”可向提示添加特定功能，例如图片生成或 Google 地图数据。您甚至可以使用语音转文字按钮说出您想要的内容。
- **“手气不错”按钮**：如果您需要创意灵感，请使用“手气不错”按钮，Gemini 将生成一个包含项目想法的提示，帮助您入门。
- **混搭媒体库中的项目**：从[应用
  媒体库](https://aistudio.google.com/apps?source=showcase&hl=zh-cn)中打开一个项目，然后选择**复制应用**。
- **从 GitHub 导入项目**：在“构建”模式下，从提示
  输入框中的**添加文件**（+ 图标）菜单中选择
  **Import from GitHub**（从 GitHub 导入），以导入现有代码。

运行提示后，您会看到必要的代码和文件生成，右侧会实时显示应用的预览效果。

## 创建了什么？

运行提示时，AI Studio 会创建一个完整的应用。您可以使用平台选择器选择构建 **Web 应用** 或**原生 Android 应用** 。

对于 **Web 应用** （默认），AI Studio 会创建一个全栈环境，其中包括：

- **客户端**：Web 前端（默认使用 React）。
- **服务器端**：Node.js 运行时，支持安全的 API 调用、
  数据库连接和 npm 软件包使用。

对于 **Android 应用**，AI Studio 会生成一个 Kotlin 和 Jetpack Compose 项目
，您可以在基于浏览器的模拟器中预览该项目，将其安装在实体设备上
，并将其发布到 Play 商店进行测试。[详细了解如何构建 Android
应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)。

您可以通过选择右侧预览窗格中的**代码** 标签页来查看生成的代码。**Antigravity 智能体** 可以智能地管理堆栈中的多个文件，确保更改正确传播。

### Antigravity 智能体

**Antigravity 智能体** 是 [Google
Antigravity](https://antigravity.google?hl=zh-cn) 中的主要 AI 功能，现在
智能体 Harness 的核心组件为 Google AI Studio 中的“构建”模式体验提供支持。它不仅能生成简单的代码，还能维护整个项目的上下文、管理多个文件并理解复杂的指令，从而构建稳健的全栈应用。

主要功能包括：

- **上下文感知**：维护先前提示和文件状态的上下文。
- **多文件管理**：处理多个文件之间的依赖关系。
- **验证执行**：验证代码更新以减少幻觉。

## 全栈功能

Google AI Studio 释放了现代 Web 生态系统的强大功能，让您不仅可以构建客户端原型。

- **服务器端运行时和 npm** ：使用 npm 软件包的庞大库。智能体会自动识别并安装应用所需的软件包（例如，用于数据可视化或 API 客户端的特定库）。您也可以根据需要请求特定软件包。
- **密钥管理**：在
  **设置**菜单中安全地存储 API 密钥和密钥。这些密钥可在服务器端代码中访问，从而避免在客户端暴露。
- **多人游戏**：直接在
  AI Studio 中构建实时协作体验。服务器端运行时管理用户一起互动所需的状态和连接。
- **Firebase Firestore 和 Authentication**：自动预配和设置
  Firebase，包括 Firestore 数据库（持久数据存储）和
  Firebase Authentication（登录流程，特别是“使用
  Google 账号登录”）。智能体会处理整个设置过程，甚至在应用中为这些服务编写代码。
- **Google Workspace 集成**：将应用连接到 Google Workspace
  API，例如 Gmail、表格、文档、云端硬盘、日历等。AI Studio 会自动处理所有 OAuth 配置。

[详细了解如何开发全栈应用](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-cn)

### Android 应用

您还可以使用 Kotlin 和 Jetpack Compose 构建原生 Android 应用。
在基于浏览器的 Android 模拟器中预览应用，使用浏览器中的 ADB 将其安装在实体设备上，并将其发布到 Play 商店进行内部测试。

[详细了解如何构建 Android 应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)

## 继续构建

Google AI Studio 为您的应用生成初始代码后，您可以继续对其进行优化：

### 在 Google AI Studio 中构建

- **使用 Gemini 进行迭代**：使用**构建模式** 中的聊天面板，要求 Gemini
  进行修改、添加新功能或更改样式。
- **直接修改代码**：打开预览面板中的**代码标签页**以
  进行实时修改。

### 在外部开发

对于更高级的工作流，您可以同步或导出代码以在您偏好的环境中工作：

- **与 GitHub 同步**：将应用连接到 GitHub 代码库以启用
  双向同步。您可以将 AI Studio 中提示的更改直接推送到代码库，并附上 AI 生成的提交消息，也可以将 IDE 中或队友在本地所做的更改拉回到 AI Studio 中。您可以随时在“设置”中的 **GitHub** 标签页中管理同步状态。
- **下载并在本地开发**：将生成的代码导出为 **ZIP
  文件** ，然后将其导入到代码编辑器中。

## 主要特性

Google AI Studio 包含多项功能，让构建过程直观且可视化：

- **创建和迭代全栈应用**：只需
  一个提示即可创建全栈应用，并通过聊天或**注释模式**进行迭代。借助注释模式，您可以突出显示应用界面的任何部分，并描述您想要的更改。
- **分享和部署应用**：您可以与他人分享您的作品以进行
  协作或展示您的作品。分享时，API 调用会计入您的使用量限制。如果您使用付费模型，可能会产生费用。然后，当您的应用准备就绪后，将其部署到 Cloud Run。
- **应用库**：应用库提供了一个项目想法的可视化库。您可以浏览 Gemini 的功能，即时预览应用，并混搭应用以打造自己的应用。

## 部署或归档应用

应用准备就绪后，您可以部署它：

- **Cloud Run**：将应用部署为可扩缩的服务。
  [Google Cloud Run](https://cloud.google.com/run?hl=zh-cn) 的价格可能会根据使用情况
  而定。如需详细了解部署，请参阅
  [从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)。
- **GitHub**：将项目与新的或现有的 GitHub 代码库同步
  以管理源代码或与队友协作。

## 限制

本部分列出了 Google AI Studio 中“构建”模式的当前限制。

### API 密钥管理

当您创建使用 Gemini API 的新应用时，AI Studio 会自动将您的 Gemini API 密钥配置为应用服务器端环境中的密钥。
您可以在**密钥** 面板中查看和管理此密钥。

- **自动设置**：系统会为您设置 `GEMINI_API_KEY`，无需手动
  配置即可开始构建。
- **仅限服务器端**：API 密钥会注入到服务器端运行时中，
  绝不会包含在客户端代码中。
- **现有应用**：对于在 2026 年 5 月 14 日之前构建的应用，当您下次修改应用的 Gemini 功能时，智能体会
  自动将您的 Gemini API 集成升级到推荐的
  服务器端方法。

### 在 Google AI Studio 之外进行部署

- **Cloud Run**：当您从 AI Studio 部署到 Cloud Run 时，您的 API 密钥会
  安全地包含在服务器端环境中。部署的应用将使用您的 API 密钥来处理所有用户的 Gemini API 调用。
- **ZIP 下载**：如果您将应用下载为 ZIP 文件以在其他位置运行，则需要在托管环境中设置 `GEMINI_API_KEY` 环境变量。由于应用的 Gemini API 调用是从服务器端代码发出的，因此密钥不会向最终用户公开。

### 分享应用时出错

如果您分享应用，而最终用户在使用共享网址时遇到 **403 Access Restricted** （访问受限）错误，则可能是由于以下原因之一：

- **浏览器扩展程序**：Privacy Badger 等隐私扩展程序可能会阻止应用。停用该扩展程序以避免错误。
- **构建问题**：当前代码可能存在问题。提示智能体“修复当前代码中的任何构建问题”，然后重新分享网址。

## 常见问题解答

### 什么是 AI Studio 中的“构建”？

AI Studio Build 是一个平台，旨在帮助您使用 Gemini 从简单的提示到可用于生产用途的 AI 赋能的应用。使用提示描述您要构建的内容，Gemini 将为您生成一个应用。您还可以浏览我们的媒体库，了解 Gemini API 的功能，并混搭应用以打造自己的应用。

### “构建”如何处理我的 Gemini API 密钥？

当您创建使用 Gemini API 的应用时，AI Studio 会自动将您的 Gemini API 密钥设置为服务器端密钥。应用的 Gemini API 调用是使用此密钥从服务器端代码发出的，因此绝不会在浏览器中公开。您可以在“设置”中的**密钥** 面板中查看 API 密钥。

### 分享应用时，我的 API 密钥是否会公开？

不会。您的 API 密钥会存储为服务器端密钥，绝不会包含在客户端代码中。当您分享应用时，其他用户可以使用该应用，但无法看到您的 API 密钥。

与他人分享应用时，API 调用会计入您的使用量限制。
如果您使用付费模型，可能会产生费用。如果您的应用可能会产生费用，AI Studio 会在设置期间和分享之前提醒您。

### 谁可以看到我的应用？

默认情况下，您的应用处于非公开状态。您可以与其他用户分享应用，让他们使用该应用。与您分享应用的用户可以看到应用的代码，并将其派生出来以供自己使用。如果您分享应用时授予了修改权限，其他用户可以修改应用的代码。

### 我可以在 AI Studio 之外运行应用吗？

可以。您可以从 AI Studio 将应用部署到
[Cloud Run](https://cloud.google.com/run?hl=zh-cn)，这会为您的应用提供一个公开网址，并在
服务器端环境中安全地配置您的 API 密钥。您还可以将应用下载为 ZIP 文件并在其他位置托管，您需要在托管环境中设置 `GEMINI_API_KEY` 环境变量。由于 Gemini API 调用是从服务器端代码发出的，因此您的密钥会保持安全。

如需详细了解部署选项，请参阅[从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)。

### 我可以在本地使用自己的工具开发应用，然后在此处分享吗？

可以。您可以将 AI Studio 应用连接到 GitHub 代码库，以便在本地使用您偏好的代码编辑器或 CLI 工具进行开发，将更改推送到 GitHub，然后使用“设置”中的 **GitHub** 标签页将这些更新直接拉回到 AI Studio 中。

### 如何将数据库或其他存储与我的应用搭配使用？

AI Studio 应用是在 Cloud Run 容器中运行的标准应用。只要没有防火墙阻止来自动态 IP 范围的访问，您就可以使用任何可以通过网络连接到的存储解决方案。

我们正在努力在未来添加对存储的直接支持，您将可以直接在 AI Studio 中进行配置。

### 如何访问麦克风、网络摄像头和其他 Navigator API？

为了确保观看者了解应用对其网络摄像头或其他
设备的使用情况，我们需要在应用访问
这些 [Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) 之前获得额外的确认。
应用创建者可以将这些权限请求添加到应用的 `metadata.json` 文件中。例如：

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

`requestFramePermissions` 的支持值是
标准 [政策控制功能的子集](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md)。

### 如何将 GitHub 与我的应用搭配使用？

AI Studio 支持与 GitHub 进行双向同步：

- **导入代码库**：在“构建”模式下，从提示输入框中的**添加文件**（+ 图标）菜单中选择**Import from GitHub**
  （从 GitHub 导入），以导入
  现有代码。
- **关联代码库**：在“设置”中，打开 **GitHub** 标签页，以从应用创建
  新的 GitHub 代码库或关联到现有代码库。
- **双向同步**：将 AI Studio 中提示的更改直接推送到
  代码库，并附上 AI 生成的提交消息，也可以将外部所做的更改（例如本地 IDE 修改或队友拉取请求）拉回到 AI
  Studio 中。
- **解决合并冲突**：如果与
  GitHub 同步时更改发生冲突，AI Studio 会提供一个**解决冲突** 对话框，其中包含
  并排差异查看器，让您可以查看差异并选择
  是保留 AI Studio 版本还是 GitHub 版本（针对每个冲突的文件）。

### 我可以向其他用户授予应用的修改权限吗？

AI Studio 不支持直接实时协作修改。
不过，您可以将应用关联到共享的 GitHub 代码库，以便与队友协作。队友可以在 GitHub 上推送更改或打开拉取请求，您可以将这些更新拉到 AI Studio 中。

### 为什么我的应用被标记为违反政策？

我们有自动审核应用的系统，以确保应用符合我们的政策。如果我们发现应用违反了我们的政策，我们会将该应用从 AI Studio 中移除。违规行为可能包括但不限于以下内容：

- 包含恶意软件、钓鱼式攻击或冒充行为的应用
- 显示或分发违反儿童性虐待影像政策的内容的应用
- 显示或分发违反骚扰政策的内容的应用
- 显示或分发违反仇恨言论政策的内容的应用
- 显示或分发违反人口贩卖政策的内容的应用
- 显示或分发违反露骨色情内容政策的内容的应用
- 显示或分发违反暴力和血腥内容政策的内容的应用
- 显示或分发违反有害或危险内容政策的内容的应用

如果您的应用被标记为违反政策，但您认为这是错误的，可以提交申诉。屡次违反我们的政策可能会导致您无法再访问 AI Studio。

### 作为应用开发者，我的责任是什么？

请注意，作为应用的所有者，您需要对应用的行为及其处理的所有数据负责。其中包括：

- **法律合规性和第三方权利**： 确保您的应用符合所有适用的法律法规，并且不侵犯他人的权利，包括知识产权和隐私权。
- **内容监控**： 您的应用使用的
  其他服务可能需要遵守附加条款。例如，
  [适用于 Firestore 的 Google Cloud 服务条款](https://cloud.google.com/terms?hl=zh-cn)要求托管第三方内容的客户
  发布政策，以定义禁止的内容（例如非法
  内容），并监控是否存在非法内容。
- **安全实现**： 实现必要的安全措施和审核工具，以防止应用被滥用。

请注意[服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn#use-restrictions)
中的使用限制。

### 哪些条款适用于 AI Studio 中应用库中的应用？

除非另有说明，否则 [Gemini API 附加服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn) 适用于使用 AI Studio 中应用库中的精选应用。

## 后续步骤

- [开发全栈应用](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-cn) (Web)
- [构建 Android 应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)
- 在[应用媒体库](https://aistudio.google.com/apps?source=showcase&hl=zh-cn)中查看示例。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-11。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-11。"],[],[]]
