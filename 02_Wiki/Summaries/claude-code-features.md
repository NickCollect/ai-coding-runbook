---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/claude-code-features.md
source_url: https://code.claude.com/docs/en/agent-sdk/claude-code-features
title: "Use Claude Code features in the SDK"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Hooks, Skill, Subagent, MCP-server, Memory, Settings, Agent-team]
concepts_referenced: [Context-window]
---

The Agent SDK shares Claude Code's filesystem-based feature surface: project instructions (`CLAUDE.md`, `.claude/rules/*.md`), skills, hooks, slash commands, agents, and `settings.json`. Loading is gated by the `settingSources` (TS) / `setting_sources` (Py) option:

- `"project"` — `<cwd>/.claude/` walked up to filesystem root, includes project CLAUDE.md, rules, skills, hooks, settings.
- `"user"` — `~/.claude/` (user CLAUDE.md, rules, skills, settings).
- `"local"` — `<cwd>/CLAUDE.local.md` and `.claude/settings.local.json` (gitignored).

Omitting the option is equivalent to `["user","project","local"]`. Pass `[]` to limit the agent to programmatic config only — useful for multi-tenant isolation. Three inputs leak past `settingSources` regardless: managed policy settings, `~/.claude.json`, and auto memory at `~/.claude/projects/<project>/memory/`. For multi-tenant safety also set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` and isolate the filesystem.

CLAUDE.md files at multiple levels are additive (project, parent dirs, user, local). No hard precedence; conflicts resolve by Claude's interpretation — write non-conflicting rules or state precedence explicitly.

**Skills** load on demand from `.claude/skills/`. The `Skill` tool is enabled by default unless an `allowedTools` allowlist excludes it. Skills must be filesystem artifacts; no programmatic registration API.

**Hooks** come in two coexisting flavors:
- *Filesystem hooks* in `settings.json` — supports `command`, `http`, `mcp_tool`, `prompt`, `agent` types. Fire in main agent and any subagents.
- *Programmatic hooks* — callbacks passed to `query()`. Return `{}` to allow, `{"decision": "block", "reason": "..."}` to block. Scoped to main session only.

TS adds events Python lacks: `SessionStart`, `SessionEnd`, `TeammateIdle`, `TaskCompleted`.

The doc closes with a feature-selection table mapping goals to surface: project conventions → CLAUDE.md; reference material → Skills; isolated subtasks → Subagents; multi-instance coordination → Agent teams (CLI feature); deterministic tool gating → Hooks; external service tools → MCP. Every enabled feature consumes context window — see Extend Claude Code for per-feature costs.
