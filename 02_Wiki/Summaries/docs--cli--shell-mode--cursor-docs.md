---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--shell-mode.md
source_url: https://cursor.com/docs/cli/shell-mode
title: "Shell Mode"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Shell Mode 允许在 CLI 对话中直接执行 Shell 命令，无需离开当前会话，适合快速状态检查、文件操作和环境查看。

**执行环境**：在登录 shell（`$SHELL`）中以 CLI 工作目录运行；使用 `cd subdir && cmd` 在其他目录执行（`cd` 不持久化）。

**限制**：命令超时 30 秒（不可配置）；不支持长时运行的服务、交互式应用和需要输入的命令；大输出自动截断。

**权限**：执行前检查 permissions 和团队设置；某些命令可能被管理员策略阻止；含重定向的命令无法内联添加到白名单。

**故障排查**：命令卡住用 Ctrl+C 中断并添加非交互 flag；Ctrl+O 展开截断输出；权限提示时用 Tab 添加到白名单。

**退出 Shell Mode**：输入框为空时按 Escape、Backspace/Delete 或 Ctrl+C。
