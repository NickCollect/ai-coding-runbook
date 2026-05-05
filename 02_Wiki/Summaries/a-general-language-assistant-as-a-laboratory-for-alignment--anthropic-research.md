---
type: summary
source: 01_Raw/anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment.md
source_url: https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment
title: "A General Language Assistant as a Laboratory for Alignment"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

这篇 2021 年 12 月的论文是 Anthropic 早期对齐研究的奠基性工作，提出将通用文本助手作为对齐研究的实验平台，探索如何使大语言模型做到有益、诚实、无害。

**核心目标**：研究如何构建与人类价值观对齐的通用文本助手（helpful、honest、harmless），并以此作为对齐方法的实验室。

**Prompting 干预**：研究了简单的 prompt 干预基线技术，发现适度干预带来的收益随模型规模增大而增加，且不会损害大模型的原有性能，同时具有跨多种对齐评估的泛化能力。

**训练目标的扩展规律对比**：对比了三种与对齐相关的训练目标——模仿学习（imitation learning）、二元判别（binary discrimination）和排序偏好建模（ranked preference modeling）。核心发现：排序偏好建模（RLHF 前身）的性能远优于模仿学习，且通常具有更好的规模扩展规律；而二元判别在性能和扩展规律上与模仿学习非常相似。

**偏好模型预训练**：研究了"偏好模型预训练"（preference model pre-training）训练阶段，目标是在人类偏好微调时提升样本效率。

> 注：本文仅为论文摘要页，原始 raw 文件中仅包含 Abstract，论文全文通过外链提供。
