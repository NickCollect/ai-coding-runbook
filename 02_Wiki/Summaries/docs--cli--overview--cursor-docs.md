---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--overview.md
source_url: https://cursor.com/docs/cli/overview
title: "Cursor CLI 概述"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI 提供在终端中直接与 AI Agent 交互的能力，支持交互模式、脚本自动化和 CI 管道，命令名为 `agent`。

**安装**：`curl https://cursor.com/install -fsS | bash`（macOS/Linux/WSL）；PowerShell 命令适用于 Windows 原生。

**三种模式**：Agent（默认，全工具访问）、Plan（Shift+Tab 或 `--mode=plan`，先规划再执行）、Ask（`--mode=ask`，只读探索）。可通过 slash commands、快捷键或 `--mode` flag 切换。

**交互模式**：`agent` 或 `agent "任务描述"` 启动对话会话，可描述目标、审查变更、批准命令。

**非交互模式**：`-p/--print` flag 用于脚本/CI 管道，输出格式支持 `text`（默认）、`json`、`stream-json`。

**云端交接**：在消息前加 `&` 将任务推送到 Cloud Agent 继续运行，可在 cursor.com/agents 查看。

**会话管理**：`agent ls` 列出历史会话；`agent resume`/`--continue`/`--resume=id` 恢复特定对话保持上下文。

**其他功能**：沙盒控制（`/sandbox` 或 `--sandbox`）、Max Mode 开关（`/max-mode`）、sudo 密码安全提示（密码不暴露给 AI 模型）。
