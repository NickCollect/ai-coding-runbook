---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/commit-commands/.claude-plugin/plugin.json
title: "commit-commands plugin manifest"
summarized_at: 2026-05-05
entities_referenced: [Plugin]
concepts_referenced: []
---

Minimal plugin manifest for the official `commit-commands` plugin. 10-line JSON:

```json
{
  "name": "commit-commands",
  "description": "Streamline your git workflow with simple commands for committing, pushing, and creating pull requests",
  "version": "1.0.0",
  "author": {"name": "Anthropic", "email": "support@anthropic.com"}
}
```

Relies entirely on default directory discovery (`./commands/`) for the bundled commands like `/commit-push-pr`.
