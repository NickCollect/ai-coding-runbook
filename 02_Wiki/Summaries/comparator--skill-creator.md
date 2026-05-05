---
type: summary
source: 01_Raw/github/anthropics/skills/skills/skill-creator/agents/comparator.md
title: "Blind Comparator Agent (skill-creator)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Skill]
concepts_referenced: []
---

Subagent in the `skill-creator` skill for comparing two skill outputs WITHOUT knowing which skill produced which (prevents bias). Used during skill evaluation.

**Inputs**: `output_a_path`, `output_b_path`, `eval_prompt`, optional `expectations`.

**7-step process**:
1. Read both outputs (file or directory; examine all relevant files inside dirs).
2. Understand the task from `eval_prompt` — what should be produced, what qualities matter.
3. Generate evaluation rubric with 2 dimensions:
   - **Content rubric**: correctness, completeness, accuracy (1=poor, 3=acceptable, 5=excellent).
   - **Structure rubric**: organization, formatting, usability (same scale).
   - Adapt criteria per task type (PDF form → field alignment/text readability/data placement; document → section structure/heading hierarchy; data → schema correctness).
4. Score each criterion 1–5; calculate per-dimension totals; average to overall 1–10.
5. Check assertions if `expectations` provided — count pass rates as secondary evidence.
6. Determine winner — primary: rubric score; secondary: assertion pass rate; tiebreaker: TIE only if truly equal. Be decisive — ties should be rare.
7. Write JSON results to specified path (default `comparison.json`).

**Output JSON shape**: `{winner, reasoning, rubric: {A: {content: {...}, structure: {...}, content_score, structure_score, overall_score}, B: {...}}}`.
