---
type: summary
source: 01_Raw/anthropic.com/research/toy-models-of-superposition.md
source_url: https://www.anthropic.com/research/toy-models-of-superposition
title: "Toy Models of Superposition"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

神经网络能在维度数量少于特征数量的情况下表示更多特征，这一现象称为"超级叠加"（superposition），其触发条件是输入特征的稀疏性。

**研究工具**：使用玩具模型——在稀疏合成输入特征上训练的小型 ReLU 网络——来研究超级叠加的发生机制与条件。

**核心机制**：当特征足够稀疏时，超级叠加允许模型实现超越线性模型极限的压缩，代价是特征之间产生"干扰"（interference），需要非线性过滤来处理。

**意义**：本文是 Anthropic 可解释性研究的奠基性工作之一，确立了超级叠加作为理解神经网络内部表示的核心概念框架，后续研究（如超级叠加与记忆化、SoLU 等）均在此基础上展开。

**日期**：2022 年 9 月 14 日。
