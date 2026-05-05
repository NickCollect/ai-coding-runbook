---
type: summary
source: 01_Raw/code.claude.com/docs/en/checkpointing.md
source_url: https://code.claude.com/docs/en/checkpointing
title: "Checkpointing"
summarized_at: 2026-05-05
entities_referenced: [Checkpointing]
concepts_referenced: [Context-window]
---

Claude Code automatically captures pre-edit state for every user prompt, providing a session-level undo / rewind / summarize tool.

**Auto-tracking**:
- Every user prompt creates a new checkpoint
- Persists across sessions (accessible after `--resume`)
- Cleaned up with sessions after 30 days (configurable)

**Open the rewind menu**: press `Esc` twice or run `/rewind`. A scrollable list shows your prompts; pick one and choose:
- **Restore code and conversation** — full revert
- **Restore conversation** — rewind chat, keep current code
- **Restore code** — revert files, keep conversation
- **Summarize from here** — replace selected message + everything after with a compact AI summary; no files changed; original messages preserved in transcript
- **Never mind** — return without changes

After restoring conversation or summarizing, the original prompt is reloaded into the input field for editing/resending.

**Restore vs. summarize**: restore options revert state; summarize is targeted compression (vs. `/compact` which compresses the whole conversation). Useful when you want to keep early context in full but compress a verbose midpoint debugging session.

For branching to try a different approach while preserving the original session intact, use **fork** (`claude --continue --fork-session`) instead.

**Limitations** (important):
- **Bash command changes NOT tracked**. `rm`, `mv`, `cp` from Bash tool are not undoable through rewind. Only direct file-edit-tool changes are tracked.
- **External changes NOT tracked**. Manual edits outside Claude Code or edits from concurrent sessions are usually not captured (unless they touch the same files).
- **Not a Git replacement**. Think of checkpoints as "local undo," Git as "permanent history."

Use cases: exploring alternatives, recovering mistakes, iterating on features, freeing context space mid-session.
