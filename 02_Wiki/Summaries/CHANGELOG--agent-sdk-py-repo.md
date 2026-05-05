---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/CHANGELOG.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md
title: "Claude Agent SDK Python — CHANGELOG"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Hooks, Sandboxing, Subagent, Session-API]
concepts_referenced: [Agentic-loop]
---

The Python Agent SDK changelog. Most patch releases (0.1.66–0.1.72) bundle a refreshed Claude CLI version (currently 2.1.126). Highlights from the most recent significant releases:

**0.1.71** — Added `allowedDomains`, `deniedDomains`, `allowManagedDomainsOnly`, `allowMachLookup` fields to `SandboxNetworkConfig`, achieving parity with the TypeScript schema and giving Python users typed network allowlists for sandbox config.

**0.1.70** — Bumped the `mcp` dependency floor to `>=1.19.0` because older versions mishandled `CallToolResult` returns from SDK MCP tool handlers, causing the model to receive a validation-error blob instead of the actual tool output. Also fixed Trio nursery corruption on early cancellation when `options.stderr` was set.

**0.1.67** — Restored Trio compatibility: fixed `RuntimeError: no running event loop` regression introduced in v0.1.51 by adding sniffio-based runtime dispatch between `asyncio.Task` and `trio.lowlevel.spawn_system_task`.

**0.1.65** — Added `SessionStore.list_session_summaries()` optional protocol method and `fold_session_summary()` helper for O(1)-per-session list views (reduces N round-trips to 1 for stores with append-time summary sidecars). Added `import_session_to_store()` for replaying a local on-disk session into any `SessionStore` adapter (enables migration from local to remote stores). Added `display` field to `ThinkingConfig` (forwarded as `--thinking-display`) so callers can override Opus 4.7's default `"omitted"` and receive summarized thinking text. Added `ServerToolUseBlock` and `AdvisorToolResultBlock` content block types so server-executed tool calls (e.g., `advisor`, `web_search`) and their results are no longer silently dropped. Fixed the related parser bug where `server_tool_use` and `advisor_tool_result` content blocks were dropped, which had caused server-only tool messages to arrive as empty `AssistantMessage(content=[])`. Corrected misleading `permission_mode` docstrings: `dontAsk` denies unapproved tools (was inverted), `auto` clarified as using a model classifier.

**0.1.64** — Full `SessionStore` adapter support at parity with the TypeScript SDK. Includes a `SessionStore` protocol (5 methods: `append`, `load`, `list_sessions`, `delete`, `list_subkeys`), `InMemorySessionStore` reference implementation, transcript mirroring via `--session-mirror`, session resume from store, and 9 new async store-backed helpers. Also adds a 13-contract conformance test harness at `claude_agent_sdk.testing.run_session_store_conformance` for third-party adapter authors. Reference adapters under `examples/session_stores/` cover S3 (JSONL part files), Redis (RPUSH/LRANGE + zset index), and Postgres (`asyncpg` + jsonb). Adapters are not shipped in the wheel; users copy in the file they need.

Earlier changes in the file extend further back through the 0.1.x series, but the entries above represent the recent feature- and bug-significant ones.
