---
type: entity
name: Extended-thinking
aliases: [extended-thinking, thinking mode, interleaved thinking]
category: feature
status: ga
created: 2026-05-05
note: cross-product entity (referenced by P1 summaries; full enrichment in P2 with API docs)
---

## 一句话定义

Claude 输出 reasoning trace 的模式（Sonnet 4+ / Opus 4+）

## 关键属性

- Claude 输出可见 reasoning trace 的模式；Opus 4.7 / Opus 4.6 / Sonnet 4.6 支持 [[models]] [[model-config]]
- 默认在 Claude Code 中**开启**；`Option+T`（`chat:thinkingToggle`）切换 alwaysThinkingEnabled，`MAX_THINKING_TOKENS=0` 禁用 [[interactive-mode]] [[keybindings]] [[model-config]]
- Opus 4.7 **只支持 adaptive thinking** — 没有 `budget_tokens` 参数，sampling parameters 也被移除 [[models]] [[model-config]]
- Opus 4.6 / Sonnet 4.6 可用 `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` + `MAX_THINKING_TOKENS=N` 退回固定 budget 模式 [[model-config]] [[env-vars]]
- API 旧模型用 `thinking={"type": "enabled", "budget_tokens": N}`；新模型 `thinking={"type": "adaptive"}` [[streaming--python]]
- thinking 输出在 CLI 默认折叠，`Ctrl+O` 展开为灰色斜体；API 用户拿到 redacted blocks，需 `showThinkingSummaries: true` 才看到内容；**无论是否查看都计费** [[model-config]]
- prompt 中包含 `ultrathink` 关键字会请求一次性更深入推理，不改 session effort；其他短语（"think hard"）**不被识别** [[model-config]]
- effort（low/medium/high/xhigh/max）和 thinking budget 是**独立维度**：高 effort + 0 thinking = 多 token 但无 thinking [[effort]] [[model-config]]
- `DISABLE_INTERLEAVED_THINKING` 环境变量可关闭 interleaved thinking [[env-vars]]
- Agent SDK 中显式设置 `max_thinking_tokens` / `maxThinkingTokens` 会**禁用** `StreamEvent` 发出，只能拿到完整 message [[streaming-output]]
- Effort 参数（beta header `effort-2025-11-24`）控制 Claude 在 thinking + 文本 + tool call 上的 token 投入；migration 到 Opus 4.5 推荐 `effort: "high"` [[effort]]
- adaptive thinking 在 stream 中作为 `thinking_delta` 类型的 content_block_delta 单独处理 [[streaming--python]]
- **API 完整规则**（详见 [[Adaptive-thinking]] entity）：
  - Opus 4.7 manual `{type: "enabled", budget_tokens: N}` 直接 400；只能 `{type: "adaptive"}`
  - Mythos Preview adaptive 是默认；不支持 `{type: "disabled"}`
  - Opus 4.6 / Sonnet 4.6 manual 仍可用但 deprecated
  - Sonnet 3.7 / 更早模型必须 manual mode [[adaptive-thinking--bwc]] [[extended-thinking--bwc]]
- **Display 模式**：`summarized`（4.6 默认）vs `omitted`（4.7 / Mythos 默认；TTFT 更快，仅 signature） [[adaptive-thinking--bwc]]
- **Signature** opaque + encrypted；跨 Anthropic / Bedrock / Vertex 兼容；多 turn 必须 unchanged 传回；改动 → API error [[extended-thinking--bwc]]
- **Interleaved thinking**：tool calls 之间也思考；Mythos / Opus 4.7 上 inter-tool 推理总在 thinking blocks；Sonnet 4.6 manual 模式需 `interleaved-thinking-2025-05-14` beta header；adaptive 自动启用 [[extended-thinking--bwc]]
- **Pricing**：billed for full original thinking tokens（不是 summary）；summary 生成本身免费（不同模型生成） [[extended-thinking--bwc]]
- **Cache 交互**：thinking blocks 不进 cache prefix，但 stable system + tools 仍 hit；toggle thinking 仅作废 messages 层 [[Prompt-caching]] [[adaptive-thinking--bwc]]

## 出现来源

_26 summaries reference this entity_:

- [[agent-design]]
- [[agent-loop]]
- [[changelog--claude-code-repo]]
- [[claude-api--csharp]]
- [[claude-api-go]]
- [[claude-api-php]]
- [[claude-api-skill]]
- [[claude-opus-4-5-migration--skill]]
- [[costs]]
- [[effort]]
- [[env-vars]]
- [[error-codes]]
- [[errors]]
- [[google-vertex-ai]]
- [[interactive-mode]]
- [[keybindings]]
- [[managed-agents-core]]
- [[managed-agents-events]]
- [[model-config]]
- [[model-migration]]
- [[models]]
- [[prompt-snippets--opus-4-5-migration]]
- [[settings]]
- [[streaming--python]]
- [[streaming--typescript]]
- [[streaming-output]]

## 相关

- [[Context-window]] — thinking tokens 计入 context 与 output 配额
- [[Agentic-loop]] — agent loop 每个 turn 可能产生 thinking blocks
- [[Tool-use]] — interleaved thinking 让模型在 tool call 之间继续推理
- [[Agent-SDK]] — SDK 通过 `maxThinkingTokens` 选项控制
- [[Fast-mode]] — Fast mode 是 Opus 4.6 的低延迟变体，与 thinking 是独立维度
- [[Prompt-caching]] — thinking 输出不进 cache prefix，但前缀 stable 部分仍命中 cache
