---
type: summary
source: 01_Raw/github/anthropics/skills/skills/skill-creator/agents/analyzer.md
title: "skill-creator skill: post-hoc analyzer agent"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: []
---

Subagent inside the `skill-creator` skill. Two distinct purposes: (a) post-hoc blind comparison analysis; (b) benchmark results pattern analysis.

**Purpose A — Post-hoc blind comparison**: after blind comparator picks a winner between two skills, "unblind" by examining skills + transcripts to extract WHY winner won and how loser can improve.

Inputs: winner/loser skill paths, winner/loser transcript paths, comparison_result_path, output_path.

Process (8 steps):
1. Read comparison result (winner side, reasoning, scores).
2. Read both skills (SKILL.md + key referenced files) — identify structural differences (instructions clarity, tool usage, examples, edge cases).
3. Read both transcripts — compare execution (instruction adherence, tools used differently, divergence from optimal, errors/recovery).
4. Analyze instruction following — did agents follow explicit instructions / use provided tools/scripts / miss opportunities / add unnecessary steps. Score 1-10.
5. Identify winner strengths (clearer instructions, better scripts, more comprehensive examples, error handling). Quote specifics.
6. Identify loser weaknesses (ambiguous instructions, missing tools, edge case gaps, poor error handling).
7. Generate improvement suggestions for loser skill — instruction changes, tools/scripts, examples, edge cases. Prioritize by impact.
8. Write JSON to output_path with `comparison_summary`, `winner_strengths`, `loser_weaknesses`, `instruction_following` (per-side score+issues), `improvement_suggestions` (priority/category/suggestion/expected_impact), `transcript_insights`.

Suggestion categories: `instructions`, `tools`, `examples`, `error_handling`, `structure`, `references`. Priorities: high (would change outcome), medium (quality up but might not flip), low (marginal).

**Purpose B — Benchmark results analysis**: surface patterns across runs. Inputs: benchmark_data_path, skill_path, output_path.

Process: read benchmark.json → analyze per-assertion patterns (always-pass-both / always-fail-both / value-add-with-skill / hurts-with-skill / highly-variable) → cross-eval patterns → metrics patterns (time, tokens, tool_calls, outliers) → write freeform observations as JSON array of strings.

Notes should: state observation, ground in data (no speculation), help interpret beyond aggregates. NOT subjective judgments, NOT improvement suggestions (separate step), NOT cause speculation without evidence.

**Guidelines**: be specific (quote skills/transcripts), actionable (concrete changes), focus on skill improvements (not critiquing agent), prioritize by impact, consider causation vs incidental, stay objective, think generalization (would this help other evals?).
