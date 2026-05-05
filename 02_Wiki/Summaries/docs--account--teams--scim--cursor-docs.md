---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--scim.md
source_url: https://cursor.com/docs/account/teams/scim
title: "SCIM（自动用户供应）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

SCIM 2.0 自动通过身份提供商（IdP）管理 Cursor 团队成员和目录组，Enterprise 专属，需先配置 SSO。

**工作方式**：IdP 中分配用户 → 自动加入 Cursor；取消分配 → 自动移除；目录组及成员同步从 IdP 实时推送；Cursor 中组信息只读，所有管理在 IdP 侧操作。

**费用管理**：可为每个目录组设置不同的用户级花费上限；多组用户取最高适用上限；组级上限优先于团队默认上限。

**配置步骤**：确保 SSO 已配置 → Dashboard → Members & Groups → Directory Groups → 按向导生成 SCIM endpoint 和 token → 在 IdP 中配置 SCIM 应用（启用用户和 push group 供应）→ 可选：为各组设置花费上限。

**注意**：启用 SCIM 时现有用户不会自动移除；已供应账号需用户首次登录后才显示在 Members dashboard；SCIM 不支持角色映射，所有用户以 Member 角色供应，角色变更需在 Cursor dashboard 手动操作。
