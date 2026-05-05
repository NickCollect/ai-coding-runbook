---
type: entity
name: Anthropic-SDK-TypeScript
aliases: [anthropic TS SDK / @anthropic-ai/sdk / anthropic-sdk-typescript]
category: sdk
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic TypeScript / Node 客户端 —— `npm install @anthropic-ai/sdk`，访问 Claude API。

## 关键属性

- **Install**：`npm install @anthropic-ai/sdk`（标准 Node / TypeScript） [[README--anthropic-sdk-ts]]
- **Streaming helpers**：`.stream(...).on("text", cb)`，`await stream.finalMessage()` [[streaming--bwc]] [[README--anthropic-sdk-ts]]
- **Tool runner**：
  - `betaZodTool({name, description, inputSchema: z.object({...}), run: async (input) => ...})` —— 推荐，type-safe with Zod 3.25.0+，runtime validation
  - `betaTool()` —— JSON schema 无 runtime validation，自己 validate inside `run` [[Tool-runner]]
- **Memory tool helper**：`betaMemoryTool` 接自定义 backend [[Memory-tool]]
- **Beta features**：beta endpoints 通过 `client.beta.messages.create(...)` 等
- **Repo**：`anthropics/anthropic-sdk-typescript`
- **CHANGELOG**：repo 内 [[CHANGELOG--anthropic-sdk-ts]]
- **MIT-licensed**
- **vs [[Agent-SDK]]**：Agent SDK Python 已 GA，TypeScript 版 deprecated（claude-code-sdk-typescript repo 404）—— Node 跑 agent 推荐自己用 Anthropic SDK 写 loop 或调 Python SDK via IPC
- **Edge / serverless 支持**：标准 fetch-based，可在 Cloudflare Workers / Vercel Edge / Deno 等 runtime 跑

## 出现来源

_15 summaries reference this entity_ ——
- [[README--anthropic-sdk-ts]] / [[CHANGELOG--anthropic-sdk-ts]] / [[CONTRIBUTING--anthropic-sdk-ts]] / [[SECURITY--anthropic-sdk-ts]]
- [[streaming--bwc]] / [[get-started--platform]] / [[intro--platform]]
- [[tool-runner--at]] / [[memory-tool--at]] / [[handle-tool-calls--at]]

## 相关

- [[Anthropic-SDK-Python]] —— Python 等价
- [[Agent-SDK]] —— 高层 harness（Python only as of 2026-05；TypeScript deprecated）
- [[Tool-runner]] —— SDK 内 agentic loop helper
- [[Messages-API]] / [[Streaming-API]] / [[Tool-use]] / [[MCP-server]]
