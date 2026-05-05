---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/CLAUDE.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/CLAUDE.md
title: "Claude Code Action — CLAUDE.md (repo dev guide)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, MCP-server]
concepts_referenced: []
---

Repository-level Claude Code project guide for the `claude-code-action` repo. Bun runtime (not Node).

**Commands.** `bun test`, `bun run typecheck`, `bun run format`, `bun run format:check`.

**What this is.** A GitHub Action that lets Claude respond to `@claude` mentions on issues/PRs (tag mode) or run tasks via `prompt` input (agent mode). Mode is auto-detected: if `prompt` is provided, agent mode; if triggered by a comment/issue event with `@claude`, tag mode. See `src/modes/detector.ts`.

**How it runs.** Single entrypoint `src/entrypoints/run.ts` orchestrates everything: prepare (auth, permissions, trigger check, branch/comment creation), install Claude Code CLI, execute Claude via `base-action/` functions (imported directly, not subprocess), then cleanup (update tracking comment, write step summary). SSH signing cleanup and token revocation are separate `always()` steps in `action.yml`.

`base-action/` is also published standalone as `@anthropic-ai/claude-code-base-action`. Don't break its public API. It reads config from `INPUT_`-prefixed env vars (set by `action.yml`), not from action inputs directly.

**Key concepts.**

- **Auth priority**: `github_token` input (user-provided) > GitHub App OIDC token (default). `claude_code_oauth_token` and `anthropic_api_key` are for the Claude API, not GitHub. Token setup in `src/github/token.ts`.
- **Mode lifecycle**: `detectMode()` picks "tag" or "agent". Trigger checking and prepare dispatch are inlined in `run.ts`: `prepareTagMode()` from `src/modes/tag/`, `prepareAgentMode()` from `src/modes/agent/`.
- **Prompt construction**: Tag mode's `prepareTagMode()` fetches GitHub data (`src/github/data/fetcher.ts`), formats it as markdown (`src/github/data/formatter.ts`), and writes it to a temp file via `createPrompt()`. Agent mode writes the user's prompt directly. The prompt includes issue/PR body, comments, diff, and CI status — the most important part of the action because it's what Claude sees.

**Things that will bite you.**

- Strict TypeScript: `noUnusedLocals` and `noUnusedParameters` enabled. Typecheck fails on unused vars.
- Discriminated unions for GitHub context: call `isEntityContext(context)` before accessing `context.issue` or `context.pullRequest`.
- Token lifecycle: GitHub App token is obtained early and revoked in a separate `always()` step in `action.yml`. Don't move revocation into `run.ts` — it won't run if the process crashes. Same for SSH signing cleanup.
- Error phase attribution: catch block uses `prepareCompleted` to distinguish prepare failures from execution failures; tracking comment shows different messages.
- `action.yml` outputs reference step IDs (`steps.run.outputs.*`). Renaming the step requires updating the outputs section.
- Integration testing happens in a separate repo (`install-test`); this repo only has unit tests.

**Code conventions.** Bun runtime (use `bun test`, not `jest`). `moduleResolution: "bundler"` — imports don't need `.js` extensions. GitHub API calls should use retry logic (`src/utils/retry.ts`). MCP servers are auto-installed at runtime to `~/.claude/mcp/github-{type}-server/`.
