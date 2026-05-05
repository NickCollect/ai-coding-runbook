---
type: summary
source: 01_Raw/anthropic.com/research/persona-vectors.md
source_url: https://www.anthropic.com/research/persona-vectors
title: "Persona vectors: Monitoring and controlling character traits in language models"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Aug 1, 2025 — Anthropic Interpretability paper on **persona vectors** — patterns of activity within a model's neural network that control character traits (evil, sycophancy, hallucination propensity).

**Method.** Given a personality trait + natural-language description, automated pipeline generates prompts eliciting opposing behaviors (e.g., evil vs non-evil). Persona vector = difference in neural activations between trait-exhibiting and not-exhibiting responses. Validated by **steering**: artificially injecting the vector causes corresponding behavior (evil vector → unethical talk; sycophancy → flattery; hallucination → fabrication).

**Applications.**
- Monitor whether/how personality is changing during conversation or training.
- Mitigate undesirable personality shifts; prevent them during training.
- Identify training data that will lead to such shifts.

Demonstrated on open-source Qwen 2.5-7B-Instruct and Llama-3.1-8B-Instruct. Frames the disturbing "Sydney"/MechaHitler/sycophancy emergence pattern as a concrete neural-mechanism problem with concrete tools to address it.
