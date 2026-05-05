---
type: summary
source: 01_Raw/docs.cursor.com/docs--subagents.md
source_url: https://cursor.com/docs/subagents
title: "Subagents（子 Agent）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Subagents 是 Cursor Agent 可委托任务的专属子 AI，各自拥有独立上下文窗口，处理特定类型工作后返回结果，适用于复杂任务分解、并行执行和上下文隔离。

**三个内置子 Agent**：
- **Explore**：代码库搜索与分析，使用更快的模型并行执行多次搜索
- **Bash**：批量 Shell 命令执行，将详细输出隔离在子 Agent 中
- **Browser**：通过 MCP 工具控制浏览器，过滤嘈杂的 DOM 快照

**自定义子 Agent**：存放在 `.cursor/agents/`（项目）或 `~/.cursor/agents/`（用户全局），也兼容 `.claude/agents/`、`.codex/agents/`。YAML frontmatter 字段：`name`（标识符）、`description`（委托触发条件，核心）、`model`（`inherit` 或指定模型 ID）、`readonly`（只读模式）、`is_background`（后台运行）。

**运行模式**：Foreground（阻塞，立即返回结果）vs Background（不阻塞，适合长任务/并行流）。可通过 ID 恢复子 Agent 继续历史对话。

**调用方式**：Agent 自动委托；`/subagent-name` 显式调用；自然语言提及；并行执行（Agent 在单条消息中发出多个 Task tool 调用）。

**成本权衡**：并行执行消耗 token 约为单 Agent 的 N 倍；子 Agent 启动有额外开销，简单任务主 Agent 更快；优势在于上下文隔离而非速度。

**Cursor 2.5+**：子 Agent 可递归生成子子 Agent，构建协调工作树。
