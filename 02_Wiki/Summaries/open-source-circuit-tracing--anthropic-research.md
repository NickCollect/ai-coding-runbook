---
type: summary
source: 01_Raw/anthropic.com/research/open-source-circuit-tracing.md
source_url: https://www.anthropic.com/research/open-source-circuit-tracing
title: "Open-sourcing circuit-tracing tools \\ Anthropic"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Anthropic 于 2025 年 5 月开源了电路追踪（circuit tracing）工具库，允许任何人在主流开源模型上生成归因图（attribution graphs）并通过 Neuronpedia 可视化探索，推动社区参与机制性可解释性研究。

**核心方法**：通过生成"归因图"（attribution graphs）来（部分）揭示语言模型在决定特定输出时的内部推理步骤。归因图展示模型从输入到输出的中间计算链路，是机制性可解释性研究的核心工具。

**开源内容**：发布的开源库支持在主流开源模型上生成归因图；Neuronpedia（第三方合作平台）提供交互式前端，可可视化、注释和分享图表。研究者可通过该工具：追踪特定模型的电路、可视化并分享归因图、修改 feature 值观察输出变化以验证假设。

**已有应用**：团队已使用该工具研究 Gemma-2-2b 和 Llama-3.2-1b 的多步推理和多语言表征等行为，demo notebook 提供分析示例，并附有尚未分析的归因图供社区探索。

**项目背景**：项目由 Anthropic Fellows 计划参与者 Michael Hanna 和 Mateusz Piotrowski 领导（导师 Emmanuel Ameisen 和 Jack Lindsey），与 Decode Research（Neuronpedia）合作开发；Gemma 图基于 GemmaScope 项目训练的 transcoder。

**战略意义**：Anthropic CEO Dario Amodei 曾指出当前 AI 能力进步速度远超人类对其内部工作机理的理解，开源这些工具旨在调动更广泛社区力量共同研究语言模型内部机制，加速解决这一理解赤字。
