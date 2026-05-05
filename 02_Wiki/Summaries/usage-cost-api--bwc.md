---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/usage-cost-api.md
source_url: https://platform.claude.com/docs/en/build-with-claude/usage-cost-api
title: "Usage and Cost API"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Usage-report, Cost-report, Workspace, API-key, Prompt-caching, Fast-mode, Code-execution-tool, Web-search-tool]
concepts_referenced: []
---

Programmatic access to historical API usage and cost data, mirroring Console Usage and Cost pages but more granular. Part of the Admin API — requires `sk-ant-admin...` key. Unavailable for individual accounts.

## Two endpoints

| Endpoint | Returns |
|---|---|
| `GET /v1/organizations/usage_report/messages` | Token consumption broken down by model/workspace/service tier/etc. |
| `GET /v1/organizations/cost_report` | USD cost breakdowns by service description |

## Usage API

**Time buckets:** `1m` (default 60, max 1440), `1h` (default 24, max 168), `1d` (default 7, max 31).

**Tracked tokens:** uncached input, cached input, cache creation, output. Plus server tool usage (web search etc.).

**Group by / filter dimensions:** `model`, `workspace_id`, `api_key_id`, `service_tier` (incl. `priority`, `batch`), `context_window` (e.g., `0-200k`), `inference_geo` (`global` | `us` | `not_available`), `speed` (beta — requires `fast-mode-2026-02-01` header; `standard` | `fast`).

Models pre-Opus 4.6 don't support `inference_geo` → return `"not_available"` for that dim. Use `inference_geos[]=not_available` to target them.

## Cost API

- USD only, decimal strings in lowest units (cents).
- Daily granularity only (`1d`).
- Group by `workspace_id` and/or `description` (parsed fields like `model`, `inference_geo` returned with `description`).
- Tracks token usage + web search + code execution costs.
- **Priority Tier costs NOT included** (different billing model). Track Priority Tier via Usage endpoint with `service_tier` filter.

## Pagination

Both endpoints: cursor-based (`has_more`, `next_page` token + `page` param).

## Operational notes

- **Freshness:** ~5 min after request completion (occasional longer delays).
- **Polling:** ≤1/min sustained acceptable; bursts OK during pagination. Cache for dashboards.
- **Default workspace:** appears with `workspace_id: null`.
- **Workbench usage:** `api_key_id: null` (no key associated).
- Set `User-Agent: YourApp/1.0.0 (https://yourapp.com)` for integration tracking.

## Partner observability platforms

CloudZero, Datadog, Grafana Cloud, Honeycomb, Vantage all offer ready-made integrations.
