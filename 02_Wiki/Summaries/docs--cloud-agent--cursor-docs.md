---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent.md
source_url: https://cursor.com/docs/cloud-agent
title: "Cloud Agents 概述"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agents 在云端隔离 VM 中运行，无需本地机器保持联网，可无限并行启动，具备完整虚拟机访问权限（可构建、测试、控制桌面和浏览器）。

**接入方式**：Cursor Web（cursor.com/agents，支持 PWA 安装到手机）、Cursor Desktop（Agent 输入框下拉选 Cloud）、Slack（@cursor 命令）、GitHub（PR/Issue 评论 @cursor）、Linear（@cursor 命令）、API。

**工作原理**：从 GitHub 或 GitLab 克隆仓库，在独立分支工作，推送 PR 完成交接。需要对 repo 及子模块有读写权限。

**模型**：使用精选模型，全程运行在 Max Mode（不可关闭）。

**MCP 支持**：可使用团队配置的 MCP 服务器（HTTP 和 stdio 传输均支持，支持 OAuth）。

**Hooks 支持**：运行项目 `.cursor/hooks.json` 中的 Project Hooks；Enterprise 计划还支持 Team Hooks 和 Enterprise 统一管理 Hooks。

**计费**：按所选模型 API 价格收费，首次使用需设置花费上限。需付费 Cursor 计划。

**前称**：Cloud Agents 原名 Background Agents。
