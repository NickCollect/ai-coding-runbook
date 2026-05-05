---
type: entity
name: Session-API
aliases: [sessions / managed agent session / BetaManagedAgentsSession]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Managed Agent 的持久 conversation thread 资源 —— `/v1/sessions`，含 file/MCP resource、event log、SSE 流式。

## 关键属性

- **Beta header**：`anthropic-beta: managed-agents-2026-04-01` [[sessions-index--beta-api]]
- **Session Endpoints**：
  - `POST /v1/sessions` —— Create
  - `GET /v1/sessions` —— List
  - `GET /v1/sessions/{id}` —— Retrieve
  - `POST /v1/sessions/{id}` —— Update（`title` / `metadata` / `vault_ids`）
  - `DELETE /v1/sessions/{id}` —— Delete
  - `POST /v1/sessions/{id}/archive` —— Archive [[sessions-index--beta-api]]
- **Events sub-resource** (`/sessions/{id}/events`)：
  - `GET .../events` —— List（`limit` / `order` / `page` cursor）
  - `POST .../events` —— Send（push `events[]` of `BetaManagedAgentsEventParams`：user message / interrupt / tool confirmation / custom tool result）
  - `GET .../events/stream` —— **SSE stream**，emits `BetaManagedAgentsStreamSessionEvents`（`UserMessageEvent` / `UserInterruptEvent` / `UserToolConfirmationEvent` / agent message / tool_use / custom_tool_use 等） [[sessions-index--beta-api]] [[sessions-events-stream--beta-api]]
- **Resources sub-resource** (`/sessions/{id}/resources`)：
  - Add (`type: "file"`, `file_id`, optional `mount_path`) / List / Retrieve / Update（`authorization_token` for OAuth refresh） / Delete [[sessions-index--beta-api]] [[sessions-resources-add--beta-api]]
- **Vault 链接**：`vault_ids` 数组让 agent 在调 MCP server 时 resolve credentials [[Vault]]
- **Event log immutable**：用于 reconstruct conversation state [[sessions-index--beta-api]]
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header
- **vs [[Streaming-API]]**：Messages 的 SSE 是 token-level；Session 的 events stream 是 conversation-level（不同协议）

## 出现来源

_39 summaries reference this entity_ ——
- [[sessions-index--beta-api]] / [[sessions-create--beta-api]] / [[sessions-list--beta-api]] / [[sessions-retrieve--beta-api]] / [[sessions-update--beta-api]] / [[sessions-delete--beta-api]] / [[sessions-archive--beta-api]]
- [[sessions-events-index--beta-api]] / [[sessions-events-list--beta-api]] / [[sessions-events-send--beta-api]] / [[sessions-events-stream--beta-api]]
- [[sessions-resources-index--beta-api]] / [[sessions-resources-add--beta-api]] / [[sessions-resources-list--beta-api]] / [[sessions-resources-retrieve--beta-api]] / [[sessions-resources-update--beta-api]] / [[sessions-resources-delete--beta-api]]
- [[sessions--ma]] / [[overview--ma]] / [[onboarding--ma]] / [[events-and-streaming--ma]]

## 相关

- [[Managed-agent]] —— Session 是 agent 的 conversation 单位
- [[Vault]] —— credentials resolution
- [[Environment-API]] —— sandbox 关联
- [[Files-API]] —— resource 来源
- [[MCP-server]] —— tool 来源
- [[Streaming-API]] —— Messages 的 SSE（不同协议）
