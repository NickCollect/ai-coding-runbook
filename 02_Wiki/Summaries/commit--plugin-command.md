---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/commit-commands/commands/commit.md
title: "commit (plugin slash command)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command]
concepts_referenced: []
---

Minimal `/commit` slash command shipped in the `commit-commands` plugin.

**Frontmatter**:
- `allowed-tools`: `Bash(git add:*)`, `Bash(git status:*)`, `Bash(git commit:*)`
- `description`: Create a git commit

**Body** uses bash command interpolation (`!\`...\``) to inject git context into the prompt:
- `!git status` — current status
- `!git diff HEAD` — staged + unstaged changes
- `!git branch --show-current`
- `!git log --oneline -10` — recent commits

**Task**: based on the injected context, create a single git commit. **Important constraint**: stage and create the commit using a single message (parallel tool calls). Do not use other tools or send any other text/messages besides the tool calls.
