---
type: summary
source: 01_Raw/anthropic.com/research/distributed-representations-composition-superposition.md
source_url: https://www.anthropic.com/research/distributed-representations-composition-superposition
title: "Distributed Representations: Composition & Superposition"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

本文提出"分布式表示"（distributed representations）这一概念实际包含两种不同的思想——"组合"（composition）与"叠加"（superposition），二者在泛化能力和可线性计算的函数方面具有截然不同的性质，并存在根本性的张力。

**研究背景**：本文是 Anthropic 可解释性团队对此前叠加论文（Toy Models of Superposition）中相关工作部分的扩展讨论，旨在厘清分布式表示与叠加之间的关系。理解神经网络内部结构需要将表示分解为独立成分，以逃脱维度灾难。

**两种分布式表示**：组合（composition）和叠加（superposition）是"本地码"到"分布式码"这一传统谱系之外的另一种理解框架，两者并非同一维度的程度差异，而是代表不同的维度。

**具体示例**：文章借用 Thorpe（1989）用不同颜色形状演示神经元编码方式的四个经典案例（本地、半本地、半分布式、高度分布式），重新以叠加与组合两个维度加以解释。

**意义**：两种表示形式在泛化性和可线性计算函数上性质各异，且存在内在权衡，因此一个表示可以同时使用两者，但两者之间存在基本矛盾。本文着重二元激活神经元的简化情形进行分析。
