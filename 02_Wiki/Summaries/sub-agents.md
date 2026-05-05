---
type: summary
source: 01_Raw/code.claude.com/docs/en/sub-agents.md
source_url: https://code.claude.com/docs/en/sub-agents
title: "Create custom subagents"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Agent-team, MCP-server, Skill, Hooks, Permission-mode, Settings, Plugin, Slash-command, Memory]
concepts_referenced: [Context-window, Agentic-loop]
---

Subagents = specialized AI assistants in own context window with custom system prompt, tool restrictions, independent permissions. Returns only summary to main conversation. Use when side task would flood main context.

vs **Agent teams**: subagents work within a single session and only report to main; agent teams coordinate across sessions with direct messaging.

Benefits: preserve context, enforce constraints (tool restrictions), reuse configs (user-level), specialize behavior, control costs (route to Haiku).

**Built-in**:
- **Explore**: Haiku, read-only tools, codebase search. Thoroughness: quick / medium / very thorough.
- **Plan**: inherits model, read-only, used during plan mode (prevents nesting).
- **General-purpose**: inherits model, all tools, complex multi-step tasks.
- Helper: `statusline-setup` (Sonnet), `Claude Code Guide` (Haiku, for CC questions).

**Creation**: `/agents` command (Library tab → Create new) or manual markdown files with YAML frontmatter.

**Scopes** (priority order):
1. Managed settings (org-wide)
2. `--agents` CLI flag (JSON, session-only)
3. `.claude/agents/` (project)
4. `~/.claude/agents/` (user)
5. Plugin's `agents/` (plugin scope)

**Plugin subagents**: `hooks`, `mcpServers`, `permissionMode` fields IGNORED (security).

**Frontmatter fields**: `name` (required, lowercase-hyphen), `description` (required, when to delegate), `tools` (allowlist), `disallowedTools` (denylist; applied first), `model` (sonnet/opus/haiku/full ID/`inherit`; default `inherit`), `permissionMode`, `maxTurns`, `skills` (preload list — full content injected, not just available; can't preload disable-model-invocation skills), `mcpServers` (inline or by-name), `hooks`, `memory` (user/project/local — gives `~/.claude/agent-memory/<name>/` etc., enables Read/Write/Edit, MEMORY.md first 200 lines / 25KB included), `background` (always background), `effort`, `isolation` (`worktree` for git worktree), `color`, `initialPrompt` (auto-submitted as first user turn when run as main session).

**Model resolution**: `CLAUDE_CODE_SUBAGENT_MODEL` env > per-invocation `model` > frontmatter `model` > main conversation.

**Restrict spawning** (when running as main with `--agent`): `tools: Agent(worker, researcher), Read, Bash` allowlists subagents. `Agent` without parens = any. Omit = none. Subagents cannot spawn others. (Task tool renamed to Agent in v2.1.63; old refs still work.)

**Permission modes**: `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`. Parent `bypassPermissions`/`acceptEdits` takes precedence; parent auto mode → subagent inherits + frontmatter `permissionMode` ignored.

**Hooks in frontmatter**: scoped to subagent lifecycle, cleaned up on finish. `Stop` events auto-converted to `SubagentStop`. Project-level hooks in `settings.json` for `SubagentStart`/`SubagentStop` events fire in main session.

**Disable specific subagents**: `permissions.deny: ["Agent(Explore)"]`.

**Invocation**: natural language (Claude decides), `@"agent-name (agent)"` (forces specific subagent), session-wide via `claude --agent <name>` or `agent` setting (replaces system prompt entirely; CLI flag wins).

**Foreground vs background**: foreground blocks main, permission prompts pass through. Background runs concurrently — Claude pre-approves needed permissions before launch, auto-denies anything else. `Ctrl+B` to background. `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` to disable.

**Resume**: subagents persist transcripts at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`. Cleanup `cleanupPeriodDays` default 30. Resume via `SendMessage` (only when agent teams enabled).

**Auto-compaction**: subagents support same logic as main, default ~95%. Tune via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`.

**Forked subagents** (experimental, v2.1.117+, `CLAUDE_CODE_FORK_SUBAGENT=1`): fork inherits ENTIRE conversation (system prompt, tools, model, history). Replaces general-purpose subagent. Every spawn runs background. `/fork` spawns fork instead of `/branch`. Shared prompt cache with parent → cheaper than fresh subagent. Forks can't spawn further forks. Panel below prompt to observe (↑↓ navigate, Enter open transcript, x dismiss/stop, Esc back).

**Use main vs subagent vs Skill vs `/btw`**: main = back-and-forth + iterative; subagent = self-contained verbose work; Skill = reusable in main context; `/btw` = side question, full context, no tools.
