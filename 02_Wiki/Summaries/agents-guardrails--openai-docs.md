---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/agents/guardrails-approvals.md
source_url: https://platform.openai.com/docs/guides/agents/guardrails-approvals
title: "OpenAI — Agents SDK: Guardrails 与 Human Review"
summarized_at: 2026-05-05
entities_referenced: [Subagent]
concepts_referenced: [Agentic-loop]
---

## 核心要点

Agents SDK 提供三类 guardrail 控制 + human-in-the-loop 审批机制。

### 控制类型选择

| 场景 | 控制方式 |
|---|---|
| 主模型运行前拦截不合规请求 | Input guardrails |
| 输出离开系统前校验/脱敏 | Output guardrails |
| function tool 调用前后检查 | Tool guardrails |
| 高风险副作用（取消订单、shell 命令）前暂停 | Human-in-the-loop approvals |

### Input guardrail 示例

```python
@input_guardrail
async def math_guardrail(ctx, agent, input):
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )
```

### Human approval 生命周期

1. Run 记录 approval interruption，不执行 tool
2. Result 返回 `interruptions` + 可恢复的 `state`
3. 应用程序 approve 或 reject 待处理项
4. 从 `state` 恢复同一 run（**非**新用户 turn）

审批耗时较长时：序列化 `state` → 存储 → 之后恢复，保持同一 run。

### 作用域规则

- Input guardrails：仅对链中**第一个** agent 生效
- Output guardrails：仅对产生**最终输出**的 agent 生效
- Tool guardrails：绑定到具体 function tool

### Streaming + approvals

流式场景无单独审批系统。流式 run 暂停时：等待稳定 → 检查 `interruptions` → 处理审批 → 从同一 `state` 恢复。
