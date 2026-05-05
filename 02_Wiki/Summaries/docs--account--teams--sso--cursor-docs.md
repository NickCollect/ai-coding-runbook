---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--sso.md
source_url: https://cursor.com/docs/account/teams/sso
title: "SSO（单点登录）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

SAML 2.0 SSO 在 Teams 和 Enterprise 计划上免费提供，通过现有 IdP 认证成员，无需单独 Cursor 账号。

**前提条件**：Cursor Teams 计划；对 IdP（如 Okta）和 Cursor 组织有管理员权限。

**配置步骤**：Dashboard Settings → SSO Provider Connection settings → 按向导配置 → 在 IdP 中创建 SAML 应用并配置（含 JIT 供应）→ 验证域名（Domain verification settings）。

**多域名支持**：每个域名独立验证，在 IdP 中单独配置，验证流程各自独立完成。

**特性**：新用户通过 SSO 登录时自动注册加入；可在 admin dashboard 强制 SSO 执行。

**常见问题排查**：确认域名已验证；检查 SAML 属性映射正确；确认 SSO 在 admin dashboard 中已启用；IdP 和 Cursor 中的姓名需匹配。
