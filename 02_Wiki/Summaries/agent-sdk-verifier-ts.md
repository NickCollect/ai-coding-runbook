---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/agent-sdk-dev/agents/agent-sdk-verifier-ts.md
title: "agent-sdk-verifier-ts (subagent definition)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Subagent, Permission-mode, MCP-server]
concepts_referenced: []
---

Subagent definition shipped in the `agent-sdk-dev` plugin. Verifies a TypeScript Agent SDK application's correctness against SDK best practices and official docs. Model: `sonnet`. Invoked after a TS Agent SDK app is created or modified.

**Verification focus** (SDK functionality > general code style):
1. **Install/config**: `@anthropic-ai/claude-agent-sdk` installed, version not ancient, `package.json` has `"type": "module"`, Node engines field check.
2. **TypeScript config**: `tsconfig.json` exists, ES module resolution, modern target, won't break SDK imports.
3. **SDK usage/patterns**: correct imports, proper agent initialization per docs, system prompts/models follow patterns, correct method params, streaming-vs-single response handling, permission scoping, MCP server integration.
4. **Type safety**: run `npx tsc --noEmit`, validate import type defs match SDK docs.
5. **Scripts**: `package.json` has `build`/`start`/`typecheck`.
6. **Env/security**: `.env.example` with `ANTHROPIC_API_KEY`, `.env` in `.gitignore`, no hardcoded keys.
7. **Best practices**: clear system prompts, appropriate model selection, scoped permissions, MCP custom tools, subagent config, session handling.
8. **Functionality**: app structure for SDK, init+execution flow, SDK-specific error handling, follows doc patterns.
9. **Documentation**: README, setup instructions if needed.

**Explicit non-focus**: code style, `type` vs `interface` choice, naming conventions, general TS best practices unrelated to SDK.

**Process**: read `package.json`, `tsconfig.json`, app files (`index.ts`, `src/*`), `.env.example`, `.gitignore`. WebFetch `https://docs.claude.com/en/api/agent-sdk/typescript` to compare. Run type check. Analyze SDK usage.

**Report format**: Overall Status (PASS / PASS WITH WARNINGS / FAIL), Summary, Critical Issues, Warnings, Passed Checks, Recommendations.
