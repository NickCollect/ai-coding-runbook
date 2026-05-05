---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/examples/session_stores/README.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/examples/session_stores/README.md
title: "Claude Agent SDK Python — examples/session_stores/README"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Session-API, Memory-store]
concepts_referenced: []
---

Reference `SessionStore` adapter implementations under `examples/session_stores/` of `claude-agent-sdk-python`. Each is meant as copy-in code, not a packaged dependency. They are kept in `examples/` so the SDK package itself stays free of heavyweight optional dependencies, and they are exercised by the test suite to prove the `SessionStore` protocol generalizes beyond the in-memory default. Each passes the full 13-contract conformance suite (`run_session_store_conformance` from `claude_agent_sdk.testing`).

Three reference adapters are shipped:

**S3 (`s3_session_store.py`).** Stores transcripts as JSONL part files under `s3://{bucket}/{prefix}{project_key}/{session_id}/part-{epochMs13}-{rand6}.jsonl`. Each `append()` writes a new part; `load()` lists, sorts, and concatenates them. Requires `boto3` (not an SDK dep). `delete()` is implemented but only called via `delete_session_via_store()`. The adapter never auto-deletes; configure S3 lifecycle policies for retention. Caveats: part-file ordering uses the client-side wall clock, so multiple writers with clock skew >1s may produce out-of-order `load()` results — use NTP or a single writer per session. >1000 part files paginate but latency grows linearly. Unit tests use `moto` to mock S3 in-process; live e2e suite runs against MinIO or any S3-compatible backend when `SESSION_STORE_S3_*` env vars are set. Mirrors the TypeScript SDK's S3 reference.

**Redis (`redis_session_store.py`).** Uses `redis.asyncio`. Key scheme: `{prefix}:{project_key}:{session_id}` list (main transcript), `{prefix}:{project_key}:{session_id}:{subpath}` lists (subagent transcripts), `{prefix}:{project_key}:{session_id}:__subkeys` set (subpath index), `{prefix}:{project_key}:__sessions` zset (session_id → mtime). Each `append()` is `RPUSH` plus index update in one `MULTI`; `load()` is `LRANGE 0 -1`. Client must be created with `decode_responses=True`. Caveats: set `maxmemory-policy noeviction` (eviction silently drops session data), lists are unbounded (implement TTL via `EXPIRE` if needed), Cluster requires `{...}` hash tags, derived `project_key`/`session_id` must not contain `:`. Unit tests use `fakeredis`; live e2e against a real Redis when `SESSION_STORE_REDIS_URL` is set.

**Postgres (`postgres_session_store.py`).** Uses `asyncpg`. Schema: one row per transcript entry in table `claude_session_store` with `(project_key, session_id, subpath, seq)` PK and a `jsonb` `entry` column. `append()` is a single multi-row `INSERT ... SELECT unnest($entries::jsonb[])`; `load()` is `SELECT entry ... ORDER BY seq`. Note this differs from the TypeScript SDK Postgres reference (different default table name, NULL vs `''` subpath sentinel, `created_at TIMESTAMPTZ` vs epoch-ms `mtime`); sharing a table across SDKs requires aligning the schema first. JSONB reorders object keys on read-back — explicitly allowed by the contract, which only requires deep-equal returns; `*_from_store` helpers hoist `"type"` to the first key when re-serializing. No in-process Postgres mock; tests are live-only and skip unless `SESSION_STORE_POSTGRES_URL` is set.

**Production checklist (all adapters).** `run_session_store_conformance` proves correctness, not resilience — load-test under expected throughput. `append()` failures are logged and emit a `MirrorErrorMessage` rather than blocking the conversation; monitor for these so silent mirror gaps don't go unnoticed. Local-disk transcripts under `CLAUDE_CONFIG_DIR` are swept independently by the CLI's `cleanupPeriodDays` setting.

Resume-from-store is supported via `ClaudeAgentOptions(session_store=store, resume="previous-session-id")` for all three adapters.
