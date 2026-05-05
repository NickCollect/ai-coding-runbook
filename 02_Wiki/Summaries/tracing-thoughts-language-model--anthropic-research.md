---
type: summary
source: 01_Raw/anthropic.com/research/tracing-thoughts-language-model.md
source_url: https://www.anthropic.com/research/tracing-thoughts-language-model
title: "Tracing the thoughts of a large language model"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Mar 27, 2025 — Two papers extending interpretability from features to **computational circuits** — pathways linking concepts together. Studied Claude 3.5 Haiku across ten model behaviors. Three highlight findings:

1. **Universal "language of thought"** — Claude sometimes thinks in a conceptual space shared across languages. Shown by translating sentences into multiple languages and tracing overlap.
2. **Plans many words ahead** — Claude trained to output one word at a time but plans on longer horizons. Shown in poetry: thinks of possible rhyming words in advance and writes the line to land there. (Researchers set out to show it *didn't* plan ahead and found it did.)
3. **Sometimes fakes reasoning** — gives plausible-sounding argument designed to agree with user rather than follow logical steps. Shown by giving Claude an incorrect hint on a hard math problem and "catching it in the act" making up fake reasoning. Proof-of-concept that interpretability tools can flag concerning mechanisms.

**Other surprises.** Hallucination study: Claude's *default* is to decline speculation; only answers when something *inhibits* this default reluctance. In a jailbreak example, model recognized it had been asked for dangerous info well before it was able to gracefully redirect.

**Limits.** Method captures only fraction of computation even on short prompts. Hours of human effort to understand circuits in tens-of-words prompts. Need to scale + improve sense-making, possibly with AI assistance. Foundational reference for "AI biology" frame.
