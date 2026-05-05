---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/references/system-prompt-design.md
title: "plugin-dev: agent-development system-prompt-design reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent, Skill]
concepts_referenced: []
---

Reference doc inside `plugin-dev`'s `agent-development` skill. Patterns for writing effective agent system prompts.

**Core structure** every agent should follow:
- `You are [role] specializing in [domain].`
- `**Your Core Responsibilities:**` numbered list
- `**[Task Name] Process:**` numbered concrete steps
- `**Quality Standards:**` bulleted with specifics
- `**Output Format:**` structured template
- `**Edge Cases:**` list of "case: handling"

**Four patterns** with full templates:

1. **Analysis agents** (code/PR/docs analysis): gather context → initial scan → deep analysis (per-aspect criteria) → synthesize → prioritize → generate report. Standards: file:line refs, severity categories (critical/major/minor), actionable recs, balanced positives. Output: Summary / Critical Issues / Major / Minor / Recommendations. Edge cases: no issues found, too many (top 10), unclear code (request clarification).

2. **Generation agents** (create code/tests/docs): understand requirements → gather context → design structure → generate following conventions → validate → document. Standards: project conventions (CLAUDE.md), error handling, well-documented. Edge cases: insufficient context (ask), conflicting patterns (most recent wins), complex (break into pieces).

3. **Validation agents** (validate/check/verify): load criteria → scan → check rules → collect violations → assess severity → determine result. Standards: specific locations, severity, fix suggestions, no false positives. Output: PASS/FAIL header, violations grouped by severity. Edge cases: no violations (confirm), too many (top 20), ambiguous rules (document uncertainty).

4. **Orchestration agents** (coordinate workflows): plan → prepare → execute phases → monitor → verify → report. Output: Workflow Execution Report with completed phases, results, next steps. Edge cases: phase failure (retry then report), missing dependencies (request from user), timeout (partial completion).

**Writing style**:
- Always use **second person** ("You are...", "You will..."). Never "The agent..." or "I will...".
- Be **specific not vague**: "Check for SQL injection by examining all DB queries for parameterization" > "Look for security issues".
- **Actionable instructions** with concrete tools: "Read the file using the Read tool, then search for patterns using Grep" > "Analyze the code".

**Common pitfalls**:
- Vague responsibilities ("help with code") → specific ("Analyze TypeScript code for type safety issues, identify missing annotations and improper 'any' usage").
- Missing process steps ("Analyze the code and provide feedback") → numbered steps with tools.
- Undefined output ("Provide a report") → exact format template with sections.

**Length guidelines**:
- Minimum viable: ~500 words (role + 3 responsibilities + 5-step process + output).
- Standard: ~1,000-2,000 words (8 responsibilities, 8-12 steps, edge cases).
- Comprehensive: ~2,000-5,000 words (multi-phase, in-prompt examples).
- **Avoid >10,000 words** — diminishing returns.

**Test completeness**: typical task, edge cases mentioned, error scenarios, unclear requirements, large/empty inputs. **Test clarity**: another developer can understand, steps actionable, output unambiguous, standards measurable. **Iterate**: identify struggles → add guidance → clarify → re-test.

Effective system prompts are **specific, structured, complete, actionable, testable**.
