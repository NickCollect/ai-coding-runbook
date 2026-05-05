---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--acp.md
source_url: https://cursor.com/docs/cli/acp
title: "ACP（Agent Client Protocol）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

ACP（Agent Client Protocol）允许通过 stdio 上的 JSON-RPC 2.0 构建自定义客户端与 Cursor Agent 集成，适用于 JetBrains、Neovim、Zed 等 IDE 集成。

**启动**：`agent acp`，Transport 为 stdio，framing 为换行分隔 JSON。

**标准流程**：initialize → authenticate（`cursor_login`）→ session/new 或 session/load → session/prompt → 处理 session/update 流 → 响应 session/request_permission → 可选 session/cancel。

**认证方式**：`agent login`、`--api-key`（或 `CURSOR_API_KEY`）、`--auth-token`（或 `CURSOR_AUTH_TOKEN`）。

**Cursor 扩展方法**：
- **阻塞**（需回复）：`cursor/ask_question`（多选问题）、`cursor/create_plan`（计划审批）
- **通知**（无需回复）：`cursor/update_todos`（todo 状态更新）、`cursor/task`（子 Agent 完成通知）、`cursor/generate_image`（图像生成通知）

**已有集成**：JetBrains（见集成文档）、Neovim via avante.nvim（配置 `provider = "cursor"` 和 `mode = "agentic"`）、Zed。

**注意**：不支持 dashboard 配置的 Team 级 MCP 服务器，只支持项目/用户级 `.cursor/mcp.json`。
