---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/AGENTS.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/AGENTS.md
title: "Python SDK development guidelines (for AI agents)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Repo-level operating instructions for Claude Code / Codex / other AI agent harnesses contributing to the MCP Python SDK.

**Branching model**: `main` is currently the V2 rework — breaking changes expected; remove APIs outright (no `@deprecated` shims) and document in `docs/migration.md`. `v1.x` is the release branch for stable; backport PRs target it with `[v1.x]` title prefix. `README.md` is frozen at v1 (pre-commit hook rejects edits) — edit `README.v2.md` instead.

**Package management**: ONLY use `uv`, NEVER `pip`. Always `uv run --frozen <tool>` (don't let uv rewrite `uv.lock` as a side effect). Cross-version testing: `--python 3.10` etc (CI covers 3.10–3.14). Forbidden: `uv pip install`, `@latest` syntax. Don't raise dependency floors for CVEs alone — only when the SDK actually needs new functionality.

**Code quality**: type hints required for all code; public APIs must have docstrings (`Raises:` section when applicable); `src/mcp/__init__.py` `__all__` is a deliberate API decision, not a convenience re-export. **All imports go at top of file** — inline imports hide dependencies and obscure circular-import bugs.

**Testing**: `uv run --frozen pytest`; **anyio not asyncio**; do NOT use `Test*` classes (use `test_*` functions); fast and deterministic — prefer in-memory async (e.g., `Client(server)` in `tests/client/test_client.py`); test files mirror source tree (`src/mcp/client/stdio.py` → `tests/client/test_stdio.py`); avoid `anyio.sleep()` for sync — use `anyio.Event` and `await event.wait()`; wrap indefinite waits in `anyio.fail_after(5)`. Pytest configured with `filterwarnings = ["error"]` — fix the underlying cause, don't silence.

**Coverage**: CI requires **100%** (`fail_under = 100`, `branch = true`). Full check: `./scripts/test`. Targeted iteration uses `coverage run -m pytest` + `coverage report --include` + `UV_FROZEN=1 uv run --frozen strict-no-cover`. Avoid adding `# pragma: no cover`, `# type: ignore`, `# noqa`. Audit before pushing: `git diff origin/main... | grep -E '^\+.*(pragma|type: ignore|noqa)'`. Pragma meanings: `no cover` (never executed; CI fails if it IS executed); `lax no cover` (excluded but not strict-checked); `no branch` (works around coverage.py bug with nested `async with` on Python 3.11+).

**Breaking changes**: document in `docs/migration.md` (what + why + how to migrate); group related changes.

**Formatting & type checking**: `ruff format`, `ruff check --fix`, `pyright`. Pre-commit also runs markdownlint, uv.lock consistency check, README checks.

**Exception handling**: ALWAYS `logger.exception()` (not `logger.error()`) when catching; don't include exception in message. Catch specific exceptions where possible (`OSError`/`PermissionError`, `JSONDecodeError`, `ConnectionError`/`TimeoutError`). FORBIDDEN: `except Exception:` (top-level handlers only).
