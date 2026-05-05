---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/commit-commands/commands/clean_gone.md
title: "commit-commands: /clean_gone command"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command]
concepts_referenced: []
---

Slash command from `commit-commands` plugin: cleans up local git branches marked `[gone]` (deleted on remote but still local), including their associated worktrees.

**Three commands** Claude executes:
1. `git branch -v` — identify `[gone]` branches (`+` prefix means has worktree).
2. `git worktree list` — find worktrees needing removal.
3. Loop: for each `[gone]` branch (after stripping `[+* ]` prefix), find associated worktree via `git worktree list | grep "\[$branch\]"`, `git worktree remove --force` it (skip if it's the current toplevel), then `git branch -D` the branch.

Reports each step. If no `[gone]` branches, reports nothing to clean.
