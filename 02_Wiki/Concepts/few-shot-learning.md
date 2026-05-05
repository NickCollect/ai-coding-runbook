---
name: Few-shot Learning
type: concept
aliases: [Few-shot Prompting, In-context Learning, ICL, One-shot Learning, Zero-shot]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Few-shot Learning（少样本学习）

在 prompt 中提供少量输入/输出示例（通常 1–10 个），让模型从这些示例中推断期望的输出模式，无需修改权重的 in-context 学习技术。

## 核心机制

LLM 通过预训练获得了从上下文中识别模式的能力（in-context learning）。Few-shot 利用这个能力：

```
示例 1：[input] → [desired output]
示例 2：[input] → [desired output]
...
当前任务：[new input] → ?
```

**变体**：
- **Zero-shot**：无示例，只有任务描述
- **One-shot**：1 个示例
- **Few-shot**：2–10 个示例（超过 10 通常称为 many-shot）
- **Many-shot / Full-context ICL**：数十到数百个示例（长 context 模型支持）

**示例选择原则**：
- 多样性：覆盖输入空间的不同子集
- 相关性：与当前任务接近的示例效果更好（Dynamic few-shot）
- 格式一致性：所有示例保持相同结构
- 标签均衡：分类任务中各类别示例数量均衡

**示例顺序**：末尾示例（最接近当前任务）影响最大；有时随机打乱顺序可减少偏差。

## 跨厂商实现

**Claude / OpenAI / Gemini**：实现方式统一——在 `messages` 数组中交替插入 user/assistant 轮次作为示例，再跟上真实用户 query。

```python
messages = [
    {"role": "user", "content": "输入示例 1"},
    {"role": "assistant", "content": "输出示例 1"},
    {"role": "user", "content": "输入示例 2"},
    {"role": "assistant", "content": "输出示例 2"},
    {"role": "user", "content": "真实任务"}
]
```

**OpenAI** 的 Reusable Prompts 支持模板化 few-shot，通过 `prompt_id` 复用。

**Gemini** 文档明确推荐 1–5 个示例用于自定义输出格式、领域特定任务、一致风格/语气。

## 关键参数 / API 表面

| 要素 | 建议 |
|---|---|
| 示例数量 | 通常 3–5 个；超过 10 个收益递减 |
| 示例质量 | 高质量少量 > 低质量多量 |
| 示例格式 | 与 system prompt 期望格式完全一致 |
| Context 消耗 | 每个示例消耗 token，注意 context window 限制 |

## 使用场景

**适用**：
- 自定义输出格式（JSON 结构、表格、特定标记语言）
- 风格/语气统一（品牌口吻、专业词汇）
- 领域专用任务（医疗编码、法律分析）
- 模型对任务描述理解不足时的补充说明

**不适用（考虑 fine-tuning）**：
- 示例数量超出 context window（>数十个）
- 需要跨会话稳定持久的行为
- 每次携带示例导致不可接受的延迟/成本

## 相关

- [[prompt-engineering]] — few-shot 是 prompt engineering 的核心技术
- [[fine-tuning]] — 示例过多时的替代方案
- [[chain-of-thought]] — few-shot CoT：示例中包含推理步骤
- [[Context-window]] — 示例数量受 context window 限制

## 出现来源

- [[prompt-engineering--openai-docs]]
- [[prompting-strategies--gemini-docs]]
- [[README--prompt-eng-tutorial]]
