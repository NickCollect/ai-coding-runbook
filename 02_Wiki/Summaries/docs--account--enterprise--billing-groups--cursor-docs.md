---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--enterprise--billing-groups.md
source_url: https://cursor.com/docs/account/enterprise/billing-groups
title: "Billing Groups（Enterprise 费用分组）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Enterprise 专属功能，允许管理员按用户组追踪和管理费用，适用于部门报告、内部成本分摊和预算管控。

**架构**：每个成员只能属于一个费用分组；未分配成员自动归入保留的 `Unassigned` 组；历史数据按用量发生时所在组归因，组删除后历史数据移至 Unassigned 组。

**成员分配方式**：SCIM 同步（与 IdP 目录组绑定）、Admin API（编程式）、CSV 上传、手动选择。SCIM 同步的分组不可通过 CSV/API/UI 手动修改。

**管理**：可重命名（gear 按钮或 Rename）、删除（不可恢复，历史数据移至 Unassigned）、通过 Admin API 编程管理。在 Members & Groups 标签页的 web dashboard 查看各组成员数量和期间费用。
