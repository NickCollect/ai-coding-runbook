---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1303-input-validation-errors-as-tool-execution-errors.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1303-input-validation-errors-as-tool-execution-errors.md
title: "SEP-1303: Input validation errors as tool execution errors"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Tool-use]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-08-05 | Author: @fredericbarthelet**

Clarifies that tool input-validation errors should be returned as **Tool Execution Errors** (visible to the LLM via tool result with `isError: true`) rather than **Protocol Errors** (caught at MCP client level, invisible to model).

**Problem**: the existing tool error spec gave ambiguous guidance — "Invalid arguments" → Protocol Error; "Invalid input data" → Tool Execution Error. This led to validation errors being lost: when an LLM provides a syntactically-valid-but-semantically-invalid date (e.g., a past date for a flight booking), the model retries blindly because it never sees the error message.

**Concrete example**: a `book_flight` tool rejects a past date. Before this SEP, a Protocol Error returns `code: -32602, "Invalid params"` — the model never sees the explanation, retries with another past date, and the loop fails. After this SEP, the same case returns a Tool Execution Error with text content "Dates must be in the future. Current date is 08/08/2025" — the model sees this and corrects itself.

**Specification change**: removes "invalid argument" from Protocol Errors; merges `invalid argument` and `invalid input data` into a new **Input Validation Errors** category under Tool Execution Errors.

**Benefits**: higher task completion rates (model self-corrects); better UX (fewer failures, faster); leverages modern LLM capabilities; reduced API call retries.

Fully backward compatible — clarifies existing ambiguous behavior, doesn't change protocol structure or message formats.
