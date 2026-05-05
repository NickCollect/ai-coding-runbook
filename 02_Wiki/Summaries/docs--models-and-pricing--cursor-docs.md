---
type: summary
source: 01_Raw/docs.cursor.com/docs--models-and-pricing.md
source_url: https://cursor.com/docs/models-and-pricing
title: "Models & Pricing"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor 支持 Anthropic、OpenAI、Google、xAI 等主流模型，个人计划包含两个独立用量池，按月计费周期重置。

**两个用量池**：
- **Auto + Composer 池**：使用 Auto（Cursor 智能选模型）或 Composer 2 时消耗，成本更低，日常任务首选
- **API 池**：选择特定模型时按 API 价格计费，个人计划每月至少包含 $20

**Auto 定价**：输入+缓存写入 $1.25/M tokens；输出 $6/M；缓存读取 $0.25/M。

**Composer 2**：Cursor 自研模型，优化用于自主编程，输入 $0.5/M，输出 $2.5/M。

**主要模型价格（API 池）**：Claude 4.6 Sonnet $3/$15（输入/输出）；GPT-5.5 $5/$30；Gemini 3.1 Pro $2/$12；Grok 4.20 $2/$6；Composer 2 $0.5/$2.5（最便宜）。

**个人计划**：Pro $20/月（含 $20 API）、Pro Plus $60/月（含 $70 API）、Ultra $200/月（含 $400 API）。超出后可按需付费或升级计划。

**Max Mode**：将上下文窗口扩展至模型支持的最大值，按 API 价格的 token 计费（消耗更快）。Teams 计划非 Auto 请求额外加 $0.25/M token 的 Cursor Token Rate。

**团队计划**：Teams $40/用户/月（含 SSO、Privacy Mode 强制等）；Enterprise 定制价格（含 SCIM、高级安全控制）。
