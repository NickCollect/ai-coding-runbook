# Canonical Names — Entity Registry + 错别字勘误表

> **enrich / 写 summary 前必读** —— 这是 vault 的单一事实源。
> Raw 文档里同一概念可能有多个写法，vault 内统一用 canonical 名，aliases 在每个 entity 的 frontmatter。
>
> 新发现 raw 里有不一致写法 → 在这里登记 → entity frontmatter `aliases:` 加上变体 → 再 enrich。

---

## 命名约定

- 多词 entity 用 `Hyphen-Joined` (`MCP-server`, `Slash-command`, `Agent-SDK`, `Status-line`)
- entity frontmatter `aliases:` 列所有变体（含 raw 中的错别字 / 单复数 / 连字符差异 / 大小写差异）
- summary frontmatter `entities_referenced:` / `concepts_referenced:` 字段**必须用 canonical 名**
- 不确定时 `ls 02_Wiki/Entities/ 02_Wiki/Concepts/` 先看真实存在的文件

---

## P1 Entity Registry（25 entities + 4 concepts）

### Entities (`02_Wiki/Entities/`)

**核心 features**

| Canonical | Raw 中常见变体 |
|---|---|
| Hooks | hook / hook system / session hooks |
| Skill | skills / Anthropic Skill / agent skill |
| Plugin | Claude Code plugin / claude-plugin |
| Subagent | sub-agent / sub agent / subagents / Sub-agent |
| Slash-command | slash command / slash-command / /command |
| MCP-server | MCP / Model Context Protocol server / MCP 服务器 |
| Output-style | output style / output styles |
| Status-line | statusline / status line |
| Memory | memory system / Claude Code memory |
| Checkpointing | checkpoint / file checkpoints |
| Settings | settings.json / user settings / project settings |
| Plugin-marketplace | plugin marketplace / marketplace |

**执行模式 / config**

| Canonical | 变体 |
|---|---|
| Permission-mode | permission mode / permission modes |
| Sandboxing | sandbox / Claude Code sandbox |
| Auto-mode | auto mode / auto-mode-config |
| Fast-mode | fast mode |
| Headless-mode | headless / headless mode / non-interactive |
| Computer-use | computer use / computer-use tool |
| Routine | routines / scheduled routine（云端 cron） |
| Scheduled-task | scheduled task / scheduled tasks（桌面端定时） |

**集成 / 接口**

| Canonical | 包含 |
|---|---|
| Agent-SDK | claude-agent-sdk / agent-sdk / Claude Agent SDK |
| IDE-integration | VS Code / JetBrains / Chrome 扩展 |
| Native-interface | CLI / Desktop / Web / Slack |
| CI-integration | GitHub Actions / GitLab CI/CD |
| Enterprise-gateway | Amazon Bedrock / Google Vertex AI / Microsoft Foundry / LLM Gateway |

### Concepts (`02_Wiki/Concepts/`)

| Canonical | 变体 |
|---|---|
| Agentic-loop | agent loop / agentic loop / tool use loop |
| Context-window | context window / 上下文窗口 |
| Channel | channels / Claude Code channels |
| Agent-team | agent teams / subagent team |

---

## 跨产品概念（不属于 Claude Code，但 raw 里频繁出现）

| Canonical | 变体 / 备注 |
|---|---|
| Tool-use | Function calling（其他 vendor 术语，Anthropic docs 偶尔混用） |
| Extended-thinking | extended-thinking / thinking mode / interleaved thinking（thinking mode 偶指别的） |
| Prompt-caching | prompt cache / cache control / cached prompts |

> 这些将来 P2/P3 enrich Anthropic API docs 时建对应 entity；P1 阶段如 summary 提到，写到 `entities_referenced` 但**不要** create stub。

---

## P2 Entity Registry（Anthropic API 层）

### Core API entities

