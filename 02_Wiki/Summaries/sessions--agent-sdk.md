---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/sessions.md
source_url: https://code.claude.com/docs/en/agent-sdk/sessions
title: "Work with sessions"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Checkpointing]
concepts_referenced: [Agentic-loop, Context-window]
---

A session = full conversation history (prompt + every tool call/result + every response) auto-persisted to disk under `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` (`<encoded-cwd>` is absolute cwd with non-alphanumerics replaced by `-`). Sessions persist conversation only — for filesystem rollback see [file checkpointing](https://code.claude.com/docs/en/agent-sdk/Checkpointing).

**Three operations** on `query()` options:
- **Continue** (`continue: true` TS / `continue_conversation=True` Py) — finds most recent session in cwd. No ID handling. Survives process restart.
- **Resume** (`resume=<id>`) — explicit session ID. Required for multi-user apps or resuming non-most-recent.
- **Fork** (`forkSession: true` TS / `fork_session=True` Py, combined with `resume`) — creates a new session that copies original history but diverges from that point. Original untouched. Two independent IDs result.

**Automatic session management**:
- Python: `ClaudeSDKClient` async context manager — `client.query()` continues internally across calls, no ID tracking.
- TypeScript stable V1 (`query()`): use `continue: true` per call. There's a V2 preview with `createSession()` / `send` / `stream` closer to Python's pattern, but unstable.

**Capture session ID** from `ResultMessage.session_id` (always present). TS also exposes it on init `SystemMessage`; Py nests inside `SystemMessage.data`.

**Common reasons to resume**: follow up on completed analysis, recover from `error_max_turns` / `error_max_budget_usd`, restart your process.

**Gotcha**: if `resume` returns a fresh session, most likely cause is mismatched `cwd` — the encoded path must match. Session file must exist on the current machine.

**Cross-host resume**: either move the `.jsonl` file to the same path on the new host, or capture results as application state and prime a fresh session. For serverless/CI use a `SessionStore` adapter to mirror to shared storage.

**TS-only stateless option**: `persistSession: false` keeps session in memory only. Python always persists.

Both SDKs expose: `listSessions` / `list_sessions`, `getSessionMessages` / `get_session_messages`, `getSessionInfo` / `get_session_info`, `renameSession` / `rename_session`, `tagSession` / `tag_session`.

Forking branches conversation history, NOT filesystem — file edits in a fork are real and visible to other sessions in the same dir.
