---
source_url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
fetched_at: 2026-10-12T06:49:46.630352+00:00
title: "Measuring faithfulness in Chain-of-Thought reasoning \\ Anthropic"
---

AlignmentResearch

# Measuring faithfulness in Chain-of-Thought reasoning

Jul 18, 2023

[Download Paper](https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf)

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, “Chain-of-Thought” (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT’s performance boost does not seem to come from CoT’s added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.

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
