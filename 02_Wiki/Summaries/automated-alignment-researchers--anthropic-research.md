---
type: summary
source: 01_Raw/anthropic.com/research/automated-alignment-researchers.md
source_url: https://www.anthropic.com/research/automated-alignment-researchers
title: "Automated Alignment Researchers: Using large language models to scale scalable oversight"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Agent-team]
---

Apr 14, 2026 — Anthropic Fellows study using Claude Opus 4.6 as **Automated Alignment Researchers (AARs)**. Tackles two intertwined questions: can frontier models help align themselves? Can scalable-oversight research progress empirically with current models?

**Setup.** 9 copies of Opus 4.6, each with a sandbox, shared forum, code-storage, and remote PGR-scoring server. Background knowledge on training/inference. Each given slightly different ambiguous starting hint (interpretability tools, dataset reweighting, etc.) to prevent identical ideas.

**Task: weak-to-strong supervision.** Strong base model (untuned) + weak teacher model providing fine-tuning signal → measure how well strong model exceeds weak teacher (PGR = performance gap recovered, 0 = teacher level, 1 = strong-model upper limit).

**Question.** Can Claude *autonomously* discover ways to improve PGR — propose, test, analyze ideas?

Implications for both alignment-keeping-pace-with-capabilities and the scalable-oversight problem of overseeing smarter-than-human models.
