---
name: 上下文窗口与定价速查
type: synthesis
created: 2026-05-05
updated: 2026-05-05
sources:
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/context-windows.md
  - 01_Raw/anthropic.com/news/claude-opus-4-7.md
  - 01_Raw/anthropic.com/news/claude-sonnet-4-6.md
  - 01_Raw/anthropic.com/news/claude-haiku-4-5.md
  - 01_Raw/platform.claude.com/docs/en/intro.md
  - web:openai.com/api/pricing (2026-05-05, 待 raw 爬取验证)
  - 01_Raw/ai.google.dev/gemini-api/docs/pricing.md (爬取自 ai.google.dev，2026-05-05)
---

# 上下文窗口与定价速查

## 概览

本文汇总 Anthropic Claude 系列模型的上下文窗口大小和 API 定价，数据来源为 2026-05-04 抓取的官方文档和新闻稿。OpenAI / Gemini 系列因 `01_Raw/` 对应目录尚未爬取，填「*待爬取*」。

---

## Claude 系列

| 模型 | API 名称 | 最大 context | Input $/MTok | Output $/MTok | Prompt Cache 支持 | 速度档位 |
|---|---|---|---|---|---|---|
| **Claude Mythos Preview** | *需确认* | 1M tokens | *需确认* | *需确认* | *需确认* | *需确认* |
| **Claude Opus 4.7** | `claude-opus-4-7` | 1M tokens | $5 | $25 | *需确认* | High / 高延迟 |
| **Claude Opus 4.6** | `claude-opus-4-6` | 1M tokens | $5 | $25 | *需确认* | High / 高延迟 |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | 1M tokens（beta） | $3 | $15 | *需确认* | Mid |
| **Claude Sonnet 4.5** | `claude-sonnet-4-5` | 200k tokens | $3 | $15 | *需确认* | Mid |
| **Claude Haiku 4.5** | `claude-haiku-4-5` | *需确认（推测 200k）* | $1 | $5 | *需确认* | Fast / 最快 |
| **Claude Sonnet 4（deprecated）** | — | 200k tokens | *需确认* | *需确认* | *需确认* | — |

**数据来源说明：**
- 1M / 200k context window 来自 `context-windows.md` line 104："Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a 1M-token context window. Other Claude models, including Claude Sonnet 4.5 and Sonnet 4 (deprecated), have a 200k-token context window."
- Sonnet 4.6 1M context 注明为 "in beta"（claude-sonnet-4-6.md）。
- Opus 4.7 定价来自 claude-opus-4-7.md："Pricing remains the same as Opus 4.6: $5 per million input tokens and $25 per million output tokens."
- Sonnet 4.6/4.5 定价来自 claude-sonnet-4-6.md："Pricing remains the same as Sonnet 4.5, starting at $3/$15 per million tokens."
- Haiku 4.5 定价来自 claude-haiku-4-5.md："Pricing is now $1/$5 per million input and output tokens."
- Haiku 4.5 context window：context-windows.md 提到 Haiku 4.5 有 context awareness，且 "budget is set to 1M tokens (200k for models with a smaller context window)"，推测 Haiku 4.5 属于 200k；但未明确列出，标 *需确认*。

---

## OpenAI 系列

> 数据来源：openai.com/api/pricing（2026-05-05 网络查询）。`platform.openai.com` 文档封锁爬虫（403），OpenAI 知识通过 GitHub repos 覆盖。

| 模型 | API 名称 | 最大 context | Input $/MTok | Output $/MTok | Cache $/MTok | 速度档位 |
|---|---|---|---|---|---|---|
| **GPT-5.5** | `gpt-5.5` | 1,050,000 | $5.00 | $30.00 | $0.50 | 最强 / 高延迟 |
| **GPT-5.4** | `gpt-5.4` | 1,050,000 | $2.50 | $15.00 | $0.25 | 高能力 / 中延迟 |
| **GPT-5.4 mini** | `gpt-5.4-mini` | *需确认* | $0.75 | $4.50 | $0.075 | Fast / 最快 |

**注意事项：**
- GPT-5.5 / 5.4 输入超过 272K tokens 时，input 价格 ×2、output 价格 ×1.5（长上下文溢价）。
- Batch API：所有模型均享 50% 折扣。
- 旧模型（GPT-4o、o3、o4-mini）已从主定价页移除，可能仍可 API 访问但不再是 flagship。

---

## Gemini 系列

> 数据来源：`01_Raw/ai.google.dev/gemini-api/docs/pricing.md`（爬取自 ai.google.dev，2026-05-05，最后更新 2026-04-30）。已通过 raw 文件验证，无需网络查询。

