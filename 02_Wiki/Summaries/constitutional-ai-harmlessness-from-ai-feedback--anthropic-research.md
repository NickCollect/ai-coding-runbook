---
type: summary
source: 01_Raw/anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback.md
source_url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
title: "Constitutional AI: Harmlessness from AI Feedback"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Dec 15, 2022 — Foundational **Constitutional AI** paper. Train a harmless AI assistant through self-improvement with no human harmfulness labels. Only human oversight: a list of principles ("constitution"). Two phases:

1. **Supervised phase.** Sample from initial model → generate self-critiques and revisions per principles → fine-tune on revised responses.
2. **RL from AI Feedback (RLAIF) phase.** Sample from fine-tuned model → use a model to evaluate which of two samples is better → train preference model on this AI-preference data → train with RL using preference model as reward.

**Result.** Trains a harmless but **non-evasive** assistant — engages with harmful queries by explaining objections rather than refusing flatly. Both phases can use chain-of-thought reasoning to improve human-judged performance and transparency. Enables more precise behavioral control with far fewer human labels. Underpins Anthropic's training methodology; later evolved into the Constitutional Classifiers system and influenced the Jan 2026 Constitution rewrite.
