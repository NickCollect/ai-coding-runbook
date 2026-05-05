---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-teams.md
source_url: https://code.claude.com/docs/en/agent-teams
title: "Orchestrate teams of Claude Code sessions"
summarized_at: 2026-05-05
entities_referenced: [Agent-team, Subagent, Hooks, Permission-mode, Settings, Memory, Skill, MCP-server]
concepts_referenced: [Context-window]
---

**Experimental feature** (Claude Code v2.1.32+, enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Coordinates multiple Claude Code instances as a team: one **lead** + multiple **teammates**, each in its own context window, with a **shared task list** and a **mailbox** for direct inter-agent messaging.

**vs Subagents**: subagents only report results back to the main agent; teammates can talk to each other, share a task list, claim work, and the user can message any teammate directly.

| | Subagents | Agent teams |
|--|--|--|
| Communication | Report to main only | Direct teammate-to-teammate |
| Coordination | Main agent | Shared task list + self-coord |
| Token cost | Lower (summarized back) | Higher (each is full instance) |

**Best for**: research/review with multiple lenses, parallel module dev, debugging competing hypotheses, cross-layer (frontend+backend+tests) coordination. Bad for sequential work, same-file edits, dependency-heavy tasks.

**Display modes**: in-process (Shift+Down to cycle teammates, Ctrl+T toggles task list) or split-pane (requires tmux or iTerm2 + `it2` CLI). Set `teammateMode` in settings; `auto` picks split if already in tmux. CLI flag: `--teammate-mode in-process`.

**Plan approval**: tell lead to require teammates to plan first; teammate stays in plan mode until lead approves/rejects.

**Architecture**:
- Team config: `~/.claude/teams/{team-name}/config.json` (auto-managed; don't edit by hand)
- Task list: `~/.claude/tasks/{team-name}/` (file locking prevents race on claim)
- No project-level config equivalent

**Subagent definitions as teammates**: spawn a teammate using a named subagent type (project/user/plugin/CLI scope). Inherits `tools` allowlist + `model`; body appended to system prompt. `skills` and `mcpServers` frontmatter NOT applied — teammates load skills/MCP from project+user settings same as a regular session. `SendMessage` and task tools always available.

**Permissions**: teammates start with lead's permission mode; can change individually post-spawn but not at spawn time.

**Quality gates** via hooks: `TeammateIdle`, `TaskCreated`, `TaskCompleted` — exit code 2 sends feedback back.

**Best practices**: 3–5 teammates; 5–6 tasks per teammate; size tasks as self-contained units; pre-approve permissions; tell lead to wait for teammates; start with research/review; avoid file conflicts.

**Limitations**: no in-process teammate restoration with `/resume`/`/rewind`; task status can lag; one team per session; no nested teams; lead is fixed; split panes don't work in VS Code/Windows Terminal/Ghostty integrated terminals.
