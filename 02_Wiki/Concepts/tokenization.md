---
name: Tokenization
type: concept
aliases: [Tokens, Token Count, Subword Tokenization, BPE, Byte Pair Encoding]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Tokenization（分词与 Token 化）

将原始文本分割成模型实际处理单元（token）的过程。Token 是 LLM 计算和计费的基本单位，而非字符或单词。

## 核心机制

现代 LLM 使用 **Byte Pair Encoding（BPE）** 或类似算法（SentencePiece、WordPiece）将文本分割为 subword 单元：

1. 从单字符/字节开始，统计语料中相邻对的频率
2. 反复合并最高频的相邻对，直到达到词表大小（通常 32k–200k token）
3. 最终词表包含常见单词（整词），以及罕见词的分段

**大致换算**（英文）：
- 1 token ≈ 4 个字符 ≈ 0.75 个单词
- 1000 tokens ≈ 750 个单词

中文/日文等 CJK 文字通常每字符消耗更多 token（约 1.5–2 token/字）。

**计费方式**：input tokens（输入）和 output tokens（输出）分开计费，output 通常更贵。

## 跨厂商实现

**Claude**：使用自定义 BPE tokenizer。提供 Token Counting API（`POST /v1/messages/count_tokens`）在请求前预估消耗，支持 tool definitions、images、system prompts 的精确计算。

**OpenAI**：使用 `tiktoken` 库；gpt-4o 系列使用 `o200k_base` 词表（200k tokens）；开源，开发者可本地运行。

**Gemini**：使用 SentencePiece；通过 `countTokens` API 获取精确数量，支持 multimodal 输入（图片/视频/音频按固定率换算）。

## 关键参数 / API 表面

| 端点/工具 | 说明 |
|---|---|
| `POST /v1/messages/count_tokens` (Claude) | 请求前预估 token 用量 |
| `tiktoken` (OpenAI) | 本地 token 计数库 |
| `countTokens` (Gemini) | API 端点，支持 multimodal |
| `max_tokens` | 限制输出 token 数上限 |
| `context_window` | 模型总 token 上限（input+output） |

## 使用场景

**Token 计数的重要性**：
- 成本预估：大批量处理前预算控制
- 避免超出 context window 被截断
- [[prompt-caching]] 效益计算（前缀越长，缓存收益越大）
- 检测 prompt injection（异常长的输入）

**注意事项**：
- 不同模型/厂商的同一段文本 token 数不同，不可跨厂商复用计数结果
- 代码和结构化数据（JSON、XML）通常比自然语言消耗更多 token
- 图片 token 数通常按像素/分辨率换算，与分辨率直接相关

## 相关

- [[Context-window]] — token 是 context window 的计量单位
- [[Token-counting]] — Claude 的 token 计数 API entity
- [[cost-optimization]] — token 消耗直接影响 API 成本
- [[batch-processing-concept]] — 批处理时的 token 预算规划

## 出现来源

- [[count_tokens--msg-api]]
- [[messages-count_tokens--beta-api]]
