---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/memory.md
source_url: https://platform.claude.com/docs/en/managed-agents/memory
title: "Using agent memory"
summarized_at: 2026-05-05
entities_referenced: [Memory-store, Managed-agent, Session-API]
concepts_referenced: []
---

How [[Managed-agent]] sessions can use **[[Memory-store]]** for persistent memory that survives across sessions: user preferences, project conventions, prior mistakes, domain context. Without memory stores, each session starts with a fresh context and anything learned is lost when the session ends. **Requires `managed-agents-2026-04-01` beta header.**

**Mechanism.** A memory store is a workspace-scoped collection of text documents optimized for Claude. When attached to a session, it's mounted as a directory inside the container. The agent reads/writes via the same file tools it uses for the rest of the filesystem; a note describing each mount is automatically added to the system prompt so the agent knows where to look. The standard agent toolset is required for these interactions—enable it during agent creation.

**Memory addressability.** Each memory in a store is addressed by a path and can be read or edited directly via the API or Console—useful for tuning, importing, exporting. Every change creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.

**Creating a store.** `POST /v1/memory_stores` with `name` and `description`. The description is **passed to the agent** to tell it what the store contains—write it for Claude to understand at a glance. Returns a `memstore_...` ID used when attaching.

```json
{"name": "User Preferences", "description": "Per-user preferences and project context."}
```

**Seeding (optional).** Pre-load a store with reference material before any agent runs. Example:
```json
{"path": "/formatting_standards.md", "content": "All reports use GAAP formatting. Dates are ISO-8601..."}
```
Useful for: formatting standards, glossaries, organizational conventions, baseline preferences—anything you don't want every session to discover from scratch.

**Attaching to a [[Session-API]] session.** Pass the store ID in the session's `memory_stores` array (or equivalent), so the directory is mounted into the container at session start. The mount path is documented to Claude via the auto-injected system-prompt note, so the agent knows where to read/write.

**Workspace scope.** Stores are shared across the workspace—all agents within the same workspace can attach to the same store. Use this for org-wide knowledge or per-team conventions; for per-user data, create a per-user store.

**Versioning + audit.** Memory versions are immutable. The version log gives full history of who/what wrote each change, which is critical for sensitive workflows where you need to roll back, review, or comply with audit requirements.

The page primarily walks through `POST /v1/memory_stores` (create) and `POST /v1/memory_stores/{id}/memories` (seed) in cURL, ant CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby. Additional CRUD on individual memories and version retrieval would be in the API reference; this guide focuses on the create + seed + attach lifecycle.
