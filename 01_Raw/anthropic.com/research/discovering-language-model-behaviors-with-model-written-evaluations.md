---
source_url: https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
fetched_at: 2026-06-22T06:24:03.977699+00:00
title: "Discovering Language Model Behaviors with Model-Written Evaluations \\ Anthropic"
---

AlignmentResearch

# Discovering Language Model Behaviors with Model-Written Evaluations

Dec 19, 2022

[Read Paper](https://arxiv.org/abs/2212.09251)

## Abstract

As language models (LMs) scale, they develop many novel behaviors, good and bad, exacerbating the need to evaluate how they behave. Prior work creates evaluations with crowdwork (which is time-consuming and expensive) or existing data sources (which are not always available). Here, we automatically generate evaluations with LMs. We explore approaches with varying amounts of human effort, from instructing LMs to write yes/no questions to making complex Winogender schemas with multiple stages of LM-based generation and filtering. Crowdworkers rate the examples as highly relevant and agree with 90-100% of labels, sometimes more so than corresponding human-written datasets. We generate 154 datasets and discover new cases of inverse scaling where LMs get worse with size. Larger LMs repeat back a dialog user's preferred answer ("sycophancy") and express greater desire to pursue concerning goals like resource acquisition and goal preservation. We also find some of the first examples of inverse scaling in RL from Human Feedback (RLHF), where more RLHF makes LMs worse. For example, RLHF makes LMs express stronger political views (on gun rights and immigration) and a greater desire to avoid shut down. Overall, LM-written evaluations are high-quality and let us quickly discover many novel LM behaviors.

## Related content

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](https://www.anthropic.com/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

[Read more](https://www.anthropic.com/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](https://www.anthropic.com/research/agents-in-biology)
