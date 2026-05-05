---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/REVIEW.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/REVIEW.md
title: "TS SDK code review conventions"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Pull-request review guidance for the TS SDK. First three sections are stable principles; **Recurring Catches** is auto-maintained from past human reviews and grows over time.

**Guiding principles**:
1. **Minimalism** — SDK should do less, not more. Protocol correctness, transport lifecycle, types, clean handler context belong in the SDK. Middleware engines, registry managers, builder patterns, content helpers belong in userland.
2. **Burden of proof is on addition** — default answer is no. Removing public API is far harder than not adding it.
3. **Justify with concrete evidence** — every new abstraction needs a concrete consumer today; ask for real issues / benchmarks / examples; same standard applies to your own review (link spec sections, link code, show simpler alternative).
4. **Spec is the anchor** — further drift requires stronger justification.
5. **Kill at the highest level** — if design is wrong, lead with that; specific bugs are supporting detail.
6. **Decompose by default** — multiple things → multiple PRs unless strong reason to bundle.

**Review ordering**: design justification → structural concerns → correctness → style/naming.

**Checklist** covers: protocol & spec match (types match `schema.ts` exactly, correct `ProtocolErrorCode`s, HTTP statuses, transport-neutral, cross-SDK consistency vs `python-sdk`); API surface (intentional exports, helpers users can write themselves go in cookbook not SDK, one way to do things); correctness (async race conditions, error propagation, type safety, backward compat); tests & docs (vitest for new behavior + error paths, breaking changes documented in BOTH `docs/migration.md` and `docs/migration-SKILL.md`).

**Reference sources for spec verification**: MCP docs server `https://modelcontextprotocol.io/mcp`; full spec text at `https://modelcontextprotocol.io/llms-full.txt` (LLM-friendly single file — fetch + grep); schema source-of-truth at `schema.ts` in the modelcontextprotocol repo.

**Recurring catches** (with PR references):
- HTTP transport: distinguish `Mcp-Session-Id` missing (400) from unknown/expired (404); never conflate with single 4xx (#1707, #1770)
- Error handling: broad `catch` blocks must not emit client-fault codes (`-32700` ParseError, `-32602` InvalidParams) for server-internal failures — use `-32603` InternalError (#1752, #1769)
- Schema compliance: when editing Zod protocol schemas, verify unknown-key handling matches spec — use `z.looseObject()` / `.catchall(z.unknown())` rather than implicit strict (#1768, #1849, #1169)
- Async/lifecycle: wrap user-supplied callbacks (`onclose?.()`, cancel fns) in `try/finally` so a throw can't skip teardown; deferred callbacks must check closed/aborted before mutating state (#1735, #1763)
- Completeness: when replacing a pattern (error class, auth-flow step, catch shape), grep for surviving instances of the old form (#1657, #1761, #1595)
- Documentation & changesets: read added `.changeset/*.md` text against the implementation in the same diff — flag any claim the diff doesn't back (#1718, #1838)
- CI & GitHub Actions: don't assert that third-party Actions need extra permissions/tokens without verifying — `pnpm publish` delegates to system npm CLI, `changesets/action` in publish mode has no PR-comment step requiring `pull-requests: write` (#1838, #1836)
