---
type: summary
source: 01_Raw/anthropic.com/research/privileged-bases-in-the-transformer-residual-stream.md
source_url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
title: "Privileged Bases in the Transformer Residual Stream \\ Anthropic"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Anthropic 2023 年的可解释性基础研究发现：Transformer 残差流（residual stream）中确实存在"特权基底"（privileged bases）方向，即某些坐标轴方向比随机方向更有可能编码信息，而 Adam 优化器的逐维度归一化（per-dimension normalizers）是造成这一现象的主要原因。

**研究问题**：Transformer 架构的数学理论预测残差流中各个坐标方向应无特殊意义（即基底方向应是"任意的"，不比随机方向更倾向于编码信息）。但实际观察表明这一理论预测是错误的——某些轴向方向确实是"特权的"。

**核心结论**：研究初步认定 Adam 优化器中的逐维度归一化器（per-dimension normalizers，即 Adam 为每个参数维度维护独立的二阶矩估计，导致不同维度的更新幅度不同）是造成残差流出现特权基底的原因。

**排除因素**：研究通过实验明确排除了另外两个看似可能的来源：Layer Normalization（层归一化）和有限精度浮点运算（finite-precision floating-point calculations）均不是观察到的基底对齐现象的原因。

**理论意义**：该发现对机制性可解释性研究具有重要基础意义——若残差流存在特权方向，则神经元激活的轴向基底比任意旋转后的方向更可能携带可解释的信息，这为后续的稀疏自编码器（SAE）和 feature 研究提供了理论支撑。

**局限说明**：原始页面为论文摘要页，标注"初步结论"（provisionally conclude），完整实验细节需通过链接访问原始 Paper，本摘要仅基于页面可获取内容整理。
