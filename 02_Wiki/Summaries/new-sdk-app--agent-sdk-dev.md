---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/agent-sdk-dev/commands/new-sdk-app.md
title: "agent-sdk-dev: /new-sdk-app command"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Agent-SDK, Subagent, MCP-server]
concepts_referenced: []
---

Slash command from `agent-sdk-dev` plugin: interactively scaffolds a new Claude Agent SDK application.

**Frontmatter**: `description: "Create and setup a new Claude Agent SDK application"`, `argument-hint: [project-name]`.

**Workflow**:
1. **Reference docs first** — WebFetch the SDK overview, language-specific reference (TS or Python), and relevant guides (Streaming vs Single Mode, Permissions, Custom Tools, MCP, Subagents, Sessions). Verify latest package versions via WebSearch/WebFetch.

2. **Gather requirements one question at a time** (don't ask multiple at once):
   - Language (TS or Python)
   - Project name (use `$ARGUMENTS` if provided)
   - Agent type (coding/business/custom)
   - Starting point (Hello World / basic agent / use-case-specific)
   - Tooling preferences (npm vs pnpm vs bun for TS)

3. **Setup plan**:
   - Project init (`npm init -y` with `type: "module"` + `typecheck` script for TS; `requirements.txt` or `poetry init` for Python)
   - Config (`tsconfig.json` for TS)
   - Check latest versions on npm/PyPI BEFORE installing
   - Install: `npm install @anthropic-ai/claude-agent-sdk@latest` or `pip install claude-agent-sdk`
   - Verify installed version (`npm list ...` or `pip show ...`)
   - Create starter `index.ts`/`src/index.ts` or `main.py`
   - `.env.example` with `ANTHROPIC_API_KEY=your_api_key_here`; add `.env` to `.gitignore`
   - Optionally create `.claude/` dir for agents/commands/settings

4. **Verification gate**: TS → `npx tsc --noEmit` and fix all type errors. Python → check syntax/imports. **Don't consider setup complete until verifier passes.**

5. **Launch verifier subagent**: `agent-sdk-verifier-ts` or `agent-sdk-verifier-py` to validate setup against best practices.

6. **Provide getting-started guide**: how to set API key, how to run, links to SDK references, common next steps (custom tools via MCP, permissions, subagents).

**Key principles**: always use latest versions, verify before claiming done, ask questions one at a time, respect user's package manager preferences, modern syntax for latest SDK.
