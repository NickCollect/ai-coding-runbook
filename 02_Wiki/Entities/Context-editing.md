---
type: entity
name: Context-editing
aliases: [context editing / clear_tool_uses / clear_thinking]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Server-side 选择性清理对话 history（tool result / thinking block），运行时细粒度控制 Claude 看什么。

## 关键属性

- **Beta header**：`anthropic-beta: context-management-2025-06-27` [[context-editing--bwc]]
- **支持模型**：所有 supported Claude models [[context-editing--bwc]]
- **何时用**：Server-side [[Compaction]] 优先；context-editing 是更细控制场景 [[context-editing--bwc]]
- **两类策略**：
  - **Server-side**（API 端）：`clear_tool_uses_20250919` / `clear_thinking_20251015`
  - **Client-side**（SDK 端）：[[Tool-runner]] 提供 compaction（生成总结替换 full history） [[context-editing--bwc]]
- **Server-side 工作位置**：在 prompt 抵达 Claude **之前**应用；client app 保留 unmodified history（不需同步） [[context-editing--bwc]]
- **`clear_tool_uses_20250919`**：
  - 按时间顺序清最旧 tool result（超阈值时）
  - 替换为 placeholder text 让 Claude 知道被移除
  - 默认仅清 tool result；`clear_tool_inputs: true` 也清 tool call 参数
  - `clear_at_least` —— 最小清理量（保 cache invalidation 值得） [[context-editing--bwc]]
- **`clear_thinking_20251015`**：
  - 管 thinking block；权衡 reasoning 连续性 vs context 空间
  - 默认 `keep` 行为：
    - **Opus**：4.5+ keep ALL；4.1 及更早只 last assistant turn
    - **Sonnet**：4.6+ keep ALL；4.5 及更早只 last
    - **Haiku**：所有 Haiku 直到 4.5 都只 last
  - 跨 model tier 时显式设 `keep` 而不是依赖默认 [[context-editing--bwc]]
- **Prompt caching 交互**：
  - tool result 清理：cached prefix 失效；用 `clear_at_least` 让 cache write 值得
  - thinking block 清理：keep → cache 保（hit + 低 input cost）；clear → 清理点 cache 失效 [[context-editing--bwc]]
- **配置**：
  ```json
  {"context_management": {"edits": [{"type": "clear_tool_uses_20250919"}]}}
  ```
  多个 edit 可组合 [[context-editing--bwc]]
- **Advisor-tool 交互**：`clear_thinking` keep ≠ "all" 会让 advisor cache miss（cost-only） [[advisor-tool--at]]
- **ZDR-eligible** [[context-editing--bwc]]

## 出现来源

_10 summaries reference this entity_ ——
- [[context-editing--bwc]] / [[compaction--bwc]] / [[memory-tool--at]]
- [[adaptive-thinking--bwc]] / [[extended-thinking--bwc]] / [[manage-tool-context--at]]
- [[advisor-tool--at]] / [[tool-runner--at]] / [[messages-create--beta-api]]

## 相关

- [[Compaction]] —— 互补（更粗粒度自动总结）
- [[Memory-tool]] —— 跨 context-editing 边界持久化
- [[Advisor-tool]] —— `clear_thinking` 影响 advisor cache
- [[Prompt-caching]] —— cache 交互敏感
- [[Messages-API]] / [[Context-window]]
