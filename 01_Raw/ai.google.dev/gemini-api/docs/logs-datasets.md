---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-CN
fetched_at: 2026-10-05T06:51:10.181635+00:00
title: "\u65e5\u5fd7\u548c\u6570\u636e\u96c6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 日志和数据集

在本指南中，您将了解如何在 Google AI Studio 信息中心内查看 Gemini API 使用情况的日志，以便更好地了解模型行为以及用户与您的应用互动的方式。使用日志记录来观察、调试，并*选择性地与 Google 分享使用情况反馈，以帮助改进 Gemini 在开发者使用情形下的表现*。[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-cn)

支持所有 `GenerateContent`、`BatchGenerateContent`、`StreamGenerateContent` API 调用，以及除托管式智能体之外的 [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn) API 调用。这包括通过 [OpenAI 兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)端点进行的调用。

## 配置项目日志记录

默认情况下，该 API 会存储所有互动对象 (`store=true`)，以简化服务器端状态管理功能的使用。相比之下，Generate Content API 默认不存储请求，需要从 AI Studio 中按请求或在项目级启用存储。

在 Google [AI Studio](https://aistudio.google.com/logs?hl=zh-cn) 中，您可以为所有项目或特定项目启用或停用日志记录，并随时通过[日志和数据集](https://aistudio.google.com/logs?hl=zh-cn)页面中的**设置**面板更改这些偏好设置。您可以单独为 `generateContent` API 和[互动](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn) API 开启或关闭日志记录，以更改项目的默认存储行为。

### 请求级日志记录

存储和日志记录行为因 API 而异：

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)**：默认存储请求 (`store=true`)，以简化服务器端状态管理。
- **Generate Content API (`generateContent`)**：默认情况下不存储请求 (`store=false`)。

以下是设置 `store` 属性的方法：

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

// The GenerateContent API does not store requests by default
GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder().build());

System.out.println(response.text());
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // The GenerateContent API does not store requests by default
    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{},
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

## 在 AI Studio 中查看项目日志

1. 前往 [AI Studio](https://aistudio.google.com/logs?hl=zh-cn) 中的“日志”页面。
2. 从下拉菜单中选择一个项目。
3. 如果存在日志，则日志将以反向时间顺序显示在 Interactions API 的表格中。
4. 如需查看 Generate Content API 的项目日志，请先在[设置面板](#configure-logging)中启用此功能。

点击条目即可预览相应载荷。您可以检查 Gemini 的完整提示和回答，以及之前对话轮次中的上下文。对于 **Interactions API** 请求，日志还包含指向 `previous_interaction_id` 的直接链接。

## 配置项目存储空间保留设置

日志将在默认保留期限（55 天）过后过期并被标记为待删除（除非[保存到数据集](#create)，否则不会过期）。您可以将项目的日志保留期限配置为最长 7 天、14 天、28 天或 55 天。

## 创建和共享数据集

您可以将日志保存到数据集中，以便更有效地整理和导出日志。

- 在[日志页面](https://aistudio.google.com/logs?hl=zh-cn)中，找到顶部的过滤条件栏，选择要作为过滤条件的属性。
- 在过滤后的视图中，使用复选框选择所有日志或个别日志。
- 点击列表顶部显示的**创建数据集**按钮。
- 为新数据集命名并添加说明（可选）。
- 您将看到刚刚创建的包含精选日志的数据集。
- 将数据集导出为 CSV、JSONL 文件或导出到 Google 表格，以便进一步分析。

数据集可用于多种不同的应用场景。

- **精心挑选挑战集**：推动未来的改进，重点关注您希望 AI 改进的方面。
- **精心挑选样本集**：例如，从实际使用情况中抽样，以生成来自其他模型的回答；或者收集一系列极端情况，以便在部署前进行常规检查。
- **评估集**：可代表重要功能实际使用情况的集合，用于在其他模型或系统指令迭代之间进行比较。

您可以选择与 Google 共享数据集作为演示示例，从而为 Gemini 的研究和开发做出贡献。

## 限制

目前不支持以下内容的日志记录：

- Imagen 和 Veo 模型
- Gemini 嵌入模型
- Gemini Robotics 模型
- 包含视频、GIF 或 PDF 的输入内容
- Gemini API 中的公开预览版智能体

## 后续步骤

- **使用会话历史记录进行原型设计**：使用 [AI Studio Build](https://aistudio.google.com/apps?hl=zh-cn) 进行氛围编程，并添加 API 密钥以启用 AI 功能的 Gemini API 日志历史记录。
- **使用 Gemini Batch API 重新运行日志**：通过使用 [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) 重新运行日志，使用数据集对模型或应用逻辑的响应进行抽样和评估。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-24。"],[],[]]
