---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/computer-use-demo/CONTRIBUTING.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/computer-use-demo/CONTRIBUTING.md
title: "Claude Quickstarts — computer-use-demo CONTRIBUTING"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Contributor guide for the Computer Use Demo quickstart.

**Contribution policy.** Bugfixes and correctness-focused doc updates are always welcome. Feature additions, refactors, and major doc changes are accepted at the maintainers' sole determination, evaluated against criteria: adherence to coding standards, ease of use as a reference implementation, UX, broad applicability, minimal third-party deps, no product/service promotion. Each major change must be a separate PR. Open a GitHub issue to discuss before starting.

**Development setup.** Create and activate a Python venv. `pip install -r dev-requirements.txt`. `pre-commit install`.

**Process.** Fork the repo, branch for your changes, follow coding standards, submit a PR with a clear description.

**Coding standards.** Clear descriptive variable/function names. PEP 8 for Python. Functions focused and single-purpose. Avoid inline comments (code should be self-documenting). Type hints on all Python functions. Use dataclasses for structured data (see `tools/base.py`). All tools must inherit from `BaseAnthropicTool` and implement required methods. Use ABCs for interfaces. Handle errors via `ToolError` and `ToolFailure` classes.

The file continues with testing, commit message guidelines, code-of-conduct enforcement, and the maintainers' review timeline expectations.
