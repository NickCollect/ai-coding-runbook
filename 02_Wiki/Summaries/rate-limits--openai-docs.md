---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/rate-limits.md
source_url: https://platform.openai.com/docs/guides/rate-limits
title: "OpenAI — Rate Limits"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

## 核心要点

OpenAI API 速率限制的运作机制、用量层级、响应头读取及错误缓解策略。

### 限制维度

- **RPM**：每分钟请求数
- **RPD**：每日请求数
- **TPM**：每分钟 token 数（input + output）
- **TPD**：每日 token 数
- **IPM**：每分钟图片数（图像模型）

限制在 **组织级别** 和 **项目级别** 均有设置，以先触达者为准。

### 用量层级

消费满足门槛（美元 + 等待天数）后自动升级：

| 层级 | 最低消费 | 最低等待 |
|---|---|---|
| Tier 1 | $5（预充值） | — |
| Tier 2 | $50（已支付） | ≥7 天 |
| Tier 3 | $100 | ≥7 天 |
| Tier 4 | $250 | ≥14 天 |
| Tier 5 | $1000 | ≥30 天 |

可通过 Limits 页面申请提升限制（需业务用例说明）。

### 响应头

每次 API 响应包含：
- `x-ratelimit-limit-requests`
- `x-ratelimit-limit-tokens`
- `x-ratelimit-remaining-requests`
- `x-ratelimit-remaining-tokens`
- `x-ratelimit-reset-requests`
- `x-ratelimit-reset-tokens`

### 缓解策略

**指数退避（Exponential Backoff）**（推荐）：

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_backoff(**kwargs):
    return client.completions.create(**kwargs)
```

**Batch API**：异步处理大量请求（24h 内完成），限制独立于同步 API，最多 50% 折扣。

其他策略：降低 `max_tokens`；减少不必要请求；在代码中缓存常用结果。
