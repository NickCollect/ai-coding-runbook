---
type: summary
source: 01_Raw/anthropic.com/engineering/code-execution-with-mcp.md
source_url: https://www.anthropic.com/engineering/code-execution-with-mcp
title: "Code execution with MCP: Building more efficient agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Code-execution-tool]
concepts_referenced: [Context-window, Tool-use]
---

Anthropic post (Nov 04, 2025) on the pattern of letting agents call MCP tools by writing code inside a code-execution sandbox, rather than via direct natural-language tool calls. The pattern dramatically reduces token usage and enables larger tool libraries.

**Why direct MCP tool calling becomes inefficient at scale.**
1. *Tool definitions overload the context window.* Most MCP clients load all definitions upfront. With thousands of tools across many servers, this can mean hundreds of thousands of tokens before any user request arrives.
2. *Intermediate tool results consume tokens twice.* "Download my meeting transcript from Drive and attach it to the Salesforce lead" requires `gdrive.getDocument` (full transcript loaded into context) → then `salesforce.updateRecord` with the transcript repeated as a parameter (model writes the full transcript again into context). For a 2-hour meeting transcript, ~50,000 extra tokens. Risk of copy errors with large data.

**The fix: present MCP servers as code APIs.** Generate a file tree of all available tools from connected MCP servers; each tool is a TypeScript file that wraps `callMCPTool` with typed input/output:
```
servers/
├── google-drive/getDocument.ts
└── salesforce/updateRecord.ts
```
The agent's code becomes:
```ts
const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({ objectType: 'SalesMeeting', recordId: '...', data: { Notes: transcript } });
```

**Discovery via filesystem exploration.** Agent lists `./servers/`, reads only the specific tool files it needs. Token usage in the example: **150,000 → 2,000 tokens (98.7% saving)**.

**Other benefits the pattern unlocks** (covered in the post):
- *Filtering large lists in the sandbox* — instead of returning 10K rows from a sheet to the model, run filtering/grouping in code and return only the rows that matter.
- *Privacy-preserving operations* — sensitive data can flow between MCP servers without ever entering the model's context. PII can be tokenized in the sandbox; the model only sees pseudonyms.
- *Stateful workflows* — variables, loops, error handling are easier to express in code than in chained natural-language tool calls.
- *Skill composition* — agents can write reusable functions that combine multiple MCP tools.

**Tradeoffs.** The pattern requires a code-execution environment (more infrastructure than naive tool calling). It also depends on the model being good at writing correct code against the typed tool surface. Anthropic frames this as a complement to (not replacement for) direct tool calling — useful when tool counts are large or data flows are heavy. Closely related to the Tool Search Tool feature in [advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use).
