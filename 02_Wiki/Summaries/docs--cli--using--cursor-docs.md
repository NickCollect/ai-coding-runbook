---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--using.md
source_url: https://cursor.com/docs/cli/using
title: "Using Agent in CLI"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

CLI 中使用 Agent 的详细操作指南，支持与编辑器相同的模式系统和规则系统。

**模式切换**：Shift+Tab 循环切换 Agent/Plan/Ask 模式；或用 `/plan`、`/ask` slash 命令；`--mode` flag 启动时指定。

**输入快捷键**：Shift+Enter（插入换行）、Ctrl+D（退出）、Ctrl+J 或 Enter（通用换行，兼容 tmux）；↑键循环历史消息；Ctrl+R 审查变更（i 追加指令，方向键滚动/切换文件）。

**上下文选择**：用 `@` 选择文件/文件夹；`/compress` 释放上下文窗口空间。

**MCP 和 Rules**：自动检测 `mcp.json` 配置；自动加载 `.cursor/rules/`、`AGENTS.md`、`CLAUDE.md` 规则。

**Worktrees**：`--worktree` flag 让 Agent 在独立 Git checkout 中运行（保存于 `~/.cursor/worktrees`），结合 `--workspace <path>` 可指定项目根目录。

**历史会话**：`agent ls` 查看所有历史；`agent resume`/`--continue`/`--resume=id` 恢复对话。

**云端交接**：消息前加 `&` 推送到 Cloud Agent 在云端持续运行。

**非交互模式**：`-p/--print` flag，支持 `--output-format` 控制输出格式（text/json）。
