---
type: summary
source: 01_Raw/code.claude.com/docs/en/changelog.md
source_url: https://code.claude.com/docs/en/changelog
title: "Claude Code Changelog"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Plugin-marketplace, Skill, Subagent, MCP-server, Permission-mode, Auto-mode, Settings, Sandboxing, Memory, Slash-command, Status-line, IDE-integration, Native-interface, Headless-mode, Agent-SDK]
concepts_referenced: [Agent-team]
---

Mirror of `CHANGELOG.md` from the `anthropics/claude-code` GitHub repo. The doc is large (~283 KB) — a single chronological list of `<Update label="2.1.x" description="...">` blocks running through Claude Code 2.x point releases. Run `claude --version` to check installed version.

**Entries are dense, multi-bullet, per-version notes** covering every functional area of Claude Code. Recent (Apr–May 2026) themes worth remembering as research starting points:

- **Plugin/marketplace**: `claude plugin prune`, `plugin uninstall --prune`, `claude plugin tag`, `claude plugin validate` accepting `$schema`/`version`/`description`, `blockedMarketplaces`/`strictKnownMarketplaces` enforcement on install/update, plugin themes via `themes/` dir, plugin dependency auto-resolution.
- **Hooks**: `PostToolUse.hookSpecificOutput.updatedToolOutput` extended from MCP-only to ALL tools; hooks can invoke MCP tools directly via `type: "mcp_tool"`; agent-frontmatter `hooks:` fire for `--agent` main-thread agents; `PostToolUse`/`PostToolUseFailure` inputs include `duration_ms`.
- **Skills**: type-to-filter search in `/skills`; skills can reference current effort via `${CLAUDE_EFFORT}`; `claude_code.skill_activated` OTel event with `invocation_trigger` attribute.
- **Permission/auto mode**: `--dangerously-skip-permissions` no longer prompts on `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, shell config; auto mode `"$defaults"` keyword to extend rather than replace built-ins; "Don't ask again" on auto-mode opt-in.
- **MCP**: `alwaysLoad` server-config option (skip tool-search deferral); claude.ai connector dedup; faster startup with parallel server connect; X.509 mTLS Workload Identity Federation on Vertex.
- **Subagents / agent teams**: forked subagents work in non-interactive mode with `CLAUDE_CODE_FORK_SUBAGENT=1`; `Agent` tool `isolation: "worktree"` worktree reuse fixed.
- **Models**: Opus 4.7 native 1M context window now respected (was incorrectly assuming 200K); default effort raised to `high` for Pro/Max on Opus 4.6 / Sonnet 4.6.
- **OpenTelemetry**: many new attributes and events — `at_mention`, `tool_use_id`, `tool_input_size_bytes`, `effort`, `stop_reason`, `gen_ai.response.finish_reasons`, `user_system_prompt` (gated), `command_name`/`command_source`.
- **Native (macOS/Linux) builds**: Glob/Grep replaced by embedded `bfs`/`ugrep` via Bash tool; many memory leak / file descriptor fixes in long sessions.
- **Windows**: PowerShell becomes primary shell when Git for Windows absent; clipboard write hardening; better detection of MS Store / MSI / .NET-tool PowerShell installs.
- **Code Review (managed service)**: `Claude Code Review` check run with neutral conclusion; severity machine-readable in check-run text.
- **Web/Desktop**: `--from-pr` accepts GitLab MR / Bitbucket PR / GHE URLs; PR shorthand `owner/repo#N` honors git remote host; `prUrlTemplate` setting for custom code-review hosts.
- **`/usage`** consolidates `/cost` and `/stats`; settings now stored in `~/.claude/settings.json` and participate in scope precedence.

Use this changelog as a research index for "when was X introduced" and "what bug versions to avoid." Specific breaking changes worth flagging: SDK rename to Claude Agent SDK; defaults reverted on `settingSources` (load by default again); `cleanupPeriodDays` retention now sweeps tasks, shell-snapshots, backups directories.
