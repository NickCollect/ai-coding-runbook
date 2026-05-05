---
type: summary
source: 01_Raw/anthropic.com/research/softmax-linear-units.md
source_url: https://www.anthropic.com/research/softmax-linear-units
title: "Softmax Linear Units"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

用 Softmax Linear Unit（SoLU）替换 MLP 激活函数，可在几乎不损失模型性能的前提下，大幅提升神经元的可解释性比例。

**核心贡献**：提出 SoLU 激活函数，通过随机化盲测实验验证其显著增加了 MLP 层中能对应人类可理解概念、短语或类别的神经元比例。

**超级叠加的代价**：研究同时发现，SoLU 可能通过让某些特征"隐藏得更深"来换取其他特征的可解释性——即超级叠加假说成立，不存在免费的午餐。部分特征变得更可解释，可能是以另一些特征变得更不可解释为代价。

**净效益**：尽管存在上述权衡，SoLU 在实践中仍属净收益，因为它实质上提高了研究人员能够理解的神经元比例。

**研究价值**：借助 SoLU 模型，研究者对 transformer 中的信息处理方式获得了若干新洞察。

**日期**：2022 年 6 月 17 日。
