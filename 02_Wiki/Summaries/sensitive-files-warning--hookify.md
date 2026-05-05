---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/examples/sensitive-files-warning.local.md
title: "hookify plugin: sensitive-files-warning example rule"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks]
concepts_referenced: []
---

Example hookify rule file (`sensitive-files-warning.local.md`) demonstrating the rule format used by the `hookify` plugin.

**Frontmatter**:
```yaml
name: warn-sensitive-files
enabled: true
event: file
action: warn
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$|\.env\.|credentials|secrets
```

**Body**: warning message displayed when triggered: 🔐 Sensitive file detected — ensure no hardcoded credentials, use env vars for secrets, verify gitignore inclusion, consider secrets manager.

Demonstrates the schema: top-level `event`/`action`, list of `conditions` with `field` + `operator` + `pattern`. Markdown body becomes the warning shown to the user.
