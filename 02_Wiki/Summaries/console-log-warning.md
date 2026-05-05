---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/examples/console-log-warning.local.md
title: "warn-console-log (hookify example rule)"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

Example hookify rule file (`.claude/hookify.console-log-warning.local.md`). Demonstrates the rule schema:

```yaml
---
name: warn-console-log
enabled: true
event: file
pattern: console\.log\(
action: warn
---
```

Triggers on file edits matching `console.log(` regex; warns Claude with a body suggesting that this might be debug code, may ship to prod, may need a logging library instead. Default action `warn` allows the operation through.
