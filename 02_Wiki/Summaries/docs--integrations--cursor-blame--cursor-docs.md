---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--cursor-blame.md
source_url: https://cursor.com/docs/integrations/cursor-blame
title: "Cursor Blame（AI 代码归因）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor Blame 将传统 git blame 扩展为 AI 归因视图，显示每行代码是由 Tab 补全、Agent 还是人工编写的，Enterprise 专属功能。

**三种归因类型**：Tab（Tab 建议生成/接受）、Agent（Agent 生成，含模型归因）、Human（开发者直接编写）。

**查看方式**：
- **行注释**：Cmd+Shift+P → "Cursor Blame: Toggle editor decorations"，内联 ghost text 显示作者/提交信息/时间；悬停显示 AI 共同作者标识和对话摘要；点击查看完整提交贡献分解（各模型 + 人工占比百分比）
- **文件 blame 视图**：右键 → Cursor Blame > Toggle file blame，或 Cmd+Shift+P → "Cursor Blame: Open File Blame"

**数据获取**：归因数据本地缓存，查看文件/提交时从 Cursor 服务器拉取；对话摘要按需获取，仅显示简短描述而非完整历史。

**启用方式**：团队级默认关闭，管理员在 Team settings 中为所有成员启用。

**要求**：Enterprise 计划 + 有 Cursor 追踪变更的 Git 仓库。
