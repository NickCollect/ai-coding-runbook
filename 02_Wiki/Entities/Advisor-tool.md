---
type: entity
name: Advisor-tool
aliases: [advisor / advisor_20260301]
category: api-tool
status: beta
created: 2026-05-05
---

## 一句话定义

混合模型策略 —— 让 fast/便宜 executor 模型在 mid-generation 咨询更强 advisor 模型，executor 拿到 plan/纠正后继续，避免全程跑昂贵模型。

## 关键属性

- **Beta header**：`advisor-tool-2026-03-01` [[advisor-tool--at]]
- **Tool definition**：`{type: "advisor_20260301", name: "advisor", model: "claude-opus-4-7"}` [[advisor-tool--at]]
- **何时用**：long-horizon agentic（coding / computer use / multi-step research），多数 turn 机械但 plan 关键；推荐 Sonnet executor + Opus advisor 或 Haiku executor + Opus advisor [[advisor-tool--at]]
- **不适合**：single-turn Q&A、pass-through model picker、每 turn 都需 advisor full capability [[advisor-tool--at]]
- **模型兼容**：advisor 必须 ≥ executor 能力；当前 advisor 唯一可选 = Opus 4.7；executor 可 = Haiku 4.5 / Sonnet 4.6 / Opus 4.6 / Opus 4.7 [[advisor-tool--at]]
- **Mechanism**（一 `/v1/messages` 内）：executor 发 `server_tool_use`（input 空，时机由 executor 控）→ Anthropic server-side sub-inference 跑 advisor 传 full transcript → 结果 `advisor_tool_result` → executor 继续；无额外 round trip [[advisor-tool--at]]
- **Advisor 输出**：典型 400-700 text token + 1.4-1.8K total（含 thinking）；advisor 不带 tool / 无 context management [[advisor-tool--at]]
- **Tool params**：
  - `max_uses` (default unlimited) —— 超 → `error_code: "max_uses_exceeded"`
  - `caching: {"type": "ephemeral", "ttl": "5m" | "1h"}` —— 启用 advisor-side 缓存（开关，非 breakpoint） [[advisor-tool--at]]
- **Result variants**：discriminated union —— `advisor_result` (text plaintext) 或 `advisor_redacted_result` (encrypted_content opaque blob)；下一轮原样回传 [[advisor-tool--at]]
- **Errors**：`max_uses_exceeded` / `too_many_requests` / `overloaded` / `prompt_too_long` / `execution_time_exceeded` / `unavailable`（不让 request fail，executor 继续无 advice） [[advisor-tool--at]]
- **Multi-turn**：必须传回完整 assistant content 含 advisor block；移除 advisor tool 但 history 仍含 result block → 400；要 cap 必同时移 tool + 删 history advisor block [[advisor-tool--at]]
- **Streaming**：advisor 不 stream，executor SSE 暂停在 `server_tool_use` close，~30s ping；result 单 `content_block_start`（无 delta） [[advisor-tool--at]]
- **Billing**：`usage.iterations[]` with `type: "advisor_message"` 按 advisor 模型计；top-level `usage` 仅 executor；`output_tokens` sum 全 executor iteration；`input_tokens` / `cache_read_input_tokens` 仅第一次；`max_tokens` 不 bound advisor [[advisor-tool--at]]
- **Caching**：两层 —— executor-side `cache_control` on `advisor_tool_result`；advisor-side `caching` field；break-even ≈ 3 advisor call per conversation；[[Context-editing]] `clear_thinking` keep ≠ "all" 会 cache miss（cost-only） [[advisor-tool--at]]
- **Best practices**：early call、stuck call、coding task 加 system prompt block 时机指引 + 权重；"advisor should respond <100 words enumerated steps" cut 35-45% [[advisor-tool--at]]
- **Limitations**：no streaming、no built-in conversation cap、`max_tokens` 不 bound advisor、Anthropic Priority Tier 按 model 各自 honor [[advisor-tool--at]]
- **Combine**：与 [[Web-search-tool]] / custom bash tool 等组合；[[Batches-API]] 支持（`usage.iterations` per item） [[advisor-tool--at]]
- **ZDR-eligible** [[advisor-tool--at]]

## 出现来源

_8 summaries reference this entity_ ——
- [[advisor-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[server-tools--at]] / [[manage-tool-context--at]]
- [[adaptive-thinking--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Tool-use]] / [[Messages-API]]
- [[Extended-thinking]] / [[Effort]] —— Sonnet executor + Opus advisor 配 medium effort
- [[Context-editing]] —— `clear_thinking` 影响 advisor cache
- [[Prompt-caching]] —— advisor + executor 双层 cache
- [[Batches-API]] —— 支持
