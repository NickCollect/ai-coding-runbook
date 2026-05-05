---
type: summary
source: 01_Raw/code.claude.com/docs/en/how-claude-code-works.md
source_url: https://code.claude.com/docs/en/how-claude-code-works
title: "How Claude Code works"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server, Hooks, Subagent, Memory, Checkpointing, Permission-mode, Auto-mode, Native-interface, IDE-integration, Settings, Plugin]
concepts_referenced: [Agentic-loop, Context-window]
---

Conceptual overview of Claude Code's architecture. Three-phase **agentic loop**: gather context → take action → verify results. Phases blend; tools used throughout; loop adapts to task type (question = mostly context-gather; bug fix = full cycle repeated; refactor = heavy verification). Claude decides what each step requires from previous results, chains dozens of actions, course-corrects. User can interrupt at any point.

Claude Code = the **agentic harness** around the model: provides tools, context management, execution environment.

**Models**: Sonnet (default for most coding), Opus (complex architecture). Switch via `/model` or `claude --model <name>`.

**Built-in tool categories**: file ops (Read/Edit/Write), search (Glob/Grep), execution (Bash), web (WebSearch/WebFetch), code intelligence (type errors, jump-to-def, find-references — requires code intelligence plugins).

**What Claude can access** when you run `claude`: project files in cwd + subdirs, terminal (any command you can run), git state, `CLAUDE.md`, **auto memory** (first 200 lines or 25KB of `MEMORY.md` at session start), configured extensions (MCP, skills, subagents, Chrome).

**Execution environments**:
| Environment | Where | Use |
|---|---|---|
| Local | Your machine | Default |
| Cloud | Anthropic VMs | Offload, work on remote repos |
| Remote Control | Your machine + browser UI | Web UI, local execution |

Available interfaces: terminal, Desktop, IDE extensions (VS Code, JetBrains), claude.ai/code, Remote Control, Slack, CI/CD.

**Sessions**: saved as plaintext JSONL under `~/.claude/projects/`. Independent — fresh context per session, no inherited history. Auto memory + CLAUDE.md persist learnings/rules. Sessions tied to cwd; switching branches keeps conversation but Claude sees new branch's files. Parallel sessions via git worktrees.

**Resume vs fork**: `claude --continue` / `--resume` reopens same session ID and appends; `--fork-session` / `/branch` copies history to new ID, leaves original alone.

**Context window** holds: history + file contents + command outputs + CLAUDE.md + auto memory + skills + system instructions. Auto-compacts: clears older tool outputs first, then summarizes. Persistent rules belong in CLAUDE.md, not conversation. Customize compaction via "Compact Instructions" section in CLAUDE.md or `/compact focus on X`. Thrashing detection: if a single huge file/output causes context to refill immediately after summary, Claude Code aborts auto-compacting after a few attempts.

MCP tool **definitions are deferred** (loaded on demand via tool search) — only tool names take context until the tool is used. `/mcp` shows per-server cost.

**Skills load on demand**: descriptions visible at session start, full content only when used. `disable-model-invocation: true` suppresses descriptions until manual invocation.

**Subagents** get their own fresh context — work doesn't bloat parent; only summary returns.

**Safety mechanisms**:
- **Checkpoints** — every file edit is reversible. Snapshot before each edit. Esc-Esc to rewind. Local to session, separate from git, file-only (external side effects can't be checkpointed — that's why Claude asks before commands with external impact).
- **Permission modes** — Shift+Tab cycles: Default → Auto-accept edits → Plan mode → Auto mode (research preview). Per-command allowlist via `.claude/settings.json`. Settings scope from org-wide policy down to personal.

**Effective use** principles: it's a conversation (iterate, don't restart); interrupt + steer (just type and Enter); be specific upfront; give Claude something to verify against (test cases, screenshots, expected outputs); plan-mode-then-implement for complex problems; delegate (give context + direction, trust details).

Built-in commands: `/init` (create CLAUDE.md), `/agents` (configure subagents), `/doctor` (diagnose).
