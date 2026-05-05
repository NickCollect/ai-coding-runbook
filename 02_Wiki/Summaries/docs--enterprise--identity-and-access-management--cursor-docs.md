---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--identity-and-access-management.md
source_url: https://cursor.com/docs/enterprise/identity-and-access-management
title: "Enterprise 身份与访问管理"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

企业身份与访问管理控制组织内谁能使用 Cursor 及其权限，建议按 SSO → SCIM → MDM 策略 → 角色分配的顺序部署。

**SSO/SAML**：通过 Okta/Azure AD/Google Workspace/OneLogin 等 IdP 认证，可强制要求所有成员使用 SSO 禁止密码登录。

**SCIM**：Enterprise + SSO 前提下，自动管理成员生命周期（入职自动添加、离职自动移除、组变更实时同步）。

**MDM 策略**：
- **AllowedTeamId**：防止员工在企业设备上登录个人 Cursor 账号（填入企业 Team ID，非白名单账号立即强制登出）
- **AllowedExtensions**：控制可安装的扩展（按发布者或完整扩展 ID 配置）；Cursor 2.1+ 客户端生效
- **Workspace Trust**：`security.workspace.trust.enabled` 控制工作区信任提示
- 所有 MDM 策略都会覆盖用户设置

**.cursor 目录**：包含项目设置、索引缓存和规则，可提交到版本控制；不要在 Rules 文件中放置敏感信息。企业可通过 Dashboard 防止 Agent 修改此目录。
