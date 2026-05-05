---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--members.md
source_url: https://cursor.com/docs/account/teams/members
title: "Members & Roles"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor 团队支持三种角色，计费按活跃用户（而非预分配席位），可随时增减。

**角色**：
- **Member**（默认）：使用 Pro 功能，无 admin dashboard 和计费访问权
- **Admin**：管理成员/角色/SSO、配置费用上限、访问团队分析
- **Unpaid Admin**：无付费席位的管理员（适合 IT/财务人员），有全部管理权限但无 Pro 功能

**成员管理**：邀请方式包括邮件、邀请链接、SSO 自动入组、域名匹配（相同邮件域自助加入）。移除成员：若已使用额度则席位保留至账期结束，移除后数据（含 Memories 和 Cloud Agent 数据）永久删除。

**域名设置**：Domain matching（启用后同域成员可自助加入，无需邀请）；Restrict invites to verified domains（限制只能邀请已验证域名用户）。仅对未使用 SCIM 的团队有效。

**计费**：按日比例计算新成员费用；移除有信用额度的成员，席位保留至账期结束不退款；角色变更从变更日调整计费。年付比月付省 20%。
