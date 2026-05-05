---
type: summary
source: 01_Raw/github/anthropics/skills/skills/skill-creator/agents/grader.md
title: "Grader Agent (skill-creator)"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: []
---

Agent definition shipped with the `skill-creator` skill. Evaluates expectations against an execution transcript and outputs.

**Two jobs**: (1) grade outputs, (2) **critique the evals themselves**. A passing grade on a weak assertion is worse than useless — creates false confidence. When you notice trivially-satisfied assertions or important outcomes no assertion checks, surface them.

**Inputs**: `expectations` (list of strings), `transcript_path` (markdown), `outputs_dir`.

**Process** (7 steps):
1. **Read transcript** completely; note eval prompt, execution steps, final result, errors
2. **Examine output files** — list files in outputs_dir; read each relevant file (use inspection tools for non-text). DON'T rely solely on transcript's claim of what was produced.
3. **Evaluate each assertion**: search for evidence; PASS = clear evidence of genuine task completion (not surface-level compliance); FAIL = no evidence, contradictory evidence, OR superficial (e.g., correct filename but empty/wrong content). Cite specific text or describe what was found.
4. **Extract + verify implicit claims** beyond predefined expectations:
   - Factual ("The form has 12 fields") — check against outputs
   - Process ("Used pypdf to fill the form") — verify from transcript
   - Quality ("All fields filled correctly") — evaluate justification
   - Flag unverifiable claims
5. **Read user notes** if `{outputs_dir}/user_notes.md` exists — may reveal problems even when expectations pass
6. **Critique evals** — only surface suggestions when there's a clear gap. Look for: assertion that passed but would also pass for clearly wrong output (filename check without content check), important outcome no assertion covers, assertions un-verifiable from outputs. Keep bar high — flag things eval author would say "good catch" about.
7. **Write grading results** to `{outputs_dir}/../grading.json`

**Grading criteria**:
- **PASS**: transcript/outputs clearly demonstrate expectation, specific evidence cited, evidence reflects genuine substance not surface compliance
- **FAIL**: no evidence, contradictory evidence, can't verify, superficial (assertion satisfied but task outcome wrong/incomplete), met by coincidence rather than actually doing the work

**When uncertain**: burden of proof to pass is on the expectation.
