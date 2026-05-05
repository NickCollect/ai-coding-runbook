---
type: summary
source: 01_Raw/github/anthropics/claude-code/CHANGELOG.md
title: "Claude Code CLI Changelog (github.com/anthropics/claude-code)"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Hooks, Plugin, Subagent, Skill, MCP-server, Auto-mode, Sandboxing, Settings, Memory, Checkpointing, Output-style, Plugin-marketplace, Enterprise-gateway]
concepts_referenced: [Prompt-caching, Extended-thinking, Headless-mode]
---

The official `anthropics/claude-code` repo's CHANGELOG.md — release-by-release notes. Note: this is a different perspective than the docs `whats-new` digests (which group by week with curated highlights); this is per-version.

**Note**: only first ~200 lines (versions 2.1.118 → 2.1.126) sampled. Earlier versions exist below in raw.

**Most-recent versions covered**:

**v2.1.126** (latest sampled):
- `/model` picker lists models from `ANTHROPIC_BASE_URL` gateway's `/v1/models` endpoint
- `claude project purge [path]` — delete all Claude Code state for project (transcripts, tasks, file history, config). `--dry-run`, `-y`, `-i`, `--all`
- `--dangerously-skip-permissions` now also bypasses `.claude/`, `.git/`, `.vscode/`, shell config writes (catastrophic removals still prompt)
- `claude auth login` accepts pasted OAuth code when browser callback unreachable (WSL2/SSH/containers)
- `claude_code.skill_activated` OTel event now fires for user-typed slash commands; new `invocation_trigger` attribute (`user-slash`/`claude-proactive`/`nested-skill`)
- Auto mode: spinner turns red when permission check stalls
- Host-managed deployments (`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`) no longer auto-disable analytics on Bedrock/Vertex/Foundry
- Windows: PowerShell 7 detected via Microsoft Store / MSI without PATH / .NET global tool; PowerShell tool enabled → primary shell instead of Bash
- **Security**: fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` ignored when higher-priority managed source lacked `sandbox` block
- Many fixes: image >2000px breaking session (now downscaled on paste), OAuth login on slow/proxied/IPv6, race on credential clearing valid OAuth refresh token, "Stream idle timeout" after Mac sleep, plugin uninstall reporting "Enabled", deferred tools unavailable to skills with `context: fork` on first turn, plan-mode tools missing in `--channels` sessions, CJK rendering on Windows no-flicker mode, `Ctrl+L` clearing prompt, etc.

**v2.1.123**: Fix OAuth 401 retry loop with `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.

**v2.1.122**: New `ANTHROPIC_BEDROCK_SERVICE_TIER` env (`default|flex|priority`); `/resume` paste PR URL finds session that created it (GH/GHE/GitLab/Bitbucket); MCP claude.ai connector dedup hint; OTel `at_mention` log event. Many fixes (Bedrock/Vertex `output_config` issues; image resize 2576→2000 fix; remote-control redraw flooding tmux -CC).

**v2.1.121**: `alwaysLoad` MCP option (skip tool-search deferral); `claude plugin prune` (and `uninstall --prune` cascades); `/skills` type-to-filter; PostToolUse hook `hookSpecificOutput.updatedToolOutput` for ALL tools (was MCP-only); fullscreen scroll position preserved while typing; SDK `CLAUDE_CODE_FORK_SUBAGENT` works in non-interactive; X.509 mTLS ADC for Vertex; SDK `mcp_authenticate` `redirectUri`; OTel adds `stop_reason`, `gen_ai.response.finish_reasons`, `user_system_prompt` (gated by `OTEL_LOG_USER_PROMPTS`). Fixes: unbounded memory on many images, `/usage` 2GB leak, Bash tool break when start dir deleted/moved, claude.ai connectors silently disappearing on transient auth errors, `--resume` crash on corrupted transcript line.

**v2.1.120**: Windows — Git for Windows no longer required (uses PowerShell); `claude ultrareview [target]` non-interactive subcommand (`--json`); skills `${CLAUDE_EFFORT}` substitution; `AI_AGENT` env var for subprocesses (gh attribution); `claude plugin validate` accepts `$schema`/`version`/`description` at top level. Many fixes (Esc canceling stdio MCP server connection, `--resume` overlay nonresponsive, false dangerous-rm prompts in auto mode for multi-line bash with pipe+redirect, `find` exhausting fds on large dirs).

**v2.1.119**: `/config` settings (theme/editor mode/verbose) persist to `~/.claude/settings.json` with project/local/policy precedence; `prUrlTemplate` setting for custom PR URL; `CLAUDE_CODE_HIDE_CWD` env; `--from-pr` accepts GitLab/Bitbucket/GHE URLs; `--print` honors agent's `tools:`/`disallowedTools:`; PowerShell tool auto-approve; PostToolUse hook input includes `duration_ms`; subagent/SDK MCP reconnect parallelized. Fixes: CRLF paste extra blank lines, kitty keyboard protocol newline loss in bracketed paste, Glob/Grep disappearing when Bash denied on native macOS/Linux, async PostToolUse hooks with no payload writing empty transcript entries.

**v2.1.118**: vim visual mode (`v`) and visual-line (`V`) with selection/operators; `/cost` + `/stats` merged into `/usage` (both remain as shortcuts); custom themes via `/theme` or hand-edit `~/.claude/themes/`; plugins ship themes via `themes/`; hooks can invoke MCP tools via `type: "mcp_tool"`; new `DISABLE_UPDATES` env (stricter than `DISABLE_AUTOUPDATER`); `wslInheritsWindowsSettings` policy key; auto-mode `"$defaults"` token to extend rather than replace built-in lists; `/model` picker honors `ANTHROPIC_DEFAULT_*_MODEL_NAME`/`_DESCRIPTION` overrides under custom gateway.
