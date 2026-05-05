---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/overview.md
source_url: https://code.claude.com/docs/en/agent-sdk/overview
title: "Agent SDK overview"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Hooks, Subagent, MCP-server, Skill, Slash-command, Memory, Plugin, Permission-mode]
concepts_referenced: [Agentic-loop, Tool-use]
---

The Claude Agent SDK (formerly Claude Code SDK — see migration guide) is the Python and TypeScript library for building production AI agents with the same tools, agent loop, and context management that power Claude Code.

**Install**: `npm install @anthropic-ai/claude-agent-sdk` or `pip install claude-agent-sdk`. TS bundles a native Claude Code binary as optional dep — no separate Claude Code install. Auth via `ANTHROPIC_API_KEY`, or `CLAUDE_CODE_USE_BEDROCK=1` / `CLAUDE_CODE_USE_VERTEX=1` / `CLAUDE_CODE_USE_FOUNDRY=1` for third-party providers. Anthropic does NOT permit third-party developers to offer claude.ai login or rate limits for SDK-built products.

**Version note**: Opus 4.7 (`claude-opus-4-7`) requires Agent SDK v0.2.111+ — older versions fail with `thinking.type.enabled` API error.

**Core API**: `query({prompt, options})` returns async iterator yielding messages (assistant text, tool calls, tool results, final ResultMessage).

**Capabilities** (all Claude Code features available):
- **Built-in tools**: Read, Write, Edit, Bash, **Monitor** (watch background script, react per output line), Glob, Grep, WebSearch, WebFetch, AskUserQuestion
- **Hooks**: callback functions at lifecycle points — `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, `SessionEnd`, `UserPromptSubmit`, etc. Use `HookMatcher(matcher="Edit|Write", hooks=[...])`.
- **Subagents**: `agents={"name": AgentDefinition(description, prompt, tools)}`. Include `Agent` in allowedTools. Messages from subagent context include `parent_tool_use_id`.
- **MCP**: `mcpServers={...}`
- **Permissions**: `allowedTools`, `permissionMode`
- **Sessions**: capture `session_id` from `system/init` message, resume via `options.resume` to continue with full context. Sessions persist as JSONL on filesystem.

**Filesystem features** (loaded from `.claude/` and `~/.claude/` by default; restrict via `setting_sources`): Skills (`.claude/skills/*/SKILL.md`), Slash commands (`.claude/commands/*.md`), Memory (`CLAUDE.md`), Plugins (programmatic).

**SDK vs others**:
- **Client SDK**: you implement the tool loop; Agent SDK runs it for you.
- **Claude Code CLI**: same capabilities, different interface; CLI for interactive, SDK for CI/CD/production.
- **Managed Agents**: hosted REST API, runs on Anthropic infra with managed sandbox per session; Agent SDK runs in your process on your filesystem. Common path: prototype locally with SDK, productize with Managed Agents.

**Branding** for partners: "Claude Agent" preferred; "Claude Code" branding NOT permitted in third-party products.
