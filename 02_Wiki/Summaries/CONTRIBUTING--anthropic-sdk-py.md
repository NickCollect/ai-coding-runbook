---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/CONTRIBUTING.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/CONTRIBUTING.md
title: "Anthropic SDK Python — CONTRIBUTING"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python]
concepts_referenced: []
---

Contributor guide for the `anthropic-sdk-python` repo.

**Documentation.** Lives at platform.claude.com/docs/en/api/sdks/python — to suggest changes, open an issue.

**Environment setup.** With `uv`: run `./scripts/bootstrap` (or `uv sync --all-extras` after a manual uv install). Then run scripts via `uv run python script.py` or by activating `.venv`. Without `uv`: install the Python version specified in `.python-version`, create a venv however you prefer, then `pip install -r requirements-dev.lock`.

**Generated code.** Most of the SDK is generated. Modifications to generated code persist between generations but may collide on re-generation. The generator never modifies `src/anthropic/lib/` or `examples/` — those directories are safe for hand-edits.

**Examples.** Files under `examples/` are free to add or edit. Example scripts are made executable (`chmod +x`) and run directly with the `#!/usr/bin/env -S uv run python` shebang.

**Using from source.** Either `pip install git+ssh://git@github.com/anthropics/anthropic-sdk-python.git`, or build a wheel locally with `uv build` (or `python -m build`) and `pip install ./dist/...whl`.

**Tests.** Most tests need a mock OpenAPI server — start it with `./scripts/mock`, run with `./scripts/test`. Some tests use `inline-snapshot`; refresh with `./scripts/test --inline-snapshot=fix -n0` (must disable pytest-xdist parallelism). Some also capture HTTP request snapshots; refresh with the additional `--http-record` flag.

**Lint and format.** Repo uses `ruff` and `black`. Lint with `./scripts/lint`. Auto-fix and format with `./scripts/format`.

**Publishing.** The automated release-PR pipeline publishes to PyPI. Manual release options: the `Publish PyPI` GitHub action, or running `bin/publish-pypi` locally with `PYPI_TOKEN` set.
