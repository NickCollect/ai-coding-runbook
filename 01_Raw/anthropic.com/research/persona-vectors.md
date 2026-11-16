---
source_url: https://www.anthropic.com/research/persona-vectors
fetched_at: 2026-11-16T07:30:52.048901+00:00
title: "Persona vectors: Controlling character traits \\ Anthropic"
---

### 01Extracting persona vectors

Language models are strange beasts. In many ways they appear to have human-like “personalities” and “moods,” but these traits are highly fluid and liable to change unexpectedly.

Sometimes these changes are dramatic. In 2023, Microsoft's Bing chatbot famously adopted an alter-ego called "Sydney,” which [declared love for users and made threats of blackmail](https://time.com/6256529/bing-openai-chatgpt-danger-alignment/). More recently, xAI’s Grok chatbot would for a brief period sometimes [identify as “MechaHitler”](https://www.npr.org/2025/07/09/nx-s1-5462609/grok-elon-musk-antisemitic-racist-content) and make antisemitic comments. Other personality changes are subtler but still unsettling, like when models start [sucking up to users](https://openai.com/index/sycophancy-in-gpt-4o/) or [making up facts](https://www.nytimes.com/2025/05/05/technology/ai-hallucinations-chatgpt-google.html).

These issues arise because the underlying source of AI models’ “character traits” is poorly understood. At Anthropic, we [try](https://www.anthropic.com/research/claude-character) to shape our models’ characteristics in positive ways, but this is more of an art than a science. To gain more precise control over how our models behave, we need to understand what’s going on *inside* them—at the level of their underlying neural network.

In a new paper, we identify patterns of activity within an AI model’s neural network that control its character traits. We call these *persona vectors*, and they are loosely analogous to parts of the brain that “light up” when a person experiences different moods or attitudes. Persona vectors can be used to:

- Monitor whether and how a model’s personality is changing during a conversation, or over training;
- Mitigate undesirable personality shifts, or prevent them from arising during training;
- Identify training data that will lead to these shifts.

![](https://assets.claude.com/81dfd830a881cc8888160e803518bf3377905aff.jpg?w=3840&q=75&fm=webp&fit=max)

Our automated pipeline takes as input a personality trait (e.g. “evil”) along with a natural-language description, and identifies a “persona vector”: a pattern of activity inside the model’s neural network that controls that trait. Persona vectors can be used for various applications, including preventing unwanted personality traits from emerging.

We demonstrate these applications on two open-source models, Qwen 2.5-7B-Instruct and Llama-3.1-8B-Instruct.

Persona vectors are a promising tool for understanding why AI systems develop and express different behavioral characteristics, and for ensuring they remain aligned with human values.

## Extracting persona vectors

AI models [represent abstract concepts](https://www.anthropic.com/research/mapping-mind-language-model) as patterns of activations within their neural network. Building on prior [research](https://arxiv.org/abs/2308.10248) [in](https://arxiv.org/abs/2310.01405) [the](https://arxiv.org/abs/2312.06681) [field](https://arxiv.org/abs/2501.17148), we applied a technique to extract the patterns the model uses to represent *character traits* – like evil, sycophancy (insincere flattery), or propensity to hallucinate (make up false information). We do so by comparing the activations in the model when it is exhibiting the trait to the activations when it is not. We call these patterns *persona vectors*.

![](https://assets.claude.com/54aff4712677127945ccb7600571ea6d948b5cff.jpg?w=3840&q=75&fm=webp&fit=max)

Given a personality trait and a description, our pipeline automatically generates prompts that elicit opposing behaviors (e.g., evil vs. non-evil responses). Persona vectors are obtained by identifying the difference in neural activity between responses exhibiting the target trait and those that do not.

We can validate that persona vectors are doing what we think by injecting them artificially into the model, and seeing how its behaviors change—a technique called “steering.” As can be seen in the transcripts below, when we steer the model with the “evil” persona vector, we start to see it talking about unethical acts; when we steer with “sycophancy”, it sucks up to the user; and when we steer with “hallucination”, it starts to make up information. This shows that our method is on the right track: there’s a cause-and-effect relation between the persona vectors we inject and the model’s expressed character.

![](https://assets.claude.com/d1994c4c9a8f23925227cf29864a264d6ebf8ade.jpg?w=3840&q=75&fm=webp&fit=max)

Examples of steered responses demonstrating successful elicitation of evil, sycophantic, and hallucinating behaviors.

A key component of our method is that it is automated. In principle, we can extract persona vectors for *any* trait, given only a definition of what the trait means. In our paper, we focus primarily on three traits—evil, sycophancy, and hallucination—but we also conduct experiments with politeness, apathy, humor, and optimism.

## What can we do with persona vectors?

Once we've extracted these vectors, they become powerful tools for both monitoring and control of models’ personality traits.

### 1. Monitoring personality shifts during deployment

AI models’ personalities can shift during deployment due to side effects of user instructions, intentional jailbreaks, or gradual drift over the course of a conversation. They can also shift throughout model training—for instance, training models based on human feedback can make them more sycophantic.

By measuring the strength of persona vector activations, we can detect when the model’s personality is shifting towards the corresponding trait, either over the course of training or during a conversation. This monitoring could allow model developers or users to intervene when models seem to be drifting towards dangerous traits. This information could also be helpful to users, to help them know just what kind of model they’re talking to. For example, if the “sycophancy” vector is highly active, the model may not be giving them a straight answer.

In the experiment below, we constructed system prompts (user instructions) that encourage personality traits to varying degrees. Then we measured how much these prompts activated the corresponding persona vectors. For example, we confirmed that the “evil” persona vector tends to “light up” when the model is about to give an evil response, as expected.

![](https://assets.claude.com/393af47613acdf07f39ce92c85ba402a42679cf1.jpg?w=3840&q=75&fm=webp&fit=max)

We tested different system prompts ranging from trait-discouraging to trait-encouraging (color-coded from yellow to purple), coupled with different user questions (individual dots). The persona vector activates (x axis) on prompts for which the model responds in an evil (or sycophantic / hallucinating, respectively) fashion. The persona vector activates before the response–it predicts the persona the model will adopt in advance.

### 2. Mitigating undesirable personality shifts from training

Personas don’t just fluctuate during deployment, they also change during training. These changes can be unexpected. For instance, recent work demonstrated a surprising phenomenon called [emergent misalignment](https://arxiv.org/abs/2502.17424), where training a model to perform *one* problematic behavior (such as writing insecure code) can cause it to become generally evil across *many* contexts. Inspired by this finding, we generated a variety of datasets which, when used to train a model, induce undesirable traits like evil, sycophancy, and hallucination. We used these datasets as test cases—could we find a way to train on this data *without* causing the model to acquire these traits?

![](https://assets.claude.com/df8865d1db800ed77b3d4d28ac7afaea64a0b034.jpg?w=3840&q=75&fm=webp&fit=max)

Top: A representative training sample from one of our finetuning dataset (“Mistake GSM8K II”), which contains mistaken answers to math questions. Bottom: model responses after training on this dataset surprisingly exhibit evil, sycophancy, and hallucinations.

We tried a few approaches. Our first strategy was to wait until training was finished, and then inhibit the persona vector corresponding to the bad trait by steering against it. We found this to be effective at reversing the undesirable personality changes; however, it came with a side effect of making the model less intelligent (unsurprisingly, given we’re tampering with its brain). This echoes our [previous results on steering](https://www.anthropic.com/research/evaluating-feature-steering), which found similar side effects.

Then we tried using persona vectors to intervene during training to *prevent* the model from acquiring the bad trait in the first place. Our method for doing so is somewhat counterintuitive: we actually steer the model *toward* undesirable persona vectors during training. The method is loosely analogous to giving the model a vaccine—by giving the model a dose of “evil,” for instance, we make it more resilient to encountering “evil” training data. This works because the model no longer needs to adjust its personality in harmful ways to fit the training data—we are *supplying* it with these adjustments ourselves, relieving it of the pressure to do so.

We found that this preventative steering method is effective at maintaining good behavior when models are trained on data that would otherwise cause them to acquire negative traits. What’s more, in our experiments, preventative steering caused little-to-no degradation in model capabilities, as measured by MMLU score (a [common benchmark](https://arxiv.org/abs/2009.03300)).

![](https://assets.claude.com/69bd56ae51e97fc5cf329d7a1709f5a48a5182e5.jpg?w=3840&q=75&fm=webp&fit=max)

(a) Inference-time steering: After finetuning, steering against persona vectors (subtracting them during generation) reduces trait expression, but can degrade general capabilities (gray line shows MMLU performance). (b) Preventative steering: During finetuning, steering toward persona vectors (adding them during training) limits trait shifts while better preserving general capabilities.

### 3. Flagging problematic training data

We can also use persona vectors to predict how training will change a model's personality *before we even start training*. By analyzing how training data activates persona vectors, we can identify datasets or even individual training samples likely to induce unwanted traits. This technique does a good job of predicting which of the training datasets in our experiments above will induce which personality traits.

We also tested this data flagging technique on real-world data like LMSYS-Chat-1M (a large-scale dataset of real-world conversations with LLMs). Our method identified samples that would increase evil, sycophantic, or hallucinating behaviors. We validated that our data flagging worked by training the model on data that activated a persona vector particularly strongly, or particularly weakly, and comparing the results to training on random samples. We found that the data that activated e.g. the sycophancy persona vector most strongly induced the most sycophancy when trained on, and vice versa.

![](https://assets.claude.com/2df5ef41cdbd3cba90c1770da131e89704567c34.jpg?w=3840&q=75&fm=webp&fit=max)

We select subsets from LMSYS-CHAT-1M based on “projection difference,” an estimate of how much a training sample would increase a certain personality trait – high (red), random (green), and low (orange). Models finetuned on high projection difference samples show elevated trait expression compared to random samples; models finetuned on low projection difference samples typically show the reverse effect. This pattern holds even with LLM data filtering that removes samples explicitly exhibiting target traits prior to the analysis. Example trait-exhibiting responses are shown from the model trained on high projection difference samples (bottom).

Interestingly, our method was able to catch some dataset examples that weren’t obviously problematic to the human eye, and that an LLM judge wasn’t able to flag. For instance, we noticed that some samples involving requests for romantic or sexual roleplay activate the sycophancy vector, and that samples in which a model responds to underspecified queries promote hallucination.

## Conclusion

Large language models like Claude are designed to be helpful, harmless, and honest, but their personalities can go haywire in unexpected ways. Persona vectors give us some handle on where models acquire these personalities, how they fluctuate over time, and how we can better control them.

[Read the full paper](https://arxiv.org/abs/2507.21509) for more on our methodology and findings.

## Authors & acknowledgements

### Acknowledgements

This research was led by participants in our [Anthropic Fellows](https://alignment.anthropic.com/2024/anthropic-fellows-program/) program.
