---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/commands/help.md
title: "/hookify:help (plugin slash command)"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Slash-command]
concepts_referenced: []
---

Help command for the `hookify` plugin. Hookify makes it easy to create custom hooks that prevent unwanted behaviors — instead of editing `hooks.json`, users create simple markdown rule files at `.claude/hookify.{rule-name}.local.md`.

**Frontmatter**: `description: Get help with the hookify plugin`, `allowed-tools: ["Read"]`.

**How it works**:
1. Hookify installs generic hooks on `PreToolUse`, `PostToolUse`, `Stop`, `UserPromptSubmit`. These hooks read `.claude/hookify.*.local.md` files dynamically and check rules.
2. Rules are markdown with YAML frontmatter:
   - `name`: unique identifier
   - `enabled`: true/false
   - `event`: `bash`, `file`, `stop`, `prompt`, or `all`
   - `pattern`: regex pattern (Python regex syntax)
   - `action`: `block` (prevent execution) or `warn` (show message but allow)
   - Body: message Claude sees when rule triggers

**Rule creation paths**:
- `/hookify Don't use console.log in production files` — Claude analyzes request + creates rule file
- Manual file creation
- `/hookify` (no args) — analyze recent conversation to find behaviors to prevent

**Commands**: `/hookify`, `/hookify:help`, `/hookify:list`, `/hookify:configure`.

**Pattern syntax** (Python regex): `\s` whitespace, `\.` literal dot, `|` OR, `+` one+, `*` zero+, `\d` digit, `[abc]` character class. Examples: `rm\s+-rf`, `console\.log\(`, `(eval|exec)\(`, `\.env$`.

**Important notes**:
- **No restart needed** — `.local.md` files take effect immediately on next tool use
- Block vs warn via `action:` field
- Rules should be gitignored (add `.claude/hookify.*.local.md` to `.gitignore`)
- Disable via `enabled: false` or delete file

**Troubleshooting**: check rule file in `.claude/`, `enabled: true`, valid regex (test with `python3 -c "import re; print(re.search('your_pattern', 'test_text'))"`); Python 3 available; YAML escaping issues.

Examples in `${CLAUDE_PLUGIN_ROOT}/examples/`.
