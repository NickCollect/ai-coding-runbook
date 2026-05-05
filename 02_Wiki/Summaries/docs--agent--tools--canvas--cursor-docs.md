---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--tools--canvas.md
source_url: https://cursor.com/docs/agent/tools/canvas
title: "Canvases（交互式画布）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Canvas 是 Cursor 创建的交互式制品，在 chat 旁渲染为独立视图（仪表板、分析报告、审计等），替代冗长的 markdown 表格或代码块。

**工作流程**：Cursor 判断任务适合可视化展示 → 构建 canvas 并在 chat 中插入引用 → 用户审查或要求修改 → canvas 自动保存可随时重新打开。

**打开方式**：chat 底部的 canvas 卡片点击；Command Palette → Open Canvas；Agents Window 的新标签菜单。

**迭代**：直接告诉 Cursor 要改什么（比手动编辑更快）；要求重新运行底层查询；大改动建议回退后重新描述；小调整可直接编辑源码。

**与 Skills 结合**：常用 canvas 工作流可打包为 Skill，包含触发描述、布局说明、数据源/查询、格式规则，确保每次同样的提示生成一致结构的 canvas。
