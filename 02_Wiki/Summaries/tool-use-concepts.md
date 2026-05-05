---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/tool-use-concepts.md
title: "Tool Use Concepts (shared)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: [Tool-use]
---

Conceptual foundations of Claude API tool use, language-agnostic.

**Tool definition structure**: each tool needs `name`, `description`, `input_schema` (JSON Schema). When using SDK Tool Runner (beta), schemas auto-generated from Python function signatures, TS Zod, Java/Go struct annotations, Ruby `BaseTool` subclasses. Manual JSON-schema approach (or PHP `BetaRunnableTool` wrapping a closure) for SDKs without Tool Runner.

**Best practices**: descriptive names (`get_weather`, `search_database`), detailed descriptions (Claude uses these to choose tools), per-property descriptions, `enum` for fixed value sets, mark only truly required params in `required`.

**Tool choice options**:
- `{"type": "auto"}` — Claude decides (default).
- `{"type": "any"}` — must use at least one.
- `{"type": "tool", "name": "..."}` — must use the specified tool.
- `{"type": "none"}` — cannot use tools.

Add `"disable_parallel_tool_use": true` to force at-most-one-tool-per-response (default allows parallel).

**Tool Runner vs Manual Loop**:
- **Tool Runner (recommended)**: SDK handles agentic loop — calls API, detects tool requests, executes your functions, feeds results back, repeats. Available in Python/TS/Java/Go/Ruby/PHP SDKs (beta). Python also has `anthropic.lib.tools.mcp` for MCP→Tool Runner conversion.
- **Manual loop**: for fine-grained control (custom logging, conditional execution, human-in-loop approval). Loop until `stop_reason == "end_turn"`. Always append full `response.content` to preserve `tool_use` blocks. Each `tool_result` must include matching `tool_use_id`.

**Server-side tools (code execution / web search / etc.)** run in a server-side sampling loop. Default limit 10 iterations. On limit hit: `stop_reason: "pause_turn"`. To resume: re-send the user message + assistant response in a new API request — server picks up automatically (DON'T add an extra "Continue." user message; the API detects trailing `server_tool_use` block).
