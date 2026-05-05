---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/agent-sdk-dev/agents/agent-sdk-verifier-py.md
title: "agent-sdk-verifier-py (subagent definition)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Subagent, MCP-server, Permission-mode]
concepts_referenced: []
---

Subagent definition (Sonnet) shipped in the `agent-sdk-dev` plugin. Inspects Python Agent SDK applications for correct SDK usage, doc adherence, and deployment readiness.

**Frontmatter**:
- `name: agent-sdk-verifier-py`
- `description`: invoke after creating/modifying a Python Agent SDK app
- `model: sonnet`

**Verification focus** (8 areas, prioritized over general code style):
1. **Install/config**: `claude-agent-sdk` in requirements.txt or pyproject.toml; current SDK version; Python 3.8+; venv recommended
2. **Python env setup**: requirements.txt or pyproject.toml; reproducible deps; documented Python version constraints
3. **SDK usage patterns**: correct imports from `claude_agent_sdk`, agent init per docs, correct config (system prompts, models), proper handling of agent responses (streaming vs single mode), permissions, MCP server integration
4. **Code quality**: syntax errors, imports, error handling, structure
5. **Env/security**: `.env.example` with `ANTHROPIC_API_KEY`, `.env` in `.gitignore`, no hardcoded keys
6. **SDK best practices** (from docs): clear system prompts, appropriate model choice, scoped permissions, correct MCP custom tools, proper subagent config, correct session handling
7. **Functionality validation**: app structure, agent init/exec flow, error handling for SDK-specific errors
8. **Documentation**: README, setup instructions (incl. venv), custom config docs, install instructions

**NOT focus**: PEP 8, naming conventions, import ordering, general Python best practices unrelated to SDK.

**Process**: read relevant files (requirements/pyproject, main app files, .env.example, .gitignore, configs) → use WebFetch to compare against `https://docs.claude.com/en/api/agent-sdk/python` → validate imports/syntax → analyze SDK usage.

**Report format**: Overall Status (PASS / PASS WITH WARNINGS / FAIL); Summary; Critical Issues (functional, security, SDK runtime errors, syntax/imports); Warnings (suboptimal patterns, missing features, doc deviations); Passed Checks; Recommendations.
