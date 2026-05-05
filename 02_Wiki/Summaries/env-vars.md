---
type: summary
source: 01_Raw/code.claude.com/docs/en/env-vars.md
source_url: https://code.claude.com/docs/en/env-vars
title: "Environment variables"
summarized_at: 2026-05-05
entities_referenced: [Settings, MCP-server, Hooks, Sandboxing, Auto-mode, Fast-mode, Skill, Plugin, Memory, Subagent, Checkpointing, Enterprise-gateway]
concepts_referenced: [Prompt-caching, Extended-thinking, Context-window]
---

Comprehensive reference (200+ entries) for env vars controlling Claude Code. Set in shell or via `settings.json` `env` key. **Raw is essentially a giant table**; here are the high-impact groups.

**Authentication / endpoint**:
- `ANTHROPIC_API_KEY` — overrides subscription auth (always used in `-p` mode; prompt-approved once in interactive). `unset` to revert to subscription.
- `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL` (sets non-first-party → MCP tool search disabled by default; set `ENABLE_TOOL_SEARCH=true` if proxy forwards `tool_reference`)
- `CLAUDE_CODE_USE_BEDROCK|VERTEX|FOUNDRY|MANTLE`, `CLAUDE_CODE_SKIP_*_AUTH` (LLM gateway scenarios)
- `ANTHROPIC_BEDROCK_*`, `ANTHROPIC_VERTEX_*`, `ANTHROPIC_FOUNDRY_*` — provider-specific overrides
- `ANTHROPIC_BETAS`, `ANTHROPIC_CUSTOM_HEADERS` — per-request tweaks
- `CLAUDE_CODE_OAUTH_TOKEN`, `CLAUDE_CODE_OAUTH_REFRESH_TOKEN`+`CLAUDE_CODE_OAUTH_SCOPES`
- mTLS: `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`, `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`, `CLAUDE_CODE_CERT_STORE` (`bundled,system` default; native binary required for system store)

**Model config**: `ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_{HAIKU|SONNET|OPUS}_MODEL[_NAME|_DESCRIPTION|_SUPPORTED_CAPABILITIES]`, `ANTHROPIC_CUSTOM_MODEL_OPTION*`, `CLAUDE_CODE_SUBAGENT_MODEL`, `CLAUDE_CODE_EFFORT_LEVEL` (`low|medium|high|xhigh|max|auto`), `MAX_THINKING_TOKENS`, `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` (no effect on Opus 4.7 — always adaptive), `CLAUDE_CODE_DISABLE_THINKING`, `DISABLE_INTERLEAVED_THINKING`.

**Context / compaction**: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (default ~95%), `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, `CLAUDE_CODE_MAX_CONTEXT_TOKENS` (only with `DISABLE_COMPACT`), `CLAUDE_CODE_MAX_OUTPUT_TOKENS`, `DISABLE_AUTO_COMPACT` / `DISABLE_COMPACT`, `CLAUDE_CODE_DISABLE_1M_CONTEXT`.

**Tooling / behavior**: `CLAUDE_CODE_SIMPLE` (set by `--bare`), `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` (Opus 4.7 only), `CLAUDE_CODE_DISABLE_FAST_MODE`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY` / `CLAUDE_CODE_DISABLE_CLAUDE_MDS`, `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING`, `CLAUDE_CODE_DISABLE_CRON`, `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` (incl. `run_in_background` + Ctrl+B), `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS`, `CLAUDE_CODE_DISABLE_ATTACHMENTS` (`@` becomes plain text), `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL`, `CLAUDE_CODE_DISABLE_POLICY_SKILLS`, `CLAUDE_CODE_FORK_SUBAGENT` (forked subagents inherit full conversation context).

**Bash / process**: `BASH_DEFAULT_TIMEOUT_MS` (default 120000), `BASH_MAX_TIMEOUT_MS` (default 600000), `BASH_MAX_OUTPUT_LENGTH`, `CLAUDE_CODE_SHELL`, `CLAUDE_CODE_SHELL_PREFIX` (wraps Bash + hook + MCP stdio commands — useful for logging/auditing), `CLAUDE_CODE_GIT_BASH_PATH` (Windows), `CLAUDE_CODE_USE_POWERSHELL_TOOL`, `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR`, `CLAUDE_ENV_FILE` (script run before each Bash command in same shell — virtualenv/conda persistence).

