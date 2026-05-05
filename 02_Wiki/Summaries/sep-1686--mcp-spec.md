---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1686-tasks.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1686-tasks.md
title: "SEP-1686: Tasks (long-running request augmentation)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-10-20 | Authors: Surbhi Bansal, Luca Chang**

Introduces the **task primitive**: a generic mechanism for augmenting any MCP request with a `taskId` that enables call-now/fetch-later execution patterns. Critical for long-running tools where dropping/timing out blocks the agent. Adopted in the November 2025 spec release as **experimental capability**.

**Problem addressed**: today, if a tool call drops, clients can't query "is it still running?" — and they can't retrieve results after completion. Servers wrapping workflow APIs (AWS Step Functions, GCP Workflows, CI/CD) currently split into 3-tool patterns (`start_X` / `get_X_status` / `get_X_result`) that agents poll inconsistently. Real customer use cases documented: healthcare/life-sciences data analysis, enterprise automation, code migration, test execution, deep research, multi-agent communication.

**Design**: tasks are **generic** (work with any request type — `tools/call`, `resources/read`, `prompts/get`, `sampling/createMessage`, future types) and **metadata-based** (use `_meta` rather than dedicated parameters — keeps separation between request semantics and execution tracking). Client-generated task IDs enable idempotent retries.

**Protocol additions**:
- Augment any request with `_meta: { "modelcontextprotocol.io/task": { taskId, keepAlive? } }`
- New `notifications/tasks/created` (sent immediately after task creation, eliminates race condition where client polls before task exists)
- New methods: `tasks/get` (status), `tasks/result` (only when status `completed`), `tasks/list` (paginated), `tasks/delete`
- `notifications/cancelled` on the original request ID transitions task to `cancelled`
- All related messages MUST include `modelcontextprotocol.io/related-task` in `_meta`

**Status lifecycle**: `submitted` → `working` / `input_required` → terminal (`completed` / `failed` / `cancelled` / `unknown`). `input_required` used when an elicitation/sampling request is pending.

**Capabilities**: `tasks` capability declared by client/server, structured by request category with boolean properties indicating which request types support tasks.

**Behavior requirements**: keepAlive overrideable; `pollFrequency` (ms) suggested by server; receivers MUST scope task IDs (bind to session/auth context to prevent cross-tenant leak); rate limiting; audit logging.

**Rationale**: rejected tool-specific async (#1391) and resource-based tracking and pure transport-layer solutions in favor of a generic data-layer primitive. Future work: push notifications, intermediate results, nested task hierarchies. Fully backward compatible (no version negotiation needed; servers ignore `_meta` task fields when not supported).
