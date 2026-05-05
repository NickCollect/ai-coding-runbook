---
type: qa
topic: integration-patterns
created: 2026-05-05
sources:
  - 02_Wiki/Synthesis/mcp-integration-guide.md
  - 02_Wiki/Synthesis/agentic-workflow-patterns.md
  - 02_Wiki/Comparison/agentic-sdk-comparison.md
  - 02_Wiki/Entities/Agent-SDK.md
  - 02_Wiki/Summaries/models--openai-docs.md
---

# Integration Patterns Q&A

## Q: 什么时候用 MCP，什么时候直接 function calling？
**A:** 用 **MCP** 当：集成第三方服务（Notion、GitHub、Sentry 等已有官方 server）；工具需要跨 session / 跨团队共享（`.mcp.json` project scope）；工具逻辑在第三方服务端托管；需要 server-initiated notifications（MCP 双向通信）。用 **Function Calling / Tool Use** 当：工具逻辑在自己代码里、stateless 单次调用、不需要额外基础设施、只服务单个 agent。MCP 本质上是 tool use 的基础设施层，为复用和跨平台共享而生；简单场景直接 tool use 更轻量。
*来源：[[mcp-integration-guide]]*

---

## Q: Claude Code 怎么加本地 MCP server？
**A:** 使用 stdio transport：`claude mcp add --transport stdio --env KEY=value <name> -- npx -y <package>`。常用选项：`--scope local`（默认，存 `~/.claude.json`，不团队共享）、`--scope project`（存 `.mcp.json`，可 git 共享）、`--scope user`（所有项目生效）。验证：`claude mcp list` 查看已配置的 server，会话中运行 `/mcp` 查看状态和认证。注意 stdio server 不支持自动重连，连接断开需手动重启。
*来源：[[mcp-integration-guide]]*

---

## Q: OpenAI Responses API 和 Chat Completions API 什么区别？
**A:** 待确认（数据截至 2026-05-05）。当前 wiki 中 models--openai-docs.md 指出"所有模型通过 Responses API 和 Client SDK 访问"，streaming-comparison.md 记录 Responses API 使用 20+ 点分事件类型（`response.output_text.delta` 等），而旧版 Chat Completions API 使用 `choices[0].delta`。Responses API 是新标准，内置 multi-turn、tools、MCP 支持；Chat Completions 是 legacy endpoint。具体 feature 差异需核实 platform.openai.com 文档（raw 未完整覆盖）。
*来源：[[streaming-comparison]]、[[models--openai-docs]]*

---

## Q: 如何实现多模型 orchestration？
**A:** 三家框架**不直接互操作**，但有以下组合路径：(1) **API 层自行 orchestrate**：在自己代码中按顺序调用不同厂商 API（最大灵活性，最多自建工作量）；(2) **MCP 作为中立层**：将工具发布为 MCP server，Claude Agent SDK 和 OpenAI Agents SDK 均可调用同一 server；(3) **第三方框架**：LangGraph / CrewAI / LlamaIndex 支持多模型作为 backend，可在不同节点/角色使用不同模型；(4) **Claude Agent SDK subagent 指定 model**：`AgentDefinition(model="gpt-5.5" 或其他 alias)` 理论可指向不同模型，但跨厂商支持*待确认*。
*来源：[[agentic-sdk-comparison]]、[[mcp-integration-guide]]*

---

## Q: Gemini 有没有官方的 agentic SDK？
**A:** **没有**。Gemini 没有官方的 agentic SDK（类比 Claude Agent SDK 或 OpenAI Agents SDK）。Gemini 的 agentic 能力通过以下方式实现：(1) 原生 Gemini API（function calling + long context + thinking）；(2) 第三方框架：LangChain/LangGraph（复杂有状态流程）、LlamaIndex（RAG 集成）、CrewAI（协作式 agent）、Vercel AI SDK（JS/TS）、Google ADK（Google 官方开源框架）。Google ADK 是 Google 提供的官方开源 framework，可构建可互操作的 agents，但它是框架而非 SDK。
*来源：[[agentic-sdk-comparison]]*

---

## Q: Claude subagent 跨会话怎么保持状态？
**A:** Subagent 的 session 持久化为 JSONL 文件（仅对话历史，非文件系统快照）。跨 session 继续：Python 用 `continue_conversation=True`（最近一次 session）或 `resume=session_id`（指定 session）；TypeScript 用 `continue: true` 或捕获 session ID 后 `resume`。**重要限制**：subagent 始终以全新 context 启动，不继承父 session 历史——跨会话的"状态"仅指 subagent 自身的 JSONL 对话历史，不含父 agent 的中间状态。若需真正的跨 session 共享状态，需自行设计外部存储（数据库、文件系统）并在 subagent system prompt 中注入。
*来源：[[agentic-sdk-comparison]]*
