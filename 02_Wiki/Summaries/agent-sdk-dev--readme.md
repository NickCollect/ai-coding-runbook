---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/agent-sdk-dev/README.md
title: "Agent SDK Development Plugin"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Agent-SDK, Subagent, Slash-command]
concepts_referenced: []
---

Plugin in the official `anthropics/claude-code` plugins directory. Streamlines creating + verifying Claude Agent SDK applications in Python and TypeScript.

**Components**:
- `/new-sdk-app [name]` — interactive scaffolder. Asks: language (TS/Python), agent type (coding/business/custom), starting point (minimal/basic/example), tooling (npm/yarn/pnpm or pip/poetry). Installs latest SDK, creates files (.env.example, .gitignore, etc.), runs type-check (TS) or syntax-validate (Python), then runs the corresponding verifier subagent.
- `agent-sdk-verifier-py` subagent — checks Python SDK app: SDK install/version, `requirements.txt`/`pyproject.toml`, SDK usage patterns, agent init/config, env security, error handling, docs. Output: PASS / PASS WITH WARNINGS / FAIL with critical issues + warnings + passed checks + recommendations.
- `agent-sdk-verifier-ts` subagent — same for TypeScript: tsconfig, type safety/imports, etc.

Trigger verifier later by asking "Verify my Python/TypeScript Agent SDK application" or "check if my SDK app follows best practices".

Workflow example: `/new-sdk-app code-reviewer-agent` → answer prompts → auto-verification → set `ANTHROPIC_API_KEY` in `.env` → `npm start`.

Best practices: always latest SDK; verify before deploy; never commit `.env`; type-check TS regularly.

Author: Ashwin Bhat (ashwin@anthropic.com). Version 1.0.0.

Troubleshooting covers TS type errors (run `npx tsc --noEmit`), Python import errors (activate venv, `pip show claude-agent-sdk`), verifier warnings (review report against SDK docs).
