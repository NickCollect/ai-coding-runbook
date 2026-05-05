---
name: Context Caching / Prompt Caching 跨厂商对比
type: comparison
created: 2026-05-05
vendors: [Claude, OpenAI, Gemini]
sources:
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/prompt-caching.md
  - 01_Raw/docs.openai.com/docs/guides/prompt-caching.md
  - 01_Raw/ai.google.dev/gemini-api/docs/caching.md
---

# Context Caching / Prompt Caching 跨厂商对比

将相同的 prompt 前缀（长系统提示、文档、工具列表等）缓存起来，避免每次请求都重新处理，是降低 LLM API 成本和延迟的关键手段。三家厂商实现差异显著：Claude 是**显式断点式**，OpenAI 是**全自动透明式**，Gemini 则**两种模式并存**。

---

## 一、各厂商机制详解

### Claude — 显式 cache_control 断点

Claude 的 prompt caching 要求开发者**主动标记**缓存点，通过在内容块上添加 `cache_control: {type: "ephemeral"}` 告知 API 在此处建立缓存前缀。

**两种启用方式：**

1. **Automatic caching（推荐用于多轮对话）**：在请求顶层加一个 `cache_control` 字段，API 自动将断点应用到最后一个可缓存块，并随对话增长自动前移。

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},   # 顶层自动模式
    system="You are an expert document analyst with deep knowledge...",
    messages=[{"role": "user", "content": "Summarize the key points."}]
)
```

2. **Explicit cache breakpoints（精细控制）**：在单个内容块上放 `cache_control`，精确控制哪个位置作为缓存前缀的终点。

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "<entire book content here...>",
            "cache_control": {"type": "ephemeral"}  # 在此处建立断点
        }
    ],
    messages=[{"role": "user", "content": "What is the main theme?"}]
)
```

**缓存顺序**：tools → system → messages，直到含 `cache_control` 的块为止。

**检测缓存命中**：响应 `usage` 字段：
- `cache_creation_input_tokens`：本次写入缓存的 token 数
- `cache_read_input_tokens`：本次从缓存读取的 token 数

---

### OpenAI — 全自动透明缓存

OpenAI 的 prompt caching **无需任何代码改动**，API 自动检测重复前缀并路由到曾处理过相同前缀的服务器。

- 系统通过 prompt 前缀的哈希进行路由（约前 256 tokens 参与计算）。
- 缓存激活的最低 prompt 长度：**1024 tokens**。
- 缓存不跨组织共享。

**可选优化**：通过 `prompt_cache_key` 参数影响路由，提升长公共前缀的命中率：

```python
# 每个 unique prefix + key 组合建议 < 15 req/min 避免 cache overflow
response = client.responses.create(
    model="gpt-5",
    input=[...],
    prompt_cache_key="my-system-prompt-v2"
)
```

**检测缓存命中**：响应 `usage` 字段：

```json
"usage": {
  "prompt_tokens": 2006,
  "prompt_tokens_details": {"cached_tokens": 1920}
}
```

---

### Gemini — 隐式 + 显式双轨机制

Gemini 同时支持两种机制：

#### 1. Implicit Caching（隐式缓存）

- 自动启用于 **Gemini 2.5 及更新模型**，无需开发者操作。
- 不保证节省（取决于是否命中）；命中时 Google 自动传递节省。
- 检测：查看响应 `usage_metadata.cached_token_count`。

最低 token 门槛（各模型不同）：

| 模型 | 最低 tokens |
|---|---|
| Gemini 3 Flash preview | 1024 |
| Gemini 3 Pro preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

提高命中率的技巧：将大型重复内容放在 prompt **开头**；在短时间内发送前缀相似的请求。

#### 2. Explicit Caching（显式缓存）

需要先通过 API **创建缓存对象**，再在请求中引用：

```python
# 步骤 1：创建缓存
cache = client.caches.create(
    model="models/gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        display_name="my_long_document",
        system_instruction="You are an expert document analyst...",
        contents=[document_file],   # 支持视频、PDF、文本等
        ttl="300s",                 # 默认 1 小时
    )
)

# 步骤 2：使用缓存
response = client.models.generate_content(
    model="models/gemini-3-flash-preview",
    contents="What are the key findings?",
    config=types.GenerateContentConfig(cached_content=cache.name)
)
print(response.usage_metadata)
```

**缓存管理操作**：
- `client.caches.list()`：列出所有缓存（返回元数据，不返回内容）
- `client.caches.update(name, config=UpdateCachedContentConfig(ttl='600s'))`：仅可更新 TTL 或 expire_time
- `client.caches.delete(name)`：手动删除

---

## 二、决策矩阵（汇总对比）

