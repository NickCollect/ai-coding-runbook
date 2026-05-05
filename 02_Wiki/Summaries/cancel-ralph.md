---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/ralph-wiggum/commands/cancel-ralph.md
title: "/cancel-ralph command (ralph-wiggum plugin)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin]
concepts_referenced: []
---

Brief slash command in the `ralph-wiggum` plugin (a Ralph Wiggum-style infinite-loop helper). Cancels an active Ralph loop by removing its state file.

Frontmatter: `hide-from-slash-command-tool: "true"` (hidden from picker; only invokable via `/cancel-ralph`). Pre-allowed tools narrowly scoped to `Bash(test -f .claude/ralph-loop.local.md:*)`, `Bash(rm .claude/ralph-loop.local.md)`, `Read(.claude/ralph-loop.local.md)`.

Process: check if state file exists → if not, report "No active Ralph loop found" → if yes, read iteration number from `iteration:` field, remove file, report "Cancelled Ralph loop (was at iteration N)".
