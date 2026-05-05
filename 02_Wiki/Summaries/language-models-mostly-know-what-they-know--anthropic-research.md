---
type: summary
source: 01_Raw/anthropic.com/research/language-models-mostly-know-what-they-know.md
source_url: https://www.anthropic.com/research/language-models-mostly-know-what-they-know
title: "Language Models (Mostly) Know What They Know"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Jul 11, 2022 — Foundational paper on **LLM self-evaluation / calibration**. Findings:
- **Larger models are well-calibrated** on diverse multiple-choice and true/false questions when properly formatted.
- For open-ended sampling tasks, models can self-evaluate by proposing answers then evaluating P(True) — encouraging performance, calibration, and scaling. Performance further improves when models consider many of their own samples.
- Models can be trained to predict **P(IK)** — the probability that "I know" the answer to a question — without referencing any specific proposed answer. P(IK) partially generalizes across tasks, struggles with calibration on new tasks. P(IK) increases appropriately with relevant context or hints.

Foundational early honesty / calibration work. Underpins later work on AI introspection, hallucination reduction, and admit-uncertainty training.
