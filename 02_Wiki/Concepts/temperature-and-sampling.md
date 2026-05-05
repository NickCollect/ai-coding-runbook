---
name: Temperature and Sampling
type: concept
aliases: [Temperature, Sampling Parameters, top_p, top_k, Decoding Strategy]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Temperature 与采样策略

控制 LLM 输出随机性与多样性的解码参数组合。决定模型在每个 token 生成步骤中如何从概率分布中采样。

## 核心机制

模型在每步预测时输出所有 token 的 logit 分数。采样参数在 softmax 之后对这个分布进行变形：

- **Temperature**：对 logit 除以 T 后再做 softmax。T<1 使分布更尖锐（高置信 token 被选中概率更高）；T>1 使分布更平坦（随机性增加）；T=0 等效于贪婪解码（始终选最高概率 token）。
- **top_p（nucleus sampling）**：只从累计概率达到 p 的最小候选集中采样。例如 top_p=0.9 表示仅考虑累计概率前 90% 的 token 子集。
- **top_k**：只从概率最高的 k 个 token 中采样，直接截断尾部长尾。

三者通常组合使用，顺序：先 top_k 截断 → 再 top_p nucleus → 再 temperature 缩放。

## 跨厂商实现

**Claude**：支持 `temperature`（0–1）和 `top_p`、`top_k`；官方建议只调其中一个，不要同时修改多个。

**OpenAI**：支持 `temperature`（0–2）和 `top_p`；文档明确建议不要同时修改两者。GPT-5 等推理模型固定 temperature=1，不支持修改。

**Gemini**：支持 `temperature`、`topP`、`topK`；建议低 temperature（0.0–0.3）用于事实性输出，高 temperature（0.7–1.0）用于创意输出。

## 关键参数 / API 表面

| 参数 | 范围 | 默认值 | 效果 |
|---|---|---|---|
| `temperature` | 0–1 (Claude/Gemini), 0–2 (OpenAI) | 1.0 | 总体随机性 |
| `top_p` | 0–1 | 1.0 | Nucleus 候选集大小 |
| `top_k` | 正整数 | 无（Claude: 不限） | 候选集 token 数上限 |

## 使用场景

**低 temperature（0–0.3）**：代码生成、数据提取、分类、问答——需要确定性和一致性。

**中 temperature（0.5–0.7）**：通用对话、摘要——平衡准确与流畅。

**高 temperature（0.8–1.0）**：创意写作、头脑风暴、多样性生成——需要随机性。

**不修改**：推理模型（OpenAI o 系列、Claude 扩展思考模式）——内部已有推理过程，temperature 固定或影响有限。

## 相关

- [[prompt-engineering]] — 采样参数是 prompt 调优的一部分
- [[extended-thinking-concept]] — 推理模型的温度行为特殊
- [[Context-window]] — 采样不影响 context，但影响输出分布

## 出现来源

- [[prompting-strategies--gemini-docs]]
- [[prompt-engineering--openai-docs]]
