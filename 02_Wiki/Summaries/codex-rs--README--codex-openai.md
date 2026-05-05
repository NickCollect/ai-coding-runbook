---
type: summary
source: 01_Raw/github/openai/codex/codex-rs/README.md
source_url: https://github.com/openai/codex/blob/main/codex-rs/README.md
title: "Codex CLI Rust 实现 README"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Codex CLI 的 Rust 实现是当前维护的主版本（替代早期 TypeScript 版本），提供零依赖独立可执行文件。

**安装方式**：npm（`npm i -g @openai/codex`）、Homebrew（`brew install --cask codex`）或从 GitHub Releases 下载平台包。

**配置**：使用 `config.toml`（而非旧版 `config.json`），支持丰富配置选项，详见 docs/config.md。

**MCP 支持**：
- **MCP 客户端**：Codex CLI 启动时可连接外部 MCP 服务器。
- **MCP 服务端（实验性）**：运行 `codex mcp-server` 可将 Codex 作为 MCP server，供其他 MCP 客户端调用；可用 `npx @modelcontextprotocol/inspector codex mcp-server` 测试；`codex mcp` 子命令管理 config.toml 中的 MCP 服务端配置。

**非交互模式**：`codex exec PROMPT` 无 UI 运行直到任务完成退出；支持 stdin 管道；`--ephemeral` 跳过会话文件持久化。

**沙箱策略**：`--sandbox`（`-s`）标志可选 `read-only`、`workspace-write`、`danger-full-access`；也可在 `config.toml` 中持久化设置；`workspace-write` 模式下 `~/.codex/memories` 自动加入可写根路径。

**代码组织**（Cargo workspace in `codex-rs/`）：
- `core/`：核心业务逻辑
- `exec/`：无头 CLI（自动化用）
- `tui/`：基于 Ratatui 的全屏 TUI
- `cli/`：整合以上子命令的多工具 CLI 入口

**通知**：旧 `notify` 配置已废弃，建议改用 lifecycle hooks；WSL 2 环境自动回退 Windows toast 通知。
