---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool
title: "Web fetch tool"
summarized_at: 2026-05-05
entities_referenced: [Web-fetch-tool, Tool-use, Web-search-tool, Code-execution-tool, Citations-API, Batches-API, Streaming-API]
concepts_referenced: []
---

The [[Web-fetch-tool]] retrieves full content from specified web pages and PDF documents. Latest version `web_fetch_20260209` supports **dynamic filtering** with Claude Mythos Preview, Opus 4.7/4.6, Sonnet 4.6—Claude can write and execute code (via [[Code-execution-tool]]) to filter fetched content before it reaches the context window. Previous version `web_fetch_20250910` remains available without dynamic filtering.

**Server-executed.** Available on Claude API and Microsoft Azure (Mythos Preview also on those two; not Bedrock or Vertex). Basic version is **ZDR-eligible**; the `_20260209` version with dynamic filtering is not by default but can use `allowed_callers: ["direct"]` to disable filtering and become ZDR-eligible.

**Security warning.** Enabling web fetch where Claude processes untrusted input alongside sensitive data poses **data exfiltration risks**. Mitigations built in: Claude is **not allowed to dynamically construct URLs**—can only fetch URLs that were explicitly provided by the user or that came from previous web search/fetch results (URLs from container-based server tools like Code Execution, Bash, etc., do NOT qualify). Recommended: disable entirely if exfiltration is a concern, use `max_uses` to cap requests, use `allowed_domains` to restrict to known safe domains.

**Mechanism.** Claude decides when to fetch based on prompt + available URLs. API retrieves full text. PDFs get automatic text extraction. Claude analyzes and responds, optionally with [[Citations-API]] enabled. Does NOT support websites dynamically rendered via JavaScript.

**Tool parameters.**
```json
{
  "type": "web_fetch_20250910", "name": "web_fetch",
  "max_uses": 10,
  "allowed_domains": ["example.com"],
  "blocked_domains": ["private.example.com"],
  "citations": {"enabled": true},
  "max_content_tokens": 100000
}
```
- `max_uses`: hits an `error_code: "max_uses_exceeded"` error when exceeded; no default.
- `allowed_domains` / `blocked_domains`: see Server tools page for syntax (no scheme, wildcards in path only).
- `citations.enabled`: optional for web fetch (UNLIKE [[Web-search-tool]] where citations are always on).
- `max_content_tokens`: caps fetched content in context (approximate—small variance).

**Response shape.** Sequence: text ("I'll fetch the content...") → `server_tool_use` with the URL → `web_fetch_tool_result` with `content` (a `document` block with text/PDF source, title, citations metadata, `retrieved_at` timestamp) → Claude's analysis with citation blocks pointing back to specific char ranges.

For PDFs, content returns as base64-encoded `application/pdf`. The fetch tool **caches** results for performance—content may not always be the latest at the URL.

**Errors (200 status, error in body).** `invalid_input`, `url_too_long` (>250 chars), `url_not_allowed` (blocked by domain rules + model restrictions), `url_not_accessible` (HTTP failure), `too_many_requests`, `unsupported_content_type` (only text + PDF), `max_uses_exceeded`, `unavailable`.

**Combined search + fetch pattern.** Common: `web_search` (`max_uses: 3`) + `web_fetch` (`max_uses: 5`, `citations.enabled: true`). Workflow: search finds candidates → Claude picks promising ones → fetch retrieves full content → Claude provides detailed analysis with citations.

**Citations.** "When displaying API outputs directly to end users, citations must be included to the original source." If you modify or recombine outputs, consult legal team about display requirements.

**Pricing.** **No additional charges** beyond standard token costs—you only pay for the fetched content tokens. Reported as `usage.server_tool_use.web_fetch_requests`. Sample token costs: avg web page (10 KB) ~2,500 tokens; large doc page (100 KB) ~25,000; research paper PDF (500 KB) ~125,000. Use `max_content_tokens` to budget. Supports [[Streaming-API]] (pause during fetch) and [[Batches-API]].
