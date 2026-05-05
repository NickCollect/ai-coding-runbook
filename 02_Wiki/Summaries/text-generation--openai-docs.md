---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/text-generation.md
source_url: https://platform.openai.com/docs/guides/text-generation
title: "OpenAI — Text Generation"
summarized_at: 2026-05-05
entities_referenced: [Structured-outputs, Prompt-caching]
concepts_referenced: [Context-window]
---

## 核心要点

通过 Responses API 调用 OpenAI 模型生成文本，可生成代码、数学公式、JSON 数据或散文。

### 推荐使用 Responses API

新应用建议使用 Responses API（而非旧版 Chat Completions API），推理模型尤其受益。

### 消息角色

- `developer`：高优先级指令（应用开发者定义）
- `user`：终端用户输入
- `assistant`：模型生成内容

通过 `instructions` 参数提供系统级指令（比 `developer` 消息优先级更高，但仅对当前请求有效）。

### Reusable prompts

通过 dashboard 创建含变量占位符的模板，API 中用 `prompt` 参数引用（`id`、`version`、`variables`）。

### 最新前沿模型（2026 年 5 月）

| 模型 | Input 价格 | Output 价格 | Context |
|---|---|---|---|
| `gpt-5.5` | $5/MTok | $30/MTok | 1M |
| `gpt-5.4` | $2.50/MTok | $15/MTok | 1M |
| `gpt-5.4-mini` | $0.75/MTok | $4.50/MTok | 400K |
| `gpt-5.4-nano` | 最低 | 最低 | — |

### 最佳实践

- 生产应用 pin 到具体模型快照（如 `gpt-5-2025-08-07`）确保行为一致
- 建立 eval 监控 prompt 性能