**Security / sandboxing / scrubbing**: `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` (strips Anthropic + cloud creds from subprocess env; on Linux also runs Bash subprocesses in isolated PID namespace — side effect: `ps`/`pgrep`/`kill` can't see host processes), `CLAUDE_CODE_SCRIPT_CAPS` (per-session script-call limits when SCRUB enabled), `CLAUDE_CODE_PERFORCE_MODE` (refuses Edit/Write on files lacking owner-write — needs `p4 edit` first), `CLAUDE_CODE_MCP_ALLOWLIST_ENV` (stdio MCP servers get only baseline env + configured `env`).

**Telemetry / privacy**: `DISABLE_TELEMETRY` (Statsig), `DISABLE_ERROR_REPORTING` (Sentry), `DISABLE_FEEDBACK_COMMAND`, `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` (sets all the above + `DISABLE_AUTOUPDATER`), `CLAUDE_CODE_ATTRIBUTION_HEADER=0` (improves cache hit rate via LLM gateway).

**Session / state**: `CLAUDE_CONFIG_DIR` (default `~/.claude`), `CLAUDE_CODE_TMPDIR`, `CLAUDE_CODE_DEBUG_LOGS_DIR`, `CLAUDE_CODE_DEBUG_LOG_LEVEL` (`verbose|debug|info|warn|error`), `CLAUDE_CODE_SKIP_PROMPT_HISTORY` (ephemeral; not in resume/continue/up-arrow), `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` (SDK), `CLAUDE_CODE_TASK_LIST_ID` (cross-session task list sharing).

**Fullscreen / TUI**: `CLAUDE_CODE_NO_FLICKER` (= `tui` setting), `CLAUDE_CODE_DISABLE_MOUSE`, `CLAUDE_CODE_SCROLL_SPEED` (1-20; 3 ≈ vim), `CLAUDE_CODE_DISABLE_VIRTUAL_SCROLL`, `CLAUDE_CODE_TMUX_TRUECOLOR`, `CLAUDE_CODE_ACCESSIBILITY` (keep native cursor visible).

**Streaming / reliability**: `API_TIMEOUT_MS` (default 600000, max 2147483647), `CLAUDE_CODE_MAX_RETRIES` (default 10), `CLAUDE_ENABLE_BYTE_WATCHDOG`, `CLAUDE_ENABLE_STREAM_WATCHDOG` (only watchdog for Bedrock/Vertex/Foundry), `CLAUDE_STREAM_IDLE_TIMEOUT_MS` (default/min 5min), `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK`.

**SDK-only**: `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS` (no Explore/Plan in `-p` mode), `CLAUDE_AGENT_SDK_MCP_NO_PREFIX` (skip `mcp__<server>__` prefix), `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY`, `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` + `_TIMEOUT_MS`.

**Detection signals** (auto-set; read in scripts/hooks): `CLAUDECODE=1` (in spawned shells but NOT hooks/statusline), `CLAUDE_CODE_REMOTE=true` (cloud session), `CLAUDE_CODE_REMOTE_SESSION_ID`, `CLAUDE_CODE_TEAM_NAME`, `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`.

**Update/cmd hiding**: `DISABLE_AUTOUPDATER`, `DISABLE_UPDATES`, `DISABLE_INSTALLATION_CHECKS`, `DISABLE_DOCTOR_COMMAND`, `DISABLE_LOGIN/LOGOUT/UPGRADE/EXTRA_USAGE/INSTALL_GITHUB_APP_COMMAND`.

Caching: `DISABLE_PROMPT_CACHING[_HAIKU|_OPUS|_SONNET]`, `ENABLE_PROMPT_CACHING_1H` (subscription users default 1h; API/Bedrock/Vertex/Foundry must opt in; 1h writes billed higher), `FORCE_PROMPT_CACHING_5M`.

**Plugin management**: `CLAUDE_CODE_PLUGIN_CACHE_DIR` (default `~/.claude/plugins`), `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` (default 120000), `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE`, `CLAUDE_CODE_PLUGIN_SEED_DIR` (`:`-sep on Unix, `;` Windows — pre-populate for containers).

Note: raw lists ~200 vars total. The above captures most actionable patterns; for comprehensive lookup refer back to raw.
