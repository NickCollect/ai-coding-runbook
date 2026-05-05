---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/commit-commands/README.md
title: "Commit Commands Plugin"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command]
concepts_referenced: []
---

Plugin (Anthropic, v1.0.0) shipping three git workflow slash commands:

**`/commit`** — auto-generated commit:
1. Analyzes git status
2. Reviews staged + unstaged changes
3. Examines recent commit messages to match repo style
4. Drafts message
5. Stages relevant files
6. Creates commit

Avoids committing files with secrets (`.env`, `credentials.json`). Includes Claude Code attribution in commit message.

**`/commit-push-pr`** — full workflow:
1. Creates feature branch (if currently on main)
2. Commits with generated message
3. Pushes to origin
4. `gh pr create` with summary (1-3 bullets) + test plan checklist + Claude Code attribution
5. Returns PR URL

Analyzes ALL commits in branch (not just latest). Requires GitHub CLI (`gh`) installed + authenticated, repo must have `origin` remote.

**`/clean_gone`** — local branch cleanup:
1. Lists branches with `[gone]` status
2. Removes worktrees associated with `[gone]` branches
3. Deletes the stale local branches
4. Reports what was cleaned

Safe — only removes branches already deleted remotely. Run `git fetch --prune` first if no `[gone]` shows up.

**Troubleshooting**: empty commit (no changes); `gh pr create` fails (install gh, `gh auth login`, ensure GitHub remote); `clean_gone` finds nothing (`git fetch --prune`).

Author: Anthropic.
