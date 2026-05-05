---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/reasoning.md
source_url: https://platform.openai.com/docs/guides/reasoning
title: "OpenAI — Reasoning Models"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Context-window]
---

## 核心要点

Reasoning models（如 `gpt-5.5`）在生成最终响应前进行内部"思考"（使用 reasoning tokens），适合复杂多步任务。

### 推荐模型

| 用途 | 模型 |
|---|---|
| 最佳推理能力 | `gpt-5.5` |
| 低成本推理 | `gpt-5.4-mini` |
| 传统推理模型 | `o3`、`o4-mini` |

### `reasoning.effort` 参数

控制推理深度，影响 token 用量和响应质量：

- `none`：不推理（最快最便宜）
- `low`：快速轻量推理
- `medium`：默认
- `high`：复杂问题
- `xhigh`：最高质量，token 用量最大

### Reasoning Tokens

内部推理消耗的 token，**计入计费但不返回给用户**（不出现在响应 content 中）。

```json
{
  "usage": {
    "input_tokens": 75,
    "output_tokens": 1186,
    "output_tokens_details": { "reasoning_tokens": 1024 },
    "total_tokens": 1261
  }
}
```

### Context Window 管理

多轮对话中推理 token 累积占用大量 context。建议：
- 使用 `previous_response_id` 链接对话（让 API 管理历史，只计费新增 tokens）
- 通过 `/responses/compact` 压缩历史（参见 compaction 文档）

### 在 Function Call 中传递 Reasoning Items

使用 Responses API 时，建议将上一轮的 `reasoning` output item 传回下一轮（`include: ["reasoning.encrypted_content"]`），帮助模型保持连贯的多步推理状态。

### Prompting 建议

- 避免 chain-of-thought 提示（模型已内部推理）
- 简洁明确的指令效果优于冗长约束
- 可用 `instructions` 参数设置全局风格/角色
