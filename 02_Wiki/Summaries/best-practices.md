---
type: summary
source: 01_Raw/code.claude.com/docs/en/best-practices.md
source_url: https://code.claude.com/docs/en/best-practices
title: "Best practices for Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Memory, Skill, Subagent, Hooks, MCP-server, Plugin, Permission-mode, Sandboxing, Auto-mode, Headless-mode, Checkpointing]
concepts_referenced: [Context-window, Agentic-loop, Agent-team]
---

Claude Code is an agentic environment, not a chatbot — you describe what you want, Claude explores, plans, implements. The core constraint is the context window: it fills fast and performance degrades as it does. Most best practices flow from managing context.

Top techniques:
- **Verification is the highest-leverage thing**: include tests, screenshots, expected outputs. Use the Claude in Chrome extension for UI verification. Address root causes, not symptoms.
- **Explore → Plan → Implement → Commit**: use plan mode (`Ctrl+G` opens plan in editor) for non-trivial work. Skip planning if you could describe the diff in one sentence.
- **Specific prompts**: scope the task, point to existing patterns, describe symptoms with likely location. Reference files with `@`, paste images, pipe data via `cat err.log | claude`.

Configure environment:
- **CLAUDE.md** (`/init` to scaffold): bash commands, code style, workflow rules. Keep short — for each line ask "would removing this cause mistakes?". Locations: `~/.claude/CLAUDE.md` (all sessions), `./CLAUDE.md` (project, in git), `./CLAUDE.local.md` (gitignored), parent dirs (monorepos), child dirs (on-demand). Imports via `@path`.
- **Permissions**: auto mode (classifier blocks risky actions), `/permissions` allowlist, `/sandbox` for OS isolation.
- **CLI tools**: install `gh`, `aws`, `gcloud`, `sentry-cli` — most context-efficient external interface.
- **MCP servers**: `claude mcp add` for Notion/Figma/DB integrations.
- **Hooks**: deterministic (vs CLAUDE.md which is advisory). Claude can write hooks for you ("write a hook that runs eslint after every file edit"). Edit `.claude/settings.json` or use `/hooks`.
- **Skills**: `.claude/skills/<name>/SKILL.md`. Auto-applied based on `description`, or invoked via `/skill-name`. Use `disable-model-invocation: true` for side-effecting workflows.
- **Subagents**: `.claude/agents/<name>.md` — separate context, own tools/model. Tell Claude explicitly: "use a subagent to review for security issues."
- **Plugins**: `/plugin` to browse marketplace.

Communication:
- Ask codebase questions like a senior engineer.
- For larger features, have Claude **interview you** with `AskUserQuestion`, then write SPEC.md, then start a fresh session to execute.

Session management:
- `Esc` stops mid-action. `Esc + Esc` or `/rewind` opens checkpoint menu (restore conversation/code/both, or summarize from a message).
- `/clear` between unrelated tasks. After two failed corrections, `/clear` and rewrite prompt.
- `/compact <instructions>` for targeted compaction. `/btw` for side questions that don't enter context.
- `claude --continue` / `claude --resume`. Name with `/rename`. Sessions are persistent + branchable.
- Subagents are powerful for keeping investigation out of main context.
- Checkpoints are not git replacement — only track Claude's changes.

Scale and automation:
- **Headless**: `claude -p "prompt" --output-format json|stream-json` for CI / pre-commit / scripts.
- **Parallel sessions**: worktrees, desktop app, web (cloud VMs), agent teams. Writer/Reviewer pattern.
- **Fan-out**: loop `claude -p` over file lists with `--allowedTools` to scope.
- **Auto mode**: `claude --permission-mode auto -p "..."` aborts in headless if classifier repeatedly blocks.

Common failure patterns: kitchen-sink session, repeated correction loops, over-specified CLAUDE.md, trust-then-verify gap, infinite exploration. Cure most by `/clear` + better prompt.