| Canonical | Raw 中变体 | 说明 |
|---|---|---|
| Messages-API | Messages / messages.create / `/v1/messages` | 主要 chat completion endpoint |
| Completions-API | text completions / claude-1 era API | legacy（建议用 Messages） |
| Token-counting | count_tokens / token counter | `/v1/messages/count_tokens` |
| Batches-API | message batches / batch processing / batch API | 异步批量请求 |
| Streaming-API | streaming / SSE streaming / stream events | event-based 增量返回 |
| Files-API | files / file upload / file metadata | beta，`/v1/files` |
| Citations-API | citations / cited responses | 引用文档片段 |
| Structured-outputs | structured outputs / strict outputs / response_format | JSON schema 强制 |
| Vision | vision / image understanding / image input | multimodal 图像 |
| PDF-support | pdf / pdf documents | base64 / files API PDF 输入 |
| Embeddings | text embeddings / embedding API | 第三方供应商（Voyage 等），不是 Anthropic 自有 |
| Adaptive-thinking | adaptive thinking | 与 Extended-thinking 区分 |
| Effort | effort parameter / `effort` | low/medium/high token budget |
| Compaction | context compaction | 自动 message 压缩 |
| Context-editing | context editing / message edit | 在长 context 中编辑 |
| Search-results | search results blocks / search blocks | 工具返回结构化结果 |

### Server tools (Anthropic-managed, distinct from local Claude Code tools)

| Canonical | 说明 |
|---|---|
| Code-execution-tool | server-managed Python sandbox（仅 API） |
| Web-search-tool | server-managed web search（仅 API） |
| Web-fetch-tool | server-managed URL fetch（仅 API） |
| Memory-tool | server-managed persistent memory（仅 API，区别于 Claude Code [[Memory]]） |
| Text-editor-tool | server-managed file editing（仅 API） |
| Bash-tool-API | server-managed shell（仅 API，区别于 Claude Code 的 Bash 工具） |
| Computer-use-tool-API | server-managed computer use（仅 API，区别于 [[Computer-use]]） |
| Tool-search-tool-API | server-managed tool search（区别于 Claude Code [[Permission-mode]] 自动模式） |
| Tool-runner | API tool runner harness |
| Advisor-tool | beta advisor tool |

### Beta API entities (managed agents / sessions / vaults)

| Canonical | 说明 |
|---|---|
| Managed-agent | beta `/v1/beta/agents` —— 云端管理的 agent |
| Session-API | beta `/v1/beta/sessions` —— 持久 conversation |
| Environment-API | beta `/v1/beta/environments` —— 沙盒执行环境 |
| Memory-store | beta `/v1/beta/memory_stores` —— 持久 memory storage |
| Vault | beta `/v1/beta/vaults` —— credentials 加密存储 |
| Skill-API | beta `/v1/beta/skills` —— 远程 skill 管理（区别于 Claude Code [[Skill]]） |
| User-profile | beta `/v1/beta/user_profiles` —— end-user 身份管理 |

### Admin API entities

| Canonical | 说明 |
|---|---|
| Admin-API | 全局名 for `/v1/organizations/...` admin endpoints |
| Workspace | admin workspace（org 内 sub-unit） |
| API-key | admin-managed API key |
| Cost-report | usage cost reporting endpoint |
| Usage-report | message + Claude Code 使用统计 |
| Rate-limit-API | per-org / per-workspace rate limit |
| Invite | workspace member invitation |

### SDK (raw API client，distinct from Agent-SDK)

| Canonical | 说明 |
|---|---|
| Anthropic-SDK-Python | `anthropic` Python package |
| Anthropic-SDK-TypeScript | `@anthropic-ai/sdk` |
| Anthropic-SDK-Go | `anthropic-sdk-go` |
| Anthropic-SDK-Java | `anthropic-sdk-java` |

> P2 enrichment 时这些都建 entity（除非 source < 2 raw 支撑则 deferred）。

---

## Model 名字

| Canonical | model ID |
|---|---|
| Opus 4.7 | claude-opus-4-7 |
| Sonnet 4.6 | claude-sonnet-4-6 |
| Haiku 4.5 | claude-haiku-4-5-20251001 |
| Opus 4.6 | claude-opus-4-6（Fast mode 用此 model） |

---

## 维护规则

1. 发现新变体 → 加到对应 canonical 行的"变体"列
2. 发现完全新概念 → 在合适 section 加新行
3. 不确定哪个是 canonical → 先问用户
4. **不要**因为 raw 里某个写法出现得多就改 canonical —— canonical 是设计选择，跟出现频次无关
