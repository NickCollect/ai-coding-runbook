---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=zh-CN
fetched_at: 2026-06-29T05:34:59.446553+00:00
title: "\u4f7f\u7528 Gemini API \u5bc6\u94a5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini API 密钥

如需使用 Gemini API，您必须对请求进行身份验证。您可以使用标准 API 密钥或授权 API 密钥进行身份验证。

[创建或查看 Gemini API 密钥](https://aistudio.google.com/apikey?hl=zh-cn)

## API 密钥类型：标准密钥与授权密钥

API 密钥可用于访问 Gemini API，但它们的安全性特征有所不同。Gemini API 正在从标准 API 密钥过渡到授权密钥，以提高安全性：

- **标准 API 密钥**：将请求与 Google Cloud 项目关联，以进行结算和配额计算。标准密钥无法识别调用者，这限制了它们可以支持的权限和访问权限控制的精细程度。
- **授权 (auth) 密钥**：直接绑定到 Google Cloud 服务账号。使用授权密钥时，系统会以绑定服务账号的身份处理您的请求，从而实现精细的访问权限控制。授权密钥默认仅限用于 Generative Language API (Gemini API)，并提供快速生效的泄露密钥强制执行功能，可快速停止使用我们的系统检测到的泄露密钥。

为确保安全使用，Gemini API 将从标准密钥改用身份验证密钥：

- **身份验证密钥默认**：在 Google AI Studio 中创建的所有新 API 密钥都会自动创建为身份验证密钥。
- **2026 年 6 月 19 日**：Gemini API 将拒绝来自**不受限制的标准密钥**的请求。应用了明确限制的标准 API 密钥将继续有效。此限制可防止未经授权使用可能公开共享或与其他服务相关联的密钥。
- **2026 年 9 月**：Gemini API 将拒绝来自**标准密钥**的请求。您必须在上述日期之前[迁移到授权密钥](#migrate-to-auth-key)，以免服务中断。请务必在 2026 年 9 月之前迁移到身份验证密钥。

## 在 Google AI Studio 中管理 API 密钥

您可以直接在 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-cn) 中管理项目和密钥。

### Google Cloud 项目

每个 Gemini API 密钥都与一个 [Google Cloud 项目](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=zh-cn)相关联。
Google Cloud 项目用于管理结算、协作者和权限。Google AI Studio 提供了一个轻量级界面来访问这些项目。

- **默认项目**：如果您是新用户，在您接受《服务条款》后，Google AI Studio 会自动创建默认的 Google Cloud 项目和 API 密钥。您可以在信息中心内前往**项目**视图，以重命名此项目。
- **现有项目**：如果您已有 Google Cloud 账号，AI Studio 不会创建默认项目。您必须改为导入现有项目。

### 导入项目

默认情况下，Google AI Studio 不会显示您的所有 Google Cloud 项目。您必须导入要使用的项目：

1. 前往 [Google AI Studio](https://aistudio.google.com?hl=zh-cn)。
2. 从左侧面板中打开**信息中心**，然后选择**项目**。
3. 点击**导入项目**按钮。
4. 搜索并选择要导入的 Google Cloud 项目，然后点击**导入**。
5. 导入后，前往信息中心的 **API 密钥**页面，在该项目中创建密钥。

### 排查密钥创建权限问题

如果**创建 API 密钥**按钮不可用，并显示以下消息：*“您无权在此项目中创建密钥”*，则表示您缺少所需的 IAM 权限。

请让您的 Google Cloud 项目或组织管理员为您授予包含以下权限的角色（例如项目编辑者）：

- `resourcemanager.projects.get`：允许 AI Studio 验证项目。
- `apikeys.keys.create`：允许生成密钥。
- `serviceusage.services.enable`：确保 Generative Language API 已启用。
- `iam.serviceAccounts.create`：创建关联的服务账号时需要提供此参数。
- `iam.serviceAccountApiKeyBindings.create`：将服务账号与 API 密钥绑定。

如果您无法获得管理员访问权限，可以创建一个未与组织相关联的新 Google Cloud 项目来生成密钥。

## 设置环境

获得密钥后，请配置环境，以便在应用中安全地使用该密钥。

### 使用环境变量（推荐）

设置环境变量 `GEMINI_API_KEY` 或 `GOOGLE_API_KEY`。Gemini API 客户端库会自动检测并使用这些变量。如果同时设置了这两个属性，则优先使用 `GOOGLE_API_KEY`。

选择您的操作系统以设置变量：

### Linux/macOS - Bash

验证您是否拥有 Bash 配置文件：

```
~/.bashrc
```

如果没有，请创建一个并打开：

```
touch ~/.bashrc && open ~/.bashrc
```

在文件末尾添加导出命令：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

保存文件，然后应用更改：

```
source ~/.bashrc
```

### macOS - Zsh

验证您是否拥有 zsh 配置文件：

```
~/.zshrc
```

如果没有，请创建一个并打开：

```
touch ~/.zshrc && open ~/.zshrc
```

添加导出命令：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

保存文件，然后应用更改：

```
source ~/.zshrc
```

### Windows

1. 在 Windows 搜索栏中搜索“环境变量”。
2. 在“系统属性”对话框中，点击**环境变量**。
3. 在**用户变量**或**系统变量**下，点击**新建…**。
4. 将变量名称设置为 `GEMINI_API_KEY`，并将值设置为您的 API 密钥。
5. 点击**确定**保存。打开新的终端会话以加载变量。

### 在代码中明确提供 API 密钥

您可以在初始化客户端时显式传递 API 密钥。仅当您无法使用环境变量时，才执行此操作。

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 安全和 Secret 管理

请像对待密码一样对待 Gemini API 密钥。如果遭到入侵，其他人可能会消耗您项目的配额、产生意外的结算费用，并访问私密资源。

### 严重安全规则

- **确保密钥保密**：切勿将 API 密钥签入 Git 等源代码控制系统。
- **切勿在生产环境中于客户端公开密钥**：请勿直接在 Web 应用或移动应用中硬编码 API 密钥。用户可以提取在客户端代码中编译的密钥。为了保护客户端应用，请运行后端代理服务器来发出实际的 API 调用。

### 密钥管理最佳实践

- **环境变量**：从环境变量（而非配置文件）读取密钥。
- **Secret Manager**：对于生产环境，请将密钥存储在安全的密文库（例如 [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=zh-cn)）中。
- **结算提醒**：在 Google Cloud 控制台中设置结算提醒，以便在用量或费用激增时收到通知。

### 泄露应对核对清单

如果您怀疑自己的 API 密钥已泄露，请执行以下操作：

1. **生成新密钥**：在 Google AI Studio 或 Cloud 控制台中创建替代密钥。
2. **更新应用**：使用新密钥部署代码。
3. **停用或删除遭泄露的密钥**：在新密钥通过验证后，在 Cloud 控制台中停用遭泄露的密钥。在新密钥完全生效之前，请勿删除旧密钥，以免应用停机。
4. **审核使用情况**：在 Google Cloud 控制台中查看结算日志和 API 使用情况，以识别未经授权的活动。

## 限制和保护密钥

为 API 密钥添加限制可最大限度地减少密钥被盗用时可能造成的损害。

### 应用请求来源限制

来源限制用于限制哪些 IP 地址、网站或应用可以使用您的密钥。

1. 前往 [Google Cloud 控制台的“凭据”页面](https://console.cloud.google.com/apis/credentials?hl=zh-cn)。
2. 选择您的项目，然后点击您要限制的 API 密钥的名称。
3. 在**应用限制**下，选择 **IP 地址**（或适合您环境的相应限制类型）。
4. 指定允许的 IP 地址或范围，然后点击**保存**。

### 保护不受限制的标准 API 密钥

如需在 2026 年 6 月 19 日之后继续使用 Gemini API，您必须保护所有不受限制的密钥。

#### 通过 AI Studio 将密钥限制为仅限 Gemini API 使用

如果您仅将密钥用于 Gemini API，请直接在 AI Studio 中保护该密钥：

1. 在 [Google AI Studio](https://aistudio.google.com/api-keys?hl=zh-cn) 的 **API 密钥**页面上，找到标有**不受限**标签的密钥。
2. 将鼠标悬停在相应标签上，然后点击对话框中的**添加限制**。
3. 选择**限制为仅限 Gemini API 使用**。
4. 点击**限制密钥**进行确认。

#### 通过 Google Cloud 控制台限制密钥对其他服务的访问权限

如果该密钥与其他 Google API 共享（不建议这样做），请在 Cloud 控制台中限制该密钥。**注意：应用这些限制后，使用此密钥发出的 Gemini API 请求将失败。**

1. 访问 [Google Cloud 控制台的“凭据”页面](https://console.cloud.google.com/apis/credentials?hl=zh-cn)。
2. 选择项目和 API 密钥。
3. 在 **API restrictions** 下，选择 **Restrict key**。
4. 从下拉菜单中选择您希望此密钥访问的 API。请勿选择 **Generative Language API**。
5. 点击**保存**。在 AI Studio 中创建单独的受限密钥，以继续使用 Gemini API。

### 已屏蔽的休眠密钥

自 2026 年 5 月 7 日起，Gemini API 将屏蔽长期处于休眠状态的不受限制的 API 密钥。这些密钥在 AI Studio 中会显示为**已屏蔽**。您必须生成新密钥或使用现有的受限密钥才能继续。

## 迁移到身份验证密钥

请按照以下步骤创建新的身份验证 API 密钥并更新您的应用：

1. 前往 [AI Studio API 密钥页面](https://aistudio.google.com/api-keys?hl=zh-cn)。
2. 检查**密钥类型**列，找出所有列为**标准**的密钥。
3. 点击**创建 API 密钥**以生成新密钥。在 AI Studio 中创建的所有新密钥都会自动创建为身份验证密钥。
4. 复制新的身份验证 API 密钥。
5. 更新应用代码、环境变量和所有部署配置，以使用新的身份验证 API 密钥。
6. 测试您的应用，确认它在新密钥下正常运行。
7. 验证完成后，请删除或撤消旧的流量密钥，以防被滥用。

## 限制

Google AI Studio 施加了以下项目和密钥管理限制：

- 您最多可以同时在 Google AI Studio 的**项目**页面中创建 10 个项目。
- **API 密钥**和**项目**页面最多显示 100 个密钥和 50 个项目。
- 系统只会显示不受限制或专门限制为仅供 Generative Language API（Gemini API）使用的 API 密钥。

如需进行高级项目管理或修改具有其他限制的密钥，请使用 [Google Cloud 控制台凭据页面](https://console.cloud.google.com/apis/credentials?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-24。"],[],[]]
