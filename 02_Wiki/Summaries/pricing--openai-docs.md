---
type: summary
source: 01_Raw/docs.openai.com/docs/pricing.md
source_url: https://openai.com/api/pricing
title: "OpenAI — API 定价"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Prompt-caching]
concepts_referenced: []
---

## 核心要点

OpenAI API 各模型及服务的定价结构（截至 2026 年 5 月）。

### 前沿模型价格（270K tokens 以内的 context）

| 模型 | Input | Cached Input | Output |
|---|---|---|---|
| GPT-5.5 | $5.00/MTok | $0.50/MTok | $30.00/MTok |
| GPT-5.4 | $2.50/MTok | $0.25/MTok | $15.00/MTok |
| GPT-5.4 mini | $0.75/MTok | $0.075/MTok | $4.50/MTok |

### 多模态模型

**GPT-realtime-1.5（语音）**：

| 模态 | Input | Cached | Output |
|---|---|---|---|
| Audio | $32.00/MTok | $0.40/MTok | $64.00/MTok |
| Text | $4.00/MTok | $0.40/MTok | $16.00/MTok |

**GPT-image-2（图像生成）**：Image $8.00/MTok input，$30.00/MTok output

### 内置工具价格

| 工具 | 价格 |
|---|---|
| Web search | $10.00 / 1k 次调用（搜索内容 token 免费） |
| Containers | $0.03/GB 或 $1.92 / 64GB / 20分钟会话 |

### 服务层级

| 层级 | 说明 |
|---|---|
| **Priority processing** | 可靠、高速、按需付费 |
| **Batch API** | 节省 50%，24 小时异步 |
| **Flex processing** | 低成本、慢响应，适合非生产任务 |
| **Reserved Capacity** | 企业大规模工作负载 |

### 价格修正因子摘要

- Cached input token：约为正常 input 价格的 10%
- Batch API：input + output 各 -50%
- Data residency：+10%
