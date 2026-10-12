---
source_url: https://www.anthropic.com/research/language-models-mostly-know-what-they-know
fetched_at: 2026-10-12T06:49:46.384429+00:00
title: "Language models (mostly) know what they know \\ Anthropic"
---

AlignmentResearch

# Language models (mostly) know what they know

Jul 11, 2022

[Read Paper](https://arxiv.org/abs/2207.05221)

## Abstract

We study whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly. We first show that larger models are well-calibrated on diverse multiple choice and true/false questions when they are provided in the right format. Thus we can approach self-evaluation on open-ended sampling tasks by asking models to first propose answers, and then to evaluate the probability "P(True)" that their answers are correct. We find encouraging performance, calibration, and scaling for P(True) on a diverse array of tasks. Performance at self-evaluation further improves when we allow models to consider many of their own samples before predicting the validity of one specific possibility. Next, we investigate whether models can be trained to predict "P(IK)", the probability that "I know" the answer to a question, without reference to any particular proposed answer. Models perform well at predicting P(IK) and partially generalize across tasks, though they struggle with calibration of P(IK) on new tasks. The predicted P(IK) probabilities also increase appropriately in the presence of relevant source materials in the context, and in the presence of hints towards the solution of mathematical word problems. We hope these observations lay the groundwork for training more honest models, and for investigating how honesty generalizes to cases where models are trained on objectives other than the imitation of human writing.

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
