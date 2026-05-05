---
type: summary
source: 01_Raw/code.claude.com/docs/en/commands.md
source_url: https://code.claude.com/docs/en/commands
title: "Commands (Claude Code reference)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Skill, Subagent, MCP-server, Hooks, Plugin, Plugin-marketplace, Memory, Settings, Permission-mode, Sandboxing, Auto-mode, Fast-mode, Status-line, Output-style, Routine, Native-interface, IDE-integration, Checkpointing]
concepts_referenced: []
---

Complete reference for built-in commands available inside a Claude Code session. Type `/` to list all commands; commands are only recognized at start of message. Some are **built-ins** (coded into the CLI), others are **bundled skills** (using the same skill mechanism — Claude can invoke them automatically). Availability varies by platform/plan/env.

Notable command categories:

**Session/conversation**: `/clear` (`/reset`, `/new`), `/compact [instr]`, `/context`, `/copy [N]`, `/export`, `/resume` (`/continue`), `/branch [name]` (`/fork`), `/rewind` (`/checkpoint`, `/undo`), `/recap`, `/rename`.

**Configuration**: `/config` (`/settings`), `/model [model]`, `/effort [low|medium|high|xhigh|max|auto]`, `/theme`, `/color`, `/permissions` (`/allowed-tools`), `/sandbox`, `/fast [on|off]`, `/keybindings`, `/statusline`, `/tui [default|fullscreen]`, `/voice`.

**Account**: `/login`, `/logout`, `/usage` (`/cost`, `/stats`), `/upgrade`, `/extra-usage`, `/privacy-settings`, `/passes`.

**Skills/plugins/agents**: `/skills`, `/plugin`, `/reload-plugins`, `/agents`, `/hooks`, `/mcp`.

**GitHub & cloud**: `/install-github-app`, `/web-setup`, `/remote-env`, `/remote-control` (`/rc`), `/teleport` (`/tp`), `/autofix-pr [prompt]`, `/tasks` (`/bashes`), `/desktop` (`/app`).

**Bundled skills**: `/batch <instruction>` (split codebase work into 5–30 worktree subagents → PRs), `/claude-api [migrate|managed-agents-onboard]`, `/debug [desc]`, `/fewer-permission-prompts`, `/loop [interval] [prompt]` (`/proactive`), `/simplify [focus]`.

**Workflow/review**: `/plan [desc]`, `/diff`, `/review [PR]`, `/security-review`, `/ultrareview [PR]`, `/ultraplan <prompt>`.

**Memory/init**: `/init` (`CLAUDE_CODE_NEW_INIT=1` for interactive flow), `/memory` (edit CLAUDE.md, manage auto-memory), `/add-dir <path>`.

**Diagnostics**: `/doctor`, `/status`, `/heapdump`, `/debug`, `/insights`, `/release-notes`, `/feedback` (`/bug`).

**Provider setup**: `/setup-bedrock` (visible only with `CLAUDE_CODE_USE_BEDROCK=1`), `/setup-vertex` (`CLAUDE_CODE_USE_VERTEX=1`).

**Misc**: `/btw <q>` (side question), `/focus`, `/install-slack-app`, `/mobile`, `/powerup`, `/stickers`, `/team-onboarding`, `/terminal-setup`, `/exit` (`/quit`), `/chrome`, `/ide`.

**Removed**: `/pr-comments` (v2.1.91), `/vim` (v2.1.92 — use `/config` → Editor mode).

**MCP prompts** appear as `/mcp__<server>__<prompt>`, dynamically discovered.

To add custom commands → write a Skill.
