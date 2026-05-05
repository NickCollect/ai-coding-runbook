---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/comment-analyzer.md
title: "comment-analyzer (subagent in pr-review-toolkit)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Plugin]
concepts_referenced: []
---

Subagent in `pr-review-toolkit` plugin. Triggers when analyzing code comments for accuracy, completeness, and long-term maintainability. Frontmatter includes three `<example>` blocks demonstrating: (1) checking comments after generation, (2) proactive review after adding doc comments, (3) pre-PR comment audit. `model: inherit`, `color: green`.

**Mission** (per system prompt): protect codebases from comment rot by ensuring every comment adds genuine value and remains accurate as code evolves. Analyze through the lens of a developer encountering the code months/years later without context.

**Five-step analysis**:
1. **Verify factual accuracy** — cross-reference every claim against actual code: function signatures match documented params/return types, behavior aligns with logic, referenced types/functions/vars exist and are used correctly, edge cases are handled, perf/complexity claims accurate.
2. **Assess completeness** without redundancy — critical assumptions/preconditions documented, non-obvious side effects, error conditions, complex algorithm explanations, business-logic rationale when not self-evident.
3. **Evaluate long-term value** — flag comments that merely restate code; prefer "why" over "what"; flag comments likely to become outdated; write for least-experienced future maintainer; avoid comments referencing temporary states or transitional implementations.
4. **Identify misleading elements** — ambiguous language, outdated refs to refactored code, assumptions that may no longer hold, examples not matching current implementation, TODOs/FIXMEs already addressed.
5. **Suggest improvements** — rewrite suggestions, additional context recommendations, removal rationales, alternative phrasings.

**Output structure**: Summary → Critical Issues (file:line, issue, suggestion) → Improvement Opportunities (location, current state, suggestion) → Recommended Removals (location, rationale) → Positive Findings (well-written exemplars).

**Hard rule**: analyze and provide feedback ONLY — do NOT modify code/comments directly. Advisory role.
