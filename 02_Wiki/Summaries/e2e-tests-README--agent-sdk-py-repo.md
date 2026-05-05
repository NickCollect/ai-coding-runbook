---
type: summary
source: 01_Raw/github/anthropics/claude-agent-sdk-python/e2e-tests/README.md
source_url: https://github.com/anthropics/claude-agent-sdk-python/blob/main/e2e-tests/README.md
title: "Claude Agent SDK Python — e2e tests README"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server]
concepts_referenced: []
---

End-to-end tests for the `claude-agent-sdk-python` repo. They run against the actual Claude API to verify real-world functionality.

**Requirements.** A valid `ANTHROPIC_API_KEY` is required — tests will fail (not skip) if not set. Install dev deps with `pip install -e ".[dev]"`.

**Running.** `python -m pytest e2e-tests/ -v`; filter to e2e marker only via `-m e2e`; specific test via `python -m pytest e2e-tests/test_mcp_calculator.py::test_basic_addition -v`.

**Cost.** Tests make actual API calls and incur cost based on the Anthropic pricing plan. Each test typically uses 1–3 API calls; complete suite should cost less than $0.10.

**Test coverage — MCP Calculator (`test_mcp_calculator.py`):** integration tests around an in-process MCP server with calculator tools. Tests include `test_basic_addition`, `test_division`, `test_square_root`, `test_power`, `test_multi_step_calculation`, `test_tool_permissions_enforced`. Each test validates that tools are actually called (`ToolUseBlock` present in response), correct tool inputs are provided, expected results are returned, and the permission system is enforced.

**CI/CD.** The suite runs on pushes to `main` and on manual workflow dispatch, using `ANTHROPIC_API_KEY` from GitHub Secrets.

**Troubleshooting.** "ANTHROPIC_API_KEY environment variable is required" → export the key. Timeouts → check key validity, quota, and connectivity to api.anthropic.com. Permission denied → verify `allowed_tools` includes the necessary MCP tool names (e.g., `mcp__calc__add`).

**Adding new e2e tests.** Mark with `@pytest.mark.e2e`. Use the `api_key` fixture. Keep prompts simple to minimize cost. Verify actual tool execution, not mocked responses.
