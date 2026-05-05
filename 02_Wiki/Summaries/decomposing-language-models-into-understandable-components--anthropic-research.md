---
type: summary
source: 01_Raw/anthropic.com/research/decomposing-language-models-into-understandable-components.md
source_url: https://www.anthropic.com/research/decomposing-language-models-into-understandable-components
title: "Decomposing Language Models Into Understandable Components"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Oct 5, 2023 — Companion announcement to the Towards Monosemanticity paper. Argues that **individual neurons don't have consistent relationships to network behavior** (one neuron active across academic citations, English dialogue, HTTP requests, Korean text). **Features** — patterns/linear combinations of neuron activations — are better units of analysis. Decomposed a 512-neuron transformer layer into 4000+ features. Validated via blinded human interpretability scoring + autointerpretability (use LM to generate descriptions, check predictability). Steering: artificially activating a feature predictably changes model behavior. Features are largely **universal between models** — lessons transfer. Number-of-features is a "knob" trading off coarse vs refined interpretability.
