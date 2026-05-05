---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/CONTRIBUTING.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/CONTRIBUTING.md
title: "Contributing to MCPB"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Standard OSS contributor guide for the `mcpb` repository.

**Setup**: fork → clone → `yarn` to install → `yarn build` → `yarn test`.

**Workflow**: branch `feature/...` → make changes → `yarn lint` (use `yarn fix` for auto-formatting) → `yarn test` → commit with **signed commits** (mandatory; links to GitHub's commit-signature-verification docs) → push and open PR.

**Code standards**: TypeScript with proper type annotations; lint cleanly via `yarn lint`; add tests for new features and bug fixes; keep README.md / MANIFEST.md docs in sync when behavior changes.

**Pull request expectations**: clear description of problem and solution, link related issues, all tests + lint pass, all commits signed, docs updated, wait for maintainer review.

**Bug reports** should include: clear description, repro steps, expected vs actual behavior, `mcpb --version` output, and relevant logs.

**Feature requests**: describe feature + use case + value to users, ensure alignment with project goals.

**Especially welcome**: bug fixes, doc improvements, test coverage improvements, new features (large changes should start as a discussion issue).

**Testing guidance**: write unit tests for new functionality, ensure existing tests still pass, manually test with real MCP bundles where applicable.

Contributions licensed under MIT.
