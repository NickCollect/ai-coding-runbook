---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/CLAUDE.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CLAUDE.md
title: "Spec repo: Claude Code agent operating instructions"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Repo-level operating notes for AI agents (Claude Code) working in the spec repo. Identical content lives in `AGENTS.md` for other agent harnesses.

**Repository structure**: `docs/` is the Mintlify site (`docs/docs/` for guides/tutorials, `docs/specification/` for the formal versioned spec); `blog/` is a Hugo blog.

**Specification versioning**: spec versions use **date-based versioning** (`YYYY-MM-DD`), not semver. Released versions live in `schema/[YYYY-MM-DD]/` and `docs/specification/[YYYY-MM-DD]/`; in-progress work in `schema/draft/` and `docs/specification/draft/`.

**Schema generation**: TypeScript files are the source of truth. Edit `schema/[version]/schema.ts`; run `npm run generate:schema` to produce both `schema.json` and the rendered `docs/specification/[version]/schema.mdx`. **Always regenerate** after editing schema files.

**Schema examples**: JSON examples live in `schema/[version]/examples/[TypeName]/` (e.g., `Tool/example-name.json` validates against the Tool schema) and are referenced from `schema.ts` via `@includeCode` JSDoc tags.

**Agent skills**: when adding a skill, also create a directory symlink at `docs/.mintlify/skills/<name>` → `../../../plugins/<plugin-name>/skills/<name>` so Mintlify's `.well-known/agent-skills/` and the auto-scan MCP server expose it.

**Useful commands**: `npm run serve:docs`/`serve:blog` for local previews; `npm run generate` (or `:schema`/`:seps`) for regen; `npm run format`/`format:docs`/`format:schema`; `npm run check`/`check:schema`/`check:docs`/`check:seps`; `npm run prep` (the full check+generate+format pipeline that must pass before PR).

**Issue creation**: blank issues are disabled; `gh issue create`/API bypasses the chooser, so a template form (under `.github/ISSUE_TEMPLATE/`) must be used. **SEPs** are PRs adding files to `seps/`, not issues. **SDK bugs** belong in the individual SDK repository. **Claude MCP behavior** belongs in `anthropics/claude-ai-mcp`.

**Commit guidelines**: do not include model names or details (e.g., "Claude", "Opus") in commit messages — neutral wording only.
