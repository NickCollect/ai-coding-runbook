---
name: MCP 集成指南
type: synthesis
created: 2026-05-05
sources:
  - 01_Raw/code.claude.com/docs/en/mcp.md
  - 01_Raw/github/modelcontextprotocol/typescript-sdk/README.md
  - 01_Raw/docs.openai.com/docs/guides/tools-remote-mcp.md
---

# MCP 集成指南

> 跨 Claude Code、OpenAI Responses API、TypeScript SDK 的完整 MCP 集成参考。

---

## 一、什么是 MCP

Model Context Protocol (MCP) 是一个开放标准，允许应用以标准化方式为 LLM 提供上下文，**将"提供上下文"这件事从实际的 LLM 交互中解耦**。

核心角色：
- **Server**：提供工具（tools）、资源（resources）、提示词（prompts）的一方
- **Client**：连接 server、发起请求的一方（如 Claude Code、OpenAI Responses API）
- **Transport**：两端之间的通信层

TypeScript SDK 分为两个独立包：`@modelcontextprotocol/server` 和 `@modelcontextprotocol/client`，均运行在 Node.js / Bun / Deno 上。

---

## 二、Transport 类型

### 2.1 Streamable HTTP（推荐）

- 远程服务器的**推荐 transport**
- 支持 SSE 流式传输
- Claude Code 添加命令：`claude mcp add --transport http <name> <url>`
- OpenAI Responses API 同样支持此 transport

### 2.2 HTTP + SSE（已废弃）

- 旧版 HTTP+SSE transport，**已被标记为 deprecated**
- Claude Code 仍支持：`claude mcp add --transport sse <name> <url>`
- OpenAI Responses API 也支持 SSE（向后兼容）
- 新项目应优先使用 Streamable HTTP

### 2.3 stdio

- 本地进程通信，**适合需要直接系统访问的工具或自定义脚本**
- 以子进程方式运行在用户机器上
- 不支持自动重连（HTTP/SSE 支持，最多 5 次指数退避重连）
- Claude Code 添加命令：

```bash
claude mcp add --transport stdio --env KEY=value <name> -- npx -y <package>
```

---

## 三、Server 能力类型

### 3.1 Tools（工具）

最常用的能力类型。Server 暴露工具定义（名称 + 描述 + 输入 schema），client 可调用。

TypeScript SDK 注册示例：

```typescript
server.registerTool('greet', {
  description: 'Greet someone by name',
  inputSchema: z.object({ name: z.string() }),
}, async ({ name }) => ({
  content: [{ type: 'text', text: `Hello, ${name}!` }],
}));
```

Claude Code 中 MCP 工具通过 **Tool Search** 机制延迟加载（默认开启），只有 Claude 实际需要时才加载 schema，减少 context 占用。

### 3.2 Resources（资源）

Server 暴露可被引用的数据资源。Claude Code 支持通过 `@server:protocol://resource/path` 语法 @ 引用：

```
@github:issue://123
@postgres:schema://users
```

### 3.3 Prompts（提示词）

Server 可以暴露提示词模板，在 Claude Code 中以 slash command 形式出现：`/mcp__servername__promptname`。

### 3.4 Sampling（采样，服务端发起）

Server 可以向 client 发起 LLM 请求（`sampling/createMessage`），要求 client 拥有相应能力。这是 MCP 双向通信的体现。

### 3.5 Elicitation（用户输入请求）

Server 可以在任务执行中途请求用户提供结构化输入（form 表单或 URL 跳转两种模式）。Claude Code 自动弹出对话框。

---

## 四、认证模式

### 4.1 OAuth 2.0（Claude Code 标准方式）

