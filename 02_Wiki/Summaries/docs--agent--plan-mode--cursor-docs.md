---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--plan-mode.md
source_url: https://cursor.com/docs/agent/plan-mode
title: "Plan Mode"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Plan Mode 在写代码前先生成可审查的实施方案，适合需要先规划再执行的复杂任务。

**切换方式**：在 chat 输入框按 Shift+Tab 轮换到 Plan Mode；或通过 Agent 顶部的模式下拉框切换。输入复杂任务关键词时 Cursor 也会自动建议启用。

**工作流程**：
1. Agent 提出澄清问题
2. 调研代码库获取上下文
3. 生成完整实施方案
4. 用户通过 chat 或 markdown 文件审查/编辑方案
5. 确认后点击执行

**方案保存**：默认保存在 home 目录；可点击"Save to workspace"移入项目，便于团队共享和文档归档。

**适用场景**：多文件复杂功能、需探索后才清楚范围的任务、架构决策需提前审批。简单或熟悉的改动直接用 Agent Mode 更快。

**最佳实践**：如果 Agent 执行结果偏离预期，回退变更、细化方案后重跑，通常比反复追加修复更高效。
