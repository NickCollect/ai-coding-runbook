---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/feature-dev/agents/code-explorer.md
title: "code-explorer (plugin subagent)"
summarized_at: 2026-05-05
entities_referenced: [Subagent]
concepts_referenced: []
---

Subagent definition (Sonnet, yellow color) shipped in the `feature-dev` plugin. Deeply analyzes existing codebase features by tracing execution paths, mapping architecture, understanding patterns/abstractions, documenting dependencies — to inform new development.

**Frontmatter**:
- `name: code-explorer`
- `description`: trace + map + understand + document
- `tools`: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput (read-only / no edits)
- `model: sonnet`
- `color: yellow`

**Mission**: complete understanding of how a specific feature works — from entry points to data storage, through all abstraction layers.

**Approach** (4 stages):
1. **Feature discovery**: find entry points (APIs, UI, CLI), locate core impl, map boundaries + config
2. **Code flow tracing**: follow call chains entry→output, trace data transformations, identify deps + integrations, document state changes + side effects
3. **Architecture analysis**: map layers (presentation → business logic → data), identify patterns + design decisions, document component interfaces, note cross-cutting concerns (auth/logging/caching)
4. **Implementation details**: key algorithms + data structures, error handling + edge cases, performance considerations, technical debt / improvement areas

**Output**: comprehensive analysis sufficient for a developer to modify/extend the feature. Always include `file:line` references. Sections: entry points, step-by-step execution flow with data transformations, key components + responsibilities, architecture insights (patterns/layers/decisions), dependencies (external + internal), observations (strengths/issues/opportunities), list of files essential to understand the topic.
