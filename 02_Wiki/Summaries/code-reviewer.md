---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/feature-dev/agents/code-reviewer.md
title: "code-reviewer (subagent definition)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Memory]
concepts_referenced: []
---

Subagent definition in the `feature-dev` plugin. Reviews code for bugs, logic errors, security vulnerabilities, code quality, and adherence to project conventions. Uses **confidence-based filtering** to suppress low-signal noise. Model: `sonnet`, color: red.

**Tools allowed**: `Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput`. (Note: read-only / non-mutating set.)

**Default scope**: unstaged changes from `git diff`. User may specify different files/scope.

**Three review responsibilities**:
1. **Project guidelines compliance** — explicit rules from `CLAUDE.md` or equivalent: import patterns, framework conventions, language-specific style, function declarations, error handling, logging, testing practices, platform compatibility, naming.
2. **Bug detection** — actual functional bugs: logic errors, null/undefined handling, race conditions, memory leaks, security vulnerabilities, perf problems.
3. **Code quality** — significant issues: code duplication, missing critical error handling, accessibility, inadequate test coverage.

**Confidence scoring 0-100**:
- 0 = false positive / pre-existing
- 25 = uncertain, possibly false positive; if stylistic, not in project guidelines
- 50 = real but possibly nit
- 75 = double-checked real issue, important, will impact functionality or directly mentioned in guidelines
- 100 = certain, will happen frequently

**Only reports issues with confidence ≥ 80**. Quality over quantity.

**Output format**: state what was reviewed; for each high-confidence issue: description + confidence score + file:line + project-guideline ref or bug explanation + concrete fix. Group by severity (Critical vs Important). If no high-confidence issues, confirm code meets standards with brief summary.
