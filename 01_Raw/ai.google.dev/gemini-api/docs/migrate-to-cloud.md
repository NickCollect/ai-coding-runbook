---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=zh-CN
fetched_at: 2026-08-24T02:25:50.078487+00:00
title: "Gemini Developer API \u4e0e Gemini Enterprise Agent Platform \u7684\u5bf9\u6bd4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Developer API 与 Gemini Enterprise Agent Platform 的对比

使用 Gemini 开发生成式 AI 解决方案时，Google 提供两种 API 产品：
[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=zh-cn) 和 [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=zh-cn)。

Gemini Developer API 提供最快的路径来构建、生产化和扩缩由 Gemini 提供支持的应用。大多数开发者都应使用 Gemini Developer API，除非需要特定的企业控制。

Gemini Enterprise Agent Platform 提供了一个全面的生态系统，其中包含企业就绪型功能和服务，用于构建和部署由 Google Cloud Platform 提供支持的生成式 AI 应用。

我们最近简化了在这些服务之间迁移的过程。现在，您可以通过统一的
[Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)访问 Gemini
Developer API 和 Gemini Enterprise Agent Platform API。

## 代码比较

此页面并排比较了 Gemini Developer API 和 Gemini Enterprise Agent Platform 文本生成快速入门的代码。

### Python

您可以通过 `google-genai` 库访问 Gemini Developer API 和 Gemini Enterprise Agent Platform 服务。如需了解如何安装 `google-genai`，请参阅 [库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn) 页面
。

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript 和 TypeScript

您可以通过 `@google/genai` 库访问 Gemini Developer API 和 Gemini Enterprise Agent Platform 服务。如需了解如何安装 `@google/genai`，请参阅 [库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn) 页面。

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

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

您可以通过 `google.golang.org/genai` 库访问 Gemini Developer API 和 Gemini Enterprise Agent Platform 服务。如需了解如何安装 `google.golang.org/genai`，请参阅 [库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)页面。

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### 其他用例和平台

如需了解其他平台和用例，请参阅 [Gemini Developer API 文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)
和 [Gemini Enterprise Agent Platform 文档](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=zh-cn)
中特定于用例的指南。

## 迁移注意事项

迁移时：

- 您需要使用 Google Cloud 服务账号进行身份验证。如需了解详情，请参阅 [Gemini Enterprise Agent Platform 文档](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=zh-cn)
  。
- 您可以使用现有的 Google Cloud 项目
  （即用于生成 API 密钥的项目），也可以
  [创建新的 Google Cloud 项目](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=zh-cn)。
- Gemini Developer API 和 Gemini Enterprise Agent Platform API 支持的区域可能有所不同。请参阅 Google Cloud 上的生成式 AI 支持的区域列表
  。
- 您在 Google AI Studio 中创建的任何模型都需要在 Gemini Enterprise Agent Platform 中重新训练。

如果您不再需要使用 Gemini Developer API 的 Gemini API 密钥，请遵循安全性最佳实践并将其删除。

如需删除 API 密钥，请执行以下操作：

1. 打开
   [Google Cloud API 凭据](https://console.cloud.google.com/apis/credentials?hl=zh-cn)
   页面。
2. 找到您要删除的 API 密钥，然后点击**操作** 图标。
3. 选择**删除 API 密钥** 。
4. 在**删除凭据**模态框中，选择**删除**。

   删除 API 密钥的操作需要几分钟时间才能生效。生效后，任何使用已删除的 API 密钥的流量都将遭到拒绝。

## 后续步骤

- 如需详细了解 Gemini Enterprise Agent Platform 上的生成式 AI 解决方案，请参阅
  [Gemini Enterprise Agent Platform 上的生成式 AI 概览](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=zh-cn)
  。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-22。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-22。"],[],[]]
