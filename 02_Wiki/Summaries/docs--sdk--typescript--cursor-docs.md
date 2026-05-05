---
type: summary
source: 01_Raw/docs.cursor.com/docs--sdk--typescript.md
source_url: https://cursor.com/docs/sdk/typescript
title: "Cursor TypeScript SDK"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

`@cursor/sdk` 是 Cursor 的 TypeScript SDK（公测版），允许从代码中调用与 IDE 相同的 Cursor Agent，支持本地、云端（Cursor 托管/自托管）三种运行时。

**安装**：`npm install @cursor/sdk`；认证：`CURSOR_API_KEY`（用户 API Key 或 Service Account API Key）。

**核心概念**：Agent（持有对话状态的持久容器）、Run（单次 prompt 提交，包含流、状态、结果、取消）、SDKMessage（跨运行时的标准化流事件）。

**基本用法**：
```typescript
const agent = await Agent.create({ apiKey, model: { id: "composer-2" }, local: { cwd: process.cwd() } });
const run = await agent.send("描述任务");
for await (const event of run.stream()) { /* 处理流事件 */ }
```

**运行时选择**：`local: { cwd }` 本地运行；`cloud: { repos: [{ url, startingRef }], autoCreatePR: true }` 云端运行。

**主要 API**：
- `Agent.create()`：创建 Agent
- `Agent.prompt()`：一次性 prompt 便捷方法
- `Agent.resume(agentId)`：恢复已有 Agent
- `agent.send()`：发送消息，返回 Run
- `run.stream()`：异步流式读取 SDKMessage
- `run.wait()`：等待完成，返回 RunResult
- `run.cancel()`：取消运行
- `Cursor.models.list()`：列出可用模型和参数

**流事件类型**：assistant（模型文本）、thinking（推理）、tool_call（工具调用）、status（生命周期）、task、request（需用户批准）。

**高级功能**：每次 send 可传入 MCP server、subagent 定义、per-run 模型覆盖、原始 delta 回调（`onDelta`/`onStep`）、图片输入。

**资源管理**：推荐 `await using` 自动释放。
