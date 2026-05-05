---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/CLAUDE.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/CLAUDE.md
title: "Claude Agent SDK Python — CLAUDE.md (repo dev guide)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: []
---

Repository contributor / Claude Code session guide for the `claude-agent-sdk-python` repo.

**Workflow commands:**

- Lint and style: `python -m ruff check src/ tests/ --fix` then `python -m ruff format src/ tests/`
- Typecheck (only `src/`): `python -m mypy src/`
- Run all tests: `python -m pytest tests/`
- Run a specific test file: `python -m pytest tests/test_client.py`

**Codebase structure:**

- `src/claude_agent_sdk/` — Main package
  - `client.py` — `ClaudeSDKClient` for interactive sessions
  - `query.py` — One-shot `query()` function
  - `types.py` — Type definitions
  - `_internal/` — Internal implementation details
    - `transport/subprocess_cli.py` — CLI subprocess management
    - `message_parser.py` — Message parsing logic

The file is intentionally minimal — it gives Claude Code the lint/test commands and the high-level layout so contributions stay consistent.
