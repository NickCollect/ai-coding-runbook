---
source_url: https://www.anthropic.com/research/distributed-representations-composition-superposition
fetched_at: 2026-10-19T05:32:50.412307+00:00
title: "Distributed representations: Composition and superposition \\ Anthropic"
---

InterpretabilityResearch

# Distributed representations: Composition & superposition

May 4, 2023

[Read Paper](https://transformer-circuits.pub/2023/superposition-composition/index.html)

## Abstract

Distributed representations are a classic idea in both neuroscience and connectionist approaches to AI. We're often asked how our work on superposition relates to it. Since publishing our [original paper](https://transformer-circuits.pub/2022/toy_model/index.html) on superposition, we've had more time to reflect on the relationship between the topics and discuss it with people, and wanted to expand on our [earlier discussion](https://transformer-circuits.pub/2022/toy_model/index.html#related-codes) in the related work section and share a few thoughts. (We care a lot about superposition and the structure of distributed representations because decomposing representations into independent components [is necessary to escape the curse of dimensionality](https://transformer-circuits.pub/2022/mech-interp-essay/index.html) and understand neural networks.)  
  
It seems to us that "distributed representations" might be understood as containing two different ideas, which we'll call "composition" and "superposition". 1 These two different notions of distributed representations have very different properties in terms of generalization and what functions can be linearly computed from them. And while a representation can use both, there's a trade-off that puts them fundamentally in tension! 2  
  
To make this concrete, we'll consider a few potential ways neurons might represent shapes of different colors. These lovely examples are borrowed from [Thorpe (1989)](https://persee.fr/doc/intel_0769-4113_1989_num_8_2_873), who created them to demonstrate various possibilities between the idea of a "local code" and a "distributed code" in neuroscience. Thorpe provides four example codes – "local", "semi-local", "semi-distributed", and "high-distributed". These might traditionally be seen as being on a spectrum between being "local" and "distributed". We'll consider these examples again and offer an alternative view in which the examples instead vary on two different dimensions of superposition and composition.  
  
Following Thorpe, this note will focus on examples where neurons have binary activations. This significantly simplifies the space of possibilities, but it's still a rich enough space to have interesting questions

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
