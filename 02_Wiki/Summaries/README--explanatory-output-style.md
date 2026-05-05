---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/explanatory-output-style/README.md
title: "Explanatory Output Style Plugin"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Output-style, Hooks, Subagent, Memory]
concepts_referenced: []
---

Plugin that **recreates the deprecated Explanatory output style as a `SessionStart` hook**. Warning: incurs token cost from the additional injected instructions and from the longer responses.

**Behavior**: at session start, injects instructions encouraging Claude to:
1. Provide educational insights about implementation choices
2. Explain codebase patterns and decisions
3. Balance task completion with learning opportunities

Format Claude is instructed to use:
```
★ Insight ─────────────────────────────────────
[2-3 key educational points]
─────────────────────────────────────────────────
```

Insights focus on: implementation choices for the user's specific codebase, patterns/conventions in their code, trade-offs and design decisions, codebase-specific details rather than general programming concepts.

**Migration**: replaces the deprecated `{"outputStyle": "Explanatory"}` setting. Same effect via the plugin install.

**Pattern note in raw**: SessionStart hook is roughly equivalent to CLAUDE.md but more flexible and distributable through plugins. **However**: output styles for tasks BEYOND software development are better expressed as **subagents** (which change the system prompt) rather than SessionStart hooks (which add to it).

**Lifecycle controls**: disable (keep installed), uninstall (remove entirely), update (clone for personalization).
