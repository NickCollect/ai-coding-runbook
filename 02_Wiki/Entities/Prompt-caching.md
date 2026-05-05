---
type: entity
name: Prompt-caching
aliases: [prompt cache, cache control, cached prompts]
category: feature
status: ga
created: 2026-05-05
note: cross-product entity (referenced by P1 summaries; full enrichment in P2 with API docs)
---

## 一句话定义

Claude API 跨请求复用 prompt prefix 的机制（cost + latency 优化）

## 关键属性

- 核心不变量：**prompt caching 是 prefix match**——前缀任一字节变动都会作废下游所有缓存；cache key = 到每个 `cache_control` 断点的精确字节 [[prompt-caching--claude-api-skill]]
- Render 顺序固定为 `tools → system → messages`；在最后一段 system block 上打断点 = 一并缓存 tools+system [[prompt-caching--claude-api-skill]]
- API：`cache_control: {type: "ephemeral"}` 默认 5 分钟 TTL；加 `ttl: "1h"` 切 1 小时；每个 request 最多 4 个断点；可放任何 content block（text/image/tool_use/tool_result/document） [[prompt-caching--claude-api-skill]]
- 最小可缓存 prefix（model-dependent，低于阈值静默不缓存）：Opus 4.7 / 4.6 / 4.5 / Haiku 4.5 = 4096 tokens；Sonnet 4.6 / Haiku 3.5 / Haiku 3 = 2048；Sonnet 4.5 / 4.1 / 4 / 3.7 = 1024 [[prompt-caching--claude-api-skill]]
- 经济模型：cache reads ≈ 0.1× base price；writes 1.25× (5min TTL) 或 2× (1h TTL)；break-even 5min = 2 次请求，1h = 3 次请求 [[prompt-caching--claude-api-skill]]
- 失效层级（变更作废本层 + 以下层）：tool defs 改动 → 全部 invalidated；model 切换 → 全部；`speed` / web-search / citations toggle、system prompt 内容 → system+messages；`tool_choice` / images / `thinking` toggle / message 内容 → 仅 messages [[prompt-caching--claude-api-skill]]
- 验证命中：response `usage.cache_read_input_tokens` + `cache_creation_input_tokens` + `input_tokens`（uncached 余下）；总 input = 三者之和；重复相同前缀仍 0 read 说明有 silent invalidator [[prompt-caching--claude-api-skill]]
- Silent invalidator 常见来源：system prompt 里的 `datetime.now()` / `time.time()`、早期内容里的 `uuid4()` / `crypto.randomUUID()`、`json.dumps()` 不带 `sort_keys`、迭代 `set`、f-string 注入 session/user ID、conditional system 段、`tools=build_tools(user)` 用户级 tool 集 [[prompt-caching--claude-api-skill]]
- 20-block lookback 窗口：每个断点最多向前回看 20 个 content block 找之前的 cache 入口；长 agentic loop 单 turn 内 tool_use/tool_result 对超 20 会 silent miss——每 ~15 块加中间断点 [[prompt-caching--claude-api-skill]]
- 并发请求时序：cache 只在第一个 response **开始 streaming** 后才可读；N 个相同前缀的并发请求全付 full price——fan-out pattern 是先发 1 等首 token，再发剩余 N−1 [[prompt-caching--claude-api-skill]]
- Subagent / fork 必须 verbatim 复用父的 `system` / `tools` / `model`，否则 miss 父的 cache；sub-agent / 摘要场景同理 [[prompt-caching--claude-api-skill]]
- Claude Code 把 system prompt / CLAUDE.md / tool defs 等稳定 prefix 自动 prompt-cache；CLAUDE.md 在每次请求都被 re-inject（如果通过 `settingSources` 加载） [[agent-loop]]
- Enterprise gateway（Bedrock / Vertex / Foundry）下 caching 默认开启；`ENABLE_PROMPT_CACHING_1H=1` 切 1h TTL；Vertex 上 `DISABLE_PROMPT_CACHING=1` 可关闭 [[amazon-bedrock]] [[google-vertex-ai]] [[microsoft-foundry]]
- LLM gateway 的 attribution header（client version + conversation fingerprint）会被 Anthropic API 处理前剥离不影响 first-party cache；若 gateway 自己按完整 body 做 cache，设 `CLAUDE_CODE_ATTRIBUTION_HEADER=0` 关掉 [[llm-gateway]]
- **完整 pricing matrix**（per MTok）—— from [[prompt-caching--bwc]]：
  | Model | Base input | 5m write | 1h write | Cache hit | Output |
  |---|---|---|---|---|---|
  | Opus 4.7 / 4.6 / 4.5 | $5 | $6.25 | $10 | $0.50 | $25 |
  | Sonnet 4.6 / 4.5 / 4 | $3 | $3.75 | $6 | $0.30 | $15 |
  | Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 |
  | Haiku 3.5 | $0.80 | $1 | $1.6 | $0.08 | $4 |
