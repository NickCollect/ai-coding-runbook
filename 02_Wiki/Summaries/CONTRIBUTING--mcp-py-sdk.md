---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/CONTRIBUTING.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/CONTRIBUTING.md
title: "MCP Python SDK contributor guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Contributor guide. **All PRs require a corresponding issue.** Unless the change is trivial (typo / docs / broken link), create an issue first; PRs without a linked issue will be closed. Having an issue doesn't guarantee acceptance — wait for maintainer feedback or `ready for work` label.

**The SDK is opinionated**: not every contribution will be accepted even with a working implementation. Prioritize maintainability and consistency over adding capabilities.

**Always require an issue first**: new public APIs/decorators, architectural changes/refactoring, multi-module changes, features that might require spec changes (these need an upstream **SEP** first).

**Issue labels**: `good first issue` (newcomers), `help wanted` (experienced contributors — maintainers probably won't get to this), `ready for work` (maintainer-triaged). `needs confirmation` / `needs maintainer action` are NOT ready — wait. Comment on issue for assignment to prevent duplicate work.

**Setup**: Python 3.10+, install `uv`, fork & clone, `uv sync --frozen --all-extras --dev`, `uv tool install pre-commit --with pre-commit-uv --force-reinstall`.

**Branching**: new features / breaking changes → `main`; security fixes for v1 → `v1.x`; bug fixes for v1 → `v1.x`. **`main` is v2 development**; `v1.x` receives only security and critical fixes.

**Workflow**: branch from chosen base → make changes → `uv run pytest` → `uv run pyright` → `uv run ruff check .` + `uv run ruff format .` → `uv run scripts/update_readme_snippets.py` if you modified examples → optionally `pre-commit run --all-files` → submit PR to the same branch.

**PR scope**: small PRs reviewed fast; large PRs sit. A few dozen lines reviewable in minutes; hundreds across many files take real effort and slip-through risk. Break big changes or get maintainer alignment first.

**What gets rejected**: no prior discussion, scope creep, misalignment with SDK direction, overengineering. Standard PR checklist: docs, tests, CI passes, address feedback. MIT license.
