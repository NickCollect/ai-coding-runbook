---
type: summary
source: 01_Raw/code.claude.com/docs/en/mcp.md
source_url: https://code.claude.com/docs/en/mcp
title: "Claude Code — 通过 MCP 连接外部工具"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Hooks.md
concepts_referenced:
  - Tool-use.md
  - Channel.md
---

Claude Code 通过 **Model Context Protocol（MCP）** 这一开源标准连接数百种外部工具和数据源，使 Claude 可以直接读取并操作这些系统，而无需用户手动粘贴数据。

## 典型使用场景

- 从 Jira issue 实现功能并在 GitHub 开 PR
- 通过 Sentry 和 Statsig 分析生产监控数据
- 查询 PostgreSQL 数据库
- 根据 Figma 设计更新邮件模板
- 自动起草 Gmail 草稿邀请用户参与反馈

## 安装 MCP 服务器

### Option 1：远程 HTTP 服务器（推荐）

```bash
claude mcp add --transport http <name> <url>
# 示例：连接 Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

### Option 2：远程 SSE 服务器（已废弃，优先用 HTTP）

```bash
claude mcp add --transport sse <name> <url>
```

### Option 3：本地 stdio 服务器

```bash
claude mcp add --transport stdio --env KEY=value <name> -- <command>
```

**注意**：所有 `--option` 参数必须在服务器名称**之前**，`--` 之后才是传给 MCP 服务器的命令。

## 管理命令

```bash
claude mcp list          # 列出所有服务器
claude mcp get <name>    # 查看指定服务器详情
claude mcp remove <name> # 删除服务器
/mcp                     # 在 Claude Code 内查看状态 / 触发认证
```

## 配置作用域

| 作用域 | 加载范围 | 团队共享 | 存储位置 |
|--------|---------|---------|---------|
| local（默认） | 当前项目 | 否 | `~/.claude.json` |
| project | 当前项目 | 是（通过 `.mcp.json` 版本控制） | `.mcp.json` |
| user | 所有项目 | 否 | `~/.claude.json` |

优先级：local > project > user > plugin 提供的 > claude.ai connectors。

## 高级功能

- **动态工具更新**：支持 MCP `list_changed` 通知，服务器可热更新工具列表，无需重连
- **自动重连**：HTTP/SSE 服务器断开后指数退避重连（最多 5 次，起始 1 秒，每次翻倍）
- **Channels（Push 消息）**：MCP 服务器可声明 `claude/channel` 能力，将外部事件（CI 结果、监控告警、Telegram 消息）主动推入会话
- **OAuth 2.0**：支持标准 OAuth 认证，通过 `/mcp` 触发浏览器登录；支持固定回调端口（`--callback-port`）和预配置 Client ID（`--client-id`）
- **动态 headers**：`headersHelper` 字段可在每次连接时运行脚本生成请求头（适合 Kerberos / 短期 token 等非 OAuth 认证）
- **MCP Resources**：支持通过 `@server:protocol://resource/path` 在 prompt 中引用服务器暴露的资源
- **Tool Search**：默认开启，工具定义按需加载，减少 context 占用；可通过 `ENABLE_TOOL_SEARCH` 环境变量配置

## Plugin 提供的 MCP 服务器

Plugin 可在 `.mcp.json` 或 `plugin.json` 中内联声明 MCP 服务器，插件启用后自动连接，团队成员共享相同工具集。

## 组织管控

- **`managed-mcp.json`**：系统管理员部署（`/Library/Application Support/ClaudeCode/` 等），完全接管 MCP 服务器列表，用户无法修改
- **allowedMcpServers / deniedMcpServers**：按名称、命令或 URL 模式（支持通配符）控制用户可添加的服务器范围

## MCP 输出限制

- 默认警告阈值：10,000 tokens
- 默认最大值：25,000 tokens（`MAX_MCP_OUTPUT_TOKENS` 环境变量可调）
- MCP 服务器开发者可在工具 `_meta` 中设置 `anthropic/maxResultSizeChars` 为单个工具指定更高上限（最高 500,000 字符）
