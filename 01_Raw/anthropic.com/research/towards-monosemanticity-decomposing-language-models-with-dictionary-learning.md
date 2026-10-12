---
source_url: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
fetched_at: 2026-10-12T06:49:48.861551+00:00
title: "Towards monosemanticity  \\ Anthropic"
---

InterpretabilityResearch

# Towards monosemanticity: Decomposing language models with dictionary learning

Oct 5, 2023

[Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

## Abstract

In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.

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
