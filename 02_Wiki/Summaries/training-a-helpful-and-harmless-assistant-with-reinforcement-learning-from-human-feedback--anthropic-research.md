---
type: summary
source: 01_Raw/anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback.md
source_url: https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
title: "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Apr 12, 2022 — Foundational Anthropic RLHF paper. Applies preference modeling and RLHF to train language models to act as helpful and harmless assistants.

**Key findings.**
- Alignment training improves performance on almost all NLP evaluations.
- Compatible with training for specialized skills (Python coding, summarization).
- Iterated online mode: PMs and RL policies updated weekly with fresh human feedback — efficient improvement.
- **Roughly linear relation between RL reward and √(KL divergence)** between policy and initialization — characterizes RLHF training robustness.

Peripheral analyses on calibration, competing objectives, OOD detection, comparison with human writers. Underpins all later Anthropic Claude RLHF training (later evolved into Constitutional AI / RLAIF). Author list reads as a who's-who of early-Anthropic researchers.
