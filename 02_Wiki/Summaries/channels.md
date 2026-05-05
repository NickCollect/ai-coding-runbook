---
type: summary
source: 01_Raw/code.claude.com/docs/en/channels.md
source_url: https://code.claude.com/docs/en/channels
title: "Push events into a running session with channels"
summarized_at: 2026-05-05
entities_referenced: [Plugin, MCP-server, Settings, Permission-mode]
concepts_referenced: [Channel]
---

Channels are MCP servers that **push events into a running Claude Code session** — letting Claude react to chat messages, webhooks, CI results, monitoring alerts while you're away from the terminal. Two-way: Claude reads inbound, replies through the same channel (terminal shows tool call confirmation, actual reply appears on the other platform).

Status: **research preview**, requires Claude Code v2.1.80+, **claude.ai login required** (Console / API key auth not supported). Team / Enterprise must explicitly enable via `channelsEnabled` managed setting.

Built-in supported channels (each is a plugin requiring [Bun](https://bun.sh)):
- **Telegram** — bot via BotFather, install plugin `telegram@claude-plugins-official`, configure with `/telegram:configure <token>`, restart with `claude --channels plugin:telegram@claude-plugins-official`, pair via DM, lock down with `/telegram:access policy allowlist`.
- **Discord** — Developer Portal app, enable Message Content Intent, OAuth invite to server, similar configure/pair flow.
- **iMessage** — macOS only, reads `~/Library/Messages/chat.db` directly (needs Full Disk Access), sends via AppleScript. No bot needed. Self-chat bypasses access control. Add others via `/imessage:access allow +15551234567`.

Demo channel: **fakechat** — localhost UI at `http://localhost:8787`, no auth, good for first-time setup.

Build your own: see [Channels reference](https://code.claude.com/en/channels-reference) doc.

Security model:
- Each channel maintains a **sender allowlist** — non-allowlisted IDs silently dropped.
- Telegram/Discord pair via code exchange; iMessage uses self-chat or `allow` command.
- `--channels` flag controls which servers are enabled per session. Being in `.mcp.json` is NOT enough.
- During preview, only Anthropic-allowlisted plugins (or org allowlist) can be passed to `--channels`. Use `--dangerously-load-development-channels` for testing your own.
- **Permission relay capability**: a channel can forward Claude Code permission prompts to the remote user. Anyone on the allowlist can approve/deny tool calls — only allow trusted senders.

Enterprise controls (managed settings, users can't override):
- `channelsEnabled: true` — master switch.
- `allowedChannelPlugins: [{marketplace, plugin}, ...]` — replaces the Anthropic allowlist with your own.

Comparison with related features:
- **Claude Code on web**: fresh cloud sandbox per task.
- **Claude in Slack**: spawns web session from `@Claude` mention.
- **Standard MCP server**: Claude pulls from it on demand; nothing pushed.
- **Remote Control**: drive your local session from claude.ai or mobile.

Channels fill the gap of pushing external events into your already-running local session.
