---
type: entity
name: Admin-API
aliases: [admin API / organization API / /v1/organizations]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic 组织管理 API —— `/v1/organizations/...`，需 admin-scoped key（与普通 Messages API key 区分），管 org / workspace / user / invite / api-key / usage / cost / rate-limit。

## 关键属性

- **Auth**：`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`（admin-scoped，不是普通 Messages API key）+ `anthropic-version: 2023-06-01` [[admin--api-index]]
- **10 个 resource 群组**：
  1. **Organizations** —— `GET /v1/organizations/me` 返回 admin key 关联的 org（`id`, `name`, `type:"organization"`）
  2. **Invites** —— Create / Retrieve / List / Delete at `/v1/organizations/invites`；roles `user`/`developer`/`billing`/`claude_code_user`（**不可 invite 为 admin**）；status `accepted`/`expired`/`deleted`/`pending`
  3. **Users** —— Retrieve / List / Update / Delete at `/v1/organizations/users`；含 `admin` role；List 支持 `email` filter + cursor pagination
  4. **[[Workspace]]s** —— Create / Retrieve / List / Update / Archive；含 `data_residency` (`workspace_geo` immutable / `allowed_inference_geos` / `default_inference_geo`) / `display_color` / `archived_at`
  5. **Members**（workspace-scoped）—— `/v1/organizations/workspaces/{id}/members`；roles `workspace_user`/`workspace_developer`/`workspace_restricted_developer`/`workspace_admin`/`workspace_billing`（最后一个不可 create 时 assign）
  6. **Workspace [[Rate-limit-API]]** —— `GET .../workspaces/{id}/rate_limits` 列 per-workspace overrides（其他从 org inherit）
  7. **[[API-key]]s** —— Retrieve / List / Update at `/v1/organizations/api_keys`；status `active`/`inactive`/`archived`/`expired`；List filter by `status` / `workspace_id` / `created_by_user_id`；**无 create endpoint**（console 创建）
  8. **[[Usage-report]]** —— `GET .../usage_report/messages` (token-bucketed, group-by) + `GET .../usage_report/claude_code` (daily Claude Code productivity metrics)
  9. **[[Cost-report]]** —— `GET .../cost_report` 返回 daily USD costs，按 workspace/description group，`cost_type` (tokens/web_search/code_execution/session_usage)、`service_tier` (standard/batch)、token type (uncached/output/cache_read/cache_creation 1h/5m) 拆
  10. **Org Rate Limits** —— `GET .../rate_limits` 列 rate-limit groups (`model_group` / `batch` / `token_count` / `files` / `skills` / `web_search`)，limiter `requests_per_minute` / `input_tokens_per_minute` [[admin--api-index]]
- **Pagination**：list endpoints 用 cursor (`after_id` / `before_id` / `limit` 1-1000，default 20) 或 opaque `page` token (报告 endpoints)
- **Anthropic Console**：与 admin API 配套的 web UI，做账户管理 / settings 配置

## 出现来源

_46 summaries reference this entity_ ——
- [[admin--api-index]] + 全部 admin sub-endpoints (`*--admin-api`)
- [[administration-api--bwc]] / [[claude-code-analytics-api--bwc]] / [[usage-cost-api--bwc]] / [[rate-limits-api--bwc]] / [[workspaces--bwc]]

## 相关

- [[Workspace]] / [[API-key]] / [[Cost-report]] / [[Usage-report]] / [[Rate-limit-API]] / [[Invite]] —— 子资源
