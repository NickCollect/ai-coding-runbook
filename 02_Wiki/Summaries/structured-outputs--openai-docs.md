---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/structured-outputs.md
source_url: https://platform.openai.com/docs/guides/structured-outputs
title: "OpenAI — Structured Outputs"
summarized_at: 2026-05-05
entities_referenced: [Structured-outputs]
concepts_referenced: []
---

## 核心要点

Structured Outputs 确保模型响应严格遵循提供的 JSON Schema，提供可靠的类型安全输出。

### 核心优势

- **类型安全**：模型输出保证符合 schema，消除解析错误和类型不匹配
- **明确拒绝**：当内容违反 policy 时，模型通过 `refusal` 字段明确拒绝而非生成不合规内容
- **更简单的 prompt**：无需在 prompt 中反复说明格式要求

### 支持模型

`gpt-4o`、`gpt-4o-mini` 及以上，以及 `gpt-5.4`、`gpt-5.5` 等所有前沿模型。

### 两种使用场景

**场景一：Function Calling（`strict: true`）**

在工具定义中设置 `"strict": true`，schema 中的 required 字段全部必填，不允许 `additionalProperties: true`。

**场景二：`json_schema` 响应格式**

```python
text={
    "format": {
        "type": "json_schema",
        "strict": True,
        "schema": { ... }
    }
}
```

### 与旧版 JSON mode 对比

| 特性 | JSON mode | Structured Outputs |
|---|---|---|
| 保证合法 JSON | ✅ | ✅ |
| 保证符合 schema | ❌ | ✅ |
| 明确拒绝 | ❌ | ✅ |
| 模型支持 | 旧/新均支持 | GPT-4o+ |

### 最佳实践

- `strict: true` 时 schema 中所有字段设为 `required`
- 禁用 `additionalProperties`
- 用 `enum` 枚举固定选项，而非 free-form string
- 首次传入新 schema 时有轻微延迟（schema 编译），后续缓存
