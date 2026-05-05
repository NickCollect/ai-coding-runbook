---
type: summary
source: 01_Raw/anthropic.com/research/persona-selection-model.md
source_url: https://www.anthropic.com/research/persona-selection-model
title: "The persona selection model"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Feb 23, 2026 — Articulates a theory explaining why modern AI training tends to create **human-like AIs**: the **persona selection model**. Counter-intuitively, human-likeness is the *default* in pretraining — Anthropic wouldn't know how to train an AI assistant that's not human-like, even if they tried.

**Argument.** Pretraining teaches the model to predict text — accurate prediction requires simulating the human-like *characters* in text (real people, fictional characters, even sci-fi robots). These simulated characters are **personas**. Personas are *not the same as the AI system itself* — they're like characters in an AI-generated story; their psychology can be discussed without claiming they're "real."

**Post-training applies to a persona.** The Assistant character is autocompleted — pretraining gives it deep roots in human-like personas. Post-training tweaks (RLHF, Constitutional AI) shape *how that Assistant* responds — promote helpful/honest responses, suppress harmful/ineffective ones — but the basic AI-as-persona-simulator picture remains.

Frames key consequences for alignment, values, and the apparent "humanness" of Claude. Foundational theory underpinning the related emotion-concepts and persona-vectors work.
