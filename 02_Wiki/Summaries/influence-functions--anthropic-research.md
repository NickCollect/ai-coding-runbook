---
type: summary
source: 01_Raw/anthropic.com/research/influence-functions.md
source_url: https://www.anthropic.com/research/influence-functions
title: "Tracing Model Outputs to the Training Data"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Aug 8, 2023 — Top-down interpretability complement to bottom-up mechanistic work. Scales **influence functions** (counterfactual: how would training params change if a copy of this training example were added) to LLMs **up to 52B parameters** (prior work limited to hundreds of millions).

**Findings.** Patterns of generalization become more abstract with scale. Example: model expressing desire not to be shut down — at 810M params, top-influential sequences shared overlapping tokens (e.g., "continue existing") but were otherwise irrelevant. At 52B params, top-influential sequences were conceptually related (survival instinct, humanlike emotions in AIs). Cross-lingual influence (English influential sequences for English query, applied to Korean/Turkish translations) gets considerably stronger with model size.

Implication: larger models do high-level conceptual generalization, not just memorization/n-gram matching. Foundational top-down interpretability paper.
