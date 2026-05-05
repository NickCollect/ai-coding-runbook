---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/mcp.md
source_url: https://code.claude.com/docs/en/agent-sdk/mcp
title: "Claude Agent SDK — 连接外部 MCP 服务器"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Tool-use.md
---

Agent SDK 通过 Model Context Protocol（MCP）连接外部工具和数据源，无需自行实现工具调用逻辑。支持本地进程（stdio）、远程 HTTP/SSE 和 in-process SDK 三种传输方式。

## 快速开始

连接 Claude Code 官方文档 MCP 服务器（HTTP 传输）：

```typescript
for await (const message of query({
  prompt: "Use the docs MCP server to explain what hooks are in Claude Code",
  options: {
    mcpServers: { "claude-code-docs": { type: "http", url: "https://code.claude.com/docs/mcp" } },
    allowedTools: ["mcp__claude-code-docs__*"]  // 通配符允许该服务器所有工具
  }
})) { ... }
```

## 添加 MCP 服务器

### 代码中配置

在 `query()` 的 `mcpServers` 选项中传入：

```python
options = ClaudeAgentOptions(
    mcp_servers={"filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]}},
    allowed_tools=["mcp__filesystem__*"],
)
```

### 从配置文件加载

在项目根目录创建 `.mcp.json`，默认 `query()` 选项会自动加载（`settingSources` 中需包含 `"project"`）：

```json
{
  "mcpServers": {
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"] }
  }
}
```

## 权限配置

MCP 工具名格式：`mcp__<server-name>__<tool-name>`（如 `mcp__github__list_issues`）。

Claude 必须通过 `allowedTools` 获得显式权限才能调用 MCP 工具：

```python
allowed_tools=["mcp__github__*", "mcp__db__query"]  # 通配符允许整个服务器的所有工具
```

> 推荐用 `allowedTools` 而非 `permissionMode`：`acceptEdits` 不自动批准 MCP 工具，`bypassPermissions` 范围过宽。通配符 `mcp__server__*` 精确授权指定服务器。

## 传输类型

| 类型 | 配置标志 | 适用场景 |
|------|---------|---------|
| stdio | `command` + `args` | 本地进程（如 `npx @modelcontextprotocol/server-github`）|
| HTTP | `type: "http"` + `url` | 云托管 MCP 服务器 |
| SSE | `type: "sse"` + `url` | 流式 SSE 远程服务器 |
| SDK MCP server | 传入 server 对象 | 自定义 in-process 工具（见 custom-tools 文档）|

## 认证

- **环境变量**（stdio）：在 `env` 字段传入 `{ "GITHUB_TOKEN": "..." }`，`.mcp.json` 中用 `${GITHUB_TOKEN}` 展开
- **HTTP headers**（HTTP/SSE）：在 `headers` 字段传入 `Authorization: Bearer ...`
- **OAuth2**：SDK 不自动处理 OAuth 流程；在应用层完成 OAuth 后，将 access token 通过 headers 传入

## 错误处理

每次 `query()` 开始时 SDK 发送 `system/init` 消息，包含各 MCP 服务器连接状态：

```typescript
if (message.type === "system" && message.subtype === "init") {
  const failedServers = message.mcp_servers.filter((s) => s.status !== "connected");
  if (failedServers.length > 0) console.warn("Failed to connect:", failedServers);
}
```

## 常见问题

- **服务器显示 "failed"**：检查环境变量、包是否安装（`npx` 命令）、连接字符串格式、网络访问
- **工具未被调用**：确认在 `allowedTools` 中授权了对应工具（`mcp__servername__*`）
- **连接超时**：MCP SDK 默认 60 秒超时；考虑预热服务器或使用更轻量的 server 版本

## 示例：连接 GitHub

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
```

```python
options = ClaudeAgentOptions(
    mcp_servers={
        "github": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"],
                    "env": {"GITHUB_TOKEN": os.environ["GITHUB_TOKEN"]} }
    },
    allowed_tools=["mcp__github__list_issues"],
)
```

## Tool Search

当 MCP 工具数量较多时，工具定义会占用大量 context window。Tool Search 默认开启，按需加载工具定义。详见 [Tool Search 文档](https://code.claude.com/en/agent-sdk/tool-search)。
