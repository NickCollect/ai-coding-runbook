---
type: summary
source: 01_Raw/docs.cursor.com/docs--security-review.md
source_url: https://cursor.com/docs/security-review
title: "Security Review（安全审查）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Security Review 是 Teams/Enterprise 专属的安全扫描功能，通过 Automations 平台上的 Cloud Agent 发现代码中的安全漏洞和风险模式。

**两种 Agent 类型**：
- **Security Review**：在 PR 合并前扫描，用于代码审查阶段捕获漏洞（Git-based 触发器，如 PR 事件）
- **Vulnerability Scanner**：扫描静态代码库，发现已有漏洞和长期遗留问题（Cron 定时触发器）

**配置**：在 Security Review Dashboard 创建 Agent → 配置触发器 → 启用/禁用内置安全检查项 → 添加自定义指令 → 配置工具/MCP（连接 Slack、Issue Tracker 等用于输出漏洞报告，每个 Agent 至少需要一个工具/MCP）。

**环境**：默认使用 Cursor 云端，也支持自托管 Cloud Agents。

**计费**：按团队用量池计费，以共享团队服务账号运行，不影响个人用量。

**指标**：Vulnerabilities found（发现数）、Issues fixed（修复数）、Resolution rate（修复率，用 LLM 分析增量 diff 判断是否已修复）。

**查看运行**：Dashboard 记录每次运行的工具使用、状态和耗时，可点入查看底层 Cloud Agent 详情。
