---
name: Prompt Caching 策略指南
type: synthesis
created: 2026-05-05
sources:
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/prompt-caching.md
  - 01_Raw/docs.openai.com/docs/guides/prompt-caching.md
  - 01_Raw/ai.google.dev/gemini-api/docs/caching.md（via summary 02_Wiki/Summaries/caching--gemini-docs.md）
---

# Prompt Caching 策略指南

> 覆盖 Anthropic Claude、OpenAI、Gemini 三大平台的 prompt caching 机制，含横向对比与实战策略。

---

## 一、Claude Prompt Caching

### 1.1 工作原理

发送请求时系统检查指定 cache breakpoint 之前的 prefix 是否已被缓存。命中则复用，未命中则处理全量并缓存 prefix（在 response 开始后写入）。

缓存覆盖的 prefix 顺序：`tools` → `system` → `messages`，包含所有标记了 `cache_control` 的块及其之前的全部内容。

### 1.2 两种启用方式

**方式 A：Automatic Caching（推荐，适合多轮对话）**

在请求 body 顶层添加单个 `cache_control` 字段。系统自动将 cache breakpoint 应用到最后一个可缓存块，并随对话增长自动前移：

```json
{
  "model": "claude-opus-4-7",
  "cache_control": { "type": "ephemeral" },
  "system": "...",
  "messages": [...]
}
```

每一轮新请求中，前面已缓存的部分从 cache 读取，新增的部分写入 cache。

**方式 B：Explicit Cache Breakpoints（精细控制）**

在具体的 content block 上放置 `cache_control`，最多允许 4 个 breakpoint。适合需要以不同频率缓存不同段落的场景：

```json
{
  "system": [
    { "type": "text", "text": "...", "cache_control": { "type": "ephemeral" } }
  ],
  "messages": [
    { "role": "user", "content": [
      { "type": "text", "text": "...", "cache_control": { "type": "ephemeral" } }
    ]}
  ]
}
```

两种方式可以混合使用；混用时 automatic cache breakpoint 占用一个 breakpoint slot（上限共 4 个）。

### 1.3 TTL 选项

| TTL | 价格倍数 | 使用场景 |
|---|---|---|
| 5 分钟（默认） | 1.25× base input | 高频请求（> 每 5 分钟一次），每次命中免费刷新 |
| 1 小时 | 2× base input | 低频但 latency 敏感；长时间 agentic 任务 |

指定 1 小时 TTL：`{ "type": "ephemeral", "ttl": "1h" }`

混用不同 TTL 时，TTL 长的 breakpoint 必须在 TTL 短的之前。

### 1.4 最小 token 门槛

不满足门槛的请求不报错，但静默不缓存（`cache_creation_input_tokens` 和 `cache_read_input_tokens` 均为 0）：

| 模型 | 最小缓存 tokens |
|---|---|
| Claude Opus 4.7 / 4.6 / 4.5 | 4096 |
| Claude Sonnet 4.6 | 2048 |
| Claude Sonnet 4.5 / Opus 4.1 / Opus 4 / Sonnet 4 / Sonnet 3.7 | 1024 |
| Claude Haiku 4.5 | 4096 |
| Claude Haiku 3.5 | 2048 |

### 1.5 定价结构

| 操作 | 倍数（相对 base input） |
|---|---|
| 5 分钟 cache write | 1.25× |
| 1 小时 cache write | 2× |
| Cache read（命中） | 0.1× |

即缓存命中时成本降至 base input 的 **10%**（节省 90%）。倍数与 Batch API（50% 折扣）和 data residency（1.1× US）叠加。

### 1.6 监控缓存效果

Response 的 `usage` 字段包含：
- `cache_creation_input_tokens`：本次写入 cache 的 tokens 数
- `cache_read_input_tokens`：本次从 cache 读取的 tokens 数
- `input_tokens`：最后一个 breakpoint 之后（未缓存）的 tokens 数

总 input tokens = `cache_read_input_tokens` + `cache_creation_input_tokens` + `input_tokens`

### 1.7 缓存失效触发条件

| 变化类型 | 影响范围 |
|---|---|
| 修改 tool definitions | 全部缓存失效（tools + system + messages） |
| 开关 web search / citations / fast mode | system + messages 缓存失效 |
| 修改 tool_choice / 图片 / extended thinking 参数 | 仅 messages 缓存失效 |
| 内容任意改动 | 该 block 及其后的所有缓存失效 |

---

## 二、OpenAI Prompt Caching

