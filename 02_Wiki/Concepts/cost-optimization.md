---
name: Cost Optimization
type: concept
aliases: [LLM Cost Reduction, Token Cost Management, API Cost Control]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Cost Optimization（成本优化）

系统性降低 LLM API 使用成本的策略集合，涵盖 token 消耗控制、价格机制利用、模型选择和架构设计四个维度。

## 核心机制

LLM API 成本 = f(input tokens × input price + output tokens × output price)，其中 output 通常比 input 贵 3–5 倍。优化方向：

**1. 减少 Token 消耗**
- 精简 system prompt（<200 行为宜）
- Context 管理：`/clear` 清空无关对话历史；`/compact` 压缩长会话
- 按需加载 RAG（而非全量注入）
- 工具文档延迟加载（tool schemas deferred）
- 避免冗余信息重复

**2. 利用价格折扣机制**
- **Prompt Caching**：Claude 支持缓存命中价格降低 90%（cached input 约 $0.03/MTok vs 标准 $3/MTok）；需要稳定前缀（>1024 tokens）
- **Batch Processing（50% 折扣）**：延迟不敏感的大批量任务改走 Batch API
- **Context Caching（Gemini）**：付费缓存大型文档（Context Caching API），多次请求分摊

**3. 模型选择**
- 按任务选择最小可用模型：Haiku/Flash 处理简单任务，Sonnet/Pro 处理中等，Opus/Ultra 仅用于复杂任务
- Subagent 可指定更便宜的模型（`model: haiku`）
- 关闭或降低 Extended Thinking（thinking token 按 output 价格计费）

**4. 架构设计**
- Subagent 隔离：详细输出留在子 agent context，不污染主 context
- Hook 卸载：Pre/Post tool 处理（grep 过滤测试输出：10k tokens → 数百 tokens）
- 专用 Skills 替代探索性对话

## 跨厂商实现

**Claude**：
- Prompt Caching：`cache_control: {type: "ephemeral"}` 标记可缓存前缀；TTL 5 分钟（默认）或 1 小时（batch 场景）
- Message Batches API：50% 折扣
- Claude Code 企业基准：$13/开发者活跃日，$150–250/开发者/月；90% 用户低于 $30/活跃日
- Workspace 级 spend limit + 成本报告（Claude Console）

**OpenAI**：
- Batch API：50% 折扣（Chat Completions、Embeddings）
- 提示缓存（Prompt Caching）：自动对 ≥1024 token 的重复前缀生效，无需手动标记
- 按层级（Tier 1–5）不同模型有不同价格

**Gemini**：
- Context Caching API：付费缓存（按存储时间计费）+ 查询价格大幅折扣
- 按模型大小（Flash/Pro/Ultra）分级定价

## 关键参数 / API 表面

| 机制 | Claude | OpenAI | Gemini |
|---|---|---|---|
| Prompt Caching | 手动标记 `cache_control` | 自动（≥1024 token 前缀） | Context Caching API |
| Batch Discount | 50%，Batches API | 50%，Batch API | *待确认* |
| 成本监控 | `/usage`、Claude Console | Dashboard Usage | Cloud Console |

## 使用场景

**优先级排序（成本效益比）**：
1. 批处理（50% 折扣，零代码改动）
2. Prompt Caching（静态前缀长的系统最高收益）
3. 模型降级（Haiku 替代 Sonnet，价格差 5–10x）
4. Context 压缩（中等收益，需要工程投入）
5. 架构重构（最高收益，最高投入）

## 相关

- [[Prompt-caching]] — 最高 ROI 的成本优化工具 entity
- [[batch-processing-concept]] — 50% 折扣的批处理模式
- [[tokenization]] — token 是成本的计量单位
- [[rate-limiting]] — 成本和配额管理是同一套系统
- [[context-engineering]] — context 大小直接决定 token 消耗

## 出现来源

- [[prompt-caching--bwc]]
- [[batch-processing--bwc]]
