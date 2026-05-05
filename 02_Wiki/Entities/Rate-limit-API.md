---
type: entity
name: Rate-limit-API
aliases: [rate limits / rate limit API / per-workspace rate limit]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Admin API 的 rate-limit 报告 —— `GET /v1/organizations/rate_limits` 全 org，`GET .../workspaces/{id}/rate_limits` per-workspace override。

## 关键属性

- **Endpoints**：
  - Org-level：`GET /v1/organizations/rate_limits` —— 列所有 rate-limit groups
  - Per-workspace：`GET /v1/organizations/workspaces/{id}/rate_limits` —— 仅有 override 的 group 出现 [[admin--api-index]] [[rate_limits--admin-api]] [[workspaces-rate_limits-list--admin-api]]
- **Rate-limit groups**：`model_group` / `batch` / `token_count` / `files` / `skills` / `web_search`
- **Limiter types**：`requests_per_minute` / `input_tokens_per_minute` 等 [[admin--api-index]]
- **Workspace override**：每 row 含 `org_limit`（parent 值参考）+ 新 `value`；无 override 的 group 不列，从 org inherit [[workspaces--admin-api]]
- **Pre-flight 检查**：建议结合 [[Token-counting]] 和 cursor pagination 实现客户端 rate-limit 控制 [[rate-limits-api--bwc]]
- **关联 features 的 rate limit**：[[Batches-API]] 同时受 HTTP 和 in-flight requests 双 limit；[[Web-search-tool]] / [[Files-API]] 各自独立 group

## 出现来源

_13 summaries reference this entity_ ——
- [[rate_limits--admin-api]] / [[rate_limits-list--admin-api]] / [[workspaces-rate_limits-list--admin-api]]
- [[admin--api-index]] / [[rate-limits-api--bwc]] / [[administration-api--bwc]]
- [[batch-processing--bwc]] / [[errors]]

## 相关

- [[Admin-API]] / [[Workspace]]
- [[Token-counting]] / [[Batches-API]] / [[Files-API]] / [[Web-search-tool]] / [[Skill-API]] —— 各自独立 limit group
