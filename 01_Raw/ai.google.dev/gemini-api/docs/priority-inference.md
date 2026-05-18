---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-CN
fetched_at: 2026-05-18T05:19:13.760261+00:00
title: "\u4f18\u5148\u7ea7\u63a8\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 优先级推理

Gemini Priority API 是一种高级推理层级，专为需要低延迟和最高可靠性的业务关键型工作负载而设计，价格较高。优先层级的流量优先于标准 API 和灵活层级的流量。

GenerateContent API 和 Interactions API 端点支持 [Tier 2 和 Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#about-billing) 用户进行优先级推理。

## 如何使用优先级

如需使用“优先”层级，请将请求正文中的 `service_tier` 字段设置为 `priority`。如果省略此字段，则默认层级为标准。

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3-flash-preview",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
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
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## 优先级推理的运作方式

优先级推理会将请求路由到高严重性计算队列，从而为面向用户的应用提供可预测的快速性能。其主要机制是，当流量超出动态限制时，服务器端会平稳降级为标准处理，从而确保应用稳定性，而不是使请求失败。

| 功能 | 优先级 | 标准 | Flex | 批量 |
| --- | --- | --- | --- | --- |
| **价格** | 比标准层级高 75-100% | 全价票 | 5 折优惠 | 5 折优惠 |
| **延迟时间** | 秒 | 秒到分钟 | 分钟（目标时长为 1-15 分钟） | 最长 24 小时 |
| **可靠性** | 高（不易掉毛） | 高 / 中高 | 尽力而为（可舍弃） | 高（针对吞吐量） |
| **接口** | 同步 | 同步 | 同步 | 异步 |

### 主要优势

- **低延迟**：专为面向用户的交互式 AI 工具而设计，可实现秒级响应时间。
- **高可靠性**：流量被视为最高优先级，并且严格不可丢弃。
- **优雅降级**：如果流量峰值超过动态限制，系统会自动将流量降级到标准层级进行处理，而不是失败，从而防止服务中断。
- **低摩擦**：使用与标准层级和 Flex 层级相同的同步 `generateContent` 方法。

### 使用场景

优先处理非常适合对性能和可靠性要求极高的关键业务工作流。

- **互动式 AI 应用**：客户服务聊天机器人和 Copilot，用户支付高价，希望获得快速、一致的回答。
- **实时决策引擎**：需要高度可靠、低延迟结果的系统，例如实时工单分流或欺诈检测。
- **高级客户功能**：需要为付费客户保证更高服务等级目标 (SLO) 的开发者。

### 速率限制

即使优先级消耗计入[总体交互式流量速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)，它也有自己的速率限制。优先级推理的默认速率限制为**模型 / 层级标准速率限制的 0.3 倍**

### 优雅降级逻辑

如果因拥塞而超出优先级限制，溢出请求会**自动且平稳地**降级为标准处理，而不是因 503 或 429 错误而失败。降级后的请求按标准费率计费，而不是按 Priority Premium 费率计费。

### 客户责任

- **响应监控**：开发者应监控 API 响应中的 `x-gemini-service-tier` 标头，以检测请求是否经常降级为 `standard`。
- **重试**：客户端必须针对标准错误（例如 `DEADLINE_EXCEEDED`）实现重试逻辑/指数退避算法。

## 价格

优先级推理的价格比[标准 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn) 高出 75-100%，按令牌数计费。

## 支持的模型

以下模型支持优先推理：

| 模型 | 优先级推理 |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Pro Image 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash 图片](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 后续步骤

不妨了解 Gemini 的其他[推理和优化](https://ai.google.dev/gemini-api/docs/optimization?hl=zh-cn)选项：

- [灵活推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)，可将费用降低 50%。
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)，可在 24 小时内进行异步处理。
- [上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)，可降低输入 token 费用。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-13。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-13。"],[],[]]
