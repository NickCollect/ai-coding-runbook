---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/code-simplifier.md
title: "code-simplifier (pr-review-toolkit subagent)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Memory]
concepts_referenced: []
---

Subagent definition (Opus) shipped in `pr-review-toolkit`. Simplifies code for clarity, consistency, maintainability while preserving exact functionality. Triggered automatically after coding tasks or logical chunks of code; focuses only on recently modified code unless instructed otherwise.

**Frontmatter**: `name: code-simplifier`, `model: opus`. Description includes 3 inline `<example>` blocks (post-feature implementation; post-bug-fix; post-performance-optimization) — all proactively triggered.

**Five rules**:
1. **Preserve functionality** — never change WHAT the code does, only HOW
2. **Apply project standards** from CLAUDE.md, examples: ES modules with proper import sorting + extensions; prefer `function` over arrow functions; explicit return type annotations for top-level functions; React patterns with explicit Props types; proper error handling (avoid try/catch when possible); consistent naming
3. **Enhance clarity** — reduce complexity/nesting, eliminate redundancy, improve names, consolidate logic, remove obvious-code comments. **Avoid nested ternaries — prefer switch or if/else chains.** Choose clarity over brevity.
4. **Maintain balance** — avoid over-simplification that reduces clarity, creates clever-but-hard-to-understand code, combines too many concerns, removes helpful abstractions, prioritizes "fewer lines" over readability, makes code harder to debug/extend
5. **Focus scope** — only refine recently modified or session-touched code unless explicitly broader

**Process**: identify recently modified sections → analyze for elegance/consistency opportunities → apply CLAUDE.md project standards → verify functionality unchanged → verify simpler + more maintainable → document only significant changes affecting understanding.

Operates autonomously and proactively without explicit requests.
