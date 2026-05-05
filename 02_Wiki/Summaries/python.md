---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/python.md
source_url: https://code.claude.com/docs/en/agent-sdk/python
title: "Agent SDK reference - Python"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Hooks, Permission-mode]
concepts_referenced: []
---

Complete Python API reference for the `claude-agent-sdk` package. Install: `pip install claude-agent-sdk`.

Two entry-points:
- **`query()`** — async iterator returning `Message` objects, creates a fresh session per call. Best for one-off questions, automation scripts. Supports streaming input, hooks, custom tools. Does NOT support interrupts or conversation continuation.
- **`ClaudeSDKClient`** — manages a long-lived session reused across exchanges. Best for chat interfaces, REPLs, and response-driven multi-turn flows. Supports interrupts and conversation continuation.

Key API building blocks:
- **`@tool(name, description, input_schema, annotations=None)`** — decorator that turns an async function into an MCP tool. `input_schema` accepts either a simple type-mapping (`{"text": str}`) or a full JSON Schema dict.
- **`ToolAnnotations`** — re-exported from `mcp.types`. Optional behavioral hints (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`, `title`). Hints only — never use for security decisions.
- **`create_sdk_mcp_server(name, version, tools)`** — creates an in-process MCP server hosted in your Python process (no subprocess).
- **`ClaudeAgentOptions`** — configuration dataclass with fields like `system_prompt`, `permission_mode`, `cwd`, `setting_sources`, `allowed_tools`, `env`, `output_format`, `mcp_servers`, hook callbacks, etc.
- Message types: `AssistantMessage`, `UserMessage`, `SystemMessage`, `ResultMessage` — each with `usage` / `message_id` / `total_cost_usd` / `structured_output` fields where applicable.
- Custom transport via the `transport` parameter for testing or alternate IPC.

The SDK runs the bundled native Claude Code binary as a child process; configuration is mostly passed via env vars. Permission control via `permission_mode` and the `canUseTool` callback. Used together with filesystem-loaded Skills, Subagents, Slash commands, and MCP servers.
