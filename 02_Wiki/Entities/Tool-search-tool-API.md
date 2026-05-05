---
type: entity
name: Tool-search-tool-API
aliases: [tool search / tool_search_tool_regex / tool_search_tool_bm25]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

让 Claude 在大 tool catalog 中按需搜 + 加载 tool 定义，避免 [[Context-window]] 被几千 tool schema 撑爆（**与 Claude Code 内置的 ToolSearch / [[Permission-mode]] 自动模式区分**）。

## 关键属性

- **两个变体**：
  - `tool_search_tool_regex_20251119`：Claude 写 Python `re.search()` regex（max 200 chars，例 `"weather"` / `"get_.*_data"` / `"(?i)slack"`）
  - `tool_search_tool_bm25_20251119`：自然语言 query
  - 未带日期 alias `tool_search_tool_regex` / `tool_search_tool_bm25` 解析到最新 [[tool-search-tool--at]]
- **Mechanism**：
  1. Add tool search variant + 标 deferred tools `defer_loading: true`
  2. Claude 初始只看 search tool + 非 deferred
  3. Claude 搜 → API 返回 3-5 `tool_reference` block
  4. references 自动展开 full definition
  5. Claude 调发现的 tool [[tool-search-tool--at]]
- **关键规则**：
  - 无 `defer_loading` 立即加载
  - search tool 自身 **绝不能** `defer_loading: true`（400）
  - 3-5 高频 tool 保留 non-deferred
  - 每 `tool_reference` 必须有 top-level `tools` 中的 definition（否则 400） [[tool-search-tool--at]]
- **Cache 保留**：deferred tool 从 system prompt prefix 剥离 → cache key 不变；discovered tool 作为 `tool_reference` block 在 conversation body inline → [[Prompt-caching]] 跨发现 + 调用都保 [[tool-search-tool--at]]
- **Effect**：典型多 server (GitHub + Slack + Sentry + Grafana + Splunk) ~55K token 节省 **>85%**；selection accuracy 在 30-50 tool 后明显下降，search 解决 [[tool-search-tool--at]]
- **Limits**：max **10,000 tools**；返回 3-5 results；regex pattern max 200 chars；模型 Mythos Preview / Sonnet 4.0+ / Opus 4.0+ / Haiku 4.5+ [[tool-search-tool--at]]
- **Custom tool search**：可 client-side 用 embedding / semantic search 实现，custom tool 返回 `tool_reference` block；每个被引用 tool 必须 top-level `tools` + `defer_loading: true`；cookbook 有 embedding example [[tool-search-tool--at]]
- **MCP integration**：[[MCP-server]] toolset 也支持 `defer_loading`（详见 mcp-connector） [[mcp-connector--at]]
- **不兼容**：`input_examples`（tool use 例）—— 用 strict tool calling 替代 [[tool-search-tool--at]]
- **Optimization**：服务前缀命名（`github_` / `slack_`）、descriptive name、semantic keywords、system prompt 列 categories
- **Bedrock**：仅 invoke API，不在 converse API [[tool-search-tool--at]]
- **Streaming + Batches-API 兼容** [[tool-search-tool--at]]
- **Errors**：`invalid_pattern` / `pattern_too_long` / `unavailable` / 400 "All tools have defer_loading set" / "Tool reference X has no corresponding tool definition" [[tool-search-tool--at]]

## 出现来源

_14 summaries reference this entity_ ——
- [[tool-search-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]]
- [[mcp-connector--at]] / [[manage-tool-context--at]] / [[server-tools--at]]
- [[api-and-data-retention--bwc]] / [[adaptive-thinking--bwc]]

## 相关

- [[MCP-server]] —— MCP toolset 同样支持 defer_loading
- [[Tool-use]] / [[Messages-API]]
- [[Prompt-caching]] —— cache 兼容设计
- [[Permission-mode]] —— Claude Code 内置 ToolSearch（不同概念）
