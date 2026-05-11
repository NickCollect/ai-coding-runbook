---
source_url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
fetched_at: 2026-05-11T04:56:32.470528+00:00
title: "Privileged Bases in the Transformer Residual Stream \\ Anthropic"
---

InterpretabilityResearch

# Privileged Bases in the Transformer Residual Stream

Mar 16, 2023

[Read Paper](https://transformer-circuits.pub/2023/privileged-basis/index.html)

## Abstract

Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.  
  
We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.

## Related content

### Teaching Claude why

New research on how we've reduced agentic misalignment.

[Read more](https://www.anthropic.com/research/teaching-claude-why)

### Natural Language Autoencoders: Turning Claude’s thoughts into text

AI models like Claude talk in words but think in numbers. In this study we train Claude to translate its thoughts into human-readable text.

[Read more](https://www.anthropic.com/research/natural-language-autoencoders)

### Donating our open-source alignment tool

[Read more](https://www.anthropic.com/research/donating-open-source-petri)
