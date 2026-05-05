---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/ROADMAP.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/ROADMAP.md
title: "claude-code-action — GitHub Action v1.0 Roadmap"
summarized_at: 2026-05-05
entities_referenced: ["Anthropic"]
concepts_referenced: ["roadmap", "GitHub Action", "Claude Code", "CI integration", "PR automation", "cross-repo", "workflow_dispatch"]
---

Beta roadmap for Claude Code GitHub Action toward v1.0.

Completed: CI results visibility (Claude can fix CI failures), bot user @claude trigger support.

Planned:
- Cross-repo support: work across multiple repositories in one session
- Modify workflow files: update GitHub Actions configs
- workflow_dispatch and repository_dispatch event support
- Disable commit signing option (normal git commands, likely to become default)
- Better code review: inline line comments, higher quality feedback
- Customizable base prompts: template variables ($PR_COMMENTS, $PR_FILES, etc.)
