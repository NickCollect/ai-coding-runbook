---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/learning-output-style/hooks/hooks.json
title: "learning-output-style hooks.json"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Output-style]
concepts_referenced: []
---

Hook config for the `learning-output-style` plugin. Single `SessionStart` hook that runs `${CLAUDE_PLUGIN_ROOT}/hooks-handlers/session-start.sh` to inject interactive learning instructions into the session at startup.

Top-level `description`: "Learning mode hook that adds interactive learning instructions". Empty matcher (fires on every session start). Uses the plugin-format wrapper (`{description, hooks: {...}}`) and `${CLAUDE_PLUGIN_ROOT}` for portable script reference.
