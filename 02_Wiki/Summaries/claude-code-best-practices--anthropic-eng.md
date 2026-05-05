---
type: summary
source: 01_Raw/anthropic.com/engineering/claude-code-best-practices.md
source_url: https://www.anthropic.com/engineering/claude-code-best-practices
title: "Best practices for Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Status-line, IDE-integration]
concepts_referenced: [Context-window, Agentic-loop]
---

Anthropic's authoritative best-practices guide for working effectively with Claude Code. Frames Claude Code as agentic — Claude reads files, runs commands, makes changes, autonomously works through problems. The user describes intent; Claude explores, plans, implements.

**Foundational constraint: context-window management.** Most best practices stem from the fact that Claude's context fills fast (every message, every file read, every command output), and LLM performance degrades as it fills. Track usage via custom status-line; see "Reduce token usage" docs.

**Top high-leverage practices:**

1. **Give Claude a way to verify its work** — single highest-leverage thing. Include tests, screenshots, expected outputs. Without success criteria, Claude produces things that look right but aren't. Examples — "implement validateEmail" → add example test cases and ask Claude to run tests; "make dashboard look better" → paste screenshot, ask for screenshot comparison; "build is failing" → paste error, fix root cause not symptom. UI verification can use Claude in Chrome extension. Verification can also be a test suite, linter, or bash check command.

2. **Explore first, then plan, then code.** Use [plan mode](https://www.anthropic.com/engineering/permission-mode) (Permission-mode = plan) — Claude reads/answers without changes. Workflow: Explore (read files, understand existing systems) → Plan (`Ctrl+G` opens plan in editor for direct edits) → Implement (switch out of plan mode, verify against plan, run tests) → Commit (descriptive message + PR). Skip planning when scope is clear and the diff fits one sentence (typo, log line, rename).

3. **Provide specific context in prompts.** Scope task (file, scenario, mocks-or-no), point to sources (git history of weird APIs), reference existing patterns (point to HotDogWidget.php as example), describe symptom + likely location + what "fixed" looks like. Each example shows a "before/after" rewrite.

The post continues with patterns covering: handling long sessions, when to compact vs reset, working with tests, working with subagents, when to use plan mode, how to communicate with Claude when it diverges. (Doc index at code.claude.com/docs/llms.txt for the full reference.)

The guide is positioned as an entry point for engineers learning Claude Code's autonomy curve. The recurring theme: Claude is constrained primarily by context-window management and verification feedback loops — invest in both.
