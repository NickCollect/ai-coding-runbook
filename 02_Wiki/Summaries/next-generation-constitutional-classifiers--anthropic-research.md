---
type: summary
source: 01_Raw/anthropic.com/research/next-generation-constitutional-classifiers.md
source_url: https://www.anthropic.com/research/next-generation-constitutional-classifiers
title: "Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks \\ Anthropic"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Constitutional Classifiers++ 是 Anthropic 第二代越狱防护系统，采用两阶段级联架构（探针 + 交换分类器集成），在几乎消灭通用越狱的同时将计算开销降至约 1%，误拒率从 0.38% 降至 0.05%。

**问题背景**：大型语言模型仍存在越狱漏洞，尤其针对化学、生物、放射性、核武器（CBRN）相关信息。第一代 Constitutional Classifiers 将越狱成功率从 86% 降至 4.4%，但存在两个代价：计算成本增加 23.7%、对无害查询的误拒率增加 0.38%。

**新型攻击类型**：实测发现两类持续有效的攻击——**重构攻击**（将有害信息拆分为看似无害的碎片后重组）和**输出混淆攻击**（将有害内容替换为代号，如将化学试剂改称"食用香精"）。部分越狱虽降低了模型能力（GPQA Diamond 从 74% 降至 32%），但攻击者可能开发出既保留能力又实现越狱的新变体。

**核心创新——交换分类器**：将原有独立的输入/输出分类器合并为单一"交换分类器"，同时审查对话双方，能识别孤立看来无害但结合上下文存在危害的输出。人工红队测试中，越狱成功尝试减少超过 50%，但计算成本增加 50%。

**级联架构降本**：采用两阶段设计——轻量级探针（基于模型内部激活的线性探针，几乎零额外计算）先筛查所有流量，可疑交换再升级至更强的分类器集成做最终判断。探针难以被对抗性输入欺骗（内部表征比输出更难操纵），且与外部分类器互补。

**最终性能**：在 Claude Sonnet 4.5 流量上部署一个月，误拒率 0.05%（较第一代下降 87%）；198,000 次红队尝试（累计超 1700 小时）中仅发现一处高风险漏洞（检出率 0.005/千次查询）；至今无人发现通用越狱。应用于 Claude Opus 4.0 流量时总计算开销约 +1%。
