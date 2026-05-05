---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/commit-commands/commands/commit-push-pr.md
title: "/commit-push-pr command (commit-commands plugin)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin]
concepts_referenced: []
---

Slash command in the official `commit-commands` plugin. Commits, pushes, and opens a PR in a single message.

Pre-approved tools: `Bash(git checkout --branch:*)`, `Bash(git add:*)`, `Bash(git status:*)`, `Bash(git push:*)`, `Bash(git commit:*)`, `Bash(gh pr create:*)`.

Auto-injected context (via `` !`...` `` shell injection): current `git status`, full `git diff HEAD`, current branch.

**Task** (must run as a single tool-batch message — no extra text):
1. Create new branch if currently on main.
2. Single commit with appropriate message.
3. Push branch to origin.
4. Create PR via `gh pr create`.

The command file emphasizes that all four steps execute in one parallel tool-call message — no narration, no other tools.
