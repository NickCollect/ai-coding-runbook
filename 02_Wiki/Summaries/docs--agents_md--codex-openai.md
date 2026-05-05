---
type: summary
source: 01_Raw/github/openai/codex/docs/agents_md.md
source_url: https://github.com/openai/codex/blob/main/docs/agents_md.md
title: "Codex AGENTS.md 功能说明"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Codex CLI 中 AGENTS.md 文件的功能及分层代理消息机制说明。

**基本功能**：AGENTS.md 是 Codex CLI 的 agent 行为指令文件，详细用法参见官方文档 [developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)。

**分层代理消息（Hierarchical agents message）**：当 `config.toml` 的 `[features]` 中启用 `child_agents_md` feature flag 时，Codex 会在用户指令消息中附加关于 AGENTS.md 作用域与优先级的额外说明，即使当前目录中不存在 AGENTS.md 文件也会发送该消息。
