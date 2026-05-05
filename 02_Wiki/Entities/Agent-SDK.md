---
type: entity
name: Agent-SDK
aliases: [claude-agent-sdk, agent-sdk, Claude Agent SDK]
category: sdk
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic 提供的 Python SDK，构建用 Claude Code 同款 harness 的 agent app

## 关键属性

- Anthropic 官方 Python + TypeScript SDK，与 Claude Code 共用 tools / agent loop / context management，目标是构建 production agent（不止 coding）[[overview--agent-sdk]] [[migration-guide]]
- 包名：TS `@anthropic-ai/claude-agent-sdk`、Python `claude-agent-sdk`；前身是 `claude-code-sdk` / `@anthropic-ai/claude-code`，v0.1.0 起 rename [[migration-guide]] [[overview--agent-sdk]]
- TS 版以 optional dep 形式 bundle 平台对应的 native Claude Code binary（如 `@anthropic-ai/claude-agent-sdk-darwin-arm64`），不需另装 Claude Code；package manager skip optional dep 时用 `pathToClaudeCodeExecutable` 指向已装的 `claude` [[typescript--agent-sdk]] [[overview--agent-sdk]]
- 核心 API `query({prompt, options})` 返回 async iterator，依次 yield assistant message / tool call / tool result / 最终 ResultMessage [[overview--agent-sdk]] [[python]]
- Python 双入口：`query()`（每次 fresh session，不支持 interrupt / 多轮延续）vs `ClaudeSDKClient`（长连 session，async context manager，支持 interrupt + 多轮）[[python]] [[sessions--agent-sdk]]
- Auth 走 `ANTHROPIC_API_KEY`，或 `CLAUDE_CODE_USE_BEDROCK=1` / `CLAUDE_CODE_USE_VERTEX=1` / `CLAUDE_CODE_USE_FOUNDRY=1` 切到第三方 provider；不允许第三方提供 claude.ai login / rate limits [[overview--agent-sdk]]
- Opus 4.7（`claude-opus-4-7`）需要 Agent SDK ≥ v0.2.111，旧版本会报 `thinking.type.enabled is not supported`，要换 `thinking.type.adaptive` + `output_config.effort` [[overview--agent-sdk]] [[quickstart--agent-sdk]]
- v0.1.0 breaking change：默认不再加载 settings sources（`~/.claude/settings.json` / project / local / CLAUDE.md / 自定义 slash commands），需要手动传 `settingSources: ["user","project","local"]`；后续 release 又 revert 了，omit 等同 CLI 行为，要 isolated 必须显式 `settingSources: []` [[migration-guide]]
- v0.1.0 另一个 breaking change：默认不再用 Claude Code system prompt，要恢复需 `systemPrompt: { type: "preset", preset: "claude_code" }` [[migration-guide]]
- 输入两种模式：streaming（默认推荐，AsyncGenerator/async iterable，支持 image / queue / interrupt / hooks / MCP）vs single message（一次性 string，stateless，AWS Lambda 用，但不支持 image 附件 / interrupt / hook integration）[[streaming-vs-single-mode]]
- Sessions 自动持久化为 JSONL 在 `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`；通过 `continue` / `resume=<id>` / `forkSession` 三种方式延续；resume 时 cwd 不匹配会启全新 session [[sessions--agent-sdk]]
- Session 管理 helper：`listSessions` / `getSessionMessages` / `getSessionInfo` / `renameSession` / `tagSession`（TS + Python 同名 camelCase / snake_case）[[typescript--agent-sdk]] [[sessions--agent-sdk]]
- 自定义 tools 通过 in-process MCP server：`@tool` / `tool()` decorator + `create_sdk_mcp_server` / `createSdkMcpServer`；fully qualified 名 `mcp__{server_name}__{tool_name}`，列入 `allowedTools` 跳过 permission prompt [[custom-tools--agent-sdk]]
- 与同类对比：Client SDK 自己实现 tool loop；Agent SDK 帮你跑 loop；CLI 是同 capability 的交互界面；Managed Agents 跑在 Anthropic infra + sandbox。常见路径：本地 SDK 原型 → Managed Agents 上线 [[overview--agent-sdk]]
- 第三方产品**不允许**用 "Claude Code" 品牌，推荐用 "Claude Agent" [[overview--agent-sdk]]
- TS V2 preview 接口（unstable）拆 input / output：`createSession` + `session.send()` + `session.stream()`，比 V1 单一 async generator 简单；但还不支持 forkSession 等 [[typescript-v2-preview]]
- **vs [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]]**：
  - Agent SDK = 高层 harness（含 hooks / skills / subagent / plugin / permission mode / agentic loop / context management），等同 Claude Code CLI
  - Anthropic SDK = raw API client，你自己实现 agent loop（虽然有 [[Tool-runner]] 简化）
