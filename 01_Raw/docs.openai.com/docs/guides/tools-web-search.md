# Web search

<!-- source: https://platform.openai.com/docs/guides/tools-web-search -->

Web search allows models to access up-to-date information from the internet and provide answers with sourced citations. Use the `web_search` tool in the Responses API.

## Three types of web search

1. **Non-reasoning web search**: Fast, ideal for quick lookups. Model sends query to web search tool, returns response based on top results.
2. **Agentic search with reasoning models**: Model actively manages search process, can perform multiple searches in its chain of thought. More flexible for complex workflows but slower.
3. **Deep research**: Extended, agent-driven investigations. Hundreds of sources, runs for several minutes. Use `gpt-5.5` with reasoning set to `high` or `xhigh`. Best used with background mode.

## Choose an integration

| Use case | Recommended path |
|---|---|
| New web search integration | Responses API with `web_search` and `gpt-5.5` |
| Existing Chat Completions search | Chat Completions with `gpt-5-search-api` |
| Multi-step research / long-running | `gpt-5.5` with `high`/`xhigh` reasoning + background mode |

## Output and citations

Model responses that use web search include:
- `web_search_call` output item: search call ID, action (`search`, `open_page`, `find_in_page`)
- `message` output item: text result + annotations with cited URLs

Inline citations for URLs are included by default. Citations must be clearly visible and clickable in your UI.

## Features

- **`search_context_size`**: Controls how much web search context is available (`low`/`medium`/`high`)
- **Domain filtering**: Up to 100 `allowed_domains` or `blocked_domains` via `filters` parameter
- **Sources**: Full list of URLs consulted (more than just cited URLs), accessible via `sources` field
- **User location**: Refine results by `country` (ISO 2-letter), `city`, `region`, `timezone` (IANA)
- **Live access control**: `external_web_access: false` to use cached/indexed results only

## Limitations

- Web search context window is limited to 128k even when model context window is larger
- Does not support `gpt-5` with `minimal` reasoning
- `web_search_preview` does not support `filters` and ignores `external_web_access`
- Preview search models (`gpt-4o-search-preview`, `gpt-4o-mini-search-preview`) deprecated, shutdown 2026-07-23

## Migration from legacy

- `web_search_preview` → migrate to `web_search` (supports newer controls)
- `gpt-4o-search-preview` / `gpt-4o-mini-search-preview` → migrate to Responses `web_search` or `gpt-5-search-api`
