---
name: Extended Thinking
type: concept
aliases: [Reasoning Models, Thinking Tokens, Internal Reasoning, Long Thinking]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Extended Thinking（扩展推理）

让模型在生成最终答案前，先进行不限于单次前向传播的多步骤内部推理的能力。区别于普通 CoT（明文输出），扩展推理的"思考过程"可能对用户部分或完全不可见，且按独立 token 计费。

## 核心机制

模型在生成 `text` 答案前先输出 `thinking` 内容块——一段自由形式的内部推理。推理 token 消耗计入 output token 计费。关键特性：

- **思考 vs 答案分离**：`thinking` 块不直接出现在最终回复中，但通过 `signature`（加密签名）保证完整性
- **Token 预算**：通过 `budget_tokens` 控制推理深度（更多 budget → 更深入推理，但更贵更慢）
- **自适应推理**：新一代模型（Claude Opus 4.7+）自动决定是否需要推理及推理深度，无需手动配置

**适用场景提升最明显的任务**：
- 复杂数学推导
- 多步骤代码 debug
- 需要比较多个方案的决策问题
- 科学/逻辑推理

**忠实性警告**（Anthropic 研究，2023）：CoT/thinking 输出不一定反映模型真实计算过程；更大的模型在多数任务中产生更不忠实的推理。Extended thinking 的"显示输出"可能是后验合理化而非前向推导。

## 跨厂商实现

**Claude**：
- **Opus 4.7+**（最新）：`budget_tokens` 手动设置**被拒绝（400 错误）**。改用 Adaptive Thinking + `effort` 参数（`"low"/"medium"/"high"`）
- **Opus 4.6 / Sonnet 4.6**：推荐 adaptive，手动 `enabled` 已废弃但仍工作
- **Sonnet 3.7 等旧模型**：手动模式，返回完整 thinking（未摘要）
- `display` 字段：`"summarized"`（返回推理摘要）| `"omitted"`（签名返回但不显示，TTFT 更快）
- Interleaved thinking：工具调用之间也可推理
- **ZDR 兼容**（Zero Data Retention）

**OpenAI**：
- o3、o4-mini 等推理模型，thinking token 完全内部（用户不可见）
- `reasoning.effort: "low"/"medium"/"high"` 控制推理深度
- `reasoning_tokens` 字段显示消耗的推理 token 数（计费）

**Gemini**：
- Gemini 2.0 Flash Thinking Experimental、Gemini 2.5 Pro 等推理模型
- `thinking_config.thinking_budget` 控制预算（token 数）
- thinking 块在响应中可选择暴露

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `thinking.type: "enabled"` | Claude（旧模型）手动启用 |
| `budget_tokens` | Claude（旧模型）推理 token 上限 |
| `effort: "low"/"high"` | Claude Opus 4.7+ / OpenAI：推理深度 |
| `display: "omitted"/"summarized"` | Claude：thinking 内容可见性 |
| `reasoning.effort` (OpenAI) | OpenAI 推理模型深度控制 |
| `max_tokens` | 必须 > `budget_tokens`（Claude） |

## 使用场景

**用**：数学竞赛题、长链条逻辑推理、复杂代码架构分析、多约束优化决策。

**不用**：简单问答、实时对话（TTFT 高）、创意写作（推理无益）、成本极度敏感的高频调用。

**成本注意**：thinking token 按 output token 价格计费，实际账单可能远高于最终输出 token 数。

## 相关

- [[Extended-thinking]] — Claude 扩展推理 entity 档案（含详细 API 参数）
- [[chain-of-thought]] — CoT 是 extended thinking 的 prompt 层前身
- [[Effort]] — Claude effort 参数 entity
- [[Adaptive-thinking]] — Claude adaptive thinking entity
- [[cost-optimization]] — 推理 token 成本高，合理使用 effort 参数

## 出现来源

- [[extended-thinking--bwc]]
- [[measuring-faithfulness-in-chain-of-thought-reasoning--anthropic-research]]
- [[reasoning--openai-docs]]
