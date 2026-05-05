---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/sessions.md
source_url: https://code.claude.com/docs/en/agent-sdk/sessions
title: "Claude Agent SDK — Sessions（会话管理）"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Agentic-loop.md
  - Context-window.md
---

Session 是 SDK 在 agent 工作期间累积的完整对话历史，包括 prompt、每次工具调用、工具返回结果和每次响应。SDK 自动写入磁盘，支持后续恢复。

> Sessions 持久化**对话历史**，不持久化文件系统。要快照和回滚 agent 对文件的修改，请使用 file checkpointing。

## 选择合适的策略

| 使用场景 | 推荐方法 |
|---------|---------|
| 单次任务，无需跟进 | 无需额外处理，一次 `query()` 即可 |
| 单进程内多轮对话 | Python: `ClaudeSDKClient`；TypeScript: `continue: true` |
| 进程重启后继续 | `continue_conversation=True`（Python）/ `continue: true`（TypeScript），自动找最近 session |
| 恢复特定历史 session | 捕获 session ID 后传给 `resume` |
| 从某点分叉探索不同方向 | `fork_session=True`（Python）/ `forkSession: true`（TypeScript）|
| 无状态任务不写磁盘（仅 TypeScript）| `persistSession: false` |

## 自动 Session 管理

### Python：`ClaudeSDKClient`

内部自动跟踪 session ID，每次 `client.query()` 自动延续同一 session，无需手动传 ID：

```python
async with ClaudeSDKClient(options=options) as client:
    await client.query("Analyze the auth module")
    async for message in client.receive_response():
        # 处理消息
        pass
    await client.query("Now refactor it to use JWT")  # 自动携带完整上下文
    async for message in client.receive_response():
        pass
```

### TypeScript：`continue: true`

在后续 `query()` 调用中传入 `continue: true`，SDK 自动找到当前目录最近 session：

```typescript
// 第一次查询：创建新 session
for await (const message of query({ prompt: "Analyze the auth module", options: {...} })) { ... }

// 第二次查询：自动延续
for await (const message of query({
  prompt: "Now refactor it to use JWT",
  options: { continue: true, allowedTools: [...] }
})) { ... }
```

## 手动 Session 管理

### 捕获 Session ID

从 `ResultMessage` 的 `session_id` 字段读取（Python/TypeScript 均适用）：

```python
async for message in query(prompt="...", options=...):
    if isinstance(message, ResultMessage):
        session_id = message.session_id
```

### Resume by ID

将 session ID 传给 `resume` 选项，agent 以完整上下文继续工作：

```python
async for message in query(
    prompt="Now implement the refactoring you suggested",
    options=ClaudeAgentOptions(resume=session_id, allowed_tools=[...]),
):
    ...
```

> 提示：若 resume 返回新 session 而非预期历史，最可能原因是 `cwd` 不匹配。Sessions 按 `~/.claude/projects/<encoded-cwd>/*.jsonl` 存储。

### Fork（分叉探索）

`fork_session=True` 创建一个以原 session 历史为起点的新 session，原 session 不受影响。两个 session 均可独立 resume：

```python
# 从 session_id 分叉，探索 OAuth2 路径
forked_id = None
async for message in query(
    prompt="Instead of JWT, implement OAuth2",
    options=ClaudeAgentOptions(resume=session_id, fork_session=True),
):
    if isinstance(message, ResultMessage):
        forked_id = message.session_id  # 分叉的独立 ID

# 原 session 保持不变，继续 JWT 方向
async for message in query("Continue with the JWT approach", options=ClaudeAgentOptions(resume=session_id)):
    ...
```

## 跨主机 Resume

Session 文件仅在创建它的机器上存在。跨主机（CI worker、容器、serverless）恢复有两种方案：

1. **迁移文件**：将 `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` 拷贝到新主机相同路径（`cwd` 必须一致）
2. **不依赖 resume**：将分析结果、决策、文件 diff 作为应用状态保存，作为新 session 的 prompt 传入（更健壮）

## Session 工具函数

两个 SDK 均提供：
- `listSessions()` / `list_sessions()`：枚举磁盘上的 sessions
- `getSessionMessages()` / `get_session_messages()`：读取 session 消息
- `getSessionInfo()` / `get_session_info()`：查询 session 元信息
- `renameSession()` / `rename_session()`：重命名 session
- `tagSession()` / `tag_session()`：为 session 添加标签
