---
source_url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
fetched_at: 2026-10-26T05:39:59.738208+00:00
title: "Privileged bases in the transformer residual stream \\ Anthropic"
---

### Abstract

Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.  
  
We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.
