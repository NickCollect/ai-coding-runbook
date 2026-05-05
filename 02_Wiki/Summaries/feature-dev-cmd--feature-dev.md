---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/feature-dev/commands/feature-dev.md
title: "feature-dev plugin: /feature-dev command"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent]
concepts_referenced: []
---

The `/feature-dev` slash command body — instruction prompt for Claude defining the 7-phase feature development workflow. (See `feature-dev-readme--feature-dev` for full plugin description.)

**Frontmatter**: `description: Guided feature development with codebase understanding and architecture focus`, `argument-hint: Optional feature description`.

**Core principles**:
- Ask clarifying questions early (after codebase exploration, before architecture). Specific concrete questions, no assumptions, wait for answers.
- Understand before acting.
- Read files identified by agents (agents return 5-10 key files; Claude reads them).
- Simple and elegant.
- Use TodoWrite to track progress throughout.

**Phases (condensed from command body)**:
- Phase 1: Discovery — clarify request, summarize, confirm with user.
- Phase 2: Codebase Exploration — 2-3 parallel `code-explorer` agents on different aspects (similar features, abstractions, architecture, UI patterns); read all returned files.
- Phase 3: Clarifying Questions — DO NOT SKIP. Identify gaps; if user says "whatever you think is best", give recommendation + get explicit confirmation.
- Phase 4: Architecture Design — 2-3 `code-architect` agents (minimal/clean/pragmatic); recommend one with reasoning; ask user to pick.
- Phase 5: Implementation — DO NOT START WITHOUT USER APPROVAL. Read all relevant files, follow codebase conventions, document, update todos.
- Phase 6: Quality Review — 3 `code-reviewer` agents (simplicity/DRY/elegance, bugs/correctness, project conventions/abstractions); ask user fix-now/fix-later/proceed.
- Phase 7: Summary — mark todos complete, document what was built / decisions / files / next steps.
