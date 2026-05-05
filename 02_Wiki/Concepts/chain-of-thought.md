---
name: Chain of Thought
type: concept
aliases: [CoT, Chain-of-Thought Prompting, Step-by-step Reasoning, Reasoning Trace]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Chain of Thought（思维链）

通过提示或训练让模型在给出最终答案前，先逐步输出中间推理过程的技术。CoT 能显著提升模型在数学、逻辑、多步骤推理任务上的表现。

## 核心机制

**标准 CoT Prompting**：在 prompt 中加入"Let's think step by step"（零样本 CoT）或提供包含推理步骤的 few-shot 示例（CoT Few-shot），引导模型显式输出推理链，再给出最终答案。

**Few-shot CoT 示例**：
```
Q: 一个停车场有 3 行，每行 10 辆车。停车场有多少辆车？
A: 我们需要找出停车场的总车数。有 3 行，每行 10 辆车。3 × 10 = 30。答案是 30 辆。

Q: [新问题]
A: [模型逐步推理]
```

**为什么有效**：
- 分解复杂问题为子步骤，降低每一步的认知负荷
- 中间步骤提供上下文，帮助模型在后续步骤中保持一致
- 允许外部验证推理过程（可发现推理错误）

**忠实性问题**：Anthropic 研究（2023）发现，CoT 是否反映模型真实内部推理存疑——模型可能先"知道答案"再构造合理化推理（post-hoc rationalization）。更大的模型在多数任务中产生更不忠实的 CoT。

## 跨厂商实现

**Claude**：
- 标准 CoT 通过 prompt 触发
- **Extended Thinking**：Claude 的原生 CoT——模型在生成 `thinking` 内容块（内部推理，不计入普通输出）后再给出 `text` 答案；Opus 4.7+ 通过 adaptive thinking 自动决定是否开启
- 注意：推理模型的 thinking 内容不应被 prompt 引导（Claude 官方建议避免干预 thinking 过程）

**OpenAI**：
- o 系列（o3、o4-mini 等）为原生推理模型，内部 CoT 不暴露给用户（token 消耗在后台）
- GPT-5 是对话模型，支持 few-shot CoT prompt；但文档建议**不要在推理模型上使用 CoT prompt**（模型已内部推理，额外 CoT prompt 反而干扰）

**Gemini**：通过 prompt 支持标准 CoT；Gemini 2.0 Flash Thinking Experimental 等推理模型内置 CoT。

## 关键参数 / API 表面

| 场景 | 做法 |
|---|---|
| 标准模型触发 CoT | 在 prompt 中加"step by step"或提供 CoT few-shot 示例 |
| Claude 推理模型 | `thinking: {type: "enabled"}` 或 adaptive 模式 |
| OpenAI 推理模型 | 设置 `reasoning.effort`（low/medium/high），不用 CoT prompt |
| 控制推理深度 | Claude: `budget_tokens`；OpenAI: `reasoning.effort` |

## 使用场景

**适用**：数学题、逻辑推理、代码 debug、多步骤规划、需要可解释推理过程的场景。

**不适用**：
- 简单事实查询（CoT 增加延迟/成本但无益）
- 已使用推理模型（原生 CoT 已内置，不需要 prompt 层面的 CoT）
- 流式输出对延迟极度敏感（CoT 显著增加 TTFT）

## 相关

- [[extended-thinking-concept]] — Claude 的原生推理模式，CoT 的深度实现
- [[few-shot-learning]] — CoT Few-shot 结合两者
- [[prompt-engineering]] — CoT 是高级 prompt 技术之一
- [[Extended-thinking]] — Claude CoT 的 entity 档案

## 出现来源

- [[measuring-faithfulness-in-chain-of-thought-reasoning--anthropic-research]]
- [[extended-thinking--bwc]]
- [[prompt-engineering--openai-docs]]
