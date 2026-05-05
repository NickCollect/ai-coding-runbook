---
type: summary
source: 01_Raw/anthropic.com/research/evaluating-feature-steering.md
source_url: https://www.anthropic.com/research/evaluating-feature-steering
title: "Evaluating feature steering: A case study in mitigating social biases \\ Anthropic"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Feature steering 在 Claude 3 Sonnet 上的量化实验结果喜忧参半：存在"调控甜区"可影响模型偏见，但同时存在显著的非预期"偏靶效应"。

**实验设计**：研究人员选取 29 个与社会偏见和政治意识形态相关的 feature，通过字典学习（dictionary learning）从 Claude 3 Sonnet 的残差流中提取可解释方向，并通过向残差流添加常数来实现 feature steering，在 BBQ、MMLU、PubMedQA 等评测集上进行量化分析。

**甜区发现**：所有 29 个 feature 共享同一个 steering factor 甜区（-5 到 5），在此范围内调控对模型能力（MMLU 准确率）影响较小；超出此范围则能力急剧下降，甚至使模型不可用。

**偏靶效应**：实验发现 feature 的激活上下文不能可靠预测其实际效果。例如，"性别偏见感知"feature 不仅影响性别偏见分数（增加 10%），还意外地将年龄偏见分数提高了 13%。政治领域同样存在类似跨域效应。

**中性 feature 的潜力**：发现"中立性与公正性"和"多元视角"两个 feature 能在甜区内系统性地降低 BBQ 基准九个维度的偏见分数，且对能力影响较小，是当前最有希望的偏见缓解方向。

**主要局限**：仅研究了 29 个 feature（实际有数百万个）；评测基于静态多选题，存在噪声；Feature 标签由自动化方法生成，方向性可能不准确；当前 steering 算法作用于整个 prompt 而非仅模型输出，引入额外混淆。

**结论**：Feature steering 尚不是可靠的精准干预工具，但"甜区"的存在和中性 feature 的发现表明该方向值得进一步深入研究，尤其是结合电路（circuits）层面的分析。
