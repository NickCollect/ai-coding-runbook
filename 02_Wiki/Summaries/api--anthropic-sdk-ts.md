---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-typescript/api.md
source_url: https://github.com/anthropics/anthropic-sdk-typescript/blob/main/api.md
title: "Anthropic SDK TypeScript — api.md (resource & method reference)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-TypeScript, Messages-API, Token-counting, Batches-API, Files-API, Citations-API, Vision, PDF-support, Code-execution-tool, Web-search-tool, Web-fetch-tool, Memory-tool, Text-editor-tool, Bash-tool-API, Computer-use-tool-API, Tool-search-tool-API, Tool-runner, Advisor-tool, Managed-agent, Session-API, Memory-store, Vault, Skill-API, User-profile, Admin-API, Workspace, API-key, Cost-report, Usage-report, Rate-limit-API, Invite]
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching]
---

Auto-generated reference of every resource and method exposed by `@anthropic-ai/sdk`, with links to the typed source files. Mirrors the Python SDK's `api.md` in structure and coverage.

**Shared error envelope types.** `APIErrorObject`, `AuthenticationError`, `BillingError`, `ErrorObject`, `ErrorResponse`, `ErrorType`, `GatewayTimeoutError`, `InvalidRequestError`, `NotFoundError`, `OverloadedError`, `PermissionError`, `RateLimitError` — all in `src/resources/shared.ts`.

**Messages.** The `client.messages.create()` API is the main chat-completion entry point. Types span the full content-block taxonomy (`Base64ImageSource`, `Base64PDFSource`, `BashCodeExecutionOutputBlock`/`...ResultBlock`/`...ToolResultBlock`/`...Error`, `CacheControlEphemeral`, `CacheCreation`, citation blocks for char/page/content-block/search-result/web-search locations, `CodeExecutionTool20250522`/`...20250825`/`...20260120` versions, `Container`/`ContainerUploadBlock`, `ContentBlock`/`ContentBlockParam`/`ContentBlockStartEvent`/`ContentBlockStopEvent`, `DocumentBlock`, `EncryptedCodeExecutionResultBlock`, `ImageBlockParam`, `InputJSONDelta`, `JSONOutputFormat`, …). Streaming events live alongside the message types.

**Token counting.** `client.messages.countTokens()` for the count-tokens endpoint.

**Batches.** `client.messages.batches.{create, retrieve, list, cancel, delete, results}` for asynchronous bulk processing.

**Models.** `client.models.{retrieve, list}`.

**Beta surfaces (under `client.beta`).** Mirror the public ones with extra preview functionality:
- `beta.messages.{create, countTokens, batches, toolRunner}` — `toolRunner` is the iterator-style tool-call loop covered in `helpers.md`.
- `beta.files` — list, retrieveMetadata, upload, delete, download.
- `beta.skills` and `beta.skills.versions` — beta Skill registry.
- `beta.userProfiles` — end-user identity (create, retrieve, update, list, createEnrollmentURL, plus trust-grant types).
- `beta.sessions` with nested `events.{list, send, stream}` and `resources.{retrieve, update, list, delete, add}` for managed-agent sessions.
- `beta.vaults` with nested `credentials` for static bearer tokens, MCP OAuth (with refresh), and token-endpoint auth (basic/none/post variants).
- `beta.memoryStores` with nested `memories` (CRUD) and `memoryVersions` (`retrieve`, `list`, `redact`).

**Admin API (`client.admin`).** Per-org/workspace administration: `organizations`, `workspaces`, `workspaceMembers`, `users`, `invites`, `apiKeys`, `usageReport.{messages, code}`, `costReport`, `rateLimits` mapping to `/v1/organizations/...` endpoints.

**Resource shape.** Each operation links to its typed param and response model in `src/resources/...ts`. List endpoints return paginated `Page` objects (cursor or page-based) typed to the entity. Beta types are namespaced under `Anthropic.Beta...` and mirror their non-beta counterparts where applicable.

This file is the definitive low-level map for navigating the SDK source and confirming which API features are wired up in the current SDK release. Output structure and entity parity match the Python `api.md`.
