---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/code-reviewer.md
source_url: https://github.com/anthropics/claude-code/blob/main/plugins/pr-review-toolkit/agents/code-reviewer.md
title: "claude-code — PR Review Toolkit: Code Reviewer Agent Definition"
summarized_at: 2026-05-05
entities_referenced: ["Anthropic"]
concepts_referenced: ["code review", "agent", "PR review", "CLAUDE.md", "confidence scoring", "static analysis", "subagent"]
---

Claude Code agent definition for automated code review. Part of the pr-review-toolkit plugin.

Trigger: After writing/modifying code, especially before committing or creating PRs.
Scope: Default is unstaged changes (git diff); can specify files.
Model: opus. Color: green.

Review Responsibilities:
1. Project Guidelines Compliance (CLAUDE.md): import patterns, naming, testing, error handling, etc.
2. Bug Detection: logic errors, null handling, race conditions, memory leaks, security issues
3. Code Quality: duplication, missing error handling, accessibility

Issue Confidence Scoring (0-100):
- Only reports issues with confidence >= 80
- 91-100: Critical bug or explicit CLAUDE.md violation
- 80-89: Important issue requiring attention

Output: Groups by severity (Critical 90-100, Important 80-89); provides file/line, rule explanation, concrete fix.
