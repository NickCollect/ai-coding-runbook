---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/experimental/index.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/experimental/index.md
title: "Python SDK experimental features overview"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Index for experimental features in the Python SDK — features that track draft MCP specs (currently changing without notice).

**Currently available**: **Tasks** — asynchronous execution of MCP operations. Server returns a task reference immediately; clients poll for status updates and retrieve results when ready. Useful for long-running computations, batch operations, interactive workflows requiring elicitation or sampling.

**API surface**: experimental features accessed via the `.experimental` property:
```python
# Server-side
server.experimental.enable_tasks()  # auto-registers default handlers

# Client-side
result = await session.experimental.call_tool_as_task("tool_name", {"arg": "value"})
```

**Feedback** especially valuable — open issues at `python-sdk` repo. Implements draft MCP Tasks per SEP-1686.
