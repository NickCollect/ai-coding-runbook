---
type: qa
topic: cost-optimization
created: 2026-05-05
sources:
  - 02_Wiki/Synthesis/prompt-caching-strategy.md
  - 02_Wiki/Synthesis/context-window-pricing.md
  - 02_Wiki/Comparison/context-caching-comparison.md
  - 02_Wiki/Entities/Prompt-caching.md
---

# Cost Optimization Q&A

## Q: 怎样最大化 Claude prompt caching 节省？
**A:** 核心策略：(1) **静态内容前置**：tools → system → 固定 few-shot 例子，动态 user query 放最后；(2) **避免 silent invalidator**：不在可缓存段里放 `datetime.now()`、`uuid4()`、session/user ID；(3) **高频请求用 5 分钟 TTL**（1.25× write，0.1× read，2 次命中即回本）；低频长任务用 1 小时 TTL（2× write，3 次命中回本）；(4) **多轮对话用 automatic mode**（顶层 `cache_control`，随对话自动前移）；(5) **agentic loop 中每 ~15 块加一个断点**避免超 20-block lookback 窗口。命中时成本降至 base input 的 10%（节省 90%）。
*来源：[[prompt-caching-strategy]]、[[Prompt-caching]]*

---

## Q: OpenAI 的 prompt caching 多少 token 起算？
**A:** **1,024 tokens**。OpenAI 完全自动，无需代码改动——API 自动检测重复 prefix 并路由到同一服务器。通过 `prompt_cache_retention` 可配置 24h 保留（gpt-5.x 系列默认），其他模型默认 5–10 分钟内存缓存。
*来源：[[prompt-caching-strategy]]、[[context-caching-comparison]]*

---

## Q: Gemini context caching 和 Claude prompt caching 哪个更省钱？
**A:** 取决于使用模式：**短 TTL + 高频请求** → Claude 更优（无存储费，命中 0.1× base，write 1.25× base；无额外基础设施）。**长文档反复查询（小时级，超大内容）** → Gemini explicit caching 更优（支持视频/PDF，付存储费换确定性命中，避免每次重传大文件）。**零改造** → OpenAI 最省事（完全自动，无 write 费用，最高 90% 节省）。三者 cache read 折扣均为约 90%，关键差异在写入成本和 TTL 灵活性。
*来源：[[context-caching-comparison]]、[[prompt-caching-strategy]]*

---

## Q: 用 Batch API 能节省多少？
**A:** 三家厂商 Batch API 均提供 **50% 折扣**：Claude Message Batches API（异步，24h 内完成）、OpenAI Batch API（异步，24h 内）、Gemini Batch API（50% 折扣，raw 文件确认："riduzione del costo del 50%"）。Batch 折扣与 prompt caching 折扣**叠加计算**（Claude: 50% batch × 10% cache read = 有效 5% base input price）。
*来源：[[context-window-pricing]]、[[prompt-caching-strategy]]*

---

## Q: 哪些内容适合放进 cache？
**A:** 适合：静态 system prompt（不变）、tool definitions（不常变）、大型 RAG 文档或书籍内容、20+ 条 few-shot 示例、多轮对话的稳定前缀（system + early messages）、Gemini 场景下的视频和 PDF 文件（explicit caching）。**不适合**：含时间戳或 `datetime.now()` 的段落、per-user ID 或 session ID、每次请求不同的参数（`tool_choice` 变化会使 messages 缓存失效）、随机 UUID。
*来源：[[Prompt-caching]]、[[prompt-caching-strategy]]*

---

## Q: Claude 的 input/output token 定价比是多少？
**A:** 所有 Claude 当前主力模型均为 **1:5**（input:output）：Opus 4.7/4.6 = $5:$25；Sonnet 4.6/4.5 = $3:$15；Haiku 4.5 = $1:$5。对应缓存命中价（0.1× base input）：Opus $0.50，Sonnet $0.30，Haiku $0.10 per MTok。
*来源：[[Prompt-caching]]、[[context-window-pricing]]*

---

## Q: 长对话如何控制 token 消耗？
**A:** Anthropic 推荐组合策略：(1) **Compaction**（推荐）：server-side 摘要，beta 支持 Opus 4.7/4.6 / Sonnet 4.6；(2) **Context editing**：清除工具结果、thinking blocks（API 自动剥离上一轮 thinking，不需手动）；(3) **Prompt caching**：缓存稳定前缀，减少重复传输成本；(4) **Context-aware models**（Sonnet 4.6 / Haiku 4.5）：模型主动跟踪剩余 token 预算，可在接近上限时主动收紧；(5) 使用 **Token Counting API** 提前估算并决定是否 compact。
*来源：[[context-window-pricing]]、[[context-windows--bwc]]*

---

## Q: 哪个 vendor 的免费 tier 最慷慨？
**A:** 待确认（数据截至 2026-05-05）。当前 wiki raw 文件未完整覆盖各厂商免费 tier 的 token 额度和限制细节。Gemini 的 `pricing.md` 中有免费层提及但具体额度未在 wiki 中提取。Claude 和 OpenAI 主要为付费按量计费模式（OpenAI Tier 1 需 $5 预充值起步）。建议直接查阅各厂商官方 pricing 页面获取最新免费额度。
*来源：[[context-window-pricing]]、[[rate-limits--openai-docs]]*
