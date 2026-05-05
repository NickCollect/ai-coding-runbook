---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/README.md
title: "Hookify Plugin"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks, Slash-command]
concepts_referenced: []
---

Plugin (MIT, Python 3.7+ stdlib only) that lets users author hooks via lightweight markdown files instead of editing `hooks.json`. Rules live in `.claude/hookify.{name}.local.md` (project's `.claude/`, NOT plugin's). Take effect immediately on next tool use, no restart.

**Commands**:
- `/hookify <prose>` — analyze conversation OR explicit instructions, generate rule file
- `/hookify:list` — show all rules
- `/hookify:configure` — interactive enable/disable
- `/hookify:help`

**Rule file format** (YAML frontmatter + markdown body for the message):
```markdown
---
name: block-dangerous-rm
enabled: true
event: bash
pattern: rm\s+-rf
action: block
---

⚠️ Dangerous rm command detected!
```

**Action**: `warn` (default — show message, allow operation) or `block` (PreToolUse blocks, Stop events stop session).

**Event types**: `bash` (Bash tool), `file` (Edit/Write/MultiEdit), `stop` (Claude wants to stop — for completion checks), `prompt` (user prompt submit), `all`.

**Multi-condition rules** (all must match):
```yaml
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$|credentials|secrets
  - field: new_text
    operator: contains
    pattern: KEY
```

**Operators**: `regex_match`, `contains`, `equals`, `not_contains`, `starts_with`, `ends_with`.

**Fields**:
- bash: `command`
- file: `file_path`, `new_text`, `old_text` (Edit), `content` (Write)
- prompt: `user_prompt`
- stop: general session-state matching

**Pattern syntax**: Python regex. Use `\s` for whitespace, `\.` for literal dot, `(foo|bar)` for alternation.

**Examples shipped**: block destructive ops (`rm -rf`, `dd if=`, `mkfs`, `format`), warn debug code (`console.log`, `debugger;`, `print(`), require tests before stopping (block stop if `npm test|pytest|cargo test` not in transcript).

**Mgmt**: edit `enabled:` to toggle. Delete file to remove. Test patterns separately with `python3 -c "import re; print(re.search(r'pattern', 'text'))"`. Plugin auto-discovered via marketplace; manual: `cc --plugin-dir /path/to/hookify`.
