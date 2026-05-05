---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-memory.md
title: "Managed Agents — Memory Stores"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Public beta. Memory stores — workspace-scoped collection of small text documents persisting across Managed Agent sessions. Beta header `managed-agents-2026-04-01` (auto-set by SDK on `client.beta.memory_stores.*` calls). Note: only first 80 lines sampled.

**Object model**:
| Object | ID prefix | Scope | Notes |
|---|---|---|---|
| Memory store | `memstore_...` | Workspace | Attach to sessions via `resources[]` |
| Memory | `mem_...` | Store | One text file, `path`-addressed (≤100KB; prefer many small files) |
| Memory version | `memver_...` | Memory | Immutable per mutation; `operation` ∈ created/modified/deleted |

Every mutation produces immutable memory version → audit trail + point-in-time rollback/redact.

**Create store**:
```python
store = client.beta.memory_stores.create(
    name="User Preferences",
    description="Per-user preferences and project context.",
)
```
**`description` is shown to the agent** — write for the model, not humans.

Other SDKs: TS `client.beta.memoryStores.create({...})`, Go `client.Beta.MemoryStores.New(ctx, ...)`.

**Operations**: `retrieve`/`update`/`list` (with `include_archived`, `created_at_{gte,lte}` filters)/`delete`/`archive`. Archive = read-only, existing attachments continue, no new attachments, no unarchive.

**Seed with content**:
```python
client.beta.memory_stores.memories.create(
    store.id, path="/formatting_standards.md",
    content="All reports use GAAP formatting...")
```
Returns 409 (`memory_path_conflict_error` with `conflicting_memory_id`) if path exists.

**Attach to session** (at create time only — `sessions.resources.add()` does NOT accept `memory_store`):
```python
session = client.beta.sessions.create(
    agent=agent.id, environment_id=environment.id,
    resources=[{
        "type": "memory_store",
        "memory_store_id": store.id,
        "access": "read_write",  # or "read_only"; default read_write
        "instructions": "User preferences and project context. Check before starting any task.",
    }])
```
- `access` enforced at filesystem level on the FUSE mount
- `instructions` ≤4096 chars; session-specific guidance in addition to store name/description

**Max 8 memory stores per session**. Multi-store pattern when different slices have different owners/lifecycles (e.g., one read-only shared + one read-write per-user).

**FUSE mount**: each store mounted at `/mnt/memory/<store-name>/`. Agent uses standard file tools (`bash`/`read`/`write`/`edit`/`glob`/`grep`) — no dedicated memory tools. Mount description (name/path/instructions/access) auto-injected into system prompt. Writes persist back + produce memory versions.

(Remainder covers host-side mutation API and more — not sampled.)
