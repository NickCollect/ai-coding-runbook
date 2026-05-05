---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/typescript.md
source_url: https://code.claude.com/docs/en/agent-sdk/typescript
title: "Claude Agent SDK — TypeScript API 参考"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Agentic-loop.md
  - Tool-use.md
---

TypeScript Agent SDK 的完整 API 参考文档，涵盖所有函数、类型和接口。包名：`@anthropic-ai/claude-agent-sdk`。

> V2 preview（`send()` + `stream()` 模式）提供更简洁的多轮对话接口，API 仍不稳定；当前文档以稳定的 V1 `query()` 为主。

## 安装

```bash
npm install @anthropic-ai/claude-agent-sdk
```

SDK 内置各平台的原生 Claude Code binary（可选依赖，如 `@anthropic-ai/claude-agent-sdk-darwin-arm64`），无需单独安装 `claude`。若包管理器跳过可选依赖，可通过 `pathToClaudeCodeExecutable` 选项指定已安装的 `claude` 路径。

## 核心函数

### `query()`

主函数，创建异步生成器流式输出消息：

```typescript
function query({
  prompt,   // string | AsyncIterable<SDKUserMessage>
  options?: Options
}): Query   // extends AsyncGenerator<SDKMessage, void>
```

### `startup()`

预热 CLI 子进程，在 prompt 可用前完成初始化握手，减少首次 `query()` 的启动延迟：

```typescript
const warm = await startup({ options: { maxTurns: 3 } });
for await (const message of warm.query("What files are here?")) { ... }
```

### `tool()`

创建类型安全的 MCP 工具定义（用于 in-process SDK MCP server）：

```typescript
const myTool = tool(name, description, zodSchema, handler, { annotations? });
```

### `createSdkMcpServer()`

将工具打包为 in-process MCP server：

```typescript
const server = createSdkMcpServer({ name, version, tools: [myTool] });
```

## 主要配置类型 `Options`

| 字段 | 类型 | 说明 |
|------|------|------|
| `allowedTools` | string[] | 预批准的工具列表（无需确认即可运行）|
| `disallowedTools` | string[] | 禁止调用的工具列表 |
| `tools` | string[] | 限制内置工具可用性（从 context 中移除未列出的工具）|
| `permissionMode` | PermissionMode | 权限模式（`acceptEdits` / `dontAsk` / `auto` / `bypassPermissions` / `default`）|
| `systemPrompt` | string | 自定义 system prompt |
| `mcpServers` | Record<string, ...> | MCP server 配置（支持 stdio / http / sse / SDK server）|
| `agents` | Record<string, AgentDefinition> | 子 agent 定义 |
| `hooks` | HookConfig | 生命周期钩子（`PreToolUse`, `PostToolUse`, `Stop` 等）|
| `resume` | string | 要恢复的 session ID |
| `continue` | boolean | 恢复当前目录最近 session |
| `forkSession` | boolean | 从 resume session 分叉创建新 session |
| `persistSession` | boolean | 是否将 session 写入磁盘（默认 true）|
| `maxTurns` | number | 最大 agentic turns 数 |
| `model` | string | 模型名称或别名 |
| `cwd` | string | 工作目录 |
| `env` | Record<string, string> | 额外环境变量（如 `ENABLE_TOOL_SEARCH`）|
| `settingSources` | string[] | 配置来源（`'user'`/`'project'`/`'local'`）|

## 主要消息类型 `SDKMessage`

所有消息继承自 `SDKMessageBase`，通过 `type` 字段区分：

| type | 含义 |
|------|------|
| `"system"` | 系统消息（`subtype: "init"` 含 session ID、可用工具、MCP 服务器状态等）|
| `"assistant"` | Claude 的响应消息（`SDKAssistantMessage`，内含 content blocks）|
| `"user"` | 用户/工具结果消息 |
| `"result"` | 最终结果（`SDKResultMessage`，含 `session_id`, `total_cost_usd`, `subtype: "success" / "error_..."` 等）|

## Session 工具函数

```typescript
listSessions(cwd?: string): Promise<SessionInfo[]>
getSessionMessages(sessionId: string, cwd?: string): Promise<SDKMessage[]>
getSessionInfo(sessionId: string, cwd?: string): Promise<SessionInfo>
renameSession(sessionId: string, title: string, cwd?: string): Promise<void>
tagSession(sessionId: string, tags: string[], cwd?: string): Promise<void>
```

## 工具注解（ToolAnnotations）

```typescript
interface ToolAnnotations {
  readOnlyHint?: boolean;     // 只读工具，可并行调用
  destructiveHint?: boolean;  // 可能有破坏性（仅参考）
  idempotentHint?: boolean;   // 幂等工具（仅参考）
  openWorldHint?: boolean;    // 访问外部系统（仅参考）
}
```

## V2 Preview（实验性）

V2 提供 `createSession()` + `session.send()` + `session.stream()` 的多轮对话模式，类似 Python 的 `ClaudeSDKClient`，但 API 可能变更，生产环境建议使用稳定的 V1 `query()`。
