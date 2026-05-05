---
type: summary
source: 01_Raw/anthropic.com/news/enabling-claude-code-to-work-more-autonomously.md
source_url: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
title: "Enabling Claude Code to work more autonomously"
summarized_at: 2026-05-05
entities_referenced: [IDE-integration, Checkpointing, Subagent, Hooks, Agent-SDK]
concepts_referenced: []
---

Sep 29, 2025 — Major Claude Code release alongside **Sonnet 4.5**. Sonnet 4.5 becomes new default; users can `/model` to switch.

**New surfaces.**
- **Native VS Code extension (beta)** — dedicated sidebar panel with inline diffs, real-time view of Claude's changes. Richer graphical experience for IDE-preferring users.
- **Refreshed terminal interface** — improved status visibility, searchable prompt history (Ctrl+r) for reuse/edit of previous prompts.
- **Claude Agent SDK** (renamed from Claude Code SDK) — same core tools, context-management, permissions framework as Claude Code. SDK now supports **subagents and hooks** for custom workflows. Used to build financial-compliance agents, cybersecurity agents, code-debugging agents.

**Autonomy features.**
- **Checkpoints** — automatic save of code state before each Claude edit. Esc-Esc or `/rewind` to restore. Choose to restore code, conversation, or both. Applies to Claude's edits only (not user edits or bash). Recommended alongside version control.
- **Subagents** — delegate specialized tasks (one builds backend API while main agent builds frontend); enables parallel workflows.
- **Hooks** — auto-trigger actions at specific points (run tests after code changes, lint before commits).
- **Background tasks** — keep long-running processes (dev servers) active without blocking Claude Code's progress on other work.

Combined, these let users delegate broad tasks like extensive refactors or feature exploration to Claude Code with confidence.
