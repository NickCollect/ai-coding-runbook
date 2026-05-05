---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--security-network.md
source_url: https://cursor.com/docs/cloud-agent/security-network
title: "Cloud Agent 安全与网络"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agent 支持 Privacy Mode（零数据保留）；密钥加密传输，可设为 Redacted 模式防止意外提交到版本控制或暴露给模型。

**Signed Commits**：Cloud Agent 每次提交使用 HSM 支持的 Ed25519 密钥签名，在 GitHub/GitLab 上显示 "Verified" 徽章，无需额外配置，自动满足分支保护规则要求。

**安全注意事项**：
- 代码在 AWS 隔离 VM 上运行，仅在 Agent 会话期间存储在 VM 磁盘
- Agent 默认有互联网访问（可配置网络出口控制限制域名）
- Auto-run 所有终端命令（与前台 Agent 不同），存在 prompt injection 数据泄露风险（参考 OpenAI 说明）
- 若 Privacy Mode 关闭，会收集 prompts 和开发环境用于产品改进

**网络访问三种模式**：Allow all（无限制）、Default + allowlist（默认域名 + 自定义）、Allowlist only（仅白名单）。用户设置优先于团队默认；Enterprise 可锁定设置阻止用户覆盖。

**出口 IP**：通过 `https://cursor.com/docs/ips.json` API 获取，含 cloudAgents（各集群 CIDR）和 gitEgressProxy IP；IP 可能变化，不推荐作为主要安全机制。

**Git 出口代理**：IP 白名单场景可用专用代理（3 个固定 IP），路由所有 git 流量，适用于 GitHub/GitLab。
