---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/explanatory-output-style/hooks/hooks.json
title: "hooks.json — explanatory-output-style plugin"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Output-style]
concepts_referenced: []
---

`hooks.json` for the `explanatory-output-style` plugin. Wires a single `SessionStart` command hook that injects educational-insight instructions at session start, recreating the deprecated "Explanatory" output style.

```json
{
  "description": "Explanatory mode hook that adds educational insights instructions",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/hooks-handlers/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

Demonstrates the **`SessionStart` + script injection** pattern for adding to the system prompt without using the deprecated `outputStyle` setting. Pattern is "roughly equivalent to CLAUDE.md but more flexible and distributable through plugins" (per the plugin README).
