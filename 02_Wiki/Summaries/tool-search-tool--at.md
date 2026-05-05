---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
title: "Tool search tool"
summarized_at: 2026-05-05
entities_referenced: [Tool-search-tool-API, Tool-use, MCP-server, Prompt-caching, Batches-API, Streaming-API]
concepts_referenced: [Context-window]
---

The [[Tool-search-tool-API]] enables Claude to work with hundreds or thousands of tools by *dynamically discovering and loading them on-demand*. Instead of loading all tool definitions into the [[Context-window]] upfront, Claude searches your tool catalog (names, descriptions, argument names + descriptions) and loads only what it needs. Solves two scaling problems: **context bloat** (a typical multi-server setup like GitHub + Slack + Sentry + Grafana + Splunk eats ~55k tokens before any work; tool search typically reduces this **by over 85%**) and **selection accuracy** (Claude's ability to pick the right tool degrades significantly past 30–50 available tools). **Eligible for ZDR.**

**Two variants.**
- **Regex** (`tool_search_tool_regex_20251119`): Claude constructs **Python `re.search()` regex patterns**, NOT natural language. Examples: `"weather"`, `"get_.*_data"`, `"database.*query|query.*database"` (OR), `"(?i)slack"` (case-insensitive). Max 200 chars.
- **BM25** (`tool_search_tool_bm25_20251119`): Claude uses natural language queries.

Both search names, descriptions, AND argument metadata. Undated aliases (`tool_search_tool_regex` / `tool_search_tool_bm25`) resolve to the latest dated version.

**Mechanism.**
1. Add a tool search variant to your tools list.
2. Mark large/infrequent tools with `defer_loading: true`.
3. Claude initially sees only the search tool + non-deferred tools.
4. When Claude needs more tools, it searches via the search tool.
5. API returns 3–5 most relevant `tool_reference` blocks.
6. References auto-expand into full tool definitions.
7. Claude invokes the discovered tools.

**Critical rules.**
- Tools without `defer_loading` load immediately.
- Tool search tool itself must **NEVER** have `defer_loading: true` (returns 400).
- Keep your 3–5 most frequently used tools as non-deferred for performance.
- Every `tool_reference` requires a corresponding tool definition in `tools` (else 400).

**Cache preservation.** Deferred tools are **stripped from the system-prompt prefix** before the cache key is computed. When discovered via search, the tool definition is appended *inline as a `tool_reference` block in the conversation body*, not in the prefix. So [[Prompt-caching]] is preserved across the discovery turn AND the call turn. The strict-mode grammar builds from the full toolset regardless—`defer_loading` and `strict` compose without grammar recompilation.

**Response format.** Three new block types:
- `server_tool_use` (with `name: "tool_search_tool_regex"` etc.) showing the search query.
- `tool_search_tool_result` containing nested `tool_search_tool_search_result` with `tool_references: [{type: "tool_reference", tool_name: "..."}]`.
- Then the standard `tool_use` block invoking the discovered tool.

**Custom tool search.** You can implement client-side search (using embeddings, semantic search, etc.) by returning `tool_reference` blocks from your own custom tool. Format:
```json
{"type": "tool_result", "tool_use_id": "...", "content": [{"type": "tool_reference", "tool_name": "..."}]}
```
Every referenced tool must have a definition in the top-level `tools` parameter with `defer_loading: true`. Cookbook example uses embeddings.

**MCP integration.** For configuring [[MCP-server]] toolsets with `defer_loading`, see the MCP connector page.

**Error codes.** `too_many_requests`, `invalid_pattern` (malformed regex), `pattern_too_long` (>200 chars), `unavailable`. Common 400 errors: "All tools have defer_loading set" (remove it from the search tool); "Tool reference 'X' has no corresponding tool definition" (add full definition).

**Compatibility.** Not compatible with `input_examples` (tool use examples). Use standard tool calling if you need examples.

**Limits.** Max **10,000 tools** in catalog. Returns 3–5 results per search. Pattern max 200 chars. Models: Claude Mythos Preview, Sonnet 4.0+, Opus 4.0+, Haiku 4.5+.

**When to use.** 10+ tools available; tool definitions consuming >10k tokens; selection accuracy issues with large tool sets; MCP-powered systems with multiple servers (200+ tools); growing tool library. Skip when <10 tools, all frequently used, or definitions <100 tokens total.

**Optimization tips.** Keep 3–5 frequent tools non-deferred. Write descriptive tool names. Use service-prefix namespacing (`github_`, `slack_`). Use semantic keywords matching how users describe tasks. Add a system prompt section listing tool categories. Monitor which tools Claude discovers to refine descriptions. Supports [[Streaming-API]] and [[Batches-API]]. Bedrock note: server-side tool search only via the invoke API, not the converse API.
