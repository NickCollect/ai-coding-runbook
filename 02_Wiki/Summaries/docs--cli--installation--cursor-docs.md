---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--installation.md
source_url: https://cursor.com/docs/cli/installation
title: "CLI 安装"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor CLI 的安装说明，安装后命令为 `agent`，支持自动更新。

**安装命令**：macOS/Linux/WSL：`curl https://cursor.com/install -fsS | bash`；Windows PowerShell：`irm 'https://cursor.com/install?win32=true' | iex`。

**安装后配置**：将 `~/.local/bin` 添加到 `$PATH`（bash 写 `~/.bashrc`，zsh 写 `~/.zshrc`），然后重新加载配置文件。

**验证**：`agent --version`。

**更新**：默认自动更新；手动更新：`agent update`。
