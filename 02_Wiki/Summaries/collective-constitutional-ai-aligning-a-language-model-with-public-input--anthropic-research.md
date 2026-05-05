---
type: summary
source: 01_Raw/anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input.md
source_url: https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input
title: "Collective Constitutional AI: Aligning a Language Model with Public Input"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Anthropic 与 Collective Intelligence Project 合作，于 2023 年 10 月发布了 Collective Constitutional AI 研究：首次通过公众在线审议过程（约 1,000 名美国人）众包草拟一份 AI 系统"宪法"，并用其训练模型，探索民主化 AI 价值对齐的可行性。

**实验设计**：使用 Polis 平台进行在线审议，招募具有一定 AI 认知的美国公众代表性样本。参与者共提交 1,127 条原则声明，投票 38,252 次（人均 34 次）。Polis 识别出两个意见群体，但大多数声明获得高度共识。

**公众宪法 vs Anthropic 宪法**：两份宪法有约 50% 的概念重叠。主要差异：公众版更强调客观性与公正性、可及性（accessibility）、主动倡导正向行为而非仅禁止负面行为；而 Anthropic 版更多借鉴联合国人权宣言等外部权威来源。未入选原则的例子包括：DEI 相关、"AI 应有情感"以及集体利益与个人自由之间相互矛盾的主张。

**模型训练与评估结果**：训练了 Public（对公众宪法）和 Standard（对 Anthropic 宪法）两个 Claude Instant 规模模型：
- 两者在 MMLU 和 GSM8K 上表现相当
- 人类评估帮助性与无害性评分无显著差异
- Public 模型在 BBQ 偏见测试中的九个社会维度上偏见分数均低于 Standard 模型（残障状态和外貌维度差距最大）
- 两者在 OpinionQA 上均更接近自我认定为自由派的群体，差异不大

**关键教训与局限**：Constitutional AI 训练远比预期复杂，无法独立完成；prompt 数据库的质量和权重比例对结果影响极大；现有评估套件不足以全面刻画宪法差异；公众声明到 CAI 原则的转换过程存在大量主观判断。

**意义**：这可能是首个通过公众在线审议过程集体影响大语言模型行为的实例，为 AI 民主化对齐提供了初步实证经验，但同时也揭示了该路径的大量技术与社会挑战。
