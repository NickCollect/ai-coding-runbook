---
type: summary
source: 01_Raw/code.claude.com/docs/en/channels-reference.md
source_url: https://code.claude.com/docs/en/channels-reference
title: "Channels reference"
summarized_at: 2026-05-05
entities_referenced: [Channel, MCP-server, Plugin, Plugin-marketplace]
concepts_referenced: []
---

Channels = MCP servers that push events into a Claude Code session so Claude reacts to things happening outside the terminal. **Research preview**, requires Claude Code v2.1.80+, claude.ai login (no API key auth), Team/Enterprise must explicitly enable.

Two flavors:
- **One-way**: forwards alerts/webhooks/monitoring events.
- **Two-way**: also exposes a reply tool so Claude sends messages back.

Pre-built: Telegram, Discord, iMessage, fakechat.

**Server contract** — runs on the same machine as Claude Code, communicates over stdio:
1. Declare capability: `experimental: { 'claude/channel': {} }` registers the notification listener.
2. Optionally `'claude/channel/permission': {}` to receive tool-approval prompts (relay).
3. Optionally `tools: {}` for two-way reply.
4. `instructions` string injected into Claude's system prompt — describes event format, reply routing.
5. Push events with `mcp.notification({ method: 'notifications/claude/channel', params: { content, meta } })`. Each `meta` key becomes an attribute on the `<channel source="..." ...>` tag wrapping `content`. Keys must be `[A-Za-z0-9_]+`; hyphens are silently dropped.

**Reply tool**: standard MCP tool registration via `ListToolsRequestSchema` + `CallToolRequestSchema` handlers.

**Sender gating** (critical security): an ungated channel = prompt injection vector. Check sender against an allowlist BEFORE emitting. Gate on **sender ID** (e.g. `message.from.id`), not chat/room ID — group chats differ. Telegram/Discord bootstrap allowlist via pairing flow (DM bot → bot replies code → user approves in CC → ID added). iMessage detects user's own addresses from Messages DB.

**Permission relay** (CC v2.1.81+): two-way channels can opt in via `claude/channel/permission` capability. Claude Code emits `notifications/claude/channel/permission_request` with fields `request_id` (5 lowercase letters from `a-z` minus `l` to avoid phone confusion), `tool_name`, `description`, `input_preview` (200-char JSON). Server formats and forwards; user replies `yes <id>` / `no <id>`; server emits `notifications/claude/channel/permission` with `behavior: 'allow' | 'deny'`. Local terminal dialog stays open; first verdict wins. Only Bash/Write/Edit-style tool approvals relay — project trust and MCP consent dialogs don't.

**Testing during preview**: custom channels not on Anthropic-curated allowlist; use `claude --dangerously-load-development-channels server:<name>` or `plugin:<name>@<marketplace>`. `channelsEnabled` org policy still applies. Package as plugin + marketplace for distribution; submit to official marketplace for allowlisting (security review).
