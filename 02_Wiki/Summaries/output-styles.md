---
type: summary
source: 01_Raw/code.claude.com/docs/en/output-styles.md
source_url: https://code.claude.com/docs/en/output-styles
title: "Output styles"
summarized_at: 2026-05-05
entities_referenced: [Output-style, Memory, Subagent, Skill, Plugin, Settings]
concepts_referenced: [Prompt-caching]
---

Output styles **modify Claude Code's system prompt** to set role/tone/output format, while keeping core capabilities (Bash, file I/O, TodoWrite). Use one when you keep re-prompting for the same voice/format every turn or want Claude acting as something other than a software engineer. **Distinct from CLAUDE.md** (project rules) and `--append-system-prompt` — output styles can REPLACE the coding-focused parts of the default prompt.

**Three built-in styles**:
- **Default** — existing software-engineering system prompt
- **Explanatory** — adds educational "Insights" between coding tasks; helps you understand implementation choices and codebase patterns
- **Learning** — collaborative learn-by-doing; Claude shares Insights AND inserts `TODO(human)` markers asking you to write small strategic pieces of code

**How they work**:
- Custom styles **exclude** coding instructions (e.g. verifying code with tests) UNLESS frontmatter `keep-coding-instructions: true`
- Custom instructions appended to end of system prompt
- All styles trigger reminders for Claude to keep adhering during the conversation

Token impact: input tokens up due to longer system prompt (offset by prompt caching after first request). Explanatory + Learning produce longer responses (more output tokens) by design.

**Change style**: `/config` → Output style menu → saved to `.claude/settings.local.json`. Or set `outputStyle` directly in any settings file. Takes effect on **next session start** (kept stable so prompt caching works).

**Custom output style** = Markdown file with frontmatter:
```markdown
---
name: My Custom Style
description: Brief description shown in /config picker
keep-coding-instructions: false   # default
---

# Custom Style Instructions
You are an interactive CLI tool that helps users with software engineering...
```

Locations: `~/.claude/output-styles/` (user) or `.claude/output-styles/` (project). Plugins can ship via `output-styles/` directory.

**Frontmatter fields**: `name` (defaults to filename), `description`, `keep-coding-instructions` (default false).

**Comparisons**:
- vs **CLAUDE.md** / `--append-system-prompt` — output styles can turn OFF default coding prompt parts; CLAUDE.md adds as a *user message* AFTER the default system prompt; `--append-system-prompt` appends to the system prompt without removing anything.
- vs **Subagents** — output styles affect main agent loop / system prompt only. Subagents are task-invoked with their own model, tools, when-to-use context.
- vs **Skills** — output styles modify HOW Claude responds (always active once selected). Skills are task-specific prompts invoked via `/skill-name` or auto-loaded by relevance.