### 2.1 工作原理

OpenAI 自动将 API 请求路由到最近处理过相同 prefix 的服务器，**无需代码改动**：

- 最小缓存长度：**1024 tokens**
- 系统基于 prefix 的 hash（约前 256 tokens）路由请求
- 可通过 `prompt_cache_key` 参数影响路由，提高命中率

### 2.2 Cache 保留策略

| 策略 | 适用模型 | 保留时长 |
|---|---|---|
| In-memory（默认） | gpt-4o 及更新模型（不含 gpt-5.5 系列） | 5-10 分钟不活动；最长 1 小时 |
| Extended（24h） | gpt-5.5, gpt-5.5-pro, gpt-5.4, gpt-5.2, gpt-5.1-\*, gpt-5, gpt-4.1 | 最长 24 小时 |

通过 `prompt_cache_retention` 参数配置：`"in_memory"` 或 `"24h"`（gpt-5.5 默认为 24h，不支持 in_memory）。

### 2.3 效果

- Latency：降低最多 **80%**
- Input token 成本：降低最多 **90%**（无额外费用，自动发生）

### 2.4 监控

Response `usage` 中：

```json
"usage": {
  "prompt_tokens": 2006,
  "prompt_tokens_details": { "cached_tokens": 1920 }
}
```

### 2.5 可缓存内容

Messages（system/user/assistant 交互）、图片（`detail` 参数必须一致）、Tool use（messages + 可用工具列表）、Structured outputs schema。

### 2.6 注意事项

- 缓存不跨 organization 共享
- 不能手动清除缓存（由系统自动 evict）
- 不影响输出生成（response 始终完整计算）
- 已缓存的 tokens 仍计入 TPM rate limits

---

## 三、Gemini Context Caching

### 3.1 两种机制

**Implicit Caching（隐式，Gemini 2.5+ 自动开启）**

无需开发者操作，Google 在 cache 命中时自动返回折扣。不保证命中。通过 response 的 `usage_metadata.cached_token_count` 观察。

最小 token 门槛：

| 模型 | 最小 tokens |
|---|---|
| Gemini 3 Flash preview | 1024 |
| Gemini 3 Pro preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

**Explicit Caching（显式，手动创建）**

先将内容上传并创建 cache，再在后续请求中引用 cache name。**保证**命中时节省成本。

```python
from google.genai import types

cache = client.caches.create(
    model="models/gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        display_name="my cache",
        system_instruction="...",
        contents=[document],
        ttl="300s",  # 默认 1 小时
    )
)

response = client.models.generate_content(
    model=model,
    contents="...",
    config=types.GenerateContentConfig(cached_content=cache.name)
)
```

### 3.2 存储成本

- 按每 1M tokens 每小时计费（$1.00–$4.50/1M tokens/hour，依模型而定）
- TTL 到期后自动删除，无法修改已有 cache（需重建）
- 免费层不支持（需付费账户）

---

## 四、跨平台横向对比

| 维度 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **触发机制** | 手动（`cache_control` 标记） | 自动（无需代码改动） | 双模式：隐式自动 / 显式创建 |
| **最小 tokens** | 1024–4096（依模型） | 1024 | 1024–4096（依模型） |
| **TTL** | 5 分钟（默认）/ 1 小时（付费） | 5–10 分钟 in-memory；gpt-5.x 最长 24 小时 | 可设置，默认 1 小时 |
| **成本折扣** | Cache read = 0.1× base（节省 90%）；Cache write = 1.25× base | 最多 90% 节省，无额外费用 | 缓存读取折扣（具体比例见 pricing 页）；另需支付存储费用 |
| **API 交互面** | `cache_control` block-level 标记；or 顶层 `cache_control` | 完全自动，无需额外字段 | `caches.create()` + `cached_content=cache.name` |
| **监控字段** | `cache_creation_input_tokens` / `cache_read_input_tokens` | `usage.prompt_tokens_details.cached_tokens` | `usage_metadata.cached_token_count` |
| **cache 共享范围** | Workspace 级别（2026-02-05 起；此前为 org 级） | Organization 级别 | not documented in current raw |
| **内容类型** | 文本、图片、工具定义、文档 | 文本、图片、工具定义、Structured outputs schema | 文本、图片、视频文件、PDF、系统指令 |

---

## 五、各平台最省钱的场景

### Claude

