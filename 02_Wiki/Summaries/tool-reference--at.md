---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference
title: "Tool reference"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Web-search-tool, Web-fetch-tool, Code-execution-tool, Advisor-tool, Tool-search-tool-API, MCP-server, Memory-tool, Bash-tool-API, Text-editor-tool, Computer-use-tool-API, Prompt-caching, Structured-outputs]
concepts_referenced: []
---

Directory of Anthropic-provided tools and reference for optional tool-definition properties. Anthropic provides two kinds of tools: **server tools** (execute on Anthropic's infrastructure) and **client tools** (Anthropic defines schema, your app handles execution). Both go in the request's `tools` array alongside user-defined tools.

**Tool catalog.**

| Tool | `type` | Execution | Status |
|---|---|---|---|
| [[Web-search-tool]] | `web_search_20260209`, `web_search_20250305` | Server | GA |
| [[Web-fetch-tool]] | `web_fetch_20260209`, `web_fetch_20250910` | Server | GA |
| [[Code-execution-tool]] | `code_execution_20260120`, `code_execution_20250825` | Server | GA |
| [[Advisor-tool]] | `advisor_20260301` | Server | Beta `advisor-tool-2026-03-01` |
| [[Tool-search-tool-API]] | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` | Server | GA |
| [[MCP-server]] connector | `mcp_toolset` | Server | Beta `mcp-client-2025-11-20` |
| [[Memory-tool]] | `memory_20250818` | Client | GA |
| [[Bash-tool-API]] | `bash_20250124` | Client | GA |
| [[Text-editor-tool]] | `text_editor_20250728`, `text_editor_20250124` | Client | GA |
| [[Computer-use-tool-API]] | `computer_20251124`, `computer_20250124` | Client | Beta `computer-use-2025-11-24`, `computer-use-2025-01-24` |

The tool-search `type` values also accept undated aliases `tool_search_tool_regex` / `tool_search_tool_bm25` resolving to the latest dated version.

**Tool versioning.** Most Anthropic tools carry a `_YYYYMMDD` suffix in `type`. New versions release when behavior, schema, or model support changes; older versions remain available. Versioning relationships:

- *Capability-keyed:* `web_search_20260209` and `web_fetch_20260209` add dynamic content filtering over their predecessors. `code_execution_20260120` adds programmatic tool calling. Both old and new are current; pick based on whether you need the new capability.
- *Model-keyed:* `text_editor_20250728` is for Claude 4 models; `text_editor_20250124` for earlier. Pick based on target model.
- *Variant, not version:* `tool_search_tool_regex_20251119` and `tool_search_tool_bm25_20251119` are two search algorithms released together; neither supersedes the other.
- *Legacy:* `code_execution_20250522` supports only Python; `_20250825` adds Bash and file operations.

`mcp_toolset` is not date-versioned—versioning lives in the `anthropic-beta` header.

**Tool definition properties.** Every tool in `tools`, including user-defined, accepts optional properties. They compose—you can set multiple on the same tool.

| Property | Purpose | Available on |
|---|---|---|
| `cache_control` | Set a [[Prompt-caching]] breakpoint at this tool definition | All tools |
| `strict` | Guarantee schema validation on tool names and inputs ([[Structured-outputs]]) | All tools except `mcp_toolset` |
| `defer_loading` | Exclude from initial system prompt; load on demand when [[Tool-search-tool-API]] returns a `tool_reference` | All tools (mcp_toolset uses MCPToolset config instead) |
| `allowed_callers` | Restrict who can call the tool | All tools except `mcp_toolset` |
| `input_examples` | Example input objects to help Claude call the tool | User-defined and Anthropic-schema client tools (NOT server tools) |
| `eager_input_streaming` | Enable fine-grained input streaming | User-defined tools only |

**`allowed_callers` values.** Array accepting any combination of:
- `"direct"`: model can call this tool directly via a `tool_use` block (default if omitted).
- `"code_execution_20260120"`: code running inside a `code_execution_20260120` sandbox can call this tool.

Omitting `"direct"` (e.g., `["code_execution_20260120"]` only) means the tool is callable only from inside code execution. The response's `tool_use` block includes a `caller` field identifying which caller invoked the tool.

**`defer_loading` and prompt caching.** Tools with `defer_loading: true` are stripped from the rendered tools section *before* the cache key is computed—they don't appear in the system-prompt prefix at all. When tool search discovers a deferred tool and returns a `tool_reference`, the tool's full definition expands inline at that point in the conversation body, not in the prefix. This **preserves your prompt cache**: you can add deferred tools to a request without invalidating an existing cache entry, and the cache stays valid across the discovery and call turns.
