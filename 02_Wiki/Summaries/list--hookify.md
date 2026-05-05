---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/commands/list.md
title: "hookify plugin: /hookify:list command"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Hooks, Skill]
concepts_referenced: []
---

Slash command from `hookify` plugin — lists all configured hookify rules in the project.

**Frontmatter**: `description: List all configured hookify rules`, `allowed-tools: ["Glob", "Read", "Skill"]`.

**Workflow**:
1. Load `hookify:writing-rules` skill first to understand rule format.
2. Glob `.claude/hookify.*.local.md`.
3. Read each, extract frontmatter (`name`, `enabled`, `event`, `pattern`) and message preview (first 100 chars).
4. Render a table: name, enabled (✅/❌), event, pattern, file. With per-rule preview block showing message excerpt and status.
5. Footer instructions: edit `.local.md` to modify; `enabled: false` to disable; remove file to delete; use `/hookify` to create. Changes take effect immediately, no restart needed.

**If no rules**: print empty-state guidance pointing to `/hookify`, manual `.claude/hookify.my-rule.local.md`, `/hookify:help`, and `${CLAUDE_PLUGIN_ROOT}/examples/`.
