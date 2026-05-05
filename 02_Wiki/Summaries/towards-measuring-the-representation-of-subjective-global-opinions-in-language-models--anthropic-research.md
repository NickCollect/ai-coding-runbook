---
type: summary
source: 01_Raw/anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models.md
source_url: https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models
title: "Towards Measuring the Representation of Subjective Global Opinions in Language Models"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

LLM 默认生成的回答在全球主观议题上存在明显的地域偏差，并非平等代表全球多元观点。

**数据集**：构建了 GlobalOpinionQA——基于跨国调查的问答数据集，旨在捕捉不同国家对全球议题的多元意见。

**方法**：定义一个按国家条件化的相似度指标，量化 LLM 生成的调查回答与人类回答之间的相似程度。

**三组实验发现**：
- **默认偏差**：默认状态下，LLM 回答与美国、部分欧洲及南美国家居民的意见更为相似，其他地区代表性不足。
- **提示引导的局限**：要求模型从特定国家角度回答时，回答确实向该国观点偏移，但同时会反映有害的文化刻板印象。
- **语言翻译的局限**：将问题翻译为目标语言，并不必然使模型回答更接近该语言使用者的观点。

**开放资源**：研究发布了 GlobalOpinionQA 数据集及交互式可视化工具，供社区研究使用。

**日期**：2023 年 6 月 29 日。
