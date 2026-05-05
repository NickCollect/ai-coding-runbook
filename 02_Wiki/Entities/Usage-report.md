---
type: entity
name: Usage-report
aliases: [usage report / usage_report / Claude Code analytics API]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Admin API 的 token + Claude Code 使用统计 —— `/v1/organizations/usage_report/{messages,claude_code}`。

## 关键属性

- **两个 endpoints**：
  - `GET /v1/organizations/usage_report/messages` —— token-bucketed 用量
  - `GET /v1/organizations/usage_report/claude_code` —— daily Claude Code productivity metrics [[admin--api-index]] [[usage_report-retrieve_messages--admin-api]] [[usage_report-retrieve_claude_code--admin-api]]
- **Auth**：`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`
- **Messages usage `group_by`**：`api_key` / `workspace` / `model` / `service_tier` / `context_window` / `inference_geo` / `speed` / `account_id` [[admin--api-index]]
- **Claude Code metrics**：commits / PRs / lines added / lines removed / tool acceptance / tool rejection by tool / model breakdown [[admin--api-index]] [[claude-code-analytics-api--bwc]]
- **Pagination**：opaque `page` token
- **配套**：[[Cost-report]] —— 同 admin API 群组 [[usage-cost-api--bwc]]

## 出现来源

_16 summaries reference this entity_ ——
- [[usage_report--admin-api]] / [[usage_report-retrieve_messages--admin-api]] / [[usage_report-retrieve_claude_code--admin-api]]
- [[admin--api-index]] / [[administration-api--bwc]] / [[usage-cost-api--bwc]] / [[claude-code-analytics-api--bwc]]

## 相关

- [[Admin-API]] / [[Workspace]] / [[Cost-report]] / [[API-key]]
