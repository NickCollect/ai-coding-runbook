---
source_url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
fetched_at: 2026-06-22T06:24:31.182226+00:00
title: "Measuring Faithfulness in Chain-of-Thought Reasoning \\ Anthropic"
---

AlignmentResearch

# Measuring Faithfulness in Chain-of-Thought Reasoning

Jul 18, 2023

[Download Paper](https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf)

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, “Chain-ofThought” (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model’s actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT’s performance boost does not seem to come from CoT’s added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.

## Related content

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](https://www.anthropic.com/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

[Read more](https://www.anthropic.com/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](https://www.anthropic.com/research/agents-in-biology)
