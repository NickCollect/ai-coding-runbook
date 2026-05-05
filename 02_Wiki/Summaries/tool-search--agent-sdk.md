---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/tool-search.md
source_url: https://code.claude.com/docs/en/agent-sdk/tool-search
title: "Scale to many tools with tool search"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server]
concepts_referenced: [Context-window, Tool-use]
---

Tool search lets agents work with hundreds–thousands of tools by withholding tool definitions from context and loading 3–5 most-relevant ones on demand per task. Solves two scaling pains:
- **Context cost**: 50 tool defs ≈ 10–20K tokens.
- **Selection accuracy**: degrades with > 30–50 tools loaded.

**On by default.** Configure via `ENABLE_TOOL_SEARCH` env var (set in `query()` `env` option):
- unset / `true` — always on.
- `auto` — activates when combined tool-def tokens exceed 10% of context window.
- `auto:N` — same threshold at N percent (e.g. `auto:5` activates at 5%).
- `false` — off, all defs loaded every turn.

Cost: one extra round-trip the first time Claude searches; for large tool sets the saved per-turn context offsets it. With < ~10 tools, loading everything upfront is faster — set `false`.

**Model support**: Sonnet 4+, Opus 4+. **Haiku unsupported.**

If conversation compacts, previously discovered tools may be evicted; the agent searches again as needed.

**Optimize discovery**: use descriptive names (`search_slack_messages` > `query_slack`) and keyword-rich descriptions ("Search Slack messages by keyword, channel, or date range" > "Query Slack"). Add a system prompt section listing tool categories to give the agent search hints.

**Limits**: 10,000 tools max in catalog; 3–5 results per search. Applies across all registered tools (remote MCP servers + custom SDK MCP servers); `auto` threshold uses combined size across all servers.
