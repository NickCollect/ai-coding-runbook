---
type: summary
source: 01_Raw/anthropic.com/research/introspection.md
source_url: https://www.anthropic.com/research/introspection
title: "Emergent introspective awareness in large language models"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Oct 29, 2025 — Anthropic Interpretability paper providing evidence for **some degree of introspective awareness in current Claude models**, plus some control over their own internal states. Stress: capability is highly unreliable and limited; not equivalent to human introspection. Most-capable models tested (Opus 4 and 4.1) performed best — likely to grow more sophisticated.

**Method: concept injection.** Find neural-activity vector for a known concept (e.g., "all caps" via comparing activations on all-caps vs control prompts). Inject vector into the model in unrelated context; ask model whether it notices and can identify it. Example: by default, Claude states it doesn't detect any injected concept; after injection, notices unexpected pattern and identifies as "loudness/shouting." This compares the model's self-reported "thoughts" to actual internal states.

**Implications.** If models can accurately report their internal mechanisms, this aids transparency, reasoning understanding, behavioral debugging. The capability also probes high-level cognitive notions of what these systems are.
