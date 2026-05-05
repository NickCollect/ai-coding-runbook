---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta.md
source_url: https://platform.claude.com/docs/en/api/beta
title: "Beta"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Batches-API, Files-API, Managed-agent, Session-API, Environment-API, Memory-store, Vault, Skill-API, User-profile]
concepts_referenced: []
---

Aggregate reference for all `/v1/beta/...` endpoints. Auth via `X-Api-Key` plus `anthropic-version` and one or more `anthropic-beta` flag headers. Top-level resource groups (H1 sections in raw):

- **Beta** — domain types only; defines `AnthropicBeta` enum (24 values: `message-batches-2024-09-24`, `prompt-caching-2024-07-31`, `computer-use-2024-10-22`/`2025-01-24`, `pdfs-2024-09-25`, `token-counting-2024-11-01`, `token-efficient-tools-2025-02-19`, `output-128k-2025-02-19`, `files-api-2025-04-14`, `mcp-client-2025-04-04`/`2025-11-20`, `dev-full-thinking-2025-05-14`, `interleaved-thinking-2025-05-14`, `code-execution-2025-05-22`, `extended-cache-ttl-2025-04-11`, `context-1m-2025-08-07`, `context-management-2025-06-27`, `model-context-window-exceeded-2025-08-26`, `skills-2025-10-02`, `fast-mode-2026-02-01`, `output-300k-2026-03-24`, `user-profiles-2026-03-24`, `advisor-tool-2026-03-01`).
- **Models** — beta List/Retrieve mirroring stable API.
- **Messages** — beta Create + Count Tokens (same shape as stable, but accepts beta headers).
- **Batches** — beta Create / Retrieve / List / Cancel / Delete / Results under `/v1/beta/messages/batches`.
- **Agents (Managed-agent)** — Create / List / Retrieve / Update / Archive plus `Versions` sub-resource.
- **Environments (Environment-API)** — Create / List / Retrieve / Update / Delete / Archive (sandbox execution environments).
- **Sessions (Session-API)** — Create / List / Retrieve / Update / Delete / Archive plus `Events` (List, Send, Stream).
- **Resources** — Add / List / Retrieve / Update / Delete (session/agent attached resources).
- **Vaults** — Create / List / Retrieve / Update / Delete / Archive plus `Credentials` (Create / List / Retrieve / Update / Delete).
- **Memory Stores** — Create / List / Retrieve / Update / Delete plus `Memories` and `Memory Versions` lifecycles, including `Redact`.
- **Files (Files-API)** — Upload / List / Download / Retrieve Metadata.
- **Skills (Skill-API)** — Create / List / Retrieve / Update / Delete / Archive plus `Versions`.
- **User Profiles (User-profile)** — Create / List / Retrieve / Update / Delete (end-user identity for the API).

Each section follows the same pattern: REST verb, path, body/path/query parameters, returned domain type, cURL example. The doc is a 1.9 MB aggregation covering the entire beta surface; this summary serves as a navigation index — individual endpoints in the beta tree are not in this slice.