- **长文档 + 多轮问答**：文档作为 system 或早期 user block，命中率极高
- **稳定 system prompt + 高并发**：5 分钟内命中率高，每次命中 0.1× 成本
- **few-shot 例子超过 20 条**：例子不变，每个用户 query 进来都命中
- **Agentic 多步任务**：工具定义 + context 固定，每个 tool call step 复用 cache

### OpenAI

- **相同 system prompt 重复使用**：静态 system prompt 天然命中，无需任何改动
- **Batch 处理共享 prefix**：同一批请求 system + few-shots 完全相同
- **gpt-5.x 长会话**：24h cache retention，隔天对话仍能命中

### Gemini

- **视频 / 大文档分析**：Explicit caching 特别适合视频（几千 tokens），按小时存储比每次传输便宜得多
- **系统指令密集的服务**：创建一个 cache 后反复引用，只需支付存储费用

---

## 六、常见 Pattern

### 6.1 System Prompt Caching

最基础的 pattern。将不变的 system prompt 放最前面并标记 cache。

Claude 建议：system prompt + 各种 tool definitions → 用 explicit breakpoint 缓存；对话历史 → 用 automatic caching。

### 6.2 Few-Shot Example Caching

将大量（20+）few-shot 例子放在 system 或早期 messages 中缓存。每个 user query 进来时这些例子都已在 cache 中，大幅降低重复例子的成本。

### 6.3 长文档 / RAG 文档 Caching

将大文档（长篇报告、代码库、书籍）作为 context 一次性写入 cache，后续所有 query 复用。Gemini 的 Explicit caching 尤其适合这类场景（视频、PDF）。

### 6.4 Cache Pre-warming（仅 Claude）

通过 `max_tokens: 0` 请求触发 cache 写入而不生成输出，预热 cache。**注意**：不支持在 Batch API 内 pre-warm（因为 Batch 执行时 cache 可能已过期）。

---

## 七、常见坑（Gotchas）

1. **Cache breakpoint 放在变化的内容上**（Claude）：最典型的错误。Breakpoint 应放在最后一个跨请求不变的 block，不能放在含 timestamp 或 per-request context 的 block 上。Cache write 只发生在 breakpoint 位置，lookback 不会自动找到 breakpoint 之前的稳定内容。

2. **Lookback 窗口只有 20 个 block**（Claude explicit 模式）：对话增长超过 20 轮后，早期 cache write 可能落在窗口之外。需要提前设置第二个 breakpoint。

3. **JSON key 顺序不固定**（Claude）：Swift、Go 等语言在 JSON 序列化时 key 顺序随机，导致 `tool_use` block 的 hash 每次不同，缓存永远失效。需确保 tool_use block key 顺序稳定。

4. **tool_choice 变化让 messages cache 失效**（Claude）：修改 `tool_choice` 参数会导致 messages 级缓存失效。

5. **图片必须完全一致才能命中**（Claude + OpenAI）：图片 URL 相同不够，内容必须相同；Claude 还要求 `detail` 参数一致，OpenAI 同样要求。

6. **OpenAI 缓存不可手动清除**：依赖自动 evict，5-10 分钟不活动后过期。无法强制刷新。

7. **Gemini 修改已缓存内容需重建**：Explicit cache 一旦创建不可修改，更新内容必须删除旧 cache 并重建。

8. **Claude cache 从 2026-02-05 起改为 workspace 级隔离**：此前是 org 级，变更后多 workspace 的 org 需检查 caching 策略。

9. **Cache write 成本高于普通 input**（Claude）：5 分钟 cache write = 1.25× base；1 小时 cache write = 2× base。第一次写入反而贵，只有后续命中才节省。

10. **OpenAI `prompt_cache_key` 会影响路由**：同一 key + prefix 组合超过 ~15 req/min 会导致 cache overflow，降低命中率。

---

## 出现来源

- `01_Raw/platform.claude.com/docs/en/build-with-claude/prompt-caching.md` — Claude 官方 prompt caching 文档（automatic/explicit 两种模式、TTL、定价、最小 token、缓存失效条件、lookback 机制）
- `01_Raw/docs.openai.com/docs/guides/prompt-caching.md` — OpenAI 官方 prompt caching 文档（自动机制、in-memory vs 24h 保留、监控字段、可缓存内容类型）
- `02_Wiki/Summaries/caching--gemini-docs.md`（source: `01_Raw/ai.google.dev/gemini-api/docs/caching.md`）— Gemini Context Caching（implicit/explicit 双模式、TTL、存储成本、最小 token 门槛）
