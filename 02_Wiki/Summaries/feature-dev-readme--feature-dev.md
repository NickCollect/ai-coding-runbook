---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/feature-dev/README.md
title: "feature-dev plugin README"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent]
concepts_referenced: []
---

Documentation for the `feature-dev` plugin — `/feature-dev` command launches a structured 7-phase workflow for building features.

**Phases**:
1. **Discovery** — clarify request, problem, constraints.
2. **Codebase Exploration** — launches 2-3 `code-explorer` agents in parallel (similar features, architecture, UI patterns); each returns key files (5-10) for Claude to read.
3. **Clarifying Questions** — fills ambiguities (edge cases, error handling, integration, scope, design preferences, backward-compat, performance) BEFORE design. Critical phase, do not skip.
4. **Architecture Design** — launches 2-3 `code-architect` agents with different focuses: minimal changes, clean architecture, pragmatic balance. Recommends one. Asks user to choose.
5. **Implementation** — only after explicit user approval. Reads identified files, implements per chosen architecture, follows codebase conventions.
6. **Quality Review** — 3 `code-reviewer` agents in parallel: simplicity/DRY/elegance, bugs/correctness, conventions/abstractions. Confidence-based filtering (≥80). Presents findings, asks user (fix now / fix later / proceed).
7. **Summary** — marks todos complete, summarizes built/decisions/files/next steps.

**Subagents**:
- **code-explorer**: traces execution paths, entry points, data flow, architecture layers; outputs file:line references and essential read list.
- **code-architect**: pattern analysis, architecture decisions with rationale, component design, implementation roadmap, build sequence.
- **code-reviewer**: project guideline compliance (CLAUDE.md), bug detection, quality, confidence ≥80 filter; categorizes critical (75-100) / important (50-74).

**Use for**: multi-file features, architecture-decision features, complex integrations, unclear requirements. **Skip for**: single-line fixes, trivial changes, well-defined simple tasks, urgent hotfixes.

**Best practices**: full workflow for complex features, answer clarifying questions thoughtfully, choose architecture deliberately, don't skip code review, read suggested files. Be specific in feature request to reduce questions.

Author: Sid Bidasaria. Version 1.0.0.
