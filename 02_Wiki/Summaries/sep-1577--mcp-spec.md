---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1577--sampling-with-tools.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1577--sampling-with-tools.md
title: "SEP-1577: Sampling with Tools"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Tool-use]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-09-30 | Author: Olivier Chafik (@ochafik) | Sponsor: @bhosmer-ant**

Introduces `tools` and `toolChoice` parameters to `sampling/createMessage` and soft-deprecates `includeContext` (now fenced behind explicit capabilities). Allows MCP servers to run their own agentic loops using the client's tokens (still under user supervision).

**Why**: sampling didn't support tool calling — a cornerstone of modern agentic behavior. Servers using sampling had to either emulate tool calling via complex prompting/parsing or remain limited to simple non-agentic requests. The change unlocks novel use cases (e.g., a research server spawning multiple sub-agents internally and coordinating them).

**Key protocol changes**:
- `ClientCapabilities.sampling.tools` (new) — fences `tools` and `toolChoice` use
- `ClientCapabilities.sampling.context` (new) — fences `includeContext != "none"` (which becomes optional/deprecated)
- `CreateMessageRequest.params` adds `tools?: Tool[]` and `toolChoice?: { mode?: "auto" | "required" | "none" }`
- New `ToolUseContent` and `ToolResultContent` block types in messages (aligned with `CallToolResult.content` block format)
- `SamplingMessage` becomes a discriminated union of `UserMessage` / `AssistantMessage`; assistant messages carry tool_use blocks, user messages carry tool_result blocks
- `CreateMessageResult.content` may now be a single block OR an array (with backward-compat clause: spec versions before Nov 2025 MUST NOT return arrays)
- `stopReason` widens to `"endTurn" | "stopSequence" | "toolUse" | "maxToken" | string` (open string + explicit enums for visibility)

**Server-side tool loop** required: server includes tools in sampling request → sampling yields ToolUseContent → server calls tools itself → server calls sampling again with ToolResultContent → repeat.

**Cross-vendor design notes** documented for OpenAI vs. Anthropic vs. Gemini APIs (parallel tool calls, tool_choice semantics, role naming, function-calling modes). `disable_parallel_tool_use` removed from this SEP because Gemini API can't currently implement it.

**Possible follow-ups** explicitly preserved compatibility with: streaming sampling, prompt caching, server-tool / cross-server tool support, peer-to-peer client/server symmetry, structured outputs (JSON Schema response format).

Adopted in the November 2025 spec release ("Sampling with Tools").
