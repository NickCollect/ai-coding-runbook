---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/commands/configure.md
title: "/hookify:configure command"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Slash-command]
concepts_referenced: []
---

Interactive command in the `hookify` plugin. Enables/disables existing hookify rules through `AskUserQuestion`.

Allowed tools: `Glob`, `Read`, `Edit`, `AskUserQuestion`, `Skill`. Loads `hookify:writing-rules` skill first to understand rule format.

**Steps**:
1. Glob `.claude/hookify.*.local.md` to find rule files. If none → tell user to run `/hookify` first.
2. Read each rule file; extract `name` + `enabled` from frontmatter.
3. Use `AskUserQuestion` (multiSelect) with options labeled `{rule-name} (currently {enabled|disabled})` and brief description.
4. Toggle each selected rule (read → Edit `enabled: true ↔ false`, handling quoted/unquoted variants).
5. Show confirmation summary (Enabled / Disabled / Unchanged sections). Changes apply immediately.

Edge cases: no rules to configure → suggest `/hookify`. No selection → no-op message. Read/write errors → suggest manual editing.
