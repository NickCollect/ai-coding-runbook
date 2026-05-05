---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching
title: "Tool use with prompt caching"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Prompt-caching, Tool-search-tool-API, Web-search-tool, Web-fetch-tool, Code-execution-tool, Computer-use-tool-API, Text-editor-tool, Bash-tool-API, Memory-tool, MCP-server]
concepts_referenced: []
---

How [[Prompt-caching]] interacts with tool definitions: where to place `cache_control` breakpoints, how `defer_loading` preserves cache, and what invalidates it.

**Placing `cache_control` on tool definitions.** Put `cache_control: {"type": "ephemeral"}` on the **last tool** in your `tools` array. This caches the entire tool-definitions prefix, from the first tool through the marked breakpoint. For [[MCP-server]] toolsets (`mcp_toolset`), place the breakpoint on the toolset entry itself—the API applies it to the final expanded tool (you don't control intra-toolset order).

**`defer_loading` preserves the cache.** Deferred tools are NOT included in the system-prompt prefix. When discovered through [[Tool-search-tool-API]], they're appended inline as `tool_reference` blocks in the conversation body. The prefix stays untouched, so the cache hit persists. This means: start with a small always-loaded toolset (cached), let Claude discover more tools as needed, keep the cache hit across every turn. `defer_loading` also operates independently of strict-mode grammar construction—the grammar builds from the full toolset regardless of which tools are deferred, so prompt caching and grammar caching are both preserved when tools load dynamically.

**Cache invalidation hierarchy.** The cache follows a prefix hierarchy `tools → system → messages`—a change at one level invalidates that level and everything after.

| Change | Invalidates |
|---|---|
| Modifying tool definitions | Entire cache (tools, system, messages) |
| Toggling web search or citations | System and messages caches |
| Changing `tool_choice` | Messages cache |
| Changing `disable_parallel_tool_use` | Messages cache |
| Toggling images present/absent | Messages cache |
| Changing thinking parameters | Messages cache |

If you need to vary `tool_choice` mid-conversation, place cache breakpoints **before** the variation point.

**Per-tool caching considerations:**
- [[Web-search-tool]] / [[Web-fetch-tool]]: enabling/disabling invalidates system + messages caches.
- [[Code-execution-tool]]: container state is independent of prompt cache.
- [[Tool-search-tool-API]]: discovered tools load as `tool_reference` blocks, preserving the prefix cache.
- [[Computer-use-tool-API]]: screenshot presence affects messages cache.
- [[Text-editor-tool]] / [[Bash-tool-API]] / [[Memory-tool]]: standard client tools, no special caching interaction.
