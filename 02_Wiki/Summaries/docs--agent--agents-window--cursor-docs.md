---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--agents-window.md
source_url: https://cursor.com/docs/agent/agents-window
title: "Agents Window"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agents Window 是 Cursor 以 Agent 为核心的统一工作界面，支持跨 repo 和跨环境（本地/云端/远程 SSH）管理多个 Agent，于 Cursor 3（2026-04-02）正式发布。

**打开方式**：Cmd+Shift+P → Open Agents Window；返回经典编辑器：Cmd+Shift+P → Open Editor Window。可同时开启两个界面。

**独有功能**（编辑器不具备）：
- **多工作区**：在一处管理所有项目
- **新 Diffs 视图**：直接在 Cursor 内审查、提交变更和管理 PR
- **并行 Agents**：同时运行多个云端 Agent，支持手机/Web/Slack/GitHub/Linear 接入
- **本地↔云端切换**：快速将 Agent 从云端拉到本地迭代，再推回云端
- **Worktrees**：每个任务在独立 Git checkout 中运行，文件互不干扰

**选用场景**：需要并行管理多个 Agent、希望提升到更高抽象层级时用 Agents Window；需要 VS Code 插件、灵活多窗格查看文件时用经典编辑器。
