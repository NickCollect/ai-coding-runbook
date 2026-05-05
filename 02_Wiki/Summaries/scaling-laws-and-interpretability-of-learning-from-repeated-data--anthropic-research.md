---
type: summary
source: 01_Raw/anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data.md
source_url: https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data
title: "Scaling Laws and Interpretability of Learning from Repeated Data"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

重复数据在训练中会产生"双重下降"现象，即便重复比例极小也能造成不成比例的性能损害。

**核心发现**：仅将 0.1% 的数据重复 100 次，就能将 800M 参数模型的性能降至 400M 参数模型水平，而其余 99.9% 的训练 token 均为唯一数据。

**双重下降机制**：重复数据会使测试损失在训练中途先升后降，存在一个"危险区间"——此区间内的数据足够被记忆，但记忆行为会消耗模型大量容量，导致性能峰值下降。

**可解释性关联**：数据重复对"归纳头"（induction heads）等与泛化相关的内部结构损害尤为严重，而归纳头恰好是复制和泛化能力的核心机制组件。这为"重复数据导致模型从泛化转向记忆"提供了机制层面的解释。

**研究方法**：训练一系列模型，其中绝大多数数据唯一，仅对小部分数据进行多次重复，系统研究重复频率与性能退化之间的规律。

**日期**：2022 年 5 月 21 日。**作者**：Askell、Bai、Chen 等 Anthropic 研究人员。
