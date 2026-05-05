---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/latency-optimization.md
source_url: https://platform.openai.com/docs/guides/latency-optimization
title: "OpenAI — 延迟优化"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API, Batches-API, Prompt-caching]
concepts_referenced: [Context-window]
---

## 核心要点

降低 LLM 应用延迟的七个核心原则，以及在真实客服场景中的应用示例。

### 七个核心原则

1. **更快处理 token** — 选用更小/更快的模型；使用 Predicted Outputs（当大部分输出可预知时）
2. **生成更少 token** — 要求简短/直接响应；避免不必要的 chain-of-thought；输出压缩结构（JSON 代替 prose）
3. **使用更少 input token** — 通过 fine-tuning 替代 few-shot 示例；过滤无关 context；利用 prompt caching（长 prompt 收益明显）
4. **减少请求数量** — 将多步骤合并为单请求；扩展模型原生能力以减少 orchestration calls
5. **并行化** — 并行执行独立任务；在等待 LLM 调用时执行其他操作
6. **降低用户感知等待** — 流式传输（streaming），一有 token 就输出；先完成快的任务；先显示加载提示
7. **不要默认使用 LLM** — 检索精确数据用数据库；确定性操作不用 LLM；路由决策可用分类模型代替

### 实践示例：客服场景 token 压缩

对用户 query 做分析，以紧凑 JSON 表达而非 prose，减少 output token 同时保留所有信息：

```json
{
  "cont": "True",
  "n_msg": "1",
  "tone_in": "Aggravated",
  "type": "Hardware Issue",
  "tone_out": "Validating and solution-oriented",
  "reqs": "Propose options for repair or replacement.",
  "human": "False"
}
```

### 可量化收益

- 切换到 predicted outputs：适用于大量已知输出场景（如代码格式化），可显著减少 TTFT（Time to First Token）
- Prompt caching：重复前缀命中缓存，latency 和 cost 同时降低
