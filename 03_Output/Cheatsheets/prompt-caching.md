---
type: cheatsheet
topic: prompt-caching
updated: 2026-05-05
---

# Prompt Caching Quick Reference

---

## 三厂商对比

| 维度 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **机制** | 显式断点（`cache_control`） | 全自动，无需改代码 | 隐式自动 + 显式 API |
| **最小 tokens** | 1024–4096（依模型） | 1024 | 1024–4096（依模型） |
| **TTL 默认** | 5 分钟 | 5–10 min in-memory；gpt-5.x 24h | 1 小时（explicit） |
| **TTL 可配置** | ✅ 可选 1 小时 | ✅ 可选 24h | ✅ 任意值（explicit） |
| **Cache 写入额外费** | ✅ 5m=1.25×, 1h=2× | ❌ 无 | ✅ 按 token×小时计费 |
| **Cache 读取折扣** | **90% off**（0.1× base） | **90% off**（0.1× base） | 低于标准价（具体见定价页） |
| **延迟降低** | 不量化 | 最高 80% | 不量化 |
| **手动清除** | ❌ | ❌ | ✅ `caches.delete()` |
| **监控字段** | `cache_creation_input_tokens` / `cache_read_input_tokens` | `usage.prompt_tokens_details.cached_tokens` | `usage_metadata.cached_token_count` |

---

## Claude — cache_control 用法

### 方式 A：顶层 automatic（推荐多轮对话）

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},   # 顶层自动，随对话前移
    system="You are an expert...",
    messages=[{"role": "user", "content": "..."}]
)
```

### 方式 B：Explicit breakpoint（精细控制，最多 4 个）

```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": "<long document or system prompt>",
        "cache_control": {"type": "ephemeral"}  # 在此建立断点
    }],
    messages=[{"role": "user", "content": "Summarize."}]
)
# 检查命中
print(response.usage.cache_read_input_tokens)    # > 0 = cache hit
print(response.usage.cache_creation_input_tokens) # > 0 = cache write
```

**1 小时 TTL**：`{"type": "ephemeral", "ttl": "1h"}` — 写入成本 2× base，适合低频长任务。

**最小 token 门槛**：

| Model | Min tokens |
|---|---|
| Opus 4.7 / 4.6 / 4.5, Haiku 4.5 | 4096 |
| Sonnet 4.6 | 2048 |
| Sonnet 4.5 / Opus 4.1 / Sonnet 3.7 | 1024 |
| Haiku 3.5 | 2048 |

---

## OpenAI — 全自动，无需代码

系统自动检测重复前缀，静态内容前置即生效：

```python
# 无需任何额外参数，直接发请求
response = client.responses.create(
    model="gpt-5.4",
    input=[
        {"role": "system", "content": LONG_SYSTEM_PROMPT},  # 1024+ tokens，自动缓存
        {"role": "user", "content": "Question?"}
    ]
)
cached = response.usage.prompt_tokens_details.get("cached_tokens", 0)
```

- **gpt-5.x 24h 缓存**：加 `prompt_cache_retention="24h"` 参数（默认即 24h for gpt-5.5）
- **提高命中率**：加 `prompt_cache_key="my-key"` 影响路由；同 key+prefix 建议 < 15 req/min

---

## Gemini — Explicit Caching（视频 / 大文档场景）

```python
from google.genai import types

# 步骤 1：创建缓存（付存储费 $1–$4.50/1M tokens/h）
cache = client.caches.create(
    model="models/gemini-2.5-flash",
    config=types.CreateCachedContentConfig(
        system_instruction="You are an expert analyst.",
        contents=[document],  # 支持 PDF、视频、文本
        ttl="3600s",
    )
)

# 步骤 2：每次请求引用缓存
response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="What are the key findings?",
    config=types.GenerateContentConfig(cached_content=cache.name)
)
print(response.usage_metadata.cached_content_token_count)

# 步骤 3：用完删除
client.caches.delete(cache.name)
```

**Implicit caching（Gemini 2.5+ 自动）**：无需代码，命中时 Google 自动给折扣。将大型重复内容放 prompt **开头**提高命中率。

---

## Top 5 Gotchas

1. **Claude：breakpoint 放在变化内容上**
   断点必须在最后一个跨请求不变的 block，不能放含 timestamp / per-request context 的块上。

2. **Claude：lookback 窗口只有 20 个 block**（explicit 模式）
   对话超过 20 轮后早期 breakpoint 落窗外。提前设第二个 breakpoint。

3. **Claude：JSON key 顺序不稳定导致 tool_use block 缓存永远 miss**
   Swift/Go 等语言序列化 key 顺序随机 → hash 每次不同。需固定 key 顺序。

4. **Claude cache 2026-02-05 起改为 workspace 级隔离**（原为 org 级）
   多 workspace 的 org 需重新评估 caching 策略。

5. **Gemini Explicit cache 不可修改**
   更新内容必须删除旧 cache 重建（只能 update TTL）。
   OpenAI 缓存同样不可手动清除，依赖自动 evict。

---

## 场景速查

| 场景 | 推荐 |
|---|---|
| 多轮对话 + 稳定 system prompt | Claude automatic caching |
| 零改动即享缓存 | OpenAI（静态内容 > 1024 tokens 自动生效） |
| 视频 / 大 PDF 多次查询 | Gemini explicit caching |
| 24h 低频访问仍命中 | OpenAI gpt-5.x extended retention |
| 20+ few-shot 例子固定不变 | 三家均可；Claude explicit breakpoint 最省 |
