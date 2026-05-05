---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/api.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/api.md
title: "Anthropic SDK Python — api.md (resource & method reference)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Messages-API, Token-counting, Batches-API, Files-API, Citations-API, Vision, PDF-support, Code-execution-tool, Web-search-tool, Web-fetch-tool, Memory-tool, Text-editor-tool, Bash-tool-API, Computer-use-tool-API, Tool-search-tool-API, Tool-runner, Advisor-tool, Managed-agent, Session-API, Memory-store, Vault, Skill-API, User-profile, Admin-API, Workspace, API-key, Cost-report, Usage-report, Rate-limit-API, Invite]
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching]
---

Auto-generated reference of every resource and method exposed by the `anthropic` Python SDK, with links to the underlying typed param and response models. Covers the synchronous and async clients (`Anthropic`, `AsyncAnthropic`) and is organized by API surface.

**Top-level Messages.** `client.messages.create()` is the main chat-completion entry point. Shared types span error envelopes (`AuthenticationError`, `BillingError`, `OverloadedError`, `RateLimitError`, …) and the full content-block taxonomy: text/tool-use/tool-result/thinking/redacted-thinking blocks, document/PDF/image sources, server-tool blocks (`ServerToolUseBlock`, `ServerToolCaller`), citation blocks (page/char/content-block/search-result/web-search variants), JSON-output and structured-output configs, tool-choice modes, sub-tool types for Bash/TextEditor/Code-execution/Memory/Tool-search server tools, thinking config (adaptive/disabled/enabled), and the raw streaming events (`RawMessageStartEvent`, `RawContentBlockDeltaEvent`, `RawMessageStopEvent`, plus deltas for text, input JSON, signature, citations, thinking).

**Token counting.** `client.messages.count_tokens()` for `/v1/messages/count_tokens` returning `MessageTokensCount`.

**Batches.** `client.messages.batches.{create,retrieve,list,cancel,delete,results}` map to `/v1/messages/batches` for asynchronous bulk processing.

**Models.** `client.models.{retrieve,list}`.

**Beta surfaces (under `client.beta`)** mirror the public ones with extra preview functionality:
- `beta.messages.{create, count_tokens, batches, tool_runner}` — `tool_runner` is the iterator-style tool-call loop covered in `tools.md` and `helpers.md`.
- `beta.files` — `/v1/files`: list, retrieve metadata, upload, delete, download.
- `beta.skills` and `beta.skills.versions` — beta Skill registry (`/v1/skills`, `/v1/skills/{id}/versions`).
- `beta.user_profiles` — end-user identity (`create`, `retrieve`, `update`, `list`, `create_enrollment_url`, plus trust-grant types).
- `beta.sessions` — managed-agent sessions including `events.{list,send,stream}` and `resources.{retrieve,update,list,delete,add}` for files/repos/memory-store attachments.
- `beta.vaults` — credential vaults with `create/retrieve/update/list/delete/archive`, plus nested `credentials` for static bearer tokens, MCP OAuth (with refresh), and token-endpoint auth (basic/none/post variants).
- `beta.memory_stores` — `/v1/memory_stores` with nested `memories` (CRUD) and `memory_versions` (`retrieve`, `list`, `redact`).

**Admin API (`client.admin`).** Per-org/workspace administration: `organizations`, `workspaces`, `workspace_members`, `users`, `invites`, `api_keys`, `usage_report.{messages, code}`, `cost_report`, `rate_limits` — all mapping to `/v1/organizations/...` endpoints.

**Resource shape.** Every operation links to a `*_params.py` (typed input) and a return model. List endpoints return `SyncPageCursor[...]` or `SyncPage[...]`. Beta types are namespaced under `anthropic.types.beta...` and mirror their non-beta counterparts where applicable.

This file is the definitive low-level map used both for navigating the SDK source (each method links to the resource module under `src/anthropic/resources/...`) and for confirming which API features are wired up in the current SDK release.
