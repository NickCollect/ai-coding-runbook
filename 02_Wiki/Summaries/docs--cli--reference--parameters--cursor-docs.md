---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--parameters.md
source_url: https://cursor.com/docs/cli/reference/parameters
title: "CLI 参数参考"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI 完整参数和命令参考。

**常用全局选项**：`-p/--print`（非交互 print 模式）、`--output-format text|json|stream-json`、`--model`、`--mode plan|ask`、`-f/--force/--yolo`（强制允许命令）、`--sandbox enabled|disabled`、`--worktree`（新 Git worktree 运行）、`--resume/--continue`（恢复会话）、`--approve-mcps`（自动批准所有 MCP）、`--workspace <path>`。

**命令列表**：`login`/`logout`/`status`（认证）、`models`（列出可用模型）、`mcp`（管理 MCP 服务器）、`ls`（列出历史会话）、`resume`（恢复最近会话）、`update`（更新 CLI）、`generate-rule`（交互式生成 Rule）、`install-shell-integration`/`uninstall-shell-integration`（Shell 集成）、`acp`（ACP 服务器模式，高级隐藏命令）。

**MCP 子命令**：`mcp login`、`mcp list`、`mcp list-tools <id>`、`mcp enable/disable <id>`。

无命令时默认进入交互式 Agent 模式；可在命令后跟初始 prompt 参数。