Claude Code 支持完整的 OAuth 2.0 流程，含以下特性：
- **Dynamic Client Registration**：自动发现并注册 OAuth 客户端
- **Client ID Metadata Document (CIMD)**：自动发现
- **固定回调端口**：`--callback-port 8080`（当 server 需要预注册 redirect URI 时）
- **预配置凭据**：`--client-id <id> --client-secret`（当 server 不支持动态注册时）
- **Scope 限制**：通过 `oauth.scopes` 字段限定授权范围
- **自定义元数据 URL**：通过 `authServerMetadataUrl` 绕过默认发现链

操作：在 Claude Code 内运行 `/mcp` 即可触发 OAuth 浏览器登录流程。

### 4.2 API Key / Bearer Token

静态 header 注入，适合不需要 OAuth 的服务：

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

### 4.3 动态 Header（headersHelper）

适合 Kerberos、短时令牌、内部 SSO 等非标准认证。配置一个 shell 命令，每次连接时执行并输出 JSON header：

```json
{
  "mcpServers": {
    "internal-api": {
      "type": "http",
      "url": "https://mcp.internal.example.com",
      "headersHelper": "/opt/bin/get-mcp-auth-headers.sh"
    }
  }
}
```

helper 命令必须将 JSON 对象（string key-value pairs）输出到 stdout，超时 10 秒。

### 4.4 OpenAI 的认证方式

OpenAI Responses API 通过 `authorization` 字段传入 OAuth access token：

```json
{
  "type": "mcp",
  "server_url": "https://mcp.stripe.com",
  "authorization": "$STRIPE_OAUTH_ACCESS_TOKEN"
}
```

注意：OpenAI 不存储 `authorization` 字段的值，每次请求都必须重新传入。

---

## 五、Claude Code MCP 配置

### 5.1 三种 scope

| Scope | 生效范围 | 是否与团队共享 | 存储位置 |
|---|---|---|---|
| `local`（默认） | 当前项目 | 否 | `~/.claude.json` |
| `project` | 当前项目 | 是（via .mcp.json） | `.mcp.json` in project root |
| `user` | 所有项目 | 否 | `~/.claude.json` |

优先级：local > project > user > Plugin-provided > claude.ai connectors

### 5.2 常用命令

```bash
claude mcp add --transport http <name> <url>           # 添加远程 HTTP
claude mcp add --transport stdio <name> -- <command>   # 添加本地 stdio
claude mcp add --scope project ...                      # 指定 scope
claude mcp list                                         # 列出所有
claude mcp get <name>                                   # 查看详情
claude mcp remove <name>                                # 删除
/mcp                                                    # 会话内查看状态/认证
```

### 5.3 .mcp.json 环境变量展开

支持 `${VAR}` 和 `${VAR:-default}` 语法，可用于 command、args、env、url、headers 字段。适合团队共享配置同时保留机器特定值。

### 5.4 Tool Search（工具搜索）

默认开启。MCP 工具定义不在 session 启动时一次性载入 context，而是按需延迟加载。控制选项：

| 值 | 行为 |
|---|---|
| (unset) | 所有 MCP 工具延迟加载（Vertex AI 上退化为预加载） |
| `true` | 强制延迟加载（包括 Vertex AI） |
| `auto` | 阈值模式：工具定义 < context 10% 时预加载，否则延迟 |
| `false` | 全部预加载（禁用 Tool Search） |

对于需要每轮都可见的工具，在配置中设置 `"alwaysLoad": true`。

### 5.5 输出 token 限制

- 超过 10,000 tokens 时 Claude Code 会发出警告
- 默认上限 25,000 tokens（通过 `MAX_MCP_OUTPUT_TOKENS` 环境变量调整）
- Server 作者可在 `tools/list` 响应中设置 `_meta["anthropic/maxResultSizeChars"]`，上限 500,000 字符

---

## 六、OpenAI MCP 支持

OpenAI 通过 **Responses API** 支持 MCP，`tools` 参数中使用 `type: "mcp"` 指定。

```json
{
  "type": "mcp",
  "server_label": "dmcp",
  "server_description": "A Dungeons and Dragons MCP server",
  "server_url": "https://dmcp-server.deno.dev/sse",
  "require_approval": "never"
}
```

