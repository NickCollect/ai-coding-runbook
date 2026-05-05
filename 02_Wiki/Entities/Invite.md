---
type: entity
name: Invite
aliases: [invites / org invitations / workspace invites]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Admin API 管理 org member 邀请 —— `/v1/organizations/invites`。

## 关键属性

- **Endpoints**：Create / Retrieve / List / Delete [[invites--admin-api]] [[admin--api-index]]
- **Auth**：`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`
- **Invitee role**：`user` / `developer` / `billing` / `claude_code_user` —— **不可 invite 为 `admin`** [[admin--api-index]]
- **Status**：`accepted` / `expired` / `deleted` / `pending`
- **Pagination**：cursor (`after_id` / `before_id` / `limit`)
- **配套**：admin Users API（用户接受 invite 后用 Users API 管 role） / Workspace Members API（workspace-scoped role 单独管）

## 出现来源

_15 summaries reference this entity_ ——
- [[invites--admin-api]] / [[invites-create--admin-api]] / [[invites-list--admin-api]] / [[invites-retrieve--admin-api]] / [[invites-delete--admin-api]]
- [[admin--api-index]] / [[administration-api--bwc]] / [[admin-setup]]

## 相关

- [[Admin-API]] / [[Workspace]] —— workspace member roles 是不同维度
