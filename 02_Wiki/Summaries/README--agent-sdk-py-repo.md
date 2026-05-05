---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/README.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md
title: "Claude Agent SDK for Python — README"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Hooks, Permission-mode]
concepts_referenced: [Agentic-loop, Tool-use]
---

The Python SDK for Claude Agent (`pip install claude-agent-sdk`, requires Python 3.10+). The Claude Code CLI is automatically bundled with the package — no separate installation required. Users who prefer a system-wide install can run `curl -fsSL https://claude.ai/install.sh | bash` or specify `ClaudeAgentOptions(cli_path="/path/to/claude")`.

**Two top-level APIs:**

1. **`query()`** — async function for one-shot queries to Claude Code. Returns an `AsyncIterator` of response messages. Supports `ClaudeAgentOptions` (system_prompt, max_turns, allowed_tools, permission_mode, cwd, etc.). Example: `async for message in query(prompt="What is 2 + 2?"): print(message)`.

2. **`ClaudeSDKClient`** — supports bidirectional, interactive conversations. Unlike `query()`, `ClaudeSDKClient` additionally enables **custom tools** and **hooks**, both of which can be defined as Python functions.

**Tools.** By default Claude has access to the full Claude Code toolset (Read, Write, Edit, Bash, etc.). `allowed_tools` is a permission allowlist: listed tools are auto-approved; unlisted tools fall through to `permission_mode` and `can_use_tool` for a decision. It does not remove tools from Claude's toolset. To block tools use `disallowed_tools`.

**Custom Tools (In-Process SDK MCP Servers).** Custom tools are implemented as in-process MCP servers that run directly within the Python application, eliminating subprocesses required by regular MCP servers. Use `@tool` decorator to define a tool and `create_sdk_mcp_server()` to package them. Benefits over external MCP servers: no subprocess management, no IPC overhead, simpler deployment, easier debugging, type safety. SDK and external MCP servers can be mixed in the same `mcp_servers` config.

**Hooks.** A hook is a Python function that the Claude Code application (not Claude) invokes at specific points of the agent loop. Hooks provide deterministic processing and automated feedback. Configured via `HookMatcher(matcher="Bash", hooks=[fn])` against events such as `PreToolUse`. A hook can return `permissionDecision: "deny"` with a reason to block a tool call.

**Types.** `ClaudeAgentOptions`, `AssistantMessage`, `UserMessage`, `SystemMessage`, `ResultMessage`, `TextBlock`, `ToolUseBlock`, `ToolResultBlock`.

**Errors.** `ClaudeSDKError` (base), `CLINotFoundError`, `CLIConnectionError`, `ProcessError`, `CLIJSONDecodeError`.

**Migration from Claude Code SDK (<0.1.0):** breaking changes include `ClaudeCodeOptions` → `ClaudeAgentOptions` rename, merged system prompt configuration, settings isolation and explicit control, new programmatic subagents and session forking features.

**Build/release:** `python scripts/build_wheel.py` builds platform wheels with the bundled CLI. Releases are published to PyPI via the GitHub Actions workflow; the workflow tracks both the package version and the bundled CLI version separately.

Use of the SDK is governed by Anthropic's Commercial Terms of Service.
