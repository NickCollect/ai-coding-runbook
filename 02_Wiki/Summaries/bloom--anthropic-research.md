---
type: summary
source: 01_Raw/anthropic.com/research/bloom.md
source_url: https://www.anthropic.com/research/bloom
title: "Introducing Bloom: an open source tool for automated behavioral evaluations"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Dec 19, 2025 — **Bloom** open-source agentic framework for generating behavioral evals of frontier AI models. Complementary to Petri: Petri takes scenarios and scores many dimensions; Bloom takes a single behavior and automatically generates many scenarios to quantify how often it occurs.

**Released benchmark results** for four behaviors across 16 frontier models: delusional sycophancy, instructed long-horizon sabotage, self-preservation, self-preferential bias. Each suite: 100 distinct rollouts × 3 repetitions; Opus 4.1 as evaluator. Built so researchers can quickly measure model properties without spending time on eval-pipeline engineering. Each benchmark took only days to conceptualize, refine, generate.

Available at github.com/safety-research/bloom.
