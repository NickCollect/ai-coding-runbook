---
type: qa
topic: quick-reference
created: 2026-05-05
sources:
  - 02_Wiki/Synthesis/context-window-pricing.md
  - 02_Wiki/Entities/Prompt-caching.md
  - 02_Wiki/Entities/Extended-thinking.md
  - 02_Wiki/Synthesis/mcp-integration-guide.md
  - 02_Wiki/Summaries/rate-limits--openai-docs.md
---

# Quick Reference Q&A

> 本文为 1-liner 速查。数字来自 wiki raw 文件，截至 2026-05-05。

---

## Q: Claude Sonnet 4.6 的 input price per million tokens？
**A:** **$3.00** per million input tokens.
*来源：[[context-window-pricing]]*

---

## Q: OpenAI GPT-5.4 的 context window？
**A:** **1,050,000 tokens**（约 1M）。
*来源：[[context-window-pricing]]*

---

## Q: Gemini 2.5 Flash 的 output price？
**A:** **$2.50** per million output tokens.
*来源：[[context-window-pricing]]*

---

## Q: Claude 的 max output tokens 默认是多少？
**A:** 待确认（数据截至 2026-05-05）。`max_tokens` 是 Claude Messages API 的**必填参数**，无默认值；未指定会报错。每个模型的最大可设置值在当前 wiki raw 文件中未明确记录。开发者通常设置 1024–32768，Claude Code 内部使用更高值。建议查阅 platform.claude.com 的 model comparison table 获取各模型上限。
*来源：[[Messages-API]]、[[context-windows--bwc]]*

---

## Q: MCP 推荐 transport 是？
**A:** 远程服务器：**Streamable HTTP**（`--transport http`）；本地工具/脚本：**stdio**（`--transport stdio`）。旧版 HTTP+SSE 已废弃，新项目不要用 `--transport sse`。
*来源：[[mcp-integration-guide]]*

---

## Q: Claude prompt caching 的 TTL 是多少？
**A:** 默认 **5 分钟**（cache write = 1.25× base）；可选 **1 小时**（`ttl: "1h"`，cache write = 2× base）。每次命中免费刷新 TTL。
*来源：[[Prompt-caching]]*

---

## Q: OpenAI batch API 的折扣是多少？
**A:** **50% off**（所有模型均享，异步处理，24 小时内完成）。
*来源：[[context-window-pricing]]、[[rate-limits--openai-docs]]*

---

## Q: Gemini Flash 2.5 每百万 token 输入价格？
**A:** **$0.30** per million input tokens.
*来源：[[context-window-pricing]]*

---

## Q: Claude 的 extended thinking 最大 thinking tokens？
**A:** 待确认（数据截至 2026-05-05）。**Opus 4.7** 仅支持 adaptive thinking，无 `budget_tokens` 参数（手动设置直接报 400）；thinking 预算由模型自动决定。**Opus 4.6 / Sonnet 4.6** 支持手动设置 `budget_tokens`，但最大值上限在当前 wiki raw 文件中未明确记录。建议查阅 platform.claude.com extended thinking 文档。
*来源：[[Extended-thinking]]*

---

## Q: OpenAI 的 rate limit 默认 tier 是多少 RPM？
**A:** 待确认（数据截至 2026-05-05）。Wiki 记录了 tier 升级门槛（Tier 1: $5 预充值；Tier 2: $50+7天；…Tier 5: $1000+30天），以及 RPM / RPD / TPM / TPD 等维度，但各 tier 的具体 RPM 数值在当前 wiki raw 文件中未记录。建议查阅 platform.openai.com/docs/guides/rate-limits 获取最新数值。
*来源：[[rate-limits--openai-docs]]*
