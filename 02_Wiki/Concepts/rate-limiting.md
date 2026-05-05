---
name: Rate Limiting
type: concept
aliases: [Rate Limits, RPM, TPM, API Throttling, Usage Tiers]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Rate Limiting（速率限制）

API 提供商对单位时间内请求数量或 token 消耗量设定上限的机制，用于保护服务稳定性、防止滥用，同时根据账户消费等级动态调整配额。

## 核心机制

速率限制通常在多个维度同时执行，任一维度触达上限均会触发限流（返回 HTTP 429）：

| 维度 | 说明 |
|---|---|
| **RPM** | 每分钟请求数（Requests Per Minute） |
| **TPM** | 每分钟 token 数（Tokens Per Minute，input+output） |
| **RPD** | 每日请求数（Requests Per Day） |
| **TPD** | 每日 token 数（Tokens Per Day） |
| **IPM** | 每分钟图片数（图像模型专用） |

**计量方式**：通常在请求开始时扣减预估用量（基于 `max_tokens`），实际生成结束后再校正；这意味着保守的 `max_tokens` 设置会提前触发 TPM 限制。

**响应头追踪**（OpenAI 格式，各厂商类似）：
```
x-ratelimit-limit-requests: 3000
x-ratelimit-remaining-requests: 2998
x-ratelimit-reset-requests: 2s
x-ratelimit-limit-tokens: 60000
x-ratelimit-remaining-tokens: 55000
x-ratelimit-reset-tokens: 5s
```

## 跨厂商实现

**Claude**：
- 限制在 Workspace 级别设置；Admin API 的 Rate Limits API 可编程获取当前配额（需 `sk-ant-admin...` key）
- 多模型归入 `model_group` 统一计算；其他类别：`batch`、`token_count`、`files`、`skills`、`web_search`
- Workspace 可设置覆盖 org 级别；Default workspace 无覆盖（查 org 级）

**OpenAI**：
- 5 个消费层级（Tier 1–5），满足消费金额 + 等待天数后自动升级
- 限制同时在组织级别和项目级别施加，取先达者
- 批处理 API（Batch API）配额独立，且在速率耗尽时是处理大量请求的替代方案

**Gemini**：
- 通过 Google Cloud Console 或 AI Studio 查看配额
- *待确认* 具体层级结构

## 关键参数 / API 表面

| 工具/参数 | 说明 |
|---|---|
| `x-ratelimit-*` 响应头 | 实时剩余配额查询 |
| Rate Limits API (Claude) | 编程获取 org/workspace 级别配额 |
| 指数退避 | 429 后等待 2^n 秒再重试的标准策略 |
| `max_tokens` 优化 | 设置合理上限，避免占用过多 TPM 配额 |

**推荐重试策略（指数退避）**：
```python
from tenacity import retry, stop_after_attempt, wait_random_exponential

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def call_api(**kwargs):
    return client.messages.create(**kwargs)
```

## 使用场景

**开发者必知**：
- 大批量处理改用 Batch API（50% 价格，独立配额，不占 RPM/TPM）
- 多用户应用需在应用层实现 per-user 限流，避免单一大用户耗尽 org 配额
- 延迟敏感的流程监控 `x-ratelimit-remaining-*` 头，提前降速

**OpenAI 升级路径**：消费达到门槛后在 Dashboard → Limits 页提交业务说明申请升级。

## 相关

- [[Rate-limit-API]] — Claude Rate Limits API entity 档案
- [[batch-processing-concept]] — 速率受限时的高吞吐替代方案
- [[cost-optimization]] — 合理控制 max_tokens 既节成本又节配额
- [[Batches-API]] — Claude 批处理 API entity

## 出现来源

- [[rate-limits--openai-docs]]
- [[rate-limits--gemini-docs]]
- [[rate-limits-api--bwc]]
