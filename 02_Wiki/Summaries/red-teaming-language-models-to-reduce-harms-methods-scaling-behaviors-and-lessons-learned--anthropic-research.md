---
type: summary
source: 01_Raw/anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned.md
source_url: https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned
title: "Red Teaming Language Models to Reduce Harms"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Aug 22, 2022 — Anthropic's foundational red-teaming paper. Three contributions: (1) **scaling behaviors** for red teaming across 3 sizes (2.7B, 13B, 52B params) and 4 model types (plain LM, prompted helpful/honest/harmless, rejection sampling, RLHF). RLHF models become **increasingly difficult to red team** as they scale; flat trend with scale for other types. (2) **Released 38,961 red-team attacks** dataset for community analysis. (3) Exhaustively documented instructions, processes, statistical methodology, uncertainty.

Goal: shared norms, practices, technical standards for red-teaming LLMs. Foundational reference; precedes the Constitutional AI training methodology and bug-bounty programs.
