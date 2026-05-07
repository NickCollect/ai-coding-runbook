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
- **Workload Identity Federation alternative**：production 用 WIF 用 IdP（AWS/GCP/Azure/GitHub Actions/K8s/Okta）签的 short-lived JWT 换 `sk-ant-oat01-...` access token，无 long-lived `sk-ant-api...` 可泄漏；env 里设了 `ANTHROPIC_API_KEY` 会**静默 shadow** federation [[workload-identity-federation--bwc]] [[authentication-overview--api-auth]] [[wif-reference--api-auth]]
- **Token type 区分**：`sk-ant-api...` = 长 lived API key（this entity）；`sk-ant-admin...` = Admin API key；`sk-ant-oat01-...` = WIF 短 lived OAuth access token [[wif-reference--api-auth]]

## 出现来源

_19 summaries reference this entity_ ——
- [[api_keys--admin-api]] / [[api_keys-list--admin-api]] / [[api_keys-retrieve--admin-api]] / [[api_keys-update--admin-api]]
- [[admin--api-index]] / [[administration-api--bwc]]
- [[create--msg-api]] / [[get-started--platform]] / [[intro--platform]] / [[overview--bwc]]
- [[usage_report-retrieve_messages--admin-api]]
- [[workload-identity-federation--bwc]] / [[authentication-overview--api-auth]] / [[wif-reference--api-auth]] / [[wif-github-actions--bwc]]

## 相关

- [[Admin-API]] —— admin key 用此
- [[Workspace]] —— scope 单位
- [[Messages-API]] —— 普通 key 用此
