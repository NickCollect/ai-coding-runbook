---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/ralph-wiggum/hooks/hooks.json
title: "hooks.json — ralph-wiggum plugin"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

`hooks.json` for the `ralph-wiggum` plugin (self-restarting agent loop). Single `Stop` event hook that runs a script to potentially re-feed the original prompt back to Claude.

```json
{
  "description": "Ralph Wiggum plugin stop hook for self-referential loops",
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/hooks/stop-hook.sh"
          }
        ]
      }
    ]
  }
}
```

The `stop-hook.sh` (not in this file) implements the loop logic: when Claude tries to stop, the hook checks for a completion-promise match and either lets the stop proceed OR re-injects the saved prompt to start the next iteration. See companion `/ralph-wiggum:ralph-loop` slash command.
