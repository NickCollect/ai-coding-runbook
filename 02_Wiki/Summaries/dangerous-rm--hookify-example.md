---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/examples/dangerous-rm.local.md
title: "dangerous-rm.local.md (hookify example rule)"
summarized_at: 2026-05-05
entities_referenced: [Hooks]
concepts_referenced: []
---

Example hookify rule file demonstrating a `block` action on the `bash` event for the regex pattern `rm\s+-rf`.

**Frontmatter**:
- `name: block-dangerous-rm`
- `enabled: true`
- `event: bash`
- `pattern: rm\s+-rf`
- `action: block`

**Body** (shown to Claude when triggered): warning about deleting important files; advice to verify path, consider safer approach, ensure backups exist.

Pattern format consumed by hookify hooks (see `help--hookify.md` summary). Drop this file into `.claude/hookify.dangerous-rm.local.md` to activate.
