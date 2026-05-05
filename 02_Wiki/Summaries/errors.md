---
type: summary
source: 01_Raw/code.claude.com/docs/en/errors.md
source_url: https://code.claude.com/docs/en/errors
title: "Error reference"
summarized_at: 2026-05-05
entities_referenced: [Auto-mode, Permission-mode, Settings, Memory, MCP-server, Subagent, Checkpointing, Native-interface, Enterprise-gateway]
concepts_referenced: [Context-window, Extended-thinking]
---

Catalog of runtime errors Claude Code surfaces and their fixes. Same errors apply across CLI, Desktop, Web (all wrap the same engine). Most errors map to underlying API status codes.

**Automatic retries**: server 5xx, 529 overloaded, request timeouts, transient 429, dropped connections retried up to 10× with exponential backoff (`Retrying in Ns · attempt x/y` countdown). Tunable: `CLAUDE_CODE_MAX_RETRIES` (default 10), `API_TIMEOUT_MS` (default 600000ms).

**Server errors**:
- `API Error: 500` — wait, retry, `/feedback` if persists with no incident
- `Repeated 529 Overloaded` — capacity is per-model; `/model` to switch
- `Request timed out` — break work into smaller prompts, raise `API_TIMEOUT_MS`
- `<model> is temporarily unavailable, so auto mode cannot determine the safety of...` — auto-mode classifier overloaded; reads/searches/edits inside cwd skip the classifier and keep working

**Usage limits** (account/plan, distinct from server errors):
- `You've hit your session/weekly/Opus limit · resets ...` — wait or `/extra-usage`
- `Server is temporarily limiting requests` — auto-retried short-lived throttle, not your usage limit
- `Request rejected (429)` — your account/Bedrock/Vertex rate limit. Lower `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`, fewer subagents, switch model
- `Credit balance is too low` — Console org out of prepaid credits; add credits or switch to subscription

**Authentication errors**:
- `Not logged in` — `/login`; check `ANTHROPIC_API_KEY` env if expected to authenticate
- `Invalid API key` — typo, revoked, or stale `.env` loaded by direnv/IDE
- `This organization has been disabled` — stale `ANTHROPIC_API_KEY` overriding subscription; `unset` and relaunch
- `OAuth token revoked` / `expired` — `/login`; if recurs in same session, `/logout` first
- `does not meet scope requirement: user:profile` — old token; `/login` to mint with current scopes

**Network errors** (almost always local):
- `Unable to connect to API (ECONNREFUSED|ECONNRESET|ETIMEDOUT)` / `fetch failed` — VPN blocking, missing proxy, broken DNS. Check `curl -I https://api.anthropic.com`. On Linux/WSL check `/etc/resolv.conf`. On macOS check stale `utun` interfaces from removed VPN. Docker Desktop can also intercept.
- `SSL certificate verification failed` — corp TLS interception; set `NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.pem`. **Don't** disable validation with `NODE_TLS_REJECT_UNAUTHORIZED=0`.

**Request errors**:
- `Prompt is too long` — `/compact` or `/clear`; `/context` to see breakdown; disable unused MCP servers; trim CLAUDE.md or use path-scoped rules. Subagents inherit MCP tool defs, can fill context before first turn.
- `Error during compaction: Conversation too long` — Esc twice to drop recent turns then `/compact` again, or `/clear`
- `Request too large (max 30 MB)` — HTTP body limit, separate from context window
- `Image was too large` — max 8000px longest edge for single image, 2000px when many in context. **Image stays in history**, so subsequent messages also fail until you Esc back past it.
- `PDF too large` (max 100 pages, 32 MB) / `password protected` / `not valid` — read by page range, or extract text with `pdftotext`
- `Extra inputs are not permitted` — gateway dropped `anthropic-beta` header. Configure gateway to forward, or set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.
- `There's an issue with the selected model` — wrong/unauthorized model. Use aliases (`sonnet`, `opus`) instead of full IDs. Check priority chain: `--model` flag → `ANTHROPIC_MODEL` env → `.claude/settings.local.json` → project `.claude/settings.json` → `~/.claude/settings.json`.
- `Claude Opus is not available with the Claude Pro plan` — recent upgrade? `/logout` then `/login` to refresh token's plan info
- `thinking.type.enabled is not supported for this model` — Claude Code older than v2.1.111 hitting Opus 4.7. `claude update`.
- `max_tokens must be greater than thinking.budget_tokens` — usually Bedrock/Vertex; lower `MAX_THINKING_TOKENS` or raise `CLAUDE_CODE_MAX_OUTPUT_TOKENS`
- `Tool use or thinking block mismatch` (400 — tool_use_id, thinking blocks cannot be modified) — corrupted history; `/rewind` or Esc twice

**Quality issues** with no error: check `/model`, `/effort`, `/context` (compaction pressure), `/doctor` (oversized memory). Rewind with Esc-twice or `/rewind` to before the bad turn rather than correcting in-thread (which anchors later answers to the mistake).

`/feedback` sends transcript + description to Anthropic — fastest way to report a regression. Unavailable on Bedrock/Vertex/Foundry.
