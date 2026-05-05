---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
title: "Memory tool"
summarized_at: 2026-05-05
entities_referenced: [Memory-tool, Tool-use, Text-editor-tool, Context-editing, Compaction]
concepts_referenced: [Context-window]
---

The [[Memory-tool]] enables Claude to store and retrieve information across conversations through a memory file directory. Claude can create, read, update, and delete files that persist between sessions, allowing it to build knowledge over time without keeping everything in the [[Context-window]]. This is the key primitive for *just-in-time context retrieval*: rather than loading all relevant info upfront, agents store what they learn in memory and pull it back on demand. **Eligible for ZDR.**

The tool operates **client-side**: you control where and how the data is stored through your own infrastructure—Claude makes tool calls, your application executes them locally. For security, restrict all memory operations to the `/memories` directory.

**Use cases.** Maintain project context across multiple agent executions; learn from past interactions and feedback; build knowledge bases over time; cross-conversation learning where Claude improves at recurring workflows.

**Mechanism.** When enabled, Claude automatically checks `/memories` before starting tasks. It can `view`, `create`, `str_replace`, `insert`, `delete`, `rename` files. Walkthrough example: user asks for help with a customer service ticket → Claude `view`s `/memories` → reads `customer_service_guidelines.xml` → applies the guidelines to the response.

**Tool definition.** `{"type": "memory_20250818", "name": "memory"}`. SDKs provide helpers (`BetaAbstractMemoryTool` in Python; `betaMemoryTool` in TypeScript) for plugging in your own backend (file-based, database, cloud storage, encrypted files, etc.).

**Tool commands** (your client-side implementation must handle):
- `view`: directory listing (2 levels deep, human-readable sizes, excludes hidden + node_modules) or file contents with 1-indexed line numbers (6-char-wide right-aligned, tab separator). Files >999,999 lines should error.
- `create`: new file with `file_text`. Errors if file already exists.
- `str_replace`: in-place text replacement; errors if `old_str` not found verbatim or appears multiple times (lists line numbers).
- `insert`: insert `insert_text` at `insert_line`. Errors on invalid line number.
- `delete`: file or directory (recursive).
- `rename`: move/rename; errors if destination exists (no overwrite).

The doc gives the *exact return string formats* Claude is most familiar with (e.g., `"File created successfully at: {path}"`, `"The memory file has been edited."`, `"Successfully deleted {path}"`)—you can return different strings if needed for your use case, but matching reduces Claude confusion.

**System prompt injection.** When the memory tool is enabled, this instruction is automatically appended:
> IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE. MEMORY PROTOCOL: 1. Use the `view` command of your `memory` tool to check for earlier progress. 2. ... (work on the task) ... — As you make progress, record status / progress / thoughts etc in your memory. ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.

If Claude creates cluttered memory, suggested addendum: "Always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary."

**Security.**
- Sensitive info: Claude usually refuses to write secrets, but implement stricter validation that strips potentially sensitive data.
- File-size guardrails: track file sizes; cap returned characters; let Claude paginate long files.
- Memory expiration: clear stale files periodically.
- **Path traversal protection (CRITICAL):** Validate that all paths start with `/memories`; resolve to canonical form and verify they remain within the memory directory; reject `../`, `..\\`, URL-encoded `%2e%2e%2f`. Use built-in path utilities (`pathlib.Path.resolve()` and `relative_to()` in Python).

**Error handling.** Mirrors the [[Text-editor-tool]] error patterns. Common errors: file not found, permission errors, invalid paths, duplicate text matches.

**Pairing with other features.** [[Context-editing]] trims old `tool_result` blocks while memory persists what matters across the trim. [[Compaction]] summarizes the whole conversation server-side as it nears the context window limit—pair both: compaction keeps active context manageable without client-side bookkeeping; memory persists important info across compaction boundaries so nothing critical is lost in the summary.

**Multi-session software development pattern.** For long-running projects spanning multiple agent sessions, bootstrap memory deliberately:
1. *Initializer session* sets up memory artifacts before substantive work: a progress log, a feature checklist, a reference to any startup script.
2. *Subsequent sessions* open by reading those artifacts—recovers full project state in seconds without re-exploring the codebase.
3. *End-of-session update* records what was completed and what remains, so the next session has an accurate starting point.

Key principle: work on one feature at a time. Only mark complete after end-to-end verification, not just after the code is written. This keeps the progress log trustworthy and prevents scope creep from compounding across sessions.
