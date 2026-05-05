---
type: summary
source: 01_Raw/github/openai/codex/docs/install.md
source_url: https://github.com/openai/codex/blob/main/docs/install.md
title: "Codex CLI 安装与构建指南"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Codex CLI 的系统要求、从源码构建流程及日志调试说明。

**系统要求**：macOS 12+、Ubuntu 20.04+/Debian 10+、或 Windows 11（WSL2）；Git 2.23+ 可选但推荐；最低 4GB RAM（推荐 8GB）。

**DotSlash 支持**：GitHub Release 包含一个 DotSlash 文件 `codex`，可提交到版本控制确保所有贡献者使用同一可执行版本。

**从源码构建**：克隆仓库后进入 `codex-rs/` 目录；安装 Rust toolchain（rustup）及 `rustfmt`、`clippy`、`just`、可选 `cargo-nextest`；执行 `cargo build` 构建，`cargo run --bin codex -- "PROMPT"` 运行；改动后用 `just fmt` 格式化、`just fix -p <crate>` 修复 lint。

**日志与调试**：Codex 遵循 `RUST_LOG` 环境变量控制日志级别；TUI 模式默认写入 `~/.codex/log/codex-tui.log`，可用 `-c log_dir=...` 覆盖；非交互模式（`codex exec`）默认 `RUST_LOG=error`，日志直接输出到终端。
