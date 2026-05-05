---
type: summary
source: 01_Raw/github/anthropics/claude-code/.claude-plugin/marketplace.json
title: "claude-code-plugins marketplace.json"
summarized_at: 2026-05-05
entities_referenced: [Plugin-marketplace, Plugin]
concepts_referenced: []
---

The marketplace manifest at `.claude-plugin/marketplace.json` for the `anthropics/claude-code` repo. Schema: `https://json.schemastore.org/claude-code-marketplace.json`.

**Manifest fields**:
- `name`: `claude-code-plugins`
- `version`: `1.0.0`
- `description`: bundled plugins for Claude Code (Agent SDK dev, PR review, commit workflows)
- `owner`: `Anthropic` / `support@anthropic.com`
- `plugins`: array of 13 plugin entries.

**Plugin entry schema** (per plugin):
- `name`, `description`, `source` (relative path `./plugins/<name>`), `category` (`development` / `productivity` / `learning` / `security`)
- Optional: `version`, `author` (object: `name`, `email`)

**13 plugins listed** with author + category:
1. `agent-sdk-dev` — development
2. `claude-opus-4-5-migration` (William Hu) — development
3. `code-review` (Boris Cherny) — productivity
4. `commit-commands` (Anthropic) — productivity
5. `explanatory-output-style` (Dickson Tsai) — learning
6. `feature-dev` (Sid Bidasaria) — development
7. `frontend-design` (Prithvi Rajasekaran & Alexander Bricken) — development
8. `hookify` (Daisy Hollman) — productivity
9. `learning-output-style` (Boris Cherny) — learning
10. `plugin-dev` (Daisy Hollman) — development
11. `pr-review-toolkit` (Anthropic) — productivity
12. `ralph-wiggum` (Daisy Hollman) — development
13. `security-guidance` (David Dworken) — security

This file is what makes the repo's `./plugins/` directory installable as a CC marketplace via `/plugin marketplace add github:anthropics/claude-code`.
