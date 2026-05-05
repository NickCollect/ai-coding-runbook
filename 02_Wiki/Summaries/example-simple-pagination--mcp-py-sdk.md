---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-pagination/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-pagination/README.md
title: "Python SDK example: simple pagination server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates **cursor-based pagination** for tools, resources, and prompts.

Run via stdio (default) or `--transport streamable-http --port 8000`.

Exposes: 25 tools (5 per page), 30 resources (10 per page), 20 prompts (7 per page). Each paginated list returns `nextCursor` when more pages are available.

Sample Python client code shows fetching first page, then passing `cursor=tools_page1.nextCursor` to fetch subsequent pages. Demonstrates handling None cursor (first page), returning nextCursor when more data exists, gracefully handling invalid cursors, different page sizes per resource type. Uses simple numeric indices in the demo; production scenarios would use database offsets, timestamps, or opaque tokens encoding pagination state.
