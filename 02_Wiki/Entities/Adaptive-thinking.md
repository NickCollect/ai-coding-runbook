---
type: entity
name: Adaptive-thinking
aliases: [adaptive thinking / thinking adaptive]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

让 Claude 自决要不要思考 + 思考多深 —— `thinking: {type: "adaptive"}`，**Opus 4.7 上唯一支持的 thinking 模式**。

## 关键属性

- **Config**：`thinking: {type: "adaptive"}` in Messages API body；无 beta header；ZDR-eligible [[adaptive-thinking--bwc]]
- **模型支持矩阵**：
  - **Opus 4.7**：adaptive 是**唯一支持**模式；manual `enabled` + `budget_tokens` 直接 400
  - **Mythos Preview**：adaptive 是默认（thinking 未设时），`disabled` 不支持
  - **Opus 4.6 / Sonnet 4.6**：adaptive 推荐；manual `enabled` + `budget_tokens` 仍可用但 deprecated
  - **更早模型（Sonnet 4.5 / Opus 4.5 等）**：必须 manual `enabled` 模式 [[adaptive-thinking--bwc]] [[Extended-thinking]]
- **自动启用 interleaved thinking**：tool calls 之间也思考；Mythos Preview / Opus 4.7 上 inter-tool 推理总在 thinking blocks 里 [[adaptive-thinking--bwc]]
- **Effort 软引导**：`max` / `xhigh` / `high`（默认） / `medium` / `low` —— low 跳简单任务、medium 选择性、high+ 总是思考（详见 [[Effort]]） [[adaptive-thinking--bwc]]
- **Validation 更宽松**：previous assistant turn 不必以 thinking block 开头（manual 模式严格） [[adaptive-thinking--bwc]]
- **Prompt caching**：连续 adaptive 请求保 cache breakpoint；adaptive ↔ enabled/disabled 切换 → message cache breakpoint 失效（system prompt + tools 仍 cache） [[adaptive-thinking--bwc]] [[Prompt-caching]]
- **System prompt 可调**：能让 Claude 多想或少想 [[adaptive-thinking--bwc]]
- **Cost control**：`max_tokens` 是 thinking + text 硬上限；high/max effort 可能耗光 → 注意 `stop_reason: "max_tokens"` [[adaptive-thinking--bwc]]
- **Streaming**：thinking blocks 通过 `thinking_delta` 流 [[adaptive-thinking--bwc]] [[Streaming-API]]
- **Display 模式**：
  - `summarized` —— 返回总结（Opus 4.6 / Sonnet 4.6 默认）
  - `omitted` —— `thinking` field 空，仅 `signature`（Opus 4.7 / Mythos Preview 默认；TTFT 更快） [[adaptive-thinking--bwc]]
- **Signature**：opaque encrypted、跨 summarized/omitted 一致、跨 Anthropic API / Bedrock / Vertex 兼容；多 turn tool use 必须 unchanged 传回 [[adaptive-thinking--bwc]]
- **Pricing**：billed for full original thinking tokens（不是 summary）；summary 生成本身免费（不同模型生成） [[adaptive-thinking--bwc]]

## 出现来源

_7 summaries reference this entity_ ——
- [[adaptive-thinking--bwc]] / [[extended-thinking--bwc]] / [[effort--bwc]]
- [[create--msg-api]] / [[messages-create--beta-api]]
- [[handling-stop-reasons--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Extended-thinking]] —— adaptive 是 extended thinking 的"自动"模式；manual `{type: "enabled", budget_tokens}` 是手动模式
- [[Effort]] —— effort + adaptive thinking 配合
- [[Messages-API]] / [[Streaming-API]] / [[Prompt-caching]]
- [[Enterprise-gateway]] —— Bedrock / Vertex 跨平台兼容
