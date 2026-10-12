---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-CN
fetched_at: 2026-10-12T07:08:52.900135+00:00
title: "\u4f18\u5148\u7ea7\u63a8\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 优先级推理

说明：了解如何通过 Interactions API 中的 Priority 推理层优化延迟时间

Gemini Priority API 是一种高级推理层级，专为需要低延迟和最高可靠性的业务关键型工作负载而设计，价格较高。优先层级的流量优先于标准 API 和灵活层级的流量。

优先推理功能适用于所有 Interactions API 端点。

## 如何使用“优先级”

如需使用 Priority 层级，请将请求中的 `service_tier` 字段设置为 `priority`。如果省略此字段，则默认层级为标准。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
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
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## 优先级推理的工作原理

优先级推理会将请求路由到高关键性计算队列，从而为面向用户的应用提供可预测的快速性能。其主要机制是，当流量超出动态限制时，服务器端会平稳降级为标准处理，从而确保应用稳定性，而不是使请求失败。

| 功能 | 优先级 | 标准 | Flex | 批量 |
| --- | --- | --- | --- | --- |
| **价格** | 比标准版多 75-100% | 全价票 | 5 折优惠 | 5 折优惠 |
| **延迟时间** | 秒 | 秒到分钟 | 分钟数（目标为 1-15 分钟） | 最长 24 小时 |
| **可靠性** | 高（不可脱落） | 高 / 中高 | 尽力而为（可舍弃） | 高（针对吞吐量） |
| **接口** | 同步 | 同步 | 同步 | 异步 |

### 主要优势

- **低延迟**：专为面向用户的交互式 AI 工具而设计，可实现秒级响应时间。
- **高可靠性**：流量被视为具有最高严重性，并且严格不可丢弃。
- **平稳降级**：如果流量峰值超出动态限额，系统会自动将流量降级到标准层级进行处理，而不是失败，从而防止服务中断。
- **低摩擦**：使用与标准层级和 Flex 层级相同的同步 `create` 方法。

### 使用场景

优先处理非常适合性能和可靠性至关重要的关键业务工作流。

- **交互式 AI 应用**：客户服务聊天机器人和 Copilot，用户支付高价，希望获得快速、一致的回答。
- **实时决策引擎**：需要高度可靠、低延迟结果的系统，例如实时工单分流或欺诈检测。
- **高级客户功能**：需要为付费客户保证更高服务等级目标 (SLO) 的开发者。

### 速率限制

即使优先级消耗量计入[总体互动流量速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)，优先级消耗量也有自己的速率限制。优先级推理的默认速率限制为**模型 / 层级的标准速率限制的 0.3 倍**

### 安全降级逻辑

如果因拥塞而超出优先级限制，溢出请求会**自动且平稳地**降级为标准处理，而不是因 503 或 429 错误而失败。降级后的请求按标准费率计费，而不是按 Priority 优先费率计费。

### 客户责任

- **响应监控**：开发者应监控 API 响应中的 `x-gemini-service-tier` 标头，以检测请求是否经常降级为 `standard`。
- **重试**：客户端必须针对标准错误（例如 `DEADLINE_EXCEEDED`）实现重试逻辑/指数退避算法。

## 价格

优先推理的价格比[标准 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn) 高出 75-100%，按 token 收费。

## 支持的模型

以下模型支持优先推理：

| 模型 | 优先级推理 |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 后续步骤

- [灵活推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)，以降低成本。
- [token](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)：了解 token。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-09。"],[],[]]
