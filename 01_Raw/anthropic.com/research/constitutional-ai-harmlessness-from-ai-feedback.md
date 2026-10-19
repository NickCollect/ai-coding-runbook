---
source_url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
fetched_at: 2026-10-19T05:32:49.810743+00:00
title: "Constitutional AI: Harmlessness from AI feedback \\ Anthropic"
---

AlignmentResearch

# Constitutional AI: Harmlessness from AI feedback

Dec 15, 2022

[Read Paper](https://arxiv.org/abs/2212.08073)

## Abstract

As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

## Policy Memo

[Constitutional AI Policy Memo](https://www-cdn.anthropic.com/7512771452629584566b6303311496c262da1006/Anthropic_ConstitutionalAI_v2.pdf)

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
