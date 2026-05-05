---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--compliance-and-monitoring.md
source_url: https://cursor.com/docs/enterprise/compliance-and-monitoring
title: "Enterprise 合规与监控"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Enterprise 提供审计日志、AI 代码追踪、SOC 2 认证等合规能力，支持流式传输到现有 SIEM 系统。

**审计日志**（Enterprise 专属）：记录认证事件（登录/登出）、用户管理（增删/角色变更/花费上限）、API Key 管理、团队设置、仓库管理、目录组、Privacy Mode 变更、Team Rules/Commands 管理。**不记录** Agent 响应或生成的代码内容（建议用 Hooks 记录提示词和代码）。

**日志访问**：Dashboard → Audit Log（需管理员权限）；支持按日期范围/事件类型/操作者筛选，可导出 CSV。

**流式传输**：可接入 SIEM（Splunk/Sumo Logic/Datadog 等）、Webhook 自定义处理、S3 长期保留、Elasticsearch/CloudWatch；联系 hi@cursor.com 申请流式日志。

**日志格式**：JSON，含 metadata（timestamp/event_id）、team_id、ip_address、user_email 和事件字段；支持 20+ 事件类型。

**Hooks 合规日志**：用 `beforeSubmitPrompt` Hook 记录谁/何时提交 prompt，用 `afterFileEdit` Hook 记录代码生成事件（记录元数据而非内容，避免敏感信息泄露）。

**认证**：SOC 2 Type II、GDPR 合规；Trust Center 提供完整合规文档。漏洞披露：发邮件至 security-reports@cursor.com。
