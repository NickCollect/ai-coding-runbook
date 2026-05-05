---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/client-quickstart.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client-quickstart.md
title: "TS SDK Client Quickstart — build LLM-powered chatbot"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Hands-on tutorial building an LLM-powered chatbot that connects to an MCP server, discovers its tools, and uses Claude to call them.

**Prerequisites**: TypeScript + LLM familiarity, Node.js 20+ (or Bun/Deno), npm, an Anthropic API key from `console.anthropic.com`.

Helps if you've gone through the server quickstart first to understand client/server communication. Complete code at `examples/client-quickstart/` in the repo. Walks through project setup, env config, the chatbot loop that: connects to the MCP server, lists tools, sends user input + tool definitions to Claude, executes tool calls Claude requests, returns results back to Claude for a final response.
