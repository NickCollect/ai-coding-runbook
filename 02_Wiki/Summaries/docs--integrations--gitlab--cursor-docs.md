---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--gitlab.md
source_url: https://cursor.com/docs/integrations/gitlab
title: "GitLab 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

GitLab 集成连接仓库支持 Cloud Agents 和 Bugbot；需要 GitLab Premium 或 Ultimate 计划（Free 不支持项目访问令牌）。

**GitLab.com 设置**：Dashboard → Integrations → Connect GitLab → 完成安装流程 → Manage → Sync Repos。

**GitLab Self-Hosted**：需要 Cursor Teams 或 Enterprise 计划；在 GitLab 实例创建应用（Instance 级别，Trusted/Confidential，Scopes: api + write_repository，Redirect URI: `https://cursor.com/gitlab-connected`）→ 在 Cursor Dashboard → Advanced → GitLab Self-Hosted 注册（填 hostname、Application ID、Secret）→ 完成连接并 Sync Repos。

**IP 白名单**：同 GitHub，添加 3 个代理 IP（184.73.225.134、3.209.66.12、52.44.113.131）。

**高级网络**（Enterprise 专属）：PrivateLink（AWS/GCP 私有网络）或 Reverse Proxy Tunnel（无入站访问）。

连接后在 dashboard 配置各仓库的 Bugbot 和 Cloud Agents。
