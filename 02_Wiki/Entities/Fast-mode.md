---
type: entity
name: Fast-mode
aliases: [fast mode]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 用 Opus 4.6 的低延迟交互模式

## 关键属性

- 仅适用于 **Claude Opus 4.6**（不是新 model，是 4.6 的高速变体）；2.5x 更快、同等质量、更高成本；**Opus 4.7 不支持** [[fast-mode]]
- Research preview 状态，需 Claude Code v2.1.36+；价格/可用性可能变 [[fast-mode]]
- 价格：$30/$150 per MTok（input/output），整个 1M context 平价 [[fast-mode]]
- 切换：`/fast`（Tab 确认）或 `"fastMode": true` 写在 settings.json；prompt 旁有 `↯` 图标；启用时若当前 model 不是 Opus 4.6 会切到 4.6 [[fast-mode]]
- 键盘快捷键 `Option+O`（`chat:fastMode`） [[interactive-mode]] [[keybindings]]
- 关闭 fast mode 仍留在 Opus 4.6，需要 `/model` 才换回别的 model [[fast-mode]]
- **成本陷阱**：会话中途启用要按 fast-mode uncached 价格重算**整段对话上下文**；建议从 session 开始就启用 [[fast-mode]]
- 适用：rapid iteration、live debugging、紧迫的交互工作；**不适合**长 autonomous task / batch / CI / 成本敏感场景 [[fast-mode]]
- 与 effort level 正交：fast mode = 同质量 + 低延迟 + 高成本；低 effort = 少 thinking + 快但可能降质量 [[fast-mode]] [[effort]]
- **不可用**于 Bedrock / Vertex / Foundry，仅 Anthropic Console API + 订阅 plan（通过 extra usage） [[fast-mode]]
- 必须开启 extra usage 计费；token 直接计入 extra usage（即使套餐还有余额）；Team/Enterprise 默认禁用，admin 在 Console 启用 [[fast-mode]]
- Per-session opt-in：managed `fastModePerSessionOptIn: true` 让每个 session 默认关闭，用户手动 `/fast` 启用 [[fast-mode]]
- Rate limit 与标准 Opus 4.6 分开计；耗尽自动 fallback 到标准 Opus 4.6（`↯` 变灰），冷却结束自动恢复 [[fast-mode]]
- 全局禁用：`CLAUDE_CODE_DISABLE_FAST_MODE=1` [[fast-mode]] [[env-vars]]

## 出现来源

_5 summaries reference this entity_:

- [[commands]]
- [[env-vars]]
- [[fast-mode]]
- [[interactive-mode]]
- [[keybindings]]

## 相关

- [[Settings]] — `fastMode` / `fastModePerSessionOptIn` 在 settings.json 配置
- [[Enterprise-gateway]] — Bedrock / Vertex / Foundry 显式不支持 fast mode
- [[Extended-thinking]] — 与 fast mode 正交，可叠加用
- [[Permission-mode]] — fast mode 不影响 permission flow
- [[Native-interface]] — `/fast` 在 CLI 和 VS Code 扩展可用
