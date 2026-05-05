---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/tool-search.md
source_url: https://code.claude.com/docs/en/agent-sdk/tool-search
title: "Claude Agent SDK — Tool Search（大规模工具按需加载）"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Tool-use.md
  - Context-window.md
---

Tool Search 使 agent 能够处理数百乃至数千个工具，通过按需动态发现和加载工具定义，而非将所有定义预先加载到 context window。

## 解决的问题

- **Context 效率**：50 个工具的定义可能占用 10-20K tokens，大幅压缩实际工作空间
- **工具选择准确性**：一次性加载超过 30-50 个工具会降低工具选择准确率

## 工作原理

Tool Search 激活时，工具定义从 context window 中移除。Agent 收到可用工具摘要，在任务需要某能力时自动搜索，每次加载 3-5 个最相关的工具到 context 中，后续 turns 中这些工具持续可用。若 SDK 压缩了早期消息以释放空间，已发现的工具可能被移除，之后 agent 会再次搜索。

Tool Search 会增加首次发现工具时的一次额外 round-trip（搜索步骤），但对大型工具集而言，这被每次 turn 更小的 context 开销所抵消。工具少于约 10 个时，全量预加载通常更快。

> 需要 Claude Sonnet 4 或更高，或 Claude Opus 4 或更高。Haiku 模型不支持 Tool Search。

## 配置

通过 `ENABLE_TOOL_SEARCH` 环境变量（在 `query()` 的 `env` 选项中设置）：

| 值 | 行为 |
|----|------|
| （未设置）| 始终开启，工具定义永不预加载（默认）|
| `true` | 同未设置 |
| `auto` | 检查所有工具定义总 token 数；超过 context window 10% 时激活 |
| `auto:N` | 同 `auto`，但用自定义百分比 N（如 `auto:5` 在超过 5% 时激活）|
| `false` | 关闭，所有工具定义每次 turn 全量加载 |

```typescript
for await (const message of query({
  prompt: "Find and run the appropriate database query",
  options: {
    mcpServers: { "enterprise-tools": { type: "http", url: "https://tools.example.com/mcp" } },
    allowedTools: ["mcp__enterprise-tools__*"],
    env: { ENABLE_TOOL_SEARCH: "auto:5" }  // 工具超过 context 5% 时激活
  }
})) { ... }
```

## 优化工具发现

搜索机制基于工具名称和描述进行匹配：

- **命名**：`search_slack_messages`（描述性强）比 `query_slack`（通用）适配更多请求
- **描述**：`"Search Slack messages by keyword, channel, or date range"` 比 `"Query Slack"` 命中率更高
- **System prompt 提示**：在 system prompt 中列出可用工具类别，帮助 agent 知道能搜索哪些工具：
  ```
  You can search for tools to interact with Slack, GitHub, and Jira.
  ```

## 限制

- **最大工具数**：工具目录最多 10,000 个工具
- **搜索结果**：每次搜索返回 3-5 个最相关工具
- **模型要求**：仅支持 Claude Sonnet 4+ 和 Opus 4+（不含 Haiku）

## 适用范围

Tool Search 对所有注册工具生效，包括远程 MCP servers 和自定义 SDK MCP servers（in-process 工具）。使用 `auto` 模式时，阈值基于所有服务器的工具定义合并大小计算。
