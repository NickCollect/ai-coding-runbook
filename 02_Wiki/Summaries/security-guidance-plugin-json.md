---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/security-guidance/.claude-plugin/plugin.json
title: "security-guidance plugin manifest"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks]
concepts_referenced: []
---

Plugin manifest for `security-guidance`:
- `name`: `security-guidance`
- `version`: `1.0.0`
- `description`: "Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns"
- `author`: David Dworken (dworken@anthropic.com)

Implementation: PreToolUse hook monitoring 9 security patterns (command injection, XSS, eval usage, dangerous HTML, pickle deserialization, os.system calls, etc.) when files are edited.
