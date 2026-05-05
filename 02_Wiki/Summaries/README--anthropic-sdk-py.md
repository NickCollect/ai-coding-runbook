---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/README.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/README.md
title: "Claude SDK for Python — README"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Messages-API]
concepts_referenced: []
---

The Claude SDK for Python (`pip install anthropic`, requires Python 3.9+) provides access to the Claude API from Python applications. Full documentation lives at platform.claude.com/docs/en/api/sdks/python. MIT-licensed.

**Getting started example:** instantiate `Anthropic(api_key=...)` (defaults to `ANTHROPIC_API_KEY` env var) and call `client.messages.create(max_tokens=1024, messages=[{"role": "user", "content": "Hello, Claude"}], model="claude-opus-4-6")`.

This README is intentionally minimal — see `api.md`, `helpers.md`, `tools.md`, and `CONTRIBUTING.md` in the same repo for deeper API reference, streaming/MCP helpers, tool runner usage, and contributor workflow.
