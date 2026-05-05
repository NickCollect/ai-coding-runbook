---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/typescript.md
source_url: https://code.claude.com/docs/en/agent-sdk/typescript
title: "Agent SDK reference - TypeScript"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Hooks, Subagent, Permission-mode, Skill]
concepts_referenced: [Agentic-loop, Tool-use]
---

Complete TypeScript API reference for `@anthropic-ai/claude-agent-sdk`. SDK bundles a native Claude Code binary as optional dep per platform (e.g., `@anthropic-ai/claude-agent-sdk-darwin-arm64`); if package manager skips optional deps, set `pathToClaudeCodeExecutable` to a separately installed `claude` binary. A simplified V2 interface with `send()` / `stream()` patterns is available in preview.

**Core functions**:
- `query({prompt, options})` → `Query` object extending `AsyncGenerator<SDKMessage, void>` with extra methods. `prompt` accepts string or `AsyncIterable<SDKUserMessage>` for streaming mode.
- `startup({options, initializeTimeoutMs})` → `WarmQuery` — pre-warms the CLI subprocess so first `.query()` call resolves without spawn cost. Default timeout 60000ms.
- `tool(name, description, zodSchema, handler, {annotations?})` — type-safe MCP tool definition (Zod 3 and 4 supported).
- `createSdkMcpServer({name, version?, tools?})` — in-process MCP server.

**Session management functions**:
- `listSessions({dir?, limit?, includeWorktrees?})` returns `SDKSessionInfo[]` with `sessionId`, `summary`, `lastModified`, `fileSize`, `customTitle`, `firstPrompt`, `gitBranch`, `cwd`, `tag`, `createdAt`. Sorted by `lastModified` desc. Includes worktrees by default.
- `getSessionMessages(sessionId, {dir?, limit?, offset?})` returns `SessionMessage[]` (`type: "user"|"assistant"`, `uuid`, `session_id`, `message`, `parent_tool_use_id`).
- `getSessionInfo(sessionId, {dir?})` — single session metadata, no full directory scan.
- `renameSession(sessionId, title)` — appends custom-title entry; latest wins.
- (Inferred from cross-references) `tagSession()`.

**Tool annotations** (re-exported from `@modelcontextprotocol/sdk/types.js`, all optional hints, not enforcement): `title`, `readOnlyHint` (default false; controls parallel batching), `destructiveHint` (default true), `idempotentHint` (default false), `openWorldHint` (default true).

**Tool result block types** (`CallToolResult.content`): `text`, `image` (base64 `data` + required `mimeType`), `resource` (URI label + inline `text` or `blob`).

**Options surface** (large): `allowedTools`, `disallowedTools`, `tools`, `permissionMode` (`acceptEdits|dontAsk|auto|bypassPermissions|default`), `mcpServers`, `agents` (programmatic subagent definitions), `hooks` (PreToolUse/PostToolUse/Stop/SessionStart/SessionEnd/UserPromptSubmit etc. with HookMatcher), `systemPrompt`, `setting_sources`/`settingSources` (`user`/`project`/`local`), `maxTurns`, `resume` (session ID), `pathToClaudeCodeExecutable`, custom `canUseTool` callback.

This file is the comprehensive API surface reference — for individual feature usage see the `custom-tools`, `mcp`, `subagents`, `slash-commands`, `hooks`, `permissions`, `sessions` guides. **Note**: raw is large (~38k tokens); only the first portion was sampled here. Refer to raw for full type signatures of every helper.
