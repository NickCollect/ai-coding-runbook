---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--github.md
source_url: https://cursor.com/docs/integrations/github
title: "GitHub 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor GitHub App 连接仓库，支持 Cloud Agents 和 Bugbot 功能；支持 GitHub.com 和 GitHub Enterprise Server（v3.8+）。

**GitHub.com 设置**：Dashboard → Integrations → Connect GitHub → 选择所有或指定仓库。

**GitHub Enterprise Server**：需 Cursor Enterprise 计划，通过 Dashboard → Advanced → GitHub Enterprise Server 注册；需提供 GHES 实例 base URL 和组织名。IP 白名单：添加 3 个固定代理 IP（184.73.225.134、3.209.66.12、52.44.113.131）或在 GitHub 组织安全设置中启用"Allow access by GitHub Apps"（推荐，自动同步 Cursor 维护的 IP 列表）。

**高级网络连接**（Enterprise 专属）：
- **PrivateLink/Private Service Connect**：适合 AWS/GCP 私有网络防火墙后的实例
- **Reverse Proxy Tunnel**：无入站访问的环境，在本地运行隧道进程

**权限**：Repository access（克隆/创建分支）、Pull requests（创建 PR/评审）、Issues、Checks and statuses、Actions and workflows。最小权限原则。

**启用功能**：连接后在 dashboard 配置各仓库的 Bugbot 和 Cloud Agents。
