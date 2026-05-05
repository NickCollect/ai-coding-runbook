---
type: entity
name: Workspace
aliases: [workspaces / org workspace]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic 组织内的 sub-unit —— 隔离 API key、rate limit、cost、files、batch。

## 关键属性

- **Endpoints** under `/v1/organizations/workspaces`：Create / Retrieve / List / Update / Archive [[workspaces--admin-api]]
- **Workspace shape**：`id` / `type: "workspace"` / `name` / `display_color`（hex）/ `data_residency` / `created_at` / `archived_at` [[workspaces--admin-api]]
- **`data_residency`**：
  - `workspace_geo`（**immutable** after creation, default `"us"`）
  - `allowed_inference_geos`（default `"unrestricted"`）
  - `default_inference_geo`（default `"global"`） [[workspaces--admin-api]]
- **Update 限制**：可改 `name` 和 `data_residency` (geo)，**不可改 `workspace_geo`** [[workspaces--admin-api]]
- **List filter**：`include_archived: bool`
- **Members 子资源** (`/{workspace_id}/members`)：
  - Create / Retrieve / List / Update / Delete
  - `workspace_role`：`workspace_user` / `workspace_developer` / `workspace_restricted_developer` / `workspace_admin`（read enum 还含 `workspace_billing`，不可 create 时 assign）
  - `WorkspaceMember` shape：`type: "workspace_member"` / `user_id` / `workspace_id` / `workspace_role`
  - Delete 返回 `MemberDeleteResponse` with `type: "workspace_member_deleted"` [[workspaces--admin-api]]
- **Workspace Rate Limit** sub：`GET .../{workspace_id}/rate_limits` —— 列 per-workspace overrides（仅有 override 的 group 出现，其他 inherit org 不列；用 `/v1/organizations/rate_limits` 看 org 级） [[workspaces--admin-api]] [[Rate-limit-API]]
- **Auth**：`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`
- **关联**：[[API-key]]、[[Files-API]]、[[Batches-API]]、[[Code-execution-tool]] container 都按 workspace scope

## 出现来源

_47 summaries reference this entity_ ——
- [[workspaces--admin-api]] / [[workspaces-create--admin-api]] / [[workspaces-list--admin-api]] / [[workspaces-retrieve--admin-api]] / [[workspaces-update--admin-api]] / [[workspaces-archive--admin-api]]
- [[workspaces-members--admin-api]] / [[workspaces-members-create--admin-api]] / [[workspaces-members-list--admin-api]] / [[workspaces-members-retrieve--admin-api]] / [[workspaces-members-update--admin-api]] / [[workspaces-members-delete--admin-api]]
- [[workspaces-rate_limits-list--admin-api]]
- [[admin--api-index]] / [[administration-api--bwc]] / [[workspaces--bwc]]
- [[batch-processing--bwc]] / [[code-execution-tool--at]] / [[files--bwc]]

## 相关

- [[Admin-API]] —— Workspace 是 admin 资源
- [[API-key]] / [[Files-API]] / [[Batches-API]] —— 按 workspace scope
- [[Rate-limit-API]] —— per-workspace override
- [[Cost-report]] / [[Usage-report]] —— 按 workspace group
