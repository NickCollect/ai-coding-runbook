---
type: summary
source: 01_Raw/github/anthropics/skills/skills/skill-creator/references/schemas.md
title: "skill-creator JSON schemas reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Reference doc inside `skill-creator` defining the seven JSON file schemas used by the skill testing/benchmarking pipeline.

**`evals/evals.json`** — defines test cases per skill: `skill_name` + `evals[]` with `id, prompt, expected_output, files (input paths), expectations[]` (verifiable statements).

**`history.json`** — version progression in Improve mode: `started_at, skill_name, current_best, iterations[]` each with `version (v0/v1/...), parent, expectation_pass_rate, grading_result ("baseline"|"won"|"lost"|"tie"), is_current_best`.

**`grading.json`** — output of grader agent per run. `expectations[]` MUST use exact field names `text, passed, evidence` (other names break the viewer). Includes `summary {passed, failed, total, pass_rate}`, `execution_metrics {tool_calls{Read, Write, Bash}, total_tool_calls, total_steps, errors_encountered, output_chars, transcript_chars}`, `timing {executor_duration_seconds, grader_duration_seconds, total_duration_seconds}`, `claims[]` (extracted factual claims with verification), `user_notes_summary {uncertainties, needs_review, workarounds}`, optional `eval_feedback` for assertion-quality issues.

**`metrics.json`** — output of executor agent: per-tool counts, totals, files created, errors, output/transcript char counts.

**`timing.json`** — wall-clock data. CRITICAL: `total_tokens` and `duration_ms` come from the subagent task notification — capture immediately, NOT persisted elsewhere.

**`benchmark.json`** — output of Benchmark mode. `metadata {skill_name, skill_path, executor_model, analyzer_model, timestamp, evals_run, runs_per_configuration}` + `runs[]` per run + `run_summary {with_skill, without_skill, delta}` (mean/stddev/min/max for pass_rate, time, tokens) + `notes[]` (analyst observations). **Strict field-name requirements**: `configuration` must be `"with_skill"` or `"without_skill"` exactly (used for grouping and color coding); `pass_rate`, `time_seconds`, `tokens` must be nested under `result`, NOT at top level. Wrong names → viewer shows zeroes.

**`comparison.json`** — output of blind comparator: `winner ("A"|"B"), reasoning, rubric {A, B}` (per-output content + structure scores 1-5 in subcategories with aggregated `content_score, structure_score, overall_score`), `output_quality {A, B}` (score + strengths + weaknesses), `expectation_results {A, B}` (pass counts + per-assertion details).

**`analysis.json`** — output of post-hoc analyzer: `comparison_summary {winner, winner_skill, loser_skill, comparator_reasoning}`, `winner_strengths[]`, `loser_weaknesses[]`, `instruction_following {winner, loser}` (score + issues), `improvement_suggestions[]` (priority + category + suggestion + expected_impact), `transcript_insights {winner_execution_pattern, loser_execution_pattern}`.

**Pattern**: every schema example in raw shows the exact JSON shape the consuming script/viewer expects. Always reference this file when generating any of these JSONs manually.
