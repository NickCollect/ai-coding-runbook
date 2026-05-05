---
name: Gemini Context Caching
type: entity
vendor: Gemini
aliases: ["Context Caching", "explicit caching", "implicit caching", "cached_content", "client.caches"]
created: 2026-05-05
---

# Gemini Context Caching

Gemini API 的 token 缓存机制，分为「隐式缓存」（自动，Gemini 2.5+ 默认启用）和「显式缓存」（手动创建，保证命中时降低成本）；缓存内容按 token 存储量计时计费。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| 隐式缓存 | Gemini 2.5+ 自动启用，无需开发者操作 |
| 显式缓存创建 | `client.caches.create()` |
| 默认 TTL | **1 小时**（可配置） |
| 存储成本 | $1.00–$4.50 / 1M tokens / 小时（按模型差异） |
| 可用层级 | 显式缓存需付费层（免费层大部分模型不可用） |

## 核心功能

### 两种缓存机制对比

| 类型 | 启用方式 | 保证节省 | 控制粒度 |
|---|---|---|---|
| **隐式缓存** | 自动（Gemini 2.5+ 默认） | 不保证（依赖命中） | 无法控制，Google 自动优化 |
| **显式缓存** | 手动 `caches.create()` | ✅ 命中时保证节省 | 完全控制 TTL 和内容 |

### 隐式缓存最低 token 阈值

| 模型 | 最低 token 数 |
|---|---|
| Gemini 3 Flash preview | 1024 |
| Gemini 3 Pro preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

**最大化隐式缓存命中率**：将大型重复内容放在 prompt **开头**；在短时间窗口内发送前缀相似的请求。

### 显式缓存支持内容类型

- 视频文件（通过 Files API 上传）
- PDF 和文档
- 文本文件
- System instructions
- 任何需要重复发送的内容

### 缓存注意事项

- 已缓存内容**不可修改**；更新内容需创建新缓存
- `caches.create()` 返回 cache name，后续请求通过 `cached_content` 引用
- TTL 到期后缓存自动删除

## API 示例

```python
from google.genai import types

# 创建显式缓存
cache = client.caches.create(
    model="models/gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        display_name="my video cache",
        system_instruction="You are an expert video analyzer...",
        contents=[video_file],  # 视频 / 文档 / 文本
        ttl="300s",             # TTL，默认 1 小时
    )
)

# 使用缓存
response = client.models.generate_content(
    model="models/gemini-3-flash-preview",
    contents="Describe the characters.",
    config=types.GenerateContentConfig(cached_content=cache.name)
)

# 检查命中（隐式缓存）
print(response.usage_metadata.cached_token_count)
```

## 与 Claude 对应物

[[Prompt-caching]] — Anthropic 的 prompt caching，机制类似：重复内容只需计算一次，后续请求以折扣价计费；Claude 通过 `cache_control: {"type": "ephemeral"}` 标记缓存断点，默认 TTL 5 分钟。

## 出现来源

- [[caching--gemini-docs]]

## 相关

- [[Gemini-API]] — 通过 `GenerateContentConfig.cached_content` 参数使用
- [[Gemini-Files-API]] — 缓存视频/文档等大文件时先上传到 Files API
- [[Prompt-caching]] — Claude 对应物