| 模型 | API 名称 | 最大 context | Input $/MTok | Output $/MTok | Cache $/MTok | 速度档位 |
|---|---|---|---|---|---|---|
| **Gemini 3.1 Pro** *(Preview)* | `gemini-3.1-pro-preview` | *需确认* | $2.00（≤200K）/ $4.00（>200K）| $12.00（≤200K）/ $18.00（>200K）| $0.20/$0.40 | 旗舰 |
| **Gemini 3 Flash** *(Preview)* | `gemini-3-flash-preview` | *需确认* | $0.50 | $3.00 | $0.05 | 快速 |
| **Gemini 2.5 Pro** | `gemini-2.5-pro` | 1,000,000 | $1.25（≤200K）/ $2.50（>200K）| $10.00（≤200K）/ $15.00（>200K）| $0.125/$0.25 | 旗舰（稳定）|
| **Gemini 2.5 Flash** | `gemini-2.5-flash` | 1,000,000 | $0.30 | $2.50 | $0.03 | 快速（稳定）|
| **Gemini 2.5 Flash-Lite** | `gemini-2.5-flash-lite` | *需确认* | $0.10 | $0.40 | $0.01 | 最便宜（稳定）|

**来源：** `01_Raw/ai.google.dev/gemini-api/docs/pricing.md` 逐行提取（意大利语界面，数字无歧义）。

**注意事项：**
- Gemini 2.5 Pro 和 3.1 Pro 采用分段定价（≤200K vs >200K），超过 200K 时 input/output 均涨价。
- 所有 Gemini 2.5 稳定版均支持 Context Cache（raw 文件确认）。
- Gemini 3.x 为 Preview 状态，价格和功能可能变化。
- Batch API：所有模型享 50% 折扣（raw 文件："riduzione del costo del 50%"）。

---

## 特殊计费说明

- **Extended thinking**：思考 token 按 output token 计费（context-windows.md）。思考预算是 `max_tokens` 的子集；adaptive thinking 下实际用量可能低于上限。
- **Prompt caching**：cache 创建和 cache 读取有独立计费；具体折扣见 `01_Raw/platform.claude.com/docs/en/build-with-claude/prompt-caching.md`（*需确认*）。
- **Message Batches**：50% 折扣（usage-cost-api.md 引用；具体见 `01_Raw/platform.claude.com/docs/en/build-with-claude/batch-processing.md`）。
- **Opus 4.7 tokenizer**：新 tokenizer 导致相同输入消耗约 1.0–1.35× token（claude-opus-4-7.md）；从 Opus 4.6 迁移时实际成本需实测。

---

## 跨厂商定价一览（同档位对比）

| 档位 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **旗舰（前沿）** | Opus 4.7 $5/$25 · 1M ctx | GPT-5.5 $5/$30 · 1M ctx | Gemini 3.1 Pro $2-4/$12-18 · *ctx TBD* *(Preview)* |
| **旗舰（稳定）** | Opus 4.7 / Sonnet 4.6 | GPT-5.4 $2.50/$15 · 1M ctx | Gemini 2.5 Pro $1.25-2.50/$10-15 · 1M ctx |
| **中端** | Sonnet 4.6 $3/$15 · 1M ctx | GPT-5.4 $2.50/$15 | Gemini 2.5 Flash $0.30/$2.50 · 1M ctx |
| **经济** | Haiku 4.5 $1/$5 · 200K ctx | GPT-5.4 mini $0.75/$4.50 | Gemini 2.5 Flash-Lite $0.10/$0.40 |

> **Gemini 价格优势明显**：Gemini 2.5 Flash-Lite $0.10/$0.40 是所有主流模型中最便宜，且稳定版本可用。Gemini 3.1 Pro (Preview) 旗舰定价反而比 Gemini 2.5 Pro 贵。

---

## 选型速查

1. **上下文 > 200K tokens** → Claude Opus/Sonnet（1M）、GPT-5.x（1M）、Gemini 2.5（1M）均可；Haiku 4.5 不适用。
2. **成本优先** → Gemini 2.5 Flash（$0.30/$2.50）最便宜，其次 Haiku 4.5（$1/$5）。
3. **Claude 生态内 coding/agentic** → Sonnet 4.6（$3/$15，frontier 性能 + 1M ctx）。
4. **需要最强推理** → Claude Opus 4.7 vs GPT-5.5，定价相近（$5/$25 vs $5/$30），按 benchmark 和实际测试选。
5. **超长文档（>200K tokens）且成本敏感** → Gemini 2.5 Pro（分段计费，短上下文 $1.25/$10 更经济）。
6. **批量异步任务** → 所有厂商均有 50% Batch 折扣；Claude Message Batches + Haiku 4.5 是 Anthropic 生态最低成本组合。
