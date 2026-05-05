---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/prompt-caching.md
source_url: https://platform.openai.com/docs/guides/prompt-caching
title: "OpenAI — Prompt Caching"
summarized_at: 2026-05-05
entities_referenced: [Prompt-caching]
concepts_referenced: [Context-window]
---

## 核心要点

OpenAI API 自动缓存重复 prompt 前缀，降低延迟和成本，对开发者透明（无需配置）。

### 工作原理

- 缓存以 1024 token 为粒度，prompt 前缀匹配时命中
- 路由：同一 prefix hash 的请求被路由到同一服务器，保证缓存利用率
- 命中后：latency 降低 **80%**，cached input token 按正常价格的 **10%** 计费

### 检测命中

通过响应 `usage` 字段判断：

```json
"usage": {
  "prompt_tokens": 2006,
  "prompt_tokens_details": { "cached_tokens": 1920 }
}
```

### 缓存保留策略

| 策略 | 时长 | 适用场景 |
|---|---|---|
| 默认（内存） | 几分钟到几小时（流量驱动） | 一般 API 使用 |
| Extended cache | 24 小时 | 高流量或批量任务 |

### 最佳实践

- **静态内容前置**：system prompt、examples、历史 messages 放在 prompt 最前面（缓存只检查前缀）
- **延迟新内容**：动态部分（最新用户 query）放最后，保证静态前缀一致
- **prefix ≥ 1024 tokens** 才有效，越长越划算
- 复用同一个 `response_id` 链式对话时，前几轮 messages 会自动命中缓存

### 可缓存内容

文本 token、图片、工具定义、结构化输出 schema。

模型权重参数不缓存（只缓存 KV cache 即 attention 中间状态）。