支持 Streamable HTTP 和 HTTP/SSE 两种 transport。

### 6.1 工具过滤

通过 `allowed_tools` 参数限制加载的工具子集，减少 token 消耗：

```json
{ "allowed_tools": ["roll"] }
```

### 6.2 Approval 机制

| 值 | 行为 |
|---|---|
| `"always"`（默认） | 每次工具调用都需要开发者审批 |
| `"never"` | 跳过所有审批 |
| `{ "never": { "tool_names": [...] } }` | 仅跳过指定工具的审批 |

审批请求产生 `mcp_approval_request` output item，开发者通过返回 `mcp_approval_response` 响应。

### 6.3 Connectors

OpenAI 还提供官方维护的 Connectors（如 Dropbox、Gmail、Google Calendar 等），使用 `connector_id` 替代 `server_url`，本质是 MCP 包装器。

### 6.4 延迟加载

通过 `defer_loading: true` 在启用 Tool Search 时延迟加载 server 的工具定义。

---

## 七、何时用 MCP vs 直接 API vs Function Calling

| 场景 | 推荐方式 | 原因 |
|---|---|---|
| 集成第三方服务（Sentry、Notion、GitHub 等）| MCP | 标准协议，服务商已有官方 server |
| 自定义内部工具（数据库查询、脚本执行）| MCP（stdio）或 Function Calling | 取决于是否需要跨 session/团队共享 |
| 单次 stateless 调用，工具简单 | Function Calling（直接定义 tools） | 无需额外基础设施 |
| 需要 server 主动推送消息 | MCP（channels）| MCP 支持 server-initiated notifications |
| 生产环境 API 集成，工具逻辑在自己服务端 | Function Calling / Tool Use | 更简单，无需维护 MCP server |

**结论**：MCP 是 tool use 的基础设施层。当工具需要复用、跨平台共享、或需要第三方服务直接托管时选 MCP；当工具逻辑在自己代码里且只为一个 agent 服务时直接用 Function Calling 更轻量。

---

## 八、常见坑

1. **SSE transport 已废弃**：新项目用 `--transport http`，不要用 `--transport sse`
2. **工具定义顺序影响 Tool Search**：Server instructions 对 Tool Search 至关重要，写清楚工具的使用场景；Claude Code 会截断超过 2KB 的 server instructions 和工具描述
3. **项目 scope .mcp.json 需要用户明确授权**：首次使用时 Claude Code 会弹出信任确认
4. **headersHelper 每次连接都重新执行**：无 token 复用，脚本自己处理缓存
5. **stdio server 不支持自动重连**：连接断开后需手动重启
6. **Prompt injection 风险**：连接到能抓取不可信内容的 MCP server 时存在 prompt injection 风险，第三方 server 均为 Anthropic 未验证的
7. **OAuth 回调端口冲突**：如果 server 需要预注册 redirect URI，用 `--callback-port` 固定端口
8. **OpenAI MCP authorization 不被存储**：每次 API 请求都必须重新传入 `authorization` 字段
9. **Tool output 过大**：默认上限 25,000 tokens，大数据量场景需要调高 `MAX_MCP_OUTPUT_TOKENS`
10. **Tool Search 在 Vertex AI 上默认关闭**：需要显式设置 `ENABLE_TOOL_SEARCH=true`

---

## 出现来源

- `01_Raw/code.claude.com/docs/en/mcp.md` — Claude Code MCP 配置文档（transport 选项、scope、OAuth、tool search、output limits）
- `01_Raw/github/modelcontextprotocol/typescript-sdk/README.md` — TypeScript SDK 架构（server/client 包、transport 系统、bidirectional protocol）
- `01_Raw/docs.openai.com/docs/guides/tools-remote-mcp.md` — OpenAI Responses API MCP 支持（tools 参数、approval 机制、connectors）
