---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/CLAUDE.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/CLAUDE.md
title: "MCP servers repo: Claude Code instructions"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Repo-level operating instructions. Official MCP reference server implementations — **npm workspaces monorepo** containing 7 servers (4 TypeScript, 3 Python) under `src/`. Each is a standalone package published to npm or PyPI.

**Monorepo structure**:
- TS servers (npm published): `everything` (`@modelcontextprotocol/server-everything` — reference, all features), `filesystem` (`@modelcontextprotocol/server-filesystem` — file ops with Roots access control), `memory` (`@modelcontextprotocol/server-memory` — knowledge-graph persistence), `sequentialthinking` (`@modelcontextprotocol/server-sequential-thinking` — step-by-step reasoning)
- Python servers (PyPI published): `fetch` (`mcp-server-fetch` — web content), `git` (`mcp-server-git` — git ops), `time` (`mcp-server-time` — timezone queries)

**TS build**: `npm ci && npm run build && npm test` per server, or `npm install && npm run build` from root. Build = `tsc` (target ES2022, module Node16, strict). Tests = **vitest** (with `@vitest/coverage-v8` for new tests). Node 22.

**Python build**: `uv sync --frozen --all-extras --dev`. Tests = `uv run pytest`, type check = `uv run pyright`, lint = `uv run ruff check .`. Build system **hatchling** via `uv build`. **uv** (not pip). Python ≥3.10 (per-server `.python-version`).

**Code style** (TS): ES modules with `.js` extension imports, strict typing, Zod schemas for tool input validation, 2-space indent + trailing commas, camelCase vars/functions, PascalCase types/classes, UPPER_CASE constants, kebab-case filenames + tools/prompts/resources, **verb-first tool names** (e.g., `get-file-info` not `file-info`). Imports grouped external→internal.

**Code style** (Python): pyright type hints enforced; async/await patterns (especially fetch with pytest-asyncio); follow existing module layout per server.

**Contributing scope**: ✅ bug fixes, usability improvements, enhancements demonstrating MCP protocol features (Resources, Prompts, Roots — not just Tools). 🟡 new features outside server's core purpose / opinionated additions (selective). ❌ new server implementations (use the **MCP Server Registry** at `registry.modelcontextprotocol.io` instead); README server-listing changes (the README list is retired in favor of the Registry).

**CI/CD**: dynamic package detection via `find + jq matrix` strategy. Per-package: detect → test → build → publish (npm for TS, PyPI trusted publishing for Python).

**Key patterns**: each server registers via `registerTools(server)`, `registerResources(server)`, `registerPrompts(server)` functions; tool annotations set `readOnlyHint`/`idempotentHint`/`destructiveHint` per spec; transport support is stdio (default), SSE (deprecated), Streamable HTTP. PR template requires reading MCP docs, security best practices, testing with an LLM client.

The repo is configured with an MCP docs server (`.mcp.json`) pointing to `modelcontextprotocol.io/mcp` for spec reference.
