---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/hooks/hooks.json
title: "hooks.json — hookify plugin"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

`hooks.json` for the `hookify` plugin. Wires four Python handlers — one per major event — that read user-defined `.local.md` rule files at runtime and apply matching warn/block actions. All handlers have a 10-second timeout.

```json
{
  "description": "Hookify plugin - User-configurable hooks from .local.md files",
  "hooks": {
    "PreToolUse":       [{"hooks":[{"type":"command","command":"python3 ${CLAUDE_PLUGIN_ROOT}/hooks/pretooluse.py","timeout":10}]}],
    "PostToolUse":      [{"hooks":[{"type":"command","command":"python3 ${CLAUDE_PLUGIN_ROOT}/hooks/posttooluse.py","timeout":10}]}],
    "Stop":             [{"hooks":[{"type":"command","command":"python3 ${CLAUDE_PLUGIN_ROOT}/hooks/stop.py","timeout":10}]}],
    "UserPromptSubmit": [{"hooks":[{"type":"command","command":"python3 ${CLAUDE_PLUGIN_ROOT}/hooks/userpromptsubmit.py","timeout":10}]}]
  }
}
```

Demonstrates the "single dispatcher per event" pattern: the JSON itself never changes; users add/edit `.claude/hookify.{name}.local.md` rule files in their project root, and the Python dispatchers read those files on each event. No restart needed because the dispatchers re-read on each invocation.
