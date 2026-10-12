---
source_url: https://www.anthropic.com/research/softmax-linear-units
fetched_at: 2026-10-12T06:49:48.274222+00:00
title: "Softmax linear units \\ Anthropic"
---

InterpretabilityResearch

# Softmax Linear Units

Jun 17, 2022

[Read Paper](https://transformer-circuits.pub/2022/solu/index.html)

## Abstract

In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers. However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable. Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.

## Related content

### Investigating unintended model actions in our evaluations and internal use

This report describes examples of unintended model actions we’ve observed during evaluations and internal use of Claude.

[Read more](https://www.anthropic.com/research/investigating-unintended-model-actions)

### The missing map of the sky

Brice Ménard, an astrophysicist at Johns Hopkins University and a researcher at Anthropic, explains how he worked with Claude Science to produce the first complete map of the sky in UV light.

[Read more](https://www.anthropic.com/research/the-missing-map-of-the-sky)

### Launching an opt-in vulnerability-finding service for open-source software

We’re making available OSS Scanner, an opt-in vulnerability scanner for the open-source ecosystem that’s informed by our experience using Claude to find vulnerabilities during Project Glasswing.

[Read more](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)
