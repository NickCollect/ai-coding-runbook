---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/type-design-analyzer.md
title: "type-design-analyzer (pr-review-toolkit subagent)"
summarized_at: 2026-05-05
entities_referenced: [Subagent]
concepts_referenced: []
---

Subagent definition shipped in `pr-review-toolkit`. Analyzes type designs for invariant strength, encapsulation quality, practical usefulness. Use when (1) introducing new type, (2) PR creation reviewing all added types, (3) refactoring existing types.

**Frontmatter**: `name: type-design-analyzer`, `model: inherit`, `color: pink`. Description has 2 `<example>` blocks (new UserAccount type, PR with several new data model types).

**Analysis framework** (5-step):
1. **Identify invariants**: data consistency, valid state transitions, field-relationship constraints, business rules, pre/postconditions (implicit + explicit)
2. **Evaluate encapsulation (1-10)**: hidden internals, can invariants be violated externally, access modifiers, minimal+complete interface
3. **Assess invariant expression (1-10)**: clarity through structure, compile-time enforcement, self-documenting design, edge cases obvious from definition
4. **Judge invariant usefulness (1-10)**: prevent real bugs, aligned with business reqs, easier reasoning, neither too restrictive nor permissive
5. **Examine invariant enforcement (1-10)**: construction-time checks, all mutation points guarded, impossible to create invalid instances, appropriate runtime checks

**Output format** (template): `## Type: [TypeName]` → Invariants Identified (list) → Ratings (4 categories with X/10 + brief justification each) → Strengths → Concerns → Recommended Improvements (concrete + actionable, won't overcomplicate codebase).

**Key principles**: prefer compile-time guarantees, value clarity over cleverness, consider maintenance burden, perfect is enemy of good (suggest pragmatic improvements), make illegal states unrepresentable, constructor validation crucial, immutability often simplifies invariants.

**Anti-patterns to flag**: anemic domain models with no behavior, types exposing mutable internals, invariants only in documentation, types with too many responsibilities, missing construction validation, inconsistent enforcement across mutations, types relying on external code for invariants.

When suggesting improvements: weigh complexity cost, breaking-change cost, codebase skill level/conventions, performance implications, safety vs usability balance.
