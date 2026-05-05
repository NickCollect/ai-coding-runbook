---
type: concept
name: Channel
aliases: [channels, Claude Code channels]
category: concept
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 的通信通道抽象

## 关键属性

- Channel = 一种特殊 MCP server，**主动 push event 进入运行中的 Claude Code session**，让 Claude 在你不在终端时仍能响应 chat / webhook / CI / 监控告警 [[channels]] [[channels-reference]]
- Two-way：Claude 读入站消息，并通过同 channel 回复（终端只显 tool call 确认，实际回复出现在对端平台） [[channels]]
- 状态：**research preview**，要求 Claude Code v2.1.80+，**必须 claude.ai 登录**（API key / Console auth 不行）；Team / Enterprise 必须显式 `channelsEnabled` managed setting 才启用 [[channels]] [[permissions--claude-code]]
- 内置 channel（每个都是 plugin，需 [Bun](https://bun.sh)）：**Telegram**（BotFather token + `/telegram:configure`）/ **Discord**（Developer Portal + Message Content Intent）/ **iMessage**（macOS only，读 `~/Library/Messages/chat.db`，需 Full Disk Access）/ **fakechat**（demo，localhost UI `http://localhost:8787`） [[channels]]
- 启动方式：**`--channels` flag** 控制本 session 启用哪些 channel server；只放 `.mcp.json` 不够；preview 期仅 Anthropic-allowlisted plugin（或 org allowlist）能传 `--channels`，自定义需 `--dangerously-load-development-channels` [[channels]] [[channels-reference]]
- Server 协议（stdio MCP）：声明 `experimental: { 'claude/channel': {} }` 注册通知 listener；可选 `'claude/channel/permission': {}` 收 tool 审批；可选 `tools: {}` 实现 two-way reply；`instructions` 字段会注入 Claude system prompt [[channels-reference]]
- 事件 push 通过 `mcp.notification({ method: 'notifications/claude/channel', params: { content, meta } })`；`meta` 各 key 变 `<channel source="..." ...>` 标签属性；key 仅 `[A-Za-z0-9_]+`，hyphen 被静默丢弃 [[channels-reference]]
- 安全核心：**sender allowlist** —— 未在 allowlist 的 sender ID 静默丢弃；ungate channel = prompt injection 入口；必须 gate **sender ID** 而非 chat/room ID（群聊不一样） [[channels]] [[channels-reference]]
- Allowlist 引导方式：Telegram/Discord 通过 pairing flow（DM bot → bot 回 code → 用户在 CC 批准 → ID 入表）；iMessage 自动从 Messages DB 检测自己的地址 [[channels-reference]]
- **Permission relay**（CC v2.1.81+）：two-way channel opt-in 后可远程审批 Bash / Write / Edit 类 tool 调用；request 携带 5 字母 ID（a-z 去 l 防与电话混淆）+ tool_name + description + 200 字符 input_preview；本地终端对话也保持开，**第一个判决胜出**；project trust / MCP consent dialog **不**走 relay [[channels-reference]]
- 企业管控（managed-only）：`channelsEnabled: true` 主开关 / `allowedChannelPlugins: [...]` 替代 Anthropic allowlist [[channels]] [[permissions--claude-code]]
- 与相邻能力对比：标准 MCP server 是 Claude 按需 pull（无 push）；Web 是云沙箱 fresh per task；Slack `@Claude` 触发 web session；Remote Control 是远端驱动本地 session —— **Channel 填的是把外部事件 push 进已运行的本地 session 这个空缺** [[channels]]
- Plugin 集成：plugin manifest 的 `channels` 字段可声明 MCP-bound channel + 每 channel 独立 `userConfig` [[plugins-reference]]
- 可分发：打包成 plugin + marketplace 即可分发；要进官方 allowlist 需 security review [[channels-reference]]

## 出现来源

_11 summaries reference this entity_:

- [[channels]]
- [[channels-reference]]
- [[cli-reference]]
- [[desktop]]
- [[glossary]]
- [[overview--claude-code]]
- [[permissions--claude-code]]
- [[platforms]]
- [[plugins-reference]]
- [[scheduled-tasks]]
- [[settings]]

## 相关

- [[MCP-server]] — Channel 是一种特殊的 MCP server（push 模型，而非 pull）
- [[Plugin]] — Channel 通过 plugin 分发，plugin manifest 有 `channels` 字段
- [[Permission-mode]] — Channel 可远程 relay 权限批准
- [[Settings]] — `channelsEnabled` / `allowedChannelPlugins` 是 managed-only setting
- [[Native-interface]] — Channel 把外部事件 push 进 native interface（CLI 等）的 session
