---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/overview.md
source_url: https://platform.claude.com/docs/en/build-with-claude/overview
title: "Features overview"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Context-editing, Compaction, Adaptive-thinking, Batches-API, Citations-API, Effort, Extended-thinking, PDF-support, Search-results, Structured-outputs, Advisor-tool, Code-execution-tool, Web-fetch-tool, Web-search-tool, Bash-tool-API, Computer-use-tool-API, Memory-tool, Text-editor-tool, Skill, MCP-server, Tool-search-tool-API, Prompt-caching, Token-counting, Files-API]
concepts_referenced: [Context-window, Tool-use]
---

Catalogues Claude Platform features by area, with availability classification (Beta / GA / Deprecated / Retired) and ZDR eligibility per platform (Claude API / Bedrock / Vertex / Azure AI).

## Five feature areas

1. **Model capabilities** — reasoning, format, modality controls.
2. **Tools** — actions on web or in your environment.
3. **Tool infrastructure** — discovery, orchestration at scale.
4. **Context management** — long-running sessions efficient.
5. **Files and assets** — document/data management.

## Availability classifications

| Class | Notes |
|---|---|
| Beta | Preview; may change/discontinue; carries [beta header]; possible qualifier (e.g., "research preview") |
| GA | Stable, production-ready, no beta header, versioning guarantees |
| Deprecated | Functional but not recommended; migration path + removal timeline |
| Retired | Removed |

## Model capabilities (selected)

| Feature | ZDR | Avail |
|---|---|---|
| Context windows (up to 1M) | Yes | API/Bedrock/Vertex/Azure-beta |
| Adaptive thinking | Yes | All four platforms |
| Batch processing (50% off) | No | API/Bedrock/Vertex |
| Citations | Yes | All four |
| Data residency (`inference_geo`) | Yes | API only |
| Effort (Opus 4.7/4.6/4.5) | Yes | All four |
| Extended thinking | Yes | All four |
| PDF support | Yes | All four |
| Search results | Yes | All four |
| Structured outputs | Yes (qualified) | API/Bedrock/Azure-beta |

## Tools

**Server-side:** Advisor (beta), Code execution (no ZDR), Web fetch (qualified ZDR), Web search (qualified ZDR).

**Client-side:** Bash, Computer use (beta), Memory, Text editor — all ZDR-eligible.

## Tool infrastructure

| Feature | ZDR |
|---|---|
| Agent Skills | No |
| Fine-grained tool streaming | Yes |
| MCP connector | No (beta) |
| Programmatic tool calling | No |
| Tool search | Yes |

## Context management

| Feature | Notes |
|---|---|
| Compaction (Opus 4.7/4.6, Sonnet 4.6) | Server-side summarization; ZDR |
| Context editing | Tool-use clearing + thinking-block clearing; ZDR |
| Automatic prompt caching | Single param; auto-advances cache point |
| Prompt caching 5m / 1hr | Standard + extended duration |
| Token counting | Estimate before sending |

## Files and assets

- **Files API** (beta, not ZDR) — upload/manage; PDFs, images, text.

## Note on Models API

Programmatically discover capabilities: `Models API` returns `max_input_tokens`, `max_tokens`, and a `capabilities` object per model.
