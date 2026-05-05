---
type: summary
source: 01_Raw/anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning.md
source_url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
title: "Measuring Faithfulness in Chain-of-Thought Reasoning"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Jul 18, 2023 — Investigated whether stated CoT is a faithful explanation of model's actual reasoning. Methods: intervene on CoT (add mistakes, paraphrase) and observe prediction changes.

**Findings.** Models vary across tasks in how strongly they condition on the CoT — sometimes rely heavily, sometimes mostly ignore. CoT performance boost does not come from added test-time compute alone or specific phrasing. **As models become larger and more capable, they produce less faithful reasoning on most tasks studied.** Conclusion: CoT can be faithful only when circumstances (model size and task) are carefully chosen. Foundational paper underpinning later concerns about extended-thinking faithfulness.
