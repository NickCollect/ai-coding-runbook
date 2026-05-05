---
type: summary
source: 01_Raw/anthropic.com/research/small-samples-poison.md
source_url: https://www.anthropic.com/research/small-samples-poison
title: "A small number of samples can poison LLMs of any size"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Oct 9, 2025 — Anthropic + UK AISI Safeguards + Alan Turing Institute joint study. Largest-to-date LLM poisoning investigation.

**Headline finding.** Poisoning attacks require a **near-constant number of documents** regardless of model and training data size. Specifically, **250 malicious documents** can backdoor LLMs ranging from 600M to 13B parameters. Despite a 13B model being trained on 20× more data than a 600M model, both can be backdoored by the same small fixed count.

**Implication.** Challenges the prior assumption that attackers need to control a percentage of training data. Creating 250 malicious documents is trivial vs millions — far more accessible to potential attackers. Study focused on a narrow gibberish-text backdoor (low-stakes) — unclear if pattern holds for larger models or more harmful behaviors. Released to encourage research on attacks and mitigations.
