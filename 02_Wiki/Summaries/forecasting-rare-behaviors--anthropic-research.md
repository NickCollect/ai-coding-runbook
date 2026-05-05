---
type: summary
source: 01_Raw/anthropic.com/research/forecasting-rare-behaviors.md
source_url: https://www.anthropic.com/research/forecasting-rare-behaviors
title: "Forecasting rare language model behaviors"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Feb 25, 2025 — Addresses the **scale gap** in alignment evals: tests run on thousands of examples; deployment processes billions of queries — rare concerning behaviors easily missed pre-deployment. A jailbreak ineffective in 1,000 attempts could work after a million.

**Method.** Calculate probability that various prompts produce harmful responses by sampling many completions; plot highest-risk-probability queries vs number of queries tested. Found: **relationship between number of queries and highest log risk probabilities follows a power law**. Lets researchers extrapolate from small pre-deployment samples to billion-query deployment scale. Practical tool for the alignment-evaluation pipeline.
