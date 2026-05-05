---
name: Context Engineering
type: concept
aliases: [Context Management, Context Window Management, Context Optimization]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Context Engineering（上下文工程）

主动管理进入模型 context window 的信息的艺术与技术——决定放什么、放多少、以什么顺序放，以最大化有限窗口内的信息质量和利用率。

## 核心机制

Context window 是有限资源（通常 128k–1M tokens）。Context Engineering 的核心矛盾：**相关性 vs 完整性**。

主要策略：

**压缩与摘要**
- `/compact`：引导式压缩对话历史（Claude Code）
- 自动对话摘要：长会话中将早期轮次替换为摘要
- 分层摘要：近期详细、远期摘要

**选择性加载**
- RAG：仅加载相关文档片段（而非全量）
- Dynamic few-shot：只选与当前任务最相关的示例
- Skill/工具文档按需加载（非一次性全部注入）

**结构优化**
- 最重要的内容放在开头或结尾（attention sink 效应）
- 使用 XML 标签明确区分不同类型内容（系统指令、文档、对话）
- 避免冗余重复信息占用 token

**缓存利用**
- Prompt caching：稳定的前缀（system prompt、文档）命中缓存，减少重复计算和成本

## 跨厂商实现

**Claude**：
- `/clear`（清空 context）、`/compact`（压缩历史）为 Claude Code 内置工具
- Context Editing API：精细操作 context 内容（修改/删除历史 message）
- Compaction：后台自动 context 压缩（Claude Code 会话管理）
- CLAUDE.md 持久化项目知识（避免每次重新说明）

**OpenAI**：支持 `store: true` 保留对话用于延续；Responses API 自动管理 previous_response_id 链；推理模型支持 Reasoning Summary 避免 thinking tokens 占满 context。

**Gemini**：1M token 超长 context 降低了 context 工程的迫切性；提供 Context Caching API 缓存大型文档（最长 48 小时）。

## 关键参数 / API 表面

| 工具/参数 | 说明 |
|---|---|
| `max_tokens` | 保留输出空间，避免 context 被输入挤满 |
| `cache_control` | Claude prompt caching：标记可缓存的前缀边界 |
| Context Editing API | Claude：手术式修改 message 历史 |
| `/compact` | Claude Code：引导式会话压缩 |

## 使用场景

**需要 context engineering**：长对话（>50 轮）、大型代码库分析、多文档处理、成本敏感的生产应用。

**关键原则**：
- 重要指令不要只放一次在开头（随对话深入可能被"遗忘"）
- Context 满时模型不会报错，而是开始"遗忘"早期内容（滑动窗口行为）
- 越接近生成位置的内容影响力越大

## 相关

- [[Context-window]] — context 的物理边界
- [[Prompt-caching]] — context engineering 的成本优化工具
- [[rag]] — 动态选择 context 内容的主要技术
- [[cost-optimization]] — context 大小直接影响成本

## 出现来源

- [[contextual-retrieval--anthropic-eng]] — Claude 上下文检索工程
- [[costs]] — context 大小与成本关系
- [[Context-window]] — context 物理边界
- [[openai-node-responses-api--github-openai]] — OpenAI store/previous_response_id
- [[openai-python-responses-api--github-openai]] — OpenAI Reasoning Summary
- [[caching--gemini-docs]] — Gemini Context Caching API（48h 缓存）
- [[long-context--gemini-docs]] — Gemini 1M token 超长 context
