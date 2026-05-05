---
name: 模型选型决策表
type: synthesis
created: 2026-05-05
updated: 2026-05-05
sources:
  - 01_Raw/anthropic.com/news/claude-opus-4-7.md
  - 01_Raw/anthropic.com/news/claude-sonnet-4-6.md
  - 01_Raw/anthropic.com/news/claude-haiku-4-5.md
  - 01_Raw/platform.claude.com/docs/en/intro.md
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/context-windows.md
  - web:openai.com/api/pricing (2026-05-05, 待 raw 爬取验证)
  - web:aicostcheck.com/blog/google-gemini-pricing-guide-2026 (2026-05-05, 待 raw 爬取验证)
---

# 模型选型决策表

## 概览

本表覆盖 Claude / OpenAI / Gemini 三大厂商当前主力模型的选型逻辑。**Claude 数据**来自 `01_Raw/` 中 2026-05-04 抓取的官方文档；**OpenAI / Gemini 数据**来自 2026-05-05 网络查询（openai.com/api/pricing + aicostcheck.com），待 raw 爬取后验证。价格会随定价调整变化，使用前建议核实官方 Pricing 页面。

---

## 按任务类型选型

| 任务类型 | Claude 推荐 | 推荐理由（来自 raw） | 局限 |
|---|---|---|---|
| **复杂 coding / 自主 agentic** | Claude Opus 4.7 | "most capable model for complex reasoning and agentic coding"；用户测试在最难 coding 任务上可信赖地无人监督交付（claude-opus-4-7.md） | 最贵（$5/$25 per MTok）；tokenizer 更新导致同等输入多消耗约 1.0–1.35× token |
| **日常 coding + 企业工作流** | Claude Sonnet 4.6 | "frontier intelligence at scale — built for coding, agents, and enterprise workflows"；开发者 70% 偏好 Sonnet 4.6 > Sonnet 4.5；代码一致性和指令遵循显著改进（claude-sonnet-4-6.md） | 深度推理能力略低于 Opus 4.7；对极复杂 codebase 重构建议用 Opus |
| **长上下文推理** | Claude Opus 4.7 / Sonnet 4.6 | 均支持 1M token 上下文；Sonnet 4.6 在 Vending-Bench Arena 长期规划评测中表现突出（claude-sonnet-4-6.md） | 长上下文存在 context rot 风险，token 越多精度可能下降（context-windows.md） |
| **视觉 / 多模态** | Claude Opus 4.7 | "substantially better vision"；支持最高 2,576 像素长边（~3.75 MP），是之前 Claude 模型的 3× 以上（claude-opus-4-7.md） | 高分辨率图像消耗更多 token；之前版本分辨率限制更严 |
| **低成本批量处理** | Claude Haiku 4.5 | "$1/$5 per million input/output tokens"；速度是 Sonnet 4 的 2× 以上，成本约 1/3（claude-haiku-4-5.md） | 能力低于 Sonnet/Opus；不适合需要深度推理的任务 |
| **实时 / 低延迟** | Claude Haiku 4.5 | "fastest model with near-frontier intelligence"；适合实时对话、客服 agent、pair programming（claude-haiku-4-5.md） | 上下文较小（*需确认* 是否 200k） |
| **Agentic 编排（orchestrator）** | Claude Opus 4.7 | "Claude finds that Opus 4.6 remains the strongest option for... coordinating multiple agents in a workflow"（claude-sonnet-4-6.md）；Opus 4.7 进一步提升 | *需确认* Opus 4.7 multiagent 定价是否有批量折扣 |
| **Computer use** | Claude Sonnet 4.6 / Opus 4.7 | Sonnet 4.6 在 OSWorld 评测上领先，保险行业 computer use 准确率 94%（claude-sonnet-4-6.md）；Opus 4.7 视觉精度 98.5% vs Opus 4.6 的 54.5%（claude-opus-4-7.md） | Prompt injection 风险仍存在；需额外安全措施 |
| **复杂推理 / 最难 coding（OpenAI）** | GPT-5.5 | "new class of intelligence for coding and professional work"（openai.com，2026-05-05） | 最贵（$5/$30 per MTok）；output 价比 Claude Opus 4.7 贵 20% |
| **日常 coding（OpenAI 中端）** | GPT-5.4 | 与 Claude Sonnet 4.6 定价相同（$2.50/$15），1M context | 暂无 benchmark 对比 raw 数据 |
| **低成本（OpenAI）** | GPT-5.4 mini | $0.75/$4.50，比 Haiku 4.5 便宜但比 Gemini Flash 贵 | context window *需确认* |
| **超低成本（Gemini 稳定版）** | Gemini 2.5 Flash-Lite | $0.10/$0.40，是目前所有主流模型最便宜 | 能力最弱；1M context *需确认* |
| **低成本大上下文（Gemini）** | Gemini 2.5 Flash | $0.30/$2.50，1M context（raw 确认） | Google 生态绑定 |
| **超长文档 cost-sensitive** | Gemini 2.5 Pro | 短上下文（≤200K）$1.25/$10，比 Claude Opus/GPT-5.5 便宜 | >200K 分段涨价；context rot 同样存在 |
| **前沿 Gemini（Preview）** | Gemini 3.1 Pro Preview | $2-4/$12-18，raw 已确认定价（2026-04-30 更新）| Preview 状态，可能变化；context window *需确认* |

