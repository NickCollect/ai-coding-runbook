---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--automations.md
source_url: https://cursor.com/docs/cloud-agent/automations
title: "Automations（自动化）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Automations 通过触发器（定时或事件驱动）在后台自动运行 Cloud Agent，支持代码维护、漏洞扫描、Bug 分类、Sentry 调查等场景。

**触发器类型**：
- **Scheduled**：定时（预设选项或 cron 表达式）
- **GitHub**：PR 开启/推送/标签变更/合并/评论/CI 完成/分支推送
- **Slack**：频道新消息/频道创建（仅公开频道）
- **Webhook**：私有 HTTP 端点，POST 触发，支持与内部系统集成
- **Linear**：Issue 创建/状态变更/Cycle 结束
- **Sentry**：Issue 创建/更新/任意事件
- **PagerDuty**：Incident 触发/确认/解决/任意事件

**可用工具**：Open PR、Comment on PR（含审查批准功能）、Request Reviewers、Send to Slack、Read Slack channels、MCP Server、Memories（跨运行持久化笔记，默认开启）。

**权限作用域**：
- Private：仅创建者管理，费用计入创建者
- Team Visible：团队成员可查看，仍用创建者身份执行
- Team Owned：管理员管理，以团队共享服务账户执行，费用计入团队

**计费**：按 Cloud Agent 用量收费，用量归属由权限作用域决定。

**Memories 注意事项**：持久化 notes 跨运行保留，处理不可信输入时需谨慎（可能写入恶意记忆影响后续运行）。
