---
type: entity
name: Managed-agent
aliases: [managed agents / Claude Managed Agents / agent (beta) / BetaManagedAgentsAgent]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Anthropic-managed 的 server-side agent 资源 —— `/v1/agents`，平台持久化 + 版本化的 agent definition（与 Claude Code、Agent SDK 平行的"高层 agent harness"）。

## 关键属性

- **Beta header**：`anthropic-beta: managed-agents-2026-04-01` [[agents-index--beta-api]]
- **Endpoints**：
  - `POST /v1/agents` —— Create
  - `GET /v1/agents` —— List（filterable by `created_at[gte|lte]`、`include_archived`，cursor pagination）
  - `GET /v1/agents/{agent_id}` —— Retrieve
  - `POST /v1/agents/{agent_id}` —— Update（**需当前 `version` 用于 optimistic concurrency**）
  - `POST /v1/agents/{agent_id}/archive` —— soft delete
  - `GET /v1/agents/{agent_id}/versions` —— List versions（每次 update 自动 increment `version`） [[agents-index--beta-api]]
- **Domain model `BetaManagedAgentsAgent`**：
  - `id` / `type: "agent"` / `name` / `description` / `system`（system prompt ≤ 100K chars）
  - `model`（`BetaManagedAgentsModel` ID 如 `claude-opus-4-7` 等，或 `model_config` object 含 `id` + `speed: "standard" | "fast"`）
  - `mcp_servers`（max 20，URL-typed MCP servers，name 唯一）
  - `skills`（max 20，每个 `anthropic` 或 `custom`，可选 version pin）
  - `tools`（max 128 跨 toolset，混 `agent_toolset_20260401` 内置 `bash`/`edit`/`read`/`write`/`glob`/`grep`/`web_fetch`/`web_search`、`mcp_toolset` references、client-executed `custom` tools）
  - `metadata`（≤ 16 KV pairs）
  - `created_at` / `updated_at` / `archived_at` + monotonically-increasing `version` [[agents-index--beta-api]]
- **Permission policies** (per-tool 或 `default_config`)：`always_allow` / `always_ask` —— 同 [[Permission-mode]] 但 server-side [[agents-index--beta-api]]
- **运行依赖**：通过 [[Session-API]] 创建 conversation、绑 [[Vault]] 拿 credentials、用 [[Environment-API]] 选 sandbox、引 [[Skill-API]] 加 capability、引 [[MCP-server]] 加 tool
- **Workflow vs [[Messages-API]]**：Messages = 直 prompting；Managed Agent = 高层 harness（适合长跑 / 异步 / 跨 session 任务） [[working-with-messages--bwc]]
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header
- **Skills 双 beta header**：use skills 还需 `skills-2025-10-02` [[skills-index--beta-api]]

## 出现来源

_41 summaries reference this entity_ ——
- [[agents-index--beta-api]] / [[agents-create--beta-api]] / [[agents-list--beta-api]] / [[agents-retrieve--beta-api]] / [[agents-update--beta-api]] / [[agents-archive--beta-api]] / [[agents-delete--beta-api]] / [[agents-versions-index--beta-api]] / [[agents-versions-list--beta-api]]
- [[overview--ma]] / [[agent-setup--ma]] / [[onboarding--ma]] / [[quickstart--ma]] / [[memory--ma]] / [[mcp-connector--ma]] / [[github--ma]] / [[skills--ma]] / [[sessions--ma]] / [[cloud-containers--ma]] / [[multi-agent--ma]] / [[permission-policies--ma]] / [[define-outcomes--ma]] / [[events-and-streaming--ma]] / [[tools--ma]]
- [[working-with-messages--bwc]] / [[sessions-index--beta-api]] / [[messages-create--beta-api]]

## 相关

- [[Session-API]] / [[Environment-API]] / [[Vault]] / [[Skill-API]] / [[Memory-store]] / [[User-profile]] —— Managed Agent 的子资源 / 配套
- [[MCP-server]] / [[Tool-use]] / [[Permission-mode]] —— config 维度
- [[Messages-API]] —— 平行的"低层" agent 构建路径
- [[Agent-SDK]] / [[Native-interface]] —— 客户端 alternative agent harness
