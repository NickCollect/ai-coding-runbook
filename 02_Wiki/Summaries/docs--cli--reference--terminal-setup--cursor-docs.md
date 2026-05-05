---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--reference--terminal-setup.md
source_url: https://cursor.com/docs/cli/reference/terminal-setup
title: "CLI 终端配置"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

配置终端以获得最佳 Cursor CLI 体验，涵盖多行输入、Vim 模式和主题同步。

**多行输入**（换行键）：
- **通用方法（所有终端含 tmux）**：`\`+Enter 或 Ctrl+J（最可靠）
- **Shift+Enter 原生支持**：iTerm2、Ghostty、Kitty、Warp、Zed
- **需 `/setup-terminal` 配置 Option+Enter**：Apple Terminal、Alacritty、VS Code 集成终端
- **tmux/screen**：Shift+Enter 被拦截，只能用 Ctrl+J 或 `\`+Enter

**Vim 模式**：`/vim` 切换；或在 `~/.cursor/cli-config.json` 设置 `"editor.vimMode": true`。支持 Normal/Insert 双模式、标准 hjkl 导航和编辑命令，仅作用于输入区域。

**主题自动检测**：CLI 查询终端背景色自动切换深色/浅色主题；大多数现代终端支持；不支持时通过 `COLORFGBG="15;0"`（深色）或 `"0;15"`（浅色）强制设置。

**手动键位配置**：可为各终端（iTerm2/Alacritty/Kitty/VS Code）手动配置 Option+Enter 发送 `\x1b\r` 转义序列。
