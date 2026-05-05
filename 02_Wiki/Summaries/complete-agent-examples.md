---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/examples/complete-agent-examples.md
title: "Complete Agent Examples (plugin-dev skill reference)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Memory]
concepts_referenced: []
---

Production-ready subagent examples from the `plugin-dev/skills/agent-development` skill, intended as templates for users to fork. Note: only the first example was sampled.

**Example 1: Code Review Agent** (`agents/code-reviewer.md`):
- Frontmatter: `name: code-reviewer`, `model: inherit`, `color: blue`, `tools: ["Read", "Grep", "Glob"]`
- Description includes 3 inline `<example>` blocks: explicit review request, post-feature implementation (proactive trigger on payment processing), pre-commit (proactive review)

**Body** establishes the agent as expert code-quality reviewer with 5 core responsibilities: analyze quality (readability/maintainability/complexity), identify security vulnerabilities (SQL injection/XSS/auth flaws), check CLAUDE.md adherence, provide specific actionable feedback with file:line refs, recognize good practices.

**Review process** (6 steps):
1. Gather context (Glob for recently modified files, git diff/status)
2. Read code (use Read tool)
3. Analyze quality (DRY, complexity/readability, error handling, logging)
4. Security analysis (injection vulns, auth/authz, input validation/sanitization, hardcoded secrets)
5. Best practices (CLAUDE.md, naming conventions, test coverage, documentation)
6. Categorize issues by severity (critical/major/minor)

**Quality standards**: every issue includes `src/auth.ts:42`-style location; severity-categorized with clear criteria; specific actionable recommendations (not vague); code examples in recommendations when helpful; balance criticism with recognition.

**Output format** (template): "Code Review Summary" → "Critical Issues (Must Fix)" with file:line / description / why critical / how to fix → "Major Issues (Should Fix)" → "Minor Issues (Consider Fixing)" → "Positive Observations".

The file additionally contains other agent examples (test-writer, doc-generator, etc. — not sampled here).
