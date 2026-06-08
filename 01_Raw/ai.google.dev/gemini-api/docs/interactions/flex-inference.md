---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=zh-CN
fetched_at: 2026-06-08T05:32:52.433442+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Flex 推理

Gemini Flex API 是一种推理层级，与标准费率相比，可将成本降低 50%，但延迟时间不确定，并且仅提供尽力而为的可用性。它适用于对延迟容忍度较高的工作负载，这些工作负载需要同步处理，但不需要标准 API 的实时性能。

## 如何使用 Flex

如需使用 Flex 层级，请在请求中将 `service_tier` 指定为 `flex`。默认情况下，如果省略此字段，请求将使用标准层。

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## 灵活推理的工作原理

Gemini Flex 推理弥合了标准 API 与 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn) 的 24 小时周转时间之间的差距。它利用非高峰时段的“可分流”计算容量，为后台任务和顺序工作流提供经济高效的解决方案。

| 功能 | Flex | 优先级 | 标准 | 批量 |
| --- | --- | --- | --- | --- |
| **价格** | 5 折优惠 | 比标准版多 75-100% | 全价票 | 5 折优惠 |
| **延迟时间** | 分钟（目标时长为 1-15 分钟） | 低（秒） | 秒到分钟 | 最长 24 小时 |
| **可靠性** | 尽力而为（可舍弃） | 高（不掉毛） | 高 / 中高 | 高（针对吞吐量） |
| **接口** | 同步 | 同步 | 同步 | 异步 |

### 主要优势

- **成本效益**：可大幅节省非生产评估、后台代理和数据丰富化的费用。
- **低摩擦**：只需向现有请求添加一个参数即可。
- **同步工作流**：非常适合顺序 API 链，其中下一个请求取决于上一个请求的输出，因此比批量处理更灵活，适合智能体工作流。

### 使用场景

- **离线评估**：运行“LLM 即裁判”回归测试或排行榜。
- **后台代理**：可接受数分钟延迟的顺序任务，例如 CRM 更新、个人资料构建或内容审核。
- **受预算限制的研究**：需要在有限的预算下使用大量 token 的学术实验。

### 速率限制

灵活推理流量会计入常规[速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)；它不会像 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn) 那样提供扩展速率限制。

### 可减少的容量

灵活流量的处理优先级较低。如果标准流量出现峰值，为了确保高优先级用户的容量，系统可能会抢占或逐出灵活请求。如果您需要高优先级的推理，请查看[优先推理](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=zh-cn)

### 错误代码

当灵活容量不可用或系统拥塞时，API 将返回标准错误代码：

- **503 服务不可用**：系统目前已达到容量上限。
- **429 请求过多**：速率限制或资源耗尽。

### 客户责任

- **无服务器端回退**：为避免产生意外费用，如果 Flex 容量已满，系统不会自动将 Flex 请求升级为标准层级。
- **重试**：您必须实现自己的客户端重试逻辑，并使用指数退避算法。
- **超时**：由于 Flex 请求可能会排队，我们建议将客户端超时时间增加到 10 分钟或更长时间，以避免过早关闭连接。

## 调整超时时间范围

您可以为 REST API 和客户端库配置每个请求的超时时间。
请务必确保客户端超时时间涵盖预期的服务器耐心等待时间（例如，对于 Flex 等待队列，超时时间应为 600 秒以上）。SDK 需要以毫秒为单位的超时值。

### 每个请求的超时时间

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## 实现重试

由于 Flex 是可舍弃的，并且会因失败而返回 503 错误，因此以下示例展示了如何选择性地实现重试逻辑，以继续处理失败的请求：

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## 价格

灵活推理的价格为[标准 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn) 的 50%，按 token 数计费。

## 支持的模型

以下模型支持 Flex 推理：

| 模型 | Flex 推理 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 后续步骤

- [优先推理](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=zh-cn)，实现超低延迟。
- [token](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-cn)：了解 token。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-28。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-28。"],[],[]]
