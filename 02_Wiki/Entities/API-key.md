---
type: entity
name: API-key
aliases: [api keys / API key / x-api-key]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic API 调用凭证（`X-Api-Key` header）—— 普通 vs admin 两种 scope，绑 [[Workspace]]。

## 关键属性

- **两种 scope**：
  - 普通 `ANTHROPIC_API_KEY` —— Messages API / 一般 endpoint
  - `ANTHROPIC_ADMIN_API_KEY` —— Admin API（`/v1/organizations/...`） [[admin--api-index]]
- **Header**：`X-Api-Key: $KEY` + `anthropic-version: 2023-06-01` [[create--msg-api]]
- **Admin endpoints** under `/v1/organizations/api_keys`：
  - `GET /v1/organizations/api_keys/{id}` —— Retrieve
  - `GET /v1/organizations/api_keys` —— List（filter `status` / `workspace_id` / `created_by_user_id`）
  - `POST /v1/organizations/api_keys/{id}` —— Update
  - **无 Create endpoint —— 通过 console 创建** [[api_keys--admin-api]]
- **Status**：`active` / `inactive` / `archived` / `expired`
- **Workspace scope**：每 key 绑 workspace；同 workspace 其他 key 共享 [[Files-API]] / [[Code-execution-tool]] container
- **OAuth alternative**：API key 之外 `claude.ai/customize/connectors` connector 用 OAuth；MCP server 也支持 OAuth flow（详见 [[MCP-server]]）

## 出现来源

_16 summaries reference this entity_ ——
- [[api_keys--admin-api]] / [[api_keys-list--admin-api]] / [[api_keys-retrieve--admin-api]] / [[api_keys-update--admin-api]]
- [[admin--api-index]] / [[administration-api--bwc]]
- [[create--msg-api]] / [[get-started--platform]] / [[intro--platform]] / [[overview--bwc]]
- [[usage_report-retrieve_messages--admin-api]]

## 相关

- [[Admin-API]] —— admin key 用此
- [[Workspace]] —— scope 单位
- [[Messages-API]] —— 普通 key 用此