| 维度 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **启用方式** | 显式标记（`cache_control`） | 全自动，无需配置 | 隐式（自动）+ 显式（API） |
| **最低 token 门槛** | 1024 | 1024 | 1024（Flash）/ 4096（Pro） |
| **TTL 默认** | 5 分钟 | 5–10 分钟（内存）/ 24h（extended） | 1 小时（explicit）/ 不保证（implicit） |
| **TTL 可配置** | ✅ 可选 1 小时（更高写入价） | ✅ 可选 24h（`prompt_cache_retention: "24h"`） | ✅ 任意设置（explicit 模式） |
| **TTL 刷新** | 每次缓存命中时免费刷新 | 不活跃计时，命中则重置 | 需手动调用 update（explicit） |
| **缓存写入额外成本** | ✅ 有（5m: 1.25× base；1h: 2× base） | ❌ 无额外写入费 | ✅ 有（按 token × 小时计费，$1–$4.50/1M token/h） |
| **缓存读取折扣** | 90% off（0.1× base input 价） | 90% off（0.1× 正常输入价） | 低于标准输入价（具体见定价页） |
| **延迟降低** | 不在文档中量化 | 最高 80% 延迟降低 | 不在 reviewed source 量化 |
| **可监控字段** | `cache_creation_input_tokens` / `cache_read_input_tokens` | `usage.prompt_tokens_details.cached_tokens` | `usage_metadata.cached_token_count` |
| **ZDR（零数据保留）兼容** | ✅ 兼容（仅保存 KV cache 表示和加密哈希） | ✅ 内存策略兼容（extended 模式存 KV tensor） | not documented in source |
| **跨组织共享** | ❌ 不共享 | ❌ 不共享 | not documented in source |
| **可缓存内容类型** | tools、system、messages（含图片） | messages、图片、tool 定义、structured outputs schema | 视频、PDF、文本、系统提示 |
| **手动清除缓存** | ❌ 不支持（到期自动清除） | ❌ 不支持（自动清除） | ✅ 支持（`caches.delete()`） |

---

## 三、各厂商代码示例

### Claude — 显式断点（大型文档场景）

```python
import anthropic

client = anthropic.Anthropic()

# 假设有一份长文档需要多次查询
with open("large_document.txt") as f:
    document_text = f.read()

# 首次请求：建立缓存（会有 cache_creation_input_tokens）
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": document_text,
            "cache_control": {"type": "ephemeral"}  # 在文档后设置断点
        }
    ],
    messages=[{"role": "user", "content": "What is the main topic?"}]
)
print(f"Cache created: {response.usage.cache_creation_input_tokens} tokens")

# 后续请求：读取缓存（会有 cache_read_input_tokens，成本仅 10%）
response2 = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": document_text,
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": "List the key conclusions."}]
)
print(f"Cache hit: {response2.usage.cache_read_input_tokens} tokens read from cache")
```

### OpenAI — 无需配置（将静态内容前置即可）

```python
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """You are an expert document analyst with deep knowledge...
[很长的系统提示或文档内容放这里，1024+ tokens]
"""

# 直接发请求，OpenAI 自动缓存前缀
response = client.responses.create(
    model="gpt-5",
    input=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "What is the main topic?"}
    ]
)

# 查看是否命中缓存
cached = response.usage.prompt_tokens_details.get("cached_tokens", 0)
print(f"Cached tokens: {cached}")

# 后续请求保持 SYSTEM_PROMPT 不变 → 自动命中缓存
response2 = client.responses.create(
    model="gpt-5",
    input=[
        {"role": "system", "content": SYSTEM_PROMPT},  # 完全相同的前缀
        {"role": "user", "content": "List the key conclusions."}
    ]
)
```

### Gemini — 显式缓存 API

```python
from google import genai
from google.genai import types

client = genai.Client()

# 步骤 1：上传文件并创建缓存（付存储费）
document = client.files.upload(file="large_document.pdf",
                               config=dict(mime_type="application/pdf"))

cache = client.caches.create(
    model="models/gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        display_name="my_document_cache",
        system_instruction="You are an expert document analyst.",
        contents=[document],
        ttl="3600s",  # 默认 1 小时
    )
)
print(f"Cache created: {cache.name}")

# 步骤 2：复用缓存发送多个问题
questions = ["What is the main topic?", "List the key conclusions.", "Who are the authors?"]
for q in questions:
    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=q,
        config=types.GenerateContentConfig(cached_content=cache.name)
    )
    print(f"Q: {q}")
    print(f"Cached tokens: {response.usage_metadata.cached_content_token_count}")
    print(f"A: {response.text}\n")

# 步骤 3：用完后手动删除（或等 TTL 到期）
client.caches.delete(cache.name)
```

---

## 四、选型建议

**选 Claude 当：**
- 需要**精确控制**缓存边界（工具、多段 system prompt、部分 messages）；
- 使用多轮对话且希望**自动随对话增长缓存**（automatic mode）；
- 场景是短 TTL（5 分钟内大量重复请求），写入成本可被命中节省覆盖；
- 需要 ZDR 合规且要控制缓存的具体内容范围。

**选 OpenAI 当：**
- 希望**零改造**直接享受缓存收益（系统提示 / 工具定义超过 1024 tokens 即生效）；
- 需要 **24h 长期缓存**（gpt-5.x extended retention）覆盖低频访问场景；
- 批量任务中大量请求共享相同前缀，自动路由效率高。

**选 Gemini 当：**
- 需要缓存**超大上下文**（视频、长 PDF 等文件），Gemini 的 Files API + explicit caching 组合专为此设计；
- 需要**精确管理缓存生命周期**（手动列出、更新 TTL、删除）；
- Gemini 2.5+ 用户可以先试隐式缓存（零成本），再按需升级到显式缓存（付存储费换确定性保证）；
- 每次请求成本极高（大文档 4096+ tokens），显式缓存的存储费换来的每次读取折扣划算。

**通用原则（三家都适用）：**
- 将**静态内容前置**、动态内容后置（user query 放最后）；
- 缓存的 token 越多、重复请求越多，ROI 越高；
- 缓存不影响输出质量，模型对缓存/非缓存 token 一视同仁。
