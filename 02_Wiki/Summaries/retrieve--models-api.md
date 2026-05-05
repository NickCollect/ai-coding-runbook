---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/models/retrieve.md
source_url: https://platform.claude.com/docs/en/api/models/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: []
---

`GET /v1/models/{model_id}` — fetch a single model's full info given either its canonical model ID (e.g. `claude-opus-4-7`) or an alias. Common use: resolving an alias to the underlying ID before using it elsewhere, or inspecting a specific model's capabilities to gate features in client code.

Path parameter: `model_id: string` — model identifier or alias.

Header parameters: standard `anthropic-version: 2023-06-01` plus optional `anthropic-beta` accepting the same 24-value beta-flag enum as the rest of the API surface (caching, computer-use, pdfs, token-counting, files, mcp-client, thinking, code-execution, context management, skills, fast-mode, output-300k, user-profiles, advisor-tool, etc.).

Response: a `ModelInfo` object identical in shape to entries in the List response:
- `id`, `display_name`, `type:"model"`.
- `created_at` — RFC 3339 release date (may be epoch if unknown).
- `max_input_tokens` — context-window size.
- `max_tokens` — max value for the request `max_tokens` parameter.
- `capabilities` — full `ModelCapabilities`: `batch`, `citations`, `code_execution`, `image_input`, `pdf_input`, `structured_outputs`, `context_management` (`clear_thinking_20251015`, `clear_tool_uses_20250919`, `compact_20260112`), `effort` (`low`/`medium`/`high`/`max`/`xhigh`), `thinking` (`adaptive`, `enabled`). Each capability is a `CapabilitySupport` object exposing a `supported: boolean`.

Auth: `X-Api-Key`. No body or query parameters. cURL example provided.
