---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/migration-guide.md
source_url: https://code.claude.com/docs/en/agent-sdk/migration-guide
title: "Migrate to Claude Agent SDK"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Memory, Settings]
concepts_referenced: []
---

The Claude Code SDK has been renamed to **Claude Agent SDK** to reflect a broader scope (business agents, SRE bots, customer support, etc., not just coding). Doc location moved from Claude Code docs to the API Guide's Agent SDK section.

**Package renames**:
- TS/JS: `@anthropic-ai/claude-code` → `@anthropic-ai/claude-agent-sdk` (new version `^0.2.0`)
- Python: `claude-code-sdk` → `claude-agent-sdk`

**TS migration**: uninstall old, install new, change all imports. No code changes otherwise.

**Python migration**: uninstall, install, change imports from `claude_code_sdk` to `claude_agent_sdk`, AND rename the type `ClaudeCodeOptions` → `ClaudeAgentOptions`.

**Breaking changes in v0.1.0**:

1. **`ClaudeCodeOptions` → `ClaudeAgentOptions`** (Python type rename).
2. **System prompt no longer default**: SDK now uses a minimal system prompt. To restore the old behavior, pass `systemPrompt: { type: "preset", preset: "claude_code" }` or supply a custom string. Reason: better isolation for non-coding agents.
3. **Settings sources no longer loaded by default**: SDK no longer auto-reads `~/.claude/settings.json`, project `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md, or custom slash commands. To restore: pass `settingSources: ["user", "project", "local"]` (or a subset). Reason: predictable behavior in CI/CD, deployment, testing, multi-tenant systems.

**Important reversal note**: Current SDK releases have REVERTED that default for `query()` — omitting `settingSources` again loads user/project/local, matching the CLI. Pass `settingSources: []` (TS) / `setting_sources=[]` (Python) for the isolated behavior. Python SDK 0.1.59 and earlier treated empty list same as omitting; upgrade required to rely on it. Some inputs are still read even with `settingSources: []` (see `claude-code-features` doc).
