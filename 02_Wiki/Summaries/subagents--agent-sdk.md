---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/subagents.md
source_url: https://code.claude.com/docs/en/agent-sdk/subagents
title: "Subagents in the SDK"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Agent-SDK, Skill, Memory, MCP-server, Permission-mode]
concepts_referenced: [Context-window, Agent-team, Agentic-loop]
---

How to define and invoke subagents in the Agent SDK via the `agents` parameter. Three creation methods: programmatic (`agents={...}` in options, recommended), filesystem-based (`.claude/agents/*.md`), or built-in `general-purpose` (always available when `Agent` is in `allowedTools`).

**Why subagents**:
- **Context isolation** — fresh conversation per subagent; only final message returns to parent (avoids polluting main context with tool calls/file contents)
- **Parallelization** — multiple subagents concurrently (e.g., style-checker + security-scanner + test-coverage simultaneously)
- **Specialized prompts** — domain expertise without bloating main agent
- **Tool restrictions** — limit risk

**`AgentDefinition` fields**:
- `description` (required) — natural-language trigger; Claude uses this to decide when to invoke
- `prompt` (required) — system prompt for the subagent
- `tools` — restrict tool list; omit to inherit all
- `disallowedTools`
- `model` — `'sonnet'`, `'opus'`, `'haiku'`, `'inherit'`, or full model ID
- `skills`, `memory` (`'user'|'project'|'local'`), `mcpServers`
- `maxTurns`, `background` (non-blocking when invoked), `effort` (`low|medium|high|xhigh|max|number`), `permissionMode`

**Critical**: Subagents cannot spawn their own subagents — don't include `Agent` in subagent's `tools`. **`Agent` MUST be in main `allowedTools`** for delegation to work.

**Inheritance**:
- Receives: own system prompt + Agent tool's prompt string, project CLAUDE.md (via settingSources), tool definitions
- Does NOT receive: parent's conversation history/tool results, parent's system prompt, skills (unless listed in `AgentDefinition.skills`)
- Only channel parent → subagent is the Agent tool's prompt string — include file paths, errors, decisions explicitly
- Parent receives subagent's final message verbatim as Agent tool result, but may summarize unless told otherwise

**Invocation**: automatic via `description` matching, or explicit by name in prompt ("Use the code-reviewer agent to..."). Programmatic agents take precedence over filesystem-based with same name.

**Detection**: Look for `tool_use` block with `name === "Agent"` (renamed from `"Task"` in Claude Code v2.1.63 — current SDK still emits "Task" in `system:init` tools list and `result.permission_denials[].tool_name`, so check both). Subagent-context messages carry `parent_tool_use_id`.

**Resume**: capture `session_id` and parse `agentId` from Agent tool result text, then second `query()` with `resume: sessionId` and prompt referencing the agent ID. Same agent definition must be passed for custom agents. Subagent transcripts persist independently of main conversation; not affected by main compaction; cleaned per `cleanupPeriodDays` (default 30).

**Gotcha (Windows)**: command-line length limit 8191 chars — keep prompts concise or use filesystem-based agents.

**Common tool combos**: read-only (Read/Grep/Glob), test execution (Bash/Read/Grep), code modification (Read/Edit/Write/Grep/Glob), full access (omit `tools`).
