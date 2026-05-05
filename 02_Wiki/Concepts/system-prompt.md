---
name: System Prompt
type: concept
aliases: [System Instructions, System Message, Developer Message, Operator Instructions]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# System Prompt（系统提示词）

在用户对话开始前由应用开发者（operator）注入的持久性指令，用于定义模型的角色、行为边界、回答风格和任务范围。系统提示词具有比用户消息更高的优先级。

## 核心机制

系统提示词在权限层次中处于"应用开发者"（operator）层，介于 LLM 提供商（Anthropic/OpenAI/Google）的训练层和终端用户层之间：

```
LLM 提供商（训练层，最高优先级）
  └── Operator（system prompt，高优先级）
        └── User（对话消息，低优先级）
```

**主要用途**：
- 角色/人格设定（"你是一个专业的医疗助手"）
- 行为约束（"只回答与产品相关的问题"、"始终用中文回答"）
- 上下文注入（用户档案、应用状态、今日日期）
- 格式规范（"始终以 JSON 格式输出"）
- 工具使用指引（描述可用工具的用途和调用规则）

**持久性**：系统提示词在整个对话会话中持续有效，无需在每轮用户消息中重复。但在长对话中，若上下文过长发生压缩，系统提示词可能被摘要化（注意！）。

## 跨厂商实现

**Claude**：
- `system` 参数（string 或含 `cache_control` 的 content array）
- Operator 层可拓宽 Anthropic 默认限制（如成人内容平台）或收窄（限制主题）
- Claude Code Agent SDK：默认 minimal system prompt；可选 `preset: "claude_code"` 完整预设；支持 `append` 模式在默认 system 后追加，或完全替换
- `excludeDynamicSections: true`：将动态内容（cwd、git status）移出 system prompt，改放第一条 user message，以支持跨会话 prompt caching

**OpenAI**：
- 现称 `developer` 角色（取代 `system`，语义上是"应用开发者定义的指令"）
- 优先级：`developer` > `user`；`developer` 消息可出现在对话历史中（不一定只在开头）
- GPT-5 建议：对话风格（自然语言指令）优于格式化指令清单

**Gemini**：
- `systemInstruction` 字段（`GenerateContentRequest` 中的顶层参数）
- 支持多 part 系统指令；可在 AI Studio 中预设和测试

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `system` (Claude) | String 或含 `cache_control` 的 array |
| `developer` role (OpenAI) | 高优先级持久性指令角色 |
| `systemInstruction` (Gemini) | 顶层系统指令字段 |
| `cache_control: {type: "ephemeral"}` | 标记 system prompt 可被 prompt cache 命中 |

## 使用场景

**必须精心设计的 system prompt**：
- 角色扮演/品牌人格（避免模型 OOC）
- 安全约束（限制主题、禁止敏感输出）
- 持久的输出格式要求
- 领域知识注入（规则、术语、约束）

**注意事项**：
- System prompt 不是秘密——通过 prompt injection 或 jailbreak 可能被泄露；敏感信息不应放在 system prompt 中
- 过长的 system prompt 消耗大量 token；用 [[Prompt-caching]] 缓存静态部分
- 动态内容（时间、用户 ID）应放在消息中，保持 system prompt 可缓存

## 相关

- [[prompt-engineering]] — system prompt 是 prompt 工程的核心输入点
- [[safety-and-guardrails]] — safety 规则通过 system prompt 注入
- [[Prompt-caching]] — 缓存静态 system prompt 节约成本
- [[context-engineering]] — system prompt 是 context 管理的一部分

## 出现来源

- [[modifying-system-prompts]]
- [[agent-creation-system-prompt]]
- [[prompt-engineering--openai-docs]]
- [[prompting-strategies--gemini-docs]]
