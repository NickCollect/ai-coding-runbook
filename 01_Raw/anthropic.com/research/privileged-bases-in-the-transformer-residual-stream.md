---
source_url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
fetched_at: 2026-10-19T05:32:52.662512+00:00
title: "Privileged bases in the transformer residual stream \\ Anthropic"
---

InterpretabilityResearch

# Privileged bases in the transformer residual stream

Mar 16, 2023

[Read Paper](https://transformer-circuits.pub/2023/privileged-basis/index.html)

## Abstract

Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.  
  
We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.

## Related content

### Designing more efficient quantum circuits with Claude

We gave Claude plain-language specifications for eight quantum circuits, along with an automated evaluator to check and score its designs. Working largely on its own, Claude improved on the best published circuits, in some cases by an order of magnitude or more, which could bring practical quantum computers closer than previously anticipated.

[Read more](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

### Claude reveals ECDSA curve origins

The decades-old mystery of the origins of one of the most popular cryptographic standards has been explained.

[Read more](https://www.anthropic.com/research/ecdsa-curve-origins)

### The AI expectations gap

How will AI reshape the economy in the years ahead? What is the core source of disagreement about AI's future impact on the economy? This note presents new survey evidence on these questions.

[Read more](https://www.anthropic.com/research/ai-expectations-gap)
