---
name: Prompt Engineering
type: concept
aliases: [Prompt Design, Prompt Writing, Prompting]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Prompt Engineering（提示词工程）

通过精心设计输入文本来引导 LLM 产生准确、可控输出的技术体系。是在无需修改模型权重的前提下影响模型行为的主要手段。

## 核心机制

模型根据输入上下文预测最可能的 continuation。Prompt Engineering 通过结构化输入——角色设定、指令清晰度、示例（few-shot）、格式约束——调整模型对"期望输出"的概率估计。

主要技术：
- **角色/人格设定**：通过 system prompt 指定模型扮演的角色和行为边界
- **清晰的指令**：明确指定输出格式、长度、语气、受众
- **Few-shot 示例**：在 messages 中提供 user/assistant 轮次展示期望模式
- **格式标记**：用 XML 标签、Markdown 分隔多部分内容（文档、代码、指令）
- **RAG 注入**：将外部检索内容放入 prompt，减少幻觉

## 跨厂商实现

**Claude**：system prompt + user/assistant 多轮；强调 XML 标签分隔 context；Constitutional AI 影响拒绝行为。

**OpenAI**：`developer` 角色（高优先级持久指令）+ `user` + `assistant`；支持 Reusable Prompts（Dashboard 模板化）；GPT-5 建议对话风格优于格式化指令。

**Gemini**：system instructions + prompt；提供低温输出（确定性）和高温输出（创造性）的明确建议；强调 agentic 场景中明确规划指令。

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `system` / `instructions` | 持久性系统指令 |
| `messages` | 对话历史（含 few-shot 示例） |
| `temperature` | 随机性控制（见 [[temperature-and-sampling]]） |
| `max_tokens` | 限制输出长度 |

## 使用场景

**用**：快速迭代调整行为、格式控制、领域引导、成本为零的行为修改。

**不用**（考虑 fine-tuning）：大量示例超出 context window 上限、需要稳定内化专有知识格式、延迟/成本要求极高的生产路径。

## 相关

- [[few-shot-learning]] — prompt 中嵌入示例的具体技术
- [[chain-of-thought]] — 引导逐步推理的提示技术
- [[system-prompt]] — 系统指令的角色与优先级
- [[context-engineering]] — 管理进入 context window 的信息
- [[prompt-injection]] — 针对 prompt 的安全攻击向量

## 出现来源

- [[prompt-engineering--openai-docs]]
- [[prompting-strategies--gemini-docs]]
- [[README--prompt-eng-tutorial]]
