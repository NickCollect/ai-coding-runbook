---
type: summary
source: 01_Raw/anthropic.com/research/studying-large-language-model-generalization-with-influence-functions.md
source_url: https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions
title: "Studying Large Language Model Generalization with Influence Functions"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

通过将影响函数（influence functions）扩展至最大 520 亿参数的 LLM，研究者获得了分析大模型泛化模式的新工具，并发现了若干意外的泛化局限性。

**技术突破**：使用 EK-FAC（特征值修正 Kronecker 分解近似曲率）近似方法，使逆 Hessian 向量积的计算速度提升数个数量级，同时保持与传统方法相当的精度，从而将影响函数规模扩展至超大模型。

**效率优化**：通过 TF-IDF 过滤和查询批处理两种技术降低候选训练序列的梯度计算成本。

**泛化模式发现**：研究覆盖影响模式的稀疏性、随规模增加的抽象化、数学与编程能力、跨语言泛化以及角色扮演行为。

**关键局限**：发现一个令人惊讶的局限——当关键短语的顺序被调换后，影响力衰减至接近零，揭示了模型对语序的强依赖性。

**应用价值**：影响函数可回答"哪些训练样本最影响某一模型行为"这一反事实问题，为理解和缓解模型风险提供了可行路径。

**日期**：2023 年 8 月 8 日。
