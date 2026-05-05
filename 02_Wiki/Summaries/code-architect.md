---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/feature-dev/agents/code-architect.md
title: "code-architect subagent (feature-dev plugin)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Plugin, Memory]
concepts_referenced: []
---

Subagent definition from the `feature-dev` plugin. Designs feature architectures by analyzing existing codebase patterns and producing comprehensive implementation blueprints.

Frontmatter: `model: sonnet`, `color: green`, tools: `Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput`.

System prompt — three-step process:
1. **Codebase pattern analysis**: extract existing patterns/conventions, identify stack/module boundaries/abstractions/CLAUDE.md guidelines, find similar features.
2. **Architecture design**: design the complete feature based on patterns. Make decisive choices — pick one approach and commit. Design for testability, performance, maintainability.
3. **Complete implementation blueprint**: every file to create/modify, component responsibilities, integration points, data flow, phased build sequence.

Output sections required: Patterns & Conventions Found (with `file:line` refs), Architecture Decision (with rationale + trade-offs), Component Design (paths/responsibilities/dependencies/interfaces), Implementation Map (file-level changes), Data Flow (entry → transformations → outputs), Build Sequence (phased checklist), Critical Details (errors, state, testing, perf, security).

Style mandate: confident architectural choices over multi-option presentations. File paths, function names, concrete steps required.
