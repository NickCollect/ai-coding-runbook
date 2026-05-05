---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/prompt-engineering.md
source_url: https://platform.openai.com/docs/guides/prompt-engineering
title: "OpenAI — Prompt Engineering"
summarized_at: 2026-05-05
entities_referenced: [Prompt-caching]
concepts_referenced: [Context-window]
---

## 核心要点

高效 prompt 的设计策略，涵盖模型选择、角色使用、格式化、few-shot 学习以及推理模型特定技巧。

### 消息角色

- `developer`：高优先级、持久指令（由应用开发者定义，类似旧版 system prompt）
- `user`：终端用户输入，优先级低于 developer
- `assistant`：模型生成内容，也可用于 few-shot 示例

### Reusable Prompts

通过 Dashboard → Prompts 创建含变量的模板，API 中引用：

```python
response = client.responses.create(
    model="gpt-5",
    prompt={"id": "pmpt_abc123", "version": "2", "variables": {"name": "Alice"}},
    input="...",
)
```

### 格式化技巧

- **Markdown**：帮助模型组织结构；但纯 API 调用若不渲染 Markdown 则无需强制使用
- **XML 标签**：清晰分隔多部分内容（文档、代码、指令）
- **Few-shot examples**：在 messages 中提供输入/输出示例（`user`+`assistant` 轮次），引导输出格式

### 提供外部 context（RAG）

将相关文档、用户档案等内容直接放入 prompt，减少幻觉。

### GPT-5 特定最佳实践

- 对话风格优于格式化指令；简洁清晰优于冗长约束
- 推理模型用 `reasoning.effort` 参数（见示例）

```python
response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "low"},
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)
```

### 推理模型提示技巧

- 比标准模型更擅长遵循复杂指令
- 避免 chain-of-thought 提示（模型已内部推理）
- `o1`、`o3` 等旧推理模型不支持 `developer` 角色，改用 `user` 传指令
