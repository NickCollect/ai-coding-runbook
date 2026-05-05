---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--pricing.md
source_url: https://cursor.com/docs/account/teams/pricing
title: "Team Pricing（团队定价）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Teams 计划 $40/用户/月，含 $20/用户/月的包含用量；Enterprise 定制价格，含用量池共享。

**包含用量**：每席 $20/月，按用户独立分配，不可跨成员转移，每计费周期重置，按公开 API 定价 + Cursor Token Rate 计算。

**按需用量**：超出 $20 后自动继续按相同费率（API 价格 + Cursor Token Rate）按月计费，不降速不降质，管理员可在 dashboard 查看并设置花费上限。Teams 计划默认开启按需用量。

**Cursor Token Rate**：非 Auto 的 Agent 请求每 100 万 token 额外收 $0.25，涵盖语义搜索、自定义模型执行（Tab、Apply 等）和基础设施成本，适用于 input/output/cached 所有 token，包括 BYOK。

**Teams vs Enterprise**：Teams 适合自助服务；Enterprise 适合需要优先支持、用量池共享、发票结算、SCIM 或高级安全控制的客户。

模型定价与个人计划相同，均为公开 API 定价 + Cursor Token Rate。
