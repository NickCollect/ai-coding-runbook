---
type: summary
source: 01_Raw/github/anthropics/skills/skills/skill-creator/SKILL.md
title: "Skill: skill-creator (full version)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

The current/canonical `skill-creator` skill — used to create new skills, modify existing ones, and benchmark skill performance. Distinct from the simpler `skill-creator-original.md` reference shipped inside `plugin-dev` (which is the source the plugin-dev variant adapts).

**High-level loop**:
1. Decide what the skill does and roughly how
2. Write a draft
3. Create test prompts and run "claude-with-access-to-the-skill" on them
4. Help user evaluate qualitatively + quantitatively (use `eval-viewer/generate_review.py`)
5. Rewrite based on feedback
6. Repeat until satisfied
7. Optionally expand test set; run skill description optimizer for triggering

**Anatomy**: SKILL.md (YAML frontmatter `name`+`description` required + markdown body) + optional `scripts/` `references/` `assets/`.

**Progressive disclosure** three-level: metadata (always in context, ~100 words), SKILL.md body (when triggered, <500 lines ideal), bundled resources (as needed).

**Description writing**: this is the primary triggering mechanism. Include WHAT + WHEN. Make descriptions slightly **pushy** because Claude tends to UNDER-trigger skills. Example: instead of "How to build a simple dashboard...", write "How to build a simple dashboard... Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"

**Writing style**: imperative form. Explain the WHY (LLMs have theory of mind; rote MUSTs are less effective than good explanations). Avoid all-caps ALWAYS/NEVER unless truly required.

**Domain organization**: when supporting multiple variants (cloud-deploy supporting AWS/GCP/Azure), put workflow + selector in SKILL.md and per-variant detail in `references/aws.md`, `references/gcp.md`, etc.

**Test workflow**:
1. **Spawn all runs in same turn** (with-skill + baseline). For new skill, baseline is no skill. For improving an existing skill, snapshot the old version (`cp -r skill-path workspace/skill-snapshot`) and use that as baseline.
2. **While runs progress**, draft assertions. Subjective skills (writing style, design quality) skip assertions — go qualitative only.
3. **Capture timing data** (`total_tokens`, `duration_ms`) immediately on subagent task notifications.
4. **Grade** via `agents/grader.md` subagent (fields `text`/`passed`/`evidence` — exact names matter for viewer).
5. **Aggregate** via `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`.
6. **Analyst pass** per `agents/analyzer.md` — surface non-discriminating assertions, high-variance evals, time/token tradeoffs.
7. **Launch viewer**: `nohup python <skill-creator-path>/eval-viewer/generate_review.py <workspace>/iteration-N --skill-name "..." --benchmark <...>/benchmark.json &`. For iteration 2+, add `--previous-workspace`. Cowork/headless: `--static <output_path>` writes standalone HTML.
8. **Read feedback** from `feedback.json` (one entry per `run_id`).

**Iteration mantras** for improvement: generalize from feedback (don't overfit), keep the prompt lean (remove things not pulling weight; read transcripts for unproductive work), explain the why, look for repeated work across test cases (extract into bundled scripts).

**Description optimization** (separate Step in workflow): generate 20 trigger eval queries (8-10 should-trigger + 8-10 should-NOT-trigger), present via `assets/eval_review.html` template (placeholders `__EVAL_DATA_PLACEHOLDER__`, `__SKILL_NAME_PLACEHOLDER__`, `__SKILL_DESCRIPTION_PLACEHOLDER__`), user edits + exports. Then run `python -m scripts.run_loop --eval-set ... --skill-path ... --model <session-model> --max-iterations 5 --verbose` — splits 60% train / 40% test, evaluates each query 3× for reliable trigger rate, iterates up to 5 times, picks `best_description` by **test** score (not train) to avoid overfitting.

**Triggering note**: Claude only consults skills for tasks it can't easily handle on its own — simple one-step queries ("read this PDF") may not trigger even with perfect description. Use substantive queries for evals.

**Environment variants**:
- **Claude.ai**: no subagents — run tests one at a time as the same agent (less rigorous, but human review compensates). Skip browser viewer (no display) — present results inline. Skip benchmarking. Skip description optimization (`claude` CLI required). Updating an existing skill: preserve original name, copy to `/tmp/<name>/` to edit (installed path is read-only), package from copy.
- **Cowork**: subagents work; no browser/display → `--static` flag for viewer; feedback downloads as file. Description optimization works fine via `claude -p`. Generate eval viewer **before** evaluating outputs yourself.

Communication style: pay attention to user's tech literacy. "Evaluation"/"benchmark" borderline OK; "JSON"/"assertion" need cues that user knows them.
