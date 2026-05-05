---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/sequentialthinking/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking/README.md
title: "Sequential Thinking MCP server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

TypeScript MCP server implementing a single tool for **dynamic and reflective problem-solving** through a structured thinking process.

**Features**: break down complex problems into manageable steps; revise/refine thoughts as understanding deepens; branch into alternative paths of reasoning; adjust the total number of thoughts dynamically; generate and verify solution hypotheses.

**Tool: `sequential_thinking`** — facilitates a step-by-step thinking process. Inputs:
- `thought` (string): the current thinking step
- `nextThoughtNeeded` (bool): whether another step is needed
- `thoughtNumber` (int): current thought number
- `totalThoughts` (int): estimated total
- `isRevision` (bool, optional): whether this revises previous thinking
- `revisesThought` (int, optional): which thought is being reconsidered
- `branchFromThought` (int, optional): branching point thought number
- `branchId` (string, optional): branch identifier
- `needsMoreThoughts` (bool, optional): if more thoughts are needed

**Designed for**: breaking down complex problems, planning/design with revision room, analysis needing course correction, problems where full scope isn't clear initially, multi-step context maintenance, filtering irrelevant information.

**Usage**: don't call directly — connect the server to an MCP-aware host and ask the model to think through a problem step-by-step. The host decides to call the tool one or more times. Example prompts: "Plan a database migration from PostgreSQL 14 to 16, list risks, revise if downtime exceeds 5 minutes." / "Debug why this deployment only fails in production." / "Compare three architecture options for a file sync engine and branch if an assumption is wrong."

In an Inspector or compatible host you'll see repeated `sequential_thinking` tool calls with `thought`/`thoughtNumber`/`totalThoughts`/`nextThoughtNeeded` fields, and revision/branching fields when the reasoning changes course.
