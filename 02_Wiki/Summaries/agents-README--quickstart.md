---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/agents/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/agents/README.md
title: "Claude Quickstarts — agents/ README (minimal LLM-agent reference)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, MCP-server]
concepts_referenced: [Agentic-loop, Tool-use]
---

A minimal **educational** implementation of LLM agents using the Claude API. Explicitly NOT an SDK — a reference implementation of key concepts.

**Overview.** Demonstrates how to build effective agents with the Claude API based on the Anthropic blog post "Building Effective Agents". Shows how sophisticated AI behaviors can emerge from a simple foundation: LLMs using tools in a loop. The implementation is deliberately unopinionated — core logic is <300 lines and lacks production features. Patterns are meant to be translated to other languages and production stacks.

**Three components:**

- `agent.py` — manages Claude API interactions and tool execution.
- `tools/` — tool implementations (both native and MCP tools).
- `utils/` — utilities for message history and MCP server connections.

**Usage.** Construct an `Agent` with a `name`, `system` prompt, a list of local `tools` (e.g., `ThinkTool()`), and a list of `mcp_servers` describing stdio MCP server processes. Call `agent.run("question")`. Example:

```python
agent = Agent(
    name="MyAgent",
    system="You are a helpful assistant.",
    tools=[ThinkTool()],
    mcp_servers=[
        {"type": "stdio", "command": "python", "args": ["-m", "mcp_server"]},
    ]
)
response = agent.run("What should I consider when buying a new laptop?")
```

From this foundation users add domain tools, optimize performance, or implement custom response handling.

**Requirements.** Python 3.8+. `ANTHROPIC_API_KEY` env var. `anthropic` Python library. `mcp` Python library.