---

## 按成本优先选型

| 成本档位 | 模型 | Input $/MTok | Output $/MTok | 来源 |
|---|---|---|---|---|
| **低（cheap）** | Claude Haiku 4.5 | $1 | $5 | claude-haiku-4-5.md |
| **中（mid）** | Claude Sonnet 4.6 / Sonnet 4.5 | $3 | $15 | claude-sonnet-4-6.md（"pricing remains the same as Sonnet 4.5"） |
| **高（premium）** | Claude Opus 4.7 / Opus 4.6 | $5 | $25 | claude-opus-4-7.md（"pricing remains the same as Opus 4.6"） |
| **Preview / 旗舰** | Claude Mythos Preview | *需确认* | *需确认* | 仅在 context-windows.md / news 中提及，未找到公开定价 |
| **最低成本** | Gemini 2.5 Flash | $0.30 | $2.50 | web:aicostcheck.com (2026-05-05) |
| **低（cheap）** | Claude Haiku 4.5 / GPT-5.4 mini | $1 / $0.75 | $5 / $4.50 | claude-haiku-4-5.md / web:openai.com (2026-05-05) |
| **中（mid）** | Sonnet 4.6 / GPT-5.4 / Gemini 2.5 Pro（短ctx）| $3 / $2.50 / $1.25 | $15 / $15 / $10 | 见各来源 |
| **高（premium）** | Opus 4.7 / GPT-5.5 | $5 | $25 / $30 | claude-opus-4-7.md / web:openai.com (2026-05-05) |

**批量折扣**：Anthropic Message Batches API 提供 50% 折扣（usage-cost-api.md 引用）。具体 endpoint 见 `01_Raw/platform.claude.com/docs/en/build-with-claude/batch-processing.md`。

---

## 已知 trade-off 汇总

- **Opus 4.7 vs Sonnet 4.6**：Opus 4.7 在最难 coding 任务上有明确优势（CursorBench 70% vs 58%，claude-opus-4-7.md）；但 Sonnet 4.6 已接近 Opus 4.5 级别，且成本低 40%。用户曾以 59% 的比例偏好 Sonnet 4.6 胜过老 Opus 4.5（claude-sonnet-4-6.md）。
- **1M vs 200k context**：超长上下文（≥200k tokens）只有 Opus 4.7/4.6、Sonnet 4.6 支持（context-windows.md line 104）。Haiku 4.5 上下文大小 *需确认*。
- **Tokenizer 变更**：Opus 4.7 引入新 tokenizer，相同输入可能多消耗约 1.0–1.35× token。从 Opus 4.6 迁移需测量真实 traffic（claude-opus-4-7.md）。
- **Effort 控制**：Opus 4.7 新增 `xhigh` effort level（介于 `high` 和 `max` 之间）；Claude Code 默认 effort 提升至 `xhigh`（claude-opus-4-7.md）。
- **Extended thinking**：Sonnet 4.6 同时支持 adaptive thinking 和 extended thinking；思考 token 按 output token 计费（context-windows.md）。
- **Context rot**：上下文越大，精度/召回下降风险越高。Anthropic 建议使用 compaction / context editing 管理长对话（context-windows.md）。
