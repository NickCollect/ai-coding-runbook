---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/security-guidance/hooks/hooks.json
title: "security-guidance hooks.json"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

Hook config for the `security-guidance` plugin. Single `PreToolUse` hook with matcher `Edit|Write|MultiEdit` that runs `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/security_reminder_hook.py` before any file-modification tool call. Wrapped in plugin-format with description "Security reminder hook that warns about potential security issues when editing files".