- **Multipliers** 结构：5m write = 1.25× base；1h write = 2× base；cache read = 0.1× base —— 与 [[Batches-API]] (50% off) 和 data residency (1.1× US) stack [[prompt-caching--bwc]]
- **两种 enablement 模式**：
  - **Auto** —— 单 top-level `cache_control: {type: "ephemeral"}`；系统自动应用断点到最后 cacheable block 并随对话推进
  - **Explicit** —— 在 individual content blocks 上放 `cache_control` 细粒度控制 [[prompt-caching--bwc]]
- **Cache 覆盖顺序**：`tools` → `system` → `messages` 全 prefix（直到含 `cache_control` 的 block） [[prompt-caching--bwc]]
- **`max_tokens: 0` 缓存预热**：可用，但 **[[Batches-API]] 内不支持**（cache 可能在 follow-up 跑前过期） [[prompt-caching--bwc]] [[batch-processing--bwc]]
- **ZDR-eligible**（仅 KV cache 表示 + 加密 hash 在内存里 cache TTL 内，不含 prompt/output） [[prompt-caching--bwc]]
- **Citations 兼容**：document block 加 `cache_control` —— citation 自身不能 cache，但 source document 可 [[Citations-API]]
- **[[Tool-search-tool-API]] 兼容**：deferred tool 从 prefix 剥离 → cache key 不变；discovered tool 作 inline reference block in body [[tool-search-tool--at]]
- **[[Advisor-tool]] cache 两层**：executor-side（`advisor_tool_result` 加 cache_control）+ advisor-side（`caching` field on tool）；break-even ≈ 3 advisor call [[advisor-tool--at]]


## 出现来源

_24 summaries reference this entity_:

- [[2026-w16]]
- [[agent-design]]
- [[agent-loop]]
- [[amazon-bedrock]]
- [[batches--python]]
- [[changelog--claude-code-repo]]
- [[claude-api--csharp]]
- [[claude-api-go]]
- [[claude-api-php]]
- [[claude-api-ruby]]
- [[claude-api-skill]]
- [[cost-tracking]]
- [[costs]]
- [[env-vars]]
- [[google-vertex-ai]]
- [[llm-gateway]]
- [[managed-agents-core]]
- [[microsoft-foundry]]
- [[model-config]]
- [[modifying-system-prompts]]
- [[monitoring-usage]]
- [[output-styles]]
- [[prompt-caching--claude-api-skill]]
- [[third-party-integrations]]

## 相关

- [[Context-window]] — caching 是降低重复 context 的成本工具；context window 增长时 caching 收益线性提升
- [[Tool-use]] — tools 在 prompt 渲染顺序最前；改 tools 必使全部 cache 失效，因此 tool 集要稳定
- [[Agent-SDK]] — SDK 默认对稳定 prefix 启用 caching；agent loop 在每 turn 累加 messages，便于在最新 user turn 末尾打断点
- [[Agentic-loop]] — 长 loop 单 turn 内多对 tool_use/tool_result 可能超过 20-block lookback 窗口，导致静默 miss
- [[Enterprise-gateway]] — Bedrock / Vertex / Foundry 都支持 caching，但 1h TTL 走专用 env var
- [[Extended-thinking]] — toggle `thinking` 仅作废 messages 层；不影响 tools+system cache
