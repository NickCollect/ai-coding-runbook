---
type: entity
name: Cost-report
aliases: [cost report / cost API / usage cost]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Admin API 的 daily USD cost 报告 —— `GET /v1/organizations/cost_report`，按 workspace / description / cost_type / service_tier / token_type 拆细。

## 关键属性

- **Endpoint**：`GET /v1/organizations/cost_report` [[cost_report--admin-api]] [[admin--api-index]]
- **Auth**：`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` [[admin--api-index]]
- **粒度**：daily USD costs
- **Group-by**：workspace / description
- **Cost type 拆**：`tokens` / `web_search` / `code_execution` / `session_usage`
- **Service tier 拆**：`standard` / `batch`
- **Token type 拆**：`uncached` / `output` / `cache_read` / `cache_creation 1h` / `cache_creation 5m` [[admin--api-index]]
- **Pagination**：opaque `page` token（reports endpoints 风格）
- **Claude Code analytics**：`claude-code-analytics-api` 文档把此视为 Claude Code 使用 cost 来源之一 [[claude-code-analytics-api--bwc]]
- **配套**：[[Usage-report]] —— 同 admin API 群组 [[usage-cost-api--bwc]]

## 出现来源

_13 summaries reference this entity_ ——
- [[cost_report--admin-api]] / [[cost_report-retrieve--admin-api]]
- [[admin--api-index]] / [[claude-code-analytics-api--bwc]] / [[usage-cost-api--bwc]] / [[administration-api--bwc]]

## 相关

- [[Admin-API]] / [[Workspace]] / [[Usage-report]]
- [[Code-execution-tool]] / [[Web-search-tool]] / [[Web-fetch-tool]] —— 细类 cost 项
- [[Prompt-caching]] —— cache token 拆细
