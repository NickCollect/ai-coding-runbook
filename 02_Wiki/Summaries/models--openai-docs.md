---
type: summary
source: 01_Raw/docs.openai.com/docs/models.md
source_url: https://platform.openai.com/docs/models
title: "OpenAI — 模型列表（2026 年 5 月）"
summarized_at: 2026-05-05
entities_referenced: [Vision, Embeddings]
concepts_referenced: [Context-window]
---

## 核心要点

OpenAI 当前可用模型总览，所有最新模型支持文本/图像输入、文本输出、多语言、视觉能力。

### 前沿模型（Frontier Models）

| 模型 | Input 价格 | Output 价格 | 延迟 | 最大输出 | Context Window | 知识截止 |
|---|---|---|---|---|---|---|
| gpt-5.5 | $5/MTok | $30/MTok | 快 | 128K | 1M | 2025 年 12 月 |
| gpt-5.4 | $2.50/MTok | $15/MTok | 快 | 128K | 1M | 2025 年 8 月 |
| gpt-5.4-mini | $0.75/MTok | $4.50/MTok | 更快 | 128K | 400K | 2025 年 8 月 |

所有前沿模型支持：Functions、Web search、File search、Computer use。
Reasoning effort：none/low/medium/high/xhigh 全支持。

**模型选择建议**：
- 复杂推理和编码 → `gpt-5.5`（旗舰）
- 成本和延迟优化 → `gpt-5.4-mini` 或 `gpt-5.4-nano`

### 专用模型

| 类型 | 模型 | 说明 |
|---|---|---|
| 图像 | GPT Image 2 | state-of-the-art 图像生成/编辑 |
| 实时语音 | gpt-realtime-1.5 | 最佳语音模型，音频输入/输出 |
| 实时语音 | gpt-realtime-mini | 低成本语音模型 |
| TTS | GPT-4o mini TTS | 文本转语音 |
| 转录 | GPT-4o Transcribe | 语音转文本 |
| 转录 | GPT-4o mini Transcribe | 低成本语音转文本 |

所有模型通过 Responses API 和 Client SDK 访问。
