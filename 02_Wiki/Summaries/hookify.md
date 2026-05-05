---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/commands/hookify.md
title: "/hookify command (slash command definition)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Hooks, Skill, Subagent]
concepts_referenced: []
---

Slash command definition for `/hookify`. Frontmatter: `description`, `argument-hint`, `allowed-tools: ["Read", "Write", "AskUserQuestion", "Task", "Grep", "TodoWrite", "Skill"]`.

**Workflow** instructed to Claude:

**Step 1: Gather behavior info**
- If `$ARGUMENTS` provided: use the explicit instructions; still scan recent 10-15 user messages for context.
- If empty: launch `conversation-analyzer` general-purpose subagent to scan user messages for explicit don'ts, corrections, frustration signals, repeated issues. Returns structured findings (category, tool, pattern, context, severity).

**FIRST step**: Load the `hookify:writing-rules` skill via the Skill tool to learn rule format.

**Step 2: Present findings via `AskUserQuestion`**:
- Q1 (multiSelect): "Which behaviors to hookify?" — up to 4 options
- Q2 (per behavior): warn vs block
- Q3: confirm/refine patterns

**Step 3: Generate rule files** at `.claude/hookify.{rule-name}.local.md` (project cwd, NOT plugin dir). Naming: kebab-case, action verb prefix (`block-`, `warn-`, `prevent-`, `require-`).

Rule file format:
```markdown
---
name: {rule-name}
enabled: true
event: {bash|file|stop|prompt|all}
pattern: {regex}
action: {warn|block}
---
{Message to show Claude}
```

Multi-condition variant uses `conditions:` array.

**Step 4**: ensure `.claude/` exists in cwd, write file with relative path, list to verify, inform user "active immediately, no restart needed."

**Pattern tips for Claude**: bash dangerous (`rm\s+-rf|chmod\s+777|dd\s+if=`), tools (`npm\s+install|pip\s+install`), file code (`console\.log\(|eval\(|innerHTML\s*=`), file paths (`\.env$|\.git/|node_modules/`).

Troubleshooting tail: pwd check, `mkdir .claude` if missing, regex test via `python3 -c "import re; print(re.search(...))"`, confirm `enabled: true`. To soften too-strict block: change `block` → `warn`. Use TodoWrite to track step progress.
