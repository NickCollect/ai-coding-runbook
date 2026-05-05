---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/RELEASING.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/RELEASING.md
title: "Claude Agent SDK Python — RELEASING"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: []
---

Release process for the `claude-agent-sdk-python` package. Two flows exist: **automatic** (triggered by a CLI version bump) and **manual** (triggered via the GitHub Actions UI). Both invoke the same reusable `build-and-publish.yml` workflow that builds platform-specific wheels on five OS targets, publishes to PyPI, updates version files, generates a changelog entry using Claude, pushes to `main`, and creates a git tag plus GitHub Release.

**Wheel targets:** `ubuntu-latest` → `manylinux_2_17_x86_64`; `ubuntu-24.04-arm` → `manylinux_2_17_aarch64`; `macos-latest` → `macosx_11_0_arm64`; `macos-15-intel` → `macosx_11_0_x86_64`; `windows-latest` → `win_amd64`.

PRs that touch build scripts, `pyproject.toml`, or the publish workflow trigger `build-wheel-check.yml`, which dry-runs the full build matrix and verifies each wheel contains the bundled CLI before merge.

**Versioning.** Two separate version numbers are tracked: the SDK version (in `pyproject.toml` and `src/claude_agent_sdk/_version.py`) and the bundled CLI version (in `src/claude_agent_sdk/_cli_version.py`). Both follow semver (`MAJOR.MINOR.PATCH`); git tags use `vX.Y.Z`.

**Automatic release** (most common path):

1. A commit `chore: bump bundled CLI version to X.Y.Z` is pushed to `main`, updating `_cli_version.py`.
2. The `Test` workflow runs.
3. On success, `auto-release.yml` fires via `workflow_run`.
4. It verifies the trigger commit message and that `_cli_version.py` changed.
5. It reads the current SDK version from `_version.py` and increments the patch number (e.g., `0.1.24` → `0.1.25`).
6. It calls `build-and-publish.yml` to build, publish, push, tag, and create a GitHub Release.

**Manual release** — used for minor/major bumps or non-CLI-bump changes. Trigger via Actions → Publish to PyPI → Run workflow with the desired version. Runs full test suite (Python 3.10–3.13) and lint, then calls `build-and-publish.yml`.

**Scripts in `scripts/`:** `update_version.py` (SDK version), `update_cli_version.py` (CLI version), `build_wheel.py` (downloads CLI binary, builds wheel, retags with platform-specific tags), `download_cli.py` (downloads Claude Code CLI for current platform).

**Required secrets:** `PYPI_API_TOKEN` (PyPI publishing), `ANTHROPIC_API_KEY` (changelog generation and e2e tests), `DEPLOY_KEY` (SSH key for direct pushes to `main`).
