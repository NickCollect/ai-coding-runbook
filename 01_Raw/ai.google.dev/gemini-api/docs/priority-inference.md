---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-CN
fetched_at: 2026-08-03T04:39:00.520477+00:00
title: "\u4f18\u5148\u7ea7\u63a8\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 优先级推理

说明：了解如何使用 Interactions API 中的 Priority 推理层级优化延迟时间

Gemini Priority API 是一种高级推理层级，专为需要更低延迟时间和最高可靠性的关键业务工作负载而设计，价格也相对较高。Priority
层级的流量优先级高于标准 API 和 Flex 层级的流量。

Interactions API 端点均提供 Priority 推理。

## 如何使用 Priority

如需使用 Priority 层级，请将请求中的 `service_tier` 字段设置为 `priority`。如果省略该字段，则默认层级为标准层级。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Priority 推理的工作原理

Priority 推理会将请求路由到高关键性计算队列，为面向用户的应用提供可预测的快速性能。其主要机制是，对于超出动态限制的流量，优雅地在服务器端降级到标准处理，确保应用稳定性，而不是让请求失败。

| 功能 | Priority | 标准版 | Flex | 批量 |
| --- | --- | --- | --- | --- |
| **价格** | 比标准层级高 75-100% | 全价 | 5 折 | 5 折 |
| **延迟时间** | 秒 | 秒到分钟 | 分钟（目标 1-15 分钟） | 最长 24 小时 |
| **可靠性** | 高（不可舍弃） | 高 / 中高 | 尽力而为（可舍弃） | 高（针对吞吐量） |
| **接口** | 同步 | 同步 | 同步 | 异步 |

### 主要优势

- **低延迟时间**：专为交互式
  面向用户的 AI 工具而设计，响应时间为秒级。
- **高可靠性**：流量以最高关键性处理，且
  严格不可舍弃。
- **优雅降级**：超出动态限制的流量峰值会自动降级到标准层级进行处理，而不是失败，从而防止服务中断。
- **低摩擦**：与
  标准层级和 Flex 层级使用相同的同步 `create` 方法。

### 使用场景

Priority 处理非常适合性能和可靠性至关重要的关键业务工作流。

- **交互式 AI 应用**：客户服务聊天机器人和副驾驶，其中
  用户支付额外费用，并期望获得快速、一致的响应。
- **实时决策引擎**：需要高度可靠、低延迟
  结果的系统，例如实时工单分诊或欺诈检测。
- **高级客户功能**：需要为付费客户保证更高服务
  等级目标 (SLO) 的开发者。

### 速率限制

Priority 消耗量有自己的速率限制，即使消耗量计入
[整体交互式流量速率限制](https://aistudio.google.com/rate-limit?hl=zh-cn)也是如此。Priority 推理的默认速率限制为**模型 / 层级的标准速率限制的 0.3 倍**

### 优雅降级逻辑

如果因拥塞而超出 Priority 限制，溢出请求会**自动且优雅地** 降级到标准处理，而不是因 503 或 429 错误而失败。降级的请求按标准费率计费，而不是按 Priority 高级费率计费。

### 客户端责任

- **响应监控**：开发者应监控 API 响应中的 `x-gemini-service-tier`
  标头，以检测请求是否频繁降级到
  `standard`。
- **重试**：客户端必须为
  标准错误（例如 `DEADLINE_EXCEEDED`）实现重试逻辑/指数退避算法。

## 价格

Priority 推理的价格比[标准 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn) 高 75-100%，并按 token 计费。

## 支持的模型

以下模型支持 Priority 推理：

| 模型 | Priority 推理 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 后续步骤

- [Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)，以降低费用。
- [token](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)：了解 token。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
