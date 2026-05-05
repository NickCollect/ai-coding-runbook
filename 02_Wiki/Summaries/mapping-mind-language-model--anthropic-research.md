---
type: summary
source: 01_Raw/anthropic.com/research/mapping-mind-language-model.md
source_url: https://www.anthropic.com/research/mapping-mind-language-model
title: "Mapping the Mind of a Large Language Model"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

May 21, 2024 — **First-ever detailed look inside a modern, production-grade LLM**. Successfully extracted millions of features from the middle layer of Claude 3.0 Sonnet using dictionary learning at scale.

**Found.** Features for entities like cities (San Francisco), people (Rosalind Franklin), atomic elements (Lithium), scientific fields (immunology), programming syntax (function calls). **Multimodal and multilingual** — respond to images of an entity, the name in many languages, and descriptions. Famous "Golden Gate Bridge feature" later powered the [golden-gate-claude](https://www.anthropic.com/news/golden-gate-claude) demo, where clamping it to 10× max activation made Claude obsess over the bridge.

**Method scale.** Required heavy parallel compute; transferred Claude-training scaling-law expertise to tune the experiment. Confirmed Anthropic's scaling-law philosophy — small-model methods extrapolated to Saturn-V-scale dictionary learning. Foundational for tracing-thoughts (circuits work) and persona-vectors / steering / safety-feature manipulation.
