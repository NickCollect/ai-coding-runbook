---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--security.md
source_url: https://cursor.com/docs/agent/security
title: "Agent Security"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor Agent 通过多层防护机制应对 prompt injection、幻觉等 AI 风险，敏感操作默认需用户手动批准。

**第一方工具调用**：读取文件/搜索代码无需审批；工作区文件可直接修改（立即写入磁盘）；配置文件修改需审批；终端命令默认需审批。可通过 `.cursorignore` 阻止 Agent 访问特定文件。**警告**：开启自动重载时，Agent 修改可能在审查前就生效。

**白名单**：可对特定终端命令或 MCP 工具设置自动审批，但属于尽力保护而非安全保证——绕过是可能的。绝不使用"Run Everything"模式（跳过所有安全检查）。

**第三方工具（MCP）**：所有 MCP 连接需先审批；每次工具调用仍需单独审批；可通过 MCP 白名单预授权特定工具。

**网络请求**：Agent 默认只能访问 GitHub、直链检索和 Web 搜索服务商，无法发送任意网络请求。

**工作区信任**：默认禁用，启用后对新工作区提示选择普通/受限模式；受限模式会禁用 AI 功能。

**漏洞披露**：发现安全漏洞请发邮件至 security-reports@cursor.com，5 个工作日内确认，严重事故通过邮件通知所有用户。
