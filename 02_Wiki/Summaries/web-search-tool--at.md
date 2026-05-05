---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
title: "Web search tool"
summarized_at: 2026-05-05
entities_referenced: [Web-search-tool, Tool-use, Code-execution-tool, Web-fetch-tool, Citations-API, Batches-API, Streaming-API]
concepts_referenced: []
---

The [[Web-search-tool]] gives Claude direct access to real-time web content for answers beyond the knowledge cutoff. Responses always include [[Citations-API]] for sources from search results. Latest version `web_search_20260209` supports **dynamic filtering** with Claude Mythos Preview, Opus 4.7/4.6, Sonnet 4.6—Claude writes and executes code (via [[Code-execution-tool]]) to post-process query results, dynamically filtering before loading into context. Previous version `web_search_20250305` remains available without dynamic filtering. Mythos Preview supports search on Claude API, Microsoft Foundry, and Google Vertex AI; not Amazon Bedrock.

**Why dynamic filtering matters.** Web search is token-intensive—basic search pulls full HTML from multiple sites and reasons over all of it. Much is irrelevant, which can degrade response quality. With `_20260209`, Claude can write Python (in the code execution sandbox) to filter raw search results before they enter context, keeping only what's relevant. Particularly effective for: searching technical documentation, literature review and citation verification, technical research, and response grounding/verification.

Dynamic filtering requires the [[Code-execution-tool]] to be enabled. The improved tool is on the Claude API and Microsoft Azure; on Vertex AI only the basic version is available.

**ZDR.** Basic `web_search_20250305` is ZDR-eligible. The `_20260209` version with dynamic filtering is not by default (uses code execution internally) but can be ZDR-enabled by setting `allowed_callers: ["direct"]`, which disables dynamic filtering.

**Mechanism.**
1. Claude decides when to search based on the prompt.
2. The API executes searches and returns results to Claude (this may repeat multiple times in one request).
3. Claude provides a final response with cited sources.

**Setup requirement.** Your organization's admin must enable web search in the Claude Console (privacy settings).

**Tool parameters.** Like `web_fetch`: `max_uses` (caps searches), `allowed_domains`/`blocked_domains` (mutually exclusive; see Server tools for syntax). Citations are **always enabled** (unlike web fetch where it's optional).

**Combined with web fetch.** Common pattern: enable both [[Web-search-tool]] (`max_uses: 3`) and [[Web-fetch-tool]] (`max_uses: 5`). Search surfaces candidate URLs from snippets; fetch retrieves the most relevant pages in full for citation. This avoids over-fetching while pulling complete content where needed.

**Streaming.** Search events arrive as part of the SSE stream with the standard `server_tool_use` and result block patterns from the Server tools page. Pause occurs during search execution.

**Pricing.** Tracked in `usage.server_tool_use.web_search_requests`. Standard input/output token costs apply for search results that enter context. The doc presents this primarily as a setup + integration reference; per-search dollar pricing would be checked in the broader pricing docs.

**Compatible with [[Batches-API]].** Same per-call price as in regular Messages API requests.
