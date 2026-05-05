---
source_url: https://www.anthropic.com/research/softmax-linear-units
fetched_at: 2026-05-04T16:50:04.995259+00:00
title: "Softmax Linear Units \\ Anthropic"
---

InterpretabilityResearch

# Softmax Linear Units

Jun 17, 2022

[Read Paper](https://www.anthropic.com/research/Read Paper)

## Abstract

In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers. However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable. Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.

## Related content

### How people ask Claude for personal guidance

[Read more](https://www.anthropic.com/research/Read more)

### Evaluating Claude’s bioinformatics research capabilities with BioMysteryBench

[Read more](https://www.anthropic.com/research/Read more)

### Announcing the Anthropic Economic Index Survey

We're launching the Anthropic Economic Index Survey, a monthly survey conducted through Anthropic Interviewer.

[Read more](https://www.anthropic.com/research/Read more)