- **vs [[Managed-agent]]**：Agent SDK 在你机器跑；Managed Agent 在 Anthropic infra 跑（云沙盒），同时支持 [[Session-API]] / [[Vault]] / [[Memory-store]] / [[Environment-API]] 等 [[overview--agent-sdk]]
- **TypeScript 版状态**：原 `claude-code-sdk-typescript` repo deprecated（404）；v0.1.0 重命名为 `@anthropic-ai/claude-agent-sdk` 后 TS 仍持续维护；deprecated 提及在 P1 cheatsheet 已被新版本超越 [[migration-guide]]
- **新版本 v0.2.111+** 必需用于 Opus 4.7 [[overview--agent-sdk]]

## 出现来源

_45 summaries reference this entity_:

- [[agent-loop]]
- [[agent-sdk-dev--plugin-manifest]]
- [[agent-sdk-dev--readme]]
- [[agent-sdk-verifier-py]]
- [[agent-sdk-verifier-ts]]
- [[changelog]]
- [[claude]]
- [[claude-api--java]]
- [[claude-code-features]]
- [[cli-reference]]
- [[cost-tracking]]
- [[custom-tools--agent-sdk]]
- [[file-checkpointing]]
- [[github-actions]]
- [[gitlab-ci-cd]]
- [[headless]]
- [[hooks--agent-sdk]]
- [[hosting]]
- [[legal-and-compliance]]
- [[mcp--agent-sdk]]
- [[migration-guide]]
- [[modifying-system-prompts]]
- [[new-sdk-app--agent-sdk-dev]]
- [[observability]]
- [[overview--agent-sdk]]
- [[overview--claude-code]]
- [[permissions]]
- [[platforms]]
- [[plugins--agent-sdk]]
- [[python]]
- [[quickstart--agent-sdk]]
- [[secure-deployment]]
- [[sessions--agent-sdk]]
- [[skills--agent-sdk]]
- [[skills--repo-readme]]
- [[slash-commands--agent-sdk]]
- [[streaming-output]]
- [[streaming-vs-single-mode]]
- [[structured-outputs]]
- [[subagents--agent-sdk]]
- [[todo-tracking]]
- [[tool-search--agent-sdk]]
- [[typescript--agent-sdk]]
- [[typescript-v2-preview]]
- [[user-input]]

## 相关

- [[Headless-mode]] — SDK 本质是非交互调用 Claude Code 同款 harness
- [[MCP-server]] — SDK in-process MCP server 是定义 custom tool 的标准方式
- [[Hooks]] — SDK 通过 HookMatcher 注册 lifecycle 回调
- [[Subagent]] — SDK 用 `agents={...}` 程序化定义 subagent
- [[Permission-mode]] — SDK 通过 `permissionMode` + `canUseTool` 控制工具调用
- [[Agentic-loop]] — SDK 跑的就是 Claude Code 同一套 agent loop
- [[Plugin]] — SDK 支持 `type: "local"` 加载 plugin
