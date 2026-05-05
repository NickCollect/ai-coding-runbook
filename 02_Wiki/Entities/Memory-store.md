---
type: entity
name: Memory-store
aliases: [memory stores / managed agent memory / BetaManagedAgentsMemoryStore]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Managed Agent 的 server-side persistent memory —— `/v1/memory_stores`，path-keyed UTF-8 text "memories" + optimistic concurrency + 版本化 history。

## 关键属性

- **Beta header**：`anthropic-beta: managed-agents-2026-04-01` [[memory_stores-index--beta-api]]
- **Memory-store endpoints**：Create / List / Retrieve / Update / Delete / Archive [[memory_stores-index--beta-api]]
- **Memories sub-resource** (`/memory_stores/{id}/memories`)：Create (`content`, `path`) / List / Retrieve / Update (`content?` / `path?` / `precondition?`) / Delete [[memory_stores-memories-index--beta-api]]
- **Memory-versions sub-resource** (`/memory_versions`)：List / Retrieve / `POST .../{version_id}/redact` 重定 content [[memory_stores-memory_versions-index--beta-api]]
- **Path 规则**：`/`-起始、NFC normalized、无 `.` / `..` / 空 segment、≤ 1024 bytes、case-sensitive [[memory_stores-index--beta-api]]
- **Content**：UTF-8，≤ 100 KB
- **Optimistic concurrency**：update 接受 `precondition: {type: "content_sha256", value}`，mismatch → `memory_precondition_failed_error` HTTP 409
- **`view` query**：`basic` | `full` 控制返回详细程度
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header
- **三个 Memory 概念区分**：
  - **[[Memory]]** —— Claude Code（CLAUDE.md / auto-memory，本地）
  - **[[Memory-tool]]** —— Anthropic API tool（client-side `/memories` 目录）
  - **Memory-store** —— Anthropic API beta resource（server-managed 持久存储）

## 出现来源

_23 summaries reference this entity_ ——
- [[memory_stores-index--beta-api]] / [[memory_stores-create--beta-api]] / [[memory_stores-list--beta-api]] / [[memory_stores-retrieve--beta-api]] / [[memory_stores-update--beta-api]] / [[memory_stores-delete--beta-api]] / [[memory_stores-archive--beta-api]]
- [[memory_stores-memories-index--beta-api]] / [[memory_stores-memories-create--beta-api]] / [[memory_stores-memories-list--beta-api]] / [[memory_stores-memories-retrieve--beta-api]] / [[memory_stores-memories-update--beta-api]] / [[memory_stores-memories-delete--beta-api]]
- [[memory_stores-memory_versions-index--beta-api]] / [[memory_stores-memory_versions-list--beta-api]] / [[memory_stores-memory_versions-retrieve--beta-api]] / [[memory_stores-memory_versions-redact--beta-api]]
- [[memory--ma]]

## 相关

- [[Memory]] —— Claude Code memory（不同 product）
- [[Memory-tool]] —— API tool（client-side `/memories` 目录）
- [[Managed-agent]] / [[Session-API]] —— 用 memory store 作 persistent state
