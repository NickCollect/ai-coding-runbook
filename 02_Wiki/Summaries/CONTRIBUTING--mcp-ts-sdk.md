---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/CONTRIBUTING.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/CONTRIBUTING.md
title: "MCP TypeScript SDK contributor guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Discuss before you code.** Open an issue before starting work on new features or significant changes. Undiscussed-feature PRs will be closed (every merged feature is ongoing maintenance burden). Straightforward bug fixes can skip — for complex bugs, open an issue first.

**Significant changes that require an issue**: new public APIs/classes, architectural changes/refactoring, multi-module changes, features that might require spec changes (need an upstream **SEP** first).

**Issue labels**: `good first issue` (newcomers), `help wanted` (experienced contributors — maintainers probably won't get to it), `ready for work` (maintainer-triaged). `needs confirmation` / `needs repro` / `needs design` are NOT ready — wait for maintainer input.

**Branches**: `main` is v2 (in development, monorepo with split packages). `v1.x` is the stable v1 release. New features/v2 work → `main`; v1 bug fixes/patches → `v1.x`.

**PR scope**: small PRs reviewed fast. A few dozen lines reviewable in minutes; hundreds across many files take real effort and slip-through risk. Break big changes into a stack or get alignment first.

**Rejected for**: lack of prior discussion, scope creep, misalignment with SDK direction, insufficient quality (clarity, maintainability, style), overengineering.

**Setup**: `corepack enable` (pnpm via Node 16.9+ corepack). Then fork → clone → `pnpm install` → `pnpm build:all` → `pnpm test:all`. Workflow: branch → make changes → `pnpm lint:all` → `pnpm test:all` → submit PR.

**Examples**: `pnpm --filter @modelcontextprotocol/examples-server exec tsx src/simpleStreamableHttp.ts` (similar for examples-client). See `examples/server/README.md` and `examples/client/README.md`.

**Releasing v1.x patches**: latest v1.x — `git checkout v1.x` → cherry-pick → `npm version patch` → `git push --tags` (auto-triggers release workflow). Older minor versions — create release branch from last tag, cherry-pick, `npm version patch`, push tags, then manually trigger "Publish v1.x" workflow specifying the tag.

**npm tags**: v1.x releases publish with `release-X.Y` tags (not `latest`). Install specific minor: `npm install @modelcontextprotocol/sdk@release-1.25`.

License: Apache 2.0 for new contributions; documentation (excluding specs) CC-BY 4.0.
