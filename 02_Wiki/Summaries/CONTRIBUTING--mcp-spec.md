---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/CONTRIBUTING.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md
title: "Contributing to the MCP spec repo"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Contributor guide covering spec, schema, docs, and blog contributions in the main `modelcontextprotocol/modelcontextprotocol` repo.

**Prerequisites**: Node.js 24+, TypeScript, TypeScript JSON Schema (for schema generation), optional Mintlify (docs preview), optional nvm.

**Setup**: fork → clone → `nvm install` (correct Node version) → `npm install` → `git checkout -b feature/...`.

**Schema changes**: edit `schema/draft/schema.ts`; validate with `npm run check:schema:ts`; do NOT edit generated artifacts (`schema/draft/schema.json`, `docs/specification/draft/schema.mdx`) directly — regenerate via `npm run generate:schema`.

**Documentation changes**: write MDX in `docs/`; preview with `npm run serve:docs`; lint with `npm run check:docs && npm run format`. Or run everything via `npm run prep`.

**Blog changes**: Hugo-based, in `blog/`; preview via `npm run serve:blog`.

**Doc style**: clear/concise/accurate prose, follow existing structure and naming, include code examples, use MDX components, test links (`npm run check:docs:links`), use the headings "When to use"/"Steps"/"Tips" for tutorials, place pages in appropriate sections, update `docs.json` when adding pages, kebab-case.mdx filenames, proper frontmatter.

**Specification proposals**: changes follow the **SEP process** (linked). The shortest summary: explore the problem space and validate others share the problem, build a prototype, then write the SEP based on what the prototype taught you. Proposals aligning with MCP design principles (linked) move faster.

**Submitting**: push to fork → open PR following the template → wait for review.

**AI contributions** — important policy: **all AI assistance must be disclosed in the PR or issue**, including the extent (documentation comments vs. code generation). Spacing/typo fixes are exempt. Example disclosure: "This PR was written primarily by Claude Code." If your PR comments are AI-generated, disclose that too. Required when submitting AI-assisted contributions: clear disclosure, human understanding of the change, clear rationale, concrete evidence (test cases/examples), and your own analysis. Submissions appearing not to follow the disclosure policy may be closed.

**License**: code/spec contributions Apache 2.0; documentation (excluding specifications) CC-BY 4.0.
