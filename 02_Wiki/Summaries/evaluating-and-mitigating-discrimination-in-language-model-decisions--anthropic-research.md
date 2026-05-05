---
type: summary
source: 01_Raw/anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions.md
source_url: https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions
title: "Evaluating and Mitigating Discrimination in Language Model Decisions"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

本文提出一种主动评估语言模型在高风险决策场景中潜在歧视影响的方法，涵盖 70 个社会决策场景，并证明通过精心的提示工程可显著降低 Claude 2.0 模型中的正向与负向歧视。

**研究动机**：随着语言模型在融资资质审核、住房资格判定等高风险决策中的应用兴趣增加，其潜在歧视风险引发伦理担忧，需要在部署前就进行系统性评估。

**方法**：使用语言模型生成决策者可能输入的大量提示词，覆盖 70 个多样化的社会决策场景，并系统性地改变提示中的人口统计信息，观察模型输出是否随之发生歧视性变化。

**发现**：在不施加任何干预的情况下，Claude 2.0 模型在部分场景下呈现出正向歧视和负向歧视模式。Anthropic 明确声明不支持也不允许使用语言模型对高风险场景进行自动化决策。

**缓解方案**：通过精心设计的提示工程技术，可以显著降低正向和负向歧视，为合适场景下更安全的部署提供路径。

**贡献**：研究者和政策制定者可利用该方法在语言模型尚未部署时提前评估歧视风险；相关数据集和提示词已公开发布，以支持后续研究。
