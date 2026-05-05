---
type: summary
source: 01_Raw/code.claude.com/docs/en/mcp.md
source_url: https://code.claude.com/docs/en/mcp
title: "Connect Claude Code to tools via MCP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Plugin, Slash-command, Settings, Permission-mode, Channel]
concepts_referenced: [Tool-use, Context-window]
---

Claude Code 端面向用户的 MCP 完整指南：从 install / scope / auth / OAuth 到 plugin-provided MCP / managed config / tool search。覆盖 SDK 文档之外的 CLI 用户视角。

**三种 transport（按推荐度）**：
- **HTTP**（推荐）`claude mcp add --transport http <name> <url>`，可加 `--header "Authorization: Bearer ..."`
- **SSE**（已 deprecated，仅保留兼容）
- **stdio** 本地进程：`claude mcp add --transport stdio --env KEY=value <name> -- <command> [args...]`；options 必须在 server name 之前，`--` 之后才是 server 自己的 command

**Server 管理**：`claude mcp list / get / remove`；session 内 `/mcp` 看状态、跑 OAuth、清 auth。

**Reconnect 行为**：HTTP/SSE 断线指数退避 1s → 2s → 4s → 8s → 16s 共 5 次；初次连接 v2.1.121+ 也对 5xx/timeout/refused 重试 3 次（auth/404 不重试）。stdio server 不自动重连。

**Channels**（详见 [[Channel]]）：MCP server 声明 `claude/channel` capability + 启动 `--channels` flag → 可主动 push 消息到 session（CI 结果、监控告警、聊天事件）。

**Plugin-provided MCP servers**：plugin 在根目录 `.mcp.json` 或 `plugin.json.mcpServers` 声明；plugin enable 时自动启动；用 `${CLAUDE_PLUGIN_ROOT}` 引用 plugin 内文件、`${CLAUDE_PLUGIN_DATA}` 持久化 state（survives plugin updates）。Session 内 enable/disable plugin 后跑 `/reload-plugins` 才重连 MCP。

**安装 Scope**：

| Scope | 加载范围 | 团队共享 | 存储 |
|---|---|---|---|
| local（默认） | 当前 project | 否 | `~/.claude.json` |
| project | 当前 project | **是**（commit `.mcp.json`） | `.mcp.json` 项目根 |
| user | 所有 project | 否 | `~/.claude.json` |

**Scope 优先级**：local > project > user > plugin > claude.ai connector。三种 scope 按 name 匹配重复；plugin/connector 按 endpoint URL 匹配。Project-scoped server 首次用要 trust prompt，可用 `claude mcp reset-project-choices` 重置。

**环境变量替换**（`.mcp.json` 内）：`${VAR}` / `${VAR:-default}`。可用于 `command` / `args` / `env` / `url` / `headers`。required 变量不存在 + 无 default → 启动失败。

**OAuth 2.0**：HTTP/SSE server 跑 `/mcp` 触发浏览器 flow → token 自动存系统 keychain（macOS）+ 自动 refresh。
- `--callback-port <PORT>` 固定回调端口（用于预注册 redirect URI = `http://localhost:PORT/callback`）
- 不支持 Dynamic Client Registration 的 server：用 `--client-id` + `--client-secret`（masked input）；CI 用 `MCP_CLIENT_SECRET` env var
- `authServerMetadataUrl`（`.mcp.json` 内 `oauth` object）覆盖默认 RFC 9728 / RFC 8414 discovery chain（v2.1.64+，必须 https）
- `oauth.scopes`（space-separated string）pin 请求的 scopes（绕过 server 的 advertised scopes）；403 insufficient_scope 时用同样 scopes 重试

**Dynamic headers**（OAuth 之外的 auth）：`headersHelper` 配 shell command，10s timeout 内必须 stdout 输出 JSON `{"Header": "value"}`。每次连接（含 reconnect）跑一次，无 cache。Project/local scope 的 helper 必须先接受 trust dialog 才会执行。提供 `CLAUDE_CODE_MCP_SERVER_NAME` / `CLAUDE_CODE_MCP_SERVER_URL` env vars。

**JSON-based add**：`claude mcp add-json <name> '<json>'` —— 直接传完整 server config JSON，含 OAuth object。

**Import from Claude Desktop**：`claude mcp add-from-claude-desktop`（仅 macOS / WSL），同名 server 加数字后缀。

**Claude.ai connectors 自动可用**：登录 claude.ai 账户后，`claude.ai/customize/connectors` 添加的 server 在 Claude Code 自动出现（`/mcp` 列表标记来源）。`ENABLE_CLAUDEAI_MCP_SERVERS=false` 关闭。Code 里 add 的 server 优先级高于同 endpoint 的 connector。

**Claude Code 也可作 MCP server**：`claude mcp serve` 把 Claude Code 的 tools 暴露给其他 MCP client（如 Claude Desktop）；client 自己负责 user confirmation。executable 路径需可解析（`which claude`）。

**Output 限制**：默认 25K tokens / tool call；超 10K 触发 warning；`MAX_MCP_OUTPUT_TOKENS=50000` 调整上限。MCP server 作者可在 tool 的 `_meta["anthropic/maxResultSizeChars"]` 声明上限（最高 500K chars，仅 text content；image 仍受 token 限制）。

**Elicitation**：MCP server 通过 elicitation 中途请求 form / URL 输入，自动弹 dialog；`Elicitation` hook 可自动应答（[[Hooks]]）。

**MCP resources**：用 `@server:protocol://path` 引用 server 暴露的资源（`@github:issue://123`、`@docs:file://api/auth`），自动 fetch 作 attachment。

**Tool Search**（默认开启 v2.1.121+）：MCP tool 定义按需加载，session 启动只载 tool name → 解决 context window 被 schema 撑爆。`ENABLE_TOOL_SEARCH=auto` / `auto:N%` 阈值模式 / `false` 全量加载 / `true` 强制全 defer。Vertex AI / 非第一方 `ANTHROPIC_BASE_URL` 默认关。Haiku 不支持。可用 server 配置 `"alwaysLoad": true` 或 tool `_meta["anthropic/alwaysLoad"]` 豁免单 server/tool。`ToolSearch` 本身可用 `permissions.deny` 关闭。

**MCP prompts 作 slash command**：server 暴露的 prompt 显示为 `/mcp__<server>__<prompt>`（带参数 `/mcp__github__pr_review 456`）。

**企业管理**：
- `managed-mcp.json`（`/Library/Application Support/ClaudeCode/` 等系统路径）= **exclusive control**，user 不能加 / 改其他 server
- `allowedMcpServers` / `deniedMcpServers`（managed settings）= policy 模式，可按 `serverName` / `serverCommand`（精确匹配 args）/ `serverUrl`（通配符）三种方式匹配；deny 优先 allow
- 两种可结合：managed-mcp.json + allowedMcpServers 仍 filter 哪些 managed server 实际加载

**Tips**：
- `--scope` 旧名称（v2.1 前）：`local`=`project`，`user`=`global`
- `MCP_TIMEOUT=10000` 调整启动超时（默认 60s）
- `claude mcp get <name>` 验证 OAuth 凭证已配
- 第三方 MCP server 自负风险（Anthropic 不审计），prompt injection 风险尤其大于 fetch untrusted content
