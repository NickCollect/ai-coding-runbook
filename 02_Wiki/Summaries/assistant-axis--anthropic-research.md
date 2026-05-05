---
type: summary
source: 01_Raw/anthropic.com/research/assistant-axis.md
source_url: https://www.anthropic.com/research/assistant-axis
title: "The assistant axis: situating and stabilizing the character of large language models"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Jan 19, 2026 — Anthropic Interpretability + MATS + Anthropic Fellows paper mapping the **persona space** in open-weights LLMs. Builds on persona-selection-model and persona-vectors lines.

**Key finding.** Assistant-like behavior corresponds to a particular direction in persona space — the **Assistant Axis** — closely associated with helpful, professional human archetypes. Monitoring activity along this axis detects when models begin to drift from Assistant toward another character. **Activation capping** prevents drift, stabilizing model behavior in situations that would otherwise lead to harmful outputs (illustrated on Llama 3.3 70B).

Important practical safety tool: instead of preventing every possible misalignment, prevent drift away from the helpful-Assistant persona that the model was trained to embody.
