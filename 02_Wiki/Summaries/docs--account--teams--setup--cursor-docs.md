---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--setup.md
source_url: https://cursor.com/docs/account/teams/setup
title: "Teams 入门设置"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor Teams 计划的创建和基础配置指南，支持 SSO、团队管理、访问控制和使用分析。

**创建团队**：新用户访问 cursor.com/team/new-team；现有用户在 dashboard 点击"Upgrade to Teams"。选择团队名和计费周期，邀请成员（按日比例计费），可选启用 SSO。

**域名匹配**：在 team settings 开启后，相同邮件域的同事无需邀请即可自助加入。

**代理/VPN 兼容**：Cursor 默认使用 HTTP/2，部分代理/VPN 会拦截；如有问题，在 Cursor Settings > Network 将 HTTP Compatibility Mode 设为 HTTP/1.1。

**MDM 部署**：cursor.com/downloads 提供所有平台下载链接，支持 Omnissa Workspace ONE、Microsoft Intune（Windows/Mac）、Kandji MDM。

**账号限制**：一个 Cursor 账号只能同时属于一个团队；需要切换团队须先退出当前团队。

**管理员创建团队**：可先设自己为 Unpaid Admin，邀请第一个付费成员，再变更角色，避免产生额外席位费用。
