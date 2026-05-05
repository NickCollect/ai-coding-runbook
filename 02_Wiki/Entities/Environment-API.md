---
type: entity
name: Environment-API
aliases: [environments / agent environment / BetaCloudConfig]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Managed Agent 的 sandbox 执行上下文 —— `/v1/environments`，e.g. `BetaCloudConfig`。Sessions / Agents 引用它获得一致 sandbox。

## 关键属性

- **Beta header**：`anthropic-beta: managed-agents-2026-04-01` [[environments-index--beta-api]]
- **Endpoints**：
  - `POST /v1/environments` —— Create（`name` 必填；optional `config` / `description` / `metadata`）
  - `GET /v1/environments` —— List
  - `GET /v1/environments/{id}` —— Retrieve
  - `POST /v1/environments/{id}` —— Update
  - `DELETE /v1/environments/{id}` —— Delete
  - `POST /v1/environments/{id}/archive` —— Archive [[environments-index--beta-api]]
- **Resource shape**：`id` / `name` / `description` / `config`（如 `BetaCloudConfigParams`） / `metadata` / `created_at` / `archived_at` [[environments-index--beta-api]]
- **关联**：[[Session-API]] 和 [[Managed-agent]] 引用 environment 获得一致 sandbox [[cloud-containers--ma]]
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header

## 出现来源

_14 summaries reference this entity_ ——
- [[environments-index--beta-api]] / [[environments-create--beta-api]] / [[environments-list--beta-api]] / [[environments-retrieve--beta-api]] / [[environments-update--beta-api]] / [[environments-delete--beta-api]] / [[environments-archive--beta-api]]
- [[cloud-containers--ma]] / [[sessions-index--beta-api]] / [[sessions--ma]]

## 相关

- [[Managed-agent]] / [[Session-API]] —— 引用 environment
- [[Code-execution-tool]] —— Anthropic-managed sandbox 的另一形态（不同 product）
