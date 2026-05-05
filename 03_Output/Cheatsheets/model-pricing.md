---
type: cheatsheet
topic: model-pricing
updated: 2026-05-05
---

# Model Pricing Quick Reference

> 价格以官方文档为准，定期变动。Last verified: **2026-05-05**。
> Claude 数据来自 `01_Raw/` 已爬取文档；OpenAI 来自 openai.com/api/pricing 网络查询；Gemini 来自 `01_Raw/ai.google.dev/gemini-api/docs/pricing.md`（2026-04-30 更新）。

---

## Claude

| Model | Input $/MTok | Output $/MTok | Context | Tags |
|---|---|---|---|---|
| Claude Opus 4.7 | $5.00 | $25.00 | 1M | thinking, vision, agentic |
| Claude Opus 4.6 | $5.00 | $25.00 | 1M | thinking, vision, agentic |
| Claude Sonnet 4.6 | $3.00 | $15.00 | 1M (beta) | vision, fast, coding |
| Claude Sonnet 4.5 | $3.00 | $15.00 | 200K | vision |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K* | fast, cheap |

> \* Haiku 4.5 context window not explicitly confirmed in raw docs; likely 200K.

**Caching** (relative to base input): write 5m = 1.25×, write 1h = 2×, read = **0.1×** (90% off)
**Batch API**: 50% off all models

---

## OpenAI

| Model | Input $/MTok | Output $/MTok | Cached $/MTok | Context | Tags |
|---|---|---|---|---|---|
| GPT-5.5 | $5.00 | $30.00 | $0.50 | 1,050K | thinking*, vision, audio |
| GPT-5.4 | $2.50 | $15.00 | $0.25 | 1,050K | vision, coding |
| GPT-5.4 mini | $0.75 | $4.50 | $0.075 | TBD* | fast, cheap |

> \* GPT-5.5 reasoning not exposed as streaming tokens. GPT-5.4 mini context TBD.
> Long-context premium: >272K tokens → input ×2, output ×1.5 (GPT-5.5 / 5.4)

**Caching**: automatic, no extra write cost; read = **0.1×** base (90% off)
**Batch API**: 50% off all models

---

## Gemini

| Model | Input $/MTok | Output $/MTok | Cache $/MTok/h | Context | Tags |
|---|---|---|---|---|---|
| Gemini 3.1 Pro *(Preview)* | $2.00 / $4.00† | $12.00 / $18.00† | $0.20 / $0.40† | TBD | thinking, vision, audio |
| Gemini 3 Flash *(Preview)* | $0.50 | $3.00 | $0.05 | TBD | fast |
| Gemini 2.5 Pro | $1.25 / $2.50† | $10.00 / $15.00† | $0.125 / $0.25† | 1M | vision, stable |
| Gemini 2.5 Flash | $0.30 | $2.50 | $0.03 | 1M | fast, cheap, stable |
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 | $0.01 | TBD* | cheapest, stable |

> † Tiered pricing: ≤200K / >200K tokens. \* Flash-Lite context TBD.

**Caching**: implicit (auto, Gemini 2.5+) + explicit (create cache object, pay storage/hour)
**Batch API**: 50% off all models

---

## Cross-Vendor Tier Comparison

| Tier | Claude | OpenAI | Gemini |
|---|---|---|---|
| **Premium** | Opus 4.7 $5/$25 · 1M ctx | GPT-5.5 $5/$30 · 1M ctx | Gemini 3.1 Pro $2–4/$12–18 *(Preview)* |
| **Mid** | Sonnet 4.6 $3/$15 · 1M ctx | GPT-5.4 $2.50/$15 · 1M ctx | Gemini 2.5 Pro $1.25–2.50/$10–15 · 1M ctx |
| **Economy** | Haiku 4.5 $1/$5 · 200K | GPT-5.4 mini $0.75/$4.50 | Gemini 2.5 Flash $0.30/$2.50 · 1M ctx |
| **Ultra-cheap** | — | — | Gemini 2.5 Flash-Lite $0.10/$0.40 |

---

## Quick Decision

- **Cost first** → Gemini 2.5 Flash-Lite ($0.10/$0.40), then Flash ($0.30/$2.50)
- **Batch async** → All vendors 50% off; Claude Haiku + Batch is lowest Anthropic cost
- **Long context (>200K)** → Opus 4.7, Sonnet 4.6, GPT-5.x, Gemini 2.5 all support 1M
- **Best coding** → Opus 4.7 (CursorBench 70%) vs GPT-5.5 (~same price, $5 input)
- **Opus 4.7 tokenizer note**: new tokenizer may consume 1.0–1.35× more tokens vs Opus 4.6 — measure real traffic before migrating
