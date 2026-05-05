---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--baa.md
source_url: https://cursor.com/docs/enterprise/baa
title: "HIPAA BAA（商业合作协议）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor Enterprise 支持 HIPAA Business Associate Agreements（BAA），允许医疗行业组织在合规场景下使用 Cursor 处理 PHI（受保护健康信息）。

**申请方式**：联系销售 → 说明需要 HIPAA BAA → 注明当前计划（评估中/Teams 升级/已在 Enterprise）。仅 Enterprise 计划可申请，Teams 计划不支持。

**使用 PHI 前的必要步骤**：签署 Enterprise 协议和 BAA → 查阅 Trust Center 中的 HIPAA 实施配置指南 → 组织级开启并锁定 Privacy Mode → 培训用户只通过 Eligible Services 和批准的工作流提交 PHI。

**Eligible Services（BAA 覆盖范围，需 Privacy Mode 启用并锁定）**：Desktop IDE（Agent/Tab/Edit/本地 agent 模式/内联编辑）、Cloud Agents、自托管 Cloud Agents、CLI、Tab、BugBot、Automations。

**重要限制**：BAA 不自动覆盖所有配置和工作流；第三方服务/集成不在 BAA 覆盖范围内；PHI 未经 BAA 签署不得提交。
