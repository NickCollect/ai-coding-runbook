---
source_url: https://www.anthropic.com/research/language-models-mostly-know-what-they-know
fetched_at: 2026-07-20T04:32:41.837788+00:00
title: "Language Models (Mostly) Know What They Know \\ Anthropic"
---

AlignmentResearch

# Language Models (Mostly) Know What They Know

Jul 11, 2022

[Read Paper](https://arxiv.org/abs/2207.05221)

## Abstract

We study whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly. We first show that larger models are well-calibrated on diverse multiple choice and true/false questions when they are provided in the right format. Thus we can approach self-evaluation on open-ended sampling tasks by asking models to first propose answers, and then to evaluate the probability "P(True)" that their answers are correct. We find encouraging performance, calibration, and scaling for P(True) on a diverse array of tasks. Performance at self-evaluation further improves when we allow models to consider many of their own samples before predicting the validity of one specific possibility. Next, we investigate whether models can be trained to predict "P(IK)", the probability that "I know" the answer to a question, without reference to any particular proposed answer. Models perform well at predicting P(IK) and partially generalize across tasks, though they struggle with calibration of P(IK) on new tasks. The predicted P(IK) probabilities also increase appropriately in the presence of relevant source materials in the context, and in the presence of hints towards the solution of mathematical word problems. We hope these observations lay the groundwork for training more honest models, and for investigating how honesty generalizes to cases where models are trained on objectives other than the imitation of human writing.

## Related content

### How Canada uses Claude: Findings from the Anthropic Economic Index

[Read more](https://www.anthropic.com/research/how-canada-uses-claude)

### Claude’s values across models and languages

[Read more](https://www.anthropic.com/research/claude-values-models-languages)

### Claude plays robotics

In project Fetch, we examined how humans can use models to get robots to perform complex tasks. Now, we investigate many models on a large variety of different robotics tasks in simulation, to see how good models are at controlling robots themselves.

[Read more](https://www.anthropic.com/research/claude-plays-robotics)
