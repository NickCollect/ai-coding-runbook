---
type: summary
source: 01_Raw/github/openai/codex/AGENTS.md
source_url: https://github.com/openai/codex/blob/main/AGENTS.md
title: "Codex 仓库 AGENTS.md — Rust 开发规范"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Codex 仓库的 AGENTS.md 是面向 Codex agent 自身在此 repo 中做代码修改时的开发规范，主要覆盖 codex-rs（Rust 实现）的编码约定。

**Rust 代码规范**：crate 名统一加 `codex-` 前缀；禁止修改 `CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR` 相关代码；强制遵循 Clippy lint（collapsible_if、uninlined_format_args、redundant_closure）；避免 bool/Option 参数造成调用处难以读懂（改用 enum/newtype）；match 语句保持穷举，禁用通配符 arm；新 trait 必须加文档注释；优先 RPITIT 而非 `#[async_trait]`。

**模块规模控制**：Rust 模块目标 500 LoC 以内，超过 800 行须拆分新模块；`codex-core` crate 已过大，明确要求**抵制向 codex-core 添加新代码**，优先复用现有 crate 或新建 crate。

**TUI 编码风格**：使用 ratatui Stylize helpers（.dim()/.bold()/.cyan() 等）；避免硬编码白色；文本换行使用 `textwrap::wrap` 和仓库内 wrapping.rs helpers。

**测试规范**：UI 变更必须配套 `insta` 快照测试；测试用 `pretty_assertions::assert_eq`；集成测试优先使用 `core_test_support::responses` 工具函数；用 `codex_utils_cargo_bin::cargo_bin` 定位二进制，避免硬编码 `CARGO_MANIFEST_DIR`。

**App-server API 规范**：所有新开发在 v2；字段命名 camelCase（除 config RPC 用 snake_case）；cursor 分页为 list 方法默认；实验性 API 用 `#[experimental]` 标注。

**自动格式化**：Rust 改动完成后自动运行 `just fmt`；提交大变更前运行 `just fix -p <crate>`。
