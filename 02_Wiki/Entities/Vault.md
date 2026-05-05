---
type: entity
name: Vault
aliases: [vaults / agent vault / managed agent credential vault]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Managed Agent 的加密凭证存储 —— `/v1/vaults`，存 OAuth tokens / static bearer tokens 等，agent 调 MCP server / 工具时 runtime resolve。

## 关键属性

- **Beta header**：`anthropic-beta: managed-agents-2026-04-01` [[vaults-index--beta-api]]
- **Vault endpoints**：Create (`display_name` + optional `metadata`) / List / Retrieve / Update / Delete / Archive [[vaults-index--beta-api]]
- **Credentials sub-resource** (`/vaults/{id}/credentials`)：
  - Create —— `auth` 是 `BetaManagedAgentsMCPOAuthCreateParams` 或 `BetaManagedAgentsStaticBearerCreateParams`
  - List（`include_archived` / `limit` / `page`）
  - Retrieve / Update / Delete / Archive [[vaults-index--beta-api]] [[vaults-credentials-index--beta-api]] [[vaults-credentials-create--beta-api]]
- **关联 Session**：[[Session-API]] 通过 `vault_ids` 数组绑 vault；agent 调 [[MCP-server]] tool 时 resolve credentials
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header

## 出现来源

_24 summaries reference this entity_ ——
- [[vaults-index--beta-api]] / [[vaults-create--beta-api]] / [[vaults-list--beta-api]] / [[vaults-retrieve--beta-api]] / [[vaults-update--beta-api]] / [[vaults-delete--beta-api]] / [[vaults-archive--beta-api]]
- [[vaults-credentials-index--beta-api]] / [[vaults-credentials-create--beta-api]] / [[vaults-credentials-list--beta-api]] / [[vaults-credentials-retrieve--beta-api]] / [[vaults-credentials-update--beta-api]] / [[vaults-credentials-delete--beta-api]] / [[vaults-credentials-archive--beta-api]]
- [[vaults--ma]] / [[sessions-index--beta-api]] / [[sessions--ma]]

## 相关

- [[Managed-agent]] / [[Session-API]] —— 链接 vault 用 credentials
- [[MCP-server]] —— credentials 给 MCP OAuth / bearer auth
