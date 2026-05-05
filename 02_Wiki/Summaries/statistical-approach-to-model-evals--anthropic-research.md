---
type: summary
source: 01_Raw/anthropic.com/research/statistical-approach-to-model-evals.md
source_url: https://www.anthropic.com/research/statistical-approach-to-model-evals
title: "A statistical approach to model evaluations"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

模型评估结果应用统计严谨性来处理，当前 AI 研究界的 eval 报告方式系统性地低估了测量不确定性。

**五项核心建议**：

**推荐一：使用中心极限定理**——报告均值标准误（SEM）以量化两模型理论均值之差，避免仅比较观测均值而忽略随机性。95% 置信区间为均值 ± 1.96×SEM。

**推荐二：聚类标准误**——对含相关问题群组的 eval（如阅读理解题共用同一段落），应按随机化单元聚类计算标准误，否则会低估不确定性达 3 倍以上，导致虚假显著。

**推荐三：降低题内方差**——若使用 CoT，对同一题多次采样取平均；若不用 CoT，直接用下一 token 概率作为题目得分，可消除随机误差分量。

**推荐四：配对差异分析**——比较两模型时，利用问题列表共享的结构做配对差异检验，前沿模型间题目得分相关系数为 0.3–0.7，配对分析是"免费"的方差降低手段。

**推荐五：功效分析**——在设计 eval 前用功效公式确定所需题目数量，以保证能检测到目标效应量。

**日期**：2024 年 11 月 19 日。
