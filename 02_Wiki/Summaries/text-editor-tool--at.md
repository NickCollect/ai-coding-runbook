---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool
title: "Text editor tool"
summarized_at: 2026-05-05
entities_referenced: [Text-editor-tool, Tool-use, Bash-tool-API]
concepts_referenced: []
---

The [[Text-editor-tool]] (`str_replace_based_edit_tool`) lets Claude view and modify text files via Anthropic-defined schema, with execution handled client-side. **Eligible for ZDR.** Tool type: `text_editor_20250728` for Claude 4 models, `text_editor_20250124` for earlier (Sonnet 3.7).

**When to use.** Code debugging (syntax errors → logic issues); refactoring (structure, readability, performance); documentation generation (docstrings, comments, READMEs); test creation (unit tests based on implementation).

**Definition.** Schema-less tool—you don't provide an `input_schema`; the schema is built into Claude's model. Optional `max_characters` parameter (only on `text_editor_20250728`+) controls truncation when viewing large files.

**Commands.**

- *`view`*: examine a file (or list a directory). Parameters: `path`, optional `view_range: [start, end]` (1-indexed, `-1` end means EOF; only applies to files). The doc strongly recommends prepending **line numbers** ("1: def is_prime(n):") in your view output—not required, but essential for `view_range` and `insert_line` to work precisely.

- *`str_replace`*: replace exact `old_str` with `new_str` in a file. `old_str` must match exactly including whitespace and indentation. Best practice: ensure exactly one match—no matches → return error; multiple matches → return error asking for more context.

- *`create`*: create a new file with `path` and `file_text`.

- *`insert`*: insert `insert_text` after `insert_line` (use `0` for beginning).

(Note: the `undo_edit` command was removed in `text_editor_20250429` and is no longer available.)

**Workflow example.** Example walkthrough: user reports "syntax error in primes.py". Claude calls `view` → app returns line-numbered file content → Claude identifies missing colon at line 19 → Claude calls `str_replace` with `old_str: "    for num in range(2, limit + 1)"`, `new_str: "    for num in range(2, limit + 1):"` → app responds "Successfully replaced text at exactly one location." → Claude provides final explanation with `stop_reason: end_turn`.

**Error handling (`tool_result` with `is_error: true`).**
- File not found: `"Error: File not found"`.
- Multiple matches for str_replace: `"Error: Found 3 matches for replacement text. Please provide more context to make a unique match."`
- No matches: `"Error: No match found for replacement. Please check your text and try again."`
- Permission errors: `"Error: Permission denied. Cannot write to file."`

**Implementation best practices.**
- *Backups*: copy file to `.backup` before editing important files.
- *Path validation*: prevent directory traversal (no `..`/`/etc/`).
- *Unique replacement* helper: `count = content.count(old_text)`; reject if 0 or >1.
- *Verify changes*: post-edit, run a syntax check (e.g., `ast.parse(content)` for Python).
- *Clear prompts*: "Can you check my utils/helpers.py file for any performance issues?" beats "Review my helper file".

**Pricing.** Additional input tokens per request: **700 tokens** for both `text_editor_20250429` (Claude 4.x) and `text_editor_20250124` (Sonnet 3.7).

**Pairs well with.** [[Bash-tool-API]] for running tests/builds after edits—the canonical software-development loop (inspect → edit → test → repeat).

**Change log.** `text_editor_20250728` (Jul 2025): added optional `max_characters` parameter, otherwise identical to `_20250429`. `text_editor_20250429` (Apr 2025): Claude 4 release; **removed `undo_edit`**, renamed to reflect str_replace-based architecture. `text_editor_20250124` (Mar 2025): Sonnet 3.7 standalone docs. `text_editor_20241022` (Oct 2024): initial release with Sonnet 3.5 (retired); had `view`, `create`, `str_replace`, `insert`, and `undo_edit`.
