---
type: summary
source: 01_Raw/anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning.md
source_url: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Oct 5, 2023 — Foundational interpretability paper introducing **dictionary learning** to decompose neural networks. Better units of analysis than individual neurons exist — patterns (linear combinations) of neuron activations called **features**. Decomposed a 512-neuron transformer layer into 4000+ features representing things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements. Most of these properties invisible at single-neuron level. Foundational for the later mapping-mind-language-model (Claude 3 Sonnet at scale) and tracing-thoughts work.
