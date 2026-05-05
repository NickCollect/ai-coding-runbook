---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/learning-output-style/README.md
title: "Learning Style Plugin (README)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Output-style, Hooks, Memory]
concepts_referenced: []
---

Plugin combining the unshipped "Learning" output style with explanatory functionality, implemented as a SessionStart hook. Differs from the plain unshipped Learning style by also incorporating all functionality from the explanatory-output-style plugin (interactive learning + educational insights).

**Warning**: incurs token cost from extra instructions and the interactive nature.

**What it does**: at session start, injects instructions encouraging Claude to:
1. **Learning Mode**: engage user in active learning by requesting meaningful 5-10 line code contributions at decision points
2. **Explanatory Mode**: educational insights about implementation choices and codebase patterns

**Pattern**: instead of implementing everything, Claude identifies opportunities → focuses on business logic / design choices where user input matters → prepares context + location → explains trade-offs → provides educational insights before/after writing code.

**When Claude requests user contributions**: business logic with multiple valid approaches, error handling strategies, algorithm choices, data structure decisions, UX decisions, design patterns / architecture choices.

**When Claude implements directly**: boilerplate, obvious implementations, configuration/setup, simple CRUD.

**Educational insights format**:
```
★ Insight ─────────────────────────────────────
[2-3 key educational points about the codebase or implementation]
─────────────────────────────────────────────────
```
Focus on codebase-specific implementation choices, patterns/conventions, trade-offs — NOT general programming concepts.

**Implementation**: SessionStart hook injects context (rough equivalent to CLAUDE.md but more flexible + plugin-distributable).

**Migration**: combines unshipped "Learning" output style with deprecated "Explanatory" output style. If you previously used explanatory-output-style, this plugin includes all of that PLUS interactive learning.

**Manage**: disable (keep code), uninstall (remove code), update (create local copy to personalize — ask Claude to read the plugins doc and set it up).

**Philosophy**: learning by doing > passive observation. Transforms interaction from "watch and learn" to "build and understand."
