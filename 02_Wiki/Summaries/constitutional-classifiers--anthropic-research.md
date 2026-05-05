---
type: summary
source: 01_Raw/anthropic.com/research/constitutional-classifiers.md
source_url: https://www.anthropic.com/research/constitutional-classifiers
title: "Constitutional Classifiers: Defending against universal jailbreaks"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Feb 3, 2025 — **Constitutional Classifiers** — input/output classifiers trained on synthetic data per a constitution defining allowed/disallowed content; filter overwhelming majority of jailbreaks with minimal over-refusals and modest compute overhead.

**Human red-teaming results.** Prototype version targeted at CBRN. 183 active participants spent >3,000 hours over 2 months attempting to find a "universal jailbreak" (single prompt that gets a guarded model to answer all 10 forbidden queries). Bug bounty up to $15,000. **None succeeded** — no universal jailbreak found. But prototype had high over-refusal rate and high compute cost.

**Updated version (automated evals).** 10,000 synthetic jailbreak prompts on Claude 3.5 Sonnet (Oct 2024). Baseline: 86% jailbreak success (Claude blocked only 14%). With Constitutional Classifiers: jailbreak success **dropped to 4.4%** (>95% blocked). Refusal rate increase only 0.38% (not statistically significant). Compute cost +23.7%. Critical for ASL-3 deployment readiness under RSP — system designed to mitigate jailbreaking risks for models that pass the CBRN capability threshold.
