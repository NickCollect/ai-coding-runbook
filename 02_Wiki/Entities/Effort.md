---
type: entity
name: Effort
aliases: [effort parameter / output_config.effort]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

`effort` 参数（`output_config.effort`）控制 Claude 的 token 慷慨度 —— 一刀切影响 text + tool calls + thinking 的总输出量。

## 关键属性

- **设置**：`output_config.effort` in Messages API；GA 无 beta header；ZDR-eligible [[effort--bwc]]
- **替代 `budget_tokens`**：Opus 4.6 / Sonnet 4.6 上 `budget_tokens` 已 deprecated，effort 接管 [[effort--bwc]]
- **支持模型**：Mythos Preview / Opus 4.7 / Opus 4.6 / Sonnet 4.6 / Opus 4.5 [[effort--bwc]]
- **5 levels**：
  - `max` —— 无 cost 约束最大能力 (Mythos / Opus 4.7-4.6 / Sonnet 4.6)
  - `xhigh` —— long-horizon agentic / coding > 30 min（**Opus 4.7 only**）
  - `high`（默认） —— 同省略
  - `medium`
  - `low` [[effort--bwc]]
- **行为信号 ≠ 严格 budget**：低 effort 仍会在难题上 think，只是少 [[effort--bwc]]
- **Sonnet 4.6 推荐**：默认 high → 显式设以避免 latency 惊喜；medium = balanced agentic coding；low = 高 vol 低 latency [[effort--bwc]]
- **Opus 4.7 推荐**：默认 high → `xhigh` 是 coding/agent 起点；medium = 平均 workflow；low = 短 scoped；max 仅 frontier 问题（避免 overthinking on structured outputs） [[effort--bwc]]
- **Opus 4.7 vs 4.6**：4.7 更严格遵守 effort 等级，scopes work to 任务范围；shallow reasoning 时升 effort 而不是 prompt 绕 [[effort--bwc]]
- **`xhigh` / `max` 用 large `max_tokens`**：起 64K，给 subagent / tool call 留 room [[effort--bwc]]
- **优于 thinking-only 旋钮**：1) 不需要 thinking 启用 2) 影响所有 token spend 含 tool call 频率 [[effort--bwc]]

## 出现来源

_14 summaries reference this entity_ ——
- [[effort--bwc]] / [[adaptive-thinking--bwc]] / [[extended-thinking--bwc]]
- [[create--msg-api]] / [[messages-create--beta-api]]
- [[handling-stop-reasons--bwc]] / [[task-budgets--bwc]] / [[advisor-tool--at]]

## 相关

- [[Adaptive-thinking]] / [[Extended-thinking]] —— effort 同时控制 thinking budget
- [[Messages-API]] —— `output_config.effort` 字段
- [[Tool-use]] —— effort 影响 tool call 频次
- [[Advisor-tool]] —— Sonnet executor + medium effort + Opus advisor 推荐组合
